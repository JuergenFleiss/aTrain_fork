"""Structural scoring checks; mocked words are not MLX timing evidence."""

import importlib.util
from pathlib import Path

import pytest

SCRIPT = Path(__file__).parents[2] / "scripts" / "mlx_whisper_evaluation" / "feasibility.py"
SPEC = importlib.util.spec_from_file_location("mlx_whisper_feasibility", SCRIPT)
feasibility = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(feasibility)


def result(words, text=" One two."):
    return {"text": text, "segments": [{"text": text, "words": words}]}


def word(text, start, end):
    return {"word": text, "start": start, "end": end, "probability": 0.9}


def test_native_word_intervals_preserve_text_and_seconds():
    inspected = feasibility.intervals(
        result([word(" One", 0.12, 0.23), word(" two.", 0.23, 0.4)]), 1000
    )
    assert inspected["problems"] == []
    assert inspected["words"][0] == {"text": " One", "start_ms": 120, "end_ms": 230}


@pytest.mark.parametrize("start,end", [(float("nan"), 0.4), (0.1, float("inf")), (True, 0.4)])
def test_invalid_timing_is_diagnosed_without_fabricating_interval(start, end):
    inspected = feasibility.intervals(result([word(" One two.", start, end)]), 1000)
    assert inspected["problems"]
    assert inspected["words"] == []


def test_missing_word_and_overlap_are_retained_as_failures():
    inspected = feasibility.intervals(
        result([word(" One", 0.1, 0.3), word(" two.", 0.2, 0.2)]), 1000
    )
    assert len(inspected["words"]) == 2
    assert any("overlapping" in issue for issue in inspected["problems"])
    assert any("nonpositive" in issue for issue in inspected["problems"])
    missing = feasibility.intervals(result([word(" One", 0.1, 0.3)]), 1000)
    assert any("coverage" in issue for issue in missing["problems"])


def test_repeated_words_score_by_sequence_without_changing_window_score():
    base = [{"text": " One", "start_ms": 100, "end_ms": 200}]
    repeated = [*base, {"text": " One", "start_ms": 300, "end_ms": 400}]
    checks = feasibility.paired_checks(
        {
            name: {"words": words, "execution_status": "completed"}
            for name, words in {
                "base": base,
                "leading": base,
                "trailing": base,
                "boundary": base,
                "internal": repeated,
            }.items()
        },
        1000,
    )
    assert checks["internal-second"]["unmatched_reference_words"] == 1
    assert checks["internal-sequence"]["second"]["matched_words"] == 1
    assert checks["internal-sequence"]["second"]["max_boundary_error_ms"] == 5800
    assert checks["internal-sequence"]["second"]["status"] == "failed"


def test_sequence_diagnostic_requires_complete_repeated_sequence():
    base = [{"text": " One", "start_ms": 100, "end_ms": 200}]
    assert feasibility.sequence_check(base, base, 6000)["status"] == "unverified"


def test_timeout_pair_is_unverified_without_timing_errors():
    completed = {"words": [], "execution_status": "completed"}
    runs = {
        name: dict(completed) for name in ("base", "leading", "trailing", "internal", "boundary")
    }
    runs["leading"]["execution_status"] = "timeout"
    check = feasibility.paired_checks(runs, 11000)["leading"]
    assert check["status"] == "unverified"
    assert "boundary_errors_ms" not in check


def test_fifty_ms_threshold_ignores_sub_nanosecond_float_noise_only():
    base = [{"text": " word", "start_ms": 330.0, "end_ms": 530.0}]
    shifted = [{"text": " word", "start_ms": 5380.000000000001, "end_ms": 5580.0}]
    assert feasibility.shift_check(base, shifted, 5000)["status"] == "passed"
    shifted[0]["start_ms"] = 5380.001
    assert feasibility.shift_check(base, shifted, 5000)["status"] == "failed"


def test_vad_samples_keep_original_seconds_and_order():
    clips = feasibility.clip_seconds(
        [{"start": 80000, "end": 240000}, {"start": 320000, "end": 400000}], 500000
    )
    assert clips == [[5.0, 15.0], [20.0, 25.0]]
    assert feasibility.clip_seconds([], 128000) == []


@pytest.mark.parametrize(
    "spans",
    [
        [{"start": -1, "end": 16000}],
        [{"start": 16000, "end": 16000}],
        [{"start": 0, "end": 160001}],
        [{"start": 0, "end": 80000}, {"start": 79999, "end": 160000}],
        [{"start": 0.0, "end": 16000}],
    ],
)
def test_invalid_vad_spans_are_rejected(spans):
    with pytest.raises(ValueError):
        feasibility.clip_seconds(spans, 160000)


def test_empty_vad_never_calls_asr():
    def forbidden(*args, **kwargs):
        pytest.fail("empty clip list must skip ASR; MLX otherwise treats it as full audio")

    result, calls = feasibility.transcribe_clips(object(), [], forbidden, {})
    assert result == {"text": "", "segments": [], "language": "en"}
    assert calls == []


def test_vad_calls_use_full_audio_and_already_absolute_native_times():
    audio = object()
    calls = []

    def fake_transcribe(supplied, **kwargs):
        assert supplied is audio
        calls.append(kwargs["clip_timestamps"])
        start, end = kwargs["clip_timestamps"]
        return {
            "text": " word",
            "segments": [{"text": " word", "words": [word(" word", start + 0.1, end - 0.1)]}],
            "language": "en",
        }

    result, _ = feasibility.transcribe_clips(
        audio, [[5.0, 10.0], [15.0, 20.0]], fake_transcribe, {"language": "en"}
    )
    assert calls == [[5.0, 10.0], [15.0, 20.0]]
    assert result["segments"][1]["words"][0]["start"] == 15.1
    assert result["text"] == " word word"


def test_native_word_leaking_outside_clip_is_diagnosed_without_clamping():
    native = result([word(" One two.", 4.98, 6.0)])
    assert feasibility.clip_interval_problems([native], [[5.0, 6.0]])
    assert native["segments"][0]["words"][0]["start"] == 4.98
