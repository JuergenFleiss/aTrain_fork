# MLX large-v3-turbo: paired native and VAD runs

[Apple hardware acceleration tests](../apple-hardware-acceleration-tests.md)

Archived on 23 October 2026. The JSON below preserves the complete aggregate
results and listed supporting diagnostics without altering values. Absolute
paths inside these historical records identify the original run environment.
Audio, model binaries and raw execution logs are not embedded. See the index
for interpretation, limitations and links to the original artifacts.

## report.json

Original file SHA-256: `e1444263dd36be755b89d223928f6700b2f214945f1698d3455b0f1a88b7c2a3`

<details>
<summary>Complete recorded result</summary>

```json
{
  "model": {
    "repo": "mlx-community/whisper-large-v3-turbo",
    "revision": "a4aaeec0636e6fef84abdcbe3544cb2bf7e9f6fb",
    "files": {
      "config.json": [
        268,
        "b34fc29e4e11e0a25e812775dd67f4dd16fc2c8eb43d28ae25ff7d660ecb6379"
      ],
      "weights.safetensors": [
        1613977612,
        "951ed3fc1203e6a62467abb2144a96ce7eafca8fa77e3704fdb8635ff3e7f8a6"
      ]
    }
  },
  "host": "macOS-15.7.9-arm64-arm-64bit",
  "machine": "arm64",
  "runner_image": "20260907.0337.1",
  "run_url": "https://github.com/JuergenFleiss/aTrain_fork/actions/runs/39928971580",
  "decoding": "greedy temperature=0, no fallback; beam search unavailable (prior baseline beam=5)",
  "vad": {
    "enabled": false,
    "method": "none; no silence compression",
    "options": null,
    "maximum_speech_duration_s": null,
    "model_sha256": null,
    "context": "condition_on_previous_text=True within each call; context resets across separate spans",
    "upstream_clip_workaround": "one original-time clip per full-waveform call avoids 0.4.3 multi-clip seek-reset defect"
  },
  "alignment": "native word_timestamps=True; cross-attention/CPU DTW; original audio seconds",
  "shift_tolerance_ms": 50,
  "boundary_error_rounding_ms": 1e-06,
  "network": "(version 1) (allow default) (deny network*)",
  "production_correctness_gate": "blocked",
  "unverified": [
    "human boundaries/WER",
    "long interviews/multilingual",
    "macOS 14 execution",
    "production packaging/model-conversion provenance",
    "repeat performance comparison"
  ],
  "fixtures": {
    "base": {
      "text": " And so, my fellow Americans, ask not what your country can do for you, ask what you can do for your country.",
      "words": [
        {
          "text": " And",
          "start_ms": 0.0,
          "end_ms": 520.0
        },
        {
          "text": " so,",
          "start_ms": 520.0,
          "end_ms": 860.0
        },
        {
          "text": " my",
          "start_ms": 1100.0,
          "end_ms": 1200.0
        },
        {
          "text": " fellow",
          "start_ms": 1200.0,
          "end_ms": 1540.0
        },
        {
          "text": " Americans,",
          "start_ms": 1540.0,
          "end_ms": 2120.0
        },
        {
          "text": " ask",
          "start_ms": 3320.0,
          "end_ms": 3780.0
        },
        {
          "text": " not",
          "start_ms": 3780.0,
          "end_ms": 4340.0
        },
        {
          "text": " what",
          "start_ms": 4340.0,
          "end_ms": 5560.0
        },
        {
          "text": " your",
          "start_ms": 5560.0,
          "end_ms": 5800.0
        },
        {
          "text": " country",
          "start_ms": 5800.0,
          "end_ms": 6240.0
        },
        {
          "text": " can",
          "start_ms": 6240.0,
          "end_ms": 6620.0
        },
        {
          "text": " do",
          "start_ms": 6620.0,
          "end_ms": 6820.0
        },
        {
          "text": " for",
          "start_ms": 6820.0,
          "end_ms": 7060.0
        },
        {
          "text": " you,",
          "start_ms": 7060.0,
          "end_ms": 7400.0
        },
        {
          "text": " ask",
          "start_ms": 7780.0,
          "end_ms": 8520.0
        },
        {
          "text": " what",
          "start_ms": 8520.0,
          "end_ms": 8800.0
        },
        {
          "text": " you",
          "start_ms": 8800.0,
          "end_ms": 9060.0
        },
        {
          "text": " can",
          "start_ms": 9060.0,
          "end_ms": 9340.0
        },
        {
          "text": " do",
          "start_ms": 9340.0,
          "end_ms": 9560.0
        },
        {
          "text": " for",
          "start_ms": 9560.0,
          "end_ms": 9780.0
        },
        {
          "text": " your",
          "start_ms": 9780.0,
          "end_ms": 9960.0
        },
        {
          "text": " country.",
          "start_ms": 9960.0,
          "end_ms": 10340.0
        }
      ],
      "problems": [],
      "execution_status": "completed",
      "process_wall_s": 22.564688625000002,
      "command": [
        "/usr/bin/sandbox-exec",
        "-p",
        "(version 1) (allow default) (deny network*)",
        "/Users/runner/work/_temp/mlx-venv/bin/python3",
        "/Users/runner/work/aTrain_fork/aTrain_fork/scripts/mlx_whisper_evaluation/feasibility.py",
        "--worker-output",
        "/Users/runner/work/_temp/mlx-whisper-report/base.json",
        "--speech",
        "/Users/runner/work/_temp/mlx-whisper-work/base.wav",
        "--model-dir",
        "/Users/runner/work/_temp/mlx-whisper-work/model"
      ],
      "worker": {
        "status": "passed",
        "phase": "ASR inference with GPU default; CPU DTW alignment",
        "network_connect_errno": 1,
        "packages": {
          "mlx-whisper": "0.4.3",
          "mlx": "0.32.4",
          "mlx-metal": "0.32.4"
        },
        "default_device": "Device(gpu, 0)",
        "metal_device_info": {
          "device_name": "Apple Paravirtual device",
          "max_recommended_working_set_size": 5010800640,
          "memory_size": 7516192768,
          "architecture": "air64_v27",
          "max_buffer_length": 3758096384,
          "resource_limit": 499000
        },
        "gpu_matmul_conv": "passed",
        "asr_invocations": 1,
        "inference_wall_s": 15.468077916999988,
        "gpu_peak_memory_bytes": 2142867018,
        "result": {
          "text": " And so, my fellow Americans, ask not what your country can do for you, ask what you can do for your country.",
          "segments": [
            {
              "id": 0,
              "seek": 0,
              "start": 0.0,
              "end": 10.34,
              "text": " And so, my fellow Americans, ask not what your country can do for you, ask what you can do for your country.",
              "tokens": [
                50365,
                400,
                370,
                11,
                452,
                7177,
                6280,
                11,
                1029,
                406,
                437,
                428,
                1941,
                393,
                360,
                337,
                291,
                11,
                1029,
                437,
                291,
                393,
                360,
                337,
                428,
                1941,
                13,
                50884
              ],
              "temperature": 0.0,
              "avg_logprob": -0.08435980204878182,
              "compression_ratio": 1.35,
              "no_speech_prob": 6.465813995326641e-11,
              "words": [
                {
                  "word": " And",
                  "start": 0.0,
                  "end": 0.52,
                  "probability": 0.7900390625
                },
                {
                  "word": " so,",
                  "start": 0.52,
                  "end": 0.86,
                  "probability": 0.99560546875
                },
                {
                  "word": " my",
                  "start": 1.1,
                  "end": 1.2,
                  "probability": 0.99853515625
                },
                {
                  "word": " fellow",
                  "start": 1.2,
                  "end": 1.54,
                  "probability": 0.9990234375
                },
                {
                  "word": " Americans,",
                  "start": 1.54,
                  "end": 2.12,
                  "probability": 0.97998046875
                },
                {
                  "word": " ask",
                  "start": 3.32,
                  "end": 3.78,
                  "probability": 0.9873046875
                },
                {
                  "word": " not",
                  "start": 3.78,
                  "end": 4.34,
                  "probability": 0.9794921875
                },
                {
                  "word": " what",
                  "start": 4.34,
                  "end": 5.56,
                  "probability": 0.98779296875
                },
                {
                  "word": " your",
                  "start": 5.56,
                  "end": 5.8,
                  "probability": 0.99560546875
                },
                {
                  "word": " country",
                  "start": 5.8,
                  "end": 6.24,
                  "probability": 0.9990234375
                },
                {
                  "word": " can",
                  "start": 6.24,
                  "end": 6.62,
                  "probability": 0.99951171875
                },
                {
                  "word": " do",
                  "start": 6.62,
                  "end": 6.82,
                  "probability": 0.99951171875
                },
                {
                  "word": " for",
                  "start": 6.82,
                  "end": 7.06,
                  "probability": 0.99951171875
                },
                {
                  "word": " you,",
                  "start": 7.06,
                  "end": 7.4,
                  "probability": 0.99951171875
                },
                {
                  "word": " ask",
                  "start": 7.78,
                  "end": 8.52,
                  "probability": 0.998046875
                },
                {
                  "word": " what",
                  "start": 8.52,
                  "end": 8.8,
                  "probability": 0.99951171875
                },
                {
                  "word": " you",
                  "start": 8.8,
                  "end": 9.06,
                  "probability": 0.9970703125
                },
                {
                  "word": " can",
                  "start": 9.06,
                  "end": 9.34,
                  "probability": 1.0
                },
                {
                  "word": " do",
                  "start": 9.34,
                  "end": 9.56,
                  "probability": 0.99951171875
                },
                {
                  "word": " for",
                  "start": 9.56,
                  "end": 9.78,
                  "probability": 0.99951171875
                },
                {
                  "word": " your",
                  "start": 9.78,
                  "end": 9.96,
                  "probability": 0.99951171875
                },
                {
                  "word": " country.",
                  "start": 9.96,
                  "end": 10.34,
                  "probability": 1.0
                }
              ]
            }
          ],
          "language": "en"
        }
      },
      "sha256": "dc39f0172a8bd64ad53dffcf906c20c175cd5579abd8099869690be6a239563b",
      "samples": 176000,
      "duration_ms": 11000.0,
      "status": "passed"
    },
    "leading": {
      "text": " And so, my fellow Americans, ask not what your country can do for you, ask what you can do for your country.",
      "words": [
        {
          "text": " And",
          "start_ms": 4879.999999999999,
          "end_ms": 5520.0
        },
        {
          "text": " so,",
          "start_ms": 5520.0,
          "end_ms": 5860.0
        },
        {
          "text": " my",
          "start_ms": 6080.0,
          "end_ms": 6200.0
        },
        {
          "text": " fellow",
          "start_ms": 6200.0,
          "end_ms": 6540.0
        },
        {
          "text": " Americans,",
          "start_ms": 6540.0,
          "end_ms": 7120.0
        },
        {
          "text": " ask",
          "start_ms": 7980.0,
          "end_ms": 8780.0
        },
        {
          "text": " not",
          "start_ms": 8780.0,
          "end_ms": 9280.0
        },
        {
          "text": " what",
          "start_ms": 9280.0,
          "end_ms": 10560.0
        },
        {
          "text": " your",
          "start_ms": 10560.0,
          "end_ms": 10800.0
        },
        {
          "text": " country",
          "start_ms": 10800.0,
          "end_ms": 11240.0
        },
        {
          "text": " can",
          "start_ms": 11240.0,
          "end_ms": 11600.0
        },
        {
          "text": " do",
          "start_ms": 11600.0,
          "end_ms": 11820.0
        },
        {
          "text": " for",
          "start_ms": 11820.0,
          "end_ms": 12060.0
        },
        {
          "text": " you,",
          "start_ms": 12060.0,
          "end_ms": 12400.0
        },
        {
          "text": " ask",
          "start_ms": 12700.0,
          "end_ms": 13520.0
        },
        {
          "text": " what",
          "start_ms": 13520.0,
          "end_ms": 13760.0
        },
        {
          "text": " you",
          "start_ms": 13760.0,
          "end_ms": 14040.0
        },
        {
          "text": " can",
          "start_ms": 14040.0,
          "end_ms": 14340.0
        },
        {
          "text": " do",
          "start_ms": 14340.0,
          "end_ms": 14560.0
        },
        {
          "text": " for",
          "start_ms": 14560.0,
          "end_ms": 14780.0
        },
        {
          "text": " your",
          "start_ms": 14780.0,
          "end_ms": 14960.0
        },
        {
          "text": " country.",
          "start_ms": 14960.0,
          "end_ms": 15360.0
        }
      ],
      "problems": [],
      "execution_status": "completed",
      "process_wall_s": 19.999387291999994,
      "command": [
        "/usr/bin/sandbox-exec",
        "-p",
        "(version 1) (allow default) (deny network*)",
        "/Users/runner/work/_temp/mlx-venv/bin/python3",
        "/Users/runner/work/aTrain_fork/aTrain_fork/scripts/mlx_whisper_evaluation/feasibility.py",
        "--worker-output",
        "/Users/runner/work/_temp/mlx-whisper-report/leading.json",
        "--speech",
        "/Users/runner/work/_temp/mlx-whisper-work/leading.wav",
        "--model-dir",
        "/Users/runner/work/_temp/mlx-whisper-work/model"
      ],
      "worker": {
        "status": "passed",
        "phase": "ASR inference with GPU default; CPU DTW alignment",
        "network_connect_errno": 1,
        "packages": {
          "mlx-whisper": "0.4.3",
          "mlx": "0.32.4",
          "mlx-metal": "0.32.4"
        },
        "default_device": "Device(gpu, 0)",
        "metal_device_info": {
          "device_name": "Apple Paravirtual device",
          "max_recommended_working_set_size": 5010800640,
          "memory_size": 7516192768,
          "architecture": "air64_v27",
          "max_buffer_length": 3758096384,
          "resource_limit": 499000
        },
        "gpu_matmul_conv": "passed",
        "asr_invocations": 1,
        "inference_wall_s": 12.603093166999997,
        "gpu_peak_memory_bytes": 2143112782,
        "result": {
          "text": " And so, my fellow Americans, ask not what your country can do for you, ask what you can do for your country.",
          "segments": [
            {
              "id": 0,
              "seek": 0,
              "start": 4.879999999999999,
              "end": 15.36,
              "text": " And so, my fellow Americans, ask not what your country can do for you, ask what you can do for your country.",
              "tokens": [
                50365,
                400,
                370,
                11,
                452,
                7177,
                6280,
                11,
                1029,
                406,
                437,
                428,
                1941,
                393,
                360,
                337,
                291,
                11,
                1029,
                437,
                291,
                393,
                360,
                337,
                428,
                1941,
                13,
                51134
              ],
              "temperature": 0.0,
              "avg_logprob": -0.17851951204497238,
              "compression_ratio": 1.35,
              "no_speech_prob": 1.276031919017484e-10,
              "words": [
                {
                  "word": " And",
                  "start": 4.879999999999999,
                  "end": 5.52,
                  "probability": 0.728515625
                },
                {
                  "word": " so,",
                  "start": 5.52,
                  "end": 5.86,
                  "probability": 0.994140625
                },
                {
                  "word": " my",
                  "start": 6.08,
                  "end": 6.2,
                  "probability": 0.998046875
                },
                {
                  "word": " fellow",
                  "start": 6.2,
                  "end": 6.54,
                  "probability": 0.998046875
                },
                {
                  "word": " Americans,",
                  "start": 6.54,
                  "end": 7.12,
                  "probability": 0.97314453125
                },
                {
                  "word": " ask",
                  "start": 7.98,
                  "end": 8.78,
                  "probability": 0.98388671875
                },
                {
                  "word": " not",
                  "start": 8.78,
                  "end": 9.28,
                  "probability": 0.97119140625
                },
                {
                  "word": " what",
                  "start": 9.28,
                  "end": 10.56,
                  "probability": 0.97900390625
                },
                {
                  "word": " your",
                  "start": 10.56,
                  "end": 10.8,
                  "probability": 0.99365234375
                },
                {
                  "word": " country",
                  "start": 10.8,
                  "end": 11.24,
                  "probability": 0.99853515625
                },
                {
                  "word": " can",
                  "start": 11.24,
                  "end": 11.6,
                  "probability": 0.9990234375
                },
                {
                  "word": " do",
                  "start": 11.6,
                  "end": 11.82,
                  "probability": 0.99951171875
                },
                {
                  "word": " for",
                  "start": 11.82,
                  "end": 12.06,
                  "probability": 0.9990234375
                },
                {
                  "word": " you,",
                  "start": 12.06,
                  "end": 12.4,
                  "probability": 0.99951171875
                },
                {
                  "word": " ask",
                  "start": 12.7,
                  "end": 13.52,
                  "probability": 0.99658203125
                },
                {
                  "word": " what",
                  "start": 13.52,
                  "end": 13.76,
                  "probability": 0.9990234375
                },
                {
                  "word": " you",
                  "start": 13.76,
                  "end": 14.04,
                  "probability": 0.99267578125
                },
                {
                  "word": " can",
                  "start": 14.04,
                  "end": 14.34,
                  "probability": 0.99951171875
                },
                {
                  "word": " do",
                  "start": 14.34,
                  "end": 14.56,
                  "probability": 0.9990234375
                },
                {
                  "word": " for",
                  "start": 14.56,
                  "end": 14.78,
                  "probability": 0.9990234375
                },
                {
                  "word": " your",
                  "start": 14.78,
                  "end": 14.96,
                  "probability": 0.9990234375
                },
                {
                  "word": " country.",
                  "start": 14.96,
                  "end": 15.36,
                  "probability": 0.99951171875
                }
              ]
            }
          ],
          "language": "en"
        }
      },
      "sha256": "a64b845ca89bc1ebd05e6d8f9a22a2f9343dbee3f6bad51d4fa8701e3a9ee12f",
      "samples": 256000,
      "duration_ms": 16000.0,
      "status": "passed"
    },
    "trailing": {
      "text": " And so, my fellow Americans, ask not what your country can do for you, ask what you can do for your country.",
      "words": [
        {
          "text": " And",
          "start_ms": 0.0,
          "end_ms": 520.0
        },
        {
          "text": " so,",
          "start_ms": 520.0,
          "end_ms": 860.0
        },
        {
          "text": " my",
          "start_ms": 1080.0,
          "end_ms": 1200.0
        },
        {
          "text": " fellow",
          "start_ms": 1200.0,
          "end_ms": 1540.0
        },
        {
          "text": " Americans,",
          "start_ms": 1540.0,
          "end_ms": 2120.0
        },
        {
          "text": " ask",
          "start_ms": 2760.0,
          "end_ms": 3780.0
        },
        {
          "text": " not",
          "start_ms": 3780.0,
          "end_ms": 4320.0
        },
        {
          "text": " what",
          "start_ms": 4320.0,
          "end_ms": 5560.0
        },
        {
          "text": " your",
          "start_ms": 5560.0,
          "end_ms": 5800.0
        },
        {
          "text": " country",
          "start_ms": 5800.0,
          "end_ms": 6240.0
        },
        {
          "text": " can",
          "start_ms": 6240.0,
          "end_ms": 6620.0
        },
        {
          "text": " do",
          "start_ms": 6620.0,
          "end_ms": 6820.0
        },
        {
          "text": " for",
          "start_ms": 6820.0,
          "end_ms": 7060.0
        },
        {
          "text": " you,",
          "start_ms": 7060.0,
          "end_ms": 7400.0
        },
        {
          "text": " ask",
          "start_ms": 7760.0,
          "end_ms": 8520.0
        },
        {
          "text": " what",
          "start_ms": 8520.0,
          "end_ms": 8780.0
        },
        {
          "text": " you",
          "start_ms": 8780.0,
          "end_ms": 9040.0
        },
        {
          "text": " can",
          "start_ms": 9040.0,
          "end_ms": 9340.0
        },
        {
          "text": " do",
          "start_ms": 9340.0,
          "end_ms": 9560.0
        },
        {
          "text": " for",
          "start_ms": 9560.0,
          "end_ms": 9780.0
        },
        {
          "text": " your",
          "start_ms": 9780.0,
          "end_ms": 9960.0
        },
        {
          "text": " country.",
          "start_ms": 9960.0,
          "end_ms": 10360.0
        }
      ],
      "problems": [],
      "execution_status": "completed",
      "process_wall_s": 12.126806125000002,
      "command": [
        "/usr/bin/sandbox-exec",
        "-p",
        "(version 1) (allow default) (deny network*)",
        "/Users/runner/work/_temp/mlx-venv/bin/python3",
        "/Users/runner/work/aTrain_fork/aTrain_fork/scripts/mlx_whisper_evaluation/feasibility.py",
        "--worker-output",
        "/Users/runner/work/_temp/mlx-whisper-report/trailing.json",
        "--speech",
        "/Users/runner/work/_temp/mlx-whisper-work/trailing.wav",
        "--model-dir",
        "/Users/runner/work/_temp/mlx-whisper-work/model"
      ],
      "worker": {
        "status": "passed",
        "phase": "ASR inference with GPU default; CPU DTW alignment",
        "network_connect_errno": 1,
        "packages": {
          "mlx-whisper": "0.4.3",
          "mlx": "0.32.4",
          "mlx-metal": "0.32.4"
        },
        "default_device": "Device(gpu, 0)",
        "metal_device_info": {
          "device_name": "Apple Paravirtual device",
          "max_recommended_working_set_size": 5010800640,
          "memory_size": 7516192768,
          "architecture": "air64_v27",
          "max_buffer_length": 3758096384,
          "resource_limit": 499000
        },
        "gpu_matmul_conv": "passed",
        "asr_invocations": 1,
        "inference_wall_s": 9.238174958000002,
        "gpu_peak_memory_bytes": 2143112778,
        "result": {
          "text": " And so, my fellow Americans, ask not what your country can do for you, ask what you can do for your country.",
          "segments": [
            {
              "id": 0,
              "seek": 0,
              "start": 0.0,
              "end": 10.36,
              "text": " And so, my fellow Americans, ask not what your country can do for you, ask what you can do for your country.",
              "tokens": [
                50365,
                400,
                370,
                11,
                452,
                7177,
                6280,
                11,
                1029,
                406,
                437,
                428,
                1941,
                393,
                360,
                337,
                291,
                11,
                1029,
                437,
                291,
                393,
                360,
                337,
                428,
                1941,
                13,
                50884
              ],
              "temperature": 0.0,
              "avg_logprob": -0.0981683402225889,
              "compression_ratio": 1.35,
              "no_speech_prob": 9.971413278409003e-11,
              "words": [
                {
                  "word": " And",
                  "start": 0.0,
                  "end": 0.52,
                  "probability": 0.77294921875
                },
                {
                  "word": " so,",
                  "start": 0.52,
                  "end": 0.86,
                  "probability": 0.99609375
                },
                {
                  "word": " my",
                  "start": 1.08,
                  "end": 1.2,
                  "probability": 0.99853515625
                },
                {
                  "word": " fellow",
                  "start": 1.2,
                  "end": 1.54,
                  "probability": 0.99853515625
                },
                {
                  "word": " Americans,",
                  "start": 1.54,
                  "end": 2.12,
                  "probability": 0.97705078125
                },
                {
                  "word": " ask",
                  "start": 2.76,
                  "end": 3.78,
                  "probability": 0.978515625
                },
                {
                  "word": " not",
                  "start": 3.78,
                  "end": 4.32,
                  "probability": 0.97216796875
                },
                {
                  "word": " what",
                  "start": 4.32,
                  "end": 5.56,
                  "probability": 0.9794921875
                },
                {
                  "word": " your",
                  "start": 5.56,
                  "end": 5.8,
                  "probability": 0.99462890625
                },
                {
                  "word": " country",
                  "start": 5.8,
                  "end": 6.24,
                  "probability": 0.9990234375
                },
                {
                  "word": " can",
                  "start": 6.24,
                  "end": 6.62,
                  "probability": 0.99951171875
                },
                {
                  "word": " do",
                  "start": 6.62,
                  "end": 6.82,
                  "probability": 0.99951171875
                },
                {
                  "word": " for",
                  "start": 6.82,
                  "end": 7.06,
                  "probability": 0.9990234375
                },
                {
                  "word": " you,",
                  "start": 7.06,
                  "end": 7.4,
                  "probability": 0.99951171875
                },
                {
                  "word": " ask",
                  "start": 7.76,
                  "end": 8.52,
                  "probability": 0.99658203125
                },
                {
                  "word": " what",
                  "start": 8.52,
                  "end": 8.78,
                  "probability": 0.9990234375
                },
                {
                  "word": " you",
                  "start": 8.78,
                  "end": 9.04,
                  "probability": 0.9951171875
                },
                {
                  "word": " can",
                  "start": 9.04,
                  "end": 9.34,
                  "probability": 0.99951171875
                },
                {
                  "word": " do",
                  "start": 9.34,
                  "end": 9.56,
                  "probability": 0.99951171875
                },
                {
                  "word": " for",
                  "start": 9.56,
                  "end": 9.78,
                  "probability": 0.99951171875
                },
                {
                  "word": " your",
                  "start": 9.78,
                  "end": 9.96,
                  "probability": 0.9990234375
                },
                {
                  "word": " country.",
                  "start": 9.96,
                  "end": 10.36,
                  "probability": 0.99951171875
                }
              ]
            }
          ],
          "language": "en"
        }
      },
      "sha256": "aec8dc2ae83b2f60307a78f5d75993ce0de0c44616a40f96ee1ba17385634d1e",
      "samples": 256000,
      "duration_ms": 16000.0,
      "status": "passed"
    },
    "internal": {
      "text": " And so, my fellow Americans, ask not what your country can do for you, ask what you can do for your country. And so, my fellow Americans, ask not what your country can do for you, ask what you can do for your country.",
      "words": [
        {
          "text": " And",
          "start_ms": 0.0,
          "end_ms": 520.0
        },
        {
          "text": " so,",
          "start_ms": 520.0,
          "end_ms": 860.0
        },
        {
          "text": " my",
          "start_ms": 1080.0,
          "end_ms": 1200.0
        },
        {
          "text": " fellow",
          "start_ms": 1200.0,
          "end_ms": 1540.0
        },
        {
          "text": " Americans,",
          "start_ms": 1540.0,
          "end_ms": 2120.0
        },
        {
          "text": " ask",
          "start_ms": 2760.0,
          "end_ms": 3780.0
        },
        {
          "text": " not",
          "start_ms": 3780.0,
          "end_ms": 4280.0
        },
        {
          "text": " what",
          "start_ms": 4280.0,
          "end_ms": 5560.0
        },
        {
          "text": " your",
          "start_ms": 5560.0,
          "end_ms": 5780.0
        },
        {
          "text": " country",
          "start_ms": 5780.0,
          "end_ms": 6240.0
        },
        {
          "text": " can",
          "start_ms": 6240.0,
          "end_ms": 6600.0
        },
        {
          "text": " do",
          "start_ms": 6600.0,
          "end_ms": 6820.0
        },
        {
          "text": " for",
          "start_ms": 6820.0,
          "end_ms": 7060.0
        },
        {
          "text": " you,",
          "start_ms": 7060.0,
          "end_ms": 7400.0
        },
        {
          "text": " ask",
          "start_ms": 7680.0,
          "end_ms": 8520.0
        },
        {
          "text": " what",
          "start_ms": 8520.0,
          "end_ms": 8740.0
        },
        {
          "text": " you",
          "start_ms": 8740.0,
          "end_ms": 9040.0
        },
        {
          "text": " can",
          "start_ms": 9040.0,
          "end_ms": 9340.0
        },
        {
          "text": " do",
          "start_ms": 9340.0,
          "end_ms": 9560.0
        },
        {
          "text": " for",
          "start_ms": 9560.0,
          "end_ms": 9780.0
        },
        {
          "text": " your",
          "start_ms": 9780.0,
          "end_ms": 9960.0
        },
        {
          "text": " country.",
          "start_ms": 9960.0,
          "end_ms": 10360.0
        },
        {
          "text": " And",
          "start_ms": 15820.0,
          "end_ms": 16500.0
        },
        {
          "text": " so,",
          "start_ms": 16500.0,
          "end_ms": 16860.0
        },
        {
          "text": " my",
          "start_ms": 17040.0,
          "end_ms": 17180.0
        },
        {
          "text": " fellow",
          "start_ms": 17180.0,
          "end_ms": 17540.0
        },
        {
          "text": " Americans,",
          "start_ms": 17540.0,
          "end_ms": 18100.0
        },
        {
          "text": " ask",
          "start_ms": 19100.0,
          "end_ms": 19780.0
        },
        {
          "text": " not",
          "start_ms": 19780.0,
          "end_ms": 20280.0
        },
        {
          "text": " what",
          "start_ms": 20280.0,
          "end_ms": 21520.0
        },
        {
          "text": " your",
          "start_ms": 21520.0,
          "end_ms": 21760.0
        },
        {
          "text": " country",
          "start_ms": 21760.0,
          "end_ms": 22240.0
        },
        {
          "text": " can",
          "start_ms": 22240.0,
          "end_ms": 22600.0
        },
        {
          "text": " do",
          "start_ms": 22600.0,
          "end_ms": 22820.0
        },
        {
          "text": " for",
          "start_ms": 22820.0,
          "end_ms": 23060.0
        },
        {
          "text": " you,",
          "start_ms": 23060.0,
          "end_ms": 23400.0
        },
        {
          "text": " ask",
          "start_ms": 23800.0,
          "end_ms": 24520.0
        },
        {
          "text": " what",
          "start_ms": 24520.0,
          "end_ms": 24740.0
        },
        {
          "text": " you",
          "start_ms": 24740.0,
          "end_ms": 25040.0
        },
        {
          "text": " can",
          "start_ms": 25040.0,
          "end_ms": 25340.0
        },
        {
          "text": " do",
          "start_ms": 25340.0,
          "end_ms": 25560.0
        },
        {
          "text": " for",
          "start_ms": 25560.0,
          "end_ms": 25780.0
        },
        {
          "text": " your",
          "start_ms": 25780.0,
          "end_ms": 25960.0
        },
        {
          "text": " country.",
          "start_ms": 25960.0,
          "end_ms": 26340.0
        }
      ],
      "problems": [],
      "execution_status": "completed",
      "process_wall_s": 11.339579708999992,
      "command": [
        "/usr/bin/sandbox-exec",
        "-p",
        "(version 1) (allow default) (deny network*)",
        "/Users/runner/work/_temp/mlx-venv/bin/python3",
        "/Users/runner/work/aTrain_fork/aTrain_fork/scripts/mlx_whisper_evaluation/feasibility.py",
        "--worker-output",
        "/Users/runner/work/_temp/mlx-whisper-report/internal.json",
        "--speech",
        "/Users/runner/work/_temp/mlx-whisper-work/internal.wav",
        "--model-dir",
        "/Users/runner/work/_temp/mlx-whisper-work/model"
      ],
      "worker": {
        "status": "passed",
        "phase": "ASR inference with GPU default; CPU DTW alignment",
        "network_connect_errno": 1,
        "packages": {
          "mlx-whisper": "0.4.3",
          "mlx": "0.32.4",
          "mlx-metal": "0.32.4"
        },
        "default_device": "Device(gpu, 0)",
        "metal_device_info": {
          "device_name": "Apple Paravirtual device",
          "max_recommended_working_set_size": 5010800640,
          "memory_size": 7516192768,
          "architecture": "air64_v27",
          "max_buffer_length": 3758096384,
          "resource_limit": 499000
        },
        "gpu_matmul_conv": "passed",
        "asr_invocations": 1,
        "inference_wall_s": 8.470375540999981,
        "gpu_peak_memory_bytes": 2143686438,
        "result": {
          "text": " And so, my fellow Americans, ask not what your country can do for you, ask what you can do for your country. And so, my fellow Americans, ask not what your country can do for you, ask what you can do for your country.",
          "segments": [
            {
              "id": 0,
              "seek": 0,
              "start": 0.0,
              "end": 10.36,
              "text": " And so, my fellow Americans, ask not what your country can do for you, ask what you can do for your country.",
              "tokens": [
                50365,
                400,
                370,
                11,
                452,
                7177,
                6280,
                11,
                1029,
                406,
                437,
                428,
                1941,
                393,
                360,
                337,
                291,
                11,
                1029,
                437,
                291,
                393,
                360,
                337,
                428,
                1941,
                13,
                50884
              ],
              "temperature": 0.0,
              "avg_logprob": -0.10302896666945073,
              "compression_ratio": 2.5232558139534884,
              "no_speech_prob": 9.733853306714835e-11,
              "words": [
                {
                  "word": " And",
                  "start": 0.0,
                  "end": 0.52,
                  "probability": 0.7919921875
                },
                {
                  "word": " so,",
                  "start": 0.52,
                  "end": 0.86,
                  "probability": 0.9951171875
                },
                {
                  "word": " my",
                  "start": 1.08,
                  "end": 1.2,
                  "probability": 0.99853515625
                },
                {
                  "word": " fellow",
                  "start": 1.2,
                  "end": 1.54,
                  "probability": 0.99853515625
                },
                {
                  "word": " Americans,",
                  "start": 1.54,
                  "end": 2.12,
                  "probability": 0.97216796875
                },
                {
                  "word": " ask",
                  "start": 2.76,
                  "end": 3.78,
                  "probability": 0.978515625
                },
                {
                  "word": " not",
                  "start": 3.78,
                  "end": 4.28,
                  "probability": 0.97607421875
                },
                {
                  "word": " what",
                  "start": 4.28,
                  "end": 5.56,
                  "probability": 0.9765625
                },
                {
                  "word": " your",
                  "start": 5.56,
                  "end": 5.78,
                  "probability": 0.99462890625
                },
                {
                  "word": " country",
                  "start": 5.78,
                  "end": 6.24,
                  "probability": 0.9990234375
                },
                {
                  "word": " can",
                  "start": 6.24,
                  "end": 6.6,
                  "probability": 0.99951171875
                },
                {
                  "word": " do",
                  "start": 6.6,
                  "end": 6.82,
                  "probability": 0.99951171875
                },
                {
                  "word": " for",
                  "start": 6.82,
                  "end": 7.06,
                  "probability": 0.9990234375
                },
                {
                  "word": " you,",
                  "start": 7.06,
                  "end": 7.4,
                  "probability": 0.99951171875
                },
                {
                  "word": " ask",
                  "start": 7.68,
                  "end": 8.52,
                  "probability": 0.9970703125
                },
                {
                  "word": " what",
                  "start": 8.52,
                  "end": 8.74,
                  "probability": 0.99951171875
                },
                {
                  "word": " you",
                  "start": 8.74,
                  "end": 9.04,
                  "probability": 0.99755859375
                },
                {
                  "word": " can",
                  "start": 9.04,
                  "end": 9.34,
                  "probability": 0.99951171875
                },
                {
                  "word": " do",
                  "start": 9.34,
                  "end": 9.56,
                  "probability": 0.99951171875
                },
                {
                  "word": " for",
                  "start": 9.56,
                  "end": 9.78,
                  "probability": 0.99951171875
                },
                {
                  "word": " your",
                  "start": 9.78,
                  "end": 9.96,
                  "probability": 0.9990234375
                },
                {
                  "word": " country.",
                  "start": 9.96,
                  "end": 10.36,
                  "probability": 0.99951171875
                }
              ]
            },
            {
              "id": 1,
              "seek": 0,
              "start": 15.82,
              "end": 26.34,
              "text": " And so, my fellow Americans, ask not what your country can do for you, ask what you can do for your country.",
              "tokens": [
                51157,
                400,
                370,
                11,
                452,
                7177,
                6280,
                11,
                1029,
                406,
                437,
                428,
                1941,
                393,
                360,
                337,
                291,
                11,
                1029,
                437,
                291,
                393,
                360,
                337,
                428,
                1941,
                13,
                51684
              ],
              "temperature": 0.0,
              "avg_logprob": -0.10302896666945073,
              "compression_ratio": 2.5232558139534884,
              "no_speech_prob": 9.733853306714835e-11,
              "words": [
                {
                  "word": " And",
                  "start": 15.82,
                  "end": 16.5,
                  "probability": 0.95703125
                },
                {
                  "word": " so,",
                  "start": 16.5,
                  "end": 16.86,
                  "probability": 0.99951171875
                },
                {
                  "word": " my",
                  "start": 17.04,
                  "end": 17.18,
                  "probability": 1.0
                },
                {
                  "word": " fellow",
                  "start": 17.18,
                  "end": 17.54,
                  "probability": 1.0
                },
                {
                  "word": " Americans,",
                  "start": 17.54,
                  "end": 18.1,
                  "probability": 0.998046875
                },
                {
                  "word": " ask",
                  "start": 19.1,
                  "end": 19.78,
                  "probability": 0.99951171875
                },
                {
                  "word": " not",
                  "start": 19.78,
                  "end": 20.28,
                  "probability": 0.99951171875
                },
                {
                  "word": " what",
                  "start": 20.28,
                  "end": 21.52,
                  "probability": 0.9990234375
                },
                {
                  "word": " your",
                  "start": 21.52,
                  "end": 21.76,
                  "probability": 0.9990234375
                },
                {
                  "word": " country",
                  "start": 21.76,
                  "end": 22.24,
                  "probability": 1.0
                },
                {
                  "word": " can",
                  "start": 22.24,
                  "end": 22.6,
                  "probability": 1.0
                },
                {
                  "word": " do",
                  "start": 22.6,
                  "end": 22.82,
                  "probability": 1.0
                },
                {
                  "word": " for",
                  "start": 22.82,
                  "end": 23.06,
                  "probability": 1.0
                },
                {
                  "word": " you,",
                  "start": 23.06,
                  "end": 23.4,
                  "probability": 1.0
                },
                {
                  "word": " ask",
                  "start": 23.8,
                  "end": 24.52,
                  "probability": 0.99951171875
                },
                {
                  "word": " what",
                  "start": 24.52,
                  "end": 24.74,
                  "probability": 1.0
                },
                {
                  "word": " you",
                  "start": 24.74,
                  "end": 25.04,
                  "probability": 1.0
                },
                {
                  "word": " can",
                  "start": 25.04,
                  "end": 25.34,
                  "probability": 1.0
                },
                {
                  "word": " do",
                  "start": 25.34,
                  "end": 25.56,
                  "probability": 1.0
                },
                {
                  "word": " for",
                  "start": 25.56,
                  "end": 25.78,
                  "probability": 1.0
                },
                {
                  "word": " your",
                  "start": 25.78,
                  "end": 25.96,
                  "probability": 1.0
                },
                {
                  "word": " country.",
                  "start": 25.96,
                  "end": 26.34,
                  "probability": 1.0
                }
              ]
            }
          ],
          "language": "en"
        }
      },
      "sha256": "a8096cff33efa366aac97ff43e8fd805684d1c8c5d8e892bb2a90a912d2852b1",
      "samples": 432000,
      "duration_ms": 27000.0,
      "status": "passed"
    },
    "boundary": {
      "text": " The President's President of the United States What your country can do for you, ask what you can do for your country.",
      "words": [
        {
          "text": " The",
          "start_ms": 29800.0,
          "end_ms": 29840.0
        },
        {
          "text": " President's",
          "start_ms": 29840.0,
          "end_ms": 29880.0
        },
        {
          "text": " President",
          "start_ms": 29880.0,
          "end_ms": 29900.0
        },
        {
          "text": " of",
          "start_ms": 29900.0,
          "end_ms": 29920.0
        },
        {
          "text": " the",
          "start_ms": 29920.0,
          "end_ms": 29940.0
        },
        {
          "text": " United",
          "start_ms": 29940.0,
          "end_ms": 29960.0
        },
        {
          "text": " States",
          "start_ms": 29960.0,
          "end_ms": 29980.0
        },
        {
          "text": " What",
          "start_ms": 30000.0,
          "end_ms": 30560.0
        },
        {
          "text": " your",
          "start_ms": 30560.0,
          "end_ms": 30800.0
        },
        {
          "text": " country",
          "start_ms": 30800.0,
          "end_ms": 31240.0
        },
        {
          "text": " can",
          "start_ms": 31240.0,
          "end_ms": 31600.0
        },
        {
          "text": " do",
          "start_ms": 31600.0,
          "end_ms": 31840.0
        },
        {
          "text": " for",
          "start_ms": 31840.0,
          "end_ms": 32060.000000000004
        },
        {
          "text": " you,",
          "start_ms": 32060.000000000004,
          "end_ms": 32439.999999999996
        },
        {
          "text": " ask",
          "start_ms": 32880.0,
          "end_ms": 33520.0
        },
        {
          "text": " what",
          "start_ms": 33520.0,
          "end_ms": 33800.0
        },
        {
          "text": " you",
          "start_ms": 33800.0,
          "end_ms": 34060.0
        },
        {
          "text": " can",
          "start_ms": 34060.0,
          "end_ms": 34340.0
        },
        {
          "text": " do",
          "start_ms": 34340.0,
          "end_ms": 34560.0
        },
        {
          "text": " for",
          "start_ms": 34560.0,
          "end_ms": 34780.0
        },
        {
          "text": " your",
          "start_ms": 34780.0,
          "end_ms": 34960.0
        },
        {
          "text": " country.",
          "start_ms": 34960.0,
          "end_ms": 35360.0
        }
      ],
      "problems": [],
      "execution_status": "completed",
      "process_wall_s": 14.167080374999983,
      "command": [
        "/usr/bin/sandbox-exec",
        "-p",
        "(version 1) (allow default) (deny network*)",
        "/Users/runner/work/_temp/mlx-venv/bin/python3",
        "/Users/runner/work/aTrain_fork/aTrain_fork/scripts/mlx_whisper_evaluation/feasibility.py",
        "--worker-output",
        "/Users/runner/work/_temp/mlx-whisper-report/boundary.json",
        "--speech",
        "/Users/runner/work/_temp/mlx-whisper-work/boundary.wav",
        "--model-dir",
        "/Users/runner/work/_temp/mlx-whisper-work/model"
      ],
      "worker": {
        "status": "passed",
        "phase": "ASR inference with GPU default; CPU DTW alignment",
        "network_connect_errno": 1,
        "packages": {
          "mlx-whisper": "0.4.3",
          "mlx": "0.32.4",
          "mlx-metal": "0.32.4"
        },
        "default_device": "Device(gpu, 0)",
        "metal_device_info": {
          "device_name": "Apple Paravirtual device",
          "max_recommended_working_set_size": 5010800640,
          "memory_size": 7516192768,
          "architecture": "air64_v27",
          "max_buffer_length": 3758096384,
          "resource_limit": 499000
        },
        "gpu_matmul_conv": "passed",
        "asr_invocations": 1,
        "inference_wall_s": 11.168155291000005,
        "gpu_peak_memory_bytes": 2144783714,
        "result": {
          "text": " The President's President of the United States What your country can do for you, ask what you can do for your country.",
          "segments": [
            {
              "id": 0,
              "seek": 0,
              "start": 29.8,
              "end": 29.98,
              "text": " The President's President of the United States",
              "tokens": [
                50365,
                440,
                3117,
                311,
                3117,
                295,
                264,
                2824,
                3040,
                51864
              ],
              "temperature": 0.0,
              "avg_logprob": -1.1293264735828747,
              "compression_ratio": 1.0454545454545454,
              "no_speech_prob": 1.0431434188662436e-10,
              "words": [
                {
                  "word": " The",
                  "start": 29.8,
                  "end": 29.84,
                  "probability": 0.057708740234375
                },
                {
                  "word": " President's",
                  "start": 29.84,
                  "end": 29.88,
                  "probability": 0.1810302734375
                },
                {
                  "word": " President",
                  "start": 29.88,
                  "end": 29.9,
                  "probability": 0.03472900390625
                },
                {
                  "word": " of",
                  "start": 29.9,
                  "end": 29.92,
                  "probability": 0.29443359375
                },
                {
                  "word": " the",
                  "start": 29.92,
                  "end": 29.94,
                  "probability": 0.84814453125
                },
                {
                  "word": " United",
                  "start": 29.94,
                  "end": 29.96,
                  "probability": 0.67724609375
                },
                {
                  "word": " States",
                  "start": 29.96,
                  "end": 29.98,
                  "probability": 0.88232421875
                }
              ]
            },
            {
              "id": 1,
              "seek": 3000,
              "start": 30.0,
              "end": 35.36,
              "text": " What your country can do for you, ask what you can do for your country.",
              "tokens": [
                50365,
                708,
                428,
                1941,
                393,
                360,
                337,
                291,
                11,
                1029,
                437,
                291,
                393,
                360,
                337,
                428,
                1941,
                13,
                50634
              ],
              "temperature": 0.0,
              "avg_logprob": -0.10787842273712159,
              "compression_ratio": 1.3653846153846154,
              "no_speech_prob": 5.64815338596758e-12,
              "words": [
                {
                  "word": " What",
                  "start": 30.0,
                  "end": 30.56,
                  "probability": 0.685546875
                },
                {
                  "word": " your",
                  "start": 30.56,
                  "end": 30.8,
                  "probability": 0.9912109375
                },
                {
                  "word": " country",
                  "start": 30.8,
                  "end": 31.24,
                  "probability": 0.99951171875
                },
                {
                  "word": " can",
                  "start": 31.24,
                  "end": 31.6,
                  "probability": 1.0
                },
                {
                  "word": " do",
                  "start": 31.6,
                  "end": 31.84,
                  "probability": 1.0
                },
                {
                  "word": " for",
                  "start": 31.84,
                  "end": 32.06,
                  "probability": 0.99951171875
                },
                {
                  "word": " you,",
                  "start": 32.06,
                  "end": 32.44,
                  "probability": 0.99951171875
                },
                {
                  "word": " ask",
                  "start": 32.88,
                  "end": 33.52,
                  "probability": 0.9970703125
                },
                {
                  "word": " what",
                  "start": 33.52,
                  "end": 33.8,
                  "probability": 0.99951171875
                },
                {
                  "word": " you",
                  "start": 33.8,
                  "end": 34.06,
                  "probability": 0.99853515625
                },
                {
                  "word": " can",
                  "start": 34.06,
                  "end": 34.34,
                  "probability": 1.0
                },
                {
                  "word": " do",
                  "start": 34.34,
                  "end": 34.56,
                  "probability": 1.0
                },
                {
                  "word": " for",
                  "start": 34.56,
                  "end": 34.78,
                  "probability": 1.0
                },
                {
                  "word": " your",
                  "start": 34.78,
                  "end": 34.96,
                  "probability": 1.0
                },
                {
                  "word": " country.",
                  "start": 34.96,
                  "end": 35.36,
                  "probability": 1.0
                }
              ]
            }
          ],
          "language": "en"
        }
      },
      "sha256": "0dd27774b732cbc838e3480477add3bdaca841e115223840b01b07ed3c86b121",
      "samples": 576000,
      "duration_ms": 36000.0,
      "status": "passed"
    },
    "silence": {
      "text": " Thank you.",
      "words": [
        {
          "text": " Thank",
          "start_ms": 0.0,
          "end_ms": 320.0
        },
        {
          "text": " you.",
          "start_ms": 320.0,
          "end_ms": 7020.0
        }
      ],
      "problems": [
        "recognized text on silence-only fixture"
      ],
      "execution_status": "completed",
      "process_wall_s": 10.947412291999996,
      "command": [
        "/usr/bin/sandbox-exec",
        "-p",
        "(version 1) (allow default) (deny network*)",
        "/Users/runner/work/_temp/mlx-venv/bin/python3",
        "/Users/runner/work/aTrain_fork/aTrain_fork/scripts/mlx_whisper_evaluation/feasibility.py",
        "--worker-output",
        "/Users/runner/work/_temp/mlx-whisper-report/silence.json",
        "--speech",
        "/Users/runner/work/_temp/mlx-whisper-work/silence.wav",
        "--model-dir",
        "/Users/runner/work/_temp/mlx-whisper-work/model"
      ],
      "worker": {
        "status": "passed",
        "phase": "ASR inference with GPU default; CPU DTW alignment",
        "network_connect_errno": 1,
        "packages": {
          "mlx-whisper": "0.4.3",
          "mlx": "0.32.4",
          "mlx-metal": "0.32.4"
        },
        "default_device": "Device(gpu, 0)",
        "metal_device_info": {
          "device_name": "Apple Paravirtual device",
          "max_recommended_working_set_size": 5010800640,
          "memory_size": 7516192768,
          "architecture": "air64_v27",
          "max_buffer_length": 3758096384,
          "resource_limit": 499000
        },
        "gpu_matmul_conv": "passed",
        "asr_invocations": 1,
        "inference_wall_s": 7.904827707999999,
        "gpu_peak_memory_bytes": 2142702906,
        "result": {
          "text": " Thank you.",
          "segments": [
            {
              "id": 0,
              "seek": 0,
              "start": 0.0,
              "end": 7.02,
              "text": " Thank you.",
              "tokens": [
                50365,
                1044,
                291,
                13,
                51864
              ],
              "temperature": 0.0,
              "avg_logprob": -0.2528083324432373,
              "compression_ratio": 0.5555555555555556,
              "no_speech_prob": 9.774109993587743e-11,
              "words": [
                {
                  "word": " Thank",
                  "start": 0.0,
                  "end": 0.32,
                  "probability": 0.1407470703125
                },
                {
                  "word": " you.",
                  "start": 0.32,
                  "end": 7.02,
                  "probability": 0.99853515625
                }
              ]
            }
          ],
          "language": "en"
        }
      },
      "sha256": "190415015d40eef0cd797e1b59ffe00846b01873050b12d44b3a216de3faa2a9",
      "samples": 128000,
      "duration_ms": 8000.0,
      "status": "failed"
    },
    "noise": {
      "text": " so",
      "words": [
        {
          "text": " so",
          "start_ms": 2600.0,
          "end_ms": 4000.0
        }
      ],
      "problems": [
        "recognized text on noise-only fixture"
      ],
      "execution_status": "completed",
      "process_wall_s": 9.088951374999994,
      "command": [
        "/usr/bin/sandbox-exec",
        "-p",
        "(version 1) (allow default) (deny network*)",
        "/Users/runner/work/_temp/mlx-venv/bin/python3",
        "/Users/runner/work/aTrain_fork/aTrain_fork/scripts/mlx_whisper_evaluation/feasibility.py",
        "--worker-output",
        "/Users/runner/work/_temp/mlx-whisper-report/noise.json",
        "--speech",
        "/Users/runner/work/_temp/mlx-whisper-work/noise.wav",
        "--model-dir",
        "/Users/runner/work/_temp/mlx-whisper-work/model"
      ],
      "worker": {
        "status": "passed",
        "phase": "ASR inference with GPU default; CPU DTW alignment",
        "network_connect_errno": 1,
        "packages": {
          "mlx-whisper": "0.4.3",
          "mlx": "0.32.4",
          "mlx-metal": "0.32.4"
        },
        "default_device": "Device(gpu, 0)",
        "metal_device_info": {
          "device_name": "Apple Paravirtual device",
          "max_recommended_working_set_size": 5010800640,
          "memory_size": 7516192768,
          "architecture": "air64_v27",
          "max_buffer_length": 3758096384,
          "resource_limit": 499000
        },
        "gpu_matmul_conv": "passed",
        "asr_invocations": 1,
        "inference_wall_s": 6.220675916999994,
        "gpu_peak_memory_bytes": 2142702890,
        "result": {
          "text": " so",
          "segments": [
            {
              "id": 0,
              "seek": 0,
              "start": 2.6,
              "end": 4.0,
              "text": " so",
              "tokens": [
                50365,
                370,
                50765
              ],
              "temperature": 0.0,
              "avg_logprob": -1.233996868133545,
              "compression_ratio": 0.2,
              "no_speech_prob": 8.810577267759356e-11,
              "words": [
                {
                  "word": " so",
                  "start": 2.6,
                  "end": 4.0,
                  "probability": 0.0750732421875
                }
              ]
            }
          ],
          "language": "en"
        }
      },
      "sha256": "52886be29e412e86511d056ebf565aafd8a3d0430ab9c6a6ea3313b22c455a84",
      "samples": 128000,
      "duration_ms": 8000.0,
      "status": "failed"
    }
  },
  "shift_checks": {
    "leading": {
      "tolerance_ms": 50,
      "matched_words": 22,
      "unmatched_reference_words": 0,
      "unmatched_candidate_words": 0,
      "boundary_errors_ms": [
        120.0,
        0.0,
        0.0,
        0.0,
        20.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        340.0,
        0.0,
        0.0,
        60.0,
        60.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        20.0,
        20.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        80.0,
        0.0,
        0.0,
        40.0,
        40.0,
        20.0,
        20.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        20.0
      ],
      "max_boundary_error_ms": 340.0,
      "median_boundary_error_ms": 0.0,
      "status": "failed"
    },
    "trailing": {
      "tolerance_ms": 50,
      "matched_words": 22,
      "unmatched_reference_words": 0,
      "unmatched_candidate_words": 0,
      "boundary_errors_ms": [
        0.0,
        0.0,
        0.0,
        0.0,
        20.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        560.0,
        0.0,
        0.0,
        20.0,
        20.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        20.0,
        0.0,
        0.0,
        20.0,
        20.0,
        20.0,
        20.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        20.0
      ],
      "max_boundary_error_ms": 560.0,
      "median_boundary_error_ms": 0.0,
      "status": "failed"
    },
    "boundary": {
      "tolerance_ms": 50,
      "matched_words": 15,
      "unmatched_reference_words": 7,
      "unmatched_candidate_words": 7,
      "boundary_errors_ms": [
        660.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        20.0,
        20.0,
        20.0,
        20.0,
        0.0,
        0.0,
        40.0,
        100.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        20.0
      ],
      "max_boundary_error_ms": 660.0,
      "median_boundary_error_ms": 0.0,
      "status": "failed"
    },
    "internal-first": {
      "tolerance_ms": 50,
      "matched_words": 22,
      "unmatched_reference_words": 0,
      "unmatched_candidate_words": 1,
      "boundary_errors_ms": [
        0.0,
        0.0,
        0.0,
        0.0,
        20.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        560.0,
        0.0,
        0.0,
        60.0,
        60.0,
        0.0,
        0.0,
        20.0,
        20.0,
        0.0,
        0.0,
        20.0,
        20.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        100.0,
        0.0,
        0.0,
        60.0,
        60.0,
        20.0,
        20.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        20.0
      ],
      "max_boundary_error_ms": 560.0,
      "median_boundary_error_ms": 0.0,
      "status": "failed"
    },
    "internal-second": {
      "tolerance_ms": 50,
      "matched_words": 21,
      "unmatched_reference_words": 1,
      "unmatched_candidate_words": 0,
      "boundary_errors_ms": [
        20.0,
        0.0,
        60.0,
        20.0,
        20.0,
        0.0,
        0.0,
        20.0,
        220.0,
        0.0,
        0.0,
        60.0,
        60.0,
        40.0,
        40.0,
        40.0,
        40.0,
        0.0,
        0.0,
        20.0,
        20.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        20.0,
        0.0,
        0.0,
        60.0,
        60.0,
        20.0,
        20.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0
      ],
      "max_boundary_error_ms": 220.0,
      "median_boundary_error_ms": 0.0,
      "status": "failed"
    },
    "internal-sequence": {
      "status": "failed",
      "first": {
        "tolerance_ms": 50,
        "matched_words": 22,
        "unmatched_reference_words": 0,
        "unmatched_candidate_words": 0,
        "boundary_errors_ms": [
          0.0,
          0.0,
          0.0,
          0.0,
          20.0,
          0.0,
          0.0,
          0.0,
          0.0,
          0.0,
          560.0,
          0.0,
          0.0,
          60.0,
          60.0,
          0.0,
          0.0,
          20.0,
          20.0,
          0.0,
          0.0,
          20.0,
          20.0,
          0.0,
          0.0,
          0.0,
          0.0,
          0.0,
          100.0,
          0.0,
          0.0,
          60.0,
          60.0,
          20.0,
          20.0,
          0.0,
          0.0,
          0.0,
          0.0,
          0.0,
          0.0,
          0.0,
          0.0,
          20.0
        ],
        "max_boundary_error_ms": 560.0,
        "median_boundary_error_ms": 0.0,
        "status": "failed"
      },
      "second": {
        "tolerance_ms": 50,
        "matched_words": 22,
        "unmatched_reference_words": 0,
        "unmatched_candidate_words": 0,
        "boundary_errors_ms": [
          180.0,
          20.0,
          20.0,
          0.0,
          60.0,
          20.0,
          20.0,
          0.0,
          0.0,
          20.0,
          220.0,
          0.0,
          0.0,
          60.0,
          60.0,
          40.0,
          40.0,
          40.0,
          40.0,
          0.0,
          0.0,
          20.0,
          20.0,
          0.0,
          0.0,
          0.0,
          0.0,
          0.0,
          20.0,
          0.0,
          0.0,
          60.0,
          60.0,
          20.0,
          20.0,
          0.0,
          0.0,
          0.0,
          0.0,
          0.0,
          0.0,
          0.0,
          0.0,
          0.0
        ],
        "max_boundary_error_ms": 220.0,
        "median_boundary_error_ms": 0.0,
        "status": "failed"
      },
      "exact_complete_repeated_sequence": true
    }
  },
  "candidate_structural_status": "failed"
}
```

</details>

## vad/report.json

Original file SHA-256: `128092fe948a2ece4cda78e06d507d74344fc7aa55b056fa3b87151b1f18827b`

<details>
<summary>Complete recorded result</summary>

```json
{
  "model": {
    "repo": "mlx-community/whisper-large-v3-turbo",
    "revision": "a4aaeec0636e6fef84abdcbe3544cb2bf7e9f6fb",
    "files": {
      "config.json": [
        268,
        "b34fc29e4e11e0a25e812775dd67f4dd16fc2c8eb43d28ae25ff7d660ecb6379"
      ],
      "weights.safetensors": [
        1613977612,
        "951ed3fc1203e6a62467abb2144a96ce7eafca8fa77e3704fdb8635ff3e7f8a6"
      ]
    }
  },
  "host": "macOS-15.7.9-arm64-arm-64bit",
  "machine": "arm64",
  "runner_image": "20260907.0337.1",
  "run_url": "https://github.com/JuergenFleiss/aTrain_fork/actions/runs/39928971580",
  "decoding": "greedy temperature=0, no fallback; beam search unavailable (prior baseline beam=5)",
  "vad": {
    "enabled": true,
    "method": "Silero original-timeline clips",
    "options": {
      "threshold": 0.5,
      "neg_threshold": 0.35,
      "min_speech_duration_ms": 0,
      "min_silence_duration_ms": 2000,
      "speech_pad_ms": 400
    },
    "maximum_speech_duration_s": "infinity (upstream default)",
    "model_sha256": "4cbf549b8326f60f80f2536d9eefeb450a9abe83365a098031c89719f1be17d2",
    "context": "condition_on_previous_text=True within each call; context resets across separate spans",
    "upstream_clip_workaround": "one original-time clip per full-waveform call avoids 0.4.3 multi-clip seek-reset defect"
  },
  "alignment": "native word_timestamps=True; cross-attention/CPU DTW; original audio seconds",
  "shift_tolerance_ms": 50,
  "boundary_error_rounding_ms": 1e-06,
  "network": "(version 1) (allow default) (deny network*)",
  "production_correctness_gate": "blocked",
  "unverified": [
    "human boundaries/WER",
    "long interviews/multilingual",
    "macOS 14 execution",
    "production packaging/model-conversion provenance",
    "repeat performance comparison"
  ],
  "fixtures": {
    "base": {
      "text": " And so, my fellow Americans, ask not what your country can do for you, ask what you can do for your country.",
      "words": [
        {
          "text": " And",
          "start_ms": 0.0,
          "end_ms": 520.0
        },
        {
          "text": " so,",
          "start_ms": 520.0,
          "end_ms": 860.0
        },
        {
          "text": " my",
          "start_ms": 1100.0,
          "end_ms": 1200.0
        },
        {
          "text": " fellow",
          "start_ms": 1200.0,
          "end_ms": 1540.0
        },
        {
          "text": " Americans,",
          "start_ms": 1540.0,
          "end_ms": 2120.0
        },
        {
          "text": " ask",
          "start_ms": 3320.0,
          "end_ms": 3780.0
        },
        {
          "text": " not",
          "start_ms": 3780.0,
          "end_ms": 4340.0
        },
        {
          "text": " what",
          "start_ms": 4340.0,
          "end_ms": 5560.0
        },
        {
          "text": " your",
          "start_ms": 5560.0,
          "end_ms": 5800.0
        },
        {
          "text": " country",
          "start_ms": 5800.0,
          "end_ms": 6240.0
        },
        {
          "text": " can",
          "start_ms": 6240.0,
          "end_ms": 6620.0
        },
        {
          "text": " do",
          "start_ms": 6620.0,
          "end_ms": 6820.0
        },
        {
          "text": " for",
          "start_ms": 6820.0,
          "end_ms": 7060.0
        },
        {
          "text": " you,",
          "start_ms": 7060.0,
          "end_ms": 7400.0
        },
        {
          "text": " ask",
          "start_ms": 7780.0,
          "end_ms": 8520.0
        },
        {
          "text": " what",
          "start_ms": 8520.0,
          "end_ms": 8800.0
        },
        {
          "text": " you",
          "start_ms": 8800.0,
          "end_ms": 9060.0
        },
        {
          "text": " can",
          "start_ms": 9060.0,
          "end_ms": 9340.0
        },
        {
          "text": " do",
          "start_ms": 9340.0,
          "end_ms": 9560.0
        },
        {
          "text": " for",
          "start_ms": 9560.0,
          "end_ms": 9780.0
        },
        {
          "text": " your",
          "start_ms": 9780.0,
          "end_ms": 9960.0
        },
        {
          "text": " country.",
          "start_ms": 9960.0,
          "end_ms": 10340.0
        }
      ],
      "problems": [],
      "execution_status": "completed",
      "process_wall_s": 10.158582209000002,
      "command": [
        "/usr/bin/sandbox-exec",
        "-p",
        "(version 1) (allow default) (deny network*)",
        "/Users/runner/work/_temp/mlx-venv/bin/python3",
        "/Users/runner/work/aTrain_fork/aTrain_fork/scripts/mlx_whisper_evaluation/feasibility.py",
        "--worker-output",
        "/Users/runner/work/_temp/mlx-whisper-report/vad/base.json",
        "--speech",
        "/Users/runner/work/_temp/mlx-whisper-work/base.wav",
        "--model-dir",
        "/Users/runner/work/_temp/mlx-whisper-work/model",
        "--vad"
      ],
      "worker": {
        "status": "passed",
        "phase": "ASR inference with GPU default; CPU DTW alignment",
        "network_connect_errno": 1,
        "packages": {
          "mlx-whisper": "0.4.3",
          "mlx": "0.32.4",
          "mlx-metal": "0.32.4"
        },
        "default_device": "Device(gpu, 0)",
        "metal_device_info": {
          "device_name": "Apple Paravirtual device",
          "max_recommended_working_set_size": 5010800640,
          "memory_size": 7516192768,
          "architecture": "air64_v27",
          "max_buffer_length": 3758096384,
          "resource_limit": 499000
        },
        "gpu_matmul_conv": "passed",
        "vad": {
          "packages": {
            "faster-whisper": "1.2.1",
            "onnxruntime": "1.27.0"
          },
          "model_filename": "silero_vad_v6.onnx",
          "model_sha256": "4cbf549b8326f60f80f2536d9eefeb450a9abe83365a098031c89719f1be17d2",
          "source_sha256": "37a9c774aefdd3162d936b896c8dcf5571b2ed938d65bffecfd631770049a18d",
          "options": {
            "threshold": 0.5,
            "neg_threshold": 0.35,
            "min_speech_duration_ms": 0,
            "min_silence_duration_ms": 2000,
            "speech_pad_ms": 400
          },
          "max_speech_duration_s": "infinity (upstream default)",
          "providers": [
            "CPUExecutionProvider"
          ],
          "wall_s": 0.2290176669999937,
          "spans_samples": [
            {
              "start": 0,
              "end": 176000
            }
          ],
          "clip_timestamps_seconds": [
            [
              0.0,
              11.0
            ]
          ],
          "effective_mlx_clip_grid_seconds": [
            [
              0.0,
              11.0
            ]
          ],
          "semantics": "already padded original sample spans; no waveform concatenation or timestamp remapping"
        },
        "native_clip_results": [
          {
            "text": " And so, my fellow Americans, ask not what your country can do for you, ask what you can do for your country.",
            "segments": [
              {
                "id": 0,
                "seek": 0,
                "start": 0.0,
                "end": 10.34,
                "text": " And so, my fellow Americans, ask not what your country can do for you, ask what you can do for your country.",
                "tokens": [
                  50365,
                  400,
                  370,
                  11,
                  452,
                  7177,
                  6280,
                  11,
                  1029,
                  406,
                  437,
                  428,
                  1941,
                  393,
                  360,
                  337,
                  291,
                  11,
                  1029,
                  437,
                  291,
                  393,
                  360,
                  337,
                  428,
                  1941,
                  13,
                  50884
                ],
                "temperature": 0.0,
                "avg_logprob": -0.08435980204878182,
                "compression_ratio": 1.35,
                "no_speech_prob": 6.465813995326641e-11,
                "words": [
                  {
                    "word": " And",
                    "start": 0.0,
                    "end": 0.52,
                    "probability": 0.7900390625
                  },
                  {
                    "word": " so,",
                    "start": 0.52,
                    "end": 0.86,
                    "probability": 0.99560546875
                  },
                  {
                    "word": " my",
                    "start": 1.1,
                    "end": 1.2,
                    "probability": 0.99853515625
                  },
                  {
                    "word": " fellow",
                    "start": 1.2,
                    "end": 1.54,
                    "probability": 0.9990234375
                  },
                  {
                    "word": " Americans,",
                    "start": 1.54,
                    "end": 2.12,
                    "probability": 0.97998046875
                  },
                  {
                    "word": " ask",
                    "start": 3.32,
                    "end": 3.78,
                    "probability": 0.9873046875
                  },
                  {
                    "word": " not",
                    "start": 3.78,
                    "end": 4.34,
                    "probability": 0.9794921875
                  },
                  {
                    "word": " what",
                    "start": 4.34,
                    "end": 5.56,
                    "probability": 0.98779296875
                  },
                  {
                    "word": " your",
                    "start": 5.56,
                    "end": 5.8,
                    "probability": 0.99560546875
                  },
                  {
                    "word": " country",
                    "start": 5.8,
                    "end": 6.24,
                    "probability": 0.9990234375
                  },
                  {
                    "word": " can",
                    "start": 6.24,
                    "end": 6.62,
                    "probability": 0.99951171875
                  },
                  {
                    "word": " do",
                    "start": 6.62,
                    "end": 6.82,
                    "probability": 0.99951171875
                  },
                  {
                    "word": " for",
                    "start": 6.82,
                    "end": 7.06,
                    "probability": 0.99951171875
                  },
                  {
                    "word": " you,",
                    "start": 7.06,
                    "end": 7.4,
                    "probability": 0.99951171875
                  },
                  {
                    "word": " ask",
                    "start": 7.78,
                    "end": 8.52,
                    "probability": 0.998046875
                  },
                  {
                    "word": " what",
                    "start": 8.52,
                    "end": 8.8,
                    "probability": 0.99951171875
                  },
                  {
                    "word": " you",
                    "start": 8.8,
                    "end": 9.06,
                    "probability": 0.9970703125
                  },
                  {
                    "word": " can",
                    "start": 9.06,
                    "end": 9.34,
                    "probability": 1.0
                  },
                  {
                    "word": " do",
                    "start": 9.34,
                    "end": 9.56,
                    "probability": 0.99951171875
                  },
                  {
                    "word": " for",
                    "start": 9.56,
                    "end": 9.78,
                    "probability": 0.99951171875
                  },
                  {
                    "word": " your",
                    "start": 9.78,
                    "end": 9.96,
                    "probability": 0.99951171875
                  },
                  {
                    "word": " country.",
                    "start": 9.96,
                    "end": 10.34,
                    "probability": 1.0
                  }
                ]
              }
            ],
            "language": "en"
          }
        ],
        "asr_invocations": 1,
        "clip_interval_problems": [],
        "inference_wall_s": 6.283866541000009,
        "gpu_peak_memory_bytes": 2142867022,
        "result": {
          "text": " And so, my fellow Americans, ask not what your country can do for you, ask what you can do for your country.",
          "segments": [
            {
              "id": 0,
              "seek": 0,
              "start": 0.0,
              "end": 10.34,
              "text": " And so, my fellow Americans, ask not what your country can do for you, ask what you can do for your country.",
              "tokens": [
                50365,
                400,
                370,
                11,
                452,
                7177,
                6280,
                11,
                1029,
                406,
                437,
                428,
                1941,
                393,
                360,
                337,
                291,
                11,
                1029,
                437,
                291,
                393,
                360,
                337,
                428,
                1941,
                13,
                50884
              ],
              "temperature": 0.0,
              "avg_logprob": -0.08435980204878182,
              "compression_ratio": 1.35,
              "no_speech_prob": 6.465813995326641e-11,
              "words": [
                {
                  "word": " And",
                  "start": 0.0,
                  "end": 0.52,
                  "probability": 0.7900390625
                },
                {
                  "word": " so,",
                  "start": 0.52,
                  "end": 0.86,
                  "probability": 0.99560546875
                },
                {
                  "word": " my",
                  "start": 1.1,
                  "end": 1.2,
                  "probability": 0.99853515625
                },
                {
                  "word": " fellow",
                  "start": 1.2,
                  "end": 1.54,
                  "probability": 0.9990234375
                },
                {
                  "word": " Americans,",
                  "start": 1.54,
                  "end": 2.12,
                  "probability": 0.97998046875
                },
                {
                  "word": " ask",
                  "start": 3.32,
                  "end": 3.78,
                  "probability": 0.9873046875
                },
                {
                  "word": " not",
                  "start": 3.78,
                  "end": 4.34,
                  "probability": 0.9794921875
                },
                {
                  "word": " what",
                  "start": 4.34,
                  "end": 5.56,
                  "probability": 0.98779296875
                },
                {
                  "word": " your",
                  "start": 5.56,
                  "end": 5.8,
                  "probability": 0.99560546875
                },
                {
                  "word": " country",
                  "start": 5.8,
                  "end": 6.24,
                  "probability": 0.9990234375
                },
                {
                  "word": " can",
                  "start": 6.24,
                  "end": 6.62,
                  "probability": 0.99951171875
                },
                {
                  "word": " do",
                  "start": 6.62,
                  "end": 6.82,
                  "probability": 0.99951171875
                },
                {
                  "word": " for",
                  "start": 6.82,
                  "end": 7.06,
                  "probability": 0.99951171875
                },
                {
                  "word": " you,",
                  "start": 7.06,
                  "end": 7.4,
                  "probability": 0.99951171875
                },
                {
                  "word": " ask",
                  "start": 7.78,
                  "end": 8.52,
                  "probability": 0.998046875
                },
                {
                  "word": " what",
                  "start": 8.52,
                  "end": 8.8,
                  "probability": 0.99951171875
                },
                {
                  "word": " you",
                  "start": 8.8,
                  "end": 9.06,
                  "probability": 0.9970703125
                },
                {
                  "word": " can",
                  "start": 9.06,
                  "end": 9.34,
                  "probability": 1.0
                },
                {
                  "word": " do",
                  "start": 9.34,
                  "end": 9.56,
                  "probability": 0.99951171875
                },
                {
                  "word": " for",
                  "start": 9.56,
                  "end": 9.78,
                  "probability": 0.99951171875
                },
                {
                  "word": " your",
                  "start": 9.78,
                  "end": 9.96,
                  "probability": 0.99951171875
                },
                {
                  "word": " country.",
                  "start": 9.96,
                  "end": 10.34,
                  "probability": 1.0
                }
              ]
            }
          ],
          "language": "en"
        }
      },
      "sha256": "dc39f0172a8bd64ad53dffcf906c20c175cd5579abd8099869690be6a239563b",
      "samples": 176000,
      "duration_ms": 11000.0,
      "status": "passed"
    },
    "leading": {
      "text": " And so, my fellow Americans, ask not what your country can do for you, ask what you can do for your country.",
      "words": [
        {
          "text": " And",
          "start_ms": 4940.0,
          "end_ms": 5520.0
        },
        {
          "text": " so,",
          "start_ms": 5520.0,
          "end_ms": 5860.0
        },
        {
          "text": " my",
          "start_ms": 6080.0,
          "end_ms": 6200.0
        },
        {
          "text": " fellow",
          "start_ms": 6200.0,
          "end_ms": 6540.0
        },
        {
          "text": " Americans,",
          "start_ms": 6540.0,
          "end_ms": 7120.0
        },
        {
          "text": " ask",
          "start_ms": 7980.0,
          "end_ms": 8780.0
        },
        {
          "text": " not",
          "start_ms": 8780.0,
          "end_ms": 9340.0
        },
        {
          "text": " what",
          "start_ms": 9340.0,
          "end_ms": 10560.0
        },
        {
          "text": " your",
          "start_ms": 10560.0,
          "end_ms": 10800.0
        },
        {
          "text": " country",
          "start_ms": 10800.0,
          "end_ms": 11240.0
        },
        {
          "text": " can",
          "start_ms": 11240.0,
          "end_ms": 11620.0
        },
        {
          "text": " do",
          "start_ms": 11620.0,
          "end_ms": 11820.0
        },
        {
          "text": " for",
          "start_ms": 11820.0,
          "end_ms": 12060.0
        },
        {
          "text": " you,",
          "start_ms": 12060.0,
          "end_ms": 12400.0
        },
        {
          "text": " ask",
          "start_ms": 12780.0,
          "end_ms": 13520.0
        },
        {
          "text": " what",
          "start_ms": 13520.0,
          "end_ms": 13800.0
        },
        {
          "text": " you",
          "start_ms": 13800.0,
          "end_ms": 14040.0
        },
        {
          "text": " can",
          "start_ms": 14040.0,
          "end_ms": 14340.0
        },
        {
          "text": " do",
          "start_ms": 14340.0,
          "end_ms": 14560.0
        },
        {
          "text": " for",
          "start_ms": 14560.0,
          "end_ms": 14780.0
        },
        {
          "text": " your",
          "start_ms": 14780.0,
          "end_ms": 14960.0
        },
        {
          "text": " country.",
          "start_ms": 14960.0,
          "end_ms": 15340.0
        }
      ],
      "problems": [],
      "execution_status": "completed",
      "process_wall_s": 9.261894791000003,
      "command": [
        "/usr/bin/sandbox-exec",
        "-p",
        "(version 1) (allow default) (deny network*)",
        "/Users/runner/work/_temp/mlx-venv/bin/python3",
        "/Users/runner/work/aTrain_fork/aTrain_fork/scripts/mlx_whisper_evaluation/feasibility.py",
        "--worker-output",
        "/Users/runner/work/_temp/mlx-whisper-report/vad/leading.json",
        "--speech",
        "/Users/runner/work/_temp/mlx-whisper-work/leading.wav",
        "--model-dir",
        "/Users/runner/work/_temp/mlx-whisper-work/model",
        "--vad"
      ],
      "worker": {
        "status": "passed",
        "phase": "ASR inference with GPU default; CPU DTW alignment",
        "network_connect_errno": 1,
        "packages": {
          "mlx-whisper": "0.4.3",
          "mlx": "0.32.4",
          "mlx-metal": "0.32.4"
        },
        "default_device": "Device(gpu, 0)",
        "metal_device_info": {
          "device_name": "Apple Paravirtual device",
          "max_recommended_working_set_size": 5010800640,
          "memory_size": 7516192768,
          "architecture": "air64_v27",
          "max_buffer_length": 3758096384,
          "resource_limit": 499000
        },
        "gpu_matmul_conv": "passed",
        "vad": {
          "packages": {
            "faster-whisper": "1.2.1",
            "onnxruntime": "1.27.0"
          },
          "model_filename": "silero_vad_v6.onnx",
          "model_sha256": "4cbf549b8326f60f80f2536d9eefeb450a9abe83365a098031c89719f1be17d2",
          "source_sha256": "37a9c774aefdd3162d936b896c8dcf5571b2ed938d65bffecfd631770049a18d",
          "options": {
            "threshold": 0.5,
            "neg_threshold": 0.35,
            "min_speech_duration_ms": 0,
            "min_silence_duration_ms": 2000,
            "speech_pad_ms": 400
          },
          "max_speech_duration_s": "infinity (upstream default)",
          "providers": [
            "CPUExecutionProvider"
          ],
          "wall_s": 0.07808245900000088,
          "spans_samples": [
            {
              "start": 79104,
              "end": 256000
            }
          ],
          "clip_timestamps_seconds": [
            [
              4.944,
              16.0
            ]
          ],
          "effective_mlx_clip_grid_seconds": [
            [
              4.94,
              16.0
            ]
          ],
          "semantics": "already padded original sample spans; no waveform concatenation or timestamp remapping"
        },
        "native_clip_results": [
          {
            "text": " And so, my fellow Americans, ask not what your country can do for you, ask what you can do for your country.",
            "segments": [
              {
                "id": 0,
                "seek": 494,
                "start": 4.94,
                "end": 15.34,
                "text": " And so, my fellow Americans, ask not what your country can do for you, ask what you can do for your country.",
                "tokens": [
                  50365,
                  400,
                  370,
                  11,
                  452,
                  7177,
                  6280,
                  11,
                  1029,
                  406,
                  437,
                  428,
                  1941,
                  393,
                  360,
                  337,
                  291,
                  11,
                  1029,
                  437,
                  291,
                  393,
                  360,
                  337,
                  428,
                  1941,
                  13,
                  50887
                ],
                "temperature": 0.0,
                "avg_logprob": -0.07973515576329725,
                "compression_ratio": 1.35,
                "no_speech_prob": 1.0613736278752839e-10,
                "words": [
                  {
                    "word": " And",
                    "start": 4.94,
                    "end": 5.52,
                    "probability": 0.796875
                  },
                  {
                    "word": " so,",
                    "start": 5.52,
                    "end": 5.86,
                    "probability": 0.99609375
                  },
                  {
                    "word": " my",
                    "start": 6.08,
                    "end": 6.2,
                    "probability": 0.9990234375
                  },
                  {
                    "word": " fellow",
                    "start": 6.2,
                    "end": 6.54,
                    "probability": 0.9990234375
                  },
                  {
                    "word": " Americans,",
                    "start": 6.54,
                    "end": 7.12,
                    "probability": 0.98095703125
                  },
                  {
                    "word": " ask",
                    "start": 7.98,
                    "end": 8.78,
                    "probability": 0.98828125
                  },
                  {
                    "word": " not",
                    "start": 8.78,
                    "end": 9.34,
                    "probability": 0.97998046875
                  },
                  {
                    "word": " what",
                    "start": 9.34,
                    "end": 10.56,
                    "probability": 0.9873046875
                  },
                  {
                    "word": " your",
                    "start": 10.56,
                    "end": 10.8,
                    "probability": 0.99658203125
                  },
                  {
                    "word": " country",
                    "start": 10.8,
                    "end": 11.24,
                    "probability": 0.99951171875
                  },
                  {
                    "word": " can",
                    "start": 11.24,
                    "end": 11.62,
                    "probability": 0.99951171875
                  },
                  {
                    "word": " do",
                    "start": 11.62,
                    "end": 11.82,
                    "probability": 0.99951171875
                  },
                  {
                    "word": " for",
                    "start": 11.82,
                    "end": 12.06,
                    "probability": 0.99951171875
                  },
                  {
                    "word": " you,",
                    "start": 12.06,
                    "end": 12.4,
                    "probability": 1.0
                  },
                  {
                    "word": " ask",
                    "start": 12.78,
                    "end": 13.52,
                    "probability": 0.998046875
                  },
                  {
                    "word": " what",
                    "start": 13.52,
                    "end": 13.8,
                    "probability": 0.99951171875
                  },
                  {
                    "word": " you",
                    "start": 13.8,
                    "end": 14.04,
                    "probability": 0.99755859375
                  },
                  {
                    "word": " can",
                    "start": 14.04,
                    "end": 14.34,
                    "probability": 1.0
                  },
                  {
                    "word": " do",
                    "start": 14.34,
                    "end": 14.56,
                    "probability": 0.99951171875
                  },
                  {
                    "word": " for",
                    "start": 14.56,
                    "end": 14.78,
                    "probability": 1.0
                  },
                  {
                    "word": " your",
                    "start": 14.78,
                    "end": 14.96,
                    "probability": 0.99951171875
                  },
                  {
                    "word": " country.",
                    "start": 14.96,
                    "end": 15.34,
                    "probability": 1.0
                  }
                ]
              }
            ],
            "language": "en"
          }
        ],
        "asr_invocations": 1,
        "clip_interval_problems": [],
        "inference_wall_s": 6.590857749999998,
        "gpu_peak_memory_bytes": 2143112782,
        "result": {
          "text": " And so, my fellow Americans, ask not what your country can do for you, ask what you can do for your country.",
          "segments": [
            {
              "id": 0,
              "seek": 494,
              "start": 4.94,
              "end": 15.34,
              "text": " And so, my fellow Americans, ask not what your country can do for you, ask what you can do for your country.",
              "tokens": [
                50365,
                400,
                370,
                11,
                452,
                7177,
                6280,
                11,
                1029,
                406,
                437,
                428,
                1941,
                393,
                360,
                337,
                291,
                11,
                1029,
                437,
                291,
                393,
                360,
                337,
                428,
                1941,
                13,
                50887
              ],
              "temperature": 0.0,
              "avg_logprob": -0.07973515576329725,
              "compression_ratio": 1.35,
              "no_speech_prob": 1.0613736278752839e-10,
              "words": [
                {
                  "word": " And",
                  "start": 4.94,
                  "end": 5.52,
                  "probability": 0.796875
                },
                {
                  "word": " so,",
                  "start": 5.52,
                  "end": 5.86,
                  "probability": 0.99609375
                },
                {
                  "word": " my",
                  "start": 6.08,
                  "end": 6.2,
                  "probability": 0.9990234375
                },
                {
                  "word": " fellow",
                  "start": 6.2,
                  "end": 6.54,
                  "probability": 0.9990234375
                },
                {
                  "word": " Americans,",
                  "start": 6.54,
                  "end": 7.12,
                  "probability": 0.98095703125
                },
                {
                  "word": " ask",
                  "start": 7.98,
                  "end": 8.78,
                  "probability": 0.98828125
                },
                {
                  "word": " not",
                  "start": 8.78,
                  "end": 9.34,
                  "probability": 0.97998046875
                },
                {
                  "word": " what",
                  "start": 9.34,
                  "end": 10.56,
                  "probability": 0.9873046875
                },
                {
                  "word": " your",
                  "start": 10.56,
                  "end": 10.8,
                  "probability": 0.99658203125
                },
                {
                  "word": " country",
                  "start": 10.8,
                  "end": 11.24,
                  "probability": 0.99951171875
                },
                {
                  "word": " can",
                  "start": 11.24,
                  "end": 11.62,
                  "probability": 0.99951171875
                },
                {
                  "word": " do",
                  "start": 11.62,
                  "end": 11.82,
                  "probability": 0.99951171875
                },
                {
                  "word": " for",
                  "start": 11.82,
                  "end": 12.06,
                  "probability": 0.99951171875
                },
                {
                  "word": " you,",
                  "start": 12.06,
                  "end": 12.4,
                  "probability": 1.0
                },
                {
                  "word": " ask",
                  "start": 12.78,
                  "end": 13.52,
                  "probability": 0.998046875
                },
                {
                  "word": " what",
                  "start": 13.52,
                  "end": 13.8,
                  "probability": 0.99951171875
                },
                {
                  "word": " you",
                  "start": 13.8,
                  "end": 14.04,
                  "probability": 0.99755859375
                },
                {
                  "word": " can",
                  "start": 14.04,
                  "end": 14.34,
                  "probability": 1.0
                },
                {
                  "word": " do",
                  "start": 14.34,
                  "end": 14.56,
                  "probability": 0.99951171875
                },
                {
                  "word": " for",
                  "start": 14.56,
                  "end": 14.78,
                  "probability": 1.0
                },
                {
                  "word": " your",
                  "start": 14.78,
                  "end": 14.96,
                  "probability": 0.99951171875
                },
                {
                  "word": " country.",
                  "start": 14.96,
                  "end": 15.34,
                  "probability": 1.0
                }
              ]
            }
          ],
          "language": "en"
        }
      },
      "sha256": "a64b845ca89bc1ebd05e6d8f9a22a2f9343dbee3f6bad51d4fa8701e3a9ee12f",
      "samples": 256000,
      "duration_ms": 16000.0,
      "status": "passed"
    },
    "trailing": {
      "text": " And so, my fellow Americans, ask not what your country can do for you, ask what you can do for your country.",
      "words": [
        {
          "text": " And",
          "start_ms": 0.0,
          "end_ms": 520.0
        },
        {
          "text": " so,",
          "start_ms": 520.0,
          "end_ms": 860.0
        },
        {
          "text": " my",
          "start_ms": 1100.0,
          "end_ms": 1200.0
        },
        {
          "text": " fellow",
          "start_ms": 1200.0,
          "end_ms": 1540.0
        },
        {
          "text": " Americans,",
          "start_ms": 1540.0,
          "end_ms": 2120.0
        },
        {
          "text": " ask",
          "start_ms": 3320.0,
          "end_ms": 3780.0
        },
        {
          "text": " not",
          "start_ms": 3780.0,
          "end_ms": 4340.0
        },
        {
          "text": " what",
          "start_ms": 4340.0,
          "end_ms": 5560.0
        },
        {
          "text": " your",
          "start_ms": 5560.0,
          "end_ms": 5800.0
        },
        {
          "text": " country",
          "start_ms": 5800.0,
          "end_ms": 6240.0
        },
        {
          "text": " can",
          "start_ms": 6240.0,
          "end_ms": 6620.0
        },
        {
          "text": " do",
          "start_ms": 6620.0,
          "end_ms": 6820.0
        },
        {
          "text": " for",
          "start_ms": 6820.0,
          "end_ms": 7060.0
        },
        {
          "text": " you,",
          "start_ms": 7060.0,
          "end_ms": 7400.0
        },
        {
          "text": " ask",
          "start_ms": 7780.0,
          "end_ms": 8520.0
        },
        {
          "text": " what",
          "start_ms": 8520.0,
          "end_ms": 8800.0
        },
        {
          "text": " you",
          "start_ms": 8800.0,
          "end_ms": 9060.0
        },
        {
          "text": " can",
          "start_ms": 9060.0,
          "end_ms": 9340.0
        },
        {
          "text": " do",
          "start_ms": 9340.0,
          "end_ms": 9560.0
        },
        {
          "text": " for",
          "start_ms": 9560.0,
          "end_ms": 9780.0
        },
        {
          "text": " your",
          "start_ms": 9780.0,
          "end_ms": 9960.0
        },
        {
          "text": " country.",
          "start_ms": 9960.0,
          "end_ms": 10340.0
        }
      ],
      "problems": [],
      "execution_status": "completed",
      "process_wall_s": 9.437322749999993,
      "command": [
        "/usr/bin/sandbox-exec",
        "-p",
        "(version 1) (allow default) (deny network*)",
        "/Users/runner/work/_temp/mlx-venv/bin/python3",
        "/Users/runner/work/aTrain_fork/aTrain_fork/scripts/mlx_whisper_evaluation/feasibility.py",
        "--worker-output",
        "/Users/runner/work/_temp/mlx-whisper-report/vad/trailing.json",
        "--speech",
        "/Users/runner/work/_temp/mlx-whisper-work/trailing.wav",
        "--model-dir",
        "/Users/runner/work/_temp/mlx-whisper-work/model",
        "--vad"
      ],
      "worker": {
        "status": "passed",
        "phase": "ASR inference with GPU default; CPU DTW alignment",
        "network_connect_errno": 1,
        "packages": {
          "mlx-whisper": "0.4.3",
          "mlx": "0.32.4",
          "mlx-metal": "0.32.4"
        },
        "default_device": "Device(gpu, 0)",
        "metal_device_info": {
          "device_name": "Apple Paravirtual device",
          "max_recommended_working_set_size": 5010800640,
          "memory_size": 7516192768,
          "architecture": "air64_v27",
          "max_buffer_length": 3758096384,
          "resource_limit": 499000
        },
        "gpu_matmul_conv": "passed",
        "vad": {
          "packages": {
            "faster-whisper": "1.2.1",
            "onnxruntime": "1.27.0"
          },
          "model_filename": "silero_vad_v6.onnx",
          "model_sha256": "4cbf549b8326f60f80f2536d9eefeb450a9abe83365a098031c89719f1be17d2",
          "source_sha256": "37a9c774aefdd3162d936b896c8dcf5571b2ed938d65bffecfd631770049a18d",
          "options": {
            "threshold": 0.5,
            "neg_threshold": 0.35,
            "min_speech_duration_ms": 0,
            "min_silence_duration_ms": 2000,
            "speech_pad_ms": 400
          },
          "max_speech_duration_s": "infinity (upstream default)",
          "providers": [
            "CPUExecutionProvider"
          ],
          "wall_s": 0.15817441600000848,
          "spans_samples": [
            {
              "start": 0,
              "end": 174336
            }
          ],
          "clip_timestamps_seconds": [
            [
              0.0,
              10.896
            ]
          ],
          "effective_mlx_clip_grid_seconds": [
            [
              0.0,
              10.9
            ]
          ],
          "semantics": "already padded original sample spans; no waveform concatenation or timestamp remapping"
        },
        "native_clip_results": [
          {
            "text": " And so, my fellow Americans, ask not what your country can do for you, ask what you can do for your country.",
            "segments": [
              {
                "id": 0,
                "seek": 0,
                "start": 0.0,
                "end": 10.34,
                "text": " And so, my fellow Americans, ask not what your country can do for you, ask what you can do for your country.",
                "tokens": [
                  50365,
                  400,
                  370,
                  11,
                  452,
                  7177,
                  6280,
                  11,
                  1029,
                  406,
                  437,
                  428,
                  1941,
                  393,
                  360,
                  337,
                  291,
                  11,
                  1029,
                  437,
                  291,
                  393,
                  360,
                  337,
                  428,
                  1941,
                  13,
                  50884
                ],
                "temperature": 0.0,
                "avg_logprob": -0.08542664297695818,
                "compression_ratio": 1.35,
                "no_speech_prob": 7.49372647268487e-11,
                "words": [
                  {
                    "word": " And",
                    "start": 0.0,
                    "end": 0.52,
                    "probability": 0.78515625
                  },
                  {
                    "word": " so,",
                    "start": 0.52,
                    "end": 0.86,
                    "probability": 0.99560546875
                  },
                  {
                    "word": " my",
                    "start": 1.1,
                    "end": 1.2,
                    "probability": 0.99853515625
                  },
                  {
                    "word": " fellow",
                    "start": 1.2,
                    "end": 1.54,
                    "probability": 0.9990234375
                  },
                  {
                    "word": " Americans,",
                    "start": 1.54,
                    "end": 2.12,
                    "probability": 0.9794921875
                  },
                  {
                    "word": " ask",
                    "start": 3.32,
                    "end": 3.78,
                    "probability": 0.9873046875
                  },
                  {
                    "word": " not",
                    "start": 3.78,
                    "end": 4.34,
                    "probability": 0.97998046875
                  },
                  {
                    "word": " what",
                    "start": 4.34,
                    "end": 5.56,
                    "probability": 0.98779296875
                  },
                  {
                    "word": " your",
                    "start": 5.56,
                    "end": 5.8,
                    "probability": 0.99560546875
                  },
                  {
                    "word": " country",
                    "start": 5.8,
                    "end": 6.24,
                    "probability": 0.9990234375
                  },
                  {
                    "word": " can",
                    "start": 6.24,
                    "end": 6.62,
                    "probability": 0.99951171875
                  },
                  {
                    "word": " do",
                    "start": 6.62,
                    "end": 6.82,
                    "probability": 0.99951171875
                  },
                  {
                    "word": " for",
                    "start": 6.82,
                    "end": 7.06,
                    "probability": 0.99951171875
                  },
                  {
                    "word": " you,",
                    "start": 7.06,
                    "end": 7.4,
                    "probability": 0.99951171875
                  },
                  {
                    "word": " ask",
                    "start": 7.78,
                    "end": 8.52,
                    "probability": 0.998046875
                  },
                  {
                    "word": " what",
                    "start": 8.52,
                    "end": 8.8,
                    "probability": 0.99951171875
                  },
                  {
                    "word": " you",
                    "start": 8.8,
                    "end": 9.06,
                    "probability": 0.9970703125
                  },
                  {
                    "word": " can",
                    "start": 9.06,
                    "end": 9.34,
                    "probability": 1.0
                  },
                  {
                    "word": " do",
                    "start": 9.34,
                    "end": 9.56,
                    "probability": 0.99951171875
                  },
                  {
                    "word": " for",
                    "start": 9.56,
                    "end": 9.78,
                    "probability": 0.99951171875
                  },
                  {
                    "word": " your",
                    "start": 9.78,
                    "end": 9.96,
                    "probability": 0.99951171875
                  },
                  {
                    "word": " country.",
                    "start": 9.96,
                    "end": 10.34,
                    "probability": 1.0
                  }
                ]
              }
            ],
            "language": "en"
          }
        ],
        "asr_invocations": 1,
        "clip_interval_problems": [],
        "inference_wall_s": 6.510425083999991,
        "gpu_peak_memory_bytes": 2143112782,
        "result": {
          "text": " And so, my fellow Americans, ask not what your country can do for you, ask what you can do for your country.",
          "segments": [
            {
              "id": 0,
              "seek": 0,
              "start": 0.0,
              "end": 10.34,
              "text": " And so, my fellow Americans, ask not what your country can do for you, ask what you can do for your country.",
              "tokens": [
                50365,
                400,
                370,
                11,
                452,
                7177,
                6280,
                11,
                1029,
                406,
                437,
                428,
                1941,
                393,
                360,
                337,
                291,
                11,
                1029,
                437,
                291,
                393,
                360,
                337,
                428,
                1941,
                13,
                50884
              ],
              "temperature": 0.0,
              "avg_logprob": -0.08542664297695818,
              "compression_ratio": 1.35,
              "no_speech_prob": 7.49372647268487e-11,
              "words": [
                {
                  "word": " And",
                  "start": 0.0,
                  "end": 0.52,
                  "probability": 0.78515625
                },
                {
                  "word": " so,",
                  "start": 0.52,
                  "end": 0.86,
                  "probability": 0.99560546875
                },
                {
                  "word": " my",
                  "start": 1.1,
                  "end": 1.2,
                  "probability": 0.99853515625
                },
                {
                  "word": " fellow",
                  "start": 1.2,
                  "end": 1.54,
                  "probability": 0.9990234375
                },
                {
                  "word": " Americans,",
                  "start": 1.54,
                  "end": 2.12,
                  "probability": 0.9794921875
                },
                {
                  "word": " ask",
                  "start": 3.32,
                  "end": 3.78,
                  "probability": 0.9873046875
                },
                {
                  "word": " not",
                  "start": 3.78,
                  "end": 4.34,
                  "probability": 0.97998046875
                },
                {
                  "word": " what",
                  "start": 4.34,
                  "end": 5.56,
                  "probability": 0.98779296875
                },
                {
                  "word": " your",
                  "start": 5.56,
                  "end": 5.8,
                  "probability": 0.99560546875
                },
                {
                  "word": " country",
                  "start": 5.8,
                  "end": 6.24,
                  "probability": 0.9990234375
                },
                {
                  "word": " can",
                  "start": 6.24,
                  "end": 6.62,
                  "probability": 0.99951171875
                },
                {
                  "word": " do",
                  "start": 6.62,
                  "end": 6.82,
                  "probability": 0.99951171875
                },
                {
                  "word": " for",
                  "start": 6.82,
                  "end": 7.06,
                  "probability": 0.99951171875
                },
                {
                  "word": " you,",
                  "start": 7.06,
                  "end": 7.4,
                  "probability": 0.99951171875
                },
                {
                  "word": " ask",
                  "start": 7.78,
                  "end": 8.52,
                  "probability": 0.998046875
                },
                {
                  "word": " what",
                  "start": 8.52,
                  "end": 8.8,
                  "probability": 0.99951171875
                },
                {
                  "word": " you",
                  "start": 8.8,
                  "end": 9.06,
                  "probability": 0.9970703125
                },
                {
                  "word": " can",
                  "start": 9.06,
                  "end": 9.34,
                  "probability": 1.0
                },
                {
                  "word": " do",
                  "start": 9.34,
                  "end": 9.56,
                  "probability": 0.99951171875
                },
                {
                  "word": " for",
                  "start": 9.56,
                  "end": 9.78,
                  "probability": 0.99951171875
                },
                {
                  "word": " your",
                  "start": 9.78,
                  "end": 9.96,
                  "probability": 0.99951171875
                },
                {
                  "word": " country.",
                  "start": 9.96,
                  "end": 10.34,
                  "probability": 1.0
                }
              ]
            }
          ],
          "language": "en"
        }
      },
      "sha256": "aec8dc2ae83b2f60307a78f5d75993ce0de0c44616a40f96ee1ba17385634d1e",
      "samples": 256000,
      "duration_ms": 16000.0,
      "status": "passed"
    },
    "internal": {
      "text": " And so, my fellow Americans, ask not what your country can do for you, ask what you can do for your country. And so, my fellow Americans, ask not what your country can do for you, ask what you can do for your country.",
      "words": [
        {
          "text": " And",
          "start_ms": 0.0,
          "end_ms": 520.0
        },
        {
          "text": " so,",
          "start_ms": 520.0,
          "end_ms": 860.0
        },
        {
          "text": " my",
          "start_ms": 1100.0,
          "end_ms": 1200.0
        },
        {
          "text": " fellow",
          "start_ms": 1200.0,
          "end_ms": 1540.0
        },
        {
          "text": " Americans,",
          "start_ms": 1540.0,
          "end_ms": 2120.0
        },
        {
          "text": " ask",
          "start_ms": 3320.0,
          "end_ms": 3780.0
        },
        {
          "text": " not",
          "start_ms": 3780.0,
          "end_ms": 4340.0
        },
        {
          "text": " what",
          "start_ms": 4340.0,
          "end_ms": 5560.0
        },
        {
          "text": " your",
          "start_ms": 5560.0,
          "end_ms": 5800.0
        },
        {
          "text": " country",
          "start_ms": 5800.0,
          "end_ms": 6240.0
        },
        {
          "text": " can",
          "start_ms": 6240.0,
          "end_ms": 6620.0
        },
        {
          "text": " do",
          "start_ms": 6620.0,
          "end_ms": 6820.0
        },
        {
          "text": " for",
          "start_ms": 6820.0,
          "end_ms": 7060.0
        },
        {
          "text": " you,",
          "start_ms": 7060.0,
          "end_ms": 7400.0
        },
        {
          "text": " ask",
          "start_ms": 7780.0,
          "end_ms": 8520.0
        },
        {
          "text": " what",
          "start_ms": 8520.0,
          "end_ms": 8800.0
        },
        {
          "text": " you",
          "start_ms": 8800.0,
          "end_ms": 9060.0
        },
        {
          "text": " can",
          "start_ms": 9060.0,
          "end_ms": 9340.0
        },
        {
          "text": " do",
          "start_ms": 9340.0,
          "end_ms": 9560.0
        },
        {
          "text": " for",
          "start_ms": 9560.0,
          "end_ms": 9780.0
        },
        {
          "text": " your",
          "start_ms": 9780.0,
          "end_ms": 9960.0
        },
        {
          "text": " country.",
          "start_ms": 9960.0,
          "end_ms": 10340.0
        },
        {
          "text": " And",
          "start_ms": 16270.0,
          "end_ms": 16530.0
        },
        {
          "text": " so,",
          "start_ms": 16530.0,
          "end_ms": 16870.0
        },
        {
          "text": " my",
          "start_ms": 17070.0,
          "end_ms": 17210.0
        },
        {
          "text": " fellow",
          "start_ms": 17210.0,
          "end_ms": 17530.0
        },
        {
          "text": " Americans,",
          "start_ms": 17530.0,
          "end_ms": 18110.0
        },
        {
          "text": " ask",
          "start_ms": 18830.0,
          "end_ms": 19770.0
        },
        {
          "text": " not",
          "start_ms": 19770.0,
          "end_ms": 20290.0
        },
        {
          "text": " what",
          "start_ms": 20290.0,
          "end_ms": 21570.0
        },
        {
          "text": " your",
          "start_ms": 21570.0,
          "end_ms": 21810.0
        },
        {
          "text": " country",
          "start_ms": 21810.0,
          "end_ms": 22250.0
        },
        {
          "text": " can",
          "start_ms": 22250.0,
          "end_ms": 22610.0
        },
        {
          "text": " do",
          "start_ms": 22610.0,
          "end_ms": 22830.0
        },
        {
          "text": " for",
          "start_ms": 22830.0,
          "end_ms": 23070.0
        },
        {
          "text": " you,",
          "start_ms": 23070.0,
          "end_ms": 23410.0
        },
        {
          "text": " ask",
          "start_ms": 23730.0,
          "end_ms": 24510.0
        },
        {
          "text": " what",
          "start_ms": 24510.0,
          "end_ms": 24790.0
        },
        {
          "text": " you",
          "start_ms": 24790.0,
          "end_ms": 25050.0
        },
        {
          "text": " can",
          "start_ms": 25050.0,
          "end_ms": 25350.0
        },
        {
          "text": " do",
          "start_ms": 25350.0,
          "end_ms": 25550.0
        },
        {
          "text": " for",
          "start_ms": 25550.0,
          "end_ms": 25770.0
        },
        {
          "text": " your",
          "start_ms": 25770.0,
          "end_ms": 25970.0
        },
        {
          "text": " country.",
          "start_ms": 25970.0,
          "end_ms": 26350.0
        }
      ],
      "problems": [],
      "execution_status": "completed",
      "process_wall_s": 12.597013250000032,
      "command": [
        "/usr/bin/sandbox-exec",
        "-p",
        "(version 1) (allow default) (deny network*)",
        "/Users/runner/work/_temp/mlx-venv/bin/python3",
        "/Users/runner/work/aTrain_fork/aTrain_fork/scripts/mlx_whisper_evaluation/feasibility.py",
        "--worker-output",
        "/Users/runner/work/_temp/mlx-whisper-report/vad/internal.json",
        "--speech",
        "/Users/runner/work/_temp/mlx-whisper-work/internal.wav",
        "--model-dir",
        "/Users/runner/work/_temp/mlx-whisper-work/model",
        "--vad"
      ],
      "worker": {
        "status": "passed",
        "phase": "ASR inference with GPU default; CPU DTW alignment",
        "network_connect_errno": 1,
        "packages": {
          "mlx-whisper": "0.4.3",
          "mlx": "0.32.4",
          "mlx-metal": "0.32.4"
        },
        "default_device": "Device(gpu, 0)",
        "metal_device_info": {
          "device_name": "Apple Paravirtual device",
          "max_recommended_working_set_size": 5010800640,
          "memory_size": 7516192768,
          "architecture": "air64_v27",
          "max_buffer_length": 3758096384,
          "resource_limit": 499000
        },
        "gpu_matmul_conv": "passed",
        "vad": {
          "packages": {
            "faster-whisper": "1.2.1",
            "onnxruntime": "1.27.0"
          },
          "model_filename": "silero_vad_v6.onnx",
          "model_sha256": "4cbf549b8326f60f80f2536d9eefeb450a9abe83365a098031c89719f1be17d2",
          "source_sha256": "37a9c774aefdd3162d936b896c8dcf5571b2ed938d65bffecfd631770049a18d",
          "options": {
            "threshold": 0.5,
            "neg_threshold": 0.35,
            "min_speech_duration_ms": 0,
            "min_silence_duration_ms": 2000,
            "speech_pad_ms": 400
          },
          "max_speech_duration_s": "infinity (upstream default)",
          "providers": [
            "CPUExecutionProvider"
          ],
          "wall_s": 0.14027187499999627,
          "spans_samples": [
            {
              "start": 0,
              "end": 174336
            },
            {
              "start": 260352,
              "end": 432000
            }
          ],
          "clip_timestamps_seconds": [
            [
              0.0,
              10.896
            ],
            [
              16.272,
              27.0
            ]
          ],
          "effective_mlx_clip_grid_seconds": [
            [
              0.0,
              10.9
            ],
            [
              16.27,
              27.0
            ]
          ],
          "semantics": "already padded original sample spans; no waveform concatenation or timestamp remapping"
        },
        "native_clip_results": [
          {
            "text": " And so, my fellow Americans, ask not what your country can do for you, ask what you can do for your country.",
            "segments": [
              {
                "id": 0,
                "seek": 0,
                "start": 0.0,
                "end": 10.34,
                "text": " And so, my fellow Americans, ask not what your country can do for you, ask what you can do for your country.",
                "tokens": [
                  50365,
                  400,
                  370,
                  11,
                  452,
                  7177,
                  6280,
                  11,
                  1029,
                  406,
                  437,
                  428,
                  1941,
                  393,
                  360,
                  337,
                  291,
                  11,
                  1029,
                  437,
                  291,
                  393,
                  360,
                  337,
                  428,
                  1941,
                  13,
                  50884
                ],
                "temperature": 0.0,
                "avg_logprob": -0.08542664297695818,
                "compression_ratio": 1.35,
                "no_speech_prob": 7.49372647268487e-11,
                "words": [
                  {
                    "word": " And",
                    "start": 0.0,
                    "end": 0.52,
                    "probability": 0.78515625
                  },
                  {
                    "word": " so,",
                    "start": 0.52,
                    "end": 0.86,
                    "probability": 0.99560546875
                  },
                  {
                    "word": " my",
                    "start": 1.1,
                    "end": 1.2,
                    "probability": 0.99853515625
                  },
                  {
                    "word": " fellow",
                    "start": 1.2,
                    "end": 1.54,
                    "probability": 0.9990234375
                  },
                  {
                    "word": " Americans,",
                    "start": 1.54,
                    "end": 2.12,
                    "probability": 0.9794921875
                  },
                  {
                    "word": " ask",
                    "start": 3.32,
                    "end": 3.78,
                    "probability": 0.9873046875
                  },
                  {
                    "word": " not",
                    "start": 3.78,
                    "end": 4.34,
                    "probability": 0.97998046875
                  },
                  {
                    "word": " what",
                    "start": 4.34,
                    "end": 5.56,
                    "probability": 0.98779296875
                  },
                  {
                    "word": " your",
                    "start": 5.56,
                    "end": 5.8,
                    "probability": 0.99560546875
                  },
                  {
                    "word": " country",
                    "start": 5.8,
                    "end": 6.24,
                    "probability": 0.9990234375
                  },
                  {
                    "word": " can",
                    "start": 6.24,
                    "end": 6.62,
                    "probability": 0.99951171875
                  },
                  {
                    "word": " do",
                    "start": 6.62,
                    "end": 6.82,
                    "probability": 0.99951171875
                  },
                  {
                    "word": " for",
                    "start": 6.82,
                    "end": 7.06,
                    "probability": 0.99951171875
                  },
                  {
                    "word": " you,",
                    "start": 7.06,
                    "end": 7.4,
                    "probability": 0.99951171875
                  },
                  {
                    "word": " ask",
                    "start": 7.78,
                    "end": 8.52,
                    "probability": 0.998046875
                  },
                  {
                    "word": " what",
                    "start": 8.52,
                    "end": 8.8,
                    "probability": 0.99951171875
                  },
                  {
                    "word": " you",
                    "start": 8.8,
                    "end": 9.06,
                    "probability": 0.9970703125
                  },
                  {
                    "word": " can",
                    "start": 9.06,
                    "end": 9.34,
                    "probability": 1.0
                  },
                  {
                    "word": " do",
                    "start": 9.34,
                    "end": 9.56,
                    "probability": 0.99951171875
                  },
                  {
                    "word": " for",
                    "start": 9.56,
                    "end": 9.78,
                    "probability": 0.99951171875
                  },
                  {
                    "word": " your",
                    "start": 9.78,
                    "end": 9.96,
                    "probability": 0.99951171875
                  },
                  {
                    "word": " country.",
                    "start": 9.96,
                    "end": 10.34,
                    "probability": 1.0
                  }
                ]
              }
            ],
            "language": "en"
          },
          {
            "text": " And so, my fellow Americans, ask not what your country can do for you, ask what you can do for your country.",
            "segments": [
              {
                "id": 0,
                "seek": 1627,
                "start": 16.27,
                "end": 26.35,
                "text": " And so, my fellow Americans, ask not what your country can do for you, ask what you can do for your country.",
                "tokens": [
                  50365,
                  400,
                  370,
                  11,
                  452,
                  7177,
                  6280,
                  11,
                  1029,
                  406,
                  437,
                  428,
                  1941,
                  393,
                  360,
                  337,
                  291,
                  11,
                  1029,
                  437,
                  291,
                  393,
                  360,
                  337,
                  428,
                  1941,
                  13,
                  50870
                ],
                "temperature": 0.0,
                "avg_logprob": -0.10645277746792497,
                "compression_ratio": 1.35,
                "no_speech_prob": 7.027510517954028e-11,
                "words": [
                  {
                    "word": " And",
                    "start": 16.27,
                    "end": 16.53,
                    "probability": 0.880859375
                  },
                  {
                    "word": " so,",
                    "start": 16.53,
                    "end": 16.87,
                    "probability": 0.998046875
                  },
                  {
                    "word": " my",
                    "start": 17.07,
                    "end": 17.21,
                    "probability": 0.99853515625
                  },
                  {
                    "word": " fellow",
                    "start": 17.21,
                    "end": 17.53,
                    "probability": 0.99951171875
                  },
                  {
                    "word": " Americans,",
                    "start": 17.53,
                    "end": 18.11,
                    "probability": 0.99072265625
                  },
                  {
                    "word": " ask",
                    "start": 18.83,
                    "end": 19.77,
                    "probability": 0.994140625
                  },
                  {
                    "word": " not",
                    "start": 19.77,
                    "end": 20.29,
                    "probability": 0.9931640625
                  },
                  {
                    "word": " what",
                    "start": 20.29,
                    "end": 21.57,
                    "probability": 0.98876953125
                  },
                  {
                    "word": " your",
                    "start": 21.57,
                    "end": 21.81,
                    "probability": 0.99609375
                  },
                  {
                    "word": " country",
                    "start": 21.81,
                    "end": 22.25,
                    "probability": 0.99951171875
                  },
                  {
                    "word": " can",
                    "start": 22.25,
                    "end": 22.61,
                    "probability": 0.99951171875
                  },
                  {
                    "word": " do",
                    "start": 22.61,
                    "end": 22.83,
                    "probability": 0.99951171875
                  },
                  {
                    "word": " for",
                    "start": 22.83,
                    "end": 23.07,
                    "probability": 0.99951171875
                  },
                  {
                    "word": " you,",
                    "start": 23.07,
                    "end": 23.41,
                    "probability": 0.99951171875
                  },
                  {
                    "word": " ask",
                    "start": 23.73,
                    "end": 24.51,
                    "probability": 0.9970703125
                  },
                  {
                    "word": " what",
                    "start": 24.51,
                    "end": 24.79,
                    "probability": 0.99951171875
                  },
                  {
                    "word": " you",
                    "start": 24.79,
                    "end": 25.05,
                    "probability": 0.99658203125
                  },
                  {
                    "word": " can",
                    "start": 25.05,
                    "end": 25.35,
                    "probability": 0.99951171875
                  },
                  {
                    "word": " do",
                    "start": 25.35,
                    "end": 25.55,
                    "probability": 0.99951171875
                  },
                  {
                    "word": " for",
                    "start": 25.55,
                    "end": 25.77,
                    "probability": 0.99951171875
                  },
                  {
                    "word": " your",
                    "start": 25.77,
                    "end": 25.97,
                    "probability": 0.99951171875
                  },
                  {
                    "word": " country.",
                    "start": 25.97,
                    "end": 26.35,
                    "probability": 1.0
                  }
                ]
              }
            ],
            "language": "en"
          }
        ],
        "asr_invocations": 2,
        "clip_interval_problems": [],
        "inference_wall_s": 8.955493999999987,
        "gpu_peak_memory_bytes": 2143686222,
        "result": {
          "text": " And so, my fellow Americans, ask not what your country can do for you, ask what you can do for your country. And so, my fellow Americans, ask not what your country can do for you, ask what you can do for your country.",
          "segments": [
            {
              "id": 0,
              "seek": 0,
              "start": 0.0,
              "end": 10.34,
              "text": " And so, my fellow Americans, ask not what your country can do for you, ask what you can do for your country.",
              "tokens": [
                50365,
                400,
                370,
                11,
                452,
                7177,
                6280,
                11,
                1029,
                406,
                437,
                428,
                1941,
                393,
                360,
                337,
                291,
                11,
                1029,
                437,
                291,
                393,
                360,
                337,
                428,
                1941,
                13,
                50884
              ],
              "temperature": 0.0,
              "avg_logprob": -0.08542664297695818,
              "compression_ratio": 1.35,
              "no_speech_prob": 7.49372647268487e-11,
              "words": [
                {
                  "word": " And",
                  "start": 0.0,
                  "end": 0.52,
                  "probability": 0.78515625
                },
                {
                  "word": " so,",
                  "start": 0.52,
                  "end": 0.86,
                  "probability": 0.99560546875
                },
                {
                  "word": " my",
                  "start": 1.1,
                  "end": 1.2,
                  "probability": 0.99853515625
                },
                {
                  "word": " fellow",
                  "start": 1.2,
                  "end": 1.54,
                  "probability": 0.9990234375
                },
                {
                  "word": " Americans,",
                  "start": 1.54,
                  "end": 2.12,
                  "probability": 0.9794921875
                },
                {
                  "word": " ask",
                  "start": 3.32,
                  "end": 3.78,
                  "probability": 0.9873046875
                },
                {
                  "word": " not",
                  "start": 3.78,
                  "end": 4.34,
                  "probability": 0.97998046875
                },
                {
                  "word": " what",
                  "start": 4.34,
                  "end": 5.56,
                  "probability": 0.98779296875
                },
                {
                  "word": " your",
                  "start": 5.56,
                  "end": 5.8,
                  "probability": 0.99560546875
                },
                {
                  "word": " country",
                  "start": 5.8,
                  "end": 6.24,
                  "probability": 0.9990234375
                },
                {
                  "word": " can",
                  "start": 6.24,
                  "end": 6.62,
                  "probability": 0.99951171875
                },
                {
                  "word": " do",
                  "start": 6.62,
                  "end": 6.82,
                  "probability": 0.99951171875
                },
                {
                  "word": " for",
                  "start": 6.82,
                  "end": 7.06,
                  "probability": 0.99951171875
                },
                {
                  "word": " you,",
                  "start": 7.06,
                  "end": 7.4,
                  "probability": 0.99951171875
                },
                {
                  "word": " ask",
                  "start": 7.78,
                  "end": 8.52,
                  "probability": 0.998046875
                },
                {
                  "word": " what",
                  "start": 8.52,
                  "end": 8.8,
                  "probability": 0.99951171875
                },
                {
                  "word": " you",
                  "start": 8.8,
                  "end": 9.06,
                  "probability": 0.9970703125
                },
                {
                  "word": " can",
                  "start": 9.06,
                  "end": 9.34,
                  "probability": 1.0
                },
                {
                  "word": " do",
                  "start": 9.34,
                  "end": 9.56,
                  "probability": 0.99951171875
                },
                {
                  "word": " for",
                  "start": 9.56,
                  "end": 9.78,
                  "probability": 0.99951171875
                },
                {
                  "word": " your",
                  "start": 9.78,
                  "end": 9.96,
                  "probability": 0.99951171875
                },
                {
                  "word": " country.",
                  "start": 9.96,
                  "end": 10.34,
                  "probability": 1.0
                }
              ]
            },
            {
              "id": 0,
              "seek": 1627,
              "start": 16.27,
              "end": 26.35,
              "text": " And so, my fellow Americans, ask not what your country can do for you, ask what you can do for your country.",
              "tokens": [
                50365,
                400,
                370,
                11,
                452,
                7177,
                6280,
                11,
                1029,
                406,
                437,
                428,
                1941,
                393,
                360,
                337,
                291,
                11,
                1029,
                437,
                291,
                393,
                360,
                337,
                428,
                1941,
                13,
                50870
              ],
              "temperature": 0.0,
              "avg_logprob": -0.10645277746792497,
              "compression_ratio": 1.35,
              "no_speech_prob": 7.027510517954028e-11,
              "words": [
                {
                  "word": " And",
                  "start": 16.27,
                  "end": 16.53,
                  "probability": 0.880859375
                },
                {
                  "word": " so,",
                  "start": 16.53,
                  "end": 16.87,
                  "probability": 0.998046875
                },
                {
                  "word": " my",
                  "start": 17.07,
                  "end": 17.21,
                  "probability": 0.99853515625
                },
                {
                  "word": " fellow",
                  "start": 17.21,
                  "end": 17.53,
                  "probability": 0.99951171875
                },
                {
                  "word": " Americans,",
                  "start": 17.53,
                  "end": 18.11,
                  "probability": 0.99072265625
                },
                {
                  "word": " ask",
                  "start": 18.83,
                  "end": 19.77,
                  "probability": 0.994140625
                },
                {
                  "word": " not",
                  "start": 19.77,
                  "end": 20.29,
                  "probability": 0.9931640625
                },
                {
                  "word": " what",
                  "start": 20.29,
                  "end": 21.57,
                  "probability": 0.98876953125
                },
                {
                  "word": " your",
                  "start": 21.57,
                  "end": 21.81,
                  "probability": 0.99609375
                },
                {
                  "word": " country",
                  "start": 21.81,
                  "end": 22.25,
                  "probability": 0.99951171875
                },
                {
                  "word": " can",
                  "start": 22.25,
                  "end": 22.61,
                  "probability": 0.99951171875
                },
                {
                  "word": " do",
                  "start": 22.61,
                  "end": 22.83,
                  "probability": 0.99951171875
                },
                {
                  "word": " for",
                  "start": 22.83,
                  "end": 23.07,
                  "probability": 0.99951171875
                },
                {
                  "word": " you,",
                  "start": 23.07,
                  "end": 23.41,
                  "probability": 0.99951171875
                },
                {
                  "word": " ask",
                  "start": 23.73,
                  "end": 24.51,
                  "probability": 0.9970703125
                },
                {
                  "word": " what",
                  "start": 24.51,
                  "end": 24.79,
                  "probability": 0.99951171875
                },
                {
                  "word": " you",
                  "start": 24.79,
                  "end": 25.05,
                  "probability": 0.99658203125
                },
                {
                  "word": " can",
                  "start": 25.05,
                  "end": 25.35,
                  "probability": 0.99951171875
                },
                {
                  "word": " do",
                  "start": 25.35,
                  "end": 25.55,
                  "probability": 0.99951171875
                },
                {
                  "word": " for",
                  "start": 25.55,
                  "end": 25.77,
                  "probability": 0.99951171875
                },
                {
                  "word": " your",
                  "start": 25.77,
                  "end": 25.97,
                  "probability": 0.99951171875
                },
                {
                  "word": " country.",
                  "start": 25.97,
                  "end": 26.35,
                  "probability": 1.0
                }
              ]
            }
          ],
          "language": "en"
        }
      },
      "sha256": "a8096cff33efa366aac97ff43e8fd805684d1c8c5d8e892bb2a90a912d2852b1",
      "samples": 432000,
      "duration_ms": 27000.0,
      "status": "passed"
    },
    "boundary": {
      "text": " And so, my fellow Americans, ask not what your country can do for you, ask what you can do for your country.",
      "words": [
        {
          "text": " And",
          "start_ms": 24980.0,
          "end_ms": 25520.0
        },
        {
          "text": " so,",
          "start_ms": 25520.0,
          "end_ms": 25860.0
        },
        {
          "text": " my",
          "start_ms": 26080.0,
          "end_ms": 26200.0
        },
        {
          "text": " fellow",
          "start_ms": 26200.0,
          "end_ms": 26540.0
        },
        {
          "text": " Americans,",
          "start_ms": 26540.0,
          "end_ms": 27120.0
        },
        {
          "text": " ask",
          "start_ms": 27760.0,
          "end_ms": 28780.0
        },
        {
          "text": " not",
          "start_ms": 28780.0,
          "end_ms": 29320.0
        },
        {
          "text": " what",
          "start_ms": 29320.0,
          "end_ms": 30560.0
        },
        {
          "text": " your",
          "start_ms": 30560.0,
          "end_ms": 30800.0
        },
        {
          "text": " country",
          "start_ms": 30800.0,
          "end_ms": 31240.0
        },
        {
          "text": " can",
          "start_ms": 31240.0,
          "end_ms": 31620.0
        },
        {
          "text": " do",
          "start_ms": 31620.0,
          "end_ms": 31820.0
        },
        {
          "text": " for",
          "start_ms": 31820.0,
          "end_ms": 32060.000000000004
        },
        {
          "text": " you,",
          "start_ms": 32060.000000000004,
          "end_ms": 32400.0
        },
        {
          "text": " ask",
          "start_ms": 32780.0,
          "end_ms": 33520.0
        },
        {
          "text": " what",
          "start_ms": 33520.0,
          "end_ms": 33800.0
        },
        {
          "text": " you",
          "start_ms": 33800.0,
          "end_ms": 34040.0
        },
        {
          "text": " can",
          "start_ms": 34040.0,
          "end_ms": 34340.0
        },
        {
          "text": " do",
          "start_ms": 34340.0,
          "end_ms": 34560.0
        },
        {
          "text": " for",
          "start_ms": 34560.0,
          "end_ms": 34780.0
        },
        {
          "text": " your",
          "start_ms": 34780.0,
          "end_ms": 34960.0
        },
        {
          "text": " country.",
          "start_ms": 34960.0,
          "end_ms": 35340.0
        }
      ],
      "problems": [],
      "execution_status": "completed",
      "process_wall_s": 9.712857999999983,
      "command": [
        "/usr/bin/sandbox-exec",
        "-p",
        "(version 1) (allow default) (deny network*)",
        "/Users/runner/work/_temp/mlx-venv/bin/python3",
        "/Users/runner/work/aTrain_fork/aTrain_fork/scripts/mlx_whisper_evaluation/feasibility.py",
        "--worker-output",
        "/Users/runner/work/_temp/mlx-whisper-report/vad/boundary.json",
        "--speech",
        "/Users/runner/work/_temp/mlx-whisper-work/boundary.wav",
        "--model-dir",
        "/Users/runner/work/_temp/mlx-whisper-work/model",
        "--vad"
      ],
      "worker": {
        "status": "passed",
        "phase": "ASR inference with GPU default; CPU DTW alignment",
        "network_connect_errno": 1,
        "packages": {
          "mlx-whisper": "0.4.3",
          "mlx": "0.32.4",
          "mlx-metal": "0.32.4"
        },
        "default_device": "Device(gpu, 0)",
        "metal_device_info": {
          "device_name": "Apple Paravirtual device",
          "max_recommended_working_set_size": 5010800640,
          "memory_size": 7516192768,
          "architecture": "air64_v27",
          "max_buffer_length": 3758096384,
          "resource_limit": 499000
        },
        "gpu_matmul_conv": "passed",
        "vad": {
          "packages": {
            "faster-whisper": "1.2.1",
            "onnxruntime": "1.27.0"
          },
          "model_filename": "silero_vad_v6.onnx",
          "model_sha256": "4cbf549b8326f60f80f2536d9eefeb450a9abe83365a098031c89719f1be17d2",
          "source_sha256": "37a9c774aefdd3162d936b896c8dcf5571b2ed938d65bffecfd631770049a18d",
          "options": {
            "threshold": 0.5,
            "neg_threshold": 0.35,
            "min_speech_duration_ms": 0,
            "min_silence_duration_ms": 2000,
            "speech_pad_ms": 400
          },
          "max_speech_duration_s": "infinity (upstream default)",
          "providers": [
            "CPUExecutionProvider"
          ],
          "wall_s": 0.1584006660000341,
          "spans_samples": [
            {
              "start": 399616,
              "end": 576000
            }
          ],
          "clip_timestamps_seconds": [
            [
              24.976,
              36.0
            ]
          ],
          "effective_mlx_clip_grid_seconds": [
            [
              24.98,
              36.0
            ]
          ],
          "semantics": "already padded original sample spans; no waveform concatenation or timestamp remapping"
        },
        "native_clip_results": [
          {
            "text": " And so, my fellow Americans, ask not what your country can do for you, ask what you can do for your country.",
            "segments": [
              {
                "id": 0,
                "seek": 2498,
                "start": 24.98,
                "end": 35.34,
                "text": " And so, my fellow Americans, ask not what your country can do for you, ask what you can do for your country.",
                "tokens": [
                  50365,
                  400,
                  370,
                  11,
                  452,
                  7177,
                  6280,
                  11,
                  1029,
                  406,
                  437,
                  428,
                  1941,
                  393,
                  360,
                  337,
                  291,
                  11,
                  1029,
                  437,
                  291,
                  393,
                  360,
                  337,
                  428,
                  1941,
                  13,
                  50885
                ],
                "temperature": 0.0,
                "avg_logprob": -0.08409228818169956,
                "compression_ratio": 1.35,
                "no_speech_prob": 9.010058671377053e-11,
                "words": [
                  {
                    "word": " And",
                    "start": 24.98,
                    "end": 25.52,
                    "probability": 0.79052734375
                  },
                  {
                    "word": " so,",
                    "start": 25.52,
                    "end": 25.86,
                    "probability": 0.99560546875
                  },
                  {
                    "word": " my",
                    "start": 26.08,
                    "end": 26.2,
                    "probability": 0.99853515625
                  },
                  {
                    "word": " fellow",
                    "start": 26.2,
                    "end": 26.54,
                    "probability": 0.9990234375
                  },
                  {
                    "word": " Americans,",
                    "start": 26.54,
                    "end": 27.12,
                    "probability": 0.978515625
                  },
                  {
                    "word": " ask",
                    "start": 27.76,
                    "end": 28.78,
                    "probability": 0.98583984375
                  },
                  {
                    "word": " not",
                    "start": 28.78,
                    "end": 29.32,
                    "probability": 0.97998046875
                  },
                  {
                    "word": " what",
                    "start": 29.32,
                    "end": 30.56,
                    "probability": 0.98681640625
                  },
                  {
                    "word": " your",
                    "start": 30.56,
                    "end": 30.8,
                    "probability": 0.99609375
                  },
                  {
                    "word": " country",
                    "start": 30.8,
                    "end": 31.24,
                    "probability": 0.9990234375
                  },
                  {
                    "word": " can",
                    "start": 31.24,
                    "end": 31.62,
                    "probability": 0.99951171875
                  },
                  {
                    "word": " do",
                    "start": 31.62,
                    "end": 31.82,
                    "probability": 0.99951171875
                  },
                  {
                    "word": " for",
                    "start": 31.82,
                    "end": 32.06,
                    "probability": 0.99951171875
                  },
                  {
                    "word": " you,",
                    "start": 32.06,
                    "end": 32.4,
                    "probability": 1.0
                  },
                  {
                    "word": " ask",
                    "start": 32.78,
                    "end": 33.52,
                    "probability": 0.998046875
                  },
                  {
                    "word": " what",
                    "start": 33.52,
                    "end": 33.8,
                    "probability": 0.99951171875
                  },
                  {
                    "word": " you",
                    "start": 33.8,
                    "end": 34.04,
                    "probability": 0.9970703125
                  },
                  {
                    "word": " can",
                    "start": 34.04,
                    "end": 34.34,
                    "probability": 1.0
                  },
                  {
                    "word": " do",
                    "start": 34.34,
                    "end": 34.56,
                    "probability": 0.99951171875
                  },
                  {
                    "word": " for",
                    "start": 34.56,
                    "end": 34.78,
                    "probability": 0.99951171875
                  },
                  {
                    "word": " your",
                    "start": 34.78,
                    "end": 34.96,
                    "probability": 0.99951171875
                  },
                  {
                    "word": " country.",
                    "start": 34.96,
                    "end": 35.34,
                    "probability": 1.0
                  }
                ]
              }
            ],
            "language": "en"
          }
        ],
        "asr_invocations": 1,
        "clip_interval_problems": [],
        "inference_wall_s": 6.656908166999983,
        "gpu_peak_memory_bytes": 2144144974,
        "result": {
          "text": " And so, my fellow Americans, ask not what your country can do for you, ask what you can do for your country.",
          "segments": [
            {
              "id": 0,
              "seek": 2498,
              "start": 24.98,
              "end": 35.34,
              "text": " And so, my fellow Americans, ask not what your country can do for you, ask what you can do for your country.",
              "tokens": [
                50365,
                400,
                370,
                11,
                452,
                7177,
                6280,
                11,
                1029,
                406,
                437,
                428,
                1941,
                393,
                360,
                337,
                291,
                11,
                1029,
                437,
                291,
                393,
                360,
                337,
                428,
                1941,
                13,
                50885
              ],
              "temperature": 0.0,
              "avg_logprob": -0.08409228818169956,
              "compression_ratio": 1.35,
              "no_speech_prob": 9.010058671377053e-11,
              "words": [
                {
                  "word": " And",
                  "start": 24.98,
                  "end": 25.52,
                  "probability": 0.79052734375
                },
                {
                  "word": " so,",
                  "start": 25.52,
                  "end": 25.86,
                  "probability": 0.99560546875
                },
                {
                  "word": " my",
                  "start": 26.08,
                  "end": 26.2,
                  "probability": 0.99853515625
                },
                {
                  "word": " fellow",
                  "start": 26.2,
                  "end": 26.54,
                  "probability": 0.9990234375
                },
                {
                  "word": " Americans,",
                  "start": 26.54,
                  "end": 27.12,
                  "probability": 0.978515625
                },
                {
                  "word": " ask",
                  "start": 27.76,
                  "end": 28.78,
                  "probability": 0.98583984375
                },
                {
                  "word": " not",
                  "start": 28.78,
                  "end": 29.32,
                  "probability": 0.97998046875
                },
                {
                  "word": " what",
                  "start": 29.32,
                  "end": 30.56,
                  "probability": 0.98681640625
                },
                {
                  "word": " your",
                  "start": 30.56,
                  "end": 30.8,
                  "probability": 0.99609375
                },
                {
                  "word": " country",
                  "start": 30.8,
                  "end": 31.24,
                  "probability": 0.9990234375
                },
                {
                  "word": " can",
                  "start": 31.24,
                  "end": 31.62,
                  "probability": 0.99951171875
                },
                {
                  "word": " do",
                  "start": 31.62,
                  "end": 31.82,
                  "probability": 0.99951171875
                },
                {
                  "word": " for",
                  "start": 31.82,
                  "end": 32.06,
                  "probability": 0.99951171875
                },
                {
                  "word": " you,",
                  "start": 32.06,
                  "end": 32.4,
                  "probability": 1.0
                },
                {
                  "word": " ask",
                  "start": 32.78,
                  "end": 33.52,
                  "probability": 0.998046875
                },
                {
                  "word": " what",
                  "start": 33.52,
                  "end": 33.8,
                  "probability": 0.99951171875
                },
                {
                  "word": " you",
                  "start": 33.8,
                  "end": 34.04,
                  "probability": 0.9970703125
                },
                {
                  "word": " can",
                  "start": 34.04,
                  "end": 34.34,
                  "probability": 1.0
                },
                {
                  "word": " do",
                  "start": 34.34,
                  "end": 34.56,
                  "probability": 0.99951171875
                },
                {
                  "word": " for",
                  "start": 34.56,
                  "end": 34.78,
                  "probability": 0.99951171875
                },
                {
                  "word": " your",
                  "start": 34.78,
                  "end": 34.96,
                  "probability": 0.99951171875
                },
                {
                  "word": " country.",
                  "start": 34.96,
                  "end": 35.34,
                  "probability": 1.0
                }
              ]
            }
          ],
          "language": "en"
        }
      },
      "sha256": "0dd27774b732cbc838e3480477add3bdaca841e115223840b01b07ed3c86b121",
      "samples": 576000,
      "duration_ms": 36000.0,
      "status": "passed"
    },
    "silence": {
      "text": "",
      "words": [],
      "problems": [],
      "execution_status": "completed",
      "process_wall_s": 2.703991583000004,
      "command": [
        "/usr/bin/sandbox-exec",
        "-p",
        "(version 1) (allow default) (deny network*)",
        "/Users/runner/work/_temp/mlx-venv/bin/python3",
        "/Users/runner/work/aTrain_fork/aTrain_fork/scripts/mlx_whisper_evaluation/feasibility.py",
        "--worker-output",
        "/Users/runner/work/_temp/mlx-whisper-report/vad/silence.json",
        "--speech",
        "/Users/runner/work/_temp/mlx-whisper-work/silence.wav",
        "--model-dir",
        "/Users/runner/work/_temp/mlx-whisper-work/model",
        "--vad"
      ],
      "worker": {
        "status": "passed",
        "phase": "VAD returned no speech; ASR explicitly skipped",
        "network_connect_errno": 1,
        "packages": {
          "mlx-whisper": "0.4.3",
          "mlx": "0.32.4",
          "mlx-metal": "0.32.4"
        },
        "default_device": "Device(gpu, 0)",
        "metal_device_info": {
          "device_name": "Apple Paravirtual device",
          "max_recommended_working_set_size": 5010800640,
          "memory_size": 7516192768,
          "architecture": "air64_v27",
          "max_buffer_length": 3758096384,
          "resource_limit": 499000
        },
        "gpu_matmul_conv": "passed",
        "vad": {
          "packages": {
            "faster-whisper": "1.2.1",
            "onnxruntime": "1.27.0"
          },
          "model_filename": "silero_vad_v6.onnx",
          "model_sha256": "4cbf549b8326f60f80f2536d9eefeb450a9abe83365a098031c89719f1be17d2",
          "source_sha256": "37a9c774aefdd3162d936b896c8dcf5571b2ed938d65bffecfd631770049a18d",
          "options": {
            "threshold": 0.5,
            "neg_threshold": 0.35,
            "min_speech_duration_ms": 0,
            "min_silence_duration_ms": 2000,
            "speech_pad_ms": 400
          },
          "max_speech_duration_s": "infinity (upstream default)",
          "providers": [
            "CPUExecutionProvider"
          ],
          "wall_s": 0.07176987499997267,
          "spans_samples": [],
          "clip_timestamps_seconds": [],
          "effective_mlx_clip_grid_seconds": [],
          "semantics": "already padded original sample spans; no waveform concatenation or timestamp remapping"
        },
        "native_clip_results": [],
        "asr_invocations": 0,
        "clip_interval_problems": [],
        "inference_wall_s": null,
        "gpu_peak_memory_bytes": null,
        "result": {
          "text": "",
          "segments": [],
          "language": "en"
        }
      },
      "sha256": "190415015d40eef0cd797e1b59ffe00846b01873050b12d44b3a216de3faa2a9",
      "samples": 128000,
      "duration_ms": 8000.0,
      "status": "passed"
    },
    "noise": {
      "text": "",
      "words": [],
      "problems": [],
      "execution_status": "completed",
      "process_wall_s": 2.4527148749999697,
      "command": [
        "/usr/bin/sandbox-exec",
        "-p",
        "(version 1) (allow default) (deny network*)",
        "/Users/runner/work/_temp/mlx-venv/bin/python3",
        "/Users/runner/work/aTrain_fork/aTrain_fork/scripts/mlx_whisper_evaluation/feasibility.py",
        "--worker-output",
        "/Users/runner/work/_temp/mlx-whisper-report/vad/noise.json",
        "--speech",
        "/Users/runner/work/_temp/mlx-whisper-work/noise.wav",
        "--model-dir",
        "/Users/runner/work/_temp/mlx-whisper-work/model",
        "--vad"
      ],
      "worker": {
        "status": "passed",
        "phase": "VAD returned no speech; ASR explicitly skipped",
        "network_connect_errno": 1,
        "packages": {
          "mlx-whisper": "0.4.3",
          "mlx": "0.32.4",
          "mlx-metal": "0.32.4"
        },
        "default_device": "Device(gpu, 0)",
        "metal_device_info": {
          "device_name": "Apple Paravirtual device",
          "max_recommended_working_set_size": 5010800640,
          "memory_size": 7516192768,
          "architecture": "air64_v27",
          "max_buffer_length": 3758096384,
          "resource_limit": 499000
        },
        "gpu_matmul_conv": "passed",
        "vad": {
          "packages": {
            "faster-whisper": "1.2.1",
            "onnxruntime": "1.27.0"
          },
          "model_filename": "silero_vad_v6.onnx",
          "model_sha256": "4cbf549b8326f60f80f2536d9eefeb450a9abe83365a098031c89719f1be17d2",
          "source_sha256": "37a9c774aefdd3162d936b896c8dcf5571b2ed938d65bffecfd631770049a18d",
          "options": {
            "threshold": 0.5,
            "neg_threshold": 0.35,
            "min_speech_duration_ms": 0,
            "min_silence_duration_ms": 2000,
            "speech_pad_ms": 400
          },
          "max_speech_duration_s": "infinity (upstream default)",
          "providers": [
            "CPUExecutionProvider"
          ],
          "wall_s": 0.05754866699999184,
          "spans_samples": [],
          "clip_timestamps_seconds": [],
          "effective_mlx_clip_grid_seconds": [],
          "semantics": "already padded original sample spans; no waveform concatenation or timestamp remapping"
        },
        "native_clip_results": [],
        "asr_invocations": 0,
        "clip_interval_problems": [],
        "inference_wall_s": null,
        "gpu_peak_memory_bytes": null,
        "result": {
          "text": "",
          "segments": [],
          "language": "en"
        }
      },
      "sha256": "52886be29e412e86511d056ebf565aafd8a3d0430ab9c6a6ea3313b22c455a84",
      "samples": 128000,
      "duration_ms": 8000.0,
      "status": "passed"
    }
  },
  "shift_checks": {
    "leading": {
      "tolerance_ms": 50,
      "matched_words": 22,
      "unmatched_reference_words": 0,
      "unmatched_candidate_words": 0,
      "boundary_errors_ms": [
        60.0,
        0.0,
        0.0,
        0.0,
        20.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        340.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        20.0,
        20.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0
      ],
      "max_boundary_error_ms": 340.0,
      "median_boundary_error_ms": 0.0,
      "status": "failed"
    },
    "trailing": {
      "tolerance_ms": 50,
      "matched_words": 22,
      "unmatched_reference_words": 0,
      "unmatched_candidate_words": 0,
      "boundary_errors_ms": [
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0
      ],
      "max_boundary_error_ms": 0.0,
      "median_boundary_error_ms": 0.0,
      "status": "passed"
    },
    "boundary": {
      "tolerance_ms": 50,
      "matched_words": 22,
      "unmatched_reference_words": 0,
      "unmatched_candidate_words": 0,
      "boundary_errors_ms": [
        20.0,
        0.0,
        0.0,
        0.0,
        20.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        560.0,
        0.0,
        0.0,
        20.0,
        20.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        20.0,
        20.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0
      ],
      "max_boundary_error_ms": 560.0,
      "median_boundary_error_ms": 0.0,
      "status": "failed"
    },
    "internal-first": {
      "tolerance_ms": 50,
      "matched_words": 22,
      "unmatched_reference_words": 0,
      "unmatched_candidate_words": 0,
      "boundary_errors_ms": [
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0
      ],
      "max_boundary_error_ms": 0.0,
      "median_boundary_error_ms": 0.0,
      "status": "passed"
    },
    "internal-second": {
      "tolerance_ms": 50,
      "matched_words": 22,
      "unmatched_reference_words": 0,
      "unmatched_candidate_words": 0,
      "boundary_errors_ms": [
        270.0,
        10.0,
        10.0,
        10.0,
        30.0,
        10.0,
        10.0,
        10.0,
        10.0,
        10.0,
        490.0,
        10.0,
        10.0,
        50.0,
        50.0,
        10.0,
        10.0,
        10.0,
        10.0,
        10.0,
        10.0,
        10.0,
        10.0,
        10.0,
        10.0,
        10.0,
        10.0,
        10.0,
        50.0,
        10.0,
        10.0,
        10.0,
        10.0,
        10.0,
        10.0,
        10.0,
        10.0,
        10.0,
        10.0,
        10.0,
        10.0,
        10.0,
        10.0,
        10.0
      ],
      "max_boundary_error_ms": 490.0,
      "median_boundary_error_ms": 10.0,
      "status": "failed"
    },
    "internal-sequence": {
      "status": "failed",
      "first": {
        "tolerance_ms": 50,
        "matched_words": 22,
        "unmatched_reference_words": 0,
        "unmatched_candidate_words": 0,
        "boundary_errors_ms": [
          0.0,
          0.0,
          0.0,
          0.0,
          0.0,
          0.0,
          0.0,
          0.0,
          0.0,
          0.0,
          0.0,
          0.0,
          0.0,
          0.0,
          0.0,
          0.0,
          0.0,
          0.0,
          0.0,
          0.0,
          0.0,
          0.0,
          0.0,
          0.0,
          0.0,
          0.0,
          0.0,
          0.0,
          0.0,
          0.0,
          0.0,
          0.0,
          0.0,
          0.0,
          0.0,
          0.0,
          0.0,
          0.0,
          0.0,
          0.0,
          0.0,
          0.0,
          0.0,
          0.0
        ],
        "max_boundary_error_ms": 0.0,
        "median_boundary_error_ms": 0.0,
        "status": "passed"
      },
      "second": {
        "tolerance_ms": 50,
        "matched_words": 22,
        "unmatched_reference_words": 0,
        "unmatched_candidate_words": 0,
        "boundary_errors_ms": [
          270.0,
          10.0,
          10.0,
          10.0,
          30.0,
          10.0,
          10.0,
          10.0,
          10.0,
          10.0,
          490.0,
          10.0,
          10.0,
          50.0,
          50.0,
          10.0,
          10.0,
          10.0,
          10.0,
          10.0,
          10.0,
          10.0,
          10.0,
          10.0,
          10.0,
          10.0,
          10.0,
          10.0,
          50.0,
          10.0,
          10.0,
          10.0,
          10.0,
          10.0,
          10.0,
          10.0,
          10.0,
          10.0,
          10.0,
          10.0,
          10.0,
          10.0,
          10.0,
          10.0
        ],
        "max_boundary_error_ms": 490.0,
        "median_boundary_error_ms": 10.0,
        "status": "failed"
      },
      "exact_complete_repeated_sequence": true
    }
  },
  "baseline_comparison": {
    "diagnostic_only": true,
    "baseline_report_sha256": "e1444263dd36be755b89d223928f6700b2f214945f1698d3455b0f1a88b7c2a3",
    "meaning": "same unchanged waveform, VAD versus no VAD; separate from inserted-silence gate",
    "fixtures": {
      "base": {
        "tolerance_ms": 50,
        "matched_words": 22,
        "unmatched_reference_words": 0,
        "unmatched_candidate_words": 0,
        "boundary_errors_ms": [
          0.0,
          0.0,
          0.0,
          0.0,
          0.0,
          0.0,
          0.0,
          0.0,
          0.0,
          0.0,
          0.0,
          0.0,
          0.0,
          0.0,
          0.0,
          0.0,
          0.0,
          0.0,
          0.0,
          0.0,
          0.0,
          0.0,
          0.0,
          0.0,
          0.0,
          0.0,
          0.0,
          0.0,
          0.0,
          0.0,
          0.0,
          0.0,
          0.0,
          0.0,
          0.0,
          0.0,
          0.0,
          0.0,
          0.0,
          0.0,
          0.0,
          0.0,
          0.0,
          0.0
        ],
        "max_boundary_error_ms": 0.0,
        "median_boundary_error_ms": 0.0,
        "status": "passed"
      },
      "leading": {
        "tolerance_ms": 50,
        "matched_words": 22,
        "unmatched_reference_words": 0,
        "unmatched_candidate_words": 0,
        "boundary_errors_ms": [
          60.0,
          0.0,
          0.0,
          0.0,
          0.0,
          0.0,
          0.0,
          0.0,
          0.0,
          0.0,
          0.0,
          0.0,
          0.0,
          60.0,
          60.0,
          0.0,
          0.0,
          0.0,
          0.0,
          0.0,
          0.0,
          20.0,
          20.0,
          0.0,
          0.0,
          0.0,
          0.0,
          0.0,
          80.0,
          0.0,
          0.0,
          40.0,
          40.0,
          0.0,
          0.0,
          0.0,
          0.0,
          0.0,
          0.0,
          0.0,
          0.0,
          0.0,
          0.0,
          20.0
        ],
        "max_boundary_error_ms": 80.0,
        "median_boundary_error_ms": 0.0,
        "status": "failed"
      },
      "trailing": {
        "tolerance_ms": 50,
        "matched_words": 22,
        "unmatched_reference_words": 0,
        "unmatched_candidate_words": 0,
        "boundary_errors_ms": [
          0.0,
          0.0,
          0.0,
          0.0,
          20.0,
          0.0,
          0.0,
          0.0,
          0.0,
          0.0,
          560.0,
          0.0,
          0.0,
          20.0,
          20.0,
          0.0,
          0.0,
          0.0,
          0.0,
          0.0,
          0.0,
          0.0,
          0.0,
          0.0,
          0.0,
          0.0,
          0.0,
          0.0,
          20.0,
          0.0,
          0.0,
          20.0,
          20.0,
          20.0,
          20.0,
          0.0,
          0.0,
          0.0,
          0.0,
          0.0,
          0.0,
          0.0,
          0.0,
          20.0
        ],
        "max_boundary_error_ms": 560.0,
        "median_boundary_error_ms": 0.0,
        "status": "failed"
      },
      "internal": {
        "tolerance_ms": 50,
        "matched_words": 44,
        "unmatched_reference_words": 0,
        "unmatched_candidate_words": 0,
        "boundary_errors_ms": [
          0.0,
          0.0,
          0.0,
          0.0,
          20.0,
          0.0,
          0.0,
          0.0,
          0.0,
          0.0,
          560.0,
          0.0,
          0.0,
          60.0,
          60.0,
          0.0,
          0.0,
          20.0,
          20.0,
          0.0,
          0.0,
          20.0,
          20.0,
          0.0,
          0.0,
          0.0,
          0.0,
          0.0,
          100.0,
          0.0,
          0.0,
          60.0,
          60.0,
          20.0,
          20.0,
          0.0,
          0.0,
          0.0,
          0.0,
          0.0,
          0.0,
          0.0,
          0.0,
          20.0,
          450.0,
          30.0,
          30.0,
          10.0,
          30.0,
          30.0,
          30.0,
          10.0,
          10.0,
          10.0,
          270.0,
          10.0,
          10.0,
          10.0,
          10.0,
          50.0,
          50.0,
          50.0,
          50.0,
          10.0,
          10.0,
          10.0,
          10.0,
          10.0,
          10.0,
          10.0,
          10.0,
          10.0,
          70.0,
          10.0,
          10.0,
          50.0,
          50.0,
          10.0,
          10.0,
          10.0,
          10.0,
          10.0,
          10.0,
          10.0,
          10.0,
          10.0,
          10.0,
          10.0
        ],
        "max_boundary_error_ms": 560.0,
        "median_boundary_error_ms": 10.0,
        "status": "failed"
      },
      "boundary": {
        "tolerance_ms": 50,
        "matched_words": 15,
        "unmatched_reference_words": 7,
        "unmatched_candidate_words": 7,
        "boundary_errors_ms": [
          680.0,
          0.0,
          0.0,
          0.0,
          0.0,
          0.0,
          0.0,
          20.0,
          20.0,
          20.0,
          20.0,
          0.0,
          0.0,
          40.0,
          100.0,
          0.0,
          0.0,
          0.0,
          0.0,
          20.0,
          20.0,
          0.0,
          0.0,
          0.0,
          0.0,
          0.0,
          0.0,
          0.0,
          0.0,
          20.0
        ],
        "max_boundary_error_ms": 680.0,
        "median_boundary_error_ms": 0.0,
        "status": "failed"
      },
      "silence": {
        "tolerance_ms": 50,
        "matched_words": 0,
        "unmatched_reference_words": 2,
        "unmatched_candidate_words": 0,
        "boundary_errors_ms": [],
        "max_boundary_error_ms": null,
        "median_boundary_error_ms": null,
        "status": "failed"
      },
      "noise": {
        "tolerance_ms": 50,
        "matched_words": 0,
        "unmatched_reference_words": 1,
        "unmatched_candidate_words": 0,
        "boundary_errors_ms": [],
        "max_boundary_error_ms": null,
        "median_boundary_error_ms": null,
        "status": "failed"
      }
    }
  },
  "candidate_structural_status": "failed"
}
```

</details>

## capability-report.json

Original file SHA-256: `bfcbca5e6135a5b3c1541f383aa07b846f6c7f345313bfe5c703325705a15a80`

<details>
<summary>Complete recorded result</summary>

```json
{
  "execution_status": "completed",
  "process_wall_s": 1.4699671249999966,
  "command": [
    "/usr/bin/sandbox-exec",
    "-p",
    "(version 1) (allow default) (deny network*)",
    "/Users/runner/work/_temp/mlx-venv/bin/python3",
    "/Users/runner/work/aTrain_fork/aTrain_fork/scripts/mlx_whisper_evaluation/feasibility.py",
    "--worker-output",
    "/Users/runner/work/_temp/mlx-whisper-report/capability.json",
    "--capability-only"
  ],
  "worker": {
    "status": "passed",
    "phase": "MLX GPU capability",
    "network_connect_errno": 1,
    "packages": {
      "mlx-whisper": "0.4.3",
      "mlx": "0.32.4",
      "mlx-metal": "0.32.4"
    },
    "default_device": "Device(gpu, 0)",
    "metal_device_info": {
      "device_name": "Apple Paravirtual device",
      "max_recommended_working_set_size": 5010800640,
      "memory_size": 7516192768,
      "architecture": "air64_v27",
      "max_buffer_length": 3758096384,
      "resource_limit": 499000
    },
    "gpu_matmul_conv": "passed"
  }
}
```

</details>

## capability.json

Original file SHA-256: `18cf85012b9d422dec30ff01215f508c03053246fa809e0e20c8de011c8aa213`

<details>
<summary>Complete recorded result</summary>

```json
{
  "status": "passed",
  "phase": "MLX GPU capability",
  "network_connect_errno": 1,
  "packages": {
    "mlx-whisper": "0.4.3",
    "mlx": "0.32.4",
    "mlx-metal": "0.32.4"
  },
  "default_device": "Device(gpu, 0)",
  "metal_device_info": {
    "device_name": "Apple Paravirtual device",
    "max_recommended_working_set_size": 5010800640,
    "memory_size": 7516192768,
    "architecture": "air64_v27",
    "max_buffer_length": 3758096384,
    "resource_limit": 499000
  },
  "gpu_matmul_conv": "passed"
}
```

</details>

## asset-provenance.json

Original file SHA-256: `0be5d8f61960471034a1a7b47aa85141d9b1e042c2ceddf354efec96ebe72f27`

<details>
<summary>Complete recorded result</summary>

```json
{
  "model_repo": "mlx-community/whisper-large-v3-turbo",
  "model_revision": "a4aaeec0636e6fef84abdcbe3544cb2bf7e9f6fb",
  "model_files": {
    "config.json": [
      268,
      "b34fc29e4e11e0a25e812775dd67f4dd16fc2c8eb43d28ae25ff7d660ecb6379"
    ],
    "weights.safetensors": [
      1613977612,
      "951ed3fc1203e6a62467abb2144a96ce7eafca8fa77e3704fdb8635ff3e7f8a6"
    ]
  },
  "model_license_note": "upstream OpenAI model MIT; converted card omits license; production provenance unverified",
  "speech_url": "https://raw.githubusercontent.com/ggml-org/whisper.cpp/d1be6fde11ac6e0407606b4e42fe72d34add8037/samples/jfk.mp3",
  "speech_mp3_sha256": "20d3323a2bcce6f25498b8911a397503a0a99fa92b6ba58d62788cb42b6e5459",
  "speech_pcm_sha256": "200cf71b13e4fc571f02943f470fd3305ea953ac02363541f444dc6139bf2463",
  "speech_samples": 176000,
  "audio_decoder": "macOS /usr/bin/afconvert; PCM equality checked separately",
  "matches_prior_cpu_pcm": false,
  "speech_recording": "White House Army Signal Agency; JFK Inaugural Address, 20 January 1961; JFKWHA-001",
  "speech_rights": "Public Domain per JFK Library recording catalog",
  "speech_rights_source": "https://www.jfklibrary.org/asset-viewer/archives/jfkwha-001",
  "speech_crop_note": "same pinned whisper.cpp excerpt as earlier CPU experiment; exact archive crop offsets unverified"
}
```

</details>
