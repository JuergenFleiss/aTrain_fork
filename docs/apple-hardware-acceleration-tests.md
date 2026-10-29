# Apple hardware acceleration tests

Results recorded through 23 October 2026. These experiments evaluate candidates
for macOS acceleration; the production transcription backend is unchanged.

| Experiment | Result | Detailed report | Saved results |
| --- | --- | --- | --- |
| whisper.cpp tiny, CPU, with and without VAD/DTW | Serializer patch fixes the gross VAD timeline mapping; word intervals still fail structural checks | [Evaluation](whisper-cpp-evaluation.md) | [Complete aggregate results and German diagnostic](acceleration-test-results/whisper-cpp-tiny.md) |
| whisper.cpp large-v3-turbo, CPU, with and without VAD/DTW | All 45 cases execute; timing instability and overlapping word intervals remain | [Evaluation](whisper-cpp-evaluation.md) | [Complete aggregate results and sequence diagnostic](acceleration-test-results/whisper-cpp-turbo.md) |
| whisper.cpp macOS CPU/Metal capability | CPU inference, Metal compute and actual Metal inference pass on the hosted VM | [Runner report](whisper-cpp-runner-probe.md) | [Successful probe](acceleration-test-results/whisper-cpp-metal.md), [initial classification failure](acceleration-test-results/whisper-cpp-metal-initial.md) |
| MLX large-v3-turbo, native word timestamps | Offline GPU inference works; silence/noise hallucinations and timestamp instability remain | [MLX evaluation](mlx-whisper-evaluation.md) | [First native run](acceleration-test-results/mlx-native.md) |
| MLX large-v3-turbo, paired native/VAD comparison | VAD fixes tested silence/noise hallucinations and long-prefix text; word timing still changes by up to 560 ms in paired shift checks | [MLX evaluation and VAD findings](mlx-whisper-evaluation.md) | [Both runs, VAD spans, word intervals and comparisons](acceleration-test-results/mlx-vad-comparison.md) |

## What these results establish

- GPU execution is demonstrated on a macOS 15.7.9 arm64 hosted VM with an Apple
  Paravirtual GPU. This is not a physical Apple Silicon performance benchmark.
- The whisper.cpp timestamp matrices ran on CPU. The separate Metal probe does
  not establish that those timestamp results were reproduced on Metal.
- Neither tested candidate passes the exploratory **50 ms maximum paired
  timestamp-shift** gate. This measures stability after controlled silence
  changes, not accuracy against human word annotations. Human-reference
  accuracy and production readiness remain unverified.
- VAD can change word alignment through different decoding context even when
  original audio positions are preserved. The MLX experiment retains the
  original timeline; it does not reproduce the whisper.cpp serializer bug.
- The two backends used different decoded PCM bytes. Cross-backend numbers are
  not a controlled accuracy or speed comparison. The paired MLX VAD comparison
  uses identical input assets.

See the [scoring protocol](whisper-cpp-scoring.md) for fixture definitions,
coverage requirements, and the distinction between exploratory stability and
the planned human-reference accuracy gate. Source revisions, model hashes,
dependencies, reproduction commands and remaining limitations are recorded in
the detailed reports above.

## Run register

All remote runs use the testing fork `JuergenFleiss/aTrain_fork`.

| Run | Outcome |
| --- | --- |
| [39920476617](https://github.com/JuergenFleiss/aTrain_fork/actions/runs/39920476617) | Initial whisper.cpp probe falsely classified successful Metal execution as failure; detection corrected and rerun |
| [39921131494](https://github.com/JuergenFleiss/aTrain_fork/actions/runs/39921131494) | Corrected whisper.cpp capability probe passes |
| [39927572399](https://github.com/JuergenFleiss/aTrain_fork/actions/runs/39927572399) | MLX preparation fails because FFmpeg is absent; no inference result; preparation changed to built-in afconvert |
| [39927763560](https://github.com/JuergenFleiss/aTrain_fork/actions/runs/39927763560) | Seven native MLX cases execute; structural scoring fails |
| [39928971580](https://github.com/JuergenFleiss/aTrain_fork/actions/runs/39928971580) | Seven native and seven VAD cases complete; structural scoring still fails; silence/noise intentionally skip ASR when VAD returns no speech |

The Markdown snapshots preserve complete aggregate reports, including per-word
results and recorded diagnostics, plus capability and asset provenance records.
They remain available when the original temporary directories and GitHub
artifacts expire. They are not an archive of every raw log, per-case CLI JSON,
audio file or model binary. Original artifact links are in the detailed reports.
The initial setup failure produced no transcription measurements to archive.

At the end of implementation, 152 offline unit tests passed; Ruff, actionlint
and the isolated dependency-lock check passed. No production application code
or root dependencies were changed for these experiments.
