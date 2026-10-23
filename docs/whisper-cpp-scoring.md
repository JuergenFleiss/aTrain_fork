# whisper.cpp fixture and scoring protocol

This document fixes the comparison rules for the feasibility experiment before
any whisper.cpp output is scored. The inventory is in
[`tests/fixtures/whisper_cpp/manifest.yaml`](../tests/fixtures/whisper_cpp/manifest.yaml).
That manifest deliberately distinguishes existing files that can be run locally
from cases that still need a verified source, human annotation, or both. A path
being present in Git does not itself establish permission to redistribute it.

## Fixture readiness

The existing English 3.2-second LibriVox excerpt is available for local
structural smoke checks. Its ID3 tags identify *Andersen's Fairy Tales*, track
1, Kara Shallenberg, and LibriVox's catalog entry describes the recording as
public domain in the USA. Preserve the source credit and verify the exact excerpt
and applicable local public-domain status before putting it in an uploaded
artifact. It is too short and too narrow to support text or timing quality
claims.

The 14.6-minute Lagarde/Enria file and its reference text already exist in the
repository and support local feasibility exploration. The README attributes
the source to an ECB YouTube publication under a Creative Commons license, but
the repository does not record the exact license version or trim offsets. Treat
it as a candidate, not as approved artifact content, until those are recorded.
The reference text has not been human-audited, so current WER results on it are
not ground-truth scores.

The manifest pins small German and Japanese public audio candidates by source
URL and SHA-256; their bytes are in `/tmp/atrain-whisper-c-sources` for this
experiment and are not committed. Re-fetch from the source and verify the hash
before use elsewhere. Human-checked German/Japanese references, reviewed English
and German text sets, word-boundary annotations, rapid speaker-turn labels, and
a verified word crossing a 30-second boundary are still pending. Do not claim
multilingual quality or word-timing accuracy before those cases are prepared.
The manifest includes deterministic recipes for silence and noise signals; a
generated file is usable only when its emitted hash and exact recipe are
included with that run.

For each new public recording, record title, author/performer, exact source URL,
license identifier and URL, retrieval date, crop offsets, transformations, and
SHA-256. Keep the license notice with any copy. For an original synthetic
signal, record sample format, duration, seed and generation parameters. Never
put private evaluation material in GitHub artifacts.

## References and human annotations

Before scoring text, have a human check the verbatim transcript against the
audio, including disfluencies, contractions, punctuation, speaker overlap and
names. Keep the source transcript and a normalized scoring view separately.
Do not label an automatic transcript or forced alignment as human ground truth.

For timing, annotate word start and end in seconds on the original file's
timeline, with a speaker label when turns are clear. Select a manageable,
representative subset and record its exact size and reviewed spans before
running either system. Include quiet speech, short words, pauses, and words near
chunk boundaries where available. Store annotations outside workflow artifacts
unless the source's license and the annotation's terms allow publication.
Pending annotations remain pending; no estimates are entered as measurements.

Suggested annotation table columns:

```text
fixture_id,audio_sha256,language,reviewer_id,word_index,word,start_s,end_s,speaker,notes
```

Use seconds from the beginning of the decoded original audio. Record audio
duration as `len(decoded_audio) / 16000`; do not round to whole seconds. Speech
word text may be normalized for matching, but retain the verbatim word and
punctuation. Do not shift references to a VAD-compressed timeline.

## Comparisons

Compare the same decoded audio and language with faster-whisper CPU beam 5 as
the baseline and whisper.cpp CPU and confirmed Metal as candidates. Keep model
family/size, source where possible, quantization, decoding options, VAD settings,
and input sample rate fixed or disclose each difference. Beam 1 is diagnostic
only. Report ordinary timings and DTW separately. A Metal result counts only
when runtime logs confirm Metal execution; CPU fallback is a separate CPU row.

Use the same text normalization for reference, baseline and candidate: lowercase,
expand common English contractions only for English, replace hyphens with
spaces, remove punctuation, collapse spaces, trim, then tokenize by the
language's chosen reference convention. Do not apply English contraction
expansion to German or the non-space-delimited case. Report reference word
count, insertion/deletion/substitution counts and WER for each language and
system. Inspect and report repeat loops and missing passages separately.

Match candidate and baseline timing to the human reference by normalized word
sequence in order. Do not discard unmatched words silently. Report reference
coverage, unmatched reference words, unmatched hypothesis words, and the number
of boundaries scored. For each matched word, calculate absolute start and end
boundary error against human reference in milliseconds. Also report each
system's median and p95 absolute boundary error. Do not report a matched-only
timing score as complete when the coverage gate fails.

## Fixed gates

These thresholds are set before comparison and must not be relaxed after looking
at results:

| Gate | Pass condition |
| --- | --- |
| Text quality, English | Candidate WER is no more than 1.0 absolute percentage point above faster-whisper CPU beam 5. |
| Text quality, German | Candidate WER is no more than 1.0 absolute percentage point above faster-whisper CPU beam 5. |
| Relative timing | Candidate median and p95 absolute boundary errors each worsen by no more than 50 ms versus baseline. |
| Original timeline | Every tested interval is finite, ordered, nonnegative, and within the exact decoded audio duration; no detected word may shift onto a VAD-compressed timeline. |
| Silence behavior | Silence-only audio returns no words. |
| Boundary and grouping | The selected multi-token word groups without loss or duplication; a word crossing the 30-second boundary remains on the original timeline and appears once. |
| Metal identity | The run is counted as Metal only with positive runtime execution evidence. Unavailable hardware is unverified and leaves the acceleration gate open. |

Report annotation count and timing coverage, plus unmatched words; do not hide
alignment failures by reporting only matched words. Structural gates apply to
every targeted case, not only the quality subset. For generated speech
composites, verify that known inserted silence shifts word times on the original
timeline and repeat around the known internal gap; do not invent a word-level
reference when the speech has not been annotated. Inspect the noise case and
report false positives.
Nonempty recognized text without usable word timing fails the correctness gate;
uniformly splitting text to manufacture boundaries is prohibited. Any missing
fixture or human annotation means its corresponding gate is **unverified**, not
passed. The current manifest therefore does not provide enough evidence to
pass the English/German text, timing, multilingual grouping, rapid speaker
change, or boundary gates.

## Measurements and artifacts

For long material, run at least three fresh-process repetitions per system and
report median and spread. Measure model load, VAD/alignment, inference and total
job time separately; include fresh-process load in end-to-end time. Report real
time factor as wall seconds divided by exact audio seconds, peak memory,
failures, and helper cleanup results. Record host/VM, OS, architecture, model
and audio hashes, model source/revision, quantization, command/options, timing
mode, VAD/Flash Attention settings, and evidence used to establish Metal.
Keep one-invocation cold results separate from any warm in-process diagnostics.

Artifacts may contain machine-readable measurements and public fixture outputs
only after the corresponding redistribution terms are verified. Do not upload
model caches, credentials, private audio, or transcripts from user recordings.
