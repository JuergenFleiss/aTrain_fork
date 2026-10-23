# MLX Whisper candidate evidence

Evidence retrieved 23 October 2026. This is an isolated feasibility experiment
after whisper.cpp failed the timestamp checks. It does not select a production
backend, approve timestamp quality, or change the application dependencies.

## First runtime result: native timestamps, no VAD

[Run 39927763560](https://github.com/JuergenFleiss/aTrain_fork/actions/runs/39927763560)
completed on macOS 15.7.9 arm64, runner image `20260907.0337.1`, Apple
Paravirtual device, 7,516,192,768 bytes reported system memory. Explicit MLX GPU
selection, evaluated matrix multiplication/convolution, and all seven complete
ASR workers passed under `sandbox-exec` network denial. Each worker's attempted
socket connection returned EPERM. Model/config downloads were verified before
this network-denied inference. This establishes this pinned stack's execution
on this particular hosted VM, including CPU DTW, not a physical-Mac benchmark.

The base recording decoded with macOS `afconvert` to 176,000 samples (11 s),
PCM SHA-256 `200cf71b13e4fc571f02943f470fd3305ea953ac02363541f444dc6139bf2463`.
Its bytes differ from the earlier FFmpeg decode, so this is not an identical-PCM
comparison with the previous backend. Base inference took 14.10 s and reported
2,142,867,022 bytes peak MLX memory. Other fresh workers had different model/JIT
and operating-system cache states; no speedup or repeat benchmark follows.

| Structural case | Native result |
| --- | --- |
| Base, 11 s | 22 words, ordered positive intervals within duration |
| Add 5 s leading silence | Same 22 words; maximum boundary shift error 340 ms |
| Add 5 s trailing silence | Same 22 words; maximum boundary shift error 560 ms |
| Two copies separated by 5 s silence, 27 s total | Complete repeated 44-word sequence retained; first/second copy maximum boundary shift errors 560/220 ms |
| Add 25 s leading silence, crossing the 30 s processing window | 22 words; seven unmatched words under the fixed ordered comparison; maximum matched boundary shift error 660 ms |
| Silence only, 8 s | Hallucinated “Thank you.” |
| Noise only, 8 s | Hallucinated “so” |

All matched shift medians were 0 ms, but every fixed 50 ms maximum-shift check
failed. These are invariance errors against the base model output after a known
audio transformation, not errors against human word annotations. The correct
conclusion is that native MLX timestamps avoid the preceding zero-duration
interval failure on this fixture, while the no-VAD candidate still fails the
structural gate. Large silence offsets were not simply dropped from the
timeline. VAD drift has not been tested by this no-VAD run.

## Reproducible inputs

The package under test is the published **mlx-whisper 0.4.3** wheel, rather than
the moving examples repository. [PyPI metadata](https://pypi.org/pypi/mlx-whisper/0.4.3/json)
identifies it as MIT, Python >=3.8, published 29 August 2025. Its direct
dependencies are `mlx>=0.11`, `numba`, `numpy`, `torch`, `tqdm`,
`more-itertools`, `tiktoken`, `huggingface_hub`, and `scipy`; these are largely
unbounded, so a locked isolated environment is necessary. The probe uses
**mlx 0.32.4** and its Darwin dependency **mlx-metal 0.32.4**. Neither is added
to the production `pyproject.toml` or `uv.lock`.

| Input | SHA-256 |
| --- | --- |
| `mlx_whisper-0.4.3-py3-none-any.whl` | `6b82b6597a994643a3e5496c7bc229a672e5ca308458455bfe276e76ae024489` |
| `mlx-0.32.4-cp312-cp312-macosx_15_0_arm64.whl` | `f0604cb3015091f285c79c7b7dbfcabcfa9948248728c7bab6e0263513c3d3fe` |
| `mlx_metal-0.32.4-py3-none-macosx_15_0_arm64.whl` | `9f0a3cc26d89724434d9684932fc6f3e4e83669d2a895d858ed2c8a55eb84e8b` |

MLX wheel hashes are from the versioned [MLX](https://pypi.org/pypi/mlx/0.32.4/json)
and [MLX Metal](https://pypi.org/pypi/mlx-metal/0.32.4/json) metadata. The actual
resolved wheel must match the Python and macOS version; the table records the
Python 3.12/macOS 15 pair, not every supported wheel.

The package's `audio.py`, `tokenizer.py`, `load_models.py`, `transcribe.py`,
`decoding.py`, `whisper.py`, and `timing.py` were extracted without importing
MLX and compared byte-for-byte with source at
[`ml-explore/mlx-examples` commit `cfc5d25acdd387fcf72eb4bb41c608b794633e96`](https://github.com/ml-explore/mlx-examples/tree/cfc5d25acdd387fcf72eb4bb41c608b794633e96/whisper).
All seven match. This was the last Whisper-path commit before the wheel upload;
the wheel does not itself attest a Git revision. In particular, current `main`
has subsequent changes and is not the executable evidence for this experiment.

The model is **`mlx-community/whisper-large-v3-turbo`**, immutable revision
**`a4aaeec0636e6fef84abdcbe3544cb2bf7e9f6fb`**, obtained from the
[Hub API](https://huggingface.co/api/models/mlx-community/whisper-large-v3-turbo?blobs=true).
The API's current revision takes precedence over stale web-index snapshots.
Only these two files are required by the pinned loader:

| File | Bytes | SHA-256 |
| --- | ---: | --- |
| `config.json` | 268 | `b34fc29e4e11e0a25e812775dd67f4dd16fc2c8eb43d28ae25ff7d660ecb6379` |
| `weights.safetensors` | 1,613,977,612 | `951ed3fc1203e6a62467abb2144a96ce7eafca8fa77e3704fdb8635ff3e7f8a6` |

The configuration was downloaded and hashed locally; the weight hash and byte
count come from the Hub's LFS metadata and must be checked after the runner
downloads it. The weights were not downloaded to the Linux development host.
The config has 128 mel bins, 32 encoder layers, four decoder layers, 20 decoder
heads, and no `quantization` entry. This is the unquantized candidate, not q4.

The converted model card says it was converted from `large-v3-turbo`, but its
upstream Markdown link has no target and it supplies neither a license field nor
a LICENSE file. The [OpenAI original](https://huggingface.co/openai/whisper-large-v3-turbo)
is marked MIT. Record that upstream attribution and retain its license; the
converted artifact's incomplete provenance remains a production registry/SBOM
follow-up. Do not invent a conversion source revision or claim byte-equivalence
to the original weights from this metadata alone.

## Runtime requirements and runner limits

The [MLX 0.32.4 installation instructions](https://github.com/ml-explore/mlx/blob/v0.32.4/docs/src/install.rst)
require Apple silicon, native Python >=3.10 and macOS >=14.0 for macOS wheels.
This is stricter than mlx-whisper's own Python metadata. Intel Macs and macOS 13
are outside this candidate's scope and need the existing CPU backend. `ffmpeg`
on PATH is needed when passing a filename; a mono float32 16 kHz waveform array
avoids the package's audio-decoder subprocess. Torch is a declared dependency
even though the inspected transcription path uses MLX rather than Torch.

The standard `macos-15` label is a scheduling choice, not evidence that MLX can
execute a model. A previous whisper.cpp probe observed an Apple Paravirtual GPU
with incomplete Metal features on this runner class. Successful Metal device
enumeration or elementary arithmetic does not establish support for MLX's
matrix, convolution, attention, or complete transcription operations. Explicit
GPU selection, evaluated compute, and a completed actual transcription must be
reported separately. A runtime failure on this VM is a runner limitation until
tested on a physical Apple silicon Mac; it does not prove MLX fails there.

No physical Mac result or acceleration speedup is established by this source
review. Timing includes CPU work in timestamp alignment, model load/JIT where
applicable, and the experiment's exact decoding settings; it cannot be compared
with faster-whisper beam 5 as if the decoding policies were identical.

## Timestamp and decoding behavior in 0.4.3

The pinned [`transcribe.py`](https://github.com/ml-explore/mlx-examples/blob/cfc5d25acdd387fcf72eb4bb41c608b794633e96/whisper/mlx_whisper/transcribe.py)
provides `word_timestamps=True` and returns `segments[].words[]` with `word`,
`start`, `end`, and `probability`. Segment timestamps come from Whisper timestamp
tokens on a 20 ms grid. Word timing runs an additional model forward pass with
cross-attention, normalizes and median-filters the attention, and applies dynamic
time warping. SciPy filtering and Numba DTW run on CPU. Punctuation merging and
duration/segment-boundary heuristics then adjust word intervals. Algorithm
support is not evidence that an interval meets a human timing reference.

[`whisper.py`](https://github.com/ml-explore/mlx-examples/blob/cfc5d25acdd387fcf72eb4bb41c608b794633e96/whisper/mlx_whisper/whisper.py)
defaults alignment to every head in the last half of the decoder layers. For
this turbo config that means layers 2 and 3, all 20 heads. The pinned loader does
not load model-specific alignment heads from the checkpoint or config. This
differs from assuming an externally selected alignment-head set.

`beam_size` exists in the options dataclass but **any non-None value raises
`NotImplementedError`**, including 1. Omit it. Temperature 0 uses greedy
decoding; positive temperature uses sampling, with optional `best_of`. The
default tuple retries temperatures from 0 to 1; `temperature=0.0` disables that
temperature fallback for the structural probe. Open beam-search proposals for
later source do not change this release's behavior.

There is no integrated Silero VAD or `vad_filter` option in this release.
Whisper's `no_speech_threshold` and `hallucination_silence_threshold` are
decoding/silence heuristics. `clip_timestamps` can select original-timeline spans;
it does not supply VAD. Any future external VAD integration needs its own pinned
model and tests preserving original audio offsets. VAD quality is not assessed
by a no-VAD probe.

## Local-only invocation

The pinned loader interprets an existing local directory as a local model and
reads `config.json` plus `weights.safetensors` (falling back to `weights.npz`).
A missing path instead calls `snapshot_download`; the probe must check both
files, pass an absolute directory, set offline environment flags, and deny
network access during inference. The API itself has no revision argument, so
download immutable URLs separately and verify the hashes first.

```python
import mlx.core as mx
import mlx_whisper

mx.set_default_device(mx.gpu)
result = mlx_whisper.transcribe(
    audio_16khz,
    path_or_hf_repo=str(verified_model_directory),
    language="en",
    temperature=0.0,
    fp16=True,
    word_timestamps=True,
    verbose=None,
)
```

This is the inspected interface, not a claim this example ran on the Linux
host. The worker must fail closed if GPU initialization or inference fails;
silently retrying on CPU would invalidate an acceleration result.

Tokenizer data is packaged locally in the wheel; it does not need a separate
HF tokenizer download. The relevant packaged assets and SHA-256 values are:

- `multilingual.tiktoken`: `b34b360dbb493e781e479794586d661700670d65564001f23024971d1f2fa126`
- `gpt2.tiktoken`: `306cd27f03c1a714eca7108e03d66b7dc042abe8c258b44c199a7ed9838dd930`
- `mel_filters.npz`: `7450ae70723a5ef9d341e3cee628c7cb0177f36ce42c44b7ed2bf3325f0f6d4c`

The first and third are needed for this multilingual turbo model. Preserve
package data when packaging. `ModelHolder` caches one model globally and keys
it by path, not dtype; use a fresh worker for a different dtype or device when
comparing runs. This source review does not replace the network-denied runtime
test, which must complete on the target host.

## Public speech fixture and interpretation

Reuse the immutable whisper.cpp `samples/jfk.mp3` excerpt used by the preceding
timestamp test, with its source commit and SHA-256 checked by the probe. The
recording is John F. Kennedy's inaugural address of 20 January 1961. The primary
[JFK Library sound-recording catalog entry, JFKWHA-001](https://www.jfklibrary.org/asset-viewer/archives/jfkwha-001)
explicitly gives its copyright status as **Public Domain** and attributes its
creation to the White House Army Signal Agency. Credit: White House Audio
Collection, *Swearing-in Ceremony and Inaugural Address, 20 January 1961*, John
F. Kennedy Presidential Library and Museum. This establishes a recording source,
not merely the copyright status of the speech's text.

The upstream excerpt's exact crop offset and transcoding chain from that archive
have not been established; do not claim the upstream MP3 is byte-identical to an
archive original. Retain the upstream bytes/hash and the archive credit. Use it
only as the disclosed public structural smoke fixture, not as a newly validated
quality benchmark. Leading/trailing silence and a second copy separated by a
known gap can test offset preservation, provided the exact sample recipe and
generated hashes are retained. Synthetic silence can independently check
hallucinated words.

No human word-boundary annotation, multilingual quality comparison, VAD-offset
pass, or user-audio upload is part of this evidence. Preserve the existing
[scoring gates](whisper-cpp-scoring.md), disclose the greedy-versus-beam decoding
difference, and report missing checks as pending rather than passing them from
nonempty word output.

## Separate VAD diagnostic contract

Reuse **faster-whisper 1.2.1**, already pinned by the application's lock, and its
bundled `faster_whisper/assets/silero_vad_v6.onnx`. The published wheel
SHA-256 is `79a66ad50688c0b794dd501dc340a736992a6342f7f95e5811be60b5224a26a7`.
The 1,245,151-byte ONNX asset SHA-256 is
`4cbf549b8326f60f80f2536d9eefeb450a9abe83365a098031c89719f1be17d2`;
`vad.py` SHA-256 is
`37a9c774aefdd3162d936b896c8dcf5571b2ed938d65bffecfd631770049a18d`.
Both were extracted from the hash-verified wheel and match upstream
[`v1.2.1`, commit `65882eee9f5cdbeeb2d877f1131d48cf241b327d`](https://github.com/SYSTRAN/faster-whisper/tree/65882eee9f5cdbeeb2d877f1131d48cf241b327d)
byte-for-byte. This requires ONNX Runtime, already a faster-whisper dependency;
the VAD uses `CPUExecutionProvider` and does not download a model.

Faster-whisper's [license](https://github.com/SYSTRAN/faster-whisper/blob/65882eee9f5cdbeeb2d877f1131d48cf241b327d/LICENSE)
is MIT. Its VAD code credits adaptation from Silero. Silero's
[`v6.0` license](https://github.com/snakers4/silero-vad/blob/fba061dc5559f696e62171e9a0741782b0fdc23c/LICENSE)
is MIT, copyright Silero Team. Retain both notices; the bundled ONNX file is
pinned through faster-whisper's published artifact, not asserted identical to
an unmodified Silero release graph.

Call `get_speech_timestamps(audio, vad_options=VadOptions(), sampling_rate=16000)`
on the same original, one-dimensional mono float32 waveform. Output is a list
of `{start, end}` **sample indices**, not seconds, on the original timeline.
Defaults are threshold 0.5, negative threshold 0.35, minimum speech 0 ms,
minimum silence 2000 ms, maximum speech infinity, padding 400 ms each side.
The implementation analyzes 512-sample windows, pads internally, and clamps
returned ends to the input length. Nearby spans share short-gap padding to
avoid overlap; do not pad again. Record the actual spans and every option.

There is a source-level trap in mlx-whisper 0.4.3: its multi-clip loop does not
reset `seek` to each subsequent `seek_clip_start`. Passing several disjoint
`clip_timestamps` pairs in one call can therefore process the intervening gap.
For this diagnostic, use **one call per VAD span against the full original
waveform**, with `clip_timestamps=[start / 16000, end / 16000]` and
`condition_on_previous_text=False`. The MLX timestamps are already original
seconds: combine the results without adding offsets, compressing the waveform,
or applying `SpeechTimestampsMap`. Clip coordinates round to 10 ms mel frames;
word alignment still uses its native grid and heuristics. Report out-of-span or
out-of-file predictions rather than clamping them into a passing result.

An empty MLX clip list means **process the whole file**, so no-speech VAD output
must explicitly return empty text/segments without invoking ASR. Empty audio
also needs an explicit short circuit. Validate sorted non-overlapping finite
spans within the original sample count before making calls. Independent clips
change decoding context and recompute the full spectrogram, so this is a
correctness diagnostic with disclosed overhead, not a performance integration.
If VAD excludes quiet words, count them as missing; do not score only the words
that survive. Keep no-VAD and VAD results separately, retain the unchanged
50 ms transformation tolerance, and test the silence/noise cases in both modes.
