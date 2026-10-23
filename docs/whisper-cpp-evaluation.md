# whisper.cpp helper evaluation

Status: source investigation and Linux CPU feasibility experiments, 23 October 2026.
Production integration is blocked pending the correctness experiment in
the integration plan. The CPU timestamp experiment below does not establish timing accuracy or
production readiness. Separate macOS capability results are recorded in
[the runner report](whisper-cpp-runner-probe.md).

## Decision from task A

Use **a narrowly patched upstream CLI as the next experimental candidate**.
Unmodified v1.9.5 fails the original-audio token timeline check with VAD. The
existing library exposes mapped interval accessors, so a custom executable is not
justified by this defect alone. The patch below repairs ordinary JSON interval
serialization only. It does not turn DTW points into intervals or establish
reliable word grouping. Do not begin tasks E–I until task D passes its full gate.
If the remaining interval/grouping checks fail, stop production integration;
access to the C API alone does not improve the alignment algorithm.

Assumptions: the first target remains arm64 macOS 14 with CPU/Metal, and English
and German are the first evaluation languages. Other languages need their own
grouping evidence. All local experiment audio is the upstream public demo excerpt
or silence derived from it; no private recordings were used. Its separate
recording-rights provenance must be finalized by the fixture manifest before
redistributing generated fixture assets or uploading them to CI.

## Pinned sources and models

The [latest stable release](https://github.com/ggml-org/whisper.cpp/releases/tag/v1.9.5)
was v1.9.5, published 6 October 2026, when checked. A shallow clone verified the
annotated tag object `d2a764c648779feb36d44363f212a29b00aad1af` resolves to commit
`d1be6fde11ac6e0407606b4e42fe72d34add8037`. Use that commit, never a moving branch.
The vendored ggml is included in the same checkout; do not substitute a system
ggml build. Older releases are not preferred because the current stable release
still reproduces the defect and already supplies the accessors needed to isolate
it. A moving PR head is not a release pin.

| Artifact | Immutable repository revision | File | SHA-256 | Bytes / verification |
| --- | --- | --- | --- | --- |
| Multilingual tiny | `ggerganov/whisper.cpp@5359861c739e955e79d9a303bcbc70fb988958b1` | `ggml-tiny.bin` | `be07e048e1e599ad46341c8d2a135645097a538221678b7acdd1b1919c6e1b21` | 77,691,713; downloaded and locally hashed |
| Production-family candidate | same revision | `ggml-large-v3-turbo.bin` | `1fc70f774d38eb169993ac391eea357ef47c88757ef72ee5943879b7e8e2bc69` | 1,624,555,275; downloaded, locally hashed and CPU-tested (repeat below) |
| Silero VAD 5.1.2 | `ggml-org/whisper-vad@9ffd54a1e1ee413ddf265af9913beaf518d1639b` | `ggml-silero-v5.1.2.bin` | `29940d98d42b91fbd05ce489f3ecf7c72f0a42f027e4875919a28fb4c04ea2cf` | 885,098; downloaded and locally hashed |

Checksums/size come from pinned HF tree metadata for
[Whisper](https://huggingface.co/api/models/ggerganov/whisper.cpp/tree/5359861c739e955e79d9a303bcbc70fb988958b1)
and [VAD](https://huggingface.co/api/models/ggml-org/whisper-vad/tree/9ffd54a1e1ee413ddf265af9913beaf518d1639b).
These are experiment sources, not invented aTrain-core production mirrors.
Both model cards declare MIT. Preserve the model licenses as well as the
[whisper.cpp MIT notice](https://github.com/ggml-org/whisper.cpp/blob/d1be6fde11ac6e0407606b4e42fe72d34add8037/LICENSE)
and vendored dependency notices when packaging.

The upstream [model guide](https://github.com/ggml-org/whisper.cpp/blob/d1be6fde11ac6e0407606b4e42fe72d34add8037/models/README.md)
says its GGML files are converted from OpenAI Whisper using
`models/convert-pt-to-ggml.py`. This experiment downloads the preconverted,
non-quantized tiny and large-v3-turbo artifacts; it does not reproduce the conversion. The precise
original checkpoint hash, converter revision and historical conversion command
for these HF blobs have not been independently established. A pinned HF blob is
reproducible download provenance, not proof of reproducible conversion. Resolve
that provenance before provisioning the production mirror. No quantization was
applied in this experiment.

## Build and CLI requirements

The pinned top-level CMake file declares 3.5, but vendored ggml requires
**CMake 3.14 or later**, C11 and C++17. Build tools need a C/C++ compiler. The Mac
Metal path also requires the Apple SDK/frameworks and `xcrun` shader toolchain.
The Linux CPU reproduction used CMake 4.2.3, GCC 15.2.0, Linux x86_64 on an AMD
Ryzen 7 PRO 6850U. No Python package or application dependency changed.

Exact local CPU build (from the pinned upstream checkout):

```bash
cmake -S . -B build-evidence \
  -DCMAKE_BUILD_TYPE=Release -DBUILD_SHARED_LIBS=OFF \
  -DWHISPER_BUILD_TESTS=OFF -DWHISPER_BUILD_SERVER=OFF \
  -DWHISPER_BUILD_IS_DEV=OFF -DWHISPER_CURL=OFF \
  -DGGML_NATIVE=OFF -DGGML_METAL=OFF -DGGML_CUDA=OFF -DGGML_VULKAN=OFF
cmake --build build-evidence --target whisper-cli -j 4
```

For a subsequent Mac build explicitly set `CMAKE_OSX_ARCHITECTURES=arm64`,
`CMAKE_OSX_DEPLOYMENT_TARGET=14.0`, `GGML_METAL=ON`,
`GGML_METAL_EMBED_LIBRARY=ON`, and `GGML_METAL_MACOSX_VERSION_MIN=14.0`.
The shader minimum has its own setting; a host deployment target alone is not
proof that every embedded shader supports macOS 14. Actual macOS 14 execution,
linked libraries, embedded resources and signing remain unverified.
`WHISPER_COREML=OFF` and no ANE claims are appropriate for this scope.

CPU inference uses `--no-gpu`; GPU is enabled by default, selected with
`--device 0`. There is no need to invent a `--gpu` option. The library can fall
back to CPU when no GPU is found. A successful exit or `use gpu = 1` records a
request, not effective Metal execution. The runner probe must establish actual
GPU work. Source logs include `whisper_backend_init_gpu: using … backend` and
`no GPU found`. `GGML_METAL_GRAPH_DEBUG=1` produces non-noop operation diagnostics
in `ggml_metal_op_encode_impl`, but the default Whisper callback filters debug logs
unless compiled with `WHISPER_DEBUG` (for example
`-DCMAKE_CXX_FLAGS=-DWHISPER_DEBUG` in a diagnostic build). Treat those logs as
operation-encoding evidence alongside a completed inference and the independent
Metal compute probe; do not benchmark a verbose diagnostic run as production.

## Timestamp semantics at the pin

Source anchors:
[API definitions](https://github.com/ggml-org/whisper.cpp/blob/d1be6fde11ac6e0407606b4e42fe72d34add8037/include/whisper.h#L131),
[JSON writer](https://github.com/ggml-org/whisper.cpp/blob/d1be6fde11ac6e0407606b4e42fe72d34add8037/examples/cli/cli.cpp#L699),
[ordinary timing algorithm](https://github.com/ggml-org/whisper.cpp/blob/d1be6fde11ac6e0407606b4e42fe72d34add8037/src/whisper.cpp#L8784),
[DTW algorithm](https://github.com/ggml-org/whisper.cpp/blob/d1be6fde11ac6e0407606b4e42fe72d34add8037/src/whisper.cpp#L9166).

| Field/control | Meaning / units | Caveat |
| --- | --- | --- |
| Library token `t0`, `t1` | Ordinary heuristic token start/end, centiseconds | Raw token struct retains VAD-processed time when VAD is enabled |
| `whisper_full_get_token_t0/t1` | Centiseconds on original audio timeline | Accessors map VAD segments; absent raw timing must be checked before calling |
| CLI `offsets.from/to` | Integer milliseconds (`t0/t1 * 10`) | Unpatched full JSON takes raw token struct values, unlike mapped segment offsets |
| CLI `timestamps.from/to` | Formatted `HH:MM:SS,mmm` | Same source values as `offsets`; strings do not repair the time base |
| CLI token `t_dtw` | Raw centisecond alignment point; audio frame increments 20 ms | Not start/end; `-1` when unavailable; not mapped by this patch |
| `-ml 1` | Segment wrapping at token boundaries after ordinary token timing | Does not compute an independent word aligner |
| `-ml 1 -sow` | Wrap only at a token whose text starts with ASCII space | Whitespace heuristic; no complete multilingual word segmentation |
| `-ojf` | Full JSON, enables ordinary token timing | Enabling DTW does not replace the ordinary `t0/t1` intervals |

Ordinary timing uses timestamp-token probabilities, proportional allocation based
on a pronunciation-length heuristic, then energy-based adjustments. It is
experimental; the mere presence of two numbers is not evidence of word accuracy.
A local no-VAD tiny run produced ` And` with a zero-duration interval
0.320–0.320 s. Any adapter must preserve recognized text and explicitly diagnose
unusable word timing, rather than discard it or fabricate intervals.

The CLI merges byte-level tokens only as needed to finish a UTF-8 code point.
That avoids invalid JSON text for CJK characters; it is not lexical word grouping.
English/German subwords need demonstrated grouping that preserves spaces and
punctuation. Non-space-delimited languages need language-aware boundaries and a
small verified case before claiming support. Do not split text uniformly in time.

DTW needs the model-matched preset (`tiny` versus `tiny.en`, and
`large.v3.turbo` for the production candidate). Presets select specific attention
heads. In the source, it re-decodes the recognized token sequence, copies cross
attention to a CPU tensor, and runs filtering/DTW on CPU. Therefore Metal inference
with DTW still includes CPU alignment overhead. Beam size is a separate decode
control; no blanket beam-search prohibition is present in this path, and the
local tiny DTW beam-5 run completed. This does not verify production-model or
Metal correctness.

**Flash Attention defaults to enabled and disables DTW**, with a warning while
allowing successful transcription. Always use `--dtw tiny --no-flash-attn` for the
DTW experiment and assert initialization reports `dtw = 1`. A local run omitting
`--no-flash-attn` confirmed the warning and `t_dtw = -1` on the text tokens.
The performance comparison must explicitly account for this change.

DTW uses `(time_index * 2) + seek`, so its point is chunk-relative plus the
current seek, not a per-chunk zero-based timestamp. The source still contains a
`FIXME` asking whether offsets are correct around the chunk call. A 36-second
local fixture (25 seconds silence plus the 11-second demo), crossing 30 seconds,
completed with DTW enabled, but ordinary `t0/t1` still gave the first recognized
` And` 0–15.480 s despite the late speech. Its `t_dtw` was 2552 (25.52 s).
This demonstrates the two timing methods differ; it does not validate boundary
accuracy, continuity across long interviews, or derive a missing DTW end time.

## VAD mismatch reproduction and isolated patch

Rechecked 23 October 2026:
[issue #4046](https://github.com/ggml-org/whisper.cpp/issues/4046) and
[PR #4068](https://github.com/ggml-org/whisper.cpp/pull/4068) are both open.
The earlier issue's closure does not establish a released fix. The PR also
changes no-speech probability behavior; this experiment does not import those
unrelated changes. Pinned-source inspection and an actual run independently
confirm the JSON bug.

Use an isolated experiment directory for every model, audio file and output.
Do not point `ATRAIN_USER_DIR` or a cache at the real Documents/aTrain folder.
Pinned `samples/jfk.mp3` is the source demo (there is no `samples/jfk.wav` in this
revision). Local-only preparation used ffmpeg:

```bash
ffmpeg -hide_banner -loglevel error -i samples/jfk.mp3 \
  -ar 16000 -ac 1 -c:a pcm_s16le "$EVIDENCE/jfk.wav"
```

The decoded demo is exactly 176,000 samples / 16,000 = 11 seconds. Prepend
80,000 zero samples (5 seconds) for the leading-silence case. For the internal-gap
case concatenate demo + 80,000 zero samples + demo (27 seconds). The long case
is 400,000 zero samples (25 seconds) + demo (36 seconds). Python's `wave` module
preserves PCM16 mono samples; duration checks use sample count, not an integer
metadata duration.

Exact inference flags, with local model paths and output prefixes supplied:

```bash
whisper-cli -m "$EVIDENCE/ggml-tiny.bin" -f "$EVIDENCE/leading.wav" \
  -l en -t 4 -bs 5 -tp 0 -nf -ng -nfa \
  --vad -vm "$EVIDENCE/ggml-silero-v5.1.2.bin" \
  -ojf -of "$EVIDENCE/leading-vad"
```

Both unmodified and patched runs exited 0. Before applying any patch the
following check failed on the unmodified JSON:

```python
first = next(
    token
    for segment in result["transcription"]
    for token in segment["tokens"]
    if not token["text"].startswith("[_")
)  # this fixture's special tokens
assert first["offsets"]["from"] >= 5000
```

Unmodified segment offsets were 5310–15450 ms, while the first recognized token
` And` was 20–220 ms. The logged VAD mapping began at original 5.31 s versus
processed 0 s. The failure is the expected removed-silence time-base mismatch.
The special-token filtering above is a focused reproduction, not a production
parser specification.

Only `examples/cli/cli.cpp` was patched in the disposable upstream checkout:

```diff
-                            merged_token m{ whisper_token_to_str(ctx, tok.id), tok, tok.t1 };
+                            merged_token m{ whisper_token_to_str(ctx, tok.id), tok,
+                                tok.t1 >= 0 ? whisper_full_get_token_t1(ctx, i, j) : tok.t1 };
+                            if (tok.t0 >= 0) {
+                                m.data.t0 = whisper_full_get_token_t0(ctx, i, j);
+                            }
@@
-                                    m.t1 = tok_next.t1;
+                                    m.t1 = whisper_full_get_token_t1(ctx, i, j);
```

The guard preserves absent ordinary timing rather than mapping a negative
sentinel to the first VAD boundary. Subsequent UTF-8 continuation pieces use
their mapped end too. Patch-file SHA-256 from `git diff -- examples/cli/cli.cpp`:
`5cbe11b8c0d3695ce52a5b24616fc13cd69ae2108bfe8f7b8ce601c5b36dc263`.
Rebuild with the same CMake target; the failing check then passes with ` And`
5330–5530 ms. The recognized text and token probabilities are identical between
these two runs; only serialized ordinary offsets change.

The library accessor snaps gap times to the nearest speech boundary and enforces
at least one centisecond on a mapped end. That can alter zero-duration tokens;
a positive duration after mapping is not proof of acoustic accuracy. Validate
bounds, gap behavior, punctuation, and text coverage independently.

With `--dtw tiny --no-flash-attn` added to that same patched VAD run, ` And`
has mapped ordinary offsets 5330–5530 ms but `t_dtw = 18` (0.18 s on the
compressed timeline). There is no corresponding VAD-aware DTW-point accessor.
The proposed interval serialization patch must not be presented as a DTW fix.

## Remaining gates and evidence retention

| Gate | Current verdict |
| --- | --- |
| Exact upstream source and model download pin | Passed for tiny and VAD; conversion provenance still incomplete |
| Real unmodified CPU VAD/JSON mismatch | Reproduced, failing |
| Narrow ordinary interval serialization repair | Leading-silence reproduction passes after patch |
| DTW disabled with default Flash Attention | Reproduced |
| DTW usable word intervals on original VAD timeline | Unverified; raw point time base known wrong for this purpose |
| English/German word grouping, non-space-delimited case | Pending fixture/scoring review and task D |
| Human word-boundary accuracy, WER, long-recording continuity | Unverified |
| Actual macOS CPU/Metal capability | Passed in the separate runner probe; timing/VAD on Metal unverified |
| Minimum OS, package/signing | Unverified |
| Inference with network externally disabled, parent-death cleanup | Unverified |
| Production adapter contract / release | Blocked |

Local logs, raw JSON, binary hashes and generated audio remain in the disposable
experiment workspace `/tmp/atrain-whisper-a`; generated transcripts/audio/models
are not intended for the source tree. There is no GitHub workflow run or artifact
link for this local reproduction. The manual workflow must upload licensed/public
fixture outputs, logs, patch and machine-readable measurements with immutable run
links before its result is called reproducible CI evidence. This report alone
records a narrow defect and repair, not a completed feasibility comparison.

## Task D: initial tiny CPU feasibility result

**Stop before task E.** The narrow ordinary-VAD patch fixes serialization, but
this pinned tiny configuration fails the fixed 50 ms inserted-silence shift
check. DTW does not repair the ordinary intervals and its separate points remain
on the compressed timeline. No custom helper is justified as a solution to these
observed alignment failures. This verdict covers the tested configuration;
it does not prove every model/configuration is incapable of passing.

The stdlib-only reproduction is
[`scripts/whisper_cpp_evaluation/feasibility.py`](../scripts/whisper_cpp_evaluation/feasibility.py).
Apply [the isolated patch](../scripts/whisper_cpp_evaluation/patches/v1.9.5-vad-json-token-intervals.patch)
to one otherwise identical source build. Keep the other helper unmodified.
It requires the exact tiny/VAD hashes above and already decoded PCM16 mono 16 kHz
WAV files. Example, using paths under a disposable directory:

```bash
python scripts/whisper_cpp_evaluation/feasibility.py \
  --upstream "$EVIDENCE/whisper-cli-unpatched" \
  --patched "$EVIDENCE/whisper-cli-patched" \
  --model "$EVIDENCE/ggml-tiny.bin" \
  --vad-model "$EVIDENCE/ggml-silero-v5.1.2.bin" \
  --speech "$EVIDENCE/jfk.wav" \
  --german "$EVIDENCE/german-left.wav" \
  --japanese "$EVIDENCE/japanese.wav" \
  --output-dir "$EVIDENCE/cpu-results"
```

The output directory must not already exist. A failed candidate structural gate
returns exit code 1 and retains logs/JSON/report. An exit code 0 still does not
pass unverified quality or production gates. The script does no downloads and
runs explicit CPU requests. It does not itself prohibit network system calls;
externally isolated inference remains a separate check.

The initial run completed **45 real helper invocations**: five configurations
across original/leading/trailing/internal/30-second-boundary/silence/noise and two
multilingual candidates. DTW rows use `--dtw tiny --no-flash-attn`; beam 5,
temperature 0, no temperature fallback and four threads are explicit throughout.
There are no three-repeat performance measurements and no speedup claim.

Paired checks compare the same normalized recognized word sequence in order and
retain unmatched counts. The provisional word grouping starts at whitespace and
attaches continuation pieces/punctuation without changing their text or timing.
This is sufficient to expose English timing instability, but not a production
multilingual grouping contract. The coordinator fixed a separate maximum 50 ms silence-shift tolerance before
the scripted matrix. This exploratory stability threshold is distinct from the
plan's median/p95 human-reference error degradation limit; it was not relaxed
after the run.

| Ordinary configuration | Leading 5 s: max boundary shift error | Internal gap: first / second copy max error | 25 s prefix / 30 s stress: max error | Result |
| --- | --- | --- | --- | --- |
| Unmodified, VAD | 5,080 ms | 160 ms / unmatched second copy on expected timeline | 25,160 ms | Failed original timeline |
| Accessor patch, VAD | 150 ms | 110 ms / 1,510 ms | 150 ms | Failed 50 ms stability threshold |

For the patched row **all English paired comparisons match all 22 provisional
words, with zero unmatched reference or candidate words**. The internal second
copy of ` Americans` moves from 1520–2100 ms in the original to 17770–19610 ms
in the composite; subtracting its exact 16,000 ms insertion offset gives boundary
errors 250 / 1510 ms. This is a relative timing failure on identical speech,
independent of missing human accuracy annotations. All targeted English patched
VAD intervals were positive, bounded and ordered. Adding DTW produces the same
ordinary-interval outcomes because DTW writes a different field.

Eight-second digital silence and deterministic noise (seed 42, signed PCM16
uniform samples in [-1500,1500]) produced no words with VAD, both patched and
unmodified. Without VAD, this tiny model emitted text on both; its original and
trailing-silence speech also contained a zero-duration first provisional word.
These are recorded failures of the corresponding configurations, not sanitized
into empty outputs.

The German source candidate is nearly opposite-polarity stereo. The initial
standard ffmpeg mono downmix had peak 111/32768 and RMS 3.83 PCM units; VAD
correctly found no speech. Do not attribute that fixture-preparation failure to
the helper. A separately labeled diagnostic selected the left channel explicitly:

```bash
ffmpeg -hide_banner -loglevel error -i german_speech.ogg \
  -af 'pan=mono|c0=c0' -ar 16000 -c:a pcm_s16le german-left.wav
```

That WAV has SHA-256
`b633063674e7e93ae31f33a158fedbaa71349b05f098f87b3c12ec30a8e23b28`,
peak 22757 and RMS 2474.45. Patched ordinary VAD returned nonempty German text
with bounded, positive provisional word intervals. Multi-token examples include
`w` + `irst`, `ber` + `ührt`, and `pack` + `en`; concatenation preserved their
recognized spelling and punctuation. This is structural grouping evidence only;
it does not establish reference transcription accuracy or timing accuracy.
The single Japanese pronunciation returned `こんにちは` as one token and one
interval, 390–1070 ms. That exercises UTF-8 output, not segmentation of a
multiword non-space-delimited utterance. Its broader grouping gate stays open.

Local machine-readable report and raw samples:
`/tmp/atrain-whisper-a-cpu-results/report.json`, plus per-run JSON/logs there;
the German channel diagnostic is `german-left-diagnostic.*`. These files are
not committed or uploaded. The initial report explicitly includes the inaudible
German downmix failure; the separate diagnostic does not overwrite it. No run or
artifact URL exists yet for D. Helper binary hashes for these local builds are:

| Helper | SHA-256 |
| --- | --- |
| Unmodified | `ed9333ba257b89517630f9f502021d43f04786d8d9fa30f535d46b9878df4031` |
| Accessor patch | `ddd1cd92a14ba88f5b23580bae7fcb97561e463772254577ce9af56882742897` |

The full production gate remains blocked by observed interval instability and
unverified human-reference quality, broader multilingual grouping, real long
interviews/turns, Metal with timing/VAD, minimum OS/runtime, packaging and
cleanup. At this initial tiny stage, the production-family model and faster-whisper
baseline comparison had not run. The requested production-family repeat is
recorded separately below; neither result justifies task E. A separately preregistered
experiment with a better configuration may reopen D; do not silently relax this
run's threshold or ship this configuration.

## Coordinator disposition

Tasks A–D produced a pinned investigation, executable macOS capability probe,
fixture inventory/scoring specification and real CPU feasibility evidence. C's
human-reference and broader fixture coverage remain incomplete. Independent
review verified the reported shift errors and the decision to stop before E.
Production tasks E–K and a full release review are not completed or approved.
No application code, model registry, dependencies or packaging were changed.

The testing branch is `feature_whisper_cpp_macos` in
[JuergenFleiss/aTrain_fork](https://github.com/JuergenFleiss/aTrain_fork/tree/feature_whisper_cpp_macos).
Ruff lint/format, 134 offline unit tests and application/engine Bandit checks
passed. Existing core/UI suites were not run because application code is
unchanged; the real-helper CPU experiment and macOS workflow are the relevant
additional execution checks. No performance, signed-package or macOS 14 runtime
claim is made.

## Task D: requested large-v3-turbo CPU repeat

This repeat tests the production-family candidate with the same protocol.
The non-quantized `ggml-large-v3-turbo.bin` at the HF revision/hash above was
downloaded and its full SHA-256 verified locally. Its bytes reside in
`/home/juergen/github/aTrain/.cache/whisper-cpp-evaluation/` (gitignored disk
storage; `/tmp` on this host is RAM-backed). Both existing pinned helper builds
were reused. The German input uses the explicit left-channel transform above.
No inference configuration or 50 ms threshold was relaxed.

The harness now accepts `--model-preset large-v3-turbo`, selecting that model's
hash and DTW preset `large.v3.turbo`; tiny remains the default. Add this option
to the earlier command, supply the turbo model path, and use a fresh output
directory. Each turbo invocation has a 900-second timeout; timeout/output/helper
errors are separately recorded and incomplete paired timing is unverified.
All **45 real turbo CPU invocations completed without timeout or execution
error**. The script exited 1 because its candidate correctness checks failed.
The tests confirm actual helper argv/preset selection and timeout classification;
their fake helpers are not timing evidence.

For patched ordinary VAD, all English per-file intervals were positive, bounded
and ordered, but the paired timeline checks still failed. Errors below combine
start and end boundaries, in milliseconds. The original time-window partition is
preserved for comparison with the tiny run:

| Case | Tiny median / max error | Turbo median / max error | Turbo matched / unmatched reference / unmatched candidate words |
| --- | --- | --- | --- |
| 5 s leading silence | 20 / 150 | 90 / 1840 | 22 / 0 / 0 |
| 5 s trailing silence | 0 / 0 | 0 / 0 | 22 / 0 / 0 |
| 25 s prefix, original timeline crosses 30 s | 10 / 150 | 10 / 150 | 22 / 0 / 0 |
| Internal gap, first window | 0 / 110 | 20 / 1380 | 22 / 0 / 1 |
| Internal gap, second window | 210 / 1510 | 490 / 1690 | 21 / 1 / 0 |

The internal window counts **do not mean text was lost**. The turbo composite's
entire normalized 44-word sequence equals its base 22-word sequence repeated
exactly twice. Its second-copy ` And` is incorrectly timed 10410–10590 ms,
placing it in the first window. The base word is 330–530 ms; adding the known
16000 ms composite offset would give 16330–16530 ms. A separate diagnostic,
performed only after verifying exact equality of the complete repeated word
sequence, splits by lexical order: all 22 second-copy words match with no
unmatched words, median error 500 ms and maximum error **5940 ms**. The original
window scores above remain unchanged. This is a concrete timing failure on
identical speech, independent of a human accuracy reference.

The audible German left-channel case also fails interval ordering after the
patch: ` Junge,` is 9250–9260 ms, ` du` is 9250–9260 ms, and ` wirst` is
9250–9340 ms. The library's positive-duration minimum has turned coincident raw
boundaries into overlapping provisional words. The harness preserves and reports
them; it does not clamp or redistribute them. Japanese returns one nonempty
UTF-8 word with a valid interval, which still does not establish multilingual
lexical grouping. VAD silence/noise cases return no words. The unmodified
no-VAD configuration has zero-duration words and emits text on silence/noise;
these separate failures are retained too.

Enabling DTW with `large.v3.turbo` and Flash Attention disabled completed and
reported `dtw = 1`. Across all nine fixtures, its ordinary text/interval results
are identical to the corresponding ordinary-VAD configuration. The separate
first text DTW point is 22 centiseconds in both the base and 5-second-prefixed
VAD cases, confirming that point remains on the compressed timeline. No DTW
start/end word interval has been derived or claimed. The 25-second-prefix case
stresses the original timeline; with VAD removing silence, it does not establish
that a word crosses an internal decoder chunk boundary.

Turbo report and raw JSON/logs are retained locally at
`/tmp/atrain-whisper-a-turbo-cpu-results/report.json`; the exact-sequence companion
is `paired-sequence-diagnostic.json` in that directory. No outputs or models were
published. There is no turbo workflow/artifact URL. Model identity, helper hashes,
commands, fixture hashes/durations, per-run wall time, interval failures, paired
errors and unmatched counts are in the report. There was one run per
configuration/case, so no repeated-run performance claim is made.

**This tested turbo CLI/ordinary-timing/VAD configuration also fails the gate;
task E remains blocked.** That verdict concerns the measured configuration and
does not establish that every possible whisper.cpp model or alignment method
fails. A different method needs a separate demonstrated interval contract and
experiment. Faster-whisper quality comparison, human timing accuracy, turbo on
Metal, long interviews, actual word-crossing decoder boundaries and release
checks remain unverified; none is needed to explain the observed failures above.
