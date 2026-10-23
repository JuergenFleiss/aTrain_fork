#!/usr/bin/env python3
"""Generate deterministic silence/noise timeline fixtures using only stdlib.

Pass a source recording already converted to mono, 16 kHz, signed 16-bit PCM
WAV and its independently computed SHA-256. The source remains untouched.
"""

from __future__ import annotations

import argparse
import hashlib
import struct
import wave
from pathlib import Path

RATE = 16_000
SAMPLE_WIDTH = 2
SEED = 20261023


def _read_source(path: Path, expected_sha256: str) -> bytes:
    digest = hashlib.sha256(path.read_bytes()).hexdigest()
    if digest.lower() != expected_sha256.lower():
        raise ValueError(f"source SHA-256 mismatch: expected {expected_sha256}, got {digest}")
    with wave.open(str(path), "rb") as source:
        params = source.getparams()
        if (params.nchannels, params.sampwidth, params.framerate, params.comptype) != (
            1,
            SAMPLE_WIDTH,
            RATE,
            "NONE",
        ):
            raise ValueError("source WAV must be uncompressed mono 16 kHz signed 16-bit PCM")
        frames = source.readframes(params.nframes)
    if not frames:
        raise ValueError("source WAV has no samples")
    return frames


def _write(path: Path, pcm: bytes) -> str:
    path.parent.mkdir(parents=True, exist_ok=True)
    with wave.open(str(path), "wb") as output:
        output.setnchannels(1)
        output.setsampwidth(SAMPLE_WIDTH)
        output.setframerate(RATE)
        output.writeframes(pcm)
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _silence(seconds: float) -> bytes:
    return bytes(round(seconds * RATE) * SAMPLE_WIDTH)


def _noise(seconds: float) -> bytes:
    # xorshift32 gives a tiny, version-independent deterministic white-noise
    # signal. Its peak amplitude is approximately 2% of full scale.
    state = SEED
    output = bytearray()
    for _ in range(round(seconds * RATE)):
        state ^= (state << 13) & 0xFFFFFFFF
        state ^= state >> 17
        state ^= (state << 5) & 0xFFFFFFFF
        state &= 0xFFFFFFFF
        sample = ((state & 0xFFFF) - 32768) // 50
        output.extend(struct.pack("<h", sample))
    return bytes(output)


def generate(output_dir: Path, speech_wav: Path | None, speech_sha256: str | None) -> None:
    outputs: dict[str, bytes] = {
        "silence_8s.wav": _silence(8),
        "noise_1s.wav": _silence(0.5) + _noise(1) + _silence(6.5),
    }
    if speech_wav is not None:
        assert speech_sha256 is not None
        speech = _read_source(speech_wav, speech_sha256)
        mid = (len(speech) // SAMPLE_WIDTH // 2) * SAMPLE_WIDTH
        lead = _silence(0.5)
        pad_to_30 = _silence(29.5)
        outputs.update(
            {
                "speech_leading_trailing_500ms.wav": lead + speech + _silence(0.5),
                "speech_internal_gap_3s.wav": speech[:mid] + _silence(3) + speech[mid:],
                # Speech audio spans 30s; a human must inspect whether a lexical
                # word itself crosses the boundary before claiming that case.
                "speech_at_30s_boundary.wav": pad_to_30 + speech,
            }
        )
    for name, pcm in outputs.items():
        digest = _write(output_dir / name, pcm)
        duration = len(pcm) / (RATE * SAMPLE_WIDTH)
        print(f"{name}\t{duration:.6f}s\t{digest}")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("output_dir", type=Path)
    parser.add_argument(
        "--speech-wav", type=Path, help="pinned speech source converted to mono 16 kHz PCM WAV"
    )
    parser.add_argument("--speech-sha256", help="required SHA-256 of the converted source WAV")
    args = parser.parse_args()
    if bool(args.speech_wav) != bool(args.speech_sha256):
        parser.error("--speech-wav and --speech-sha256 must be supplied together")
    generate(args.output_dir, args.speech_wav, args.speech_sha256)


if __name__ == "__main__":
    main()
