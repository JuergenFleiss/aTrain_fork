"""Real-browser transcription run: upload, speaker detection on, Start, wait.

Opt-in with ATRAIN_E2E_TRANSCRIBE=1, since it needs a real transcription model
(the preselected one, `large-v3-turbo` when present) and `speaker-detection`
in the server's model dir. Prints when each
task starts, so a slow step shows in the log (#307: 12 minutes for 12 s of
audio on macOS).
"""

import os
import re
import time
from pathlib import Path

import pytest
from playwright.sync_api import Page, expect

AUDIO = Path(__file__).parents[1] / "fixtures" / "sample_short.mp3"
TIMEOUT_S = int(os.environ.get("ATRAIN_E2E_TRANSCRIBE_TIMEOUT", "1500"))

pytestmark = pytest.mark.skipif(
    not os.environ.get("ATRAIN_E2E_TRANSCRIBE"),
    reason="needs real models; set ATRAIN_E2E_TRANSCRIBE=1",
)


def test_transcription_with_speaker_detection_finishes(atrain_server: str, page: Page) -> None:
    page.goto(atrain_server)
    model = page.locator(".q-select").nth(0)
    expect(model).to_be_visible(timeout=120_000)  # splash imports torch first
    assert "No models yet" not in model.inner_text()
    print(f"model: {model.inner_text().splitlines()[0]}", flush=True)
    page.get_by_text("Speaker Detection").last.click()
    expect(page.get_by_text("Number of Speakers")).to_be_visible()
    page.locator("input[type=file]").set_input_files(AUDIO)
    expect(page.get_by_text("1 File Added")).to_be_visible()

    start = time.monotonic()
    page.get_by_role("button", name="Start").click()
    expect(page.get_by_text("We are working on it!")).to_be_visible(timeout=60_000)

    finished = page.get_by_text("We finished the transcription!")
    error = page.get_by_text("The following error occured")
    last_task = None
    while time.monotonic() - start < TIMEOUT_S:
        if finished.is_visible() or error.is_visible():
            break
        dialog = page.locator(".q-dialog").last
        text = " ".join(dialog.inner_text().split()) if dialog.count() else ""
        match = re.search(r"Task \S+: .*?(?= Running on|$)", text)
        task = match.group(0) if match else None
        if task and task != last_task:
            print(f"{time.monotonic() - start:7.1f} s  {task}", flush=True)
            last_task = task
        page.wait_for_timeout(2000)

    elapsed = time.monotonic() - start
    print(f"{elapsed:7.1f} s  end", flush=True)
    if error.is_visible():
        pytest.fail(
            f"Transcription failed after {elapsed:.0f} s:\n{page.locator('.q-dialog').last.inner_text()}"
        )
    assert finished.is_visible(), f"Not finished after {TIMEOUT_S} s (last: {last_task})"
