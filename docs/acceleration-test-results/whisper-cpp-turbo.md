# whisper.cpp large-v3-turbo: CPU timestamp experiment

[Apple hardware acceleration tests](../apple-hardware-acceleration-tests.md)

Archived on 23 October 2026. The JSON below preserves the complete aggregate
results and listed supporting diagnostics without altering values. Absolute
paths inside these historical records identify the original run environment.
Audio, model binaries and raw execution logs are not embedded. See the index
for interpretation, limitations and links to the original artifacts.

## report.json

Original file SHA-256: `753fdae91b2d2e5325f12a5e400d98dedd92333a208163dadf6458e78cb000d0`

<details>
<summary>Complete recorded result</summary>

```json
{
  "source_commit": "d1be6fde11ac6e0407606b4e42fe72d34add8037",
  "host": "Linux-7.0.0-38-generic-x86_64-with-glibc2.43",
  "machine": "x86_64",
  "model_preset": "large-v3-turbo",
  "dtw_preset": "large.v3.turbo",
  "timeout_s": 900,
  "model_sha256": "1fc70f774d38eb169993ac391eea357ef47c88757ef72ee5943879b7e8e2bc69",
  "vad_sha256": "29940d98d42b91fbd05ce489f3ecf7c72f0a42f027e4875919a28fb4c04ea2cf",
  "helper_hashes": {
    "upstream": "ed9333ba257b89517630f9f502021d43f04786d8d9fa30f535d46b9878df4031",
    "patched": "ddd1cd92a14ba88f5b23580bae7fcb97561e463772254577ce9af56882742897"
  },
  "shift_tolerance_ms": 50,
  "grouping": "provisional whitespace EN/DE only; JA segmentation unverified",
  "fixtures": {
    "base": {
      "path": "/tmp/atrain-whisper-a-turbo-cpu-results/audio/base.wav",
      "sha256": "e94f7cfc2aa04ce40619f1e6d0b8a6c0faf94470f17fc23ddd0f804f25717f78",
      "samples": 176000,
      "duration_ms": 11000.0,
      "language": "en"
    },
    "leading": {
      "path": "/tmp/atrain-whisper-a-turbo-cpu-results/audio/leading.wav",
      "sha256": "7207dc380ee424c434c3d3602c2f6eaf86b12af6f680e6ee1cffb626e4ee21a8",
      "samples": 256000,
      "duration_ms": 16000.0,
      "language": "en"
    },
    "trailing": {
      "path": "/tmp/atrain-whisper-a-turbo-cpu-results/audio/trailing.wav",
      "sha256": "3b3bc59b1c2ff60801fa46e0dcce778d0d6111170323b8e46cce56c6b19cbd59",
      "samples": 256000,
      "duration_ms": 16000.0,
      "language": "en"
    },
    "internal": {
      "path": "/tmp/atrain-whisper-a-turbo-cpu-results/audio/internal.wav",
      "sha256": "70dc75ae98b68b01e44c58e2219db0ed7437a0511f5f4eaa2c7bdeb0623c6bb6",
      "samples": 432000,
      "duration_ms": 27000.0,
      "language": "en"
    },
    "boundary": {
      "path": "/tmp/atrain-whisper-a-turbo-cpu-results/audio/boundary.wav",
      "sha256": "4546b555cbeb960e7d6ddebe27e2c69effed93f5ecc8651bc34c58e1ad6714e3",
      "samples": 576000,
      "duration_ms": 36000.0,
      "language": "en"
    },
    "silence": {
      "path": "/tmp/atrain-whisper-a-turbo-cpu-results/audio/silence.wav",
      "sha256": "190415015d40eef0cd797e1b59ffe00846b01873050b12d44b3a216de3faa2a9",
      "samples": 128000,
      "duration_ms": 8000.0,
      "language": "en"
    },
    "noise": {
      "path": "/tmp/atrain-whisper-a-turbo-cpu-results/audio/noise.wav",
      "sha256": "52886be29e412e86511d056ebf565aafd8a3d0430ab9c6a6ea3313b22c455a84",
      "samples": 128000,
      "duration_ms": 8000.0,
      "language": "en"
    },
    "german": {
      "path": "/tmp/atrain-whisper-a-turbo-cpu-results/audio/german.wav",
      "sha256": "f2ccc92f26b5859d99c80fcac2c714324674da8e2c492b25625a2c88a62e3e0b",
      "samples": 480000,
      "duration_ms": 30000.0,
      "language": "de"
    },
    "japanese": {
      "path": "/tmp/atrain-whisper-a-turbo-cpu-results/audio/japanese.wav",
      "sha256": "843407942e21491c592f452e2a32e17995ff5ba700190531eba114c792cd45eb",
      "samples": 23034,
      "duration_ms": 1439.625,
      "language": "ja"
    }
  },
  "runs": {
    "upstream-ordinary-no-vad": {
      "fixtures": {
        "base": {
          "text": " And so, my fellow Americans, ask not what your country can do for you, ask what you can do for your country.",
          "words": [
            {
              "text": " And",
              "start_ms": 100,
              "end_ms": 240,
              "pieces": [
                " And"
              ]
            },
            {
              "text": " so,",
              "start_ms": 330,
              "end_ms": 540,
              "pieces": [
                " so",
                ","
              ]
            },
            {
              "text": " my",
              "start_ms": 680,
              "end_ms": 730,
              "pieces": [
                " my"
              ]
            },
            {
              "text": " fellow",
              "start_ms": 730,
              "end_ms": 1220,
              "pieces": [
                " fellow"
              ]
            },
            {
              "text": " Americans,",
              "start_ms": 1220,
              "end_ms": 2890,
              "pieces": [
                " Americans",
                ","
              ]
            },
            {
              "text": " ask",
              "start_ms": 3290,
              "end_ms": 3650,
              "pieces": [
                " ask"
              ]
            },
            {
              "text": " not",
              "start_ms": 4010,
              "end_ms": 4290,
              "pieces": [
                " not"
              ]
            },
            {
              "text": " what",
              "start_ms": 4980,
              "end_ms": 5260,
              "pieces": [
                " what"
              ]
            },
            {
              "text": " your",
              "start_ms": 5410,
              "end_ms": 5520,
              "pieces": [
                " your"
              ]
            },
            {
              "text": " country",
              "start_ms": 5520,
              "end_ms": 6000,
              "pieces": [
                " country"
              ]
            },
            {
              "text": " can",
              "start_ms": 6000,
              "end_ms": 6540,
              "pieces": [
                " can"
              ]
            },
            {
              "text": " do",
              "start_ms": 6540,
              "end_ms": 6900,
              "pieces": [
                " do"
              ]
            },
            {
              "text": " for",
              "start_ms": 7010,
              "end_ms": 7440,
              "pieces": [
                " for"
              ]
            },
            {
              "text": " you,",
              "start_ms": 7440,
              "end_ms": 8170,
              "pieces": [
                " you",
                ","
              ]
            },
            {
              "text": " ask",
              "start_ms": 8190,
              "end_ms": 8430,
              "pieces": [
                " ask"
              ]
            },
            {
              "text": " what",
              "start_ms": 8430,
              "end_ms": 8750,
              "pieces": [
                " what"
              ]
            },
            {
              "text": " you",
              "start_ms": 8910,
              "end_ms": 9080,
              "pieces": [
                " you"
              ]
            },
            {
              "text": " can",
              "start_ms": 9080,
              "end_ms": 9350,
              "pieces": [
                " can"
              ]
            },
            {
              "text": " do",
              "start_ms": 9350,
              "end_ms": 9580,
              "pieces": [
                " do"
              ]
            },
            {
              "text": " for",
              "start_ms": 9580,
              "end_ms": 9670,
              "pieces": [
                " for"
              ]
            },
            {
              "text": " your",
              "start_ms": 9730,
              "end_ms": 9910,
              "pieces": [
                " your"
              ]
            },
            {
              "text": " country.",
              "start_ms": 9910,
              "end_ms": 10400,
              "pieces": [
                " country",
                "."
              ]
            }
          ],
          "problems": [],
          "dtw_points": [
            {
              "text": " And",
              "point_cs": -1
            },
            {
              "text": " so",
              "point_cs": -1
            },
            {
              "text": ",",
              "point_cs": -1
            },
            {
              "text": " my",
              "point_cs": -1
            },
            {
              "text": " fellow",
              "point_cs": -1
            },
            {
              "text": " Americans",
              "point_cs": -1
            },
            {
              "text": ",",
              "point_cs": -1
            },
            {
              "text": " ask",
              "point_cs": -1
            },
            {
              "text": " not",
              "point_cs": -1
            },
            {
              "text": " what",
              "point_cs": -1
            },
            {
              "text": " your",
              "point_cs": -1
            },
            {
              "text": " country",
              "point_cs": -1
            },
            {
              "text": " can",
              "point_cs": -1
            },
            {
              "text": " do",
              "point_cs": -1
            },
            {
              "text": " for",
              "point_cs": -1
            },
            {
              "text": " you",
              "point_cs": -1
            },
            {
              "text": ",",
              "point_cs": -1
            },
            {
              "text": " ask",
              "point_cs": -1
            },
            {
              "text": " what",
              "point_cs": -1
            },
            {
              "text": " you",
              "point_cs": -1
            },
            {
              "text": " can",
              "point_cs": -1
            },
            {
              "text": " do",
              "point_cs": -1
            },
            {
              "text": " for",
              "point_cs": -1
            },
            {
              "text": " your",
              "point_cs": -1
            },
            {
              "text": " country",
              "point_cs": -1
            },
            {
              "text": ".",
              "point_cs": -1
            }
          ],
          "command": [
            "/tmp/atrain-whisper-a/.whisper-cli-unpatched",
            "-m",
            "/home/juergen/github/aTrain/.cache/whisper-cpp-evaluation/ggml-large-v3-turbo.bin",
            "-f",
            "/tmp/atrain-whisper-a-turbo-cpu-results/audio/base.wav",
            "-l",
            "en",
            "-t",
            "4",
            "-bs",
            "5",
            "-tp",
            "0",
            "-nf",
            "-ng",
            "-nfa",
            "-ojf",
            "-of",
            "/tmp/atrain-whisper-a-turbo-cpu-results/upstream-ordinary-no-vad-base"
          ],
          "wall_s": 17.809281434994773,
          "execution_status": "completed",
          "status": "passed"
        },
        "leading": {
          "text": " And so, my fellow Americans, ask not what your country can do for you, ask what you can do for your country.",
          "words": [
            {
              "text": " And",
              "start_ms": 5000,
              "end_ms": 5000,
              "pieces": [
                " And"
              ]
            },
            {
              "text": " so,",
              "start_ms": 5060,
              "end_ms": 5380,
              "pieces": [
                " so",
                ","
              ]
            },
            {
              "text": " my",
              "start_ms": 5380,
              "end_ms": 5540,
              "pieces": [
                " my"
              ]
            },
            {
              "text": " fellow",
              "start_ms": 5680,
              "end_ms": 6140,
              "pieces": [
                " fellow"
              ]
            },
            {
              "text": " Americans,",
              "start_ms": 6140,
              "end_ms": 7100,
              "pieces": [
                " Americans",
                ","
              ]
            },
            {
              "text": " ask",
              "start_ms": 8280,
              "end_ms": 8700,
              "pieces": [
                " ask"
              ]
            },
            {
              "text": " not",
              "start_ms": 9030,
              "end_ms": 9280,
              "pieces": [
                " not"
              ]
            },
            {
              "text": " what",
              "start_ms": 9280,
              "end_ms": 10000,
              "pieces": [
                " what"
              ]
            },
            {
              "text": " your",
              "start_ms": 10030,
              "end_ms": 10350,
              "pieces": [
                " your"
              ]
            },
            {
              "text": " country",
              "start_ms": 10410,
              "end_ms": 11000,
              "pieces": [
                " country"
              ]
            },
            {
              "text": " can",
              "start_ms": 11000,
              "end_ms": 11600,
              "pieces": [
                " can"
              ]
            },
            {
              "text": " do",
              "start_ms": 11600,
              "end_ms": 11920,
              "pieces": [
                " do"
              ]
            },
            {
              "text": " for",
              "start_ms": 12010,
              "end_ms": 12490,
              "pieces": [
                " for"
              ]
            },
            {
              "text": " you,",
              "start_ms": 12490,
              "end_ms": 13170,
              "pieces": [
                " you",
                ","
              ]
            },
            {
              "text": " ask",
              "start_ms": 13190,
              "end_ms": 13430,
              "pieces": [
                " ask"
              ]
            },
            {
              "text": " what",
              "start_ms": 13430,
              "end_ms": 13750,
              "pieces": [
                " what"
              ]
            },
            {
              "text": " you",
              "start_ms": 13910,
              "end_ms": 14000,
              "pieces": [
                " you"
              ]
            },
            {
              "text": " can",
              "start_ms": 14000,
              "end_ms": 14380,
              "pieces": [
                " can"
              ]
            },
            {
              "text": " do",
              "start_ms": 14380,
              "end_ms": 14580,
              "pieces": [
                " do"
              ]
            },
            {
              "text": " for",
              "start_ms": 14580,
              "end_ms": 14800,
              "pieces": [
                " for"
              ]
            },
            {
              "text": " your",
              "start_ms": 14800,
              "end_ms": 15190,
              "pieces": [
                " your"
              ]
            },
            {
              "text": " country.",
              "start_ms": 15230,
              "end_ms": 15990,
              "pieces": [
                " country",
                "."
              ]
            }
          ],
          "problems": [
            "nonpositive word interval: ' And'"
          ],
          "dtw_points": [
            {
              "text": " And",
              "point_cs": -1
            },
            {
              "text": " so",
              "point_cs": -1
            },
            {
              "text": ",",
              "point_cs": -1
            },
            {
              "text": " my",
              "point_cs": -1
            },
            {
              "text": " fellow",
              "point_cs": -1
            },
            {
              "text": " Americans",
              "point_cs": -1
            },
            {
              "text": ",",
              "point_cs": -1
            },
            {
              "text": " ask",
              "point_cs": -1
            },
            {
              "text": " not",
              "point_cs": -1
            },
            {
              "text": " what",
              "point_cs": -1
            },
            {
              "text": " your",
              "point_cs": -1
            },
            {
              "text": " country",
              "point_cs": -1
            },
            {
              "text": " can",
              "point_cs": -1
            },
            {
              "text": " do",
              "point_cs": -1
            },
            {
              "text": " for",
              "point_cs": -1
            },
            {
              "text": " you",
              "point_cs": -1
            },
            {
              "text": ",",
              "point_cs": -1
            },
            {
              "text": " ask",
              "point_cs": -1
            },
            {
              "text": " what",
              "point_cs": -1
            },
            {
              "text": " you",
              "point_cs": -1
            },
            {
              "text": " can",
              "point_cs": -1
            },
            {
              "text": " do",
              "point_cs": -1
            },
            {
              "text": " for",
              "point_cs": -1
            },
            {
              "text": " your",
              "point_cs": -1
            },
            {
              "text": " country",
              "point_cs": -1
            },
            {
              "text": ".",
              "point_cs": -1
            }
          ],
          "command": [
            "/tmp/atrain-whisper-a/.whisper-cli-unpatched",
            "-m",
            "/home/juergen/github/aTrain/.cache/whisper-cpp-evaluation/ggml-large-v3-turbo.bin",
            "-f",
            "/tmp/atrain-whisper-a-turbo-cpu-results/audio/leading.wav",
            "-l",
            "en",
            "-t",
            "4",
            "-bs",
            "5",
            "-tp",
            "0",
            "-nf",
            "-ng",
            "-nfa",
            "-ojf",
            "-of",
            "/tmp/atrain-whisper-a-turbo-cpu-results/upstream-ordinary-no-vad-leading"
          ],
          "wall_s": 18.060687108998536,
          "execution_status": "completed",
          "status": "failed"
        },
        "trailing": {
          "text": " And so, my fellow Americans, ask not what your country can do for you, ask what you can do for your country.",
          "words": [
            {
              "text": " And",
              "start_ms": 100,
              "end_ms": 240,
              "pieces": [
                " And"
              ]
            },
            {
              "text": " so,",
              "start_ms": 330,
              "end_ms": 540,
              "pieces": [
                " so",
                ","
              ]
            },
            {
              "text": " my",
              "start_ms": 680,
              "end_ms": 730,
              "pieces": [
                " my"
              ]
            },
            {
              "text": " fellow",
              "start_ms": 730,
              "end_ms": 1220,
              "pieces": [
                " fellow"
              ]
            },
            {
              "text": " Americans,",
              "start_ms": 1220,
              "end_ms": 2890,
              "pieces": [
                " Americans",
                ","
              ]
            },
            {
              "text": " ask",
              "start_ms": 3290,
              "end_ms": 3650,
              "pieces": [
                " ask"
              ]
            },
            {
              "text": " not",
              "start_ms": 4010,
              "end_ms": 4290,
              "pieces": [
                " not"
              ]
            },
            {
              "text": " what",
              "start_ms": 4980,
              "end_ms": 5260,
              "pieces": [
                " what"
              ]
            },
            {
              "text": " your",
              "start_ms": 5410,
              "end_ms": 5520,
              "pieces": [
                " your"
              ]
            },
            {
              "text": " country",
              "start_ms": 5520,
              "end_ms": 6000,
              "pieces": [
                " country"
              ]
            },
            {
              "text": " can",
              "start_ms": 6000,
              "end_ms": 6540,
              "pieces": [
                " can"
              ]
            },
            {
              "text": " do",
              "start_ms": 6540,
              "end_ms": 6900,
              "pieces": [
                " do"
              ]
            },
            {
              "text": " for",
              "start_ms": 7010,
              "end_ms": 7440,
              "pieces": [
                " for"
              ]
            },
            {
              "text": " you,",
              "start_ms": 7440,
              "end_ms": 8170,
              "pieces": [
                " you",
                ","
              ]
            },
            {
              "text": " ask",
              "start_ms": 8190,
              "end_ms": 8430,
              "pieces": [
                " ask"
              ]
            },
            {
              "text": " what",
              "start_ms": 8430,
              "end_ms": 8750,
              "pieces": [
                " what"
              ]
            },
            {
              "text": " you",
              "start_ms": 8910,
              "end_ms": 9080,
              "pieces": [
                " you"
              ]
            },
            {
              "text": " can",
              "start_ms": 9080,
              "end_ms": 9350,
              "pieces": [
                " can"
              ]
            },
            {
              "text": " do",
              "start_ms": 9350,
              "end_ms": 9580,
              "pieces": [
                " do"
              ]
            },
            {
              "text": " for",
              "start_ms": 9580,
              "end_ms": 9670,
              "pieces": [
                " for"
              ]
            },
            {
              "text": " your",
              "start_ms": 9730,
              "end_ms": 9910,
              "pieces": [
                " your"
              ]
            },
            {
              "text": " country.",
              "start_ms": 9910,
              "end_ms": 10400,
              "pieces": [
                " country",
                "."
              ]
            }
          ],
          "problems": [],
          "dtw_points": [
            {
              "text": " And",
              "point_cs": -1
            },
            {
              "text": " so",
              "point_cs": -1
            },
            {
              "text": ",",
              "point_cs": -1
            },
            {
              "text": " my",
              "point_cs": -1
            },
            {
              "text": " fellow",
              "point_cs": -1
            },
            {
              "text": " Americans",
              "point_cs": -1
            },
            {
              "text": ",",
              "point_cs": -1
            },
            {
              "text": " ask",
              "point_cs": -1
            },
            {
              "text": " not",
              "point_cs": -1
            },
            {
              "text": " what",
              "point_cs": -1
            },
            {
              "text": " your",
              "point_cs": -1
            },
            {
              "text": " country",
              "point_cs": -1
            },
            {
              "text": " can",
              "point_cs": -1
            },
            {
              "text": " do",
              "point_cs": -1
            },
            {
              "text": " for",
              "point_cs": -1
            },
            {
              "text": " you",
              "point_cs": -1
            },
            {
              "text": ",",
              "point_cs": -1
            },
            {
              "text": " ask",
              "point_cs": -1
            },
            {
              "text": " what",
              "point_cs": -1
            },
            {
              "text": " you",
              "point_cs": -1
            },
            {
              "text": " can",
              "point_cs": -1
            },
            {
              "text": " do",
              "point_cs": -1
            },
            {
              "text": " for",
              "point_cs": -1
            },
            {
              "text": " your",
              "point_cs": -1
            },
            {
              "text": " country",
              "point_cs": -1
            },
            {
              "text": ".",
              "point_cs": -1
            }
          ],
          "command": [
            "/tmp/atrain-whisper-a/.whisper-cli-unpatched",
            "-m",
            "/home/juergen/github/aTrain/.cache/whisper-cpp-evaluation/ggml-large-v3-turbo.bin",
            "-f",
            "/tmp/atrain-whisper-a-turbo-cpu-results/audio/trailing.wav",
            "-l",
            "en",
            "-t",
            "4",
            "-bs",
            "5",
            "-tp",
            "0",
            "-nf",
            "-ng",
            "-nfa",
            "-ojf",
            "-of",
            "/tmp/atrain-whisper-a-turbo-cpu-results/upstream-ordinary-no-vad-trailing"
          ],
          "wall_s": 18.5077611010056,
          "execution_status": "completed",
          "status": "passed"
        },
        "internal": {
          "text": " And so, my fellow Americans, ask not what your country can do for you, ask what you can do for your country. And so, my fellow Americans, ask not what your country can do for you, ask what you can do for your country.",
          "words": [
            {
              "text": " And",
              "start_ms": 320,
              "end_ms": 370,
              "pieces": [
                " And"
              ]
            },
            {
              "text": " so,",
              "start_ms": 370,
              "end_ms": 860,
              "pieces": [
                " so",
                ","
              ]
            },
            {
              "text": " my",
              "start_ms": 860,
              "end_ms": 1110,
              "pieces": [
                " my"
              ]
            },
            {
              "text": " fellow",
              "start_ms": 1110,
              "end_ms": 1850,
              "pieces": [
                " fellow"
              ]
            },
            {
              "text": " Americans,",
              "start_ms": 1850,
              "end_ms": 3000,
              "pieces": [
                " Americans",
                ","
              ]
            },
            {
              "text": " ask",
              "start_ms": 3340,
              "end_ms": 3990,
              "pieces": [
                " ask"
              ]
            },
            {
              "text": " not",
              "start_ms": 4020,
              "end_ms": 4970,
              "pieces": [
                " not"
              ]
            },
            {
              "text": " what",
              "start_ms": 5010,
              "end_ms": 5110,
              "pieces": [
                " what"
              ]
            },
            {
              "text": " your",
              "start_ms": 5110,
              "end_ms": 5520,
              "pieces": [
                " your"
              ]
            },
            {
              "text": " country",
              "start_ms": 5520,
              "end_ms": 6000,
              "pieces": [
                " country"
              ]
            },
            {
              "text": " can",
              "start_ms": 6290,
              "end_ms": 6540,
              "pieces": [
                " can"
              ]
            },
            {
              "text": " do",
              "start_ms": 6540,
              "end_ms": 6650,
              "pieces": [
                " do"
              ]
            },
            {
              "text": " for",
              "start_ms": 7010,
              "end_ms": 7280,
              "pieces": [
                " for"
              ]
            },
            {
              "text": " you,",
              "start_ms": 7280,
              "end_ms": 8000,
              "pieces": [
                " you",
                ","
              ]
            },
            {
              "text": " ask",
              "start_ms": 8310,
              "end_ms": 8310,
              "pieces": [
                " ask"
              ]
            },
            {
              "text": " what",
              "start_ms": 8340,
              "end_ms": 8720,
              "pieces": [
                " what"
              ]
            },
            {
              "text": " you",
              "start_ms": 8720,
              "end_ms": 9030,
              "pieces": [
                " you"
              ]
            },
            {
              "text": " can",
              "start_ms": 9030,
              "end_ms": 9240,
              "pieces": [
                " can"
              ]
            },
            {
              "text": " do",
              "start_ms": 9370,
              "end_ms": 9540,
              "pieces": [
                " do"
              ]
            },
            {
              "text": " for",
              "start_ms": 9540,
              "end_ms": 9850,
              "pieces": [
                " for"
              ]
            },
            {
              "text": " your",
              "start_ms": 9850,
              "end_ms": 10100,
              "pieces": [
                " your"
              ]
            },
            {
              "text": " country.",
              "start_ms": 10100,
              "end_ms": 11000,
              "pieces": [
                " country",
                "."
              ]
            },
            {
              "text": " And",
              "start_ms": 16000,
              "end_ms": 16000,
              "pieces": [
                " And"
              ]
            },
            {
              "text": " so,",
              "start_ms": 16000,
              "end_ms": 16000,
              "pieces": [
                " so",
                ","
              ]
            },
            {
              "text": " my",
              "start_ms": 16000,
              "end_ms": 16000,
              "pieces": [
                " my"
              ]
            },
            {
              "text": " fellow",
              "start_ms": 16000,
              "end_ms": 16000,
              "pieces": [
                " fellow"
              ]
            },
            {
              "text": " Americans,",
              "start_ms": 16340,
              "end_ms": 19000,
              "pieces": [
                " Americans",
                ","
              ]
            },
            {
              "text": " ask",
              "start_ms": 19320,
              "end_ms": 19460,
              "pieces": [
                " ask"
              ]
            },
            {
              "text": " not",
              "start_ms": 19460,
              "end_ms": 19920,
              "pieces": [
                " not"
              ]
            },
            {
              "text": " what",
              "start_ms": 19920,
              "end_ms": 20540,
              "pieces": [
                " what"
              ]
            },
            {
              "text": " your",
              "start_ms": 20540,
              "end_ms": 21100,
              "pieces": [
                " your"
              ]
            },
            {
              "text": " country",
              "start_ms": 21160,
              "end_ms": 22240,
              "pieces": [
                " country"
              ]
            },
            {
              "text": " can",
              "start_ms": 22290,
              "end_ms": 22650,
              "pieces": [
                " can"
              ]
            },
            {
              "text": " do",
              "start_ms": 23010,
              "end_ms": 23020,
              "pieces": [
                " do"
              ]
            },
            {
              "text": " for",
              "start_ms": 23020,
              "end_ms": 23280,
              "pieces": [
                " for"
              ]
            },
            {
              "text": " you,",
              "start_ms": 23280,
              "end_ms": 24000,
              "pieces": [
                " you",
                ","
              ]
            },
            {
              "text": " ask",
              "start_ms": 24280,
              "end_ms": 24280,
              "pieces": [
                " ask"
              ]
            },
            {
              "text": " what",
              "start_ms": 24330,
              "end_ms": 24530,
              "pieces": [
                " what"
              ]
            },
            {
              "text": " you",
              "start_ms": 24690,
              "end_ms": 24930,
              "pieces": [
                " you"
              ]
            },
            {
              "text": " can",
              "start_ms": 24930,
              "end_ms": 25210,
              "pieces": [
                " can"
              ]
            },
            {
              "text": " do",
              "start_ms": 25210,
              "end_ms": 25390,
              "pieces": [
                " do"
              ]
            },
            {
              "text": " for",
              "start_ms": 25390,
              "end_ms": 25670,
              "pieces": [
                " for"
              ]
            },
            {
              "text": " your",
              "start_ms": 25670,
              "end_ms": 25980,
              "pieces": [
                " your"
              ]
            },
            {
              "text": " country.",
              "start_ms": 26030,
              "end_ms": 27000,
              "pieces": [
                " country",
                "."
              ]
            }
          ],
          "problems": [
            "nonpositive word interval: ' ask'",
            "nonpositive word interval: ' And'",
            "nonpositive word interval: ' so,'",
            "nonpositive word interval: ' my'",
            "nonpositive word interval: ' fellow'",
            "nonpositive word interval: ' ask'"
          ],
          "dtw_points": [
            {
              "text": " And",
              "point_cs": -1
            },
            {
              "text": " so",
              "point_cs": -1
            },
            {
              "text": ",",
              "point_cs": -1
            },
            {
              "text": " my",
              "point_cs": -1
            },
            {
              "text": " fellow",
              "point_cs": -1
            },
            {
              "text": " Americans",
              "point_cs": -1
            },
            {
              "text": ",",
              "point_cs": -1
            },
            {
              "text": " ask",
              "point_cs": -1
            },
            {
              "text": " not",
              "point_cs": -1
            },
            {
              "text": " what",
              "point_cs": -1
            },
            {
              "text": " your",
              "point_cs": -1
            },
            {
              "text": " country",
              "point_cs": -1
            },
            {
              "text": " can",
              "point_cs": -1
            },
            {
              "text": " do",
              "point_cs": -1
            },
            {
              "text": " for",
              "point_cs": -1
            },
            {
              "text": " you",
              "point_cs": -1
            },
            {
              "text": ",",
              "point_cs": -1
            },
            {
              "text": " ask",
              "point_cs": -1
            },
            {
              "text": " what",
              "point_cs": -1
            },
            {
              "text": " you",
              "point_cs": -1
            },
            {
              "text": " can",
              "point_cs": -1
            },
            {
              "text": " do",
              "point_cs": -1
            },
            {
              "text": " for",
              "point_cs": -1
            },
            {
              "text": " your",
              "point_cs": -1
            },
            {
              "text": " country",
              "point_cs": -1
            },
            {
              "text": ".",
              "point_cs": -1
            },
            {
              "text": " And",
              "point_cs": -1
            },
            {
              "text": " so",
              "point_cs": -1
            },
            {
              "text": ",",
              "point_cs": -1
            },
            {
              "text": " my",
              "point_cs": -1
            },
            {
              "text": " fellow",
              "point_cs": -1
            },
            {
              "text": " Americans",
              "point_cs": -1
            },
            {
              "text": ",",
              "point_cs": -1
            },
            {
              "text": " ask",
              "point_cs": -1
            },
            {
              "text": " not",
              "point_cs": -1
            },
            {
              "text": " what",
              "point_cs": -1
            },
            {
              "text": " your",
              "point_cs": -1
            },
            {
              "text": " country",
              "point_cs": -1
            },
            {
              "text": " can",
              "point_cs": -1
            },
            {
              "text": " do",
              "point_cs": -1
            },
            {
              "text": " for",
              "point_cs": -1
            },
            {
              "text": " you",
              "point_cs": -1
            },
            {
              "text": ",",
              "point_cs": -1
            },
            {
              "text": " ask",
              "point_cs": -1
            },
            {
              "text": " what",
              "point_cs": -1
            },
            {
              "text": " you",
              "point_cs": -1
            },
            {
              "text": " can",
              "point_cs": -1
            },
            {
              "text": " do",
              "point_cs": -1
            },
            {
              "text": " for",
              "point_cs": -1
            },
            {
              "text": " your",
              "point_cs": -1
            },
            {
              "text": " country",
              "point_cs": -1
            },
            {
              "text": ".",
              "point_cs": -1
            }
          ],
          "command": [
            "/tmp/atrain-whisper-a/.whisper-cli-unpatched",
            "-m",
            "/home/juergen/github/aTrain/.cache/whisper-cpp-evaluation/ggml-large-v3-turbo.bin",
            "-f",
            "/tmp/atrain-whisper-a-turbo-cpu-results/audio/internal.wav",
            "-l",
            "en",
            "-t",
            "4",
            "-bs",
            "5",
            "-tp",
            "0",
            "-nf",
            "-ng",
            "-nfa",
            "-ojf",
            "-of",
            "/tmp/atrain-whisper-a-turbo-cpu-results/upstream-ordinary-no-vad-internal"
          ],
          "wall_s": 19.211459185011336,
          "execution_status": "completed",
          "status": "failed"
        },
        "boundary": {
          "text": " And so, my fellow Americans, ask not what your country can do for you, ask what you can do for your country.",
          "words": [
            {
              "text": " And",
              "start_ms": 24990,
              "end_ms": 25000,
              "pieces": [
                " And"
              ]
            },
            {
              "text": " so,",
              "start_ms": 25340,
              "end_ms": 26030,
              "pieces": [
                " so",
                ","
              ]
            },
            {
              "text": " my",
              "start_ms": 26030,
              "end_ms": 26160,
              "pieces": [
                " my"
              ]
            },
            {
              "text": " fellow",
              "start_ms": 26160,
              "end_ms": 26570,
              "pieces": [
                " fellow"
              ]
            },
            {
              "text": " Americans,",
              "start_ms": 26570,
              "end_ms": 27220,
              "pieces": [
                " Americans",
                ","
              ]
            },
            {
              "text": " ask",
              "start_ms": 27820,
              "end_ms": 28320,
              "pieces": [
                " ask"
              ]
            },
            {
              "text": " not",
              "start_ms": 28320,
              "end_ms": 28820,
              "pieces": [
                " not"
              ]
            },
            {
              "text": " what",
              "start_ms": 28820,
              "end_ms": 29480,
              "pieces": [
                " what"
              ]
            },
            {
              "text": " your",
              "start_ms": 29480,
              "end_ms": 30140,
              "pieces": [
                " your"
              ]
            },
            {
              "text": " country",
              "start_ms": 30140,
              "end_ms": 31320,
              "pieces": [
                " country"
              ]
            },
            {
              "text": " can",
              "start_ms": 31320,
              "end_ms": 31640,
              "pieces": [
                " can"
              ]
            },
            {
              "text": " do",
              "start_ms": 31640,
              "end_ms": 31860,
              "pieces": [
                " do"
              ]
            },
            {
              "text": " for",
              "start_ms": 31860,
              "end_ms": 32180,
              "pieces": [
                " for"
              ]
            },
            {
              "text": " you,",
              "start_ms": 32180,
              "end_ms": 32500,
              "pieces": [
                " you",
                ","
              ]
            },
            {
              "text": " ask",
              "start_ms": 33200,
              "end_ms": 33200,
              "pieces": [
                " ask"
              ]
            },
            {
              "text": " what",
              "start_ms": 33200,
              "end_ms": 33200,
              "pieces": [
                " what"
              ]
            },
            {
              "text": " you",
              "start_ms": 33200,
              "end_ms": 33400,
              "pieces": [
                " you"
              ]
            },
            {
              "text": " can",
              "start_ms": 33400,
              "end_ms": 33670,
              "pieces": [
                " can"
              ]
            },
            {
              "text": " do",
              "start_ms": 33670,
              "end_ms": 33850,
              "pieces": [
                " do"
              ]
            },
            {
              "text": " for",
              "start_ms": 33850,
              "end_ms": 34120,
              "pieces": [
                " for"
              ]
            },
            {
              "text": " your",
              "start_ms": 34120,
              "end_ms": 34480,
              "pieces": [
                " your"
              ]
            },
            {
              "text": " country.",
              "start_ms": 34480,
              "end_ms": 35380,
              "pieces": [
                " country",
                "."
              ]
            }
          ],
          "problems": [
            "nonpositive word interval: ' ask'",
            "nonpositive word interval: ' what'"
          ],
          "dtw_points": [
            {
              "text": " And",
              "point_cs": -1
            },
            {
              "text": " so",
              "point_cs": -1
            },
            {
              "text": ",",
              "point_cs": -1
            },
            {
              "text": " my",
              "point_cs": -1
            },
            {
              "text": " fellow",
              "point_cs": -1
            },
            {
              "text": " Americans",
              "point_cs": -1
            },
            {
              "text": ",",
              "point_cs": -1
            },
            {
              "text": " ask",
              "point_cs": -1
            },
            {
              "text": " not",
              "point_cs": -1
            },
            {
              "text": " what",
              "point_cs": -1
            },
            {
              "text": " your",
              "point_cs": -1
            },
            {
              "text": " country",
              "point_cs": -1
            },
            {
              "text": " can",
              "point_cs": -1
            },
            {
              "text": " do",
              "point_cs": -1
            },
            {
              "text": " for",
              "point_cs": -1
            },
            {
              "text": " you",
              "point_cs": -1
            },
            {
              "text": ",",
              "point_cs": -1
            },
            {
              "text": " ask",
              "point_cs": -1
            },
            {
              "text": " what",
              "point_cs": -1
            },
            {
              "text": " you",
              "point_cs": -1
            },
            {
              "text": " can",
              "point_cs": -1
            },
            {
              "text": " do",
              "point_cs": -1
            },
            {
              "text": " for",
              "point_cs": -1
            },
            {
              "text": " your",
              "point_cs": -1
            },
            {
              "text": " country",
              "point_cs": -1
            },
            {
              "text": ".",
              "point_cs": -1
            }
          ],
          "command": [
            "/tmp/atrain-whisper-a/.whisper-cli-unpatched",
            "-m",
            "/home/juergen/github/aTrain/.cache/whisper-cpp-evaluation/ggml-large-v3-turbo.bin",
            "-f",
            "/tmp/atrain-whisper-a-turbo-cpu-results/audio/boundary.wav",
            "-l",
            "en",
            "-t",
            "4",
            "-bs",
            "5",
            "-tp",
            "0",
            "-nf",
            "-ng",
            "-nfa",
            "-ojf",
            "-of",
            "/tmp/atrain-whisper-a-turbo-cpu-results/upstream-ordinary-no-vad-boundary"
          ],
          "wall_s": 36.30615086200123,
          "execution_status": "completed",
          "status": "failed"
        },
        "silence": {
          "text": " Thank you.",
          "words": [
            {
              "text": " Thank",
              "start_ms": 0,
              "end_ms": 7990,
              "pieces": [
                " Thank"
              ]
            },
            {
              "text": " you.",
              "start_ms": 7990,
              "end_ms": 7990,
              "pieces": [
                " you",
                "."
              ]
            }
          ],
          "problems": [
            "nonpositive word interval: ' you.'",
            "recognized words on silence-only fixture"
          ],
          "dtw_points": [
            {
              "text": " Thank",
              "point_cs": -1
            },
            {
              "text": " you",
              "point_cs": -1
            },
            {
              "text": ".",
              "point_cs": -1
            }
          ],
          "command": [
            "/tmp/atrain-whisper-a/.whisper-cli-unpatched",
            "-m",
            "/home/juergen/github/aTrain/.cache/whisper-cpp-evaluation/ggml-large-v3-turbo.bin",
            "-f",
            "/tmp/atrain-whisper-a-turbo-cpu-results/audio/silence.wav",
            "-l",
            "en",
            "-t",
            "4",
            "-bs",
            "5",
            "-tp",
            "0",
            "-nf",
            "-ng",
            "-nfa",
            "-ojf",
            "-of",
            "/tmp/atrain-whisper-a-turbo-cpu-results/upstream-ordinary-no-vad-silence"
          ],
          "wall_s": 19.210636899006204,
          "execution_status": "completed",
          "status": "failed"
        },
        "noise": {
          "text": " so",
          "words": [
            {
              "text": " so",
              "start_ms": 0,
              "end_ms": 7990,
              "pieces": [
                " so"
              ]
            }
          ],
          "problems": [
            "recognized words on noise-only fixture"
          ],
          "dtw_points": [
            {
              "text": " so",
              "point_cs": -1
            }
          ],
          "command": [
            "/tmp/atrain-whisper-a/.whisper-cli-unpatched",
            "-m",
            "/home/juergen/github/aTrain/.cache/whisper-cpp-evaluation/ggml-large-v3-turbo.bin",
            "-f",
            "/tmp/atrain-whisper-a-turbo-cpu-results/audio/noise.wav",
            "-l",
            "en",
            "-t",
            "4",
            "-bs",
            "5",
            "-tp",
            "0",
            "-nf",
            "-ng",
            "-nfa",
            "-ojf",
            "-of",
            "/tmp/atrain-whisper-a-turbo-cpu-results/upstream-ordinary-no-vad-noise"
          ],
          "wall_s": 18.659601233986905,
          "execution_status": "completed",
          "status": "failed"
        },
        "german": {
          "text": " Hiro, Kapitel 8 Flach halten, flach halten. Junge, du wirst es nicht packen. Das ist doch, vergiss es, vergiss es einfach. Doch, das hast du gut gemacht. Nein, so nicht. Netz, Netz, hat berührt, hat berührt. Vergiss alles, was man dir gesagt hat. Den wirst du nicht packen. »Das ist gut.«",
          "words": [
            {
              "text": " Hiro,",
              "start_ms": 480,
              "end_ms": 1000,
              "pieces": [
                " Hi",
                "ro",
                ","
              ]
            },
            {
              "text": " Kapitel",
              "start_ms": 1230,
              "end_ms": 1660,
              "pieces": [
                " Kap",
                "itel"
              ]
            },
            {
              "text": " 8",
              "start_ms": 2460,
              "end_ms": 2720,
              "pieces": [
                " 8"
              ]
            },
            {
              "text": " Flach",
              "start_ms": 2730,
              "end_ms": 3850,
              "pieces": [
                " Fl",
                "ach"
              ]
            },
            {
              "text": " halten,",
              "start_ms": 4700,
              "end_ms": 5770,
              "pieces": [
                " halten",
                ","
              ]
            },
            {
              "text": " flach",
              "start_ms": 5780,
              "end_ms": 6560,
              "pieces": [
                " fl",
                "ach"
              ]
            },
            {
              "text": " halten.",
              "start_ms": 7000,
              "end_ms": 7520,
              "pieces": [
                " halten",
                "."
              ]
            },
            {
              "text": " Junge,",
              "start_ms": 8860,
              "end_ms": 8860,
              "pieces": [
                " Jun",
                "ge",
                ","
              ]
            },
            {
              "text": " du",
              "start_ms": 8860,
              "end_ms": 8860,
              "pieces": [
                " du"
              ]
            },
            {
              "text": " wirst",
              "start_ms": 8860,
              "end_ms": 8860,
              "pieces": [
                " w",
                "irst"
              ]
            },
            {
              "text": " es",
              "start_ms": 8860,
              "end_ms": 9050,
              "pieces": [
                " es"
              ]
            },
            {
              "text": " nicht",
              "start_ms": 9540,
              "end_ms": 9540,
              "pieces": [
                " nicht"
              ]
            },
            {
              "text": " packen.",
              "start_ms": 9610,
              "end_ms": 10440,
              "pieces": [
                " pack",
                "en",
                "."
              ]
            },
            {
              "text": " Das",
              "start_ms": 10840,
              "end_ms": 10840,
              "pieces": [
                " Das"
              ]
            },
            {
              "text": " ist",
              "start_ms": 10840,
              "end_ms": 11000,
              "pieces": [
                " ist"
              ]
            },
            {
              "text": " doch,",
              "start_ms": 11000,
              "end_ms": 11510,
              "pieces": [
                " doch",
                ","
              ]
            },
            {
              "text": " vergiss",
              "start_ms": 11590,
              "end_ms": 12000,
              "pieces": [
                " verg",
                "iss"
              ]
            },
            {
              "text": " es,",
              "start_ms": 12100,
              "end_ms": 12440,
              "pieces": [
                " es",
                ","
              ]
            },
            {
              "text": " vergiss",
              "start_ms": 12780,
              "end_ms": 13030,
              "pieces": [
                " verg",
                "iss"
              ]
            },
            {
              "text": " es",
              "start_ms": 13030,
              "end_ms": 13200,
              "pieces": [
                " es"
              ]
            },
            {
              "text": " einfach.",
              "start_ms": 13200,
              "end_ms": 14110,
              "pieces": [
                " einfach",
                "."
              ]
            },
            {
              "text": " Doch,",
              "start_ms": 14780,
              "end_ms": 14780,
              "pieces": [
                " Doch",
                ","
              ]
            },
            {
              "text": " das",
              "start_ms": 14780,
              "end_ms": 15080,
              "pieces": [
                " das"
              ]
            },
            {
              "text": " hast",
              "start_ms": 15510,
              "end_ms": 15510,
              "pieces": [
                " hast"
              ]
            },
            {
              "text": " du",
              "start_ms": 15530,
              "end_ms": 15680,
              "pieces": [
                " du"
              ]
            },
            {
              "text": " gut",
              "start_ms": 15760,
              "end_ms": 15910,
              "pieces": [
                " gut"
              ]
            },
            {
              "text": " gemacht.",
              "start_ms": 16760,
              "end_ms": 17140,
              "pieces": [
                " gemacht",
                "."
              ]
            },
            {
              "text": " Nein,",
              "start_ms": 17520,
              "end_ms": 17820,
              "pieces": [
                " Nein",
                ","
              ]
            },
            {
              "text": " so",
              "start_ms": 17820,
              "end_ms": 18050,
              "pieces": [
                " so"
              ]
            },
            {
              "text": " nicht.",
              "start_ms": 18270,
              "end_ms": 18690,
              "pieces": [
                " nicht",
                "."
              ]
            },
            {
              "text": " Netz,",
              "start_ms": 19200,
              "end_ms": 19620,
              "pieces": [
                " Netz",
                ","
              ]
            },
            {
              "text": " Netz,",
              "start_ms": 19950,
              "end_ms": 20250,
              "pieces": [
                " Netz",
                ","
              ]
            },
            {
              "text": " hat",
              "start_ms": 20250,
              "end_ms": 20370,
              "pieces": [
                " hat"
              ]
            },
            {
              "text": " berührt,",
              "start_ms": 20560,
              "end_ms": 21540,
              "pieces": [
                " ber",
                "ührt",
                ","
              ]
            },
            {
              "text": " hat",
              "start_ms": 21540,
              "end_ms": 21800,
              "pieces": [
                " hat"
              ]
            },
            {
              "text": " berührt.",
              "start_ms": 21860,
              "end_ms": 23040,
              "pieces": [
                " ber",
                "ührt",
                "."
              ]
            },
            {
              "text": " Vergiss",
              "start_ms": 24200,
              "end_ms": 24200,
              "pieces": [
                " Verg",
                "iss"
              ]
            },
            {
              "text": " alles,",
              "start_ms": 24200,
              "end_ms": 24320,
              "pieces": [
                " alles",
                ","
              ]
            },
            {
              "text": " was",
              "start_ms": 24320,
              "end_ms": 24590,
              "pieces": [
                " was"
              ]
            },
            {
              "text": " man",
              "start_ms": 24860,
              "end_ms": 24860,
              "pieces": [
                " man"
              ]
            },
            {
              "text": " dir",
              "start_ms": 24950,
              "end_ms": 25120,
              "pieces": [
                " dir"
              ]
            },
            {
              "text": " gesagt",
              "start_ms": 25130,
              "end_ms": 25330,
              "pieces": [
                " gesagt"
              ]
            },
            {
              "text": " hat.",
              "start_ms": 25650,
              "end_ms": 26280,
              "pieces": [
                " hat",
                "."
              ]
            },
            {
              "text": " Den",
              "start_ms": 27160,
              "end_ms": 27160,
              "pieces": [
                " Den"
              ]
            },
            {
              "text": " wirst",
              "start_ms": 27160,
              "end_ms": 27160,
              "pieces": [
                " w",
                "irst"
              ]
            },
            {
              "text": " du",
              "start_ms": 27160,
              "end_ms": 27180,
              "pieces": [
                " du"
              ]
            },
            {
              "text": " nicht",
              "start_ms": 27180,
              "end_ms": 27630,
              "pieces": [
                " nicht"
              ]
            },
            {
              "text": " packen.",
              "start_ms": 27910,
              "end_ms": 28330,
              "pieces": [
                " pack",
                "en",
                "."
              ]
            },
            {
              "text": " »Das",
              "start_ms": 28480,
              "end_ms": 28900,
              "pieces": [
                " »",
                "Das"
              ]
            },
            {
              "text": " ist",
              "start_ms": 29220,
              "end_ms": 29220,
              "pieces": [
                " ist"
              ]
            },
            {
              "text": " gut.«",
              "start_ms": 29230,
              "end_ms": 30000,
              "pieces": [
                " gut",
                ".",
                "«"
              ]
            }
          ],
          "problems": [
            "nonpositive word interval: ' Junge,'",
            "nonpositive word interval: ' du'",
            "nonpositive word interval: ' wirst'",
            "nonpositive word interval: ' nicht'",
            "nonpositive word interval: ' Das'",
            "nonpositive word interval: ' Doch,'",
            "nonpositive word interval: ' hast'",
            "nonpositive word interval: ' Vergiss'",
            "nonpositive word interval: ' man'",
            "nonpositive word interval: ' Den'",
            "nonpositive word interval: ' wirst'",
            "nonpositive word interval: ' ist'"
          ],
          "dtw_points": [
            {
              "text": " Hi",
              "point_cs": -1
            },
            {
              "text": "ro",
              "point_cs": -1
            },
            {
              "text": ",",
              "point_cs": -1
            },
            {
              "text": " Kap",
              "point_cs": -1
            },
            {
              "text": "itel",
              "point_cs": -1
            },
            {
              "text": " 8",
              "point_cs": -1
            },
            {
              "text": " Fl",
              "point_cs": -1
            },
            {
              "text": "ach",
              "point_cs": -1
            },
            {
              "text": " halten",
              "point_cs": -1
            },
            {
              "text": ",",
              "point_cs": -1
            },
            {
              "text": " fl",
              "point_cs": -1
            },
            {
              "text": "ach",
              "point_cs": -1
            },
            {
              "text": " halten",
              "point_cs": -1
            },
            {
              "text": ".",
              "point_cs": -1
            },
            {
              "text": " Jun",
              "point_cs": -1
            },
            {
              "text": "ge",
              "point_cs": -1
            },
            {
              "text": ",",
              "point_cs": -1
            },
            {
              "text": " du",
              "point_cs": -1
            },
            {
              "text": " w",
              "point_cs": -1
            },
            {
              "text": "irst",
              "point_cs": -1
            },
            {
              "text": " es",
              "point_cs": -1
            },
            {
              "text": " nicht",
              "point_cs": -1
            },
            {
              "text": " pack",
              "point_cs": -1
            },
            {
              "text": "en",
              "point_cs": -1
            },
            {
              "text": ".",
              "point_cs": -1
            },
            {
              "text": " Das",
              "point_cs": -1
            },
            {
              "text": " ist",
              "point_cs": -1
            },
            {
              "text": " doch",
              "point_cs": -1
            },
            {
              "text": ",",
              "point_cs": -1
            },
            {
              "text": " verg",
              "point_cs": -1
            },
            {
              "text": "iss",
              "point_cs": -1
            },
            {
              "text": " es",
              "point_cs": -1
            },
            {
              "text": ",",
              "point_cs": -1
            },
            {
              "text": " verg",
              "point_cs": -1
            },
            {
              "text": "iss",
              "point_cs": -1
            },
            {
              "text": " es",
              "point_cs": -1
            },
            {
              "text": " einfach",
              "point_cs": -1
            },
            {
              "text": ".",
              "point_cs": -1
            },
            {
              "text": " Doch",
              "point_cs": -1
            },
            {
              "text": ",",
              "point_cs": -1
            },
            {
              "text": " das",
              "point_cs": -1
            },
            {
              "text": " hast",
              "point_cs": -1
            },
            {
              "text": " du",
              "point_cs": -1
            },
            {
              "text": " gut",
              "point_cs": -1
            },
            {
              "text": " gemacht",
              "point_cs": -1
            },
            {
              "text": ".",
              "point_cs": -1
            },
            {
              "text": " Nein",
              "point_cs": -1
            },
            {
              "text": ",",
              "point_cs": -1
            },
            {
              "text": " so",
              "point_cs": -1
            },
            {
              "text": " nicht",
              "point_cs": -1
            },
            {
              "text": ".",
              "point_cs": -1
            },
            {
              "text": " Netz",
              "point_cs": -1
            },
            {
              "text": ",",
              "point_cs": -1
            },
            {
              "text": " Netz",
              "point_cs": -1
            },
            {
              "text": ",",
              "point_cs": -1
            },
            {
              "text": " hat",
              "point_cs": -1
            },
            {
              "text": " ber",
              "point_cs": -1
            },
            {
              "text": "ührt",
              "point_cs": -1
            },
            {
              "text": ",",
              "point_cs": -1
            },
            {
              "text": " hat",
              "point_cs": -1
            },
            {
              "text": " ber",
              "point_cs": -1
            },
            {
              "text": "ührt",
              "point_cs": -1
            },
            {
              "text": ".",
              "point_cs": -1
            },
            {
              "text": " Verg",
              "point_cs": -1
            },
            {
              "text": "iss",
              "point_cs": -1
            },
            {
              "text": " alles",
              "point_cs": -1
            },
            {
              "text": ",",
              "point_cs": -1
            },
            {
              "text": " was",
              "point_cs": -1
            },
            {
              "text": " man",
              "point_cs": -1
            },
            {
              "text": " dir",
              "point_cs": -1
            },
            {
              "text": " gesagt",
              "point_cs": -1
            },
            {
              "text": " hat",
              "point_cs": -1
            },
            {
              "text": ".",
              "point_cs": -1
            },
            {
              "text": " Den",
              "point_cs": -1
            },
            {
              "text": " w",
              "point_cs": -1
            },
            {
              "text": "irst",
              "point_cs": -1
            },
            {
              "text": " du",
              "point_cs": -1
            },
            {
              "text": " nicht",
              "point_cs": -1
            },
            {
              "text": " pack",
              "point_cs": -1
            },
            {
              "text": "en",
              "point_cs": -1
            },
            {
              "text": ".",
              "point_cs": -1
            },
            {
              "text": " »",
              "point_cs": -1
            },
            {
              "text": "Das",
              "point_cs": -1
            },
            {
              "text": " ist",
              "point_cs": -1
            },
            {
              "text": " gut",
              "point_cs": -1
            },
            {
              "text": ".",
              "point_cs": -1
            },
            {
              "text": "«",
              "point_cs": -1
            }
          ],
          "command": [
            "/tmp/atrain-whisper-a/.whisper-cli-unpatched",
            "-m",
            "/home/juergen/github/aTrain/.cache/whisper-cpp-evaluation/ggml-large-v3-turbo.bin",
            "-f",
            "/tmp/atrain-whisper-a-turbo-cpu-results/audio/german.wav",
            "-l",
            "de",
            "-t",
            "4",
            "-bs",
            "5",
            "-tp",
            "0",
            "-nf",
            "-ng",
            "-nfa",
            "-ojf",
            "-of",
            "/tmp/atrain-whisper-a-turbo-cpu-results/upstream-ordinary-no-vad-german"
          ],
          "wall_s": 37.35569243499776,
          "execution_status": "completed",
          "status": "failed"
        },
        "japanese": {
          "text": "こんにちは",
          "words": [
            {
              "text": "こんにちは",
              "start_ms": 390,
              "end_ms": 1070,
              "pieces": [
                "こんにちは"
              ]
            }
          ],
          "problems": [],
          "dtw_points": [
            {
              "text": "こんにちは",
              "point_cs": -1
            }
          ],
          "command": [
            "/tmp/atrain-whisper-a/.whisper-cli-unpatched",
            "-m",
            "/home/juergen/github/aTrain/.cache/whisper-cpp-evaluation/ggml-large-v3-turbo.bin",
            "-f",
            "/tmp/atrain-whisper-a-turbo-cpu-results/audio/japanese.wav",
            "-l",
            "ja",
            "-t",
            "4",
            "-bs",
            "5",
            "-tp",
            "0",
            "-nf",
            "-ng",
            "-nfa",
            "-ojf",
            "-of",
            "/tmp/atrain-whisper-a-turbo-cpu-results/upstream-ordinary-no-vad-japanese"
          ],
          "wall_s": 18.165497112000594,
          "execution_status": "completed",
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
            100,
            240,
            270,
            160,
            300,
            190,
            50,
            80,
            80,
            790,
            10,
            50,
            20,
            10,
            700,
            260,
            380,
            170,
            110,
            0,
            0,
            60,
            60,
            20,
            0,
            50,
            50,
            0,
            0,
            0,
            0,
            0,
            0,
            80,
            80,
            30,
            30,
            0,
            0,
            130,
            70,
            280,
            320,
            590
          ],
          "max_boundary_error_ms": 790,
          "median_boundary_error_ms": 60.0,
          "status": "failed"
        },
        "trailing": {
          "tolerance_ms": 50,
          "matched_words": 22,
          "unmatched_reference_words": 0,
          "unmatched_candidate_words": 0,
          "boundary_errors_ms": [
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0
          ],
          "max_boundary_error_ms": 0,
          "median_boundary_error_ms": 0.0,
          "status": "passed"
        },
        "boundary": {
          "tolerance_ms": 50,
          "matched_words": 22,
          "unmatched_reference_words": 0,
          "unmatched_candidate_words": 0,
          "boundary_errors_ms": [
            110,
            240,
            10,
            490,
            350,
            430,
            430,
            350,
            350,
            670,
            470,
            330,
            690,
            470,
            1160,
            780,
            930,
            380,
            380,
            320,
            320,
            100,
            100,
            40,
            150,
            260,
            260,
            670,
            10,
            230,
            230,
            550,
            710,
            680,
            680,
            680,
            680,
            730,
            730,
            550,
            610,
            430,
            430,
            20
          ],
          "max_boundary_error_ms": 1160,
          "median_boundary_error_ms": 430.0,
          "status": "failed"
        },
        "internal-first": {
          "tolerance_ms": 50,
          "matched_words": 22,
          "unmatched_reference_words": 0,
          "unmatched_candidate_words": 0,
          "boundary_errors_ms": [
            220,
            130,
            40,
            320,
            180,
            380,
            380,
            630,
            630,
            110,
            50,
            340,
            10,
            680,
            30,
            150,
            300,
            0,
            0,
            0,
            290,
            0,
            0,
            250,
            0,
            160,
            160,
            170,
            120,
            120,
            90,
            30,
            190,
            50,
            50,
            110,
            20,
            40,
            40,
            180,
            120,
            190,
            190,
            600
          ],
          "max_boundary_error_ms": 680,
          "median_boundary_error_ms": 125.0,
          "status": "failed"
        },
        "internal-second": {
          "tolerance_ms": 50,
          "matched_words": 22,
          "unmatched_reference_words": 0,
          "unmatched_candidate_words": 0,
          "boundary_errors_ms": [
            100,
            240,
            330,
            540,
            680,
            730,
            730,
            1220,
            880,
            110,
            30,
            190,
            550,
            370,
            1060,
            720,
            870,
            420,
            360,
            240,
            290,
            110,
            470,
            120,
            10,
            160,
            160,
            170,
            90,
            150,
            100,
            220,
            220,
            150,
            150,
            140,
            140,
            190,
            190,
            0,
            60,
            70,
            120,
            600
          ],
          "max_boundary_error_ms": 1220,
          "median_boundary_error_ms": 190.0,
          "status": "failed"
        }
      }
    },
    "upstream-ordinary-vad": {
      "fixtures": {
        "base": {
          "text": " And so, my fellow Americans, ask not what your country can do for you, ask what you can do for your country.",
          "words": [
            {
              "text": " And",
              "start_ms": 40,
              "end_ms": 240,
              "pieces": [
                " And"
              ]
            },
            {
              "text": " so,",
              "start_ms": 390,
              "end_ms": 570,
              "pieces": [
                " so",
                ","
              ]
            },
            {
              "text": " my",
              "start_ms": 570,
              "end_ms": 680,
              "pieces": [
                " my"
              ]
            },
            {
              "text": " fellow",
              "start_ms": 730,
              "end_ms": 1220,
              "pieces": [
                " fellow"
              ]
            },
            {
              "text": " Americans,",
              "start_ms": 1220,
              "end_ms": 2290,
              "pieces": [
                " Americans",
                ","
              ]
            },
            {
              "text": " ask",
              "start_ms": 2290,
              "end_ms": 2500,
              "pieces": [
                " ask"
              ]
            },
            {
              "text": " not",
              "start_ms": 2840,
              "end_ms": 3100,
              "pieces": [
                " not"
              ]
            },
            {
              "text": " what",
              "start_ms": 3430,
              "end_ms": 3510,
              "pieces": [
                " what"
              ]
            },
            {
              "text": " your",
              "start_ms": 3510,
              "end_ms": 3840,
              "pieces": [
                " your"
              ]
            },
            {
              "text": " country",
              "start_ms": 3840,
              "end_ms": 4400,
              "pieces": [
                " country"
              ]
            },
            {
              "text": " can",
              "start_ms": 4400,
              "end_ms": 4640,
              "pieces": [
                " can"
              ]
            },
            {
              "text": " do",
              "start_ms": 4650,
              "end_ms": 4810,
              "pieces": [
                " do"
              ]
            },
            {
              "text": " for",
              "start_ms": 4810,
              "end_ms": 5050,
              "pieces": [
                " for"
              ]
            },
            {
              "text": " you,",
              "start_ms": 5050,
              "end_ms": 5490,
              "pieces": [
                " you",
                ","
              ]
            },
            {
              "text": " ask",
              "start_ms": 5490,
              "end_ms": 5580,
              "pieces": [
                " ask"
              ]
            },
            {
              "text": " what",
              "start_ms": 5900,
              "end_ms": 6400,
              "pieces": [
                " what"
              ]
            },
            {
              "text": " you",
              "start_ms": 6400,
              "end_ms": 6800,
              "pieces": [
                " you"
              ]
            },
            {
              "text": " can",
              "start_ms": 6800,
              "end_ms": 7080,
              "pieces": [
                " can"
              ]
            },
            {
              "text": " do",
              "start_ms": 7080,
              "end_ms": 7300,
              "pieces": [
                " do"
              ]
            },
            {
              "text": " for",
              "start_ms": 7300,
              "end_ms": 7440,
              "pieces": [
                " for"
              ]
            },
            {
              "text": " your",
              "start_ms": 7440,
              "end_ms": 7620,
              "pieces": [
                " your"
              ]
            },
            {
              "text": " country.",
              "start_ms": 7620,
              "end_ms": 8090,
              "pieces": [
                " country",
                "."
              ]
            }
          ],
          "problems": [],
          "dtw_points": [
            {
              "text": " And",
              "point_cs": -1
            },
            {
              "text": " so",
              "point_cs": -1
            },
            {
              "text": ",",
              "point_cs": -1
            },
            {
              "text": " my",
              "point_cs": -1
            },
            {
              "text": " fellow",
              "point_cs": -1
            },
            {
              "text": " Americans",
              "point_cs": -1
            },
            {
              "text": ",",
              "point_cs": -1
            },
            {
              "text": " ask",
              "point_cs": -1
            },
            {
              "text": " not",
              "point_cs": -1
            },
            {
              "text": " what",
              "point_cs": -1
            },
            {
              "text": " your",
              "point_cs": -1
            },
            {
              "text": " country",
              "point_cs": -1
            },
            {
              "text": " can",
              "point_cs": -1
            },
            {
              "text": " do",
              "point_cs": -1
            },
            {
              "text": " for",
              "point_cs": -1
            },
            {
              "text": " you",
              "point_cs": -1
            },
            {
              "text": ",",
              "point_cs": -1
            },
            {
              "text": " ask",
              "point_cs": -1
            },
            {
              "text": " what",
              "point_cs": -1
            },
            {
              "text": " you",
              "point_cs": -1
            },
            {
              "text": " can",
              "point_cs": -1
            },
            {
              "text": " do",
              "point_cs": -1
            },
            {
              "text": " for",
              "point_cs": -1
            },
            {
              "text": " your",
              "point_cs": -1
            },
            {
              "text": " country",
              "point_cs": -1
            },
            {
              "text": ".",
              "point_cs": -1
            }
          ],
          "command": [
            "/tmp/atrain-whisper-a/.whisper-cli-unpatched",
            "-m",
            "/home/juergen/github/aTrain/.cache/whisper-cpp-evaluation/ggml-large-v3-turbo.bin",
            "-f",
            "/tmp/atrain-whisper-a-turbo-cpu-results/audio/base.wav",
            "-l",
            "en",
            "-t",
            "4",
            "-bs",
            "5",
            "-tp",
            "0",
            "-nf",
            "-ng",
            "-nfa",
            "-ojf",
            "-of",
            "/tmp/atrain-whisper-a-turbo-cpu-results/upstream-ordinary-vad-base",
            "--vad",
            "-vm",
            "/tmp/atrain-whisper-a/.ggml-silero-v5.1.2.bin"
          ],
          "wall_s": 19.562814075005008,
          "execution_status": "completed",
          "status": "passed"
        },
        "leading": {
          "text": " And so, my fellow Americans, ask not what your country can do for you, ask what you can do for your country.",
          "words": [
            {
              "text": " And",
              "start_ms": 20,
              "end_ms": 200,
              "pieces": [
                " And"
              ]
            },
            {
              "text": " so,",
              "start_ms": 200,
              "end_ms": 460,
              "pieces": [
                " so",
                ","
              ]
            },
            {
              "text": " my",
              "start_ms": 460,
              "end_ms": 590,
              "pieces": [
                " my"
              ]
            },
            {
              "text": " fellow",
              "start_ms": 590,
              "end_ms": 930,
              "pieces": [
                " fellow"
              ]
            },
            {
              "text": " Americans,",
              "start_ms": 1060,
              "end_ms": 1790,
              "pieces": [
                " Americans",
                ","
              ]
            },
            {
              "text": " ask",
              "start_ms": 1790,
              "end_ms": 1810,
              "pieces": [
                " ask"
              ]
            },
            {
              "text": " not",
              "start_ms": 2150,
              "end_ms": 2460,
              "pieces": [
                " not"
              ]
            },
            {
              "text": " what",
              "start_ms": 2460,
              "end_ms": 2510,
              "pieces": [
                " what"
              ]
            },
            {
              "text": " your",
              "start_ms": 2890,
              "end_ms": 3140,
              "pieces": [
                " your"
              ]
            },
            {
              "text": " country",
              "start_ms": 3480,
              "end_ms": 4080,
              "pieces": [
                " country"
              ]
            },
            {
              "text": " can",
              "start_ms": 4080,
              "end_ms": 4410,
              "pieces": [
                " can"
              ]
            },
            {
              "text": " do",
              "start_ms": 4410,
              "end_ms": 4630,
              "pieces": [
                " do"
              ]
            },
            {
              "text": " for",
              "start_ms": 4630,
              "end_ms": 4960,
              "pieces": [
                " for"
              ]
            },
            {
              "text": " you,",
              "start_ms": 5080,
              "end_ms": 5540,
              "pieces": [
                " you",
                ","
              ]
            },
            {
              "text": " ask",
              "start_ms": 5540,
              "end_ms": 5660,
              "pieces": [
                " ask"
              ]
            },
            {
              "text": " what",
              "start_ms": 5980,
              "end_ms": 6470,
              "pieces": [
                " what"
              ]
            },
            {
              "text": " you",
              "start_ms": 6470,
              "end_ms": 6880,
              "pieces": [
                " you"
              ]
            },
            {
              "text": " can",
              "start_ms": 6880,
              "end_ms": 7160,
              "pieces": [
                " can"
              ]
            },
            {
              "text": " do",
              "start_ms": 7160,
              "end_ms": 7380,
              "pieces": [
                " do"
              ]
            },
            {
              "text": " for",
              "start_ms": 7380,
              "end_ms": 7460,
              "pieces": [
                " for"
              ]
            },
            {
              "text": " your",
              "start_ms": 7520,
              "end_ms": 7690,
              "pieces": [
                " your"
              ]
            },
            {
              "text": " country.",
              "start_ms": 7690,
              "end_ms": 8160,
              "pieces": [
                " country",
                "."
              ]
            }
          ],
          "problems": [],
          "dtw_points": [
            {
              "text": " And",
              "point_cs": -1
            },
            {
              "text": " so",
              "point_cs": -1
            },
            {
              "text": ",",
              "point_cs": -1
            },
            {
              "text": " my",
              "point_cs": -1
            },
            {
              "text": " fellow",
              "point_cs": -1
            },
            {
              "text": " Americans",
              "point_cs": -1
            },
            {
              "text": ",",
              "point_cs": -1
            },
            {
              "text": " ask",
              "point_cs": -1
            },
            {
              "text": " not",
              "point_cs": -1
            },
            {
              "text": " what",
              "point_cs": -1
            },
            {
              "text": " your",
              "point_cs": -1
            },
            {
              "text": " country",
              "point_cs": -1
            },
            {
              "text": " can",
              "point_cs": -1
            },
            {
              "text": " do",
              "point_cs": -1
            },
            {
              "text": " for",
              "point_cs": -1
            },
            {
              "text": " you",
              "point_cs": -1
            },
            {
              "text": ",",
              "point_cs": -1
            },
            {
              "text": " ask",
              "point_cs": -1
            },
            {
              "text": " what",
              "point_cs": -1
            },
            {
              "text": " you",
              "point_cs": -1
            },
            {
              "text": " can",
              "point_cs": -1
            },
            {
              "text": " do",
              "point_cs": -1
            },
            {
              "text": " for",
              "point_cs": -1
            },
            {
              "text": " your",
              "point_cs": -1
            },
            {
              "text": " country",
              "point_cs": -1
            },
            {
              "text": ".",
              "point_cs": -1
            }
          ],
          "command": [
            "/tmp/atrain-whisper-a/.whisper-cli-unpatched",
            "-m",
            "/home/juergen/github/aTrain/.cache/whisper-cpp-evaluation/ggml-large-v3-turbo.bin",
            "-f",
            "/tmp/atrain-whisper-a-turbo-cpu-results/audio/leading.wav",
            "-l",
            "en",
            "-t",
            "4",
            "-bs",
            "5",
            "-tp",
            "0",
            "-nf",
            "-ng",
            "-nfa",
            "-ojf",
            "-of",
            "/tmp/atrain-whisper-a-turbo-cpu-results/upstream-ordinary-vad-leading",
            "--vad",
            "-vm",
            "/tmp/atrain-whisper-a/.ggml-silero-v5.1.2.bin"
          ],
          "wall_s": 18.664297210998484,
          "execution_status": "completed",
          "status": "passed"
        },
        "trailing": {
          "text": " And so, my fellow Americans, ask not what your country can do for you, ask what you can do for your country.",
          "words": [
            {
              "text": " And",
              "start_ms": 40,
              "end_ms": 240,
              "pieces": [
                " And"
              ]
            },
            {
              "text": " so,",
              "start_ms": 390,
              "end_ms": 570,
              "pieces": [
                " so",
                ","
              ]
            },
            {
              "text": " my",
              "start_ms": 570,
              "end_ms": 680,
              "pieces": [
                " my"
              ]
            },
            {
              "text": " fellow",
              "start_ms": 730,
              "end_ms": 1220,
              "pieces": [
                " fellow"
              ]
            },
            {
              "text": " Americans,",
              "start_ms": 1220,
              "end_ms": 2290,
              "pieces": [
                " Americans",
                ","
              ]
            },
            {
              "text": " ask",
              "start_ms": 2290,
              "end_ms": 2500,
              "pieces": [
                " ask"
              ]
            },
            {
              "text": " not",
              "start_ms": 2840,
              "end_ms": 3100,
              "pieces": [
                " not"
              ]
            },
            {
              "text": " what",
              "start_ms": 3430,
              "end_ms": 3510,
              "pieces": [
                " what"
              ]
            },
            {
              "text": " your",
              "start_ms": 3510,
              "end_ms": 3840,
              "pieces": [
                " your"
              ]
            },
            {
              "text": " country",
              "start_ms": 3840,
              "end_ms": 4400,
              "pieces": [
                " country"
              ]
            },
            {
              "text": " can",
              "start_ms": 4400,
              "end_ms": 4640,
              "pieces": [
                " can"
              ]
            },
            {
              "text": " do",
              "start_ms": 4650,
              "end_ms": 4810,
              "pieces": [
                " do"
              ]
            },
            {
              "text": " for",
              "start_ms": 4810,
              "end_ms": 5050,
              "pieces": [
                " for"
              ]
            },
            {
              "text": " you,",
              "start_ms": 5050,
              "end_ms": 5490,
              "pieces": [
                " you",
                ","
              ]
            },
            {
              "text": " ask",
              "start_ms": 5490,
              "end_ms": 5580,
              "pieces": [
                " ask"
              ]
            },
            {
              "text": " what",
              "start_ms": 5900,
              "end_ms": 6400,
              "pieces": [
                " what"
              ]
            },
            {
              "text": " you",
              "start_ms": 6400,
              "end_ms": 6800,
              "pieces": [
                " you"
              ]
            },
            {
              "text": " can",
              "start_ms": 6800,
              "end_ms": 7080,
              "pieces": [
                " can"
              ]
            },
            {
              "text": " do",
              "start_ms": 7080,
              "end_ms": 7300,
              "pieces": [
                " do"
              ]
            },
            {
              "text": " for",
              "start_ms": 7300,
              "end_ms": 7440,
              "pieces": [
                " for"
              ]
            },
            {
              "text": " your",
              "start_ms": 7440,
              "end_ms": 7620,
              "pieces": [
                " your"
              ]
            },
            {
              "text": " country.",
              "start_ms": 7620,
              "end_ms": 8090,
              "pieces": [
                " country",
                "."
              ]
            }
          ],
          "problems": [],
          "dtw_points": [
            {
              "text": " And",
              "point_cs": -1
            },
            {
              "text": " so",
              "point_cs": -1
            },
            {
              "text": ",",
              "point_cs": -1
            },
            {
              "text": " my",
              "point_cs": -1
            },
            {
              "text": " fellow",
              "point_cs": -1
            },
            {
              "text": " Americans",
              "point_cs": -1
            },
            {
              "text": ",",
              "point_cs": -1
            },
            {
              "text": " ask",
              "point_cs": -1
            },
            {
              "text": " not",
              "point_cs": -1
            },
            {
              "text": " what",
              "point_cs": -1
            },
            {
              "text": " your",
              "point_cs": -1
            },
            {
              "text": " country",
              "point_cs": -1
            },
            {
              "text": " can",
              "point_cs": -1
            },
            {
              "text": " do",
              "point_cs": -1
            },
            {
              "text": " for",
              "point_cs": -1
            },
            {
              "text": " you",
              "point_cs": -1
            },
            {
              "text": ",",
              "point_cs": -1
            },
            {
              "text": " ask",
              "point_cs": -1
            },
            {
              "text": " what",
              "point_cs": -1
            },
            {
              "text": " you",
              "point_cs": -1
            },
            {
              "text": " can",
              "point_cs": -1
            },
            {
              "text": " do",
              "point_cs": -1
            },
            {
              "text": " for",
              "point_cs": -1
            },
            {
              "text": " your",
              "point_cs": -1
            },
            {
              "text": " country",
              "point_cs": -1
            },
            {
              "text": ".",
              "point_cs": -1
            }
          ],
          "command": [
            "/tmp/atrain-whisper-a/.whisper-cli-unpatched",
            "-m",
            "/home/juergen/github/aTrain/.cache/whisper-cpp-evaluation/ggml-large-v3-turbo.bin",
            "-f",
            "/tmp/atrain-whisper-a-turbo-cpu-results/audio/trailing.wav",
            "-l",
            "en",
            "-t",
            "4",
            "-bs",
            "5",
            "-tp",
            "0",
            "-nf",
            "-ng",
            "-nfa",
            "-ojf",
            "-of",
            "/tmp/atrain-whisper-a-turbo-cpu-results/upstream-ordinary-vad-trailing",
            "--vad",
            "-vm",
            "/tmp/atrain-whisper-a/.ggml-silero-v5.1.2.bin"
          ],
          "wall_s": 18.813660927000456,
          "execution_status": "completed",
          "status": "passed"
        },
        "internal": {
          "text": " And so, my fellow Americans, ask not what your country can do for you, ask what you can do for your country. And so, my fellow Americans, ask not what your country can do for you, ask what you can do for your country.",
          "words": [
            {
              "text": " And",
              "start_ms": 40,
              "end_ms": 240,
              "pieces": [
                " And"
              ]
            },
            {
              "text": " so,",
              "start_ms": 390,
              "end_ms": 570,
              "pieces": [
                " so",
                ","
              ]
            },
            {
              "text": " my",
              "start_ms": 570,
              "end_ms": 680,
              "pieces": [
                " my"
              ]
            },
            {
              "text": " fellow",
              "start_ms": 730,
              "end_ms": 1220,
              "pieces": [
                " fellow"
              ]
            },
            {
              "text": " Americans,",
              "start_ms": 1220,
              "end_ms": 2190,
              "pieces": [
                " Americans",
                ","
              ]
            },
            {
              "text": " ask",
              "start_ms": 2190,
              "end_ms": 2480,
              "pieces": [
                " ask"
              ]
            },
            {
              "text": " not",
              "start_ms": 2480,
              "end_ms": 2500,
              "pieces": [
                " not"
              ]
            },
            {
              "text": " what",
              "start_ms": 2850,
              "end_ms": 3100,
              "pieces": [
                " what"
              ]
            },
            {
              "text": " your",
              "start_ms": 3430,
              "end_ms": 3530,
              "pieces": [
                " your"
              ]
            },
            {
              "text": " country",
              "start_ms": 3530,
              "end_ms": 4110,
              "pieces": [
                " country"
              ]
            },
            {
              "text": " can",
              "start_ms": 4230,
              "end_ms": 4440,
              "pieces": [
                " can"
              ]
            },
            {
              "text": " do",
              "start_ms": 4510,
              "end_ms": 4670,
              "pieces": [
                " do"
              ]
            },
            {
              "text": " for",
              "start_ms": 4690,
              "end_ms": 4940,
              "pieces": [
                " for"
              ]
            },
            {
              "text": " you,",
              "start_ms": 5030,
              "end_ms": 5480,
              "pieces": [
                " you",
                ","
              ]
            },
            {
              "text": " ask",
              "start_ms": 5480,
              "end_ms": 5580,
              "pieces": [
                " ask"
              ]
            },
            {
              "text": " what",
              "start_ms": 5900,
              "end_ms": 6380,
              "pieces": [
                " what"
              ]
            },
            {
              "text": " you",
              "start_ms": 6380,
              "end_ms": 6780,
              "pieces": [
                " you"
              ]
            },
            {
              "text": " can",
              "start_ms": 6780,
              "end_ms": 7080,
              "pieces": [
                " can"
              ]
            },
            {
              "text": " do",
              "start_ms": 7080,
              "end_ms": 7300,
              "pieces": [
                " do"
              ]
            },
            {
              "text": " for",
              "start_ms": 7300,
              "end_ms": 7500,
              "pieces": [
                " for"
              ]
            },
            {
              "text": " your",
              "start_ms": 7500,
              "end_ms": 7660,
              "pieces": [
                " your"
              ]
            },
            {
              "text": " country.",
              "start_ms": 7660,
              "end_ms": 8080,
              "pieces": [
                " country",
                "."
              ]
            },
            {
              "text": " And",
              "start_ms": 8120,
              "end_ms": 8330,
              "pieces": [
                " And"
              ]
            },
            {
              "text": " so,",
              "start_ms": 8470,
              "end_ms": 8710,
              "pieces": [
                " so",
                ","
              ]
            },
            {
              "text": " my",
              "start_ms": 8710,
              "end_ms": 8890,
              "pieces": [
                " my"
              ]
            },
            {
              "text": " fellow",
              "start_ms": 8890,
              "end_ms": 9430,
              "pieces": [
                " fellow"
              ]
            },
            {
              "text": " Americans,",
              "start_ms": 9430,
              "end_ms": 10430,
              "pieces": [
                " Americans",
                ","
              ]
            },
            {
              "text": " ask",
              "start_ms": 10430,
              "end_ms": 10570,
              "pieces": [
                " ask"
              ]
            },
            {
              "text": " not",
              "start_ms": 10920,
              "end_ms": 10970,
              "pieces": [
                " not"
              ]
            },
            {
              "text": " what",
              "start_ms": 10970,
              "end_ms": 11180,
              "pieces": [
                " what"
              ]
            },
            {
              "text": " your",
              "start_ms": 11510,
              "end_ms": 11670,
              "pieces": [
                " your"
              ]
            },
            {
              "text": " country",
              "start_ms": 11750,
              "end_ms": 12330,
              "pieces": [
                " country"
              ]
            },
            {
              "text": " can",
              "start_ms": 12330,
              "end_ms": 12520,
              "pieces": [
                " can"
              ]
            },
            {
              "text": " do",
              "start_ms": 12600,
              "end_ms": 12780,
              "pieces": [
                " do"
              ]
            },
            {
              "text": " for",
              "start_ms": 12780,
              "end_ms": 13020,
              "pieces": [
                " for"
              ]
            },
            {
              "text": " you,",
              "start_ms": 13110,
              "end_ms": 13500,
              "pieces": [
                " you",
                ","
              ]
            },
            {
              "text": " ask",
              "start_ms": 13500,
              "end_ms": 13620,
              "pieces": [
                " ask"
              ]
            },
            {
              "text": " what",
              "start_ms": 13980,
              "end_ms": 14130,
              "pieces": [
                " what"
              ]
            },
            {
              "text": " you",
              "start_ms": 14130,
              "end_ms": 14250,
              "pieces": [
                " you"
              ]
            },
            {
              "text": " can",
              "start_ms": 14420,
              "end_ms": 14540,
              "pieces": [
                " can"
              ]
            },
            {
              "text": " do",
              "start_ms": 14700,
              "end_ms": 14850,
              "pieces": [
                " do"
              ]
            },
            {
              "text": " for",
              "start_ms": 14850,
              "end_ms": 15110,
              "pieces": [
                " for"
              ]
            },
            {
              "text": " your",
              "start_ms": 15110,
              "end_ms": 15460,
              "pieces": [
                " your"
              ]
            },
            {
              "text": " country.",
              "start_ms": 15510,
              "end_ms": 16450,
              "pieces": [
                " country",
                "."
              ]
            }
          ],
          "problems": [],
          "dtw_points": [
            {
              "text": " And",
              "point_cs": -1
            },
            {
              "text": " so",
              "point_cs": -1
            },
            {
              "text": ",",
              "point_cs": -1
            },
            {
              "text": " my",
              "point_cs": -1
            },
            {
              "text": " fellow",
              "point_cs": -1
            },
            {
              "text": " Americans",
              "point_cs": -1
            },
            {
              "text": ",",
              "point_cs": -1
            },
            {
              "text": " ask",
              "point_cs": -1
            },
            {
              "text": " not",
              "point_cs": -1
            },
            {
              "text": " what",
              "point_cs": -1
            },
            {
              "text": " your",
              "point_cs": -1
            },
            {
              "text": " country",
              "point_cs": -1
            },
            {
              "text": " can",
              "point_cs": -1
            },
            {
              "text": " do",
              "point_cs": -1
            },
            {
              "text": " for",
              "point_cs": -1
            },
            {
              "text": " you",
              "point_cs": -1
            },
            {
              "text": ",",
              "point_cs": -1
            },
            {
              "text": " ask",
              "point_cs": -1
            },
            {
              "text": " what",
              "point_cs": -1
            },
            {
              "text": " you",
              "point_cs": -1
            },
            {
              "text": " can",
              "point_cs": -1
            },
            {
              "text": " do",
              "point_cs": -1
            },
            {
              "text": " for",
              "point_cs": -1
            },
            {
              "text": " your",
              "point_cs": -1
            },
            {
              "text": " country",
              "point_cs": -1
            },
            {
              "text": ".",
              "point_cs": -1
            },
            {
              "text": " And",
              "point_cs": -1
            },
            {
              "text": " so",
              "point_cs": -1
            },
            {
              "text": ",",
              "point_cs": -1
            },
            {
              "text": " my",
              "point_cs": -1
            },
            {
              "text": " fellow",
              "point_cs": -1
            },
            {
              "text": " Americans",
              "point_cs": -1
            },
            {
              "text": ",",
              "point_cs": -1
            },
            {
              "text": " ask",
              "point_cs": -1
            },
            {
              "text": " not",
              "point_cs": -1
            },
            {
              "text": " what",
              "point_cs": -1
            },
            {
              "text": " your",
              "point_cs": -1
            },
            {
              "text": " country",
              "point_cs": -1
            },
            {
              "text": " can",
              "point_cs": -1
            },
            {
              "text": " do",
              "point_cs": -1
            },
            {
              "text": " for",
              "point_cs": -1
            },
            {
              "text": " you",
              "point_cs": -1
            },
            {
              "text": ",",
              "point_cs": -1
            },
            {
              "text": " ask",
              "point_cs": -1
            },
            {
              "text": " what",
              "point_cs": -1
            },
            {
              "text": " you",
              "point_cs": -1
            },
            {
              "text": " can",
              "point_cs": -1
            },
            {
              "text": " do",
              "point_cs": -1
            },
            {
              "text": " for",
              "point_cs": -1
            },
            {
              "text": " your",
              "point_cs": -1
            },
            {
              "text": " country",
              "point_cs": -1
            },
            {
              "text": ".",
              "point_cs": -1
            }
          ],
          "command": [
            "/tmp/atrain-whisper-a/.whisper-cli-unpatched",
            "-m",
            "/home/juergen/github/aTrain/.cache/whisper-cpp-evaluation/ggml-large-v3-turbo.bin",
            "-f",
            "/tmp/atrain-whisper-a-turbo-cpu-results/audio/internal.wav",
            "-l",
            "en",
            "-t",
            "4",
            "-bs",
            "5",
            "-tp",
            "0",
            "-nf",
            "-ng",
            "-nfa",
            "-ojf",
            "-of",
            "/tmp/atrain-whisper-a-turbo-cpu-results/upstream-ordinary-vad-internal",
            "--vad",
            "-vm",
            "/tmp/atrain-whisper-a/.ggml-silero-v5.1.2.bin"
          ],
          "wall_s": 19.51358798299043,
          "execution_status": "completed",
          "status": "passed"
        },
        "boundary": {
          "text": " And so, my fellow Americans, ask not what your country can do for you, ask what you can do for your country.",
          "words": [
            {
              "text": " And",
              "start_ms": 20,
              "end_ms": 230,
              "pieces": [
                " And"
              ]
            },
            {
              "text": " so,",
              "start_ms": 370,
              "end_ms": 570,
              "pieces": [
                " so",
                ","
              ]
            },
            {
              "text": " my",
              "start_ms": 570,
              "end_ms": 730,
              "pieces": [
                " my"
              ]
            },
            {
              "text": " fellow",
              "start_ms": 730,
              "end_ms": 1220,
              "pieces": [
                " fellow"
              ]
            },
            {
              "text": " Americans,",
              "start_ms": 1220,
              "end_ms": 2290,
              "pieces": [
                " Americans",
                ","
              ]
            },
            {
              "text": " ask",
              "start_ms": 2290,
              "end_ms": 2450,
              "pieces": [
                " ask"
              ]
            },
            {
              "text": " not",
              "start_ms": 2860,
              "end_ms": 3120,
              "pieces": [
                " not"
              ]
            },
            {
              "text": " what",
              "start_ms": 3390,
              "end_ms": 3500,
              "pieces": [
                " what"
              ]
            },
            {
              "text": " your",
              "start_ms": 3500,
              "end_ms": 3810,
              "pieces": [
                " your"
              ]
            },
            {
              "text": " country",
              "start_ms": 3950,
              "end_ms": 4370,
              "pieces": [
                " country"
              ]
            },
            {
              "text": " can",
              "start_ms": 4370,
              "end_ms": 4610,
              "pieces": [
                " can"
              ]
            },
            {
              "text": " do",
              "start_ms": 4620,
              "end_ms": 4780,
              "pieces": [
                " do"
              ]
            },
            {
              "text": " for",
              "start_ms": 4780,
              "end_ms": 5020,
              "pieces": [
                " for"
              ]
            },
            {
              "text": " you,",
              "start_ms": 5020,
              "end_ms": 5440,
              "pieces": [
                " you",
                ","
              ]
            },
            {
              "text": " ask",
              "start_ms": 5440,
              "end_ms": 5570,
              "pieces": [
                " ask"
              ]
            },
            {
              "text": " what",
              "start_ms": 5890,
              "end_ms": 6380,
              "pieces": [
                " what"
              ]
            },
            {
              "text": " you",
              "start_ms": 6380,
              "end_ms": 6800,
              "pieces": [
                " you"
              ]
            },
            {
              "text": " can",
              "start_ms": 6800,
              "end_ms": 7080,
              "pieces": [
                " can"
              ]
            },
            {
              "text": " do",
              "start_ms": 7080,
              "end_ms": 7280,
              "pieces": [
                " do"
              ]
            },
            {
              "text": " for",
              "start_ms": 7280,
              "end_ms": 7370,
              "pieces": [
                " for"
              ]
            },
            {
              "text": " your",
              "start_ms": 7430,
              "end_ms": 7600,
              "pieces": [
                " your"
              ]
            },
            {
              "text": " country.",
              "start_ms": 7600,
              "end_ms": 8070,
              "pieces": [
                " country",
                "."
              ]
            }
          ],
          "problems": [],
          "dtw_points": [
            {
              "text": " And",
              "point_cs": -1
            },
            {
              "text": " so",
              "point_cs": -1
            },
            {
              "text": ",",
              "point_cs": -1
            },
            {
              "text": " my",
              "point_cs": -1
            },
            {
              "text": " fellow",
              "point_cs": -1
            },
            {
              "text": " Americans",
              "point_cs": -1
            },
            {
              "text": ",",
              "point_cs": -1
            },
            {
              "text": " ask",
              "point_cs": -1
            },
            {
              "text": " not",
              "point_cs": -1
            },
            {
              "text": " what",
              "point_cs": -1
            },
            {
              "text": " your",
              "point_cs": -1
            },
            {
              "text": " country",
              "point_cs": -1
            },
            {
              "text": " can",
              "point_cs": -1
            },
            {
              "text": " do",
              "point_cs": -1
            },
            {
              "text": " for",
              "point_cs": -1
            },
            {
              "text": " you",
              "point_cs": -1
            },
            {
              "text": ",",
              "point_cs": -1
            },
            {
              "text": " ask",
              "point_cs": -1
            },
            {
              "text": " what",
              "point_cs": -1
            },
            {
              "text": " you",
              "point_cs": -1
            },
            {
              "text": " can",
              "point_cs": -1
            },
            {
              "text": " do",
              "point_cs": -1
            },
            {
              "text": " for",
              "point_cs": -1
            },
            {
              "text": " your",
              "point_cs": -1
            },
            {
              "text": " country",
              "point_cs": -1
            },
            {
              "text": ".",
              "point_cs": -1
            }
          ],
          "command": [
            "/tmp/atrain-whisper-a/.whisper-cli-unpatched",
            "-m",
            "/home/juergen/github/aTrain/.cache/whisper-cpp-evaluation/ggml-large-v3-turbo.bin",
            "-f",
            "/tmp/atrain-whisper-a-turbo-cpu-results/audio/boundary.wav",
            "-l",
            "en",
            "-t",
            "4",
            "-bs",
            "5",
            "-tp",
            "0",
            "-nf",
            "-ng",
            "-nfa",
            "-ojf",
            "-of",
            "/tmp/atrain-whisper-a-turbo-cpu-results/upstream-ordinary-vad-boundary",
            "--vad",
            "-vm",
            "/tmp/atrain-whisper-a/.ggml-silero-v5.1.2.bin"
          ],
          "wall_s": 19.159000475003268,
          "execution_status": "completed",
          "status": "passed"
        },
        "silence": {
          "text": "",
          "words": [],
          "problems": [],
          "dtw_points": [],
          "command": [
            "/tmp/atrain-whisper-a/.whisper-cli-unpatched",
            "-m",
            "/home/juergen/github/aTrain/.cache/whisper-cpp-evaluation/ggml-large-v3-turbo.bin",
            "-f",
            "/tmp/atrain-whisper-a-turbo-cpu-results/audio/silence.wav",
            "-l",
            "en",
            "-t",
            "4",
            "-bs",
            "5",
            "-tp",
            "0",
            "-nf",
            "-ng",
            "-nfa",
            "-ojf",
            "-of",
            "/tmp/atrain-whisper-a-turbo-cpu-results/upstream-ordinary-vad-silence",
            "--vad",
            "-vm",
            "/tmp/atrain-whisper-a/.ggml-silero-v5.1.2.bin"
          ],
          "wall_s": 1.5184296169900335,
          "execution_status": "completed",
          "status": "passed"
        },
        "noise": {
          "text": "",
          "words": [],
          "problems": [],
          "dtw_points": [],
          "command": [
            "/tmp/atrain-whisper-a/.whisper-cli-unpatched",
            "-m",
            "/home/juergen/github/aTrain/.cache/whisper-cpp-evaluation/ggml-large-v3-turbo.bin",
            "-f",
            "/tmp/atrain-whisper-a-turbo-cpu-results/audio/noise.wav",
            "-l",
            "en",
            "-t",
            "4",
            "-bs",
            "5",
            "-tp",
            "0",
            "-nf",
            "-ng",
            "-nfa",
            "-ojf",
            "-of",
            "/tmp/atrain-whisper-a-turbo-cpu-results/upstream-ordinary-vad-noise",
            "--vad",
            "-vm",
            "/tmp/atrain-whisper-a/.ggml-silero-v5.1.2.bin"
          ],
          "wall_s": 1.267495414998848,
          "execution_status": "completed",
          "status": "passed"
        },
        "german": {
          "text": " Hiro, Kapitel 8. Flach halten. Flach halten. Junge, du wirst es nicht packen. Das ist doch... Vergiss es. Vergiss es einfach. Doch, das hast du gut gemacht. Nein, so nicht. Netz, Netz. Hat berührt. Hat berührt. Vergiss alles, was man dir gesagt hat. Den wirst du nicht packen. Der ist gut.",
          "words": [
            {
              "text": " Hiro,",
              "start_ms": 40,
              "end_ms": 460,
              "pieces": [
                " Hi",
                "ro",
                ","
              ]
            },
            {
              "text": " Kapitel",
              "start_ms": 730,
              "end_ms": 1140,
              "pieces": [
                " Kap",
                "itel"
              ]
            },
            {
              "text": " 8.",
              "start_ms": 1140,
              "end_ms": 1650,
              "pieces": [
                " 8",
                "."
              ]
            },
            {
              "text": " Flach",
              "start_ms": 1650,
              "end_ms": 2000,
              "pieces": [
                " Fl",
                "ach"
              ]
            },
            {
              "text": " halten.",
              "start_ms": 2000,
              "end_ms": 2640,
              "pieces": [
                " halten",
                "."
              ]
            },
            {
              "text": " Flach",
              "start_ms": 2640,
              "end_ms": 3170,
              "pieces": [
                " Fl",
                "ach"
              ]
            },
            {
              "text": " halten.",
              "start_ms": 3170,
              "end_ms": 4130,
              "pieces": [
                " halten",
                "."
              ]
            },
            {
              "text": " Junge,",
              "start_ms": 4920,
              "end_ms": 4920,
              "pieces": [
                " Jun",
                "ge",
                ","
              ]
            },
            {
              "text": " du",
              "start_ms": 4920,
              "end_ms": 4920,
              "pieces": [
                " du"
              ]
            },
            {
              "text": " wirst",
              "start_ms": 4920,
              "end_ms": 5060,
              "pieces": [
                " w",
                "irst"
              ]
            },
            {
              "text": " es",
              "start_ms": 5060,
              "end_ms": 5100,
              "pieces": [
                " es"
              ]
            },
            {
              "text": " nicht",
              "start_ms": 5180,
              "end_ms": 5340,
              "pieces": [
                " nicht"
              ]
            },
            {
              "text": " packen.",
              "start_ms": 5650,
              "end_ms": 6180,
              "pieces": [
                " pack",
                "en",
                "."
              ]
            },
            {
              "text": " Das",
              "start_ms": 6180,
              "end_ms": 6390,
              "pieces": [
                " Das"
              ]
            },
            {
              "text": " ist",
              "start_ms": 6510,
              "end_ms": 6640,
              "pieces": [
                " ist"
              ]
            },
            {
              "text": " doch...",
              "start_ms": 6640,
              "end_ms": 7670,
              "pieces": [
                " doch",
                "..."
              ]
            },
            {
              "text": " Vergiss",
              "start_ms": 7670,
              "end_ms": 8100,
              "pieces": [
                " Verg",
                "iss"
              ]
            },
            {
              "text": " es.",
              "start_ms": 8100,
              "end_ms": 8380,
              "pieces": [
                " es",
                "."
              ]
            },
            {
              "text": " Vergiss",
              "start_ms": 8390,
              "end_ms": 8810,
              "pieces": [
                " Verg",
                "iss"
              ]
            },
            {
              "text": " es",
              "start_ms": 8930,
              "end_ms": 8940,
              "pieces": [
                " es"
              ]
            },
            {
              "text": " einfach.",
              "start_ms": 8940,
              "end_ms": 9600,
              "pieces": [
                " einfach",
                "."
              ]
            },
            {
              "text": " Doch,",
              "start_ms": 10160,
              "end_ms": 10160,
              "pieces": [
                " Doch",
                ","
              ]
            },
            {
              "text": " das",
              "start_ms": 10200,
              "end_ms": 10290,
              "pieces": [
                " das"
              ]
            },
            {
              "text": " hast",
              "start_ms": 10290,
              "end_ms": 10560,
              "pieces": [
                " hast"
              ]
            },
            {
              "text": " du",
              "start_ms": 10600,
              "end_ms": 10620,
              "pieces": [
                " du"
              ]
            },
            {
              "text": " gut",
              "start_ms": 10890,
              "end_ms": 10980,
              "pieces": [
                " gut"
              ]
            },
            {
              "text": " gemacht.",
              "start_ms": 10980,
              "end_ms": 11800,
              "pieces": [
                " gemacht",
                "."
              ]
            },
            {
              "text": " Nein,",
              "start_ms": 11800,
              "end_ms": 12450,
              "pieces": [
                " Nein",
                ","
              ]
            },
            {
              "text": " so",
              "start_ms": 12450,
              "end_ms": 12670,
              "pieces": [
                " so"
              ]
            },
            {
              "text": " nicht.",
              "start_ms": 12670,
              "end_ms": 13560,
              "pieces": [
                " nicht",
                "."
              ]
            },
            {
              "text": " Netz,",
              "start_ms": 13560,
              "end_ms": 14230,
              "pieces": [
                " Netz",
                ","
              ]
            },
            {
              "text": " Netz.",
              "start_ms": 14230,
              "end_ms": 15020,
              "pieces": [
                " Netz",
                "."
              ]
            },
            {
              "text": " Hat",
              "start_ms": 15150,
              "end_ms": 15270,
              "pieces": [
                " Hat"
              ]
            },
            {
              "text": " berührt.",
              "start_ms": 15270,
              "end_ms": 15990,
              "pieces": [
                " ber",
                "ührt",
                "."
              ]
            },
            {
              "text": " Hat",
              "start_ms": 16060,
              "end_ms": 16330,
              "pieces": [
                " Hat"
              ]
            },
            {
              "text": " berührt.",
              "start_ms": 16660,
              "end_ms": 17550,
              "pieces": [
                " ber",
                "ührt",
                "."
              ]
            },
            {
              "text": " Vergiss",
              "start_ms": 18420,
              "end_ms": 18420,
              "pieces": [
                " Verg",
                "iss"
              ]
            },
            {
              "text": " alles,",
              "start_ms": 18460,
              "end_ms": 18720,
              "pieces": [
                " alles",
                ","
              ]
            },
            {
              "text": " was",
              "start_ms": 18720,
              "end_ms": 18860,
              "pieces": [
                " was"
              ]
            },
            {
              "text": " man",
              "start_ms": 19150,
              "end_ms": 19200,
              "pieces": [
                " man"
              ]
            },
            {
              "text": " dir",
              "start_ms": 19200,
              "end_ms": 19440,
              "pieces": [
                " dir"
              ]
            },
            {
              "text": " gesagt",
              "start_ms": 19440,
              "end_ms": 19740,
              "pieces": [
                " gesagt"
              ]
            },
            {
              "text": " hat.",
              "start_ms": 20010,
              "end_ms": 20400,
              "pieces": [
                " hat",
                "."
              ]
            },
            {
              "text": " Den",
              "start_ms": 20400,
              "end_ms": 20640,
              "pieces": [
                " Den"
              ]
            },
            {
              "text": " wirst",
              "start_ms": 20640,
              "end_ms": 21040,
              "pieces": [
                " w",
                "irst"
              ]
            },
            {
              "text": " du",
              "start_ms": 21040,
              "end_ms": 21160,
              "pieces": [
                " du"
              ]
            },
            {
              "text": " nicht",
              "start_ms": 21530,
              "end_ms": 21600,
              "pieces": [
                " nicht"
              ]
            },
            {
              "text": " packen.",
              "start_ms": 21600,
              "end_ms": 22310,
              "pieces": [
                " pack",
                "en",
                "."
              ]
            },
            {
              "text": " Der",
              "start_ms": 22430,
              "end_ms": 22550,
              "pieces": [
                " Der"
              ]
            },
            {
              "text": " ist",
              "start_ms": 22550,
              "end_ms": 22660,
              "pieces": [
                " ist"
              ]
            },
            {
              "text": " gut.",
              "start_ms": 22770,
              "end_ms": 23120,
              "pieces": [
                " gut",
                "."
              ]
            }
          ],
          "problems": [
            "nonpositive word interval: ' Junge,'",
            "nonpositive word interval: ' du'",
            "nonpositive word interval: ' Doch,'",
            "nonpositive word interval: ' Vergiss'"
          ],
          "dtw_points": [
            {
              "text": " Hi",
              "point_cs": -1
            },
            {
              "text": "ro",
              "point_cs": -1
            },
            {
              "text": ",",
              "point_cs": -1
            },
            {
              "text": " Kap",
              "point_cs": -1
            },
            {
              "text": "itel",
              "point_cs": -1
            },
            {
              "text": " 8",
              "point_cs": -1
            },
            {
              "text": ".",
              "point_cs": -1
            },
            {
              "text": " Fl",
              "point_cs": -1
            },
            {
              "text": "ach",
              "point_cs": -1
            },
            {
              "text": " halten",
              "point_cs": -1
            },
            {
              "text": ".",
              "point_cs": -1
            },
            {
              "text": " Fl",
              "point_cs": -1
            },
            {
              "text": "ach",
              "point_cs": -1
            },
            {
              "text": " halten",
              "point_cs": -1
            },
            {
              "text": ".",
              "point_cs": -1
            },
            {
              "text": " Jun",
              "point_cs": -1
            },
            {
              "text": "ge",
              "point_cs": -1
            },
            {
              "text": ",",
              "point_cs": -1
            },
            {
              "text": " du",
              "point_cs": -1
            },
            {
              "text": " w",
              "point_cs": -1
            },
            {
              "text": "irst",
              "point_cs": -1
            },
            {
              "text": " es",
              "point_cs": -1
            },
            {
              "text": " nicht",
              "point_cs": -1
            },
            {
              "text": " pack",
              "point_cs": -1
            },
            {
              "text": "en",
              "point_cs": -1
            },
            {
              "text": ".",
              "point_cs": -1
            },
            {
              "text": " Das",
              "point_cs": -1
            },
            {
              "text": " ist",
              "point_cs": -1
            },
            {
              "text": " doch",
              "point_cs": -1
            },
            {
              "text": "...",
              "point_cs": -1
            },
            {
              "text": " Verg",
              "point_cs": -1
            },
            {
              "text": "iss",
              "point_cs": -1
            },
            {
              "text": " es",
              "point_cs": -1
            },
            {
              "text": ".",
              "point_cs": -1
            },
            {
              "text": " Verg",
              "point_cs": -1
            },
            {
              "text": "iss",
              "point_cs": -1
            },
            {
              "text": " es",
              "point_cs": -1
            },
            {
              "text": " einfach",
              "point_cs": -1
            },
            {
              "text": ".",
              "point_cs": -1
            },
            {
              "text": " Doch",
              "point_cs": -1
            },
            {
              "text": ",",
              "point_cs": -1
            },
            {
              "text": " das",
              "point_cs": -1
            },
            {
              "text": " hast",
              "point_cs": -1
            },
            {
              "text": " du",
              "point_cs": -1
            },
            {
              "text": " gut",
              "point_cs": -1
            },
            {
              "text": " gemacht",
              "point_cs": -1
            },
            {
              "text": ".",
              "point_cs": -1
            },
            {
              "text": " Nein",
              "point_cs": -1
            },
            {
              "text": ",",
              "point_cs": -1
            },
            {
              "text": " so",
              "point_cs": -1
            },
            {
              "text": " nicht",
              "point_cs": -1
            },
            {
              "text": ".",
              "point_cs": -1
            },
            {
              "text": " Netz",
              "point_cs": -1
            },
            {
              "text": ",",
              "point_cs": -1
            },
            {
              "text": " Netz",
              "point_cs": -1
            },
            {
              "text": ".",
              "point_cs": -1
            },
            {
              "text": " Hat",
              "point_cs": -1
            },
            {
              "text": " ber",
              "point_cs": -1
            },
            {
              "text": "ührt",
              "point_cs": -1
            },
            {
              "text": ".",
              "point_cs": -1
            },
            {
              "text": " Hat",
              "point_cs": -1
            },
            {
              "text": " ber",
              "point_cs": -1
            },
            {
              "text": "ührt",
              "point_cs": -1
            },
            {
              "text": ".",
              "point_cs": -1
            },
            {
              "text": " Verg",
              "point_cs": -1
            },
            {
              "text": "iss",
              "point_cs": -1
            },
            {
              "text": " alles",
              "point_cs": -1
            },
            {
              "text": ",",
              "point_cs": -1
            },
            {
              "text": " was",
              "point_cs": -1
            },
            {
              "text": " man",
              "point_cs": -1
            },
            {
              "text": " dir",
              "point_cs": -1
            },
            {
              "text": " gesagt",
              "point_cs": -1
            },
            {
              "text": " hat",
              "point_cs": -1
            },
            {
              "text": ".",
              "point_cs": -1
            },
            {
              "text": " Den",
              "point_cs": -1
            },
            {
              "text": " w",
              "point_cs": -1
            },
            {
              "text": "irst",
              "point_cs": -1
            },
            {
              "text": " du",
              "point_cs": -1
            },
            {
              "text": " nicht",
              "point_cs": -1
            },
            {
              "text": " pack",
              "point_cs": -1
            },
            {
              "text": "en",
              "point_cs": -1
            },
            {
              "text": ".",
              "point_cs": -1
            },
            {
              "text": " Der",
              "point_cs": -1
            },
            {
              "text": " ist",
              "point_cs": -1
            },
            {
              "text": " gut",
              "point_cs": -1
            },
            {
              "text": ".",
              "point_cs": -1
            }
          ],
          "command": [
            "/tmp/atrain-whisper-a/.whisper-cli-unpatched",
            "-m",
            "/home/juergen/github/aTrain/.cache/whisper-cpp-evaluation/ggml-large-v3-turbo.bin",
            "-f",
            "/tmp/atrain-whisper-a-turbo-cpu-results/audio/german.wav",
            "-l",
            "de",
            "-t",
            "4",
            "-bs",
            "5",
            "-tp",
            "0",
            "-nf",
            "-ng",
            "-nfa",
            "-ojf",
            "-of",
            "/tmp/atrain-whisper-a-turbo-cpu-results/upstream-ordinary-vad-german",
            "--vad",
            "-vm",
            "/tmp/atrain-whisper-a/.ggml-silero-v5.1.2.bin"
          ],
          "wall_s": 20.114232963998802,
          "execution_status": "completed",
          "status": "failed"
        },
        "japanese": {
          "text": "こんにちは",
          "words": [
            {
              "text": "こんにちは",
              "start_ms": 40,
              "end_ms": 720,
              "pieces": [
                "こんにちは"
              ]
            }
          ],
          "problems": [],
          "dtw_points": [
            {
              "text": "こんにちは",
              "point_cs": -1
            }
          ],
          "command": [
            "/tmp/atrain-whisper-a/.whisper-cli-unpatched",
            "-m",
            "/home/juergen/github/aTrain/.cache/whisper-cpp-evaluation/ggml-large-v3-turbo.bin",
            "-f",
            "/tmp/atrain-whisper-a-turbo-cpu-results/audio/japanese.wav",
            "-l",
            "ja",
            "-t",
            "4",
            "-bs",
            "5",
            "-tp",
            "0",
            "-nf",
            "-ng",
            "-nfa",
            "-ojf",
            "-of",
            "/tmp/atrain-whisper-a-turbo-cpu-results/upstream-ordinary-vad-japanese",
            "--vad",
            "-vm",
            "/tmp/atrain-whisper-a/.ggml-silero-v5.1.2.bin"
          ],
          "wall_s": 19.561231376996147,
          "execution_status": "completed",
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
            5020,
            5040,
            5190,
            5110,
            5110,
            5090,
            5140,
            5290,
            5160,
            5500,
            5500,
            5690,
            5690,
            5640,
            5970,
            6000,
            5620,
            5700,
            5360,
            5320,
            5320,
            5230,
            5240,
            5180,
            5180,
            5090,
            4970,
            4950,
            4950,
            4920,
            4920,
            4930,
            4930,
            4920,
            4920,
            4920,
            4920,
            4920,
            4920,
            4980,
            4920,
            4930,
            4930,
            4930
          ],
          "max_boundary_error_ms": 6000,
          "median_boundary_error_ms": 5100.0,
          "status": "failed"
        },
        "trailing": {
          "tolerance_ms": 50,
          "matched_words": 22,
          "unmatched_reference_words": 0,
          "unmatched_candidate_words": 0,
          "boundary_errors_ms": [
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0
          ],
          "max_boundary_error_ms": 0,
          "median_boundary_error_ms": 0.0,
          "status": "passed"
        },
        "boundary": {
          "tolerance_ms": 50,
          "matched_words": 22,
          "unmatched_reference_words": 0,
          "unmatched_candidate_words": 0,
          "boundary_errors_ms": [
            25020,
            25010,
            25020,
            25000,
            25000,
            24950,
            25000,
            25000,
            25000,
            25000,
            25000,
            25050,
            24980,
            24980,
            25040,
            25010,
            25010,
            25030,
            24890,
            25030,
            25030,
            25030,
            25030,
            25030,
            25030,
            25030,
            25030,
            25050,
            25050,
            25010,
            25010,
            25020,
            25020,
            25000,
            25000,
            25000,
            25000,
            25020,
            25020,
            25070,
            25010,
            25020,
            25020,
            25020
          ],
          "max_boundary_error_ms": 25070,
          "median_boundary_error_ms": 25020.0,
          "status": "failed"
        },
        "internal-first": {
          "tolerance_ms": 50,
          "matched_words": 22,
          "unmatched_reference_words": 0,
          "unmatched_candidate_words": 22,
          "boundary_errors_ms": [
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            100,
            100,
            20,
            360,
            600,
            580,
            410,
            80,
            310,
            310,
            290,
            170,
            200,
            140,
            140,
            120,
            110,
            20,
            10,
            10,
            0,
            0,
            20,
            20,
            20,
            20,
            0,
            0,
            0,
            0,
            60,
            60,
            40,
            40,
            10
          ],
          "max_boundary_error_ms": 600,
          "median_boundary_error_ms": 20.0,
          "status": "failed"
        },
        "internal-second": {
          "tolerance_ms": 50,
          "matched_words": 0,
          "unmatched_reference_words": 22,
          "unmatched_candidate_words": 0,
          "boundary_errors_ms": [],
          "max_boundary_error_ms": null,
          "median_boundary_error_ms": null,
          "status": "failed"
        }
      }
    },
    "patched-ordinary-vad": {
      "fixtures": {
        "base": {
          "text": " And so, my fellow Americans, ask not what your country can do for you, ask what you can do for your country.",
          "words": [
            {
              "text": " And",
              "start_ms": 330,
              "end_ms": 530,
              "pieces": [
                " And"
              ]
            },
            {
              "text": " so,",
              "start_ms": 680,
              "end_ms": 860,
              "pieces": [
                " so",
                ","
              ]
            },
            {
              "text": " my",
              "start_ms": 860,
              "end_ms": 970,
              "pieces": [
                " my"
              ]
            },
            {
              "text": " fellow",
              "start_ms": 1020,
              "end_ms": 1510,
              "pieces": [
                " fellow"
              ]
            },
            {
              "text": " Americans,",
              "start_ms": 1510,
              "end_ms": 3440,
              "pieces": [
                " Americans",
                ","
              ]
            },
            {
              "text": " ask",
              "start_ms": 3440,
              "end_ms": 3650,
              "pieces": [
                " ask"
              ]
            },
            {
              "text": " not",
              "start_ms": 4020,
              "end_ms": 4280,
              "pieces": [
                " not"
              ]
            },
            {
              "text": " what",
              "start_ms": 5410,
              "end_ms": 5490,
              "pieces": [
                " what"
              ]
            },
            {
              "text": " your",
              "start_ms": 5490,
              "end_ms": 5820,
              "pieces": [
                " your"
              ]
            },
            {
              "text": " country",
              "start_ms": 5820,
              "end_ms": 6380,
              "pieces": [
                " country"
              ]
            },
            {
              "text": " can",
              "start_ms": 6380,
              "end_ms": 6620,
              "pieces": [
                " can"
              ]
            },
            {
              "text": " do",
              "start_ms": 6630,
              "end_ms": 6790,
              "pieces": [
                " do"
              ]
            },
            {
              "text": " for",
              "start_ms": 6790,
              "end_ms": 7030,
              "pieces": [
                " for"
              ]
            },
            {
              "text": " you,",
              "start_ms": 7030,
              "end_ms": 7470,
              "pieces": [
                " you",
                ","
              ]
            },
            {
              "text": " ask",
              "start_ms": 7470,
              "end_ms": 7560,
              "pieces": [
                " ask"
              ]
            },
            {
              "text": " what",
              "start_ms": 8190,
              "end_ms": 8690,
              "pieces": [
                " what"
              ]
            },
            {
              "text": " you",
              "start_ms": 8690,
              "end_ms": 9090,
              "pieces": [
                " you"
              ]
            },
            {
              "text": " can",
              "start_ms": 9090,
              "end_ms": 9370,
              "pieces": [
                " can"
              ]
            },
            {
              "text": " do",
              "start_ms": 9370,
              "end_ms": 9590,
              "pieces": [
                " do"
              ]
            },
            {
              "text": " for",
              "start_ms": 9590,
              "end_ms": 9730,
              "pieces": [
                " for"
              ]
            },
            {
              "text": " your",
              "start_ms": 9730,
              "end_ms": 9910,
              "pieces": [
                " your"
              ]
            },
            {
              "text": " country.",
              "start_ms": 9910,
              "end_ms": 10380,
              "pieces": [
                " country",
                "."
              ]
            }
          ],
          "problems": [],
          "dtw_points": [
            {
              "text": " And",
              "point_cs": -1
            },
            {
              "text": " so",
              "point_cs": -1
            },
            {
              "text": ",",
              "point_cs": -1
            },
            {
              "text": " my",
              "point_cs": -1
            },
            {
              "text": " fellow",
              "point_cs": -1
            },
            {
              "text": " Americans",
              "point_cs": -1
            },
            {
              "text": ",",
              "point_cs": -1
            },
            {
              "text": " ask",
              "point_cs": -1
            },
            {
              "text": " not",
              "point_cs": -1
            },
            {
              "text": " what",
              "point_cs": -1
            },
            {
              "text": " your",
              "point_cs": -1
            },
            {
              "text": " country",
              "point_cs": -1
            },
            {
              "text": " can",
              "point_cs": -1
            },
            {
              "text": " do",
              "point_cs": -1
            },
            {
              "text": " for",
              "point_cs": -1
            },
            {
              "text": " you",
              "point_cs": -1
            },
            {
              "text": ",",
              "point_cs": -1
            },
            {
              "text": " ask",
              "point_cs": -1
            },
            {
              "text": " what",
              "point_cs": -1
            },
            {
              "text": " you",
              "point_cs": -1
            },
            {
              "text": " can",
              "point_cs": -1
            },
            {
              "text": " do",
              "point_cs": -1
            },
            {
              "text": " for",
              "point_cs": -1
            },
            {
              "text": " your",
              "point_cs": -1
            },
            {
              "text": " country",
              "point_cs": -1
            },
            {
              "text": ".",
              "point_cs": -1
            }
          ],
          "command": [
            "/tmp/atrain-whisper-a/.whisper-cli-patched",
            "-m",
            "/home/juergen/github/aTrain/.cache/whisper-cpp-evaluation/ggml-large-v3-turbo.bin",
            "-f",
            "/tmp/atrain-whisper-a-turbo-cpu-results/audio/base.wav",
            "-l",
            "en",
            "-t",
            "4",
            "-bs",
            "5",
            "-tp",
            "0",
            "-nf",
            "-ng",
            "-nfa",
            "-ojf",
            "-of",
            "/tmp/atrain-whisper-a-turbo-cpu-results/patched-ordinary-vad-base",
            "--vad",
            "-vm",
            "/tmp/atrain-whisper-a/.ggml-silero-v5.1.2.bin"
          ],
          "wall_s": 19.411097313000937,
          "execution_status": "completed",
          "status": "passed"
        },
        "leading": {
          "text": " And so, my fellow Americans, ask not what your country can do for you, ask what you can do for your country.",
          "words": [
            {
              "text": " And",
              "start_ms": 5330,
              "end_ms": 5510,
              "pieces": [
                " And"
              ]
            },
            {
              "text": " so,",
              "start_ms": 5510,
              "end_ms": 5770,
              "pieces": [
                " so",
                ","
              ]
            },
            {
              "text": " my",
              "start_ms": 5770,
              "end_ms": 5900,
              "pieces": [
                " my"
              ]
            },
            {
              "text": " fellow",
              "start_ms": 5900,
              "end_ms": 6240,
              "pieces": [
                " fellow"
              ]
            },
            {
              "text": " Americans,",
              "start_ms": 6370,
              "end_ms": 7100,
              "pieces": [
                " Americans",
                ","
              ]
            },
            {
              "text": " ask",
              "start_ms": 7100,
              "end_ms": 7120,
              "pieces": [
                " ask"
              ]
            },
            {
              "text": " not",
              "start_ms": 8290,
              "end_ms": 8600,
              "pieces": [
                " not"
              ]
            },
            {
              "text": " what",
              "start_ms": 8600,
              "end_ms": 8650,
              "pieces": [
                " what"
              ]
            },
            {
              "text": " your",
              "start_ms": 9030,
              "end_ms": 9280,
              "pieces": [
                " your"
              ]
            },
            {
              "text": " country",
              "start_ms": 10410,
              "end_ms": 11010,
              "pieces": [
                " country"
              ]
            },
            {
              "text": " can",
              "start_ms": 11010,
              "end_ms": 11340,
              "pieces": [
                " can"
              ]
            },
            {
              "text": " do",
              "start_ms": 11340,
              "end_ms": 11560,
              "pieces": [
                " do"
              ]
            },
            {
              "text": " for",
              "start_ms": 11560,
              "end_ms": 11890,
              "pieces": [
                " for"
              ]
            },
            {
              "text": " you,",
              "start_ms": 12010,
              "end_ms": 12470,
              "pieces": [
                " you",
                ","
              ]
            },
            {
              "text": " ask",
              "start_ms": 12470,
              "end_ms": 12590,
              "pieces": [
                " ask"
              ]
            },
            {
              "text": " what",
              "start_ms": 13190,
              "end_ms": 13680,
              "pieces": [
                " what"
              ]
            },
            {
              "text": " you",
              "start_ms": 13680,
              "end_ms": 14090,
              "pieces": [
                " you"
              ]
            },
            {
              "text": " can",
              "start_ms": 14090,
              "end_ms": 14370,
              "pieces": [
                " can"
              ]
            },
            {
              "text": " do",
              "start_ms": 14370,
              "end_ms": 14590,
              "pieces": [
                " do"
              ]
            },
            {
              "text": " for",
              "start_ms": 14590,
              "end_ms": 14670,
              "pieces": [
                " for"
              ]
            },
            {
              "text": " your",
              "start_ms": 14730,
              "end_ms": 14900,
              "pieces": [
                " your"
              ]
            },
            {
              "text": " country.",
              "start_ms": 14900,
              "end_ms": 15370,
              "pieces": [
                " country",
                "."
              ]
            }
          ],
          "problems": [],
          "dtw_points": [
            {
              "text": " And",
              "point_cs": -1
            },
            {
              "text": " so",
              "point_cs": -1
            },
            {
              "text": ",",
              "point_cs": -1
            },
            {
              "text": " my",
              "point_cs": -1
            },
            {
              "text": " fellow",
              "point_cs": -1
            },
            {
              "text": " Americans",
              "point_cs": -1
            },
            {
              "text": ",",
              "point_cs": -1
            },
            {
              "text": " ask",
              "point_cs": -1
            },
            {
              "text": " not",
              "point_cs": -1
            },
            {
              "text": " what",
              "point_cs": -1
            },
            {
              "text": " your",
              "point_cs": -1
            },
            {
              "text": " country",
              "point_cs": -1
            },
            {
              "text": " can",
              "point_cs": -1
            },
            {
              "text": " do",
              "point_cs": -1
            },
            {
              "text": " for",
              "point_cs": -1
            },
            {
              "text": " you",
              "point_cs": -1
            },
            {
              "text": ",",
              "point_cs": -1
            },
            {
              "text": " ask",
              "point_cs": -1
            },
            {
              "text": " what",
              "point_cs": -1
            },
            {
              "text": " you",
              "point_cs": -1
            },
            {
              "text": " can",
              "point_cs": -1
            },
            {
              "text": " do",
              "point_cs": -1
            },
            {
              "text": " for",
              "point_cs": -1
            },
            {
              "text": " your",
              "point_cs": -1
            },
            {
              "text": " country",
              "point_cs": -1
            },
            {
              "text": ".",
              "point_cs": -1
            }
          ],
          "command": [
            "/tmp/atrain-whisper-a/.whisper-cli-patched",
            "-m",
            "/home/juergen/github/aTrain/.cache/whisper-cpp-evaluation/ggml-large-v3-turbo.bin",
            "-f",
            "/tmp/atrain-whisper-a-turbo-cpu-results/audio/leading.wav",
            "-l",
            "en",
            "-t",
            "4",
            "-bs",
            "5",
            "-tp",
            "0",
            "-nf",
            "-ng",
            "-nfa",
            "-ojf",
            "-of",
            "/tmp/atrain-whisper-a-turbo-cpu-results/patched-ordinary-vad-leading",
            "--vad",
            "-vm",
            "/tmp/atrain-whisper-a/.ggml-silero-v5.1.2.bin"
          ],
          "wall_s": 19.610963433005963,
          "execution_status": "completed",
          "status": "passed"
        },
        "trailing": {
          "text": " And so, my fellow Americans, ask not what your country can do for you, ask what you can do for your country.",
          "words": [
            {
              "text": " And",
              "start_ms": 330,
              "end_ms": 530,
              "pieces": [
                " And"
              ]
            },
            {
              "text": " so,",
              "start_ms": 680,
              "end_ms": 860,
              "pieces": [
                " so",
                ","
              ]
            },
            {
              "text": " my",
              "start_ms": 860,
              "end_ms": 970,
              "pieces": [
                " my"
              ]
            },
            {
              "text": " fellow",
              "start_ms": 1020,
              "end_ms": 1510,
              "pieces": [
                " fellow"
              ]
            },
            {
              "text": " Americans,",
              "start_ms": 1510,
              "end_ms": 3440,
              "pieces": [
                " Americans",
                ","
              ]
            },
            {
              "text": " ask",
              "start_ms": 3440,
              "end_ms": 3650,
              "pieces": [
                " ask"
              ]
            },
            {
              "text": " not",
              "start_ms": 4020,
              "end_ms": 4280,
              "pieces": [
                " not"
              ]
            },
            {
              "text": " what",
              "start_ms": 5410,
              "end_ms": 5490,
              "pieces": [
                " what"
              ]
            },
            {
              "text": " your",
              "start_ms": 5490,
              "end_ms": 5820,
              "pieces": [
                " your"
              ]
            },
            {
              "text": " country",
              "start_ms": 5820,
              "end_ms": 6380,
              "pieces": [
                " country"
              ]
            },
            {
              "text": " can",
              "start_ms": 6380,
              "end_ms": 6620,
              "pieces": [
                " can"
              ]
            },
            {
              "text": " do",
              "start_ms": 6630,
              "end_ms": 6790,
              "pieces": [
                " do"
              ]
            },
            {
              "text": " for",
              "start_ms": 6790,
              "end_ms": 7030,
              "pieces": [
                " for"
              ]
            },
            {
              "text": " you,",
              "start_ms": 7030,
              "end_ms": 7470,
              "pieces": [
                " you",
                ","
              ]
            },
            {
              "text": " ask",
              "start_ms": 7470,
              "end_ms": 7560,
              "pieces": [
                " ask"
              ]
            },
            {
              "text": " what",
              "start_ms": 8190,
              "end_ms": 8690,
              "pieces": [
                " what"
              ]
            },
            {
              "text": " you",
              "start_ms": 8690,
              "end_ms": 9090,
              "pieces": [
                " you"
              ]
            },
            {
              "text": " can",
              "start_ms": 9090,
              "end_ms": 9370,
              "pieces": [
                " can"
              ]
            },
            {
              "text": " do",
              "start_ms": 9370,
              "end_ms": 9590,
              "pieces": [
                " do"
              ]
            },
            {
              "text": " for",
              "start_ms": 9590,
              "end_ms": 9730,
              "pieces": [
                " for"
              ]
            },
            {
              "text": " your",
              "start_ms": 9730,
              "end_ms": 9910,
              "pieces": [
                " your"
              ]
            },
            {
              "text": " country.",
              "start_ms": 9910,
              "end_ms": 10380,
              "pieces": [
                " country",
                "."
              ]
            }
          ],
          "problems": [],
          "dtw_points": [
            {
              "text": " And",
              "point_cs": -1
            },
            {
              "text": " so",
              "point_cs": -1
            },
            {
              "text": ",",
              "point_cs": -1
            },
            {
              "text": " my",
              "point_cs": -1
            },
            {
              "text": " fellow",
              "point_cs": -1
            },
            {
              "text": " Americans",
              "point_cs": -1
            },
            {
              "text": ",",
              "point_cs": -1
            },
            {
              "text": " ask",
              "point_cs": -1
            },
            {
              "text": " not",
              "point_cs": -1
            },
            {
              "text": " what",
              "point_cs": -1
            },
            {
              "text": " your",
              "point_cs": -1
            },
            {
              "text": " country",
              "point_cs": -1
            },
            {
              "text": " can",
              "point_cs": -1
            },
            {
              "text": " do",
              "point_cs": -1
            },
            {
              "text": " for",
              "point_cs": -1
            },
            {
              "text": " you",
              "point_cs": -1
            },
            {
              "text": ",",
              "point_cs": -1
            },
            {
              "text": " ask",
              "point_cs": -1
            },
            {
              "text": " what",
              "point_cs": -1
            },
            {
              "text": " you",
              "point_cs": -1
            },
            {
              "text": " can",
              "point_cs": -1
            },
            {
              "text": " do",
              "point_cs": -1
            },
            {
              "text": " for",
              "point_cs": -1
            },
            {
              "text": " your",
              "point_cs": -1
            },
            {
              "text": " country",
              "point_cs": -1
            },
            {
              "text": ".",
              "point_cs": -1
            }
          ],
          "command": [
            "/tmp/atrain-whisper-a/.whisper-cli-patched",
            "-m",
            "/home/juergen/github/aTrain/.cache/whisper-cpp-evaluation/ggml-large-v3-turbo.bin",
            "-f",
            "/tmp/atrain-whisper-a-turbo-cpu-results/audio/trailing.wav",
            "-l",
            "en",
            "-t",
            "4",
            "-bs",
            "5",
            "-tp",
            "0",
            "-nf",
            "-ng",
            "-nfa",
            "-ojf",
            "-of",
            "/tmp/atrain-whisper-a-turbo-cpu-results/patched-ordinary-vad-trailing",
            "--vad",
            "-vm",
            "/tmp/atrain-whisper-a/.ggml-silero-v5.1.2.bin"
          ],
          "wall_s": 19.81280915500247,
          "execution_status": "completed",
          "status": "passed"
        },
        "internal": {
          "text": " And so, my fellow Americans, ask not what your country can do for you, ask what you can do for your country. And so, my fellow Americans, ask not what your country can do for you, ask what you can do for your country.",
          "words": [
            {
              "text": " And",
              "start_ms": 330,
              "end_ms": 530,
              "pieces": [
                " And"
              ]
            },
            {
              "text": " so,",
              "start_ms": 680,
              "end_ms": 860,
              "pieces": [
                " so",
                ","
              ]
            },
            {
              "text": " my",
              "start_ms": 860,
              "end_ms": 970,
              "pieces": [
                " my"
              ]
            },
            {
              "text": " fellow",
              "start_ms": 1020,
              "end_ms": 1510,
              "pieces": [
                " fellow"
              ]
            },
            {
              "text": " Americans,",
              "start_ms": 1510,
              "end_ms": 3340,
              "pieces": [
                " Americans",
                ","
              ]
            },
            {
              "text": " ask",
              "start_ms": 3340,
              "end_ms": 3630,
              "pieces": [
                " ask"
              ]
            },
            {
              "text": " not",
              "start_ms": 3630,
              "end_ms": 3650,
              "pieces": [
                " not"
              ]
            },
            {
              "text": " what",
              "start_ms": 4030,
              "end_ms": 4280,
              "pieces": [
                " what"
              ]
            },
            {
              "text": " your",
              "start_ms": 5410,
              "end_ms": 5510,
              "pieces": [
                " your"
              ]
            },
            {
              "text": " country",
              "start_ms": 5510,
              "end_ms": 6090,
              "pieces": [
                " country"
              ]
            },
            {
              "text": " can",
              "start_ms": 6210,
              "end_ms": 6420,
              "pieces": [
                " can"
              ]
            },
            {
              "text": " do",
              "start_ms": 6490,
              "end_ms": 6650,
              "pieces": [
                " do"
              ]
            },
            {
              "text": " for",
              "start_ms": 6670,
              "end_ms": 6920,
              "pieces": [
                " for"
              ]
            },
            {
              "text": " you,",
              "start_ms": 7010,
              "end_ms": 7460,
              "pieces": [
                " you",
                ","
              ]
            },
            {
              "text": " ask",
              "start_ms": 7460,
              "end_ms": 7560,
              "pieces": [
                " ask"
              ]
            },
            {
              "text": " what",
              "start_ms": 8190,
              "end_ms": 8670,
              "pieces": [
                " what"
              ]
            },
            {
              "text": " you",
              "start_ms": 8670,
              "end_ms": 9070,
              "pieces": [
                " you"
              ]
            },
            {
              "text": " can",
              "start_ms": 9070,
              "end_ms": 9370,
              "pieces": [
                " can"
              ]
            },
            {
              "text": " do",
              "start_ms": 9370,
              "end_ms": 9590,
              "pieces": [
                " do"
              ]
            },
            {
              "text": " for",
              "start_ms": 9590,
              "end_ms": 9790,
              "pieces": [
                " for"
              ]
            },
            {
              "text": " your",
              "start_ms": 9790,
              "end_ms": 9950,
              "pieces": [
                " your"
              ]
            },
            {
              "text": " country.",
              "start_ms": 9950,
              "end_ms": 10370,
              "pieces": [
                " country",
                "."
              ]
            },
            {
              "text": " And",
              "start_ms": 10410,
              "end_ms": 10590,
              "pieces": [
                " And"
              ]
            },
            {
              "text": " so,",
              "start_ms": 16350,
              "end_ms": 16560,
              "pieces": [
                " so",
                ","
              ]
            },
            {
              "text": " my",
              "start_ms": 16560,
              "end_ms": 16740,
              "pieces": [
                " my"
              ]
            },
            {
              "text": " fellow",
              "start_ms": 16740,
              "end_ms": 17280,
              "pieces": [
                " fellow"
              ]
            },
            {
              "text": " Americans,",
              "start_ms": 17280,
              "end_ms": 19270,
              "pieces": [
                " Americans",
                ","
              ]
            },
            {
              "text": " ask",
              "start_ms": 19270,
              "end_ms": 19320,
              "pieces": [
                " ask"
              ]
            },
            {
              "text": " not",
              "start_ms": 19670,
              "end_ms": 19720,
              "pieces": [
                " not"
              ]
            },
            {
              "text": " what",
              "start_ms": 19720,
              "end_ms": 19970,
              "pieces": [
                " what"
              ]
            },
            {
              "text": " your",
              "start_ms": 20260,
              "end_ms": 20380,
              "pieces": [
                " your"
              ]
            },
            {
              "text": " country",
              "start_ms": 21380,
              "end_ms": 21880,
              "pieces": [
                " country"
              ]
            },
            {
              "text": " can",
              "start_ms": 21880,
              "end_ms": 22070,
              "pieces": [
                " can"
              ]
            },
            {
              "text": " do",
              "start_ms": 22150,
              "end_ms": 22330,
              "pieces": [
                " do"
              ]
            },
            {
              "text": " for",
              "start_ms": 22330,
              "end_ms": 22570,
              "pieces": [
                " for"
              ]
            },
            {
              "text": " you,",
              "start_ms": 22660,
              "end_ms": 23050,
              "pieces": [
                " you",
                ","
              ]
            },
            {
              "text": " ask",
              "start_ms": 23050,
              "end_ms": 23170,
              "pieces": [
                " ask"
              ]
            },
            {
              "text": " what",
              "start_ms": 23530,
              "end_ms": 23650,
              "pieces": [
                " what"
              ]
            },
            {
              "text": " you",
              "start_ms": 23650,
              "end_ms": 24160,
              "pieces": [
                " you"
              ]
            },
            {
              "text": " can",
              "start_ms": 24280,
              "end_ms": 24400,
              "pieces": [
                " can"
              ]
            },
            {
              "text": " do",
              "start_ms": 24560,
              "end_ms": 24710,
              "pieces": [
                " do"
              ]
            },
            {
              "text": " for",
              "start_ms": 24710,
              "end_ms": 24970,
              "pieces": [
                " for"
              ]
            },
            {
              "text": " your",
              "start_ms": 24970,
              "end_ms": 25320,
              "pieces": [
                " your"
              ]
            },
            {
              "text": " country.",
              "start_ms": 25370,
              "end_ms": 26310,
              "pieces": [
                " country",
                "."
              ]
            }
          ],
          "problems": [],
          "dtw_points": [
            {
              "text": " And",
              "point_cs": -1
            },
            {
              "text": " so",
              "point_cs": -1
            },
            {
              "text": ",",
              "point_cs": -1
            },
            {
              "text": " my",
              "point_cs": -1
            },
            {
              "text": " fellow",
              "point_cs": -1
            },
            {
              "text": " Americans",
              "point_cs": -1
            },
            {
              "text": ",",
              "point_cs": -1
            },
            {
              "text": " ask",
              "point_cs": -1
            },
            {
              "text": " not",
              "point_cs": -1
            },
            {
              "text": " what",
              "point_cs": -1
            },
            {
              "text": " your",
              "point_cs": -1
            },
            {
              "text": " country",
              "point_cs": -1
            },
            {
              "text": " can",
              "point_cs": -1
            },
            {
              "text": " do",
              "point_cs": -1
            },
            {
              "text": " for",
              "point_cs": -1
            },
            {
              "text": " you",
              "point_cs": -1
            },
            {
              "text": ",",
              "point_cs": -1
            },
            {
              "text": " ask",
              "point_cs": -1
            },
            {
              "text": " what",
              "point_cs": -1
            },
            {
              "text": " you",
              "point_cs": -1
            },
            {
              "text": " can",
              "point_cs": -1
            },
            {
              "text": " do",
              "point_cs": -1
            },
            {
              "text": " for",
              "point_cs": -1
            },
            {
              "text": " your",
              "point_cs": -1
            },
            {
              "text": " country",
              "point_cs": -1
            },
            {
              "text": ".",
              "point_cs": -1
            },
            {
              "text": " And",
              "point_cs": -1
            },
            {
              "text": " so",
              "point_cs": -1
            },
            {
              "text": ",",
              "point_cs": -1
            },
            {
              "text": " my",
              "point_cs": -1
            },
            {
              "text": " fellow",
              "point_cs": -1
            },
            {
              "text": " Americans",
              "point_cs": -1
            },
            {
              "text": ",",
              "point_cs": -1
            },
            {
              "text": " ask",
              "point_cs": -1
            },
            {
              "text": " not",
              "point_cs": -1
            },
            {
              "text": " what",
              "point_cs": -1
            },
            {
              "text": " your",
              "point_cs": -1
            },
            {
              "text": " country",
              "point_cs": -1
            },
            {
              "text": " can",
              "point_cs": -1
            },
            {
              "text": " do",
              "point_cs": -1
            },
            {
              "text": " for",
              "point_cs": -1
            },
            {
              "text": " you",
              "point_cs": -1
            },
            {
              "text": ",",
              "point_cs": -1
            },
            {
              "text": " ask",
              "point_cs": -1
            },
            {
              "text": " what",
              "point_cs": -1
            },
            {
              "text": " you",
              "point_cs": -1
            },
            {
              "text": " can",
              "point_cs": -1
            },
            {
              "text": " do",
              "point_cs": -1
            },
            {
              "text": " for",
              "point_cs": -1
            },
            {
              "text": " your",
              "point_cs": -1
            },
            {
              "text": " country",
              "point_cs": -1
            },
            {
              "text": ".",
              "point_cs": -1
            }
          ],
          "command": [
            "/tmp/atrain-whisper-a/.whisper-cli-patched",
            "-m",
            "/home/juergen/github/aTrain/.cache/whisper-cpp-evaluation/ggml-large-v3-turbo.bin",
            "-f",
            "/tmp/atrain-whisper-a-turbo-cpu-results/audio/internal.wav",
            "-l",
            "en",
            "-t",
            "4",
            "-bs",
            "5",
            "-tp",
            "0",
            "-nf",
            "-ng",
            "-nfa",
            "-ojf",
            "-of",
            "/tmp/atrain-whisper-a-turbo-cpu-results/patched-ordinary-vad-internal",
            "--vad",
            "-vm",
            "/tmp/atrain-whisper-a/.ggml-silero-v5.1.2.bin"
          ],
          "wall_s": 21.22347320400877,
          "execution_status": "completed",
          "status": "passed"
        },
        "boundary": {
          "text": " And so, my fellow Americans, ask not what your country can do for you, ask what you can do for your country.",
          "words": [
            {
              "text": " And",
              "start_ms": 25330,
              "end_ms": 25540,
              "pieces": [
                " And"
              ]
            },
            {
              "text": " so,",
              "start_ms": 25680,
              "end_ms": 25880,
              "pieces": [
                " so",
                ","
              ]
            },
            {
              "text": " my",
              "start_ms": 25880,
              "end_ms": 26040,
              "pieces": [
                " my"
              ]
            },
            {
              "text": " fellow",
              "start_ms": 26040,
              "end_ms": 26530,
              "pieces": [
                " fellow"
              ]
            },
            {
              "text": " Americans,",
              "start_ms": 26530,
              "end_ms": 28490,
              "pieces": [
                " Americans",
                ","
              ]
            },
            {
              "text": " ask",
              "start_ms": 28490,
              "end_ms": 28650,
              "pieces": [
                " ask"
              ]
            },
            {
              "text": " not",
              "start_ms": 29020,
              "end_ms": 29280,
              "pieces": [
                " not"
              ]
            },
            {
              "text": " what",
              "start_ms": 30410,
              "end_ms": 30520,
              "pieces": [
                " what"
              ]
            },
            {
              "text": " your",
              "start_ms": 30520,
              "end_ms": 30830,
              "pieces": [
                " your"
              ]
            },
            {
              "text": " country",
              "start_ms": 30970,
              "end_ms": 31390,
              "pieces": [
                " country"
              ]
            },
            {
              "text": " can",
              "start_ms": 31390,
              "end_ms": 31630,
              "pieces": [
                " can"
              ]
            },
            {
              "text": " do",
              "start_ms": 31640,
              "end_ms": 31800,
              "pieces": [
                " do"
              ]
            },
            {
              "text": " for",
              "start_ms": 31800,
              "end_ms": 32040,
              "pieces": [
                " for"
              ]
            },
            {
              "text": " you,",
              "start_ms": 32040,
              "end_ms": 32460,
              "pieces": [
                " you",
                ","
              ]
            },
            {
              "text": " ask",
              "start_ms": 32460,
              "end_ms": 32590,
              "pieces": [
                " ask"
              ]
            },
            {
              "text": " what",
              "start_ms": 33190,
              "end_ms": 33680,
              "pieces": [
                " what"
              ]
            },
            {
              "text": " you",
              "start_ms": 33680,
              "end_ms": 34100,
              "pieces": [
                " you"
              ]
            },
            {
              "text": " can",
              "start_ms": 34100,
              "end_ms": 34380,
              "pieces": [
                " can"
              ]
            },
            {
              "text": " do",
              "start_ms": 34380,
              "end_ms": 34580,
              "pieces": [
                " do"
              ]
            },
            {
              "text": " for",
              "start_ms": 34580,
              "end_ms": 34670,
              "pieces": [
                " for"
              ]
            },
            {
              "text": " your",
              "start_ms": 34730,
              "end_ms": 34900,
              "pieces": [
                " your"
              ]
            },
            {
              "text": " country.",
              "start_ms": 34900,
              "end_ms": 35370,
              "pieces": [
                " country",
                "."
              ]
            }
          ],
          "problems": [],
          "dtw_points": [
            {
              "text": " And",
              "point_cs": -1
            },
            {
              "text": " so",
              "point_cs": -1
            },
            {
              "text": ",",
              "point_cs": -1
            },
            {
              "text": " my",
              "point_cs": -1
            },
            {
              "text": " fellow",
              "point_cs": -1
            },
            {
              "text": " Americans",
              "point_cs": -1
            },
            {
              "text": ",",
              "point_cs": -1
            },
            {
              "text": " ask",
              "point_cs": -1
            },
            {
              "text": " not",
              "point_cs": -1
            },
            {
              "text": " what",
              "point_cs": -1
            },
            {
              "text": " your",
              "point_cs": -1
            },
            {
              "text": " country",
              "point_cs": -1
            },
            {
              "text": " can",
              "point_cs": -1
            },
            {
              "text": " do",
              "point_cs": -1
            },
            {
              "text": " for",
              "point_cs": -1
            },
            {
              "text": " you",
              "point_cs": -1
            },
            {
              "text": ",",
              "point_cs": -1
            },
            {
              "text": " ask",
              "point_cs": -1
            },
            {
              "text": " what",
              "point_cs": -1
            },
            {
              "text": " you",
              "point_cs": -1
            },
            {
              "text": " can",
              "point_cs": -1
            },
            {
              "text": " do",
              "point_cs": -1
            },
            {
              "text": " for",
              "point_cs": -1
            },
            {
              "text": " your",
              "point_cs": -1
            },
            {
              "text": " country",
              "point_cs": -1
            },
            {
              "text": ".",
              "point_cs": -1
            }
          ],
          "command": [
            "/tmp/atrain-whisper-a/.whisper-cli-patched",
            "-m",
            "/home/juergen/github/aTrain/.cache/whisper-cpp-evaluation/ggml-large-v3-turbo.bin",
            "-f",
            "/tmp/atrain-whisper-a-turbo-cpu-results/audio/boundary.wav",
            "-l",
            "en",
            "-t",
            "4",
            "-bs",
            "5",
            "-tp",
            "0",
            "-nf",
            "-ng",
            "-nfa",
            "-ojf",
            "-of",
            "/tmp/atrain-whisper-a-turbo-cpu-results/patched-ordinary-vad-boundary",
            "--vad",
            "-vm",
            "/tmp/atrain-whisper-a/.ggml-silero-v5.1.2.bin"
          ],
          "wall_s": 20.413067246001447,
          "execution_status": "completed",
          "status": "passed"
        },
        "silence": {
          "text": "",
          "words": [],
          "problems": [],
          "dtw_points": [],
          "command": [
            "/tmp/atrain-whisper-a/.whisper-cli-patched",
            "-m",
            "/home/juergen/github/aTrain/.cache/whisper-cpp-evaluation/ggml-large-v3-turbo.bin",
            "-f",
            "/tmp/atrain-whisper-a-turbo-cpu-results/audio/silence.wav",
            "-l",
            "en",
            "-t",
            "4",
            "-bs",
            "5",
            "-tp",
            "0",
            "-nf",
            "-ng",
            "-nfa",
            "-ojf",
            "-of",
            "/tmp/atrain-whisper-a-turbo-cpu-results/patched-ordinary-vad-silence",
            "--vad",
            "-vm",
            "/tmp/atrain-whisper-a/.ggml-silero-v5.1.2.bin"
          ],
          "wall_s": 1.5675537470087875,
          "execution_status": "completed",
          "status": "passed"
        },
        "noise": {
          "text": "",
          "words": [],
          "problems": [],
          "dtw_points": [],
          "command": [
            "/tmp/atrain-whisper-a/.whisper-cli-patched",
            "-m",
            "/home/juergen/github/aTrain/.cache/whisper-cpp-evaluation/ggml-large-v3-turbo.bin",
            "-f",
            "/tmp/atrain-whisper-a-turbo-cpu-results/audio/noise.wav",
            "-l",
            "en",
            "-t",
            "4",
            "-bs",
            "5",
            "-tp",
            "0",
            "-nf",
            "-ng",
            "-nfa",
            "-ojf",
            "-of",
            "/tmp/atrain-whisper-a-turbo-cpu-results/patched-ordinary-vad-noise",
            "--vad",
            "-vm",
            "/tmp/atrain-whisper-a/.ggml-silero-v5.1.2.bin"
          ],
          "wall_s": 1.5676333690062165,
          "execution_status": "completed",
          "status": "passed"
        },
        "german": {
          "text": " Hiro, Kapitel 8. Flach halten. Flach halten. Junge, du wirst es nicht packen. Das ist doch... Vergiss es. Vergiss es einfach. Doch, das hast du gut gemacht. Nein, so nicht. Netz, Netz. Hat berührt. Hat berührt. Vergiss alles, was man dir gesagt hat. Den wirst du nicht packen. Der ist gut.",
          "words": [
            {
              "text": " Hiro,",
              "start_ms": 750,
              "end_ms": 1170,
              "pieces": [
                " Hi",
                "ro",
                ","
              ]
            },
            {
              "text": " Kapitel",
              "start_ms": 1990,
              "end_ms": 2390,
              "pieces": [
                " Kap",
                "itel"
              ]
            },
            {
              "text": " 8.",
              "start_ms": 2390,
              "end_ms": 4470,
              "pieces": [
                " 8",
                "."
              ]
            },
            {
              "text": " Flach",
              "start_ms": 4470,
              "end_ms": 4820,
              "pieces": [
                " Fl",
                "ach"
              ]
            },
            {
              "text": " halten.",
              "start_ms": 4820,
              "end_ms": 5460,
              "pieces": [
                " halten",
                "."
              ]
            },
            {
              "text": " Flach",
              "start_ms": 5460,
              "end_ms": 6530,
              "pieces": [
                " Fl",
                "ach"
              ]
            },
            {
              "text": " halten.",
              "start_ms": 6530,
              "end_ms": 7490,
              "pieces": [
                " halten",
                "."
              ]
            },
            {
              "text": " Junge,",
              "start_ms": 9250,
              "end_ms": 9260,
              "pieces": [
                " Jun",
                "ge",
                ","
              ]
            },
            {
              "text": " du",
              "start_ms": 9250,
              "end_ms": 9260,
              "pieces": [
                " du"
              ]
            },
            {
              "text": " wirst",
              "start_ms": 9250,
              "end_ms": 9340,
              "pieces": [
                " w",
                "irst"
              ]
            },
            {
              "text": " es",
              "start_ms": 9340,
              "end_ms": 9380,
              "pieces": [
                " es"
              ]
            },
            {
              "text": " nicht",
              "start_ms": 9460,
              "end_ms": 9620,
              "pieces": [
                " nicht"
              ]
            },
            {
              "text": " packen.",
              "start_ms": 9930,
              "end_ms": 10460,
              "pieces": [
                " pack",
                "en",
                "."
              ]
            },
            {
              "text": " Das",
              "start_ms": 10460,
              "end_ms": 10820,
              "pieces": [
                " Das"
              ]
            },
            {
              "text": " ist",
              "start_ms": 10850,
              "end_ms": 10980,
              "pieces": [
                " ist"
              ]
            },
            {
              "text": " doch...",
              "start_ms": 10980,
              "end_ms": 12010,
              "pieces": [
                " doch",
                "..."
              ]
            },
            {
              "text": " Vergiss",
              "start_ms": 12010,
              "end_ms": 12440,
              "pieces": [
                " Verg",
                "iss"
              ]
            },
            {
              "text": " es.",
              "start_ms": 12440,
              "end_ms": 12720,
              "pieces": [
                " es",
                "."
              ]
            },
            {
              "text": " Vergiss",
              "start_ms": 12730,
              "end_ms": 13150,
              "pieces": [
                " Verg",
                "iss"
              ]
            },
            {
              "text": " es",
              "start_ms": 13270,
              "end_ms": 13280,
              "pieces": [
                " es"
              ]
            },
            {
              "text": " einfach.",
              "start_ms": 13280,
              "end_ms": 13940,
              "pieces": [
                " einfach",
                "."
              ]
            },
            {
              "text": " Doch,",
              "start_ms": 14780,
              "end_ms": 14790,
              "pieces": [
                " Doch",
                ","
              ]
            },
            {
              "text": " das",
              "start_ms": 14820,
              "end_ms": 14910,
              "pieces": [
                " das"
              ]
            },
            {
              "text": " hast",
              "start_ms": 14910,
              "end_ms": 15180,
              "pieces": [
                " hast"
              ]
            },
            {
              "text": " du",
              "start_ms": 15220,
              "end_ms": 15240,
              "pieces": [
                " du"
              ]
            },
            {
              "text": " gut",
              "start_ms": 16210,
              "end_ms": 16300,
              "pieces": [
                " gut"
              ]
            },
            {
              "text": " gemacht.",
              "start_ms": 16300,
              "end_ms": 17120,
              "pieces": [
                " gemacht",
                "."
              ]
            },
            {
              "text": " Nein,",
              "start_ms": 17120,
              "end_ms": 17860,
              "pieces": [
                " Nein",
                ","
              ]
            },
            {
              "text": " so",
              "start_ms": 17860,
              "end_ms": 18080,
              "pieces": [
                " so"
              ]
            },
            {
              "text": " nicht.",
              "start_ms": 18080,
              "end_ms": 18970,
              "pieces": [
                " nicht",
                "."
              ]
            },
            {
              "text": " Netz,",
              "start_ms": 18970,
              "end_ms": 19640,
              "pieces": [
                " Netz",
                ","
              ]
            },
            {
              "text": " Netz.",
              "start_ms": 19640,
              "end_ms": 20430,
              "pieces": [
                " Netz",
                "."
              ]
            },
            {
              "text": " Hat",
              "start_ms": 20560,
              "end_ms": 20680,
              "pieces": [
                " Hat"
              ]
            },
            {
              "text": " berührt.",
              "start_ms": 20680,
              "end_ms": 21400,
              "pieces": [
                " ber",
                "ührt",
                "."
              ]
            },
            {
              "text": " Hat",
              "start_ms": 21470,
              "end_ms": 21740,
              "pieces": [
                " Hat"
              ]
            },
            {
              "text": " berührt.",
              "start_ms": 22070,
              "end_ms": 22960,
              "pieces": [
                " ber",
                "ührt",
                "."
              ]
            },
            {
              "text": " Vergiss",
              "start_ms": 24250,
              "end_ms": 24260,
              "pieces": [
                " Verg",
                "iss"
              ]
            },
            {
              "text": " alles,",
              "start_ms": 24290,
              "end_ms": 24550,
              "pieces": [
                " alles",
                ","
              ]
            },
            {
              "text": " was",
              "start_ms": 24550,
              "end_ms": 24690,
              "pieces": [
                " was"
              ]
            },
            {
              "text": " man",
              "start_ms": 24980,
              "end_ms": 25030,
              "pieces": [
                " man"
              ]
            },
            {
              "text": " dir",
              "start_ms": 25030,
              "end_ms": 25270,
              "pieces": [
                " dir"
              ]
            },
            {
              "text": " gesagt",
              "start_ms": 25270,
              "end_ms": 25570,
              "pieces": [
                " gesagt"
              ]
            },
            {
              "text": " hat.",
              "start_ms": 25840,
              "end_ms": 26230,
              "pieces": [
                " hat",
                "."
              ]
            },
            {
              "text": " Den",
              "start_ms": 26230,
              "end_ms": 26470,
              "pieces": [
                " Den"
              ]
            },
            {
              "text": " wirst",
              "start_ms": 26470,
              "end_ms": 27160,
              "pieces": [
                " w",
                "irst"
              ]
            },
            {
              "text": " du",
              "start_ms": 27160,
              "end_ms": 27280,
              "pieces": [
                " du"
              ]
            },
            {
              "text": " nicht",
              "start_ms": 27650,
              "end_ms": 27720,
              "pieces": [
                " nicht"
              ]
            },
            {
              "text": " packen.",
              "start_ms": 27720,
              "end_ms": 28430,
              "pieces": [
                " pack",
                "en",
                "."
              ]
            },
            {
              "text": " Der",
              "start_ms": 28550,
              "end_ms": 28570,
              "pieces": [
                " Der"
              ]
            },
            {
              "text": " ist",
              "start_ms": 28570,
              "end_ms": 29070,
              "pieces": [
                " ist"
              ]
            },
            {
              "text": " gut.",
              "start_ms": 29180,
              "end_ms": 29530,
              "pieces": [
                " gut",
                "."
              ]
            }
          ],
          "problems": [
            "overlapping word interval: ' du'",
            "overlapping word interval: ' wirst'"
          ],
          "dtw_points": [
            {
              "text": " Hi",
              "point_cs": -1
            },
            {
              "text": "ro",
              "point_cs": -1
            },
            {
              "text": ",",
              "point_cs": -1
            },
            {
              "text": " Kap",
              "point_cs": -1
            },
            {
              "text": "itel",
              "point_cs": -1
            },
            {
              "text": " 8",
              "point_cs": -1
            },
            {
              "text": ".",
              "point_cs": -1
            },
            {
              "text": " Fl",
              "point_cs": -1
            },
            {
              "text": "ach",
              "point_cs": -1
            },
            {
              "text": " halten",
              "point_cs": -1
            },
            {
              "text": ".",
              "point_cs": -1
            },
            {
              "text": " Fl",
              "point_cs": -1
            },
            {
              "text": "ach",
              "point_cs": -1
            },
            {
              "text": " halten",
              "point_cs": -1
            },
            {
              "text": ".",
              "point_cs": -1
            },
            {
              "text": " Jun",
              "point_cs": -1
            },
            {
              "text": "ge",
              "point_cs": -1
            },
            {
              "text": ",",
              "point_cs": -1
            },
            {
              "text": " du",
              "point_cs": -1
            },
            {
              "text": " w",
              "point_cs": -1
            },
            {
              "text": "irst",
              "point_cs": -1
            },
            {
              "text": " es",
              "point_cs": -1
            },
            {
              "text": " nicht",
              "point_cs": -1
            },
            {
              "text": " pack",
              "point_cs": -1
            },
            {
              "text": "en",
              "point_cs": -1
            },
            {
              "text": ".",
              "point_cs": -1
            },
            {
              "text": " Das",
              "point_cs": -1
            },
            {
              "text": " ist",
              "point_cs": -1
            },
            {
              "text": " doch",
              "point_cs": -1
            },
            {
              "text": "...",
              "point_cs": -1
            },
            {
              "text": " Verg",
              "point_cs": -1
            },
            {
              "text": "iss",
              "point_cs": -1
            },
            {
              "text": " es",
              "point_cs": -1
            },
            {
              "text": ".",
              "point_cs": -1
            },
            {
              "text": " Verg",
              "point_cs": -1
            },
            {
              "text": "iss",
              "point_cs": -1
            },
            {
              "text": " es",
              "point_cs": -1
            },
            {
              "text": " einfach",
              "point_cs": -1
            },
            {
              "text": ".",
              "point_cs": -1
            },
            {
              "text": " Doch",
              "point_cs": -1
            },
            {
              "text": ",",
              "point_cs": -1
            },
            {
              "text": " das",
              "point_cs": -1
            },
            {
              "text": " hast",
              "point_cs": -1
            },
            {
              "text": " du",
              "point_cs": -1
            },
            {
              "text": " gut",
              "point_cs": -1
            },
            {
              "text": " gemacht",
              "point_cs": -1
            },
            {
              "text": ".",
              "point_cs": -1
            },
            {
              "text": " Nein",
              "point_cs": -1
            },
            {
              "text": ",",
              "point_cs": -1
            },
            {
              "text": " so",
              "point_cs": -1
            },
            {
              "text": " nicht",
              "point_cs": -1
            },
            {
              "text": ".",
              "point_cs": -1
            },
            {
              "text": " Netz",
              "point_cs": -1
            },
            {
              "text": ",",
              "point_cs": -1
            },
            {
              "text": " Netz",
              "point_cs": -1
            },
            {
              "text": ".",
              "point_cs": -1
            },
            {
              "text": " Hat",
              "point_cs": -1
            },
            {
              "text": " ber",
              "point_cs": -1
            },
            {
              "text": "ührt",
              "point_cs": -1
            },
            {
              "text": ".",
              "point_cs": -1
            },
            {
              "text": " Hat",
              "point_cs": -1
            },
            {
              "text": " ber",
              "point_cs": -1
            },
            {
              "text": "ührt",
              "point_cs": -1
            },
            {
              "text": ".",
              "point_cs": -1
            },
            {
              "text": " Verg",
              "point_cs": -1
            },
            {
              "text": "iss",
              "point_cs": -1
            },
            {
              "text": " alles",
              "point_cs": -1
            },
            {
              "text": ",",
              "point_cs": -1
            },
            {
              "text": " was",
              "point_cs": -1
            },
            {
              "text": " man",
              "point_cs": -1
            },
            {
              "text": " dir",
              "point_cs": -1
            },
            {
              "text": " gesagt",
              "point_cs": -1
            },
            {
              "text": " hat",
              "point_cs": -1
            },
            {
              "text": ".",
              "point_cs": -1
            },
            {
              "text": " Den",
              "point_cs": -1
            },
            {
              "text": " w",
              "point_cs": -1
            },
            {
              "text": "irst",
              "point_cs": -1
            },
            {
              "text": " du",
              "point_cs": -1
            },
            {
              "text": " nicht",
              "point_cs": -1
            },
            {
              "text": " pack",
              "point_cs": -1
            },
            {
              "text": "en",
              "point_cs": -1
            },
            {
              "text": ".",
              "point_cs": -1
            },
            {
              "text": " Der",
              "point_cs": -1
            },
            {
              "text": " ist",
              "point_cs": -1
            },
            {
              "text": " gut",
              "point_cs": -1
            },
            {
              "text": ".",
              "point_cs": -1
            }
          ],
          "command": [
            "/tmp/atrain-whisper-a/.whisper-cli-patched",
            "-m",
            "/home/juergen/github/aTrain/.cache/whisper-cpp-evaluation/ggml-large-v3-turbo.bin",
            "-f",
            "/tmp/atrain-whisper-a-turbo-cpu-results/audio/german.wav",
            "-l",
            "de",
            "-t",
            "4",
            "-bs",
            "5",
            "-tp",
            "0",
            "-nf",
            "-ng",
            "-nfa",
            "-ojf",
            "-of",
            "/tmp/atrain-whisper-a-turbo-cpu-results/patched-ordinary-vad-german",
            "--vad",
            "-vm",
            "/tmp/atrain-whisper-a/.ggml-silero-v5.1.2.bin"
          ],
          "wall_s": 22.117509396994137,
          "execution_status": "completed",
          "status": "failed"
        },
        "japanese": {
          "text": "こんにちは",
          "words": [
            {
              "text": "こんにちは",
              "start_ms": 390,
              "end_ms": 1070,
              "pieces": [
                "こんにちは"
              ]
            }
          ],
          "problems": [],
          "dtw_points": [
            {
              "text": "こんにちは",
              "point_cs": -1
            }
          ],
          "command": [
            "/tmp/atrain-whisper-a/.whisper-cli-patched",
            "-m",
            "/home/juergen/github/aTrain/.cache/whisper-cpp-evaluation/ggml-large-v3-turbo.bin",
            "-f",
            "/tmp/atrain-whisper-a-turbo-cpu-results/audio/japanese.wav",
            "-l",
            "ja",
            "-t",
            "4",
            "-bs",
            "5",
            "-tp",
            "0",
            "-nf",
            "-ng",
            "-nfa",
            "-ojf",
            "-of",
            "/tmp/atrain-whisper-a-turbo-cpu-results/patched-ordinary-vad-japanese",
            "--vad",
            "-vm",
            "/tmp/atrain-whisper-a/.ggml-silero-v5.1.2.bin"
          ],
          "wall_s": 19.613836038988666,
          "execution_status": "completed",
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
            0,
            20,
            170,
            90,
            90,
            70,
            120,
            270,
            140,
            1340,
            1340,
            1530,
            730,
            680,
            1810,
            1840,
            1460,
            1540,
            410,
            370,
            370,
            280,
            290,
            230,
            230,
            140,
            20,
            0,
            0,
            30,
            0,
            10,
            10,
            0,
            0,
            0,
            0,
            0,
            0,
            60,
            0,
            10,
            10,
            10
          ],
          "max_boundary_error_ms": 1840,
          "median_boundary_error_ms": 90.0,
          "status": "failed"
        },
        "trailing": {
          "tolerance_ms": 50,
          "matched_words": 22,
          "unmatched_reference_words": 0,
          "unmatched_candidate_words": 0,
          "boundary_errors_ms": [
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0
          ],
          "max_boundary_error_ms": 0,
          "median_boundary_error_ms": 0.0,
          "status": "passed"
        },
        "boundary": {
          "tolerance_ms": 50,
          "matched_words": 22,
          "unmatched_reference_words": 0,
          "unmatched_candidate_words": 0,
          "boundary_errors_ms": [
            0,
            10,
            0,
            20,
            20,
            70,
            20,
            20,
            20,
            50,
            50,
            0,
            0,
            0,
            0,
            30,
            30,
            10,
            150,
            10,
            10,
            10,
            10,
            10,
            10,
            10,
            10,
            10,
            10,
            30,
            0,
            10,
            10,
            10,
            10,
            10,
            10,
            10,
            10,
            60,
            0,
            10,
            10,
            10
          ],
          "max_boundary_error_ms": 150,
          "median_boundary_error_ms": 10.0,
          "status": "failed"
        },
        "internal-first": {
          "tolerance_ms": 50,
          "matched_words": 22,
          "unmatched_reference_words": 0,
          "unmatched_candidate_words": 1,
          "boundary_errors_ms": [
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            100,
            100,
            20,
            390,
            630,
            1380,
            1210,
            80,
            310,
            310,
            290,
            170,
            200,
            140,
            140,
            120,
            110,
            20,
            10,
            10,
            0,
            0,
            20,
            20,
            20,
            20,
            0,
            0,
            0,
            0,
            60,
            60,
            40,
            40,
            10
          ],
          "max_boundary_error_ms": 1380,
          "median_boundary_error_ms": 20.0,
          "status": "failed"
        },
        "internal-second": {
          "tolerance_ms": 50,
          "matched_words": 21,
          "unmatched_reference_words": 1,
          "unmatched_candidate_words": 0,
          "boundary_errors_ms": [
            330,
            300,
            300,
            230,
            280,
            230,
            230,
            170,
            170,
            330,
            350,
            560,
            1690,
            1520,
            1230,
            1440,
            440,
            500,
            500,
            550,
            480,
            460,
            460,
            460,
            370,
            420,
            420,
            390,
            660,
            1040,
            1040,
            930,
            810,
            970,
            810,
            880,
            880,
            760,
            760,
            590,
            540,
            70
          ],
          "max_boundary_error_ms": 1690,
          "median_boundary_error_ms": 490.0,
          "status": "failed"
        }
      }
    },
    "upstream-dtw-vad": {
      "fixtures": {
        "base": {
          "text": " And so, my fellow Americans, ask not what your country can do for you, ask what you can do for your country.",
          "words": [
            {
              "text": " And",
              "start_ms": 40,
              "end_ms": 240,
              "pieces": [
                " And"
              ]
            },
            {
              "text": " so,",
              "start_ms": 390,
              "end_ms": 570,
              "pieces": [
                " so",
                ","
              ]
            },
            {
              "text": " my",
              "start_ms": 570,
              "end_ms": 680,
              "pieces": [
                " my"
              ]
            },
            {
              "text": " fellow",
              "start_ms": 730,
              "end_ms": 1220,
              "pieces": [
                " fellow"
              ]
            },
            {
              "text": " Americans,",
              "start_ms": 1220,
              "end_ms": 2290,
              "pieces": [
                " Americans",
                ","
              ]
            },
            {
              "text": " ask",
              "start_ms": 2290,
              "end_ms": 2500,
              "pieces": [
                " ask"
              ]
            },
            {
              "text": " not",
              "start_ms": 2840,
              "end_ms": 3100,
              "pieces": [
                " not"
              ]
            },
            {
              "text": " what",
              "start_ms": 3430,
              "end_ms": 3510,
              "pieces": [
                " what"
              ]
            },
            {
              "text": " your",
              "start_ms": 3510,
              "end_ms": 3840,
              "pieces": [
                " your"
              ]
            },
            {
              "text": " country",
              "start_ms": 3840,
              "end_ms": 4400,
              "pieces": [
                " country"
              ]
            },
            {
              "text": " can",
              "start_ms": 4400,
              "end_ms": 4640,
              "pieces": [
                " can"
              ]
            },
            {
              "text": " do",
              "start_ms": 4650,
              "end_ms": 4810,
              "pieces": [
                " do"
              ]
            },
            {
              "text": " for",
              "start_ms": 4810,
              "end_ms": 5050,
              "pieces": [
                " for"
              ]
            },
            {
              "text": " you,",
              "start_ms": 5050,
              "end_ms": 5490,
              "pieces": [
                " you",
                ","
              ]
            },
            {
              "text": " ask",
              "start_ms": 5490,
              "end_ms": 5580,
              "pieces": [
                " ask"
              ]
            },
            {
              "text": " what",
              "start_ms": 5900,
              "end_ms": 6400,
              "pieces": [
                " what"
              ]
            },
            {
              "text": " you",
              "start_ms": 6400,
              "end_ms": 6800,
              "pieces": [
                " you"
              ]
            },
            {
              "text": " can",
              "start_ms": 6800,
              "end_ms": 7080,
              "pieces": [
                " can"
              ]
            },
            {
              "text": " do",
              "start_ms": 7080,
              "end_ms": 7300,
              "pieces": [
                " do"
              ]
            },
            {
              "text": " for",
              "start_ms": 7300,
              "end_ms": 7440,
              "pieces": [
                " for"
              ]
            },
            {
              "text": " your",
              "start_ms": 7440,
              "end_ms": 7620,
              "pieces": [
                " your"
              ]
            },
            {
              "text": " country.",
              "start_ms": 7620,
              "end_ms": 8090,
              "pieces": [
                " country",
                "."
              ]
            }
          ],
          "problems": [],
          "dtw_points": [
            {
              "text": " And",
              "point_cs": 22
            },
            {
              "text": " so",
              "point_cs": 56
            },
            {
              "text": ",",
              "point_cs": 80
            },
            {
              "text": " my",
              "point_cs": 92
            },
            {
              "text": " fellow",
              "point_cs": 126
            },
            {
              "text": " Americans",
              "point_cs": 182
            },
            {
              "text": ",",
              "point_cs": 220
            },
            {
              "text": " ask",
              "point_cs": 262
            },
            {
              "text": " not",
              "point_cs": 310
            },
            {
              "text": " what",
              "point_cs": 358
            },
            {
              "text": " your",
              "point_cs": 382
            },
            {
              "text": " country",
              "point_cs": 426
            },
            {
              "text": " can",
              "point_cs": 464
            },
            {
              "text": " do",
              "point_cs": 484
            },
            {
              "text": " for",
              "point_cs": 508
            },
            {
              "text": " you",
              "point_cs": 542
            },
            {
              "text": ",",
              "point_cs": 578
            },
            {
              "text": " ask",
              "point_cs": 622
            },
            {
              "text": " what",
              "point_cs": 648
            },
            {
              "text": " you",
              "point_cs": 674
            },
            {
              "text": " can",
              "point_cs": 706
            },
            {
              "text": " do",
              "point_cs": 726
            },
            {
              "text": " for",
              "point_cs": 748
            },
            {
              "text": " your",
              "point_cs": 766
            },
            {
              "text": " country",
              "point_cs": 808
            },
            {
              "text": ".",
              "point_cs": 808
            }
          ],
          "command": [
            "/tmp/atrain-whisper-a/.whisper-cli-unpatched",
            "-m",
            "/home/juergen/github/aTrain/.cache/whisper-cpp-evaluation/ggml-large-v3-turbo.bin",
            "-f",
            "/tmp/atrain-whisper-a-turbo-cpu-results/audio/base.wav",
            "-l",
            "en",
            "-t",
            "4",
            "-bs",
            "5",
            "-tp",
            "0",
            "-nf",
            "-ng",
            "-nfa",
            "-ojf",
            "-of",
            "/tmp/atrain-whisper-a-turbo-cpu-results/upstream-dtw-vad-base",
            "--vad",
            "-vm",
            "/tmp/atrain-whisper-a/.ggml-silero-v5.1.2.bin",
            "--dtw",
            "large.v3.turbo"
          ],
          "wall_s": 20.311832079998567,
          "execution_status": "completed",
          "status": "passed"
        },
        "leading": {
          "text": " And so, my fellow Americans, ask not what your country can do for you, ask what you can do for your country.",
          "words": [
            {
              "text": " And",
              "start_ms": 20,
              "end_ms": 200,
              "pieces": [
                " And"
              ]
            },
            {
              "text": " so,",
              "start_ms": 200,
              "end_ms": 460,
              "pieces": [
                " so",
                ","
              ]
            },
            {
              "text": " my",
              "start_ms": 460,
              "end_ms": 590,
              "pieces": [
                " my"
              ]
            },
            {
              "text": " fellow",
              "start_ms": 590,
              "end_ms": 930,
              "pieces": [
                " fellow"
              ]
            },
            {
              "text": " Americans,",
              "start_ms": 1060,
              "end_ms": 1790,
              "pieces": [
                " Americans",
                ","
              ]
            },
            {
              "text": " ask",
              "start_ms": 1790,
              "end_ms": 1810,
              "pieces": [
                " ask"
              ]
            },
            {
              "text": " not",
              "start_ms": 2150,
              "end_ms": 2460,
              "pieces": [
                " not"
              ]
            },
            {
              "text": " what",
              "start_ms": 2460,
              "end_ms": 2510,
              "pieces": [
                " what"
              ]
            },
            {
              "text": " your",
              "start_ms": 2890,
              "end_ms": 3140,
              "pieces": [
                " your"
              ]
            },
            {
              "text": " country",
              "start_ms": 3480,
              "end_ms": 4080,
              "pieces": [
                " country"
              ]
            },
            {
              "text": " can",
              "start_ms": 4080,
              "end_ms": 4410,
              "pieces": [
                " can"
              ]
            },
            {
              "text": " do",
              "start_ms": 4410,
              "end_ms": 4630,
              "pieces": [
                " do"
              ]
            },
            {
              "text": " for",
              "start_ms": 4630,
              "end_ms": 4960,
              "pieces": [
                " for"
              ]
            },
            {
              "text": " you,",
              "start_ms": 5080,
              "end_ms": 5540,
              "pieces": [
                " you",
                ","
              ]
            },
            {
              "text": " ask",
              "start_ms": 5540,
              "end_ms": 5660,
              "pieces": [
                " ask"
              ]
            },
            {
              "text": " what",
              "start_ms": 5980,
              "end_ms": 6470,
              "pieces": [
                " what"
              ]
            },
            {
              "text": " you",
              "start_ms": 6470,
              "end_ms": 6880,
              "pieces": [
                " you"
              ]
            },
            {
              "text": " can",
              "start_ms": 6880,
              "end_ms": 7160,
              "pieces": [
                " can"
              ]
            },
            {
              "text": " do",
              "start_ms": 7160,
              "end_ms": 7380,
              "pieces": [
                " do"
              ]
            },
            {
              "text": " for",
              "start_ms": 7380,
              "end_ms": 7460,
              "pieces": [
                " for"
              ]
            },
            {
              "text": " your",
              "start_ms": 7520,
              "end_ms": 7690,
              "pieces": [
                " your"
              ]
            },
            {
              "text": " country.",
              "start_ms": 7690,
              "end_ms": 8160,
              "pieces": [
                " country",
                "."
              ]
            }
          ],
          "problems": [],
          "dtw_points": [
            {
              "text": " And",
              "point_cs": 22
            },
            {
              "text": " so",
              "point_cs": 56
            },
            {
              "text": ",",
              "point_cs": 78
            },
            {
              "text": " my",
              "point_cs": 90
            },
            {
              "text": " fellow",
              "point_cs": 124
            },
            {
              "text": " Americans",
              "point_cs": 180
            },
            {
              "text": ",",
              "point_cs": 220
            },
            {
              "text": " ask",
              "point_cs": 264
            },
            {
              "text": " not",
              "point_cs": 316
            },
            {
              "text": " what",
              "point_cs": 362
            },
            {
              "text": " your",
              "point_cs": 388
            },
            {
              "text": " country",
              "point_cs": 432
            },
            {
              "text": " can",
              "point_cs": 468
            },
            {
              "text": " do",
              "point_cs": 490
            },
            {
              "text": " for",
              "point_cs": 514
            },
            {
              "text": " you",
              "point_cs": 548
            },
            {
              "text": ",",
              "point_cs": 590
            },
            {
              "text": " ask",
              "point_cs": 630
            },
            {
              "text": " what",
              "point_cs": 656
            },
            {
              "text": " you",
              "point_cs": 684
            },
            {
              "text": " can",
              "point_cs": 714
            },
            {
              "text": " do",
              "point_cs": 734
            },
            {
              "text": " for",
              "point_cs": 756
            },
            {
              "text": " your",
              "point_cs": 776
            },
            {
              "text": " country",
              "point_cs": 814
            },
            {
              "text": ".",
              "point_cs": 814
            }
          ],
          "command": [
            "/tmp/atrain-whisper-a/.whisper-cli-unpatched",
            "-m",
            "/home/juergen/github/aTrain/.cache/whisper-cpp-evaluation/ggml-large-v3-turbo.bin",
            "-f",
            "/tmp/atrain-whisper-a-turbo-cpu-results/audio/leading.wav",
            "-l",
            "en",
            "-t",
            "4",
            "-bs",
            "5",
            "-tp",
            "0",
            "-nf",
            "-ng",
            "-nfa",
            "-ojf",
            "-of",
            "/tmp/atrain-whisper-a-turbo-cpu-results/upstream-dtw-vad-leading",
            "--vad",
            "-vm",
            "/tmp/atrain-whisper-a/.ggml-silero-v5.1.2.bin",
            "--dtw",
            "large.v3.turbo"
          ],
          "wall_s": 19.660031623003306,
          "execution_status": "completed",
          "status": "passed"
        },
        "trailing": {
          "text": " And so, my fellow Americans, ask not what your country can do for you, ask what you can do for your country.",
          "words": [
            {
              "text": " And",
              "start_ms": 40,
              "end_ms": 240,
              "pieces": [
                " And"
              ]
            },
            {
              "text": " so,",
              "start_ms": 390,
              "end_ms": 570,
              "pieces": [
                " so",
                ","
              ]
            },
            {
              "text": " my",
              "start_ms": 570,
              "end_ms": 680,
              "pieces": [
                " my"
              ]
            },
            {
              "text": " fellow",
              "start_ms": 730,
              "end_ms": 1220,
              "pieces": [
                " fellow"
              ]
            },
            {
              "text": " Americans,",
              "start_ms": 1220,
              "end_ms": 2290,
              "pieces": [
                " Americans",
                ","
              ]
            },
            {
              "text": " ask",
              "start_ms": 2290,
              "end_ms": 2500,
              "pieces": [
                " ask"
              ]
            },
            {
              "text": " not",
              "start_ms": 2840,
              "end_ms": 3100,
              "pieces": [
                " not"
              ]
            },
            {
              "text": " what",
              "start_ms": 3430,
              "end_ms": 3510,
              "pieces": [
                " what"
              ]
            },
            {
              "text": " your",
              "start_ms": 3510,
              "end_ms": 3840,
              "pieces": [
                " your"
              ]
            },
            {
              "text": " country",
              "start_ms": 3840,
              "end_ms": 4400,
              "pieces": [
                " country"
              ]
            },
            {
              "text": " can",
              "start_ms": 4400,
              "end_ms": 4640,
              "pieces": [
                " can"
              ]
            },
            {
              "text": " do",
              "start_ms": 4650,
              "end_ms": 4810,
              "pieces": [
                " do"
              ]
            },
            {
              "text": " for",
              "start_ms": 4810,
              "end_ms": 5050,
              "pieces": [
                " for"
              ]
            },
            {
              "text": " you,",
              "start_ms": 5050,
              "end_ms": 5490,
              "pieces": [
                " you",
                ","
              ]
            },
            {
              "text": " ask",
              "start_ms": 5490,
              "end_ms": 5580,
              "pieces": [
                " ask"
              ]
            },
            {
              "text": " what",
              "start_ms": 5900,
              "end_ms": 6400,
              "pieces": [
                " what"
              ]
            },
            {
              "text": " you",
              "start_ms": 6400,
              "end_ms": 6800,
              "pieces": [
                " you"
              ]
            },
            {
              "text": " can",
              "start_ms": 6800,
              "end_ms": 7080,
              "pieces": [
                " can"
              ]
            },
            {
              "text": " do",
              "start_ms": 7080,
              "end_ms": 7300,
              "pieces": [
                " do"
              ]
            },
            {
              "text": " for",
              "start_ms": 7300,
              "end_ms": 7440,
              "pieces": [
                " for"
              ]
            },
            {
              "text": " your",
              "start_ms": 7440,
              "end_ms": 7620,
              "pieces": [
                " your"
              ]
            },
            {
              "text": " country.",
              "start_ms": 7620,
              "end_ms": 8090,
              "pieces": [
                " country",
                "."
              ]
            }
          ],
          "problems": [],
          "dtw_points": [
            {
              "text": " And",
              "point_cs": 22
            },
            {
              "text": " so",
              "point_cs": 56
            },
            {
              "text": ",",
              "point_cs": 80
            },
            {
              "text": " my",
              "point_cs": 92
            },
            {
              "text": " fellow",
              "point_cs": 126
            },
            {
              "text": " Americans",
              "point_cs": 182
            },
            {
              "text": ",",
              "point_cs": 220
            },
            {
              "text": " ask",
              "point_cs": 262
            },
            {
              "text": " not",
              "point_cs": 310
            },
            {
              "text": " what",
              "point_cs": 358
            },
            {
              "text": " your",
              "point_cs": 382
            },
            {
              "text": " country",
              "point_cs": 426
            },
            {
              "text": " can",
              "point_cs": 464
            },
            {
              "text": " do",
              "point_cs": 484
            },
            {
              "text": " for",
              "point_cs": 508
            },
            {
              "text": " you",
              "point_cs": 542
            },
            {
              "text": ",",
              "point_cs": 578
            },
            {
              "text": " ask",
              "point_cs": 622
            },
            {
              "text": " what",
              "point_cs": 648
            },
            {
              "text": " you",
              "point_cs": 674
            },
            {
              "text": " can",
              "point_cs": 706
            },
            {
              "text": " do",
              "point_cs": 726
            },
            {
              "text": " for",
              "point_cs": 748
            },
            {
              "text": " your",
              "point_cs": 766
            },
            {
              "text": " country",
              "point_cs": 808
            },
            {
              "text": ".",
              "point_cs": 808
            }
          ],
          "command": [
            "/tmp/atrain-whisper-a/.whisper-cli-unpatched",
            "-m",
            "/home/juergen/github/aTrain/.cache/whisper-cpp-evaluation/ggml-large-v3-turbo.bin",
            "-f",
            "/tmp/atrain-whisper-a-turbo-cpu-results/audio/trailing.wav",
            "-l",
            "en",
            "-t",
            "4",
            "-bs",
            "5",
            "-tp",
            "0",
            "-nf",
            "-ng",
            "-nfa",
            "-ojf",
            "-of",
            "/tmp/atrain-whisper-a-turbo-cpu-results/upstream-dtw-vad-trailing",
            "--vad",
            "-vm",
            "/tmp/atrain-whisper-a/.ggml-silero-v5.1.2.bin",
            "--dtw",
            "large.v3.turbo"
          ],
          "wall_s": 19.714844492991688,
          "execution_status": "completed",
          "status": "passed"
        },
        "internal": {
          "text": " And so, my fellow Americans, ask not what your country can do for you, ask what you can do for your country. And so, my fellow Americans, ask not what your country can do for you, ask what you can do for your country.",
          "words": [
            {
              "text": " And",
              "start_ms": 40,
              "end_ms": 240,
              "pieces": [
                " And"
              ]
            },
            {
              "text": " so,",
              "start_ms": 390,
              "end_ms": 570,
              "pieces": [
                " so",
                ","
              ]
            },
            {
              "text": " my",
              "start_ms": 570,
              "end_ms": 680,
              "pieces": [
                " my"
              ]
            },
            {
              "text": " fellow",
              "start_ms": 730,
              "end_ms": 1220,
              "pieces": [
                " fellow"
              ]
            },
            {
              "text": " Americans,",
              "start_ms": 1220,
              "end_ms": 2190,
              "pieces": [
                " Americans",
                ","
              ]
            },
            {
              "text": " ask",
              "start_ms": 2190,
              "end_ms": 2480,
              "pieces": [
                " ask"
              ]
            },
            {
              "text": " not",
              "start_ms": 2480,
              "end_ms": 2500,
              "pieces": [
                " not"
              ]
            },
            {
              "text": " what",
              "start_ms": 2850,
              "end_ms": 3100,
              "pieces": [
                " what"
              ]
            },
            {
              "text": " your",
              "start_ms": 3430,
              "end_ms": 3530,
              "pieces": [
                " your"
              ]
            },
            {
              "text": " country",
              "start_ms": 3530,
              "end_ms": 4110,
              "pieces": [
                " country"
              ]
            },
            {
              "text": " can",
              "start_ms": 4230,
              "end_ms": 4440,
              "pieces": [
                " can"
              ]
            },
            {
              "text": " do",
              "start_ms": 4510,
              "end_ms": 4670,
              "pieces": [
                " do"
              ]
            },
            {
              "text": " for",
              "start_ms": 4690,
              "end_ms": 4940,
              "pieces": [
                " for"
              ]
            },
            {
              "text": " you,",
              "start_ms": 5030,
              "end_ms": 5480,
              "pieces": [
                " you",
                ","
              ]
            },
            {
              "text": " ask",
              "start_ms": 5480,
              "end_ms": 5580,
              "pieces": [
                " ask"
              ]
            },
            {
              "text": " what",
              "start_ms": 5900,
              "end_ms": 6380,
              "pieces": [
                " what"
              ]
            },
            {
              "text": " you",
              "start_ms": 6380,
              "end_ms": 6780,
              "pieces": [
                " you"
              ]
            },
            {
              "text": " can",
              "start_ms": 6780,
              "end_ms": 7080,
              "pieces": [
                " can"
              ]
            },
            {
              "text": " do",
              "start_ms": 7080,
              "end_ms": 7300,
              "pieces": [
                " do"
              ]
            },
            {
              "text": " for",
              "start_ms": 7300,
              "end_ms": 7500,
              "pieces": [
                " for"
              ]
            },
            {
              "text": " your",
              "start_ms": 7500,
              "end_ms": 7660,
              "pieces": [
                " your"
              ]
            },
            {
              "text": " country.",
              "start_ms": 7660,
              "end_ms": 8080,
              "pieces": [
                " country",
                "."
              ]
            },
            {
              "text": " And",
              "start_ms": 8120,
              "end_ms": 8330,
              "pieces": [
                " And"
              ]
            },
            {
              "text": " so,",
              "start_ms": 8470,
              "end_ms": 8710,
              "pieces": [
                " so",
                ","
              ]
            },
            {
              "text": " my",
              "start_ms": 8710,
              "end_ms": 8890,
              "pieces": [
                " my"
              ]
            },
            {
              "text": " fellow",
              "start_ms": 8890,
              "end_ms": 9430,
              "pieces": [
                " fellow"
              ]
            },
            {
              "text": " Americans,",
              "start_ms": 9430,
              "end_ms": 10430,
              "pieces": [
                " Americans",
                ","
              ]
            },
            {
              "text": " ask",
              "start_ms": 10430,
              "end_ms": 10570,
              "pieces": [
                " ask"
              ]
            },
            {
              "text": " not",
              "start_ms": 10920,
              "end_ms": 10970,
              "pieces": [
                " not"
              ]
            },
            {
              "text": " what",
              "start_ms": 10970,
              "end_ms": 11180,
              "pieces": [
                " what"
              ]
            },
            {
              "text": " your",
              "start_ms": 11510,
              "end_ms": 11670,
              "pieces": [
                " your"
              ]
            },
            {
              "text": " country",
              "start_ms": 11750,
              "end_ms": 12330,
              "pieces": [
                " country"
              ]
            },
            {
              "text": " can",
              "start_ms": 12330,
              "end_ms": 12520,
              "pieces": [
                " can"
              ]
            },
            {
              "text": " do",
              "start_ms": 12600,
              "end_ms": 12780,
              "pieces": [
                " do"
              ]
            },
            {
              "text": " for",
              "start_ms": 12780,
              "end_ms": 13020,
              "pieces": [
                " for"
              ]
            },
            {
              "text": " you,",
              "start_ms": 13110,
              "end_ms": 13500,
              "pieces": [
                " you",
                ","
              ]
            },
            {
              "text": " ask",
              "start_ms": 13500,
              "end_ms": 13620,
              "pieces": [
                " ask"
              ]
            },
            {
              "text": " what",
              "start_ms": 13980,
              "end_ms": 14130,
              "pieces": [
                " what"
              ]
            },
            {
              "text": " you",
              "start_ms": 14130,
              "end_ms": 14250,
              "pieces": [
                " you"
              ]
            },
            {
              "text": " can",
              "start_ms": 14420,
              "end_ms": 14540,
              "pieces": [
                " can"
              ]
            },
            {
              "text": " do",
              "start_ms": 14700,
              "end_ms": 14850,
              "pieces": [
                " do"
              ]
            },
            {
              "text": " for",
              "start_ms": 14850,
              "end_ms": 15110,
              "pieces": [
                " for"
              ]
            },
            {
              "text": " your",
              "start_ms": 15110,
              "end_ms": 15460,
              "pieces": [
                " your"
              ]
            },
            {
              "text": " country.",
              "start_ms": 15510,
              "end_ms": 16450,
              "pieces": [
                " country",
                "."
              ]
            }
          ],
          "problems": [],
          "dtw_points": [
            {
              "text": " And",
              "point_cs": 22
            },
            {
              "text": " so",
              "point_cs": 56
            },
            {
              "text": ",",
              "point_cs": 80
            },
            {
              "text": " my",
              "point_cs": 92
            },
            {
              "text": " fellow",
              "point_cs": 124
            },
            {
              "text": " Americans",
              "point_cs": 180
            },
            {
              "text": ",",
              "point_cs": 216
            },
            {
              "text": " ask",
              "point_cs": 262
            },
            {
              "text": " not",
              "point_cs": 314
            },
            {
              "text": " what",
              "point_cs": 358
            },
            {
              "text": " your",
              "point_cs": 382
            },
            {
              "text": " country",
              "point_cs": 426
            },
            {
              "text": " can",
              "point_cs": 464
            },
            {
              "text": " do",
              "point_cs": 484
            },
            {
              "text": " for",
              "point_cs": 508
            },
            {
              "text": " you",
              "point_cs": 542
            },
            {
              "text": ",",
              "point_cs": 582
            },
            {
              "text": " ask",
              "point_cs": 620
            },
            {
              "text": " what",
              "point_cs": 646
            },
            {
              "text": " you",
              "point_cs": 674
            },
            {
              "text": " can",
              "point_cs": 706
            },
            {
              "text": " do",
              "point_cs": 726
            },
            {
              "text": " for",
              "point_cs": 748
            },
            {
              "text": " your",
              "point_cs": 768
            },
            {
              "text": " country",
              "point_cs": 806
            },
            {
              "text": ".",
              "point_cs": 830
            },
            {
              "text": " And",
              "point_cs": 866
            },
            {
              "text": " so",
              "point_cs": 900
            },
            {
              "text": ",",
              "point_cs": 920
            },
            {
              "text": " my",
              "point_cs": 934
            },
            {
              "text": " fellow",
              "point_cs": 968
            },
            {
              "text": " Americans",
              "point_cs": 1022
            },
            {
              "text": ",",
              "point_cs": 1058
            },
            {
              "text": " ask",
              "point_cs": 1102
            },
            {
              "text": " not",
              "point_cs": 1150
            },
            {
              "text": " what",
              "point_cs": 1200
            },
            {
              "text": " your",
              "point_cs": 1224
            },
            {
              "text": " country",
              "point_cs": 1268
            },
            {
              "text": " can",
              "point_cs": 1306
            },
            {
              "text": " do",
              "point_cs": 1328
            },
            {
              "text": " for",
              "point_cs": 1350
            },
            {
              "text": " you",
              "point_cs": 1384
            },
            {
              "text": ",",
              "point_cs": 1426
            },
            {
              "text": " ask",
              "point_cs": 1466
            },
            {
              "text": " what",
              "point_cs": 1488
            },
            {
              "text": " you",
              "point_cs": 1518
            },
            {
              "text": " can",
              "point_cs": 1548
            },
            {
              "text": " do",
              "point_cs": 1570
            },
            {
              "text": " for",
              "point_cs": 1592
            },
            {
              "text": " your",
              "point_cs": 1610
            },
            {
              "text": " country",
              "point_cs": 1648
            },
            {
              "text": ".",
              "point_cs": 1648
            }
          ],
          "command": [
            "/tmp/atrain-whisper-a/.whisper-cli-unpatched",
            "-m",
            "/home/juergen/github/aTrain/.cache/whisper-cpp-evaluation/ggml-large-v3-turbo.bin",
            "-f",
            "/tmp/atrain-whisper-a-turbo-cpu-results/audio/internal.wav",
            "-l",
            "en",
            "-t",
            "4",
            "-bs",
            "5",
            "-tp",
            "0",
            "-nf",
            "-ng",
            "-nfa",
            "-ojf",
            "-of",
            "/tmp/atrain-whisper-a-turbo-cpu-results/upstream-dtw-vad-internal",
            "--vad",
            "-vm",
            "/tmp/atrain-whisper-a/.ggml-silero-v5.1.2.bin",
            "--dtw",
            "large.v3.turbo"
          ],
          "wall_s": 20.36492648400599,
          "execution_status": "completed",
          "status": "passed"
        },
        "boundary": {
          "text": " And so, my fellow Americans, ask not what your country can do for you, ask what you can do for your country.",
          "words": [
            {
              "text": " And",
              "start_ms": 20,
              "end_ms": 230,
              "pieces": [
                " And"
              ]
            },
            {
              "text": " so,",
              "start_ms": 370,
              "end_ms": 570,
              "pieces": [
                " so",
                ","
              ]
            },
            {
              "text": " my",
              "start_ms": 570,
              "end_ms": 730,
              "pieces": [
                " my"
              ]
            },
            {
              "text": " fellow",
              "start_ms": 730,
              "end_ms": 1220,
              "pieces": [
                " fellow"
              ]
            },
            {
              "text": " Americans,",
              "start_ms": 1220,
              "end_ms": 2290,
              "pieces": [
                " Americans",
                ","
              ]
            },
            {
              "text": " ask",
              "start_ms": 2290,
              "end_ms": 2450,
              "pieces": [
                " ask"
              ]
            },
            {
              "text": " not",
              "start_ms": 2860,
              "end_ms": 3120,
              "pieces": [
                " not"
              ]
            },
            {
              "text": " what",
              "start_ms": 3390,
              "end_ms": 3500,
              "pieces": [
                " what"
              ]
            },
            {
              "text": " your",
              "start_ms": 3500,
              "end_ms": 3810,
              "pieces": [
                " your"
              ]
            },
            {
              "text": " country",
              "start_ms": 3950,
              "end_ms": 4370,
              "pieces": [
                " country"
              ]
            },
            {
              "text": " can",
              "start_ms": 4370,
              "end_ms": 4610,
              "pieces": [
                " can"
              ]
            },
            {
              "text": " do",
              "start_ms": 4620,
              "end_ms": 4780,
              "pieces": [
                " do"
              ]
            },
            {
              "text": " for",
              "start_ms": 4780,
              "end_ms": 5020,
              "pieces": [
                " for"
              ]
            },
            {
              "text": " you,",
              "start_ms": 5020,
              "end_ms": 5440,
              "pieces": [
                " you",
                ","
              ]
            },
            {
              "text": " ask",
              "start_ms": 5440,
              "end_ms": 5570,
              "pieces": [
                " ask"
              ]
            },
            {
              "text": " what",
              "start_ms": 5890,
              "end_ms": 6380,
              "pieces": [
                " what"
              ]
            },
            {
              "text": " you",
              "start_ms": 6380,
              "end_ms": 6800,
              "pieces": [
                " you"
              ]
            },
            {
              "text": " can",
              "start_ms": 6800,
              "end_ms": 7080,
              "pieces": [
                " can"
              ]
            },
            {
              "text": " do",
              "start_ms": 7080,
              "end_ms": 7280,
              "pieces": [
                " do"
              ]
            },
            {
              "text": " for",
              "start_ms": 7280,
              "end_ms": 7370,
              "pieces": [
                " for"
              ]
            },
            {
              "text": " your",
              "start_ms": 7430,
              "end_ms": 7600,
              "pieces": [
                " your"
              ]
            },
            {
              "text": " country.",
              "start_ms": 7600,
              "end_ms": 8070,
              "pieces": [
                " country",
                "."
              ]
            }
          ],
          "problems": [],
          "dtw_points": [
            {
              "text": " And",
              "point_cs": 22
            },
            {
              "text": " so",
              "point_cs": 54
            },
            {
              "text": ",",
              "point_cs": 78
            },
            {
              "text": " my",
              "point_cs": 90
            },
            {
              "text": " fellow",
              "point_cs": 122
            },
            {
              "text": " Americans",
              "point_cs": 180
            },
            {
              "text": ",",
              "point_cs": 218
            },
            {
              "text": " ask",
              "point_cs": 258
            },
            {
              "text": " not",
              "point_cs": 312
            },
            {
              "text": " what",
              "point_cs": 354
            },
            {
              "text": " your",
              "point_cs": 378
            },
            {
              "text": " country",
              "point_cs": 422
            },
            {
              "text": " can",
              "point_cs": 460
            },
            {
              "text": " do",
              "point_cs": 480
            },
            {
              "text": " for",
              "point_cs": 504
            },
            {
              "text": " you",
              "point_cs": 538
            },
            {
              "text": ",",
              "point_cs": 570
            },
            {
              "text": " ask",
              "point_cs": 622
            },
            {
              "text": " what",
              "point_cs": 646
            },
            {
              "text": " you",
              "point_cs": 672
            },
            {
              "text": " can",
              "point_cs": 704
            },
            {
              "text": " do",
              "point_cs": 726
            },
            {
              "text": " for",
              "point_cs": 748
            },
            {
              "text": " your",
              "point_cs": 766
            },
            {
              "text": " country",
              "point_cs": 806
            },
            {
              "text": ".",
              "point_cs": 806
            }
          ],
          "command": [
            "/tmp/atrain-whisper-a/.whisper-cli-unpatched",
            "-m",
            "/home/juergen/github/aTrain/.cache/whisper-cpp-evaluation/ggml-large-v3-turbo.bin",
            "-f",
            "/tmp/atrain-whisper-a-turbo-cpu-results/audio/boundary.wav",
            "-l",
            "en",
            "-t",
            "4",
            "-bs",
            "5",
            "-tp",
            "0",
            "-nf",
            "-ng",
            "-nfa",
            "-ojf",
            "-of",
            "/tmp/atrain-whisper-a-turbo-cpu-results/upstream-dtw-vad-boundary",
            "--vad",
            "-vm",
            "/tmp/atrain-whisper-a/.ggml-silero-v5.1.2.bin",
            "--dtw",
            "large.v3.turbo"
          ],
          "wall_s": 21.317135766003048,
          "execution_status": "completed",
          "status": "passed"
        },
        "silence": {
          "text": "",
          "words": [],
          "problems": [],
          "dtw_points": [],
          "command": [
            "/tmp/atrain-whisper-a/.whisper-cli-unpatched",
            "-m",
            "/home/juergen/github/aTrain/.cache/whisper-cpp-evaluation/ggml-large-v3-turbo.bin",
            "-f",
            "/tmp/atrain-whisper-a-turbo-cpu-results/audio/silence.wav",
            "-l",
            "en",
            "-t",
            "4",
            "-bs",
            "5",
            "-tp",
            "0",
            "-nf",
            "-ng",
            "-nfa",
            "-ojf",
            "-of",
            "/tmp/atrain-whisper-a-turbo-cpu-results/upstream-dtw-vad-silence",
            "--vad",
            "-vm",
            "/tmp/atrain-whisper-a/.ggml-silero-v5.1.2.bin",
            "--dtw",
            "large.v3.turbo"
          ],
          "wall_s": 1.5678192810009932,
          "execution_status": "completed",
          "status": "passed"
        },
        "noise": {
          "text": "",
          "words": [],
          "problems": [],
          "dtw_points": [],
          "command": [
            "/tmp/atrain-whisper-a/.whisper-cli-unpatched",
            "-m",
            "/home/juergen/github/aTrain/.cache/whisper-cpp-evaluation/ggml-large-v3-turbo.bin",
            "-f",
            "/tmp/atrain-whisper-a-turbo-cpu-results/audio/noise.wav",
            "-l",
            "en",
            "-t",
            "4",
            "-bs",
            "5",
            "-tp",
            "0",
            "-nf",
            "-ng",
            "-nfa",
            "-ojf",
            "-of",
            "/tmp/atrain-whisper-a-turbo-cpu-results/upstream-dtw-vad-noise",
            "--vad",
            "-vm",
            "/tmp/atrain-whisper-a/.ggml-silero-v5.1.2.bin",
            "--dtw",
            "large.v3.turbo"
          ],
          "wall_s": 1.5178096360032214,
          "execution_status": "completed",
          "status": "passed"
        },
        "german": {
          "text": " Hiro, Kapitel 8. Flach halten. Flach halten. Junge, du wirst es nicht packen. Das ist doch... Vergiss es. Vergiss es einfach. Doch, das hast du gut gemacht. Nein, so nicht. Netz, Netz. Hat berührt. Hat berührt. Vergiss alles, was man dir gesagt hat. Den wirst du nicht packen. Der ist gut.",
          "words": [
            {
              "text": " Hiro,",
              "start_ms": 40,
              "end_ms": 460,
              "pieces": [
                " Hi",
                "ro",
                ","
              ]
            },
            {
              "text": " Kapitel",
              "start_ms": 730,
              "end_ms": 1140,
              "pieces": [
                " Kap",
                "itel"
              ]
            },
            {
              "text": " 8.",
              "start_ms": 1140,
              "end_ms": 1650,
              "pieces": [
                " 8",
                "."
              ]
            },
            {
              "text": " Flach",
              "start_ms": 1650,
              "end_ms": 2000,
              "pieces": [
                " Fl",
                "ach"
              ]
            },
            {
              "text": " halten.",
              "start_ms": 2000,
              "end_ms": 2640,
              "pieces": [
                " halten",
                "."
              ]
            },
            {
              "text": " Flach",
              "start_ms": 2640,
              "end_ms": 3170,
              "pieces": [
                " Fl",
                "ach"
              ]
            },
            {
              "text": " halten.",
              "start_ms": 3170,
              "end_ms": 4130,
              "pieces": [
                " halten",
                "."
              ]
            },
            {
              "text": " Junge,",
              "start_ms": 4920,
              "end_ms": 4920,
              "pieces": [
                " Jun",
                "ge",
                ","
              ]
            },
            {
              "text": " du",
              "start_ms": 4920,
              "end_ms": 4920,
              "pieces": [
                " du"
              ]
            },
            {
              "text": " wirst",
              "start_ms": 4920,
              "end_ms": 5060,
              "pieces": [
                " w",
                "irst"
              ]
            },
            {
              "text": " es",
              "start_ms": 5060,
              "end_ms": 5100,
              "pieces": [
                " es"
              ]
            },
            {
              "text": " nicht",
              "start_ms": 5180,
              "end_ms": 5340,
              "pieces": [
                " nicht"
              ]
            },
            {
              "text": " packen.",
              "start_ms": 5650,
              "end_ms": 6180,
              "pieces": [
                " pack",
                "en",
                "."
              ]
            },
            {
              "text": " Das",
              "start_ms": 6180,
              "end_ms": 6390,
              "pieces": [
                " Das"
              ]
            },
            {
              "text": " ist",
              "start_ms": 6510,
              "end_ms": 6640,
              "pieces": [
                " ist"
              ]
            },
            {
              "text": " doch...",
              "start_ms": 6640,
              "end_ms": 7670,
              "pieces": [
                " doch",
                "..."
              ]
            },
            {
              "text": " Vergiss",
              "start_ms": 7670,
              "end_ms": 8100,
              "pieces": [
                " Verg",
                "iss"
              ]
            },
            {
              "text": " es.",
              "start_ms": 8100,
              "end_ms": 8380,
              "pieces": [
                " es",
                "."
              ]
            },
            {
              "text": " Vergiss",
              "start_ms": 8390,
              "end_ms": 8810,
              "pieces": [
                " Verg",
                "iss"
              ]
            },
            {
              "text": " es",
              "start_ms": 8930,
              "end_ms": 8940,
              "pieces": [
                " es"
              ]
            },
            {
              "text": " einfach.",
              "start_ms": 8940,
              "end_ms": 9600,
              "pieces": [
                " einfach",
                "."
              ]
            },
            {
              "text": " Doch,",
              "start_ms": 10160,
              "end_ms": 10160,
              "pieces": [
                " Doch",
                ","
              ]
            },
            {
              "text": " das",
              "start_ms": 10200,
              "end_ms": 10290,
              "pieces": [
                " das"
              ]
            },
            {
              "text": " hast",
              "start_ms": 10290,
              "end_ms": 10560,
              "pieces": [
                " hast"
              ]
            },
            {
              "text": " du",
              "start_ms": 10600,
              "end_ms": 10620,
              "pieces": [
                " du"
              ]
            },
            {
              "text": " gut",
              "start_ms": 10890,
              "end_ms": 10980,
              "pieces": [
                " gut"
              ]
            },
            {
              "text": " gemacht.",
              "start_ms": 10980,
              "end_ms": 11800,
              "pieces": [
                " gemacht",
                "."
              ]
            },
            {
              "text": " Nein,",
              "start_ms": 11800,
              "end_ms": 12450,
              "pieces": [
                " Nein",
                ","
              ]
            },
            {
              "text": " so",
              "start_ms": 12450,
              "end_ms": 12670,
              "pieces": [
                " so"
              ]
            },
            {
              "text": " nicht.",
              "start_ms": 12670,
              "end_ms": 13560,
              "pieces": [
                " nicht",
                "."
              ]
            },
            {
              "text": " Netz,",
              "start_ms": 13560,
              "end_ms": 14230,
              "pieces": [
                " Netz",
                ","
              ]
            },
            {
              "text": " Netz.",
              "start_ms": 14230,
              "end_ms": 15020,
              "pieces": [
                " Netz",
                "."
              ]
            },
            {
              "text": " Hat",
              "start_ms": 15150,
              "end_ms": 15270,
              "pieces": [
                " Hat"
              ]
            },
            {
              "text": " berührt.",
              "start_ms": 15270,
              "end_ms": 15990,
              "pieces": [
                " ber",
                "ührt",
                "."
              ]
            },
            {
              "text": " Hat",
              "start_ms": 16060,
              "end_ms": 16330,
              "pieces": [
                " Hat"
              ]
            },
            {
              "text": " berührt.",
              "start_ms": 16660,
              "end_ms": 17550,
              "pieces": [
                " ber",
                "ührt",
                "."
              ]
            },
            {
              "text": " Vergiss",
              "start_ms": 18420,
              "end_ms": 18420,
              "pieces": [
                " Verg",
                "iss"
              ]
            },
            {
              "text": " alles,",
              "start_ms": 18460,
              "end_ms": 18720,
              "pieces": [
                " alles",
                ","
              ]
            },
            {
              "text": " was",
              "start_ms": 18720,
              "end_ms": 18860,
              "pieces": [
                " was"
              ]
            },
            {
              "text": " man",
              "start_ms": 19150,
              "end_ms": 19200,
              "pieces": [
                " man"
              ]
            },
            {
              "text": " dir",
              "start_ms": 19200,
              "end_ms": 19440,
              "pieces": [
                " dir"
              ]
            },
            {
              "text": " gesagt",
              "start_ms": 19440,
              "end_ms": 19740,
              "pieces": [
                " gesagt"
              ]
            },
            {
              "text": " hat.",
              "start_ms": 20010,
              "end_ms": 20400,
              "pieces": [
                " hat",
                "."
              ]
            },
            {
              "text": " Den",
              "start_ms": 20400,
              "end_ms": 20640,
              "pieces": [
                " Den"
              ]
            },
            {
              "text": " wirst",
              "start_ms": 20640,
              "end_ms": 21040,
              "pieces": [
                " w",
                "irst"
              ]
            },
            {
              "text": " du",
              "start_ms": 21040,
              "end_ms": 21160,
              "pieces": [
                " du"
              ]
            },
            {
              "text": " nicht",
              "start_ms": 21530,
              "end_ms": 21600,
              "pieces": [
                " nicht"
              ]
            },
            {
              "text": " packen.",
              "start_ms": 21600,
              "end_ms": 22310,
              "pieces": [
                " pack",
                "en",
                "."
              ]
            },
            {
              "text": " Der",
              "start_ms": 22430,
              "end_ms": 22550,
              "pieces": [
                " Der"
              ]
            },
            {
              "text": " ist",
              "start_ms": 22550,
              "end_ms": 22660,
              "pieces": [
                " ist"
              ]
            },
            {
              "text": " gut.",
              "start_ms": 22770,
              "end_ms": 23120,
              "pieces": [
                " gut",
                "."
              ]
            }
          ],
          "problems": [
            "nonpositive word interval: ' Junge,'",
            "nonpositive word interval: ' du'",
            "nonpositive word interval: ' Doch,'",
            "nonpositive word interval: ' Vergiss'"
          ],
          "dtw_points": [
            {
              "text": " Hi",
              "point_cs": 18
            },
            {
              "text": "ro",
              "point_cs": 36
            },
            {
              "text": ",",
              "point_cs": 72
            },
            {
              "text": " Kap",
              "point_cs": 90
            },
            {
              "text": "itel",
              "point_cs": 108
            },
            {
              "text": " 8",
              "point_cs": 132
            },
            {
              "text": ".",
              "point_cs": 162
            },
            {
              "text": " Fl",
              "point_cs": 174
            },
            {
              "text": "ach",
              "point_cs": 200
            },
            {
              "text": " halten",
              "point_cs": 260
            },
            {
              "text": ".",
              "point_cs": 292
            },
            {
              "text": " Fl",
              "point_cs": 318
            },
            {
              "text": "ach",
              "point_cs": 350
            },
            {
              "text": " halten",
              "point_cs": 412
            },
            {
              "text": ".",
              "point_cs": 488
            },
            {
              "text": " Jun",
              "point_cs": 508
            },
            {
              "text": "ge",
              "point_cs": 522
            },
            {
              "text": ",",
              "point_cs": 534
            },
            {
              "text": " du",
              "point_cs": 534
            },
            {
              "text": " w",
              "point_cs": 550
            },
            {
              "text": "irst",
              "point_cs": 556
            },
            {
              "text": " es",
              "point_cs": 568
            },
            {
              "text": " nicht",
              "point_cs": 582
            },
            {
              "text": " pack",
              "point_cs": 606
            },
            {
              "text": "en",
              "point_cs": 618
            },
            {
              "text": ".",
              "point_cs": 650
            },
            {
              "text": " Das",
              "point_cs": 662
            },
            {
              "text": " ist",
              "point_cs": 676
            },
            {
              "text": " doch",
              "point_cs": 706
            },
            {
              "text": "...",
              "point_cs": 742
            },
            {
              "text": " Verg",
              "point_cs": 796
            },
            {
              "text": "iss",
              "point_cs": 824
            },
            {
              "text": " es",
              "point_cs": 848
            },
            {
              "text": ".",
              "point_cs": 860
            },
            {
              "text": " Verg",
              "point_cs": 886
            },
            {
              "text": "iss",
              "point_cs": 908
            },
            {
              "text": " es",
              "point_cs": 922
            },
            {
              "text": " einfach",
              "point_cs": 960
            },
            {
              "text": ".",
              "point_cs": 998
            },
            {
              "text": " Doch",
              "point_cs": 1046
            },
            {
              "text": ",",
              "point_cs": 1082
            },
            {
              "text": " das",
              "point_cs": 1098
            },
            {
              "text": " hast",
              "point_cs": 1112
            },
            {
              "text": " du",
              "point_cs": 1122
            },
            {
              "text": " gut",
              "point_cs": 1138
            },
            {
              "text": " gemacht",
              "point_cs": 1172
            },
            {
              "text": ".",
              "point_cs": 1200
            },
            {
              "text": " Nein",
              "point_cs": 1242
            },
            {
              "text": ",",
              "point_cs": 1272
            },
            {
              "text": " so",
              "point_cs": 1290
            },
            {
              "text": " nicht",
              "point_cs": 1352
            },
            {
              "text": ".",
              "point_cs": 1372
            },
            {
              "text": " Netz",
              "point_cs": 1416
            },
            {
              "text": ",",
              "point_cs": 1452
            },
            {
              "text": " Netz",
              "point_cs": 1494
            },
            {
              "text": ".",
              "point_cs": 1532
            },
            {
              "text": " Hat",
              "point_cs": 1552
            },
            {
              "text": " ber",
              "point_cs": 1576
            },
            {
              "text": "ührt",
              "point_cs": 1606
            },
            {
              "text": ".",
              "point_cs": 1632
            },
            {
              "text": " Hat",
              "point_cs": 1664
            },
            {
              "text": " ber",
              "point_cs": 1714
            },
            {
              "text": "ührt",
              "point_cs": 1748
            },
            {
              "text": ".",
              "point_cs": 1796
            },
            {
              "text": " Verg",
              "point_cs": 1868
            },
            {
              "text": "iss",
              "point_cs": 1894
            },
            {
              "text": " alles",
              "point_cs": 1930
            },
            {
              "text": ",",
              "point_cs": 1948
            },
            {
              "text": " was",
              "point_cs": 1958
            },
            {
              "text": " man",
              "point_cs": 1972
            },
            {
              "text": " dir",
              "point_cs": 1986
            },
            {
              "text": " gesagt",
              "point_cs": 2018
            },
            {
              "text": " hat",
              "point_cs": 2044
            },
            {
              "text": ".",
              "point_cs": 2096
            },
            {
              "text": " Den",
              "point_cs": 2124
            },
            {
              "text": " w",
              "point_cs": 2150
            },
            {
              "text": "irst",
              "point_cs": 2158
            },
            {
              "text": " du",
              "point_cs": 2176
            },
            {
              "text": " nicht",
              "point_cs": 2196
            },
            {
              "text": " pack",
              "point_cs": 2220
            },
            {
              "text": "en",
              "point_cs": 2234
            },
            {
              "text": ".",
              "point_cs": 2258
            },
            {
              "text": " Der",
              "point_cs": 2276
            },
            {
              "text": " ist",
              "point_cs": 2288
            },
            {
              "text": " gut",
              "point_cs": 2310
            },
            {
              "text": ".",
              "point_cs": 2310
            }
          ],
          "command": [
            "/tmp/atrain-whisper-a/.whisper-cli-unpatched",
            "-m",
            "/home/juergen/github/aTrain/.cache/whisper-cpp-evaluation/ggml-large-v3-turbo.bin",
            "-f",
            "/tmp/atrain-whisper-a-turbo-cpu-results/audio/german.wav",
            "-l",
            "de",
            "-t",
            "4",
            "-bs",
            "5",
            "-tp",
            "0",
            "-nf",
            "-ng",
            "-nfa",
            "-ojf",
            "-of",
            "/tmp/atrain-whisper-a-turbo-cpu-results/upstream-dtw-vad-german",
            "--vad",
            "-vm",
            "/tmp/atrain-whisper-a/.ggml-silero-v5.1.2.bin",
            "--dtw",
            "large.v3.turbo"
          ],
          "wall_s": 21.611626071011415,
          "execution_status": "completed",
          "status": "failed"
        },
        "japanese": {
          "text": "こんにちは",
          "words": [
            {
              "text": "こんにちは",
              "start_ms": 40,
              "end_ms": 720,
              "pieces": [
                "こんにちは"
              ]
            }
          ],
          "problems": [],
          "dtw_points": [
            {
              "text": "こんにちは",
              "point_cs": 64
            }
          ],
          "command": [
            "/tmp/atrain-whisper-a/.whisper-cli-unpatched",
            "-m",
            "/home/juergen/github/aTrain/.cache/whisper-cpp-evaluation/ggml-large-v3-turbo.bin",
            "-f",
            "/tmp/atrain-whisper-a-turbo-cpu-results/audio/japanese.wav",
            "-l",
            "ja",
            "-t",
            "4",
            "-bs",
            "5",
            "-tp",
            "0",
            "-nf",
            "-ng",
            "-nfa",
            "-ojf",
            "-of",
            "/tmp/atrain-whisper-a-turbo-cpu-results/upstream-dtw-vad-japanese",
            "--vad",
            "-vm",
            "/tmp/atrain-whisper-a/.ggml-silero-v5.1.2.bin",
            "--dtw",
            "large.v3.turbo"
          ],
          "wall_s": 19.458405030003632,
          "execution_status": "completed",
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
            5020,
            5040,
            5190,
            5110,
            5110,
            5090,
            5140,
            5290,
            5160,
            5500,
            5500,
            5690,
            5690,
            5640,
            5970,
            6000,
            5620,
            5700,
            5360,
            5320,
            5320,
            5230,
            5240,
            5180,
            5180,
            5090,
            4970,
            4950,
            4950,
            4920,
            4920,
            4930,
            4930,
            4920,
            4920,
            4920,
            4920,
            4920,
            4920,
            4980,
            4920,
            4930,
            4930,
            4930
          ],
          "max_boundary_error_ms": 6000,
          "median_boundary_error_ms": 5100.0,
          "status": "failed"
        },
        "trailing": {
          "tolerance_ms": 50,
          "matched_words": 22,
          "unmatched_reference_words": 0,
          "unmatched_candidate_words": 0,
          "boundary_errors_ms": [
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0
          ],
          "max_boundary_error_ms": 0,
          "median_boundary_error_ms": 0.0,
          "status": "passed"
        },
        "boundary": {
          "tolerance_ms": 50,
          "matched_words": 22,
          "unmatched_reference_words": 0,
          "unmatched_candidate_words": 0,
          "boundary_errors_ms": [
            25020,
            25010,
            25020,
            25000,
            25000,
            24950,
            25000,
            25000,
            25000,
            25000,
            25000,
            25050,
            24980,
            24980,
            25040,
            25010,
            25010,
            25030,
            24890,
            25030,
            25030,
            25030,
            25030,
            25030,
            25030,
            25030,
            25030,
            25050,
            25050,
            25010,
            25010,
            25020,
            25020,
            25000,
            25000,
            25000,
            25000,
            25020,
            25020,
            25070,
            25010,
            25020,
            25020,
            25020
          ],
          "max_boundary_error_ms": 25070,
          "median_boundary_error_ms": 25020.0,
          "status": "failed"
        },
        "internal-first": {
          "tolerance_ms": 50,
          "matched_words": 22,
          "unmatched_reference_words": 0,
          "unmatched_candidate_words": 22,
          "boundary_errors_ms": [
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            100,
            100,
            20,
            360,
            600,
            580,
            410,
            80,
            310,
            310,
            290,
            170,
            200,
            140,
            140,
            120,
            110,
            20,
            10,
            10,
            0,
            0,
            20,
            20,
            20,
            20,
            0,
            0,
            0,
            0,
            60,
            60,
            40,
            40,
            10
          ],
          "max_boundary_error_ms": 600,
          "median_boundary_error_ms": 20.0,
          "status": "failed"
        },
        "internal-second": {
          "tolerance_ms": 50,
          "matched_words": 0,
          "unmatched_reference_words": 22,
          "unmatched_candidate_words": 0,
          "boundary_errors_ms": [],
          "max_boundary_error_ms": null,
          "median_boundary_error_ms": null,
          "status": "failed"
        }
      }
    },
    "patched-dtw-vad": {
      "fixtures": {
        "base": {
          "text": " And so, my fellow Americans, ask not what your country can do for you, ask what you can do for your country.",
          "words": [
            {
              "text": " And",
              "start_ms": 330,
              "end_ms": 530,
              "pieces": [
                " And"
              ]
            },
            {
              "text": " so,",
              "start_ms": 680,
              "end_ms": 860,
              "pieces": [
                " so",
                ","
              ]
            },
            {
              "text": " my",
              "start_ms": 860,
              "end_ms": 970,
              "pieces": [
                " my"
              ]
            },
            {
              "text": " fellow",
              "start_ms": 1020,
              "end_ms": 1510,
              "pieces": [
                " fellow"
              ]
            },
            {
              "text": " Americans,",
              "start_ms": 1510,
              "end_ms": 3440,
              "pieces": [
                " Americans",
                ","
              ]
            },
            {
              "text": " ask",
              "start_ms": 3440,
              "end_ms": 3650,
              "pieces": [
                " ask"
              ]
            },
            {
              "text": " not",
              "start_ms": 4020,
              "end_ms": 4280,
              "pieces": [
                " not"
              ]
            },
            {
              "text": " what",
              "start_ms": 5410,
              "end_ms": 5490,
              "pieces": [
                " what"
              ]
            },
            {
              "text": " your",
              "start_ms": 5490,
              "end_ms": 5820,
              "pieces": [
                " your"
              ]
            },
            {
              "text": " country",
              "start_ms": 5820,
              "end_ms": 6380,
              "pieces": [
                " country"
              ]
            },
            {
              "text": " can",
              "start_ms": 6380,
              "end_ms": 6620,
              "pieces": [
                " can"
              ]
            },
            {
              "text": " do",
              "start_ms": 6630,
              "end_ms": 6790,
              "pieces": [
                " do"
              ]
            },
            {
              "text": " for",
              "start_ms": 6790,
              "end_ms": 7030,
              "pieces": [
                " for"
              ]
            },
            {
              "text": " you,",
              "start_ms": 7030,
              "end_ms": 7470,
              "pieces": [
                " you",
                ","
              ]
            },
            {
              "text": " ask",
              "start_ms": 7470,
              "end_ms": 7560,
              "pieces": [
                " ask"
              ]
            },
            {
              "text": " what",
              "start_ms": 8190,
              "end_ms": 8690,
              "pieces": [
                " what"
              ]
            },
            {
              "text": " you",
              "start_ms": 8690,
              "end_ms": 9090,
              "pieces": [
                " you"
              ]
            },
            {
              "text": " can",
              "start_ms": 9090,
              "end_ms": 9370,
              "pieces": [
                " can"
              ]
            },
            {
              "text": " do",
              "start_ms": 9370,
              "end_ms": 9590,
              "pieces": [
                " do"
              ]
            },
            {
              "text": " for",
              "start_ms": 9590,
              "end_ms": 9730,
              "pieces": [
                " for"
              ]
            },
            {
              "text": " your",
              "start_ms": 9730,
              "end_ms": 9910,
              "pieces": [
                " your"
              ]
            },
            {
              "text": " country.",
              "start_ms": 9910,
              "end_ms": 10380,
              "pieces": [
                " country",
                "."
              ]
            }
          ],
          "problems": [],
          "dtw_points": [
            {
              "text": " And",
              "point_cs": 22
            },
            {
              "text": " so",
              "point_cs": 56
            },
            {
              "text": ",",
              "point_cs": 80
            },
            {
              "text": " my",
              "point_cs": 92
            },
            {
              "text": " fellow",
              "point_cs": 126
            },
            {
              "text": " Americans",
              "point_cs": 182
            },
            {
              "text": ",",
              "point_cs": 220
            },
            {
              "text": " ask",
              "point_cs": 262
            },
            {
              "text": " not",
              "point_cs": 310
            },
            {
              "text": " what",
              "point_cs": 358
            },
            {
              "text": " your",
              "point_cs": 382
            },
            {
              "text": " country",
              "point_cs": 426
            },
            {
              "text": " can",
              "point_cs": 464
            },
            {
              "text": " do",
              "point_cs": 484
            },
            {
              "text": " for",
              "point_cs": 508
            },
            {
              "text": " you",
              "point_cs": 542
            },
            {
              "text": ",",
              "point_cs": 578
            },
            {
              "text": " ask",
              "point_cs": 622
            },
            {
              "text": " what",
              "point_cs": 648
            },
            {
              "text": " you",
              "point_cs": 674
            },
            {
              "text": " can",
              "point_cs": 706
            },
            {
              "text": " do",
              "point_cs": 726
            },
            {
              "text": " for",
              "point_cs": 748
            },
            {
              "text": " your",
              "point_cs": 766
            },
            {
              "text": " country",
              "point_cs": 808
            },
            {
              "text": ".",
              "point_cs": 808
            }
          ],
          "command": [
            "/tmp/atrain-whisper-a/.whisper-cli-patched",
            "-m",
            "/home/juergen/github/aTrain/.cache/whisper-cpp-evaluation/ggml-large-v3-turbo.bin",
            "-f",
            "/tmp/atrain-whisper-a-turbo-cpu-results/audio/base.wav",
            "-l",
            "en",
            "-t",
            "4",
            "-bs",
            "5",
            "-tp",
            "0",
            "-nf",
            "-ng",
            "-nfa",
            "-ojf",
            "-of",
            "/tmp/atrain-whisper-a-turbo-cpu-results/patched-dtw-vad-base",
            "--vad",
            "-vm",
            "/tmp/atrain-whisper-a/.ggml-silero-v5.1.2.bin",
            "--dtw",
            "large.v3.turbo"
          ],
          "wall_s": 20.059603462010273,
          "execution_status": "completed",
          "status": "passed"
        },
        "leading": {
          "text": " And so, my fellow Americans, ask not what your country can do for you, ask what you can do for your country.",
          "words": [
            {
              "text": " And",
              "start_ms": 5330,
              "end_ms": 5510,
              "pieces": [
                " And"
              ]
            },
            {
              "text": " so,",
              "start_ms": 5510,
              "end_ms": 5770,
              "pieces": [
                " so",
                ","
              ]
            },
            {
              "text": " my",
              "start_ms": 5770,
              "end_ms": 5900,
              "pieces": [
                " my"
              ]
            },
            {
              "text": " fellow",
              "start_ms": 5900,
              "end_ms": 6240,
              "pieces": [
                " fellow"
              ]
            },
            {
              "text": " Americans,",
              "start_ms": 6370,
              "end_ms": 7100,
              "pieces": [
                " Americans",
                ","
              ]
            },
            {
              "text": " ask",
              "start_ms": 7100,
              "end_ms": 7120,
              "pieces": [
                " ask"
              ]
            },
            {
              "text": " not",
              "start_ms": 8290,
              "end_ms": 8600,
              "pieces": [
                " not"
              ]
            },
            {
              "text": " what",
              "start_ms": 8600,
              "end_ms": 8650,
              "pieces": [
                " what"
              ]
            },
            {
              "text": " your",
              "start_ms": 9030,
              "end_ms": 9280,
              "pieces": [
                " your"
              ]
            },
            {
              "text": " country",
              "start_ms": 10410,
              "end_ms": 11010,
              "pieces": [
                " country"
              ]
            },
            {
              "text": " can",
              "start_ms": 11010,
              "end_ms": 11340,
              "pieces": [
                " can"
              ]
            },
            {
              "text": " do",
              "start_ms": 11340,
              "end_ms": 11560,
              "pieces": [
                " do"
              ]
            },
            {
              "text": " for",
              "start_ms": 11560,
              "end_ms": 11890,
              "pieces": [
                " for"
              ]
            },
            {
              "text": " you,",
              "start_ms": 12010,
              "end_ms": 12470,
              "pieces": [
                " you",
                ","
              ]
            },
            {
              "text": " ask",
              "start_ms": 12470,
              "end_ms": 12590,
              "pieces": [
                " ask"
              ]
            },
            {
              "text": " what",
              "start_ms": 13190,
              "end_ms": 13680,
              "pieces": [
                " what"
              ]
            },
            {
              "text": " you",
              "start_ms": 13680,
              "end_ms": 14090,
              "pieces": [
                " you"
              ]
            },
            {
              "text": " can",
              "start_ms": 14090,
              "end_ms": 14370,
              "pieces": [
                " can"
              ]
            },
            {
              "text": " do",
              "start_ms": 14370,
              "end_ms": 14590,
              "pieces": [
                " do"
              ]
            },
            {
              "text": " for",
              "start_ms": 14590,
              "end_ms": 14670,
              "pieces": [
                " for"
              ]
            },
            {
              "text": " your",
              "start_ms": 14730,
              "end_ms": 14900,
              "pieces": [
                " your"
              ]
            },
            {
              "text": " country.",
              "start_ms": 14900,
              "end_ms": 15370,
              "pieces": [
                " country",
                "."
              ]
            }
          ],
          "problems": [],
          "dtw_points": [
            {
              "text": " And",
              "point_cs": 22
            },
            {
              "text": " so",
              "point_cs": 56
            },
            {
              "text": ",",
              "point_cs": 78
            },
            {
              "text": " my",
              "point_cs": 90
            },
            {
              "text": " fellow",
              "point_cs": 124
            },
            {
              "text": " Americans",
              "point_cs": 180
            },
            {
              "text": ",",
              "point_cs": 220
            },
            {
              "text": " ask",
              "point_cs": 264
            },
            {
              "text": " not",
              "point_cs": 316
            },
            {
              "text": " what",
              "point_cs": 362
            },
            {
              "text": " your",
              "point_cs": 388
            },
            {
              "text": " country",
              "point_cs": 432
            },
            {
              "text": " can",
              "point_cs": 468
            },
            {
              "text": " do",
              "point_cs": 490
            },
            {
              "text": " for",
              "point_cs": 514
            },
            {
              "text": " you",
              "point_cs": 548
            },
            {
              "text": ",",
              "point_cs": 590
            },
            {
              "text": " ask",
              "point_cs": 630
            },
            {
              "text": " what",
              "point_cs": 656
            },
            {
              "text": " you",
              "point_cs": 684
            },
            {
              "text": " can",
              "point_cs": 714
            },
            {
              "text": " do",
              "point_cs": 734
            },
            {
              "text": " for",
              "point_cs": 756
            },
            {
              "text": " your",
              "point_cs": 776
            },
            {
              "text": " country",
              "point_cs": 814
            },
            {
              "text": ".",
              "point_cs": 814
            }
          ],
          "command": [
            "/tmp/atrain-whisper-a/.whisper-cli-patched",
            "-m",
            "/home/juergen/github/aTrain/.cache/whisper-cpp-evaluation/ggml-large-v3-turbo.bin",
            "-f",
            "/tmp/atrain-whisper-a-turbo-cpu-results/audio/leading.wav",
            "-l",
            "en",
            "-t",
            "4",
            "-bs",
            "5",
            "-tp",
            "0",
            "-nf",
            "-ng",
            "-nfa",
            "-ojf",
            "-of",
            "/tmp/atrain-whisper-a-turbo-cpu-results/patched-dtw-vad-leading",
            "--vad",
            "-vm",
            "/tmp/atrain-whisper-a/.ggml-silero-v5.1.2.bin",
            "--dtw",
            "large.v3.turbo"
          ],
          "wall_s": 20.16468765398895,
          "execution_status": "completed",
          "status": "passed"
        },
        "trailing": {
          "text": " And so, my fellow Americans, ask not what your country can do for you, ask what you can do for your country.",
          "words": [
            {
              "text": " And",
              "start_ms": 330,
              "end_ms": 530,
              "pieces": [
                " And"
              ]
            },
            {
              "text": " so,",
              "start_ms": 680,
              "end_ms": 860,
              "pieces": [
                " so",
                ","
              ]
            },
            {
              "text": " my",
              "start_ms": 860,
              "end_ms": 970,
              "pieces": [
                " my"
              ]
            },
            {
              "text": " fellow",
              "start_ms": 1020,
              "end_ms": 1510,
              "pieces": [
                " fellow"
              ]
            },
            {
              "text": " Americans,",
              "start_ms": 1510,
              "end_ms": 3440,
              "pieces": [
                " Americans",
                ","
              ]
            },
            {
              "text": " ask",
              "start_ms": 3440,
              "end_ms": 3650,
              "pieces": [
                " ask"
              ]
            },
            {
              "text": " not",
              "start_ms": 4020,
              "end_ms": 4280,
              "pieces": [
                " not"
              ]
            },
            {
              "text": " what",
              "start_ms": 5410,
              "end_ms": 5490,
              "pieces": [
                " what"
              ]
            },
            {
              "text": " your",
              "start_ms": 5490,
              "end_ms": 5820,
              "pieces": [
                " your"
              ]
            },
            {
              "text": " country",
              "start_ms": 5820,
              "end_ms": 6380,
              "pieces": [
                " country"
              ]
            },
            {
              "text": " can",
              "start_ms": 6380,
              "end_ms": 6620,
              "pieces": [
                " can"
              ]
            },
            {
              "text": " do",
              "start_ms": 6630,
              "end_ms": 6790,
              "pieces": [
                " do"
              ]
            },
            {
              "text": " for",
              "start_ms": 6790,
              "end_ms": 7030,
              "pieces": [
                " for"
              ]
            },
            {
              "text": " you,",
              "start_ms": 7030,
              "end_ms": 7470,
              "pieces": [
                " you",
                ","
              ]
            },
            {
              "text": " ask",
              "start_ms": 7470,
              "end_ms": 7560,
              "pieces": [
                " ask"
              ]
            },
            {
              "text": " what",
              "start_ms": 8190,
              "end_ms": 8690,
              "pieces": [
                " what"
              ]
            },
            {
              "text": " you",
              "start_ms": 8690,
              "end_ms": 9090,
              "pieces": [
                " you"
              ]
            },
            {
              "text": " can",
              "start_ms": 9090,
              "end_ms": 9370,
              "pieces": [
                " can"
              ]
            },
            {
              "text": " do",
              "start_ms": 9370,
              "end_ms": 9590,
              "pieces": [
                " do"
              ]
            },
            {
              "text": " for",
              "start_ms": 9590,
              "end_ms": 9730,
              "pieces": [
                " for"
              ]
            },
            {
              "text": " your",
              "start_ms": 9730,
              "end_ms": 9910,
              "pieces": [
                " your"
              ]
            },
            {
              "text": " country.",
              "start_ms": 9910,
              "end_ms": 10380,
              "pieces": [
                " country",
                "."
              ]
            }
          ],
          "problems": [],
          "dtw_points": [
            {
              "text": " And",
              "point_cs": 22
            },
            {
              "text": " so",
              "point_cs": 56
            },
            {
              "text": ",",
              "point_cs": 80
            },
            {
              "text": " my",
              "point_cs": 92
            },
            {
              "text": " fellow",
              "point_cs": 126
            },
            {
              "text": " Americans",
              "point_cs": 182
            },
            {
              "text": ",",
              "point_cs": 220
            },
            {
              "text": " ask",
              "point_cs": 262
            },
            {
              "text": " not",
              "point_cs": 310
            },
            {
              "text": " what",
              "point_cs": 358
            },
            {
              "text": " your",
              "point_cs": 382
            },
            {
              "text": " country",
              "point_cs": 426
            },
            {
              "text": " can",
              "point_cs": 464
            },
            {
              "text": " do",
              "point_cs": 484
            },
            {
              "text": " for",
              "point_cs": 508
            },
            {
              "text": " you",
              "point_cs": 542
            },
            {
              "text": ",",
              "point_cs": 578
            },
            {
              "text": " ask",
              "point_cs": 622
            },
            {
              "text": " what",
              "point_cs": 648
            },
            {
              "text": " you",
              "point_cs": 674
            },
            {
              "text": " can",
              "point_cs": 706
            },
            {
              "text": " do",
              "point_cs": 726
            },
            {
              "text": " for",
              "point_cs": 748
            },
            {
              "text": " your",
              "point_cs": 766
            },
            {
              "text": " country",
              "point_cs": 808
            },
            {
              "text": ".",
              "point_cs": 808
            }
          ],
          "command": [
            "/tmp/atrain-whisper-a/.whisper-cli-patched",
            "-m",
            "/home/juergen/github/aTrain/.cache/whisper-cpp-evaluation/ggml-large-v3-turbo.bin",
            "-f",
            "/tmp/atrain-whisper-a-turbo-cpu-results/audio/trailing.wav",
            "-l",
            "en",
            "-t",
            "4",
            "-bs",
            "5",
            "-tp",
            "0",
            "-nf",
            "-ng",
            "-nfa",
            "-ojf",
            "-of",
            "/tmp/atrain-whisper-a-turbo-cpu-results/patched-dtw-vad-trailing",
            "--vad",
            "-vm",
            "/tmp/atrain-whisper-a/.ggml-silero-v5.1.2.bin",
            "--dtw",
            "large.v3.turbo"
          ],
          "wall_s": 21.763423031006823,
          "execution_status": "completed",
          "status": "passed"
        },
        "internal": {
          "text": " And so, my fellow Americans, ask not what your country can do for you, ask what you can do for your country. And so, my fellow Americans, ask not what your country can do for you, ask what you can do for your country.",
          "words": [
            {
              "text": " And",
              "start_ms": 330,
              "end_ms": 530,
              "pieces": [
                " And"
              ]
            },
            {
              "text": " so,",
              "start_ms": 680,
              "end_ms": 860,
              "pieces": [
                " so",
                ","
              ]
            },
            {
              "text": " my",
              "start_ms": 860,
              "end_ms": 970,
              "pieces": [
                " my"
              ]
            },
            {
              "text": " fellow",
              "start_ms": 1020,
              "end_ms": 1510,
              "pieces": [
                " fellow"
              ]
            },
            {
              "text": " Americans,",
              "start_ms": 1510,
              "end_ms": 3340,
              "pieces": [
                " Americans",
                ","
              ]
            },
            {
              "text": " ask",
              "start_ms": 3340,
              "end_ms": 3630,
              "pieces": [
                " ask"
              ]
            },
            {
              "text": " not",
              "start_ms": 3630,
              "end_ms": 3650,
              "pieces": [
                " not"
              ]
            },
            {
              "text": " what",
              "start_ms": 4030,
              "end_ms": 4280,
              "pieces": [
                " what"
              ]
            },
            {
              "text": " your",
              "start_ms": 5410,
              "end_ms": 5510,
              "pieces": [
                " your"
              ]
            },
            {
              "text": " country",
              "start_ms": 5510,
              "end_ms": 6090,
              "pieces": [
                " country"
              ]
            },
            {
              "text": " can",
              "start_ms": 6210,
              "end_ms": 6420,
              "pieces": [
                " can"
              ]
            },
            {
              "text": " do",
              "start_ms": 6490,
              "end_ms": 6650,
              "pieces": [
                " do"
              ]
            },
            {
              "text": " for",
              "start_ms": 6670,
              "end_ms": 6920,
              "pieces": [
                " for"
              ]
            },
            {
              "text": " you,",
              "start_ms": 7010,
              "end_ms": 7460,
              "pieces": [
                " you",
                ","
              ]
            },
            {
              "text": " ask",
              "start_ms": 7460,
              "end_ms": 7560,
              "pieces": [
                " ask"
              ]
            },
            {
              "text": " what",
              "start_ms": 8190,
              "end_ms": 8670,
              "pieces": [
                " what"
              ]
            },
            {
              "text": " you",
              "start_ms": 8670,
              "end_ms": 9070,
              "pieces": [
                " you"
              ]
            },
            {
              "text": " can",
              "start_ms": 9070,
              "end_ms": 9370,
              "pieces": [
                " can"
              ]
            },
            {
              "text": " do",
              "start_ms": 9370,
              "end_ms": 9590,
              "pieces": [
                " do"
              ]
            },
            {
              "text": " for",
              "start_ms": 9590,
              "end_ms": 9790,
              "pieces": [
                " for"
              ]
            },
            {
              "text": " your",
              "start_ms": 9790,
              "end_ms": 9950,
              "pieces": [
                " your"
              ]
            },
            {
              "text": " country.",
              "start_ms": 9950,
              "end_ms": 10370,
              "pieces": [
                " country",
                "."
              ]
            },
            {
              "text": " And",
              "start_ms": 10410,
              "end_ms": 10590,
              "pieces": [
                " And"
              ]
            },
            {
              "text": " so,",
              "start_ms": 16350,
              "end_ms": 16560,
              "pieces": [
                " so",
                ","
              ]
            },
            {
              "text": " my",
              "start_ms": 16560,
              "end_ms": 16740,
              "pieces": [
                " my"
              ]
            },
            {
              "text": " fellow",
              "start_ms": 16740,
              "end_ms": 17280,
              "pieces": [
                " fellow"
              ]
            },
            {
              "text": " Americans,",
              "start_ms": 17280,
              "end_ms": 19270,
              "pieces": [
                " Americans",
                ","
              ]
            },
            {
              "text": " ask",
              "start_ms": 19270,
              "end_ms": 19320,
              "pieces": [
                " ask"
              ]
            },
            {
              "text": " not",
              "start_ms": 19670,
              "end_ms": 19720,
              "pieces": [
                " not"
              ]
            },
            {
              "text": " what",
              "start_ms": 19720,
              "end_ms": 19970,
              "pieces": [
                " what"
              ]
            },
            {
              "text": " your",
              "start_ms": 20260,
              "end_ms": 20380,
              "pieces": [
                " your"
              ]
            },
            {
              "text": " country",
              "start_ms": 21380,
              "end_ms": 21880,
              "pieces": [
                " country"
              ]
            },
            {
              "text": " can",
              "start_ms": 21880,
              "end_ms": 22070,
              "pieces": [
                " can"
              ]
            },
            {
              "text": " do",
              "start_ms": 22150,
              "end_ms": 22330,
              "pieces": [
                " do"
              ]
            },
            {
              "text": " for",
              "start_ms": 22330,
              "end_ms": 22570,
              "pieces": [
                " for"
              ]
            },
            {
              "text": " you,",
              "start_ms": 22660,
              "end_ms": 23050,
              "pieces": [
                " you",
                ","
              ]
            },
            {
              "text": " ask",
              "start_ms": 23050,
              "end_ms": 23170,
              "pieces": [
                " ask"
              ]
            },
            {
              "text": " what",
              "start_ms": 23530,
              "end_ms": 23650,
              "pieces": [
                " what"
              ]
            },
            {
              "text": " you",
              "start_ms": 23650,
              "end_ms": 24160,
              "pieces": [
                " you"
              ]
            },
            {
              "text": " can",
              "start_ms": 24280,
              "end_ms": 24400,
              "pieces": [
                " can"
              ]
            },
            {
              "text": " do",
              "start_ms": 24560,
              "end_ms": 24710,
              "pieces": [
                " do"
              ]
            },
            {
              "text": " for",
              "start_ms": 24710,
              "end_ms": 24970,
              "pieces": [
                " for"
              ]
            },
            {
              "text": " your",
              "start_ms": 24970,
              "end_ms": 25320,
              "pieces": [
                " your"
              ]
            },
            {
              "text": " country.",
              "start_ms": 25370,
              "end_ms": 26310,
              "pieces": [
                " country",
                "."
              ]
            }
          ],
          "problems": [],
          "dtw_points": [
            {
              "text": " And",
              "point_cs": 22
            },
            {
              "text": " so",
              "point_cs": 56
            },
            {
              "text": ",",
              "point_cs": 80
            },
            {
              "text": " my",
              "point_cs": 92
            },
            {
              "text": " fellow",
              "point_cs": 124
            },
            {
              "text": " Americans",
              "point_cs": 180
            },
            {
              "text": ",",
              "point_cs": 216
            },
            {
              "text": " ask",
              "point_cs": 262
            },
            {
              "text": " not",
              "point_cs": 314
            },
            {
              "text": " what",
              "point_cs": 358
            },
            {
              "text": " your",
              "point_cs": 382
            },
            {
              "text": " country",
              "point_cs": 426
            },
            {
              "text": " can",
              "point_cs": 464
            },
            {
              "text": " do",
              "point_cs": 484
            },
            {
              "text": " for",
              "point_cs": 508
            },
            {
              "text": " you",
              "point_cs": 542
            },
            {
              "text": ",",
              "point_cs": 582
            },
            {
              "text": " ask",
              "point_cs": 620
            },
            {
              "text": " what",
              "point_cs": 646
            },
            {
              "text": " you",
              "point_cs": 674
            },
            {
              "text": " can",
              "point_cs": 706
            },
            {
              "text": " do",
              "point_cs": 726
            },
            {
              "text": " for",
              "point_cs": 748
            },
            {
              "text": " your",
              "point_cs": 768
            },
            {
              "text": " country",
              "point_cs": 806
            },
            {
              "text": ".",
              "point_cs": 830
            },
            {
              "text": " And",
              "point_cs": 866
            },
            {
              "text": " so",
              "point_cs": 900
            },
            {
              "text": ",",
              "point_cs": 920
            },
            {
              "text": " my",
              "point_cs": 934
            },
            {
              "text": " fellow",
              "point_cs": 968
            },
            {
              "text": " Americans",
              "point_cs": 1022
            },
            {
              "text": ",",
              "point_cs": 1058
            },
            {
              "text": " ask",
              "point_cs": 1102
            },
            {
              "text": " not",
              "point_cs": 1150
            },
            {
              "text": " what",
              "point_cs": 1200
            },
            {
              "text": " your",
              "point_cs": 1224
            },
            {
              "text": " country",
              "point_cs": 1268
            },
            {
              "text": " can",
              "point_cs": 1306
            },
            {
              "text": " do",
              "point_cs": 1328
            },
            {
              "text": " for",
              "point_cs": 1350
            },
            {
              "text": " you",
              "point_cs": 1384
            },
            {
              "text": ",",
              "point_cs": 1426
            },
            {
              "text": " ask",
              "point_cs": 1466
            },
            {
              "text": " what",
              "point_cs": 1488
            },
            {
              "text": " you",
              "point_cs": 1518
            },
            {
              "text": " can",
              "point_cs": 1548
            },
            {
              "text": " do",
              "point_cs": 1570
            },
            {
              "text": " for",
              "point_cs": 1592
            },
            {
              "text": " your",
              "point_cs": 1610
            },
            {
              "text": " country",
              "point_cs": 1648
            },
            {
              "text": ".",
              "point_cs": 1648
            }
          ],
          "command": [
            "/tmp/atrain-whisper-a/.whisper-cli-patched",
            "-m",
            "/home/juergen/github/aTrain/.cache/whisper-cpp-evaluation/ggml-large-v3-turbo.bin",
            "-f",
            "/tmp/atrain-whisper-a-turbo-cpu-results/audio/internal.wav",
            "-l",
            "en",
            "-t",
            "4",
            "-bs",
            "5",
            "-tp",
            "0",
            "-nf",
            "-ng",
            "-nfa",
            "-ojf",
            "-of",
            "/tmp/atrain-whisper-a-turbo-cpu-results/patched-dtw-vad-internal",
            "--vad",
            "-vm",
            "/tmp/atrain-whisper-a/.ggml-silero-v5.1.2.bin",
            "--dtw",
            "large.v3.turbo"
          ],
          "wall_s": 23.773142805002863,
          "execution_status": "completed",
          "status": "passed"
        },
        "boundary": {
          "text": " And so, my fellow Americans, ask not what your country can do for you, ask what you can do for your country.",
          "words": [
            {
              "text": " And",
              "start_ms": 25330,
              "end_ms": 25540,
              "pieces": [
                " And"
              ]
            },
            {
              "text": " so,",
              "start_ms": 25680,
              "end_ms": 25880,
              "pieces": [
                " so",
                ","
              ]
            },
            {
              "text": " my",
              "start_ms": 25880,
              "end_ms": 26040,
              "pieces": [
                " my"
              ]
            },
            {
              "text": " fellow",
              "start_ms": 26040,
              "end_ms": 26530,
              "pieces": [
                " fellow"
              ]
            },
            {
              "text": " Americans,",
              "start_ms": 26530,
              "end_ms": 28490,
              "pieces": [
                " Americans",
                ","
              ]
            },
            {
              "text": " ask",
              "start_ms": 28490,
              "end_ms": 28650,
              "pieces": [
                " ask"
              ]
            },
            {
              "text": " not",
              "start_ms": 29020,
              "end_ms": 29280,
              "pieces": [
                " not"
              ]
            },
            {
              "text": " what",
              "start_ms": 30410,
              "end_ms": 30520,
              "pieces": [
                " what"
              ]
            },
            {
              "text": " your",
              "start_ms": 30520,
              "end_ms": 30830,
              "pieces": [
                " your"
              ]
            },
            {
              "text": " country",
              "start_ms": 30970,
              "end_ms": 31390,
              "pieces": [
                " country"
              ]
            },
            {
              "text": " can",
              "start_ms": 31390,
              "end_ms": 31630,
              "pieces": [
                " can"
              ]
            },
            {
              "text": " do",
              "start_ms": 31640,
              "end_ms": 31800,
              "pieces": [
                " do"
              ]
            },
            {
              "text": " for",
              "start_ms": 31800,
              "end_ms": 32040,
              "pieces": [
                " for"
              ]
            },
            {
              "text": " you,",
              "start_ms": 32040,
              "end_ms": 32460,
              "pieces": [
                " you",
                ","
              ]
            },
            {
              "text": " ask",
              "start_ms": 32460,
              "end_ms": 32590,
              "pieces": [
                " ask"
              ]
            },
            {
              "text": " what",
              "start_ms": 33190,
              "end_ms": 33680,
              "pieces": [
                " what"
              ]
            },
            {
              "text": " you",
              "start_ms": 33680,
              "end_ms": 34100,
              "pieces": [
                " you"
              ]
            },
            {
              "text": " can",
              "start_ms": 34100,
              "end_ms": 34380,
              "pieces": [
                " can"
              ]
            },
            {
              "text": " do",
              "start_ms": 34380,
              "end_ms": 34580,
              "pieces": [
                " do"
              ]
            },
            {
              "text": " for",
              "start_ms": 34580,
              "end_ms": 34670,
              "pieces": [
                " for"
              ]
            },
            {
              "text": " your",
              "start_ms": 34730,
              "end_ms": 34900,
              "pieces": [
                " your"
              ]
            },
            {
              "text": " country.",
              "start_ms": 34900,
              "end_ms": 35370,
              "pieces": [
                " country",
                "."
              ]
            }
          ],
          "problems": [],
          "dtw_points": [
            {
              "text": " And",
              "point_cs": 22
            },
            {
              "text": " so",
              "point_cs": 54
            },
            {
              "text": ",",
              "point_cs": 78
            },
            {
              "text": " my",
              "point_cs": 90
            },
            {
              "text": " fellow",
              "point_cs": 122
            },
            {
              "text": " Americans",
              "point_cs": 180
            },
            {
              "text": ",",
              "point_cs": 218
            },
            {
              "text": " ask",
              "point_cs": 258
            },
            {
              "text": " not",
              "point_cs": 312
            },
            {
              "text": " what",
              "point_cs": 354
            },
            {
              "text": " your",
              "point_cs": 378
            },
            {
              "text": " country",
              "point_cs": 422
            },
            {
              "text": " can",
              "point_cs": 460
            },
            {
              "text": " do",
              "point_cs": 480
            },
            {
              "text": " for",
              "point_cs": 504
            },
            {
              "text": " you",
              "point_cs": 538
            },
            {
              "text": ",",
              "point_cs": 570
            },
            {
              "text": " ask",
              "point_cs": 622
            },
            {
              "text": " what",
              "point_cs": 646
            },
            {
              "text": " you",
              "point_cs": 672
            },
            {
              "text": " can",
              "point_cs": 704
            },
            {
              "text": " do",
              "point_cs": 726
            },
            {
              "text": " for",
              "point_cs": 748
            },
            {
              "text": " your",
              "point_cs": 766
            },
            {
              "text": " country",
              "point_cs": 806
            },
            {
              "text": ".",
              "point_cs": 806
            }
          ],
          "command": [
            "/tmp/atrain-whisper-a/.whisper-cli-patched",
            "-m",
            "/home/juergen/github/aTrain/.cache/whisper-cpp-evaluation/ggml-large-v3-turbo.bin",
            "-f",
            "/tmp/atrain-whisper-a-turbo-cpu-results/audio/boundary.wav",
            "-l",
            "en",
            "-t",
            "4",
            "-bs",
            "5",
            "-tp",
            "0",
            "-nf",
            "-ng",
            "-nfa",
            "-ojf",
            "-of",
            "/tmp/atrain-whisper-a-turbo-cpu-results/patched-dtw-vad-boundary",
            "--vad",
            "-vm",
            "/tmp/atrain-whisper-a/.ggml-silero-v5.1.2.bin",
            "--dtw",
            "large.v3.turbo"
          ],
          "wall_s": 22.519108349006274,
          "execution_status": "completed",
          "status": "passed"
        },
        "silence": {
          "text": "",
          "words": [],
          "problems": [],
          "dtw_points": [],
          "command": [
            "/tmp/atrain-whisper-a/.whisper-cli-patched",
            "-m",
            "/home/juergen/github/aTrain/.cache/whisper-cpp-evaluation/ggml-large-v3-turbo.bin",
            "-f",
            "/tmp/atrain-whisper-a-turbo-cpu-results/audio/silence.wav",
            "-l",
            "en",
            "-t",
            "4",
            "-bs",
            "5",
            "-tp",
            "0",
            "-nf",
            "-ng",
            "-nfa",
            "-ojf",
            "-of",
            "/tmp/atrain-whisper-a-turbo-cpu-results/patched-dtw-vad-silence",
            "--vad",
            "-vm",
            "/tmp/atrain-whisper-a/.ggml-silero-v5.1.2.bin",
            "--dtw",
            "large.v3.turbo"
          ],
          "wall_s": 1.6178506889991695,
          "execution_status": "completed",
          "status": "passed"
        },
        "noise": {
          "text": "",
          "words": [],
          "problems": [],
          "dtw_points": [],
          "command": [
            "/tmp/atrain-whisper-a/.whisper-cli-patched",
            "-m",
            "/home/juergen/github/aTrain/.cache/whisper-cpp-evaluation/ggml-large-v3-turbo.bin",
            "-f",
            "/tmp/atrain-whisper-a-turbo-cpu-results/audio/noise.wav",
            "-l",
            "en",
            "-t",
            "4",
            "-bs",
            "5",
            "-tp",
            "0",
            "-nf",
            "-ng",
            "-nfa",
            "-ojf",
            "-of",
            "/tmp/atrain-whisper-a-turbo-cpu-results/patched-dtw-vad-noise",
            "--vad",
            "-vm",
            "/tmp/atrain-whisper-a/.ggml-silero-v5.1.2.bin",
            "--dtw",
            "large.v3.turbo"
          ],
          "wall_s": 1.5679145789908944,
          "execution_status": "completed",
          "status": "passed"
        },
        "german": {
          "text": " Hiro, Kapitel 8. Flach halten. Flach halten. Junge, du wirst es nicht packen. Das ist doch... Vergiss es. Vergiss es einfach. Doch, das hast du gut gemacht. Nein, so nicht. Netz, Netz. Hat berührt. Hat berührt. Vergiss alles, was man dir gesagt hat. Den wirst du nicht packen. Der ist gut.",
          "words": [
            {
              "text": " Hiro,",
              "start_ms": 750,
              "end_ms": 1170,
              "pieces": [
                " Hi",
                "ro",
                ","
              ]
            },
            {
              "text": " Kapitel",
              "start_ms": 1990,
              "end_ms": 2390,
              "pieces": [
                " Kap",
                "itel"
              ]
            },
            {
              "text": " 8.",
              "start_ms": 2390,
              "end_ms": 4470,
              "pieces": [
                " 8",
                "."
              ]
            },
            {
              "text": " Flach",
              "start_ms": 4470,
              "end_ms": 4820,
              "pieces": [
                " Fl",
                "ach"
              ]
            },
            {
              "text": " halten.",
              "start_ms": 4820,
              "end_ms": 5460,
              "pieces": [
                " halten",
                "."
              ]
            },
            {
              "text": " Flach",
              "start_ms": 5460,
              "end_ms": 6530,
              "pieces": [
                " Fl",
                "ach"
              ]
            },
            {
              "text": " halten.",
              "start_ms": 6530,
              "end_ms": 7490,
              "pieces": [
                " halten",
                "."
              ]
            },
            {
              "text": " Junge,",
              "start_ms": 9250,
              "end_ms": 9260,
              "pieces": [
                " Jun",
                "ge",
                ","
              ]
            },
            {
              "text": " du",
              "start_ms": 9250,
              "end_ms": 9260,
              "pieces": [
                " du"
              ]
            },
            {
              "text": " wirst",
              "start_ms": 9250,
              "end_ms": 9340,
              "pieces": [
                " w",
                "irst"
              ]
            },
            {
              "text": " es",
              "start_ms": 9340,
              "end_ms": 9380,
              "pieces": [
                " es"
              ]
            },
            {
              "text": " nicht",
              "start_ms": 9460,
              "end_ms": 9620,
              "pieces": [
                " nicht"
              ]
            },
            {
              "text": " packen.",
              "start_ms": 9930,
              "end_ms": 10460,
              "pieces": [
                " pack",
                "en",
                "."
              ]
            },
            {
              "text": " Das",
              "start_ms": 10460,
              "end_ms": 10820,
              "pieces": [
                " Das"
              ]
            },
            {
              "text": " ist",
              "start_ms": 10850,
              "end_ms": 10980,
              "pieces": [
                " ist"
              ]
            },
            {
              "text": " doch...",
              "start_ms": 10980,
              "end_ms": 12010,
              "pieces": [
                " doch",
                "..."
              ]
            },
            {
              "text": " Vergiss",
              "start_ms": 12010,
              "end_ms": 12440,
              "pieces": [
                " Verg",
                "iss"
              ]
            },
            {
              "text": " es.",
              "start_ms": 12440,
              "end_ms": 12720,
              "pieces": [
                " es",
                "."
              ]
            },
            {
              "text": " Vergiss",
              "start_ms": 12730,
              "end_ms": 13150,
              "pieces": [
                " Verg",
                "iss"
              ]
            },
            {
              "text": " es",
              "start_ms": 13270,
              "end_ms": 13280,
              "pieces": [
                " es"
              ]
            },
            {
              "text": " einfach.",
              "start_ms": 13280,
              "end_ms": 13940,
              "pieces": [
                " einfach",
                "."
              ]
            },
            {
              "text": " Doch,",
              "start_ms": 14780,
              "end_ms": 14790,
              "pieces": [
                " Doch",
                ","
              ]
            },
            {
              "text": " das",
              "start_ms": 14820,
              "end_ms": 14910,
              "pieces": [
                " das"
              ]
            },
            {
              "text": " hast",
              "start_ms": 14910,
              "end_ms": 15180,
              "pieces": [
                " hast"
              ]
            },
            {
              "text": " du",
              "start_ms": 15220,
              "end_ms": 15240,
              "pieces": [
                " du"
              ]
            },
            {
              "text": " gut",
              "start_ms": 16210,
              "end_ms": 16300,
              "pieces": [
                " gut"
              ]
            },
            {
              "text": " gemacht.",
              "start_ms": 16300,
              "end_ms": 17120,
              "pieces": [
                " gemacht",
                "."
              ]
            },
            {
              "text": " Nein,",
              "start_ms": 17120,
              "end_ms": 17860,
              "pieces": [
                " Nein",
                ","
              ]
            },
            {
              "text": " so",
              "start_ms": 17860,
              "end_ms": 18080,
              "pieces": [
                " so"
              ]
            },
            {
              "text": " nicht.",
              "start_ms": 18080,
              "end_ms": 18970,
              "pieces": [
                " nicht",
                "."
              ]
            },
            {
              "text": " Netz,",
              "start_ms": 18970,
              "end_ms": 19640,
              "pieces": [
                " Netz",
                ","
              ]
            },
            {
              "text": " Netz.",
              "start_ms": 19640,
              "end_ms": 20430,
              "pieces": [
                " Netz",
                "."
              ]
            },
            {
              "text": " Hat",
              "start_ms": 20560,
              "end_ms": 20680,
              "pieces": [
                " Hat"
              ]
            },
            {
              "text": " berührt.",
              "start_ms": 20680,
              "end_ms": 21400,
              "pieces": [
                " ber",
                "ührt",
                "."
              ]
            },
            {
              "text": " Hat",
              "start_ms": 21470,
              "end_ms": 21740,
              "pieces": [
                " Hat"
              ]
            },
            {
              "text": " berührt.",
              "start_ms": 22070,
              "end_ms": 22960,
              "pieces": [
                " ber",
                "ührt",
                "."
              ]
            },
            {
              "text": " Vergiss",
              "start_ms": 24250,
              "end_ms": 24260,
              "pieces": [
                " Verg",
                "iss"
              ]
            },
            {
              "text": " alles,",
              "start_ms": 24290,
              "end_ms": 24550,
              "pieces": [
                " alles",
                ","
              ]
            },
            {
              "text": " was",
              "start_ms": 24550,
              "end_ms": 24690,
              "pieces": [
                " was"
              ]
            },
            {
              "text": " man",
              "start_ms": 24980,
              "end_ms": 25030,
              "pieces": [
                " man"
              ]
            },
            {
              "text": " dir",
              "start_ms": 25030,
              "end_ms": 25270,
              "pieces": [
                " dir"
              ]
            },
            {
              "text": " gesagt",
              "start_ms": 25270,
              "end_ms": 25570,
              "pieces": [
                " gesagt"
              ]
            },
            {
              "text": " hat.",
              "start_ms": 25840,
              "end_ms": 26230,
              "pieces": [
                " hat",
                "."
              ]
            },
            {
              "text": " Den",
              "start_ms": 26230,
              "end_ms": 26470,
              "pieces": [
                " Den"
              ]
            },
            {
              "text": " wirst",
              "start_ms": 26470,
              "end_ms": 27160,
              "pieces": [
                " w",
                "irst"
              ]
            },
            {
              "text": " du",
              "start_ms": 27160,
              "end_ms": 27280,
              "pieces": [
                " du"
              ]
            },
            {
              "text": " nicht",
              "start_ms": 27650,
              "end_ms": 27720,
              "pieces": [
                " nicht"
              ]
            },
            {
              "text": " packen.",
              "start_ms": 27720,
              "end_ms": 28430,
              "pieces": [
                " pack",
                "en",
                "."
              ]
            },
            {
              "text": " Der",
              "start_ms": 28550,
              "end_ms": 28570,
              "pieces": [
                " Der"
              ]
            },
            {
              "text": " ist",
              "start_ms": 28570,
              "end_ms": 29070,
              "pieces": [
                " ist"
              ]
            },
            {
              "text": " gut.",
              "start_ms": 29180,
              "end_ms": 29530,
              "pieces": [
                " gut",
                "."
              ]
            }
          ],
          "problems": [
            "overlapping word interval: ' du'",
            "overlapping word interval: ' wirst'"
          ],
          "dtw_points": [
            {
              "text": " Hi",
              "point_cs": 18
            },
            {
              "text": "ro",
              "point_cs": 36
            },
            {
              "text": ",",
              "point_cs": 72
            },
            {
              "text": " Kap",
              "point_cs": 90
            },
            {
              "text": "itel",
              "point_cs": 108
            },
            {
              "text": " 8",
              "point_cs": 132
            },
            {
              "text": ".",
              "point_cs": 162
            },
            {
              "text": " Fl",
              "point_cs": 174
            },
            {
              "text": "ach",
              "point_cs": 200
            },
            {
              "text": " halten",
              "point_cs": 260
            },
            {
              "text": ".",
              "point_cs": 292
            },
            {
              "text": " Fl",
              "point_cs": 318
            },
            {
              "text": "ach",
              "point_cs": 350
            },
            {
              "text": " halten",
              "point_cs": 412
            },
            {
              "text": ".",
              "point_cs": 488
            },
            {
              "text": " Jun",
              "point_cs": 508
            },
            {
              "text": "ge",
              "point_cs": 522
            },
            {
              "text": ",",
              "point_cs": 534
            },
            {
              "text": " du",
              "point_cs": 534
            },
            {
              "text": " w",
              "point_cs": 550
            },
            {
              "text": "irst",
              "point_cs": 556
            },
            {
              "text": " es",
              "point_cs": 568
            },
            {
              "text": " nicht",
              "point_cs": 582
            },
            {
              "text": " pack",
              "point_cs": 606
            },
            {
              "text": "en",
              "point_cs": 618
            },
            {
              "text": ".",
              "point_cs": 650
            },
            {
              "text": " Das",
              "point_cs": 662
            },
            {
              "text": " ist",
              "point_cs": 676
            },
            {
              "text": " doch",
              "point_cs": 706
            },
            {
              "text": "...",
              "point_cs": 742
            },
            {
              "text": " Verg",
              "point_cs": 796
            },
            {
              "text": "iss",
              "point_cs": 824
            },
            {
              "text": " es",
              "point_cs": 848
            },
            {
              "text": ".",
              "point_cs": 860
            },
            {
              "text": " Verg",
              "point_cs": 886
            },
            {
              "text": "iss",
              "point_cs": 908
            },
            {
              "text": " es",
              "point_cs": 922
            },
            {
              "text": " einfach",
              "point_cs": 960
            },
            {
              "text": ".",
              "point_cs": 998
            },
            {
              "text": " Doch",
              "point_cs": 1046
            },
            {
              "text": ",",
              "point_cs": 1082
            },
            {
              "text": " das",
              "point_cs": 1098
            },
            {
              "text": " hast",
              "point_cs": 1112
            },
            {
              "text": " du",
              "point_cs": 1122
            },
            {
              "text": " gut",
              "point_cs": 1138
            },
            {
              "text": " gemacht",
              "point_cs": 1172
            },
            {
              "text": ".",
              "point_cs": 1200
            },
            {
              "text": " Nein",
              "point_cs": 1242
            },
            {
              "text": ",",
              "point_cs": 1272
            },
            {
              "text": " so",
              "point_cs": 1290
            },
            {
              "text": " nicht",
              "point_cs": 1352
            },
            {
              "text": ".",
              "point_cs": 1372
            },
            {
              "text": " Netz",
              "point_cs": 1416
            },
            {
              "text": ",",
              "point_cs": 1452
            },
            {
              "text": " Netz",
              "point_cs": 1494
            },
            {
              "text": ".",
              "point_cs": 1532
            },
            {
              "text": " Hat",
              "point_cs": 1552
            },
            {
              "text": " ber",
              "point_cs": 1576
            },
            {
              "text": "ührt",
              "point_cs": 1606
            },
            {
              "text": ".",
              "point_cs": 1632
            },
            {
              "text": " Hat",
              "point_cs": 1664
            },
            {
              "text": " ber",
              "point_cs": 1714
            },
            {
              "text": "ührt",
              "point_cs": 1748
            },
            {
              "text": ".",
              "point_cs": 1796
            },
            {
              "text": " Verg",
              "point_cs": 1868
            },
            {
              "text": "iss",
              "point_cs": 1894
            },
            {
              "text": " alles",
              "point_cs": 1930
            },
            {
              "text": ",",
              "point_cs": 1948
            },
            {
              "text": " was",
              "point_cs": 1958
            },
            {
              "text": " man",
              "point_cs": 1972
            },
            {
              "text": " dir",
              "point_cs": 1986
            },
            {
              "text": " gesagt",
              "point_cs": 2018
            },
            {
              "text": " hat",
              "point_cs": 2044
            },
            {
              "text": ".",
              "point_cs": 2096
            },
            {
              "text": " Den",
              "point_cs": 2124
            },
            {
              "text": " w",
              "point_cs": 2150
            },
            {
              "text": "irst",
              "point_cs": 2158
            },
            {
              "text": " du",
              "point_cs": 2176
            },
            {
              "text": " nicht",
              "point_cs": 2196
            },
            {
              "text": " pack",
              "point_cs": 2220
            },
            {
              "text": "en",
              "point_cs": 2234
            },
            {
              "text": ".",
              "point_cs": 2258
            },
            {
              "text": " Der",
              "point_cs": 2276
            },
            {
              "text": " ist",
              "point_cs": 2288
            },
            {
              "text": " gut",
              "point_cs": 2310
            },
            {
              "text": ".",
              "point_cs": 2310
            }
          ],
          "command": [
            "/tmp/atrain-whisper-a/.whisper-cli-patched",
            "-m",
            "/home/juergen/github/aTrain/.cache/whisper-cpp-evaluation/ggml-large-v3-turbo.bin",
            "-f",
            "/tmp/atrain-whisper-a-turbo-cpu-results/audio/german.wav",
            "-l",
            "de",
            "-t",
            "4",
            "-bs",
            "5",
            "-tp",
            "0",
            "-nf",
            "-ng",
            "-nfa",
            "-ojf",
            "-of",
            "/tmp/atrain-whisper-a-turbo-cpu-results/patched-dtw-vad-german",
            "--vad",
            "-vm",
            "/tmp/atrain-whisper-a/.ggml-silero-v5.1.2.bin",
            "--dtw",
            "large.v3.turbo"
          ],
          "wall_s": 21.5716965229949,
          "execution_status": "completed",
          "status": "failed"
        },
        "japanese": {
          "text": "こんにちは",
          "words": [
            {
              "text": "こんにちは",
              "start_ms": 390,
              "end_ms": 1070,
              "pieces": [
                "こんにちは"
              ]
            }
          ],
          "problems": [],
          "dtw_points": [
            {
              "text": "こんにちは",
              "point_cs": 64
            }
          ],
          "command": [
            "/tmp/atrain-whisper-a/.whisper-cli-patched",
            "-m",
            "/home/juergen/github/aTrain/.cache/whisper-cpp-evaluation/ggml-large-v3-turbo.bin",
            "-f",
            "/tmp/atrain-whisper-a-turbo-cpu-results/audio/japanese.wav",
            "-l",
            "ja",
            "-t",
            "4",
            "-bs",
            "5",
            "-tp",
            "0",
            "-nf",
            "-ng",
            "-nfa",
            "-ojf",
            "-of",
            "/tmp/atrain-whisper-a-turbo-cpu-results/patched-dtw-vad-japanese",
            "--vad",
            "-vm",
            "/tmp/atrain-whisper-a/.ggml-silero-v5.1.2.bin",
            "--dtw",
            "large.v3.turbo"
          ],
          "wall_s": 19.410166027999367,
          "execution_status": "completed",
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
            0,
            20,
            170,
            90,
            90,
            70,
            120,
            270,
            140,
            1340,
            1340,
            1530,
            730,
            680,
            1810,
            1840,
            1460,
            1540,
            410,
            370,
            370,
            280,
            290,
            230,
            230,
            140,
            20,
            0,
            0,
            30,
            0,
            10,
            10,
            0,
            0,
            0,
            0,
            0,
            0,
            60,
            0,
            10,
            10,
            10
          ],
          "max_boundary_error_ms": 1840,
          "median_boundary_error_ms": 90.0,
          "status": "failed"
        },
        "trailing": {
          "tolerance_ms": 50,
          "matched_words": 22,
          "unmatched_reference_words": 0,
          "unmatched_candidate_words": 0,
          "boundary_errors_ms": [
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0
          ],
          "max_boundary_error_ms": 0,
          "median_boundary_error_ms": 0.0,
          "status": "passed"
        },
        "boundary": {
          "tolerance_ms": 50,
          "matched_words": 22,
          "unmatched_reference_words": 0,
          "unmatched_candidate_words": 0,
          "boundary_errors_ms": [
            0,
            10,
            0,
            20,
            20,
            70,
            20,
            20,
            20,
            50,
            50,
            0,
            0,
            0,
            0,
            30,
            30,
            10,
            150,
            10,
            10,
            10,
            10,
            10,
            10,
            10,
            10,
            10,
            10,
            30,
            0,
            10,
            10,
            10,
            10,
            10,
            10,
            10,
            10,
            60,
            0,
            10,
            10,
            10
          ],
          "max_boundary_error_ms": 150,
          "median_boundary_error_ms": 10.0,
          "status": "failed"
        },
        "internal-first": {
          "tolerance_ms": 50,
          "matched_words": 22,
          "unmatched_reference_words": 0,
          "unmatched_candidate_words": 1,
          "boundary_errors_ms": [
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            100,
            100,
            20,
            390,
            630,
            1380,
            1210,
            80,
            310,
            310,
            290,
            170,
            200,
            140,
            140,
            120,
            110,
            20,
            10,
            10,
            0,
            0,
            20,
            20,
            20,
            20,
            0,
            0,
            0,
            0,
            60,
            60,
            40,
            40,
            10
          ],
          "max_boundary_error_ms": 1380,
          "median_boundary_error_ms": 20.0,
          "status": "failed"
        },
        "internal-second": {
          "tolerance_ms": 50,
          "matched_words": 21,
          "unmatched_reference_words": 1,
          "unmatched_candidate_words": 0,
          "boundary_errors_ms": [
            330,
            300,
            300,
            230,
            280,
            230,
            230,
            170,
            170,
            330,
            350,
            560,
            1690,
            1520,
            1230,
            1440,
            440,
            500,
            500,
            550,
            480,
            460,
            460,
            460,
            370,
            420,
            420,
            390,
            660,
            1040,
            1040,
            930,
            810,
            970,
            810,
            880,
            880,
            760,
            760,
            590,
            540,
            70
          ],
          "max_boundary_error_ms": 1690,
          "median_boundary_error_ms": 490.0,
          "status": "failed"
        }
      }
    }
  },
  "unverified": [
    "human reference text/boundaries; quality gates",
    "non-space-delimited-language lexical grouping",
    "word crossing 30-second boundary (audio boundary stress only)",
    "rapid speaker turns; long interviews",
    "Metal/macOS; network externally blocked; process lifecycle"
  ],
  "ordinary_candidate_structural_status": "failed",
  "production_correctness_gate": "blocked"
}
```

</details>

## paired-sequence-diagnostic.json

Original file SHA-256: `3f48cad3d8b2386f4defd94aedba68520174d4612ee779b1e6f4c65b727ff85b`

<details>
<summary>Complete recorded result</summary>

```json
{
  "method": "Diagnostic: full recognized normalized sequence equals base sequence repeated exactly twice; split by lexical order, preserving all words. No human accuracy reference.",
  "first": {
    "tolerance_ms": 50,
    "matched_words": 22,
    "unmatched_reference_words": 0,
    "unmatched_candidate_words": 0,
    "boundary_errors_ms": [
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      100,
      100,
      20,
      390,
      630,
      1380,
      1210,
      80,
      310,
      310,
      290,
      170,
      200,
      140,
      140,
      120,
      110,
      20,
      10,
      10,
      0,
      0,
      20,
      20,
      20,
      20,
      0,
      0,
      0,
      0,
      60,
      60,
      40,
      40,
      10
    ],
    "max_boundary_error_ms": 1380,
    "median_boundary_error_ms": 20.0,
    "status": "failed"
  },
  "second": {
    "tolerance_ms": 50,
    "matched_words": 22,
    "unmatched_reference_words": 0,
    "unmatched_candidate_words": 0,
    "boundary_errors_ms": [
      5920,
      5940,
      330,
      300,
      300,
      230,
      280,
      230,
      230,
      170,
      170,
      330,
      350,
      560,
      1690,
      1520,
      1230,
      1440,
      440,
      500,
      500,
      550,
      480,
      460,
      460,
      460,
      370,
      420,
      420,
      390,
      660,
      1040,
      1040,
      930,
      810,
      970,
      810,
      880,
      880,
      760,
      760,
      590,
      540,
      70
    ],
    "max_boundary_error_ms": 5940,
    "median_boundary_error_ms": 500.0,
    "status": "failed"
  },
  "boundary_words": [
    {
      "text": " your",
      "start_ms": 9790,
      "end_ms": 9950,
      "pieces": [
        " your"
      ]
    },
    {
      "text": " country.",
      "start_ms": 9950,
      "end_ms": 10370,
      "pieces": [
        " country",
        "."
      ]
    },
    {
      "text": " And",
      "start_ms": 10410,
      "end_ms": 10590,
      "pieces": [
        " And"
      ]
    },
    {
      "text": " so,",
      "start_ms": 16350,
      "end_ms": 16560,
      "pieces": [
        " so",
        ","
      ]
    },
    {
      "text": " my",
      "start_ms": 16560,
      "end_ms": 16740,
      "pieces": [
        " my"
      ]
    }
  ]
}
```

</details>
