#!/usr/bin/env python3
"""Small, offline CPU timestamp experiment for pinned multilingual Whisper models and v1.9.5.

This deliberately reports unverified word grouping/quality rather than claiming
that its provisional English/German whitespace grouping is a production parser.
Supply only licensed public audio if the output directory will be uploaded.
Build both helpers from the pin; apply the adjacent patch only to --patched.
All model/audio paths must already exist. No downloads or application imports.
"""

from __future__ import annotations

import argparse
import difflib
import hashlib
import json
import math
import platform
import random
import re
import statistics
import struct
import subprocess
import time
import wave
from pathlib import Path

PIN = "d1be6fde11ac6e0407606b4e42fe72d34add8037"
MODELS = {
    "tiny": {
        "sha256": "be07e048e1e599ad46341c8d2a135645097a538221678b7acdd1b1919c6e1b21",
        "dtw": "tiny",
        "timeout_s": 120,
    },
    "large-v3-turbo": {
        "sha256": "1fc70f774d38eb169993ac391eea357ef47c88757ef72ee5943879b7e8e2bc69",
        "dtw": "large.v3.turbo",
        "timeout_s": 900,
    },
}
VAD_SHA256 = "29940d98d42b91fbd05ce489f3ecf7c72f0a42f027e4875919a28fb4c04ea2cf"
SHIFT_TOLERANCE_MS = 50


def digest(path: Path) -> str:
    with path.open("rb") as stream:
        return hashlib.file_digest(stream, "sha256").hexdigest()


def read_audio(path: Path) -> bytes:
    with wave.open(str(path), "rb") as audio:
        if (audio.getnchannels(), audio.getsampwidth(), audio.getframerate()) != (
            1,
            2,
            16000,
        ):
            raise ValueError(f"Expected PCM16 mono 16 kHz: {path}")
        if audio.getcomptype() != "NONE":
            raise ValueError(f"Expected uncompressed WAV: {path}")
        return audio.readframes(audio.getnframes())


def write_audio(path: Path, data: bytes) -> None:
    with wave.open(str(path), "wb") as audio:
        audio.setnchannels(1)
        audio.setsampwidth(2)
        audio.setframerate(16000)
        audio.writeframes(data)


def normalized(text: str) -> str:
    return re.sub(r"[^\w]", "", text.lower())


def intervals(result: dict, duration_ms: float) -> dict:
    """Inspect ordinary intervals; do not reinterpret t_dtw as a word boundary."""
    groups = []
    text_parts = []
    problems = []
    raw_dtw = []
    for segment_index, segment in enumerate(result.get("transcription", [])):
        segment_text = segment.get("text", "")
        text_parts.append(segment_text)
        token_text = ""
        group = None
        for token in segment.get("tokens", []):
            # Both pinned multilingual models use EOT 50257.
            if token["id"] >= 50257:
                continue
            text = token["text"]
            token_text += text
            offsets = token.get("offsets")
            if not offsets:
                problems.append(f"segment {segment_index}: missing timing for {text!r}")
                continue
            start, end = offsets["from"], offsets["to"]
            if not all(isinstance(t, (int, float)) and math.isfinite(t) for t in (start, end)):
                problems.append(f"nonfinite timing for {text!r}")
                continue
            if not 0 <= start <= end <= duration_ms:
                problems.append(f"out-of-bounds timing for {text!r}: {start}, {end}")
            if text[:1].isspace() or group is None:
                if group is not None:
                    groups.append(group)
                group = {"text": text, "start_ms": start, "end_ms": end, "pieces": [text]}
            else:
                group["text"] += text
                group["end_ms"] = end
                group["pieces"].append(text)
            raw_dtw.append({"text": text, "point_cs": token.get("t_dtw")})
        if group is not None:
            groups.append(group)
        if segment_text != token_text:
            problems.append(f"segment {segment_index}: token text does not reproduce segment text")
    previous_end = 0
    for group in groups:
        if group["start_ms"] < previous_end:
            problems.append(f"overlapping word interval: {group['text']!r}")
        if group["end_ms"] <= group["start_ms"]:
            problems.append(f"nonpositive word interval: {group['text']!r}")
        previous_end = group["end_ms"]
    if any(part.strip() for part in text_parts) and not groups:
        problems.append("recognized text has no timed words")
    return {
        "text": "".join(text_parts),
        "words": groups,
        "problems": problems,
        "dtw_points": raw_dtw,
    }


def shift_check(reference: list[dict], candidate: list[dict], shift_ms: int) -> dict:
    ref_keys = [normalized(word["text"]) for word in reference]
    hyp_keys = [normalized(word["text"]) for word in candidate]
    matcher = difflib.SequenceMatcher(a=ref_keys, b=hyp_keys, autojunk=False)
    errors = []
    matched = 0
    for block in matcher.get_matching_blocks():
        for index in range(block.size):
            first = reference[block.a + index]
            second = candidate[block.b + index]
            errors.extend(
                abs(second[key] - first[key] - shift_ms) for key in ("start_ms", "end_ms")
            )
            matched += 1
    unmatched_ref = len(reference) - matched
    unmatched_hyp = len(candidate) - matched
    return {
        "tolerance_ms": SHIFT_TOLERANCE_MS,
        "matched_words": matched,
        "unmatched_reference_words": unmatched_ref,
        "unmatched_candidate_words": unmatched_hyp,
        "boundary_errors_ms": errors,
        "max_boundary_error_ms": max(errors, default=None),
        "median_boundary_error_ms": statistics.median(errors) if errors else None,
        "status": "passed"
        if errors and max(errors) <= SHIFT_TOLERANCE_MS and not unmatched_ref and not unmatched_hyp
        else "failed",
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--upstream", type=Path, required=True)
    parser.add_argument("--patched", type=Path, required=True)
    parser.add_argument("--model", type=Path, required=True)
    parser.add_argument("--model-preset", choices=MODELS, default="tiny")
    parser.add_argument(
        "--timeout-seconds", type=int, help="Per inference; default tiny=120, turbo=900"
    )
    parser.add_argument("--vad-model", type=Path, required=True)
    parser.add_argument(
        "--speech", type=Path, required=True, help="Public English PCM16 mono 16 kHz WAV"
    )
    parser.add_argument("--german", type=Path)
    parser.add_argument("--japanese", type=Path)
    parser.add_argument("--output-dir", type=Path, required=True)
    args = parser.parse_args()
    model = MODELS[args.model_preset]
    timeout_s = args.timeout_seconds if args.timeout_seconds is not None else model["timeout_s"]
    if timeout_s <= 0:
        parser.error("--timeout-seconds must be positive")
    for path, expected in ((args.model, model["sha256"]), (args.vad_model, VAD_SHA256)):
        if digest(path) != expected:
            raise ValueError(f"Pinned model checksum mismatch: {path}")
    out = args.output_dir.resolve()
    out.mkdir(parents=True, exist_ok=False)
    audio_dir = out / "audio"
    audio_dir.mkdir()
    speech = read_audio(args.speech)
    silence = b"\0" * 16000 * 2
    rng = random.Random(42)  # noqa: S311 - deterministic synthetic audio, no security use
    noise = struct.pack("<128000h", *(rng.randint(-1500, 1500) for _ in range(128000)))
    data = {
        "base": (speech, "en"),
        "leading": (silence * 5 + speech, "en"),
        "trailing": (speech + silence * 5, "en"),
        "internal": (speech + silence * 5 + speech, "en"),
        "boundary": (silence * 25 + speech, "en"),
        "silence": (silence * 8, "en"),
        "noise": (noise, "en"),
    }
    for name, path, language in (("german", args.german, "de"), ("japanese", args.japanese, "ja")):
        if path:
            data[name] = (read_audio(path), language)
    fixtures = {}
    for name, (samples, language) in data.items():
        path = audio_dir / f"{name}.wav"
        write_audio(path, samples)
        fixtures[name] = {
            "path": str(path),
            "sha256": digest(path),
            "samples": len(samples) // 2,
            "duration_ms": len(samples) / 2 / 16,
            "language": language,
        }
    report = {
        "source_commit": PIN,
        "host": platform.platform(),
        "machine": platform.machine(),
        "model_preset": args.model_preset,
        "dtw_preset": model["dtw"],
        "timeout_s": timeout_s,
        "model_sha256": digest(args.model),
        "vad_sha256": digest(args.vad_model),
        "helper_hashes": {
            name: digest(path)
            for name, path in (("upstream", args.upstream), ("patched", args.patched))
        },
        "shift_tolerance_ms": SHIFT_TOLERANCE_MS,
        "grouping": "provisional whitespace EN/DE only; JA segmentation unverified",
        "fixtures": fixtures,
        "runs": {},
        "unverified": [
            "human reference text/boundaries; quality gates",
            "non-space-delimited-language lexical grouping",
            "word crossing 30-second boundary (audio boundary stress only)",
            "rapid speaker turns; long interviews",
            "Metal/macOS; network externally blocked; process lifecycle",
        ],
    }
    configurations = (
        ("upstream-ordinary-no-vad", args.upstream, False, False),
        ("upstream-ordinary-vad", args.upstream, True, False),
        ("patched-ordinary-vad", args.patched, True, False),
        ("upstream-dtw-vad", args.upstream, True, True),
        ("patched-dtw-vad", args.patched, True, True),
    )
    for config, helper, vad, dtw in configurations:
        results = {}
        for name, fixture in fixtures.items():
            prefix = out / f"{config}-{name}"
            command = [
                str(helper.resolve()),
                "-m",
                str(args.model.resolve()),
                "-f",
                fixture["path"],
                "-l",
                fixture["language"],
                "-t",
                "4",
                "-bs",
                "5",
                "-tp",
                "0",
                "-nf",
                "-ng",
                "-nfa",
                "-ojf",
                "-of",
                str(prefix),
            ]
            if vad:
                command += ["--vad", "-vm", str(args.vad_model.resolve())]
            if dtw:
                command += ["--dtw", model["dtw"]]
            started = time.monotonic()
            execution_status = "completed"
            try:
                with (
                    prefix.with_suffix(".stdout").open("wb") as stdout,
                    prefix.with_suffix(".log").open("wb") as stderr,
                ):
                    process = subprocess.run(
                        command, stdout=stdout, stderr=stderr, timeout=timeout_s, check=False
                    )
                elapsed = time.monotonic() - started
                parsed = (
                    json.loads(prefix.with_suffix(".json").read_text())
                    if process.returncode == 0
                    else {}
                )
                inspection = intervals(parsed, fixture["duration_ms"])
                if process.returncode:
                    execution_status = "helper_error"
                    inspection["problems"].append(f"helper exit {process.returncode}")
            except (subprocess.TimeoutExpired, ValueError, KeyError, OSError, TypeError) as exc:
                elapsed = time.monotonic() - started
                execution_status = (
                    "timeout" if isinstance(exc, subprocess.TimeoutExpired) else "output_error"
                )
                inspection = {"text": "", "words": [], "problems": [str(exc)], "dtw_points": []}
            if name in {"silence", "noise"} and inspection["words"]:
                inspection["problems"].append(f"recognized words on {name}-only fixture")
            if (
                execution_status == "completed"
                and name not in {"silence", "noise"}
                and not inspection["words"]
            ):
                inspection["problems"].append("speech fixture returned no timed words")
            inspection.update(command=command, wall_s=elapsed, execution_status=execution_status)
            inspection["status"] = (
                "error"
                if execution_status != "completed"
                else "failed"
                if inspection["problems"]
                else "passed"
            )
            results[name] = inspection
            print(f"{config}/{name}: {inspection['status']}", flush=True)
        base = results["base"]["words"]
        shifts = {
            "leading": shift_check(base, results["leading"]["words"], 5000),
            "trailing": shift_check(base, results["trailing"]["words"], 0),
            "boundary": shift_check(base, results["boundary"]["words"], 25000),
        }
        split_ms = fixtures["base"]["duration_ms"] + 5000
        internal = results["internal"]["words"]
        shifts["internal-first"] = shift_check(
            base, [word for word in internal if word["start_ms"] < split_ms], 0
        )
        shifts["internal-second"] = shift_check(
            base, [word for word in internal if word["start_ms"] >= split_ms], int(split_ms)
        )
        for name in shifts:
            case = "internal" if name.startswith("internal-") else name
            if any(results[key]["execution_status"] != "completed" for key in ("base", case)):
                shifts[name] = {
                    "status": "unverified",
                    "reason": "paired helper execution incomplete",
                }
        report["runs"][config] = {"fixtures": results, "shift_checks": shifts}
    candidate = report["runs"]["patched-ordinary-vad"]
    candidate_statuses = {
        item["status"]
        for item in [*candidate["fixtures"].values(), *candidate["shift_checks"].values()]
    }
    report["ordinary_candidate_structural_status"] = (
        "failed"
        if "failed" in candidate_statuses
        else "unverified"
        if candidate_statuses != {"passed"}
        else "passed"
    )
    report["production_correctness_gate"] = "blocked"
    (out / "report.json").write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n")
    print(
        f"Candidate structural gate: {report['ordinary_candidate_structural_status']}; full production gate blocked; report: {out / 'report.json'}"
    )
    return 0 if report["ordinary_candidate_structural_status"] == "passed" else 1


if __name__ == "__main__":
    raise SystemExit(main())
