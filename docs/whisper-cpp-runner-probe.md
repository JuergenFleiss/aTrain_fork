# whisper.cpp GitHub macOS runner probe

Status: implementation prepared on 23 October 2026; **no macOS workflow run has
been observed yet**. CPU inference, Metal compute and Metal inference are all
unverified. Local classifier tests are not hardware evidence.

This report covers task B of the macOS integration plan. It does not approve
word timestamps, VAD, quality, performance or production integration.

## Reproduction and registration

The manual workflow is `.github/workflows/whisper-cpp-evaluation.yml`. It uses
only the standard `macos-15` label, read-only repository permissions and no
secrets. The job is bounded to 30 minutes (build 15 minutes, probe 10 minutes),
individual commands are bounded, and artifacts expire after 14 days. No paid
runner is selected or provisioned. A larger-runner or physical Mac experiment
requires a separate explicit choice after checking account access and billing.

GitHub requires a dispatch workflow to exist on the default branch before it is
discoverable. Bootstrap in the testing fork with a narrowly scoped temporary
push trigger on the experiment branch, or a pull-request trigger without secrets,
then remove the temporary trigger after validation. Do not change the default
branch. Once registered:

```sh
gh workflow run whisper-cpp-evaluation.yml --repo OWNER/TESTING_FORK --ref EXPERIMENT_BRANCH
```

See [GitHub's manual-run instructions](https://docs.github.com/en/actions/how-tos/manage-workflow-runs/manually-run-a-workflow).
Runner labels and advertised resources are scheduling information; this probe
measures the actual host rather than assuming GPU access from
[runner specifications](https://docs.github.com/en/actions/reference/runners/github-hosted-runners).

## Pinned inputs and commands

- Upstream `ggml-org/whisper.cpp` v1.9.5, commit
  `d1be6fde11ac6e0407606b4e42fe72d34add8037`; MIT license retained in artifacts.
- Model `ggerganov/whisper.cpp`, Hugging Face revision
  `5359861c739e955e79d9a303bcbc70fb988958b1`, `ggml-tiny.bin`, SHA256
  `be07e048e1e599ad46341c8d2a135645097a538221678b7acdd1b1919c6e1b21`.
  Downloaded from the immutable revision URL and checked before inference.
- Synthetic English speech, generated locally by macOS `say`, voice `Samantha`,
  170 words/minute: “The quick brown fox jumps over the lazy dog. This is a local
  transcription test.” `afconvert` creates mono 16 kHz PCM16 WAV. The text,
  commands, available voices and resulting audio hash are recorded. Voice assets
  can vary with the runner image, so this is a capability smoke test, not a fixed
  quality benchmark. Audio stays in the isolated temporary cache and is not uploaded.

Build options are Release, `GGML_METAL=ON`, `GGML_METAL_EMBED_LIBRARY=ON`,
`WHISPER_COREML=OFF`, `WHISPER_BUILD_TESTS=OFF`, deployment target 14.0 and
`CMAKE_CXX_FLAGS=-DWHISPER_DEBUG`. The final flag retains debug-level Metal
operation logs; this diagnostic build is unsuitable for performance comparisons.
The source revision, build cache/options, compiler, binary hash, Xcode/SDK, image
version, OS, architecture, CPU and memory are retained.

The same binary/model/audio runs twice with English, beam size 5, temperature 0,
no temperature fallback, Flash Attention disabled, full JSON, three threads:

```sh
whisper-cli --model ggml-tiny.bin --file speech.wav --language en \
  --beam-size 5 --temperature 0 --no-fallback --no-flash-attn \
  --output-json-full --threads 3 --no-gpu --output-file cpu
GGML_METAL_GRAPH_DEBUG=1 whisper-cli --model ggml-tiny.bin --file speech.wav \
  --language en --beam-size 5 --temperature 0 --no-fallback --no-flash-attn \
  --output-json-full --threads 3 --device 0 --output-file metal
```

At this pinned revision GPU use defaults on; `--device 0` selects it and
`--no-gpu` explicitly disables it. The probe never supplies the CLI's model
download options. Model/user/cache paths are temporary and independent of the
user's real aTrain directory. This probe does not yet establish network-isolated
inference; task J requires that separate check.

## Evidence and separate outcomes

`metal_probe.swift` enumerates Metal devices and records names, memory limits,
unified-memory support, threadgroup limits and Apple/Mac GPU families. It compiles
a shader, dispatches 256 float multiplications on a Metal command queue, waits
for successful completion and checks every result. Shader compilation alone is
insufficient. A Metal compile or execution failure does not prevent the separate
CPU helper test.

`result.json` and the Actions summary emit these independent statuses:

| Check | Passed | Failed | Unavailable |
| --- | --- | --- | --- |
| CPU | Explicit `--no-gpu`, exit zero and nonempty structured transcription | Build/model/fixture/inference/schema failure | Never |
| Metal compute | Command completed and every computed value matched | Compiler/resource/command/result failure | No devices and no default device |
| Metal inference | Compute passed; real helper inference exited zero with nonempty JSON; initialization and Metal `MUL_MAT` operation logs present | Missing execution evidence, CPU fallback or inference error | Only when device probe proved absence |

The pinned-source markers are `ggml_metal_init: picking default device:` and
`ggml_metal_op_encode: node[...] ... MUL_MAT`. The latter is emitted from the
Metal operation encoder with `GGML_METAL_GRAPH_DEBUG=1`, and the diagnostic build
retains it. The classifier rejects missing markers and known fallback/error logs.
It does not treat an advertised GPU, initialized backend or CPU success as Metal
execution. Raw logs are retained for review of this conclusion.

The job fails for CPU failure or Metal failure. GPU absence permits a successful
exploratory job **with Metal explicitly unavailable**; this never satisfies the
acceleration gate. Build logs, machine metadata, compute logs, CPU/Metal logs and
public synthetic-text JSON survive failures via `always()` artifact upload.
Models, caches and audio are excluded.

## Current validation and open gates

Local Linux validation: actionlint passes, Ruff lint/format passes, and the focused
offline classifier suite passes (11 tests). Swift compilation, actual helper
Metal logs and macOS inference remain pending the first workflow run. Record the
run URL, artifact URL, observed hardware and all three statuses here after it runs.

If standard runners have no usable Metal device, CPU correctness and packaging
work can continue; acceleration needs a separately selected capable runner or
physical Mac. This workflow makes no Neural Engine claim. Targeting macOS 14
while running on macOS 15 does not establish minimum-OS runtime compatibility.
Signed-bundle launch, VAD timelines, word boundaries, quality and performance
remain separate gates in the integration plan.
