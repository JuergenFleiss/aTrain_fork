"""Harness argument and error checks; mocks are not alignment evidence."""

import importlib.util
import json
import subprocess
import sys
from pathlib import Path
from types import SimpleNamespace

import pytest

SCRIPT = Path(__file__).parents[2] / "scripts" / "whisper_cpp_evaluation" / "feasibility.py"
SPEC = importlib.util.spec_from_file_location("whisper_cpp_feasibility", SCRIPT)
feasibility = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(feasibility)


def run_harness(tmp_path, monkeypatch, model_name, timeout_leading=False):
    model = tmp_path / "model.bin"
    model.write_bytes(model_name.encode())
    vad = tmp_path / "vad.bin"
    vad.write_bytes(b"vad")
    speech = tmp_path / "speech.wav"
    feasibility.write_audio(speech, b"\0" * 32000)
    helpers = [tmp_path / "upstream", tmp_path / "patched"]
    for helper in helpers:
        helper.write_bytes(b"fake boundary")
    selected = dict(feasibility.MODELS[model_name], sha256=feasibility.digest(model))
    monkeypatch.setitem(feasibility.MODELS, model_name, selected)
    monkeypatch.setattr(feasibility, "VAD_SHA256", feasibility.digest(vad))
    output = tmp_path / "results"
    arguments = [
        str(SCRIPT),
        "--upstream",
        str(helpers[0]),
        "--patched",
        str(helpers[1]),
        "--model",
        str(model),
        "--vad-model",
        str(vad),
        "--speech",
        str(speech),
        "--output-dir",
        str(output),
    ]
    if model_name != "tiny":
        arguments += ["--model-preset", model_name]
    monkeypatch.setattr(sys, "argv", arguments)
    calls = []

    def fake_run(command, **kwargs):
        calls.append((command, kwargs["timeout"]))
        prefix = Path(command[command.index("-of") + 1])
        if timeout_leading and prefix.name == "patched-ordinary-vad-leading":
            raise subprocess.TimeoutExpired(command, kwargs["timeout"])
        segments = []
        if not prefix.name.endswith(("-silence", "-noise")):
            segments = [
                {
                    "text": " word",
                    "tokens": [
                        {"id": 1, "text": " word", "offsets": {"from": 100, "to": 200}, "t_dtw": -1}
                    ],
                }
            ]
        prefix.with_suffix(".json").write_text(json.dumps({"transcription": segments}))
        return SimpleNamespace(returncode=0)

    monkeypatch.setattr(feasibility.platform, "platform", lambda: "test host")
    monkeypatch.setattr(feasibility.subprocess, "run", fake_run)
    feasibility.main()
    return calls, json.loads((output / "report.json").read_text()), model


@pytest.mark.parametrize(
    "model_name,dtw_preset,timeout_s",
    [("tiny", "tiny", 120), ("large-v3-turbo", "large.v3.turbo", 900)],
)
def test_selected_model_reaches_helper_argv(
    tmp_path, monkeypatch, model_name, dtw_preset, timeout_s
):
    calls, report, model = run_harness(tmp_path, monkeypatch, model_name)
    assert len(calls) == 35
    assert all(command[command.index("-m") + 1] == str(model) for command, _ in calls)
    dtw_calls = [command for command, _ in calls if "--dtw" in command]
    assert len(dtw_calls) == 14
    assert all(command[command.index("--dtw") + 1] == dtw_preset for command in dtw_calls)
    assert all(timeout == timeout_s for _, timeout in calls)
    assert report["model_preset"] == model_name
    assert report["dtw_preset"] == dtw_preset


def test_timed_out_inference_is_not_scored_as_timing_failure(tmp_path, monkeypatch):
    _, report, _ = run_harness(tmp_path, monkeypatch, "large-v3-turbo", timeout_leading=True)
    candidate = report["runs"]["patched-ordinary-vad"]
    assert candidate["fixtures"]["leading"]["execution_status"] == "timeout"
    assert candidate["fixtures"]["leading"]["status"] == "error"
    assert candidate["shift_checks"]["leading"]["status"] == "unverified"
    assert "boundary_errors_ms" not in candidate["shift_checks"]["leading"]
