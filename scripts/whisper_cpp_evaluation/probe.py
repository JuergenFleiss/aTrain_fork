"""Bounded macOS runner experiment; no application imports or dependencies."""

import argparse
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
import time
from pathlib import Path
from urllib.request import urlopen

SOURCE_REVISION = "d1be6fde11ac6e0407606b4e42fe72d34add8037"
MODEL_REVISION = "5359861c739e955e79d9a303bcbc70fb988958b1"
MODEL_SHA256 = "be07e048e1e599ad46341c8d2a135645097a538221678b7acdd1b1919c6e1b21"
MODEL_URL = f"https://huggingface.co/ggerganov/whisper.cpp/resolve/{MODEL_REVISION}/ggml-tiny.bin"


def sha256(path):
    with path.open("rb") as stream:
        return hashlib.file_digest(stream, "sha256").hexdigest()


def run(argv, log, timeout=120, env=None):
    """Keep complete diagnostics in files, including nonzero exits/timeouts."""
    started = time.monotonic()
    with log.open("w") as stream:
        stream.write(json.dumps({"argv": [str(value) for value in argv]}) + "\n")
        stream.flush()
        try:
            completed = subprocess.run(
                argv,
                stdout=stream,
                stderr=subprocess.STDOUT,
                timeout=timeout,
                env=env,
                check=False,
            )
            code = completed.returncode
        except (OSError, subprocess.TimeoutExpired) as error:
            stream.write(f"\n{error}\n")
            code = -1
    return {"exit_code": code, "wall_seconds": time.monotonic() - started}


def classify_inference(result, log, output, metal=False):
    """A successful CPU fallback cannot satisfy the Metal execution check."""
    if result["exit_code"] != 0:
        return "failed"
    try:
        segments = json.loads(output.read_text())["transcription"]
        if not isinstance(segments, list) or not all(
            isinstance(segment, dict) and isinstance(segment.get("text"), str)
            for segment in segments
        ):
            return "failed"
        if not any(segment["text"].strip() for segment in segments):
            return "failed"
    except (OSError, ValueError, KeyError, TypeError):
        return "failed"
    if metal:
        text = log.read_text()
        # Pinned-source initialization AND actual Metal operation encoding.
        # WHISPER_DEBUG is required to retain GGML_LOG_DEBUG node messages.
        initialized = "ggml_metal_init: picking default device:" in text
        executed = re.search(
            r"^ggml_metal_op_encode_impl: node\[\s*\d+\] -\s+"
            r"(?:MUL_MAT|ADD|MUL|SCALE|UNARY)\b(?![^\n]*\(noop\))",
            text,
            re.MULTILINE,
        )
        failed = re.search(r"no GPU found|failed to initialize|error:", text, re.I)
        if not initialized or not executed or failed:
            return "failed"
    return "passed"


def probe_metal(report, cache, metadata):
    swift = Path(__file__).with_name("metal_probe.swift")
    executable = cache.resolve() / "metal-probe"
    compiled = run(
        ["xcrun", "swiftc", swift, "-framework", "Metal", "-o", executable],
        report / "metal-compile.log",
    )
    metadata["metal_compile"] = compiled
    if compiled["exit_code"] != 0:
        return "failed"
    probe = run([executable], report / "metal-compute.log", timeout=60)
    metadata["metal_compute"] = probe
    try:
        # run() prepends argv as one JSON line; retain the probe JSON verbatim.
        data = json.loads((report / "metal-compute.log").read_text().split("\n", 1)[1])
        if probe["exit_code"] == 77 and data["status"] == "unavailable" and not data["devices"]:
            return "unavailable"
        if probe["exit_code"] == 0 and data["status"] == "passed":
            return "passed"
    except (ValueError, KeyError, IndexError, TypeError) as error:
        metadata["metal_error"] = str(error)
    return "failed"


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", type=Path, required=True)
    parser.add_argument("--helper", type=Path, required=True)
    parser.add_argument("--report", type=Path, required=True)
    parser.add_argument("--cache", type=Path, required=True)
    args = parser.parse_args()
    report = args.report.resolve()
    report.mkdir(parents=True, exist_ok=True)
    args.cache.mkdir(parents=True, exist_ok=True)
    source = args.source.resolve()
    helper = args.helper.resolve()
    statuses = {"cpu": "failed", "metal": "failed", "metal_compute": "failed"}
    metadata = {
        "source_revision": SOURCE_REVISION,
        "model_url": MODEL_URL,
        "model_sha256": MODEL_SHA256,
        "runner_label": "macos-15",
        "image_os": os.environ.get("ImageOS"),  # noqa: SIM112 - runner-defined name
        "image_version": os.environ.get("ImageVersion"),  # noqa: SIM112
        "runner_arch": os.environ.get("RUNNER_ARCH"),
        "run_url": (
            f"{os.environ.get('GITHUB_SERVER_URL')}/{os.environ.get('GITHUB_REPOSITORY')}"
            f"/actions/runs/{os.environ.get('GITHUB_RUN_ID')}"
        ),
        "diagnostic_build": "Release; WHISPER_DEBUG; Metal embedded; Core ML OFF; target macOS 14",
    }
    try:
        for name, argv in {
            "os": ["sw_vers"],
            "architecture": ["uname", "-a"],
            "cpu_memory": [
                "sysctl",
                "hw.model",
                "hw.machine",
                "hw.ncpu",
                "hw.memsize",
                "machdep.cpu.brand_string",
            ],
            "xcode": ["xcodebuild", "-version"],
            "sdk": ["xcrun", "--show-sdk-version"],
            "compiler": ["clang", "--version"],
            "display": ["system_profiler", "SPDisplaysDataType", "-json"],
        }.items():
            metadata[name] = run(argv, report / f"{name}.log", timeout=60)

        statuses["metal_compute"] = probe_metal(report, args.cache, metadata)
        if statuses["metal_compute"] == "unavailable":
            statuses["metal"] = "unavailable"

        revision = subprocess.check_output(
            ["/usr/bin/git", "-C", source, "rev-parse", "HEAD"], text=True
        ).strip()
        if revision != SOURCE_REVISION:
            raise ValueError(f"unexpected source revision: {revision}")
        # Fixed synthetic public text; no private recordings or fixture uploads.
        fixture_text = (
            "The quick brown fox jumps over the lazy dog. This is a local transcription test."
        )
        intermediate = args.cache.resolve() / "speech.aiff"
        fixture = args.cache.resolve() / "speech.wav"
        metadata["voices"] = run(["/usr/bin/say", "-v", "?"], report / "voices.log")
        generated = run(
            ["/usr/bin/say", "-v", "Samantha", "-r", "170", "-o", intermediate, fixture_text],
            report / "fixture-generate.log",
        )
        converted = run(
            [
                "/usr/bin/afconvert",
                "-f",
                "WAVE",
                "-d",
                "LEI16@16000",
                "-c",
                "1",
                intermediate,
                fixture,
            ],
            report / "fixture-convert.log",
        )
        if generated["exit_code"] != 0 or converted["exit_code"] != 0:
            raise ValueError("synthetic speech fixture generation failed")
        metadata["fixture"] = {
            "text": fixture_text,
            "voice": "Samantha",
            "words_per_minute": 170,
            "format": "16000 Hz mono PCM16 WAV",
            "sha256": sha256(fixture),
            "purpose": "capability smoke only; generated voice may vary with runner image",
        }
        shutil.copyfile(source / "LICENSE", report / "whisper-cpp-LICENSE")
        metadata["helper_sha256"] = sha256(helper)
        model = args.cache.resolve() / "ggml-tiny.bin"
        # No helper-owned download, moving Hub revision, or application cache.
        with urlopen(MODEL_URL, timeout=120) as response, model.open("wb") as destination:
            shutil.copyfileobj(response, destination)
        if sha256(model) != MODEL_SHA256:
            raise ValueError("tiny model SHA256 mismatch")
        common = [
            helper,
            "--model",
            model,
            "--file",
            fixture,
            "--language",
            "en",
            "--beam-size",
            "5",
            "--temperature",
            "0",
            "--no-fallback",
            "--no-flash-attn",
            "--output-json-full",
            "--threads",
            "3",
        ]
        for device in ("cpu", "metal"):
            if device == "metal" and statuses["metal_compute"] != "passed":
                continue
            log = report / f"{device}.log"
            output = report / device
            flags = ["--no-gpu"] if device == "cpu" else ["--device", "0"]
            env = dict(os.environ, GGML_METAL_GRAPH_DEBUG="1")
            result = run(common + flags + ["--output-file", output], log, timeout=180, env=env)
            metadata[device] = result
            statuses[device] = classify_inference(
                result, log, output.with_suffix(".json"), metal=device == "metal"
            )
    except (OSError, ValueError, KeyError, subprocess.SubprocessError) as error:
        metadata["error"] = str(error)
    finally:
        metadata["statuses"] = statuses
        (report / "result.json").write_text(json.dumps(metadata, indent=2) + "\n")
        summary = "\n".join(f"- {key}: **{value}**" for key, value in statuses.items())
        summary += "\n\nMetal unavailable does not satisfy the acceleration gate.\n"
        (report / "summary.md").write_text(summary)
        if os.environ.get("GITHUB_STEP_SUMMARY"):
            with open(os.environ["GITHUB_STEP_SUMMARY"], "a") as stream:
                stream.write(summary)
        print(summary)
    return int(statuses["cpu"] != "passed" or statuses["metal"] == "failed")


if __name__ == "__main__":
    sys.exit(main())
