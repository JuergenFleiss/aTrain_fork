# Plan: whisper.cpp helper backend and macOS validation

Status: proposed; implementation and hardware validation have not started.
Baseline: `develop` at `75f90f7`, inspected on 23 October 2026.

This plan supersedes the MLX-first direction in
[the acceleration evaluation](../macos-acceleration-evaluation.md) for the next
prototype. The chosen integration is a Python backend adapter that invokes a
bundled whisper.cpp executable. The user has no Mac, so macOS validation starts
in GitHub Actions. A successful CPU run must never count as a Metal test.

## 1. Scope and decisions

- `aTrain_core/data/models.json` remains the source of truth for backend selection:
  new, separately named GGML model entries use `"backend": "whisper-cpp"`.
  Existing faster-whisper and CrisperWhisper entries keep their current backends.
  There is no independent backend selector in the UI.
- Implement the existing `Transcriber` contract: decoded NumPy audio in,
  timestamped word segments out, plus progress, logging and `close()`.
- Start with upstream `whisper-cli` as the helper. A small custom executable linked
  to whisper.cpp is a contingency if the CLI cannot expose the required data.
  Decide this after the timestamp experiment, before production integration.
- First shipping target: Apple Silicon macOS, minimum macOS 14. Support CPU and
  Metal within this backend. Existing engines remain the supported paths on
  Windows, Linux and Intel macOS; do not expose unusable model choices there.
- Keep speaker detection on CPU for the new macOS path. ASR device selection must
  not send pyannote to CUDA. Crisper MPS, MLX, Neural Engine/Core ML acceleration,
  a new queue system and a persistent helper server are outside this first scope.
- The GGML checkpoint can serve CPU and Metal. If Metal is unavailable, report it
  and offer an explicit CPU retry with that checkpoint. Do not silently substitute
  a different model/backend or download a CTranslate2 model during recovery.
- One helper invocation per recording initially. Count model-load overhead in
  end-to-end measurements; do not promise cross-job model reuse.
- Audio/transcripts remain local in the product. CI uses only public or synthetic
  fixtures whose redistribution is allowed. Never upload a user's interview to a
  runner or include private recordings in workflow artifacts.
- Python dependency changes use uv and include `uv.lock`. Build the native helper
  from a pinned source commit; record its build options and required licenses.

These are implementation assumptions, not benchmark results. Proposed quantitative
acceptance thresholds below should be fixed in the experiment manifest before
running the comparison, and not relaxed after seeing unfavorable results.

## 2. Current integration points

| Area | Existing files and required change |
| --- | --- |
| Backend dispatch | `aTrain_core/engine.py`: register an adapter implemented in new `aTrain_core/backends/whisper_cpp.py`; retain lazy imports. |
| Device/settings | `aTrain_core/settings.py`, `aTrain_core/cli.py`: validate the selected backend/device combination and meaningful precision settings. |
| Process ownership | `aTrain_core/transcribe.py`, `aTrain/utils/transcription.py`: support the helper without leaving child processes behind or following CUDA-only branches. |
| Model lifecycle | `aTrain_core/data/models.json`, `aTrain_core/load_resources.py`, `aTrain/utils/models.py`: separate GGML entries, checked files, supported-platform filtering and correct installed status. |
| UI | `aTrain/components/settings/advanced.py`, `aTrain/components/settings/model.py`, `aTrain/components/dialogs/process.py`, `aTrain/pages/models.py`: model-aware settings and actual execution device. |
| Output | `aTrain_core/backends/common.py`, `aTrain_core/outputs.py`: preserve word spacing, punctuation, timestamps, speaker assignment and effective-backend metadata. |
| Packaging | `macos_freeze.spec`, `.github/workflows/release.yml`, `.github/scripts/build-sbom.py`: include native helper/resources, provenance and smoke tests. |

The current checkout has no `aTrain_core/runner.py` or queue service. If the queue
or CLI-worker work lands first, rebase and move process ownership into that runner;
do not create a second scheduler or retain two competing execution paths.
The current release workflow already builds an unsigned/ad-hoc signed arm64 DMG
on `macos-15` and smoke-tests it on `xcode-27`. Coordinate with the separate signing
work: a test of that artifact does not establish Developer ID/hardened-runtime
compatibility.

## 3. Task ownership and parallel execution

Model names below are explicit subagent assignments. Use `gpt-6.1-sol` for Sol 6.1
and `gpt-6-luna` for Luna 6; set the listed reasoning effort. Spawn with a focused
brief and `fork_turns="none"` when selecting a model override. These are future
execution assignments, not claims that these tasks have already run.

The coordinating agent owns shared contracts, merges, gate decisions and final
verification. Limit concurrency to three worker subagents plus the coordinator.
Give each worker its own branch/worktree when implementing in parallel. Branch
from `develop` using `feature_<topic>`; use the PR template and target `develop`.
Preserve unrelated local changes, including existing untracked planning documents.

| ID | Subtask | Subagent / effort | Depends on | Output / ownership |
| --- | --- | --- | --- | --- |
| A | Pin upstream and investigate timestamp semantics | Sol 6.1 / high | None | Evidence report, revision candidates; no runtime edits |
| B | Probe GitHub macOS runner capabilities | Sol 6.1 / high | None | Standalone manual workflow and capability report |
| C | Prepare public fixtures and scoring specification | Luna 6 / medium | None | Fixture manifest, licenses, expected structural checks |
| D | Run helper/timestamp feasibility comparison | Sol 6.1 / high | A, B, C | Reproduction scripts, output samples, feasibility decision |
| E | Freeze minimal backend/helper contract | Sol 6.1 / high | D passes correctness gate | Short contract recorded in this plan/evidence report |
| F | Implement helper adapter and process lifecycle | Sol 6.1 / high | E | Backend module, focused unit/core tests |
| G | Prepare model registry and lifecycle integration | Luna 6 / high | E | Model manifest and model-management changes/tests |
| H | Implement device resolution, CLI and UI | Sol 6.1 / high | E; integrate after F/G | Settings, orchestration, UI and associated tests |
| I | Build and package native helper | Sol 6.1 / high | E | Build script, PyInstaller changes, native SBOM entries |
| J | Add full runner integration checks and benchmarks | Sol 6.1 / high | F, G, H, I | Functional workflow, benchmark report, packaged smoke tests |
| K | Update user/developer documentation | Luna 6 / medium | E; finalize after J | Installation, model and limitation documentation |
| L | Independent review and release decision | Sol 6.1 / high | J, K | Findings, required fixes, explicit gate verdicts |

Execution waves:

1. A, B and C run in parallel. B can build a provisional pinned revision, but D
   must rerun on the final revision selected by A.
2. D runs after their evidence is combined; E follows the result.
3. F, G and I run in parallel with distinct file ownership. G prepares changes to
   shared files for coordinator integration. No concurrent edits to `uv.lock`,
   `engine.py`, `settings.py` or the release workflow.
4. H integrates the fixed contract after F/G; I can continue independently. K can
   draft documentation in parallel, leaving unverified claims clearly pending.
5. J tests the combined change. K incorporates observed behavior; L reviews it.

Escalate G from Luna to Sol 6.1 / high if it needs a registry-schema redesign,
conversion debugging or changes to integrity policy. Luna should not make those
architectural decisions independently. L should be performed by a fresh reviewer,
not the subagent that implemented the adapter.

## 4. Exploration tasks and feasibility gates

### A — Upstream and timestamp investigation

- Select a release/commit, review its build requirements and license, and record
  exact revision, model conversion provenance and flags. Recheck issue/PR status
  at implementation time; do not build from a moving `master`.
- Distinguish ordinary token timings, `-ml 1` segment splitting, and DTW token
  alignment. Establish which output fields describe start/end intervals, their
  units and time base, and how tokens become words in supported languages.
- Reproduce the VAD/JSON mismatch rather than assuming a closed issue means fixed.
  If a patch is needed, isolate it against the pinned revision, add a failing
  reproduction first, and record why it is necessary. An upstream PR being open
  is not evidence that a released binary contains its fix.
- Inspect DTW's interaction with Flash Attention, Metal, beam search and model
  presets. Check long recordings and chunk boundaries, not just a short sample.
- Deliver a recommendation: usable upstream CLI, narrowly patched CLI, custom
  helper, or stop because reliable word intervals have not been demonstrated.

Keep the investigation and experiment results in a new
`docs/whisper-cpp-evaluation.md`, including exact commands, source/model revisions,
patches and workflow/artifact links. Store larger public-fixture output samples
and machine-readable measurements as workflow artifacts rather than committing
generated transcripts to the source tree.

### B — GitHub runner probe

Create `.github/workflows/whisper-cpp-evaluation.yml` with `workflow_dispatch`,
read-only repository permissions, bounded runtime and artifact retention. Start
on standard `macos-15`; make any larger-runner label a separate, explicitly
selected option subject to account availability and billing. Do not assume the
user has an eligible organization plan or provision a paid runner automatically.

Bootstrap the first run explicitly: GitHub requires the dispatch workflow to
exist on the default branch. If it is not there yet, use a narrowly scoped
temporary push trigger on the experiment branch in the testing fork, or a PR
trigger without secrets. Remove the temporary trigger after validation. Once
registered, dispatch the desired branch via the UI or `gh workflow run ... --ref`.
Do not change the repository's default branch to work around discoverability.
See [GitHub's manual-run instructions](https://docs.github.com/en/actions/how-tos/manage-workflow-runs/manually-run-a-workflow).

Record OS, architecture, CPU, memory, Xcode/image version, Metal devices and
capabilities. Compile and execute a small Metal compute operation, then a real
whisper.cpp inference with GPU requested. Inspect initialization/execution logs
to distinguish an actual Metal run from CPU fallback. Test CPU explicitly too.
An advertised GPU or a successful shader compilation is insufficient evidence.

Emit separate statuses: CPU passed/failed; Metal passed/failed/unavailable.
Missing hardware may skip the exploratory GPU test, but a Metal execution error
on a capable runner is a failure. Retain logs and metadata even after failure.
Never let an unavailable GPU satisfy the production acceleration gate.

If standard runners cannot execute Metal, correctness and packaging work can
continue. A larger-runner probe or remotely hosted physical Mac is then an
external prerequisite for acceleration validation. Do not claim Neural Engine
coverage from this workflow. A build targeting macOS 14 on a newer OS does not
prove runtime compatibility on macOS 14; record that remaining test separately.

### C — Fixtures and expected results

- Reuse suitable `tests/fixtures` audio and add only small licensed/public or
  synthetic fixtures. Keep source/license and checksum records. Private
  evaluation audio, if later supplied, stays on its owner's machine.
- Include English and German speech, a word split into multiple tokens, leading
  silence, long internal silence, trailing silence, silence-only audio, noise,
  punctuation, rapid speaker changes and speech spanning a 30-second boundary.
- Include a short non-space-delimited-language case before claiming broad
  multilingual word grouping. A whitespace-only splitter is insufficient.
- Prepare longer licensed interview material for repeated manual workflow runs;
  keep the regular CI smoke suite small.
- Specify human-checked reference text and word boundaries for a manageable
  subset. Sol validates the scoring specification before D; automatic alignment
  from another engine is a comparison, not ground truth.

### D — Run the feasibility experiment

Build the candidate helper and transcribe a tiny model for structural smoke tests,
then an equivalent production-family model (initial candidate: large-v3-turbo).
Use matching model sources where possible and record precision/quantization.
Download only public test models from Hugging Face; pin revisions/hashes. Use
isolated `ATRAIN_USER_DIR` and cache directories, never the real user model folder.

Compare current CPU faster-whisper beam 5 against whisper.cpp CPU and actual
Metal execution, with word timing and VAD enabled. Add faster-whisper beam 1 only
as a diagnostic. Exercise ordinary timing and DTW separately; keep the exact
decoding options and any unavailable controls in the report.

Explicitly test the VAD time base: prepend a known silence interval and verify
word times shift by that interval within tolerance; repeat with internal gaps.
Test token grouping, finite/bounded timestamps, ordering, empty output and missing
word data. Nonempty recognized text without usable timing must produce a clear
failure, not silently disappear or masquerade as accurately timed words.
Use `len(decoded_audio) / 16000` as the exact duration for boundary checks; the
current `engine.decode()` returns an integer duration and loses fractional seconds.

**Correctness gate:** choose a reproducible configuration that returns usable
word intervals on the original audio timeline and passes the targeted regression
fixtures. If none does, stop production integration and document the blocker.
Do not solve it by inventing word boundaries through uniform text splitting.
If a custom helper is necessary, implement only the experiment first and repeat
this gate; API access alone does not improve the alignment algorithm.

## 5. Implementation subtasks

### E — Define the contract before parallel implementation

Record helper revision/patches, invocation and output schema, timing method,
language/prompt/temperature mappings, VAD model/configuration, executable lookup,
device resolution, precision policy, progress representation and error behavior.

Use an explicit Metal device value rather than reinterpreting the existing CUDA
`GPU` value. Validate backend/device combinations: faster-whisper and Crisper must
not accidentally receive Metal; whisper.cpp Metal must not require `torch.cuda`.
For whisper.cpp, checkpoint quantization is a model property; the current int8/
float16/float32 selector must not imply runtime conversions that do not exist.
Define how old saved settings are migrated/defaulted and what the CLI accepts.

Freeze whether the helper is the upstream CLI or a small wrapper. Prefer file
JSON for results and separate logs/progress, with no local HTTP server. Keep the
contract small enough that an upstream CLI remains usable if it passes D.
Also choose and demonstrate the parent-death cleanup mechanism on macOS before
freezing this choice. The stock CLI passing the timestamp test is insufficient
if it outlives a forcibly killed NiceGUI worker; a wrapper/watchdog may be needed.
Keep this lifecycle mechanism independent of timestamp post-processing.

### F — Adapter and process lifecycle

- Add `WhisperCppTranscriber` using the current engine interface. Resolve only
  the application-owned helper path, not an arbitrary executable from `PATH`.
- Convert already decoded audio into a temporary 16 kHz mono WAV supported by
  the helper; test precision and duration. Use explicit argv, never a shell
  command string. Handle spaces and non-ASCII paths, prompts and filenames.
- Pass verified local model/VAD paths. Inference must not trigger helper-owned
  downloads or depend on external ffmpeg or developer build directories.
- Parse and validate structured results, normalize units, group token pieces
  according to the proven method, then reuse `words_to_segments`. Preserve raw
  spacing/punctuation and detected language. Test JSON/SRT/TXT output downstream.
- Drain process output without pipe deadlocks; provide truthful phase/progress
  reporting. Use an indeterminate phase if the chosen API supplies no reliable
  percentage. Bound retained diagnostics and report nonzero exit, malformed JSON,
  missing results, GPU initialization failure and out-of-memory errors clearly.
- Own the child through `close()` and `finally`: terminate, wait/reap and clean
  temporary files on failure or cancellation. Test interruption of the parent
  process too; a Python `finally` alone cannot handle forced parent termination.
- Avoid the current CUDA-specific `os._exit`/result-handling branches. Do not add
  another Python worker layer solely to launch a native executable. Verify the
  existing NiceGUI process-pool boundary and CLI path both return errors correctly.
- Default recovery is an explicit retry. If Metal failed, a CPU retry uses the
  same checkpoint and records CPU as the effective device; no retry loops.

### G — Models, integrity and availability

Prepare separately named smoke and production GGML entries, with display names
that explain Apple acceleration without exposing internal implementation details.
Runtime mirrors must follow `docs/adding-a-model.md`: maintainers provision the
`aTrain-core` Hugging Face mirror, with pinned source/conversion provenance,
license and exact file hashes. Do not invent repository names, commits or hashes.
Mirror publication requires maintainer access; until available, keep the public
experiment manifest separate from the production registry.

Include any Silero VAD weights as a pinned, licensed artifact in the existing
model lifecycle. Check installed-state detection, incomplete downloads, checksum
failure, removal, offline reuse, and model-list behavior on unsupported platforms.
Review `load all`/initialization behavior so an optional macOS backend does not
cause unnecessary downloads elsewhere. Preserve existing model IDs and files.

### H — Settings, CLI and UI

Make settings depend on the model's JSON backend and runtime capabilities.
Display CPU/Apple GPU appropriately for whisper.cpp and retain existing CUDA
behavior for other backends. Disable irrelevant precision controls and explain
CPU speaker detection. Changing models must invalidate incompatible saved device
or precision choices before a job starts.

Keep heavy native/ML imports out of startup. Probe runtime capability in the
worker/helper; cache only what is safe for display and revalidate before use.
Record requested/effective backend, device, helper version, timing mode and
quantization in job metadata/logs. Update the process dialog so it reports actual
execution rather than the legacy `GPU` storage boolean.

Add CLI validation tests, NiceGUI `user` fixture tests, browser interaction tests
where useful, and click through the running app. Check model download/select,
settings changes, transcription, speaker detection, failure, CPU retry and export.
Do not add a cancellation UI as a side project if none exists at implementation
time; still test cleanup when execution is interrupted or the application exits.

### I — Native build and macOS packaging

Build pinned source via a small reproducible script under `packaging/macos/`.
Prefer a statically linked whisper/ggml core where practical, while verifying all
remaining dylib dependencies and Metal resources. Build arm64 with the macOS 14
deployment target; include helper and resources through `macos_freeze.spec`.

Record compiler/toolchain, build flags, source revision, patch hashes and binary
hashes. Extend the SBOM to cover the native helper, whisper.cpp/ggml and relevant
native dependencies/licenses; a Python-only dependency report misses them.
Test source-run lookup as well as packaged lookup without relying on the build
machine's `PATH`, current directory or Homebrew libraries.

Run architecture/deployment-target and dynamic-library dependency checks. Sign
nested binaries consistently with the app's signing pipeline. Exercise helper
launch and transcription from the final signed bundle once Developer ID signing
is available; ad-hoc smoke success is not that check. Coordinate release workflow
edits with the existing DMG/signing work instead of duplicating it.

## 6. Validation tasks and acceptance criteria

### J — Automated checks and reproducible measurements

| Layer | Tests and location | Required result |
| --- | --- | --- |
| Unit, offline | `tests/unit`: parsing, token grouping, time conversions, settings resolution, helper errors/cleanup using fake processes, registry/platform behavior | Deterministic tests run without a Mac, model downloads or MLX/CUDA; add only necessary lightweight test dependencies to the lean CI job |
| Core, CPU | `tests/core`: real helper, tiny GGML model, public fixture, VAD silence regression, exports and CPU speaker detection | Correct nonempty/empty results as appropriate; original timeline; controlled failures; all model paths isolated |
| macOS helper | Manual evaluation workflow first, then a small CI job on arm64 | Native build and CPU tests pass; Metal capability/execution reported separately |
| Metal | Real inference with timing + VAD, beam settings and logs | Confirmed Metal execution; no disguised CPU fallback; correctness checks pass |
| GUI | `tests/ui`, selected `tests/e2e_browser`, running-app click-through | Compatible controls, truthful progress/device, usable error/retry flow and exports |
| Frozen app | Existing DMG workflow plus focused helper smoke test | Helper launches from bundle, resources resolve offline, same timestamp tests pass |
| Cross-platform | Existing Windows/Linux unit/core checks and import/startup tests | Existing backends remain usable without the new native helper |

Write a failing test before each bug fix. Mock external boundaries for unit tests,
but do not use mocks as evidence of timestamp accuracy or Metal support. For
offline validation, pre-provision models, disable network access for the inference
process, and run both first and subsequent transcriptions. Hub offline flags
alone are insufficient proof that no other network access occurs.

Reuse the existing seams: extend backend dispatch checks in
`tests/core/test_engine.py`, CLI/output smoke patterns in
`tests/core/test_transcription_e2e.py` and `tests/core/test_output_steps.py`, model
interaction coverage in `tests/ui/test_models_interactions.py`, and manifest/SBOM
checks in `tests/unit/test_refresh_model_hashes.py` and
`tests/unit/test_build_sbom.py`. New pure parser/device logic belongs in the unit
suite; do not move or duplicate existing suites just to fit this plan.

Measure fresh-process load time, first-run total time, inference time, audio decode,
VAD/alignment overhead, diarization, export and complete job time. Report real-time
factor as wall seconds / audio seconds. Record peak memory, failures and at least
three repeats; use medians plus spread. Include short clips and long interviews.
Separate any in-process warm benchmark from the actual per-invocation helper
workflow. Record hardware/virtualization, OS, versions, model hashes, precision,
beam/temperature, VAD and Flash Attention/DTW settings with every result.

Proposed gates for the initial supported model/configuration:

- Structural correctness: all targeted timeline, word-grouping, silence and
  export tests pass; no lost recognized text, negative/nonfinite intervals or
  words beyond audio duration. Test repeated jobs and clean recovery after failure.
- Text quality: on fixed English/German reference sets, WER increases by no more
  than 1 absolute percentage point per language against current beam-5 CPU
  faster-whisper. Inspect omissions/repetition individually; aggregate WER does
  not excuse a repeat loop or a missing interview passage.
- Timing quality: on human-annotated matched words, median and p95 absolute
  boundary error each worsen by no more than 50 ms versus the baseline. Also
  report absolute errors and unmatched-word coverage so alignment failures are
  not hidden by excluding difficult words. Inspect speaker-turn attribution.
- Performance: target at least 2x median transcription-stage speedup over the
  current CPU baseline on the selected Metal runner for long recordings, with
  timing/VAD enabled. Publish end-to-end improvement separately. This is a
  proposed acceptance target, not a prediction or a guarantee for all Macs.
- Memory/stability: complete the long fixture and repeated-job test within the
  documented runner memory budget without crashes or accumulation of orphaned
  helpers. Do not infer 8 GB Mac compatibility from a higher-memory VM.
- Distribution: source and frozen-bundle tests pass; signed-bundle behavior and
  minimum-OS runtime coverage are verified or explicitly remain release blockers.

A missed quality gate blocks shipping that configuration. A missed speed target
requires an explicit decision to keep the backend experimental or stop; do not
change the target retroactively. If GPU hardware is unavailable, mark acceleration
unverified and keep the release gate open while completing independent work.

Use repository checks at each implementation PR: ruff check and format check,
Bandit, offline unit tests, and the relevant core/UI/browser suites. Use
`uv sync --locked --extra gui`, install test tooling through the repository's uv
workflow, and run pytest with `uv run --no-sync`. Keep real-model tests separate
from the fast offline unit suite. Upload public-fixture reports/logs/JSON as
workflow artifacts; never upload arbitrary audio or model caches.

### K — Documentation

Update the model-adding guide, source/build instructions, macOS support statement
and relevant verification docs. Describe helper build provenance, model format,
CPU retry, CPU diarization, supported settings, measured limitations and how to
reproduce tests. Update AGENTS.md's CPU-only macOS statement only when acceleration
is implemented. Record useful new pitfalls, especially VAD time bases and the
chosen timestamp/Flash Attention behavior.

### L — Independent review and release decision

Review process ownership, offline inference, local path handling, timestamp fields,
device routing, model integrity, licenses/SBOM, lazy imports and packaged launch.
Repeat only checks justified by findings or new changes. Produce a table of each
gate with passed/failed/unverified, exact workflow/artifact links and remaining
limitations. A green build alone is not a production-readiness verdict.

Suggested PR sequence: (1) manual experiment and evidence; (2) adapter, model and
settings integration with tests; (3) packaging, signed-bundle verification and
documentation. Keep each PR based on `develop`, use the repository PR template,
and do not publish a release as part of an exploration run.

## 7. Upstream evidence to recheck before implementation

These links were inspected on 23 October 2026; issue statuses and runner offerings
may change. Pin the implementation evidence to the chosen source revision.

- [DTW PR #1485](https://github.com/ggml-org/whisper.cpp/pull/1485): merged in March
  2024; discussion covers token alignment and deriving words.
- [Timing discussion #2307](https://github.com/ggml-org/whisper.cpp/discussions/2307):
  historical accuracy/configuration report; not a benchmark of the chosen version.
- [VAD JSON issue #4046](https://github.com/ggml-org/whisper.cpp/issues/4046) and
  [proposed fix #4068](https://github.com/ggml-org/whisper.cpp/pull/4068): both open
  when checked; original-audio versus VAD-compressed token timestamps.
- [whisper.cpp API](https://github.com/ggml-org/whisper.cpp/blob/master/include/whisper.h):
  DTW supplies a separate token timing value, not a ready-made word interval.
- [whisper.cpp implementation](https://github.com/ggml-org/whisper.cpp/blob/master/src/whisper.cpp):
  inspected code disables DTW when Flash Attention is enabled. Verify actual
  behavior in the selected build.
- [GitHub runner images](https://github.com/actions/runner-images) and
  [larger runner specifications](https://docs.github.com/en/actions/reference/runners/larger-runners):
  select available labels and verify compute capabilities in execution. GPU
  advertising and old virtualization reports are not substitutes for the probe.

## 8. Completion checklist

- [ ] A–C: pinned source investigation, runner probe and fixture manifest complete.
- [ ] D: word intervals and VAD timeline validated; helper variant selected.
- [ ] E: interface/device/model contract recorded before parallel runtime edits.
- [ ] F–I: adapter, model management, settings/UI and packaged helper integrated.
- [ ] J: CPU, Metal, offline, timestamp, quality and performance evidence recorded.
- [ ] Minimum macOS 14 and final signing/runtime checks completed or explicitly blocked.
- [ ] K–L: documentation and independent review complete; all release gates resolved.
