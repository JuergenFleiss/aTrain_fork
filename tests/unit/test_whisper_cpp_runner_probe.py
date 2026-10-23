"""Offline evidence classification; these are not Metal hardware tests."""

import importlib.util
import json
from pathlib import Path

import pytest

PROBE_PATH = Path(__file__).parents[2] / "scripts" / "whisper_cpp_evaluation" / "probe.py"
SPEC = importlib.util.spec_from_file_location("whisper_cpp_probe", PROBE_PATH)
probe = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(probe)


@pytest.mark.parametrize(
    ("exit_code", "log_text", "payload", "expected"),
    [
        (0, "", {"transcription": [{"text": "hello"}]}, "failed"),
        (
            0,
            "ggml_metal_init: picking default device: Apple M1",
            {"transcription": [{"text": "hello"}]},
            "failed",
        ),
        (
            0,
            "ggml_metal_init: picking default device: Apple M1\nggml_metal_op_encode: node[    1] - MUL_MAT",
            {"transcription": [{"text": "hello"}]},
            "passed",
        ),
        (
            1,
            "ggml_metal_init: picking default device: Apple M1\nggml_metal_op_encode: node[    1] - MUL_MAT",
            {"transcription": [{"text": "hello"}]},
            "failed",
        ),
        (
            0,
            "ggml_metal_init: picking default device: Apple M1\nggml_metal_op_encode: node[    1] - MUL_MAT\nerror: command buffer failed",
            {"transcription": [{"text": "hello"}]},
            "failed",
        ),
    ],
)
def test_metal_requires_execution_evidence(tmp_path, exit_code, log_text, payload, expected):
    log = tmp_path / "metal.log"
    output = tmp_path / "metal.json"
    log.write_text(log_text)
    output.write_text(json.dumps(payload))
    assert probe.classify_inference({"exit_code": exit_code}, log, output, metal=True) == expected


@pytest.mark.parametrize(
    "payload",
    [{}, {"transcription": []}, {"transcription": "hello"}, {"transcription": [{"text": None}]}],
)
def test_cpu_rejects_missing_or_malformed_text(tmp_path, payload):
    output = tmp_path / "cpu.json"
    output.write_text(json.dumps(payload))
    assert probe.classify_inference({"exit_code": 0}, tmp_path / "cpu.log", output) == "failed"


def test_cpu_pass_does_not_need_metal_logs(tmp_path):
    output = tmp_path / "cpu.json"
    output.write_text(json.dumps({"transcription": [{"text": "hello"}]}))
    assert probe.classify_inference({"exit_code": 0}, tmp_path / "cpu.log", output) == "passed"


def test_metal_malformed_output_is_failed_without_raising(tmp_path, monkeypatch):
    def fake_run(argv, log, **_kwargs):
        log.write_text("{}\nnot JSON")
        return {"exit_code": 0}

    monkeypatch.setattr(probe, "run", fake_run)
    metadata = {}
    assert probe.probe_metal(tmp_path, tmp_path, metadata) == "failed"
    assert "metal_error" in metadata
