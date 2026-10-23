#!/usr/bin/env python3
"""Download/hash pinned public experiment assets before offline inference."""

import argparse
import hashlib
import json
import shutil
import subprocess
from pathlib import Path
from urllib.request import urlopen

from feasibility import MODEL_FILES, MODEL_REPO, MODEL_REVISION, shared

SOURCE_REVISION = "d1be6fde11ac6e0407606b4e42fe72d34add8037"
SPEECH_SHA256 = "20d3323a2bcce6f25498b8911a397503a0a99fa92b6ba58d62788cb42b6e5459"


def download(url, path, expected):
    if not url.startswith("https://"):
        raise ValueError("only pinned HTTPS downloads are permitted")
    with urlopen(url, timeout=120) as source, path.open("wb") as destination:  # noqa: S310
        shutil.copyfileobj(source, destination)
    if shared.digest(path) != expected:
        raise ValueError(f"download checksum mismatch: {path.name}")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--work-dir", type=Path, required=True)
    parser.add_argument("--output-dir", type=Path, required=True)
    args = parser.parse_args()
    work, out = args.work_dir.resolve(), args.output_dir.resolve()
    if work == out or out in work.parents:
        parser.error("download directory must be outside uploaded reports")
    model = work / "model"
    model.mkdir(parents=True, exist_ok=False)
    out.mkdir(parents=True, exist_ok=True)
    for filename, (size, expected) in MODEL_FILES.items():
        path = model / filename
        download(
            f"https://huggingface.co/{MODEL_REPO}/resolve/{MODEL_REVISION}/{filename}",
            path,
            expected,
        )
        if path.stat().st_size != size:
            raise ValueError(f"model size mismatch: {filename}")
    mp3, wav = work / "jfk.mp3", work / "jfk.wav"
    url = (
        f"https://raw.githubusercontent.com/ggml-org/whisper.cpp/{SOURCE_REVISION}/samples/jfk.mp3"
    )
    download(url, mp3, SPEECH_SHA256)
    subprocess.run(
        [
            shutil.which("ffmpeg") or "/opt/homebrew/bin/ffmpeg",
            "-hide_banner",
            "-loglevel",
            "error",
            "-i",
            str(mp3),
            "-ar",
            "16000",
            "-ac",
            "1",
            "-c:a",
            "pcm_s16le",
            str(wav),
        ],
        check=True,
        timeout=60,
    )
    samples = shared.read_audio(wav)
    if len(samples) != 352000:
        raise ValueError("expected the same 176000-sample / 11-second source excerpt")
    (out / "asset-provenance.json").write_text(
        json.dumps(
            {
                "model_repo": MODEL_REPO,
                "model_revision": MODEL_REVISION,
                "model_files": MODEL_FILES,
                "model_license_note": "upstream OpenAI model MIT; converted card omits license; production provenance unverified",
                "speech_url": url,
                "speech_mp3_sha256": SPEECH_SHA256,
                "speech_pcm_sha256": hashlib.sha256(samples).hexdigest(),
                "speech_samples": len(samples) // 2,
                "matches_prior_cpu_pcm": hashlib.sha256(samples).hexdigest()
                == "d7c87c75282610a7e9432708b91e1c9367253de2fc08890f91eeb74387b1da60",
                "speech_recording": "White House Army Signal Agency; JFK Inaugural Address, 20 January 1961; JFKWHA-001",
                "speech_rights": "Public Domain per JFK Library recording catalog",
                "speech_rights_source": "https://www.jfklibrary.org/asset-viewer/archives/jfkwha-001",
                "speech_crop_note": "same pinned whisper.cpp excerpt as earlier CPU experiment; exact archive crop offsets unverified",
            },
            indent=2,
        )
        + "\n"
    )


if __name__ == "__main__":
    main()
