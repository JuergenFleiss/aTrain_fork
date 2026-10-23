#!/usr/bin/env python3
"""Isolated MLX GPU timestamp experiment; no application imports or downloads.

Run on native arm64 macOS using the adjacent locked uv project. Audio/model/cache
files belong in --work-dir; only JSON/logs belong in --output-dir. The exploratory
50 ms shift gate is not a human word-boundary accuracy reference.
"""

from __future__ import annotations

import argparse
import errno
import importlib.metadata
import importlib.util
import json
import math
import os
import platform
import random
import re
import socket
import statistics
import struct
import subprocess
import sys
import time
import traceback
from pathlib import Path

SHARED_PATH = Path(__file__).parents[1] / "whisper_cpp_evaluation" / "feasibility.py"
SHARED_SPEC = importlib.util.spec_from_file_location("whisper_cpp_scoring", SHARED_PATH)
shared = importlib.util.module_from_spec(SHARED_SPEC)
SHARED_SPEC.loader.exec_module(shared)

MODEL_REPO = "mlx-community/whisper-large-v3-turbo"
MODEL_REVISION = "a4aaeec0636e6fef84abdcbe3544cb2bf7e9f6fb"
MODEL_FILES = {
    "config.json": (268, "b34fc29e4e11e0a25e812775dd67f4dd16fc2c8eb43d28ae25ff7d660ecb6379"),
    "weights.safetensors": (
        1613977612,
        "951ed3fc1203e6a62467abb2144a96ce7eafca8fa77e3704fdb8635ff3e7f8a6",
    ),
}
NETWORK_POLICY = "(version 1) (allow default) (deny network*)"
PACKAGES = {"mlx-whisper": "0.4.3", "mlx": "0.32.4", "mlx-metal": "0.32.4"}


def compact(text):
    return re.sub(r"\s+", "", text)


def intervals(result: dict, duration_ms: float) -> dict:
    """Validate native word intervals and complete text; never repair or drop text."""
    words, problems, texts = [], [], []
    for index, segment in enumerate(result["segments"]):
        text = segment["text"]
        texts.append(text)
        native = segment.get("words", [])
        if compact("".join(word["word"] for word in native)) != compact(text):
            problems.append(f"segment {index}: word text coverage mismatch")
        for word in native:
            start, end = word.get("start"), word.get("end")
            if not all(
                type(value) in (int, float) and math.isfinite(value) for value in (start, end)
            ):
                problems.append(f"nonfinite or missing word interval: {word['word']!r}")
                continue
            words.append({"text": word["word"], "start_ms": start * 1000, "end_ms": end * 1000})
            if not 0 <= start * 1000 <= end * 1000 <= duration_ms:
                problems.append(f"out-of-bounds interval: {word['word']!r}")
    if compact("".join(texts)) != compact(result["text"]):
        problems.append("segment text coverage does not reproduce full text")
    previous_end = 0
    for word in words:
        if word["start_ms"] < previous_end:
            problems.append(f"overlapping word interval: {word['text']!r}")
        if word["end_ms"] <= word["start_ms"]:
            problems.append(f"nonpositive word interval: {word['text']!r}")
        previous_end = word["end_ms"]
    if compact(result["text"]) and not words:
        problems.append("recognized text has no timed words")
    return {"text": result["text"], "words": words, "problems": problems}


def shift_check(reference, candidate, shift_ms):
    """Retain the fixed 50 ms gate, rounding only sub-nanosecond float noise."""
    check = shared.shift_check(reference, candidate, shift_ms)
    errors = [round(error, 6) for error in check["boundary_errors_ms"]]
    check.update(
        boundary_errors_ms=errors,
        max_boundary_error_ms=max(errors, default=None),
        median_boundary_error_ms=statistics.median(errors) if errors else None,
    )
    check["status"] = (
        "passed"
        if errors
        and max(errors) <= shared.SHIFT_TOLERANCE_MS
        and not check["unmatched_reference_words"]
        and not check["unmatched_candidate_words"]
        else "failed"
    )
    return check


def sequence_check(base, repeated, split_ms):
    """Diagnose copy identity by order only after exact full-sequence equality."""
    expected = [shared.normalized(word["text"]) for word in base] * 2
    actual = [shared.normalized(word["text"]) for word in repeated]
    if not base or actual != expected:
        return {
            "status": "unverified",
            "reason": "complete repeated sequence differs from base twice",
        }
    first = shift_check(base, repeated[: len(base)], 0)
    second = shift_check(base, repeated[len(base) :], split_ms)
    return {
        "status": "passed" if first["status"] == second["status"] == "passed" else "failed",
        "first": first,
        "second": second,
        "exact_complete_repeated_sequence": True,
    }


def paired_checks(results, base_duration_ms):
    base = results["base"]["words"]
    split_ms = base_duration_ms + 5000
    internal = results["internal"]["words"]
    checks = {
        name: shift_check(base, results[name]["words"], shift)
        for name, shift in (("leading", 5000), ("trailing", 0), ("boundary", 25000))
    }
    checks["internal-first"] = shift_check(
        base, [word for word in internal if word["start_ms"] < split_ms], 0
    )
    checks["internal-second"] = shift_check(
        base, [word for word in internal if word["start_ms"] >= split_ms], split_ms
    )
    checks["internal-sequence"] = sequence_check(base, internal, split_ms)
    for name in checks:
        case = "internal" if name.startswith("internal-") else name
        if any(results[key]["execution_status"] != "completed" for key in ("base", case)):
            checks[name] = {"status": "unverified", "reason": "paired inference incomplete"}
    return checks


def write_json(path, data):
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False, allow_nan=False) + "\n")


def worker(args):
    """This process must be launched under sandbox-exec, including capability mode."""
    metadata = {"status": "error", "phase": "network isolation"}
    try:
        with socket.socket() as connection:
            try:
                connection.connect(("127.0.0.1", 9))
            except OSError as error:
                metadata["network_connect_errno"] = error.errno
                if error.errno not in {errno.EPERM, errno.EACCES}:
                    raise RuntimeError("network deny policy not established") from error
            else:
                raise RuntimeError("sandbox unexpectedly permitted network connection")
        metadata["phase"] = "MLX GPU capability"
        import mlx.core as mx
        import numpy as np

        metadata["packages"] = {name: importlib.metadata.version(name) for name in PACKAGES}
        if metadata["packages"] != PACKAGES:
            raise RuntimeError("unexpected MLX package versions")
        if platform.system() != "Darwin" or platform.machine() != "arm64":
            raise RuntimeError("requires native arm64 macOS; no CPU fallback")
        if not mx.metal.is_available():
            raise RuntimeError("Metal unavailable; no CPU fallback")
        mx.set_default_device(mx.gpu)
        if mx.default_device() != mx.gpu:
            raise RuntimeError("GPU default device could not be selected")
        metadata["default_device"] = str(mx.default_device())
        metadata["metal_device_info"] = mx.metal.device_info()
        product = mx.ones((64, 64), dtype=mx.float16) @ mx.ones((64, 64), dtype=mx.float16)
        convolution = mx.conv1d(mx.ones((1, 16, 4)), mx.ones((8, 3, 4)))
        mx.eval(product, convolution)
        mx.synchronize()
        if product[0, 0].item() != 64 or convolution.sum().item() != 1344:
            raise RuntimeError("GPU arithmetic verification failed")
        metadata["gpu_matmul_conv"] = "passed"
        if not args.capability_only:
            metadata["phase"] = "ASR inference with GPU default; CPU DTW alignment"
            import mlx_whisper

            audio = np.frombuffer(shared.read_audio(args.speech), dtype="<i2").astype(np.float32)
            audio /= 32768
            mx.reset_peak_memory()
            started = time.monotonic()
            result = mlx_whisper.transcribe(
                audio,
                path_or_hf_repo=str(args.model_dir.resolve()),
                word_timestamps=True,
                language="en",
                temperature=0.0,
                fp16=True,
                verbose=None,
                condition_on_previous_text=True,
                no_speech_threshold=0.6,
                logprob_threshold=-1.0,
                compression_ratio_threshold=2.4,
                hallucination_silence_threshold=None,
            )
            mx.synchronize()
            metadata["inference_wall_s"] = time.monotonic() - started
            metadata["gpu_peak_memory_bytes"] = mx.get_peak_memory()
            if metadata["gpu_peak_memory_bytes"] <= 0 or mx.default_device() != mx.gpu:
                raise RuntimeError("GPU inference evidence missing")
            metadata["result"] = result
        metadata["status"] = "passed"
    except Exception as error:
        metadata["error"] = f"{type(error).__name__}: {error}"
        traceback.print_exc()
    write_json(args.worker_output, metadata)
    return 0 if metadata["status"] == "passed" else 2


def child(args, name, speech=None):
    output = args.output_dir / f"{name}.json"
    command = [
        "/usr/bin/sandbox-exec",
        "-p",
        NETWORK_POLICY,
        sys.executable,
        str(Path(__file__).resolve()),
        "--worker-output",
        str(output),
    ]
    if speech is None:
        command += ["--capability-only"]
    else:
        command += ["--speech", str(speech), "--model-dir", str(args.model_dir.resolve())]
    started = time.monotonic()
    execution_status = "completed"
    try:
        with (args.output_dir / f"{name}.log").open("w") as log:
            completed = subprocess.run(
                command,
                stdout=log,
                stderr=subprocess.STDOUT,
                timeout=args.timeout_seconds,
                check=False,
            )
        data = json.loads(output.read_text()) if output.exists() else {}
        if completed.returncode or data.get("status") != "passed":
            execution_status = "inference_error"
    except (subprocess.TimeoutExpired, OSError, ValueError) as error:
        data = {"error": str(error)}
        execution_status = (
            "timeout" if isinstance(error, subprocess.TimeoutExpired) else "output_error"
        )
    return {
        "execution_status": execution_status,
        "process_wall_s": time.monotonic() - started,
        "command": command,
        "worker": data,
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--model-dir", type=Path)
    parser.add_argument("--speech", type=Path)
    parser.add_argument("--work-dir", type=Path)
    parser.add_argument("--output-dir", type=Path)
    parser.add_argument("--timeout-seconds", type=int, default=240)
    parser.add_argument("--capability-only", action="store_true")
    parser.add_argument("--worker-output", type=Path, help=argparse.SUPPRESS)
    args = parser.parse_args()
    if args.worker_output:
        return worker(args)
    if not args.output_dir or not args.work_dir or args.timeout_seconds <= 0:
        parser.error("--output-dir/--work-dir and a positive timeout are required")
    args.output_dir = args.output_dir.resolve()
    args.work_dir = args.work_dir.resolve()
    if args.work_dir == args.output_dir or args.output_dir in args.work_dir.parents:
        parser.error("work/audio/models must be outside the uploaded output directory")
    args.output_dir.mkdir(parents=True, exist_ok=True)
    args.work_dir.mkdir(parents=True, exist_ok=True)
    if args.capability_only:
        capability = child(args, "capability")
        write_json(args.output_dir / "capability-report.json", capability)
        return 0 if capability["execution_status"] == "completed" else 2
    if not args.model_dir or not args.speech:
        parser.error("--model-dir and --speech are required for inference")
    for filename, (size, sha256) in MODEL_FILES.items():
        path = args.model_dir / filename
        if path.stat().st_size != size or shared.digest(path) != sha256:
            raise ValueError(f"pinned model mismatch: {filename}")
    speech = shared.read_audio(args.speech)
    silence = b"\0" * 32000
    rng = random.Random(42)  # noqa: S311 - deterministic synthetic audio
    noise = struct.pack("<128000h", *(rng.randint(-1500, 1500) for _ in range(128000)))
    fixtures = {
        "base": speech,
        "leading": silence * 5 + speech,
        "trailing": speech + silence * 5,
        "internal": speech + silence * 5 + speech,
        "boundary": silence * 25 + speech,
        "silence": silence * 8,
        "noise": noise,
    }
    report = {
        "model": {"repo": MODEL_REPO, "revision": MODEL_REVISION, "files": MODEL_FILES},
        "host": platform.platform(),
        "machine": platform.machine(),
        "runner_image": os.environ.get("ImageVersion"),  # noqa: SIM112 - runner-defined name
        "run_url": f"https://github.com/{os.environ.get('GITHUB_REPOSITORY')}/actions/runs/{os.environ.get('GITHUB_RUN_ID')}",
        "decoding": "greedy temperature=0, no fallback; beam search unavailable (prior baseline beam=5)",
        "vad": "unavailable; no VAD or silence compression applied",
        "alignment": "native word_timestamps=True; cross-attention/CPU DTW; original audio seconds",
        "shift_tolerance_ms": shared.SHIFT_TOLERANCE_MS,
        "boundary_error_rounding_ms": 0.000001,
        "network": NETWORK_POLICY,
        "production_correctness_gate": "blocked",
        "unverified": [
            "human boundaries/WER",
            "long interviews/multilingual",
            "macOS 14 execution",
            "production packaging/model-conversion provenance",
            "repeat performance comparison",
        ],
        "fixtures": {},
    }
    for name, samples in fixtures.items():
        audio = args.work_dir / f"{name}.wav"
        shared.write_audio(audio, samples)
        run = child(args, name, audio)
        try:
            inspection = (
                intervals(run["worker"]["result"], len(samples) / 32)
                if run["execution_status"] == "completed"
                else {
                    "text": "",
                    "words": [],
                    "problems": ["inference incomplete; not a timestamp failure"],
                }
            )
        except (KeyError, TypeError, ValueError) as error:
            run["execution_status"] = "output_error"
            inspection = {"text": "", "words": [], "problems": [str(error)]}
        if run["execution_status"] == "completed":
            if name in {"silence", "noise"} and inspection["text"].strip():
                inspection["problems"].append(f"recognized text on {name}-only fixture")
            if name not in {"silence", "noise"} and not inspection["words"]:
                inspection["problems"].append("speech returned no timed words")
        inspection.update(run)
        inspection.update(
            sha256=shared.digest(audio), samples=len(samples) // 2, duration_ms=len(samples) / 32
        )
        inspection["status"] = (
            "unverified"
            if run["execution_status"] != "completed"
            else "failed"
            if inspection["problems"]
            else "passed"
        )
        report["fixtures"][name] = inspection
        write_json(args.output_dir / "report.json", report)
        print(f"{name}: {inspection['status']}", flush=True)
        if name == "base" and run["execution_status"] != "completed":
            report["candidate_structural_status"] = "unverified"
            report["reason"] = "base ASR execution failed; remaining timing cases not run"
            write_json(args.output_dir / "report.json", report)
            return 2
    checks = paired_checks(report["fixtures"], len(speech) / 32)
    report["shift_checks"] = checks
    statuses = {item["status"] for item in [*report["fixtures"].values(), *checks.values()]}
    report["candidate_structural_status"] = (
        "failed" if "failed" in statuses else "passed" if statuses == {"passed"} else "unverified"
    )
    write_json(args.output_dir / "report.json", report)
    return 0 if report["candidate_structural_status"] == "passed" else 1


if __name__ == "__main__":
    raise SystemExit(main())
