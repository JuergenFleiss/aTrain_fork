# whisper.cpp tiny: CPU timestamp experiment

[Apple hardware acceleration tests](../apple-hardware-acceleration-tests.md)

Archived on 23 October 2026. The JSON below preserves the complete aggregate
results and listed supporting diagnostics without altering values. Absolute
paths inside these historical records identify the original run environment.
Audio, model binaries and raw execution logs are not embedded. See the index
for interpretation, limitations and links to the original artifacts.

## report.json

Original file SHA-256: `2153d9f51ad6bbc1e56f1c40d0dd286dbc00fc02468ef01f9bfb981a9acbacf2`

<details>
<summary>Complete recorded result</summary>

```json
{
  "source_commit": "d1be6fde11ac6e0407606b4e42fe72d34add8037",
  "host": "Linux-7.0.0-38-generic-x86_64-with-glibc2.43",
  "machine": "x86_64",
  "model_sha256": "be07e048e1e599ad46341c8d2a135645097a538221678b7acdd1b1919c6e1b21",
  "vad_sha256": "29940d98d42b91fbd05ce489f3ecf7c72f0a42f027e4875919a28fb4c04ea2cf",
  "helper_hashes": {
    "upstream": "ed9333ba257b89517630f9f502021d43f04786d8d9fa30f535d46b9878df4031",
    "patched": "ddd1cd92a14ba88f5b23580bae7fcb97561e463772254577ce9af56882742897"
  },
  "shift_tolerance_ms": 50,
  "grouping": "provisional whitespace EN/DE only; JA segmentation unverified",
  "fixtures": {
    "base": {
      "path": "/tmp/atrain-whisper-a-cpu-results/audio/base.wav",
      "sha256": "e94f7cfc2aa04ce40619f1e6d0b8a6c0faf94470f17fc23ddd0f804f25717f78",
      "samples": 176000,
      "duration_ms": 11000.0,
      "language": "en"
    },
    "leading": {
      "path": "/tmp/atrain-whisper-a-cpu-results/audio/leading.wav",
      "sha256": "7207dc380ee424c434c3d3602c2f6eaf86b12af6f680e6ee1cffb626e4ee21a8",
      "samples": 256000,
      "duration_ms": 16000.0,
      "language": "en"
    },
    "trailing": {
      "path": "/tmp/atrain-whisper-a-cpu-results/audio/trailing.wav",
      "sha256": "3b3bc59b1c2ff60801fa46e0dcce778d0d6111170323b8e46cce56c6b19cbd59",
      "samples": 256000,
      "duration_ms": 16000.0,
      "language": "en"
    },
    "internal": {
      "path": "/tmp/atrain-whisper-a-cpu-results/audio/internal.wav",
      "sha256": "70dc75ae98b68b01e44c58e2219db0ed7437a0511f5f4eaa2c7bdeb0623c6bb6",
      "samples": 432000,
      "duration_ms": 27000.0,
      "language": "en"
    },
    "boundary": {
      "path": "/tmp/atrain-whisper-a-cpu-results/audio/boundary.wav",
      "sha256": "4546b555cbeb960e7d6ddebe27e2c69effed93f5ecc8651bc34c58e1ad6714e3",
      "samples": 576000,
      "duration_ms": 36000.0,
      "language": "en"
    },
    "silence": {
      "path": "/tmp/atrain-whisper-a-cpu-results/audio/silence.wav",
      "sha256": "190415015d40eef0cd797e1b59ffe00846b01873050b12d44b3a216de3faa2a9",
      "samples": 128000,
      "duration_ms": 8000.0,
      "language": "en"
    },
    "noise": {
      "path": "/tmp/atrain-whisper-a-cpu-results/audio/noise.wav",
      "sha256": "52886be29e412e86511d056ebf565aafd8a3d0430ab9c6a6ea3313b22c455a84",
      "samples": 128000,
      "duration_ms": 8000.0,
      "language": "en"
    },
    "german": {
      "path": "/tmp/atrain-whisper-a-cpu-results/audio/german.wav",
      "sha256": "f409a49a190c352d282f316a5933b16d7feae401f394ee5cb552ea94706d5e56",
      "samples": 480000,
      "duration_ms": 30000.0,
      "language": "de"
    },
    "japanese": {
      "path": "/tmp/atrain-whisper-a-cpu-results/audio/japanese.wav",
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
              "start_ms": 320,
              "end_ms": 320,
              "pieces": [
                " And"
              ]
            },
            {
              "text": " so,",
              "start_ms": 330,
              "end_ms": 740,
              "pieces": [
                " so",
                ","
              ]
            },
            {
              "text": " my",
              "start_ms": 740,
              "end_ms": 950,
              "pieces": [
                " my"
              ]
            },
            {
              "text": " fellow",
              "start_ms": 950,
              "end_ms": 1590,
              "pieces": [
                " fellow"
              ]
            },
            {
              "text": " Americans,",
              "start_ms": 1590,
              "end_ms": 3000,
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
              "end_ms": 4280,
              "pieces": [
                " not"
              ]
            },
            {
              "text": " what",
              "start_ms": 4650,
              "end_ms": 5200,
              "pieces": [
                " what"
              ]
            },
            {
              "text": " your",
              "start_ms": 5410,
              "end_ms": 5560,
              "pieces": [
                " your"
              ]
            },
            {
              "text": " country",
              "start_ms": 5650,
              "end_ms": 6410,
              "pieces": [
                " country"
              ]
            },
            {
              "text": " can",
              "start_ms": 6410,
              "end_ms": 6750,
              "pieces": [
                " can"
              ]
            },
            {
              "text": " do",
              "start_ms": 6750,
              "end_ms": 6920,
              "pieces": [
                " do"
              ]
            },
            {
              "text": " for",
              "start_ms": 7010,
              "end_ms": 7490,
              "pieces": [
                " for"
              ]
            },
            {
              "text": " you,",
              "start_ms": 7490,
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
              "end_ms": 9040,
              "pieces": [
                " you"
              ]
            },
            {
              "text": " can",
              "start_ms": 9040,
              "end_ms": 9350,
              "pieces": [
                " can"
              ]
            },
            {
              "text": " do",
              "start_ms": 9350,
              "end_ms": 9500,
              "pieces": [
                " do"
              ]
            },
            {
              "text": " for",
              "start_ms": 9500,
              "end_ms": 9710,
              "pieces": [
                " for"
              ]
            },
            {
              "text": " your",
              "start_ms": 9720,
              "end_ms": 9980,
              "pieces": [
                " your"
              ]
            },
            {
              "text": " country.",
              "start_ms": 9990,
              "end_ms": 10500,
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
            "/tmp/atrain-whisper-a/.ggml-tiny.bin",
            "-f",
            "/tmp/atrain-whisper-a-cpu-results/audio/base.wav",
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
            "/tmp/atrain-whisper-a-cpu-results/upstream-ordinary-no-vad-base"
          ],
          "wall_s": 0.7663286589959171,
          "status": "failed"
        },
        "leading": {
          "text": " And so my fellow Americans ask not what your country can do for you ask what you can do for your country.",
          "words": [
            {
              "text": " And",
              "start_ms": 0,
              "end_ms": 1000,
              "pieces": [
                " And"
              ]
            },
            {
              "text": " so",
              "start_ms": 1000,
              "end_ms": 1670,
              "pieces": [
                " so"
              ]
            },
            {
              "text": " my",
              "start_ms": 1670,
              "end_ms": 2340,
              "pieces": [
                " my"
              ]
            },
            {
              "text": " fellow",
              "start_ms": 2340,
              "end_ms": 4340,
              "pieces": [
                " fellow"
              ]
            },
            {
              "text": " Americans",
              "start_ms": 5330,
              "end_ms": 7100,
              "pieces": [
                " Americans"
              ]
            },
            {
              "text": " ask",
              "start_ms": 7570,
              "end_ms": 8340,
              "pieces": [
                " ask"
              ]
            },
            {
              "text": " not",
              "start_ms": 8340,
              "end_ms": 9280,
              "pieces": [
                " not"
              ]
            },
            {
              "text": " what",
              "start_ms": 9350,
              "end_ms": 9860,
              "pieces": [
                " what"
              ]
            },
            {
              "text": " your",
              "start_ms": 10040,
              "end_ms": 10320,
              "pieces": [
                " your"
              ]
            },
            {
              "text": " country",
              "start_ms": 10410,
              "end_ms": 11320,
              "pieces": [
                " country"
              ]
            },
            {
              "text": " can",
              "start_ms": 11320,
              "end_ms": 11710,
              "pieces": [
                " can"
              ]
            },
            {
              "text": " do",
              "start_ms": 11710,
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
              "text": " you",
              "start_ms": 12490,
              "end_ms": 12970,
              "pieces": [
                " you"
              ]
            },
            {
              "text": " ask",
              "start_ms": 13190,
              "end_ms": 13440,
              "pieces": [
                " ask"
              ]
            },
            {
              "text": " what",
              "start_ms": 13440,
              "end_ms": 13750,
              "pieces": [
                " what"
              ]
            },
            {
              "text": " you",
              "start_ms": 13910,
              "end_ms": 14140,
              "pieces": [
                " you"
              ]
            },
            {
              "text": " can",
              "start_ms": 14150,
              "end_ms": 14360,
              "pieces": [
                " can"
              ]
            },
            {
              "text": " do",
              "start_ms": 14360,
              "end_ms": 14560,
              "pieces": [
                " do"
              ]
            },
            {
              "text": " for",
              "start_ms": 14560,
              "end_ms": 14760,
              "pieces": [
                " for"
              ]
            },
            {
              "text": " your",
              "start_ms": 14760,
              "end_ms": 14950,
              "pieces": [
                " your"
              ]
            },
            {
              "text": " country.",
              "start_ms": 14950,
              "end_ms": 15440,
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
            "/tmp/atrain-whisper-a/.ggml-tiny.bin",
            "-f",
            "/tmp/atrain-whisper-a-cpu-results/audio/leading.wav",
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
            "/tmp/atrain-whisper-a-cpu-results/upstream-ordinary-no-vad-leading"
          ],
          "wall_s": 0.7657948120031506,
          "status": "passed"
        },
        "trailing": {
          "text": " And so, my fellow Americans, ask not what your country can do for you, ask what you can do for your country.",
          "words": [
            {
              "text": " And",
              "start_ms": 320,
              "end_ms": 320,
              "pieces": [
                " And"
              ]
            },
            {
              "text": " so,",
              "start_ms": 330,
              "end_ms": 740,
              "pieces": [
                " so",
                ","
              ]
            },
            {
              "text": " my",
              "start_ms": 740,
              "end_ms": 950,
              "pieces": [
                " my"
              ]
            },
            {
              "text": " fellow",
              "start_ms": 950,
              "end_ms": 1590,
              "pieces": [
                " fellow"
              ]
            },
            {
              "text": " Americans,",
              "start_ms": 1590,
              "end_ms": 3000,
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
              "end_ms": 4280,
              "pieces": [
                " not"
              ]
            },
            {
              "text": " what",
              "start_ms": 4650,
              "end_ms": 5200,
              "pieces": [
                " what"
              ]
            },
            {
              "text": " your",
              "start_ms": 5410,
              "end_ms": 5560,
              "pieces": [
                " your"
              ]
            },
            {
              "text": " country",
              "start_ms": 5650,
              "end_ms": 6410,
              "pieces": [
                " country"
              ]
            },
            {
              "text": " can",
              "start_ms": 6410,
              "end_ms": 6750,
              "pieces": [
                " can"
              ]
            },
            {
              "text": " do",
              "start_ms": 6750,
              "end_ms": 6920,
              "pieces": [
                " do"
              ]
            },
            {
              "text": " for",
              "start_ms": 7010,
              "end_ms": 7490,
              "pieces": [
                " for"
              ]
            },
            {
              "text": " you,",
              "start_ms": 7490,
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
              "end_ms": 9040,
              "pieces": [
                " you"
              ]
            },
            {
              "text": " can",
              "start_ms": 9040,
              "end_ms": 9350,
              "pieces": [
                " can"
              ]
            },
            {
              "text": " do",
              "start_ms": 9350,
              "end_ms": 9500,
              "pieces": [
                " do"
              ]
            },
            {
              "text": " for",
              "start_ms": 9500,
              "end_ms": 9710,
              "pieces": [
                " for"
              ]
            },
            {
              "text": " your",
              "start_ms": 9720,
              "end_ms": 9980,
              "pieces": [
                " your"
              ]
            },
            {
              "text": " country.",
              "start_ms": 9990,
              "end_ms": 10500,
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
            "/tmp/atrain-whisper-a/.ggml-tiny.bin",
            "-f",
            "/tmp/atrain-whisper-a-cpu-results/audio/trailing.wav",
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
            "/tmp/atrain-whisper-a-cpu-results/upstream-ordinary-no-vad-trailing"
          ],
          "wall_s": 0.8161702729994431,
          "status": "failed"
        },
        "internal": {
          "text": " And so my fellow Americans ask not what your country can do for you ask what you can do for your country. And so my fellow Americans ask not what your country can do for you ask what you can do for your country.",
          "words": [
            {
              "text": " And",
              "start_ms": 320,
              "end_ms": 350,
              "pieces": [
                " And"
              ]
            },
            {
              "text": " so",
              "start_ms": 350,
              "end_ms": 540,
              "pieces": [
                " so"
              ]
            },
            {
              "text": " my",
              "start_ms": 680,
              "end_ms": 810,
              "pieces": [
                " my"
              ]
            },
            {
              "text": " fellow",
              "start_ms": 810,
              "end_ms": 1510,
              "pieces": [
                " fellow"
              ]
            },
            {
              "text": " Americans",
              "start_ms": 1510,
              "end_ms": 2100,
              "pieces": [
                " Americans"
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
              "end_ms": 4280,
              "pieces": [
                " not"
              ]
            },
            {
              "text": " what",
              "start_ms": 4650,
              "end_ms": 5160,
              "pieces": [
                " what"
              ]
            },
            {
              "text": " your",
              "start_ms": 5410,
              "end_ms": 5560,
              "pieces": [
                " your"
              ]
            },
            {
              "text": " country",
              "start_ms": 5650,
              "end_ms": 6270,
              "pieces": [
                " country"
              ]
            },
            {
              "text": " can",
              "start_ms": 6270,
              "end_ms": 6570,
              "pieces": [
                " can"
              ]
            },
            {
              "text": " do",
              "start_ms": 6570,
              "end_ms": 6800,
              "pieces": [
                " do"
              ]
            },
            {
              "text": " for",
              "start_ms": 6800,
              "end_ms": 7090,
              "pieces": [
                " for"
              ]
            },
            {
              "text": " you",
              "start_ms": 7150,
              "end_ms": 7400,
              "pieces": [
                " you"
              ]
            },
            {
              "text": " ask",
              "start_ms": 7400,
              "end_ms": 8480,
              "pieces": [
                " ask"
              ]
            },
            {
              "text": " what",
              "start_ms": 8630,
              "end_ms": 8750,
              "pieces": [
                " what"
              ]
            },
            {
              "text": " you",
              "start_ms": 8910,
              "end_ms": 9040,
              "pieces": [
                " you"
              ]
            },
            {
              "text": " can",
              "start_ms": 9040,
              "end_ms": 9350,
              "pieces": [
                " can"
              ]
            },
            {
              "text": " do",
              "start_ms": 9350,
              "end_ms": 9500,
              "pieces": [
                " do"
              ]
            },
            {
              "text": " for",
              "start_ms": 9500,
              "end_ms": 9710,
              "pieces": [
                " for"
              ]
            },
            {
              "text": " your",
              "start_ms": 9720,
              "end_ms": 9980,
              "pieces": [
                " your"
              ]
            },
            {
              "text": " country.",
              "start_ms": 9990,
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
              "text": " so",
              "start_ms": 16000,
              "end_ms": 16000,
              "pieces": [
                " so"
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
              "text": " Americans",
              "start_ms": 16330,
              "end_ms": 18100,
              "pieces": [
                " Americans"
              ]
            },
            {
              "text": " ask",
              "start_ms": 19290,
              "end_ms": 19650,
              "pieces": [
                " ask"
              ]
            },
            {
              "text": " not",
              "start_ms": 20010,
              "end_ms": 20290,
              "pieces": [
                " not"
              ]
            },
            {
              "text": " what",
              "start_ms": 21410,
              "end_ms": 21430,
              "pieces": [
                " what"
              ]
            },
            {
              "text": " your",
              "start_ms": 21430,
              "end_ms": 21830,
              "pieces": [
                " your"
              ]
            },
            {
              "text": " country",
              "start_ms": 21970,
              "end_ms": 22610,
              "pieces": [
                " country"
              ]
            },
            {
              "text": " can",
              "start_ms": 22620,
              "end_ms": 22900,
              "pieces": [
                " can"
              ]
            },
            {
              "text": " do",
              "start_ms": 23010,
              "end_ms": 23150,
              "pieces": [
                " do"
              ]
            },
            {
              "text": " for",
              "start_ms": 23150,
              "end_ms": 23470,
              "pieces": [
                " for"
              ]
            },
            {
              "text": " you",
              "start_ms": 23470,
              "end_ms": 23670,
              "pieces": [
                " you"
              ]
            },
            {
              "text": " ask",
              "start_ms": 23780,
              "end_ms": 24100,
              "pieces": [
                " ask"
              ]
            },
            {
              "text": " what",
              "start_ms": 24190,
              "end_ms": 24470,
              "pieces": [
                " what"
              ]
            },
            {
              "text": " you",
              "start_ms": 24640,
              "end_ms": 24750,
              "pieces": [
                " you"
              ]
            },
            {
              "text": " can",
              "start_ms": 24910,
              "end_ms": 25170,
              "pieces": [
                " can"
              ]
            },
            {
              "text": " do",
              "start_ms": 25190,
              "end_ms": 25380,
              "pieces": [
                " do"
              ]
            },
            {
              "text": " for",
              "start_ms": 25440,
              "end_ms": 25670,
              "pieces": [
                " for"
              ]
            },
            {
              "text": " your",
              "start_ms": 25720,
              "end_ms": 26140,
              "pieces": [
                " your"
              ]
            },
            {
              "text": " country.",
              "start_ms": 26140,
              "end_ms": 27000,
              "pieces": [
                " country",
                "."
              ]
            }
          ],
          "problems": [
            "nonpositive word interval: ' And'",
            "nonpositive word interval: ' so'",
            "nonpositive word interval: ' my'",
            "nonpositive word interval: ' fellow'"
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
            "/tmp/atrain-whisper-a/.ggml-tiny.bin",
            "-f",
            "/tmp/atrain-whisper-a-cpu-results/audio/internal.wav",
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
            "/tmp/atrain-whisper-a-cpu-results/upstream-ordinary-no-vad-internal"
          ],
          "wall_s": 0.9160425570007646,
          "status": "failed"
        },
        "boundary": {
          "text": " And so my fellow Americans, ask not. Watch your country, can do for you, ask what you can do for your country.",
          "words": [
            {
              "text": " And",
              "start_ms": 0,
              "end_ms": 15480,
              "pieces": [
                " And"
              ]
            },
            {
              "text": " so",
              "start_ms": 25070,
              "end_ms": 25820,
              "pieces": [
                " so"
              ]
            },
            {
              "text": " my",
              "start_ms": 25820,
              "end_ms": 26070,
              "pieces": [
                " my"
              ]
            },
            {
              "text": " fellow",
              "start_ms": 26070,
              "end_ms": 26830,
              "pieces": [
                " fellow"
              ]
            },
            {
              "text": " Americans,",
              "start_ms": 26830,
              "end_ms": 28310,
              "pieces": [
                " Americans",
                ","
              ]
            },
            {
              "text": " ask",
              "start_ms": 28310,
              "end_ms": 28650,
              "pieces": [
                " ask"
              ]
            },
            {
              "text": " not.",
              "start_ms": 29010,
              "end_ms": 29240,
              "pieces": [
                " not",
                "."
              ]
            },
            {
              "text": " Watch",
              "start_ms": 29240,
              "end_ms": 29900,
              "pieces": [
                " Watch"
              ]
            },
            {
              "text": " your",
              "start_ms": 29900,
              "end_ms": 30420,
              "pieces": [
                " your"
              ]
            },
            {
              "text": " country,",
              "start_ms": 30420,
              "end_ms": 31600,
              "pieces": [
                " country",
                ","
              ]
            },
            {
              "text": " can",
              "start_ms": 31600,
              "end_ms": 31990,
              "pieces": [
                " can"
              ]
            },
            {
              "text": " do",
              "start_ms": 31990,
              "end_ms": 32250,
              "pieces": [
                " do"
              ]
            },
            {
              "text": " for",
              "start_ms": 32250,
              "end_ms": 32640,
              "pieces": [
                " for"
              ]
            },
            {
              "text": " you,",
              "start_ms": 32640,
              "end_ms": 33230,
              "pieces": [
                " you",
                ","
              ]
            },
            {
              "text": " ask",
              "start_ms": 33230,
              "end_ms": 33460,
              "pieces": [
                " ask"
              ]
            },
            {
              "text": " what",
              "start_ms": 33460,
              "end_ms": 33760,
              "pieces": [
                " what"
              ]
            },
            {
              "text": " you",
              "start_ms": 33760,
              "end_ms": 33990,
              "pieces": [
                " you"
              ]
            },
            {
              "text": " can",
              "start_ms": 33990,
              "end_ms": 34220,
              "pieces": [
                " can"
              ]
            },
            {
              "text": " do",
              "start_ms": 34220,
              "end_ms": 34370,
              "pieces": [
                " do"
              ]
            },
            {
              "text": " for",
              "start_ms": 34370,
              "end_ms": 34600,
              "pieces": [
                " for"
              ]
            },
            {
              "text": " your",
              "start_ms": 34600,
              "end_ms": 34900,
              "pieces": [
                " your"
              ]
            },
            {
              "text": " country.",
              "start_ms": 34900,
              "end_ms": 35480,
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
              "text": ".",
              "point_cs": -1
            },
            {
              "text": " Watch",
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
              "text": ",",
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
            "/tmp/atrain-whisper-a/.ggml-tiny.bin",
            "-f",
            "/tmp/atrain-whisper-a-cpu-results/audio/boundary.wav",
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
            "/tmp/atrain-whisper-a-cpu-results/upstream-ordinary-no-vad-boundary"
          ],
          "wall_s": 1.2669080250052502,
          "status": "passed"
        },
        "silence": {
          "text": " [BLANK_AUDIO]",
          "words": [
            {
              "text": " [BLANK_AUDIO]",
              "start_ms": 0,
              "end_ms": 7990,
              "pieces": [
                " [",
                "BLANK",
                "_",
                "AUDIO",
                "]"
              ]
            }
          ],
          "problems": [
            "recognized words on silence-only fixture"
          ],
          "dtw_points": [
            {
              "text": " [",
              "point_cs": -1
            },
            {
              "text": "BLANK",
              "point_cs": -1
            },
            {
              "text": "_",
              "point_cs": -1
            },
            {
              "text": "AUDIO",
              "point_cs": -1
            },
            {
              "text": "]",
              "point_cs": -1
            }
          ],
          "command": [
            "/tmp/atrain-whisper-a/.whisper-cli-unpatched",
            "-m",
            "/tmp/atrain-whisper-a/.ggml-tiny.bin",
            "-f",
            "/tmp/atrain-whisper-a-cpu-results/audio/silence.wav",
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
            "/tmp/atrain-whisper-a-cpu-results/upstream-ordinary-no-vad-silence"
          ],
          "wall_s": 0.615721323993057,
          "status": "failed"
        },
        "noise": {
          "text": " (water bubbling)",
          "words": [
            {
              "text": " (water",
              "start_ms": 0,
              "end_ms": 1020,
              "pieces": [
                " (",
                "water"
              ]
            },
            {
              "text": " bubbling)",
              "start_ms": 1020,
              "end_ms": 2580,
              "pieces": [
                " bubbling",
                ")"
              ]
            }
          ],
          "problems": [
            "recognized words on noise-only fixture"
          ],
          "dtw_points": [
            {
              "text": " (",
              "point_cs": -1
            },
            {
              "text": "water",
              "point_cs": -1
            },
            {
              "text": " bubbling",
              "point_cs": -1
            },
            {
              "text": ")",
              "point_cs": -1
            }
          ],
          "command": [
            "/tmp/atrain-whisper-a/.whisper-cli-unpatched",
            "-m",
            "/tmp/atrain-whisper-a/.ggml-tiny.bin",
            "-f",
            "/tmp/atrain-whisper-a-cpu-results/audio/noise.wav",
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
            "/tmp/atrain-whisper-a-cpu-results/upstream-ordinary-no-vad-noise"
          ],
          "wall_s": 0.6155212619923986,
          "status": "failed"
        },
        "german": {
          "text": " Das ist das Video, das ist das Video, das Video, das Video, das Video, das Video, das Video, das Video, das Video, das Video, das Video, das Video, das Video, das Video, das Video, das Video, das Video, das Video, das Video, das Video, das Video, das Video, das Video, das Video, das Video, das Video, das Video, das Video, das Video, das Video, das Video, das Video, das Video, das Video, das Video, das Video, das Video, das Video, das Video, das Video, das Video, das Video, das Video, das Video, das Video, das Video, das Video, das Video, das Video, das Video, das Video, das Video, das Video, das Video, das Video, das Video, das Video, das Video, das Video, das Video, das Video, das Video, das Video, das Video, das Video, das Video, das Video, das Video, das Video, das Video, das Video, das Video",
          "words": [
            {
              "text": " Das",
              "start_ms": 0,
              "end_ms": 510,
              "pieces": [
                " Das"
              ]
            },
            {
              "text": " ist",
              "start_ms": 710,
              "end_ms": 1040,
              "pieces": [
                " ist"
              ]
            },
            {
              "text": " das",
              "start_ms": 1040,
              "end_ms": 1270,
              "pieces": [
                " das"
              ]
            },
            {
              "text": " Video,",
              "start_ms": 1980,
              "end_ms": 2760,
              "pieces": [
                " Video",
                ","
              ]
            },
            {
              "text": " das",
              "start_ms": 2760,
              "end_ms": 3290,
              "pieces": [
                " das"
              ]
            },
            {
              "text": " ist",
              "start_ms": 3290,
              "end_ms": 3810,
              "pieces": [
                " ist"
              ]
            },
            {
              "text": " das",
              "start_ms": 4240,
              "end_ms": 4330,
              "pieces": [
                " das"
              ]
            },
            {
              "text": " Video,",
              "start_ms": 4330,
              "end_ms": 5520,
              "pieces": [
                " Video",
                ","
              ]
            },
            {
              "text": " das",
              "start_ms": 5520,
              "end_ms": 6060,
              "pieces": [
                " das"
              ]
            },
            {
              "text": " Video,",
              "start_ms": 6320,
              "end_ms": 7110,
              "pieces": [
                " Video",
                ","
              ]
            },
            {
              "text": " das",
              "start_ms": 7110,
              "end_ms": 7260,
              "pieces": [
                " das"
              ]
            },
            {
              "text": " Video,",
              "start_ms": 7270,
              "end_ms": 7640,
              "pieces": [
                " Video",
                ","
              ]
            },
            {
              "text": " das",
              "start_ms": 7650,
              "end_ms": 7810,
              "pieces": [
                " das"
              ]
            },
            {
              "text": " Video,",
              "start_ms": 7810,
              "end_ms": 8190,
              "pieces": [
                " Video",
                ","
              ]
            },
            {
              "text": " das",
              "start_ms": 8190,
              "end_ms": 8350,
              "pieces": [
                " das"
              ]
            },
            {
              "text": " Video,",
              "start_ms": 8350,
              "end_ms": 8730,
              "pieces": [
                " Video",
                ","
              ]
            },
            {
              "text": " das",
              "start_ms": 8730,
              "end_ms": 8830,
              "pieces": [
                " das"
              ]
            },
            {
              "text": " Video,",
              "start_ms": 8960,
              "end_ms": 9240,
              "pieces": [
                " Video",
                ","
              ]
            },
            {
              "text": " das",
              "start_ms": 9280,
              "end_ms": 9400,
              "pieces": [
                " das"
              ]
            },
            {
              "text": " Video,",
              "start_ms": 9450,
              "end_ms": 9810,
              "pieces": [
                " Video",
                ","
              ]
            },
            {
              "text": " das",
              "start_ms": 9810,
              "end_ms": 9960,
              "pieces": [
                " das"
              ]
            },
            {
              "text": " Video,",
              "start_ms": 9980,
              "end_ms": 10350,
              "pieces": [
                " Video",
                ","
              ]
            },
            {
              "text": " das",
              "start_ms": 10350,
              "end_ms": 10470,
              "pieces": [
                " das"
              ]
            },
            {
              "text": " Video,",
              "start_ms": 10500,
              "end_ms": 10890,
              "pieces": [
                " Video",
                ","
              ]
            },
            {
              "text": " das",
              "start_ms": 10890,
              "end_ms": 10980,
              "pieces": [
                " das"
              ]
            },
            {
              "text": " Video,",
              "start_ms": 11050,
              "end_ms": 11430,
              "pieces": [
                " Video",
                ","
              ]
            },
            {
              "text": " das",
              "start_ms": 11430,
              "end_ms": 11470,
              "pieces": [
                " das"
              ]
            },
            {
              "text": " Video,",
              "start_ms": 11580,
              "end_ms": 12020,
              "pieces": [
                " Video",
                ","
              ]
            },
            {
              "text": " das",
              "start_ms": 12080,
              "end_ms": 12150,
              "pieces": [
                " das"
              ]
            },
            {
              "text": " Video,",
              "start_ms": 12280,
              "end_ms": 12340,
              "pieces": [
                " Video",
                ","
              ]
            },
            {
              "text": " das",
              "start_ms": 12370,
              "end_ms": 12440,
              "pieces": [
                " das"
              ]
            },
            {
              "text": " Video,",
              "start_ms": 12450,
              "end_ms": 12640,
              "pieces": [
                " Video",
                ","
              ]
            },
            {
              "text": " das",
              "start_ms": 12660,
              "end_ms": 12750,
              "pieces": [
                " das"
              ]
            },
            {
              "text": " Video,",
              "start_ms": 12750,
              "end_ms": 12960,
              "pieces": [
                " Video",
                ","
              ]
            },
            {
              "text": " das",
              "start_ms": 12960,
              "end_ms": 13050,
              "pieces": [
                " das"
              ]
            },
            {
              "text": " Video,",
              "start_ms": 13050,
              "end_ms": 13250,
              "pieces": [
                " Video",
                ","
              ]
            },
            {
              "text": " das",
              "start_ms": 13260,
              "end_ms": 13350,
              "pieces": [
                " das"
              ]
            },
            {
              "text": " Video,",
              "start_ms": 13350,
              "end_ms": 13550,
              "pieces": [
                " Video",
                ","
              ]
            },
            {
              "text": " das",
              "start_ms": 13550,
              "end_ms": 13650,
              "pieces": [
                " das"
              ]
            },
            {
              "text": " Video,",
              "start_ms": 13650,
              "end_ms": 13860,
              "pieces": [
                " Video",
                ","
              ]
            },
            {
              "text": " das",
              "start_ms": 13860,
              "end_ms": 13950,
              "pieces": [
                " das"
              ]
            },
            {
              "text": " Video,",
              "start_ms": 13950,
              "end_ms": 14160,
              "pieces": [
                " Video",
                ","
              ]
            },
            {
              "text": " das",
              "start_ms": 14160,
              "end_ms": 14250,
              "pieces": [
                " das"
              ]
            },
            {
              "text": " Video,",
              "start_ms": 14250,
              "end_ms": 14460,
              "pieces": [
                " Video",
                ","
              ]
            },
            {
              "text": " das",
              "start_ms": 14460,
              "end_ms": 14550,
              "pieces": [
                " das"
              ]
            },
            {
              "text": " Video,",
              "start_ms": 14580,
              "end_ms": 14760,
              "pieces": [
                " Video",
                ","
              ]
            },
            {
              "text": " das",
              "start_ms": 14780,
              "end_ms": 14850,
              "pieces": [
                " das"
              ]
            },
            {
              "text": " Video,",
              "start_ms": 14850,
              "end_ms": 15060,
              "pieces": [
                " Video",
                ","
              ]
            },
            {
              "text": " das",
              "start_ms": 15060,
              "end_ms": 15150,
              "pieces": [
                " das"
              ]
            },
            {
              "text": " Video,",
              "start_ms": 15150,
              "end_ms": 15360,
              "pieces": [
                " Video",
                ","
              ]
            },
            {
              "text": " das",
              "start_ms": 15360,
              "end_ms": 15430,
              "pieces": [
                " das"
              ]
            },
            {
              "text": " Video,",
              "start_ms": 15440,
              "end_ms": 15650,
              "pieces": [
                " Video",
                ","
              ]
            },
            {
              "text": " das",
              "start_ms": 15660,
              "end_ms": 15750,
              "pieces": [
                " das"
              ]
            },
            {
              "text": " Video,",
              "start_ms": 15750,
              "end_ms": 15960,
              "pieces": [
                " Video",
                ","
              ]
            },
            {
              "text": " das",
              "start_ms": 15960,
              "end_ms": 16050,
              "pieces": [
                " das"
              ]
            },
            {
              "text": " Video,",
              "start_ms": 16090,
              "end_ms": 16240,
              "pieces": [
                " Video",
                ","
              ]
            },
            {
              "text": " das",
              "start_ms": 16260,
              "end_ms": 16350,
              "pieces": [
                " das"
              ]
            },
            {
              "text": " Video,",
              "start_ms": 16350,
              "end_ms": 16550,
              "pieces": [
                " Video",
                ","
              ]
            },
            {
              "text": " das",
              "start_ms": 16570,
              "end_ms": 16650,
              "pieces": [
                " das"
              ]
            },
            {
              "text": " Video,",
              "start_ms": 16650,
              "end_ms": 16840,
              "pieces": [
                " Video",
                ","
              ]
            },
            {
              "text": " das",
              "start_ms": 16870,
              "end_ms": 16950,
              "pieces": [
                " das"
              ]
            },
            {
              "text": " Video,",
              "start_ms": 16950,
              "end_ms": 17150,
              "pieces": [
                " Video",
                ","
              ]
            },
            {
              "text": " das",
              "start_ms": 17160,
              "end_ms": 17250,
              "pieces": [
                " das"
              ]
            },
            {
              "text": " Video,",
              "start_ms": 17250,
              "end_ms": 17460,
              "pieces": [
                " Video",
                ","
              ]
            },
            {
              "text": " das",
              "start_ms": 17460,
              "end_ms": 17550,
              "pieces": [
                " das"
              ]
            },
            {
              "text": " Video,",
              "start_ms": 17550,
              "end_ms": 17750,
              "pieces": [
                " Video",
                ","
              ]
            },
            {
              "text": " das",
              "start_ms": 17760,
              "end_ms": 17850,
              "pieces": [
                " das"
              ]
            },
            {
              "text": " Video,",
              "start_ms": 17850,
              "end_ms": 18050,
              "pieces": [
                " Video",
                ","
              ]
            },
            {
              "text": " das",
              "start_ms": 18060,
              "end_ms": 18150,
              "pieces": [
                " das"
              ]
            },
            {
              "text": " Video,",
              "start_ms": 18150,
              "end_ms": 18360,
              "pieces": [
                " Video",
                ","
              ]
            },
            {
              "text": " das",
              "start_ms": 18360,
              "end_ms": 18450,
              "pieces": [
                " das"
              ]
            },
            {
              "text": " Video,",
              "start_ms": 18450,
              "end_ms": 18650,
              "pieces": [
                " Video",
                ","
              ]
            },
            {
              "text": " das",
              "start_ms": 18650,
              "end_ms": 18750,
              "pieces": [
                " das"
              ]
            },
            {
              "text": " Video,",
              "start_ms": 18750,
              "end_ms": 18960,
              "pieces": [
                " Video",
                ","
              ]
            },
            {
              "text": " das",
              "start_ms": 18960,
              "end_ms": 19000,
              "pieces": [
                " das"
              ]
            },
            {
              "text": " Video,",
              "start_ms": 19190,
              "end_ms": 19220,
              "pieces": [
                " Video",
                ","
              ]
            },
            {
              "text": " das",
              "start_ms": 19270,
              "end_ms": 19340,
              "pieces": [
                " das"
              ]
            },
            {
              "text": " Video,",
              "start_ms": 19390,
              "end_ms": 19550,
              "pieces": [
                " Video",
                ","
              ]
            },
            {
              "text": " das",
              "start_ms": 19560,
              "end_ms": 19650,
              "pieces": [
                " das"
              ]
            },
            {
              "text": " Video,",
              "start_ms": 19650,
              "end_ms": 19830,
              "pieces": [
                " Video",
                ","
              ]
            },
            {
              "text": " das",
              "start_ms": 19940,
              "end_ms": 19940,
              "pieces": [
                " das"
              ]
            },
            {
              "text": " Video,",
              "start_ms": 19970,
              "end_ms": 20160,
              "pieces": [
                " Video",
                ","
              ]
            },
            {
              "text": " das",
              "start_ms": 20160,
              "end_ms": 20190,
              "pieces": [
                " das"
              ]
            },
            {
              "text": " Video,",
              "start_ms": 20330,
              "end_ms": 20400,
              "pieces": [
                " Video",
                ","
              ]
            },
            {
              "text": " das",
              "start_ms": 20460,
              "end_ms": 20550,
              "pieces": [
                " das"
              ]
            },
            {
              "text": " Video,",
              "start_ms": 20550,
              "end_ms": 20760,
              "pieces": [
                " Video",
                ","
              ]
            },
            {
              "text": " das",
              "start_ms": 20760,
              "end_ms": 20850,
              "pieces": [
                " das"
              ]
            },
            {
              "text": " Video,",
              "start_ms": 20850,
              "end_ms": 21050,
              "pieces": [
                " Video",
                ","
              ]
            },
            {
              "text": " das",
              "start_ms": 21060,
              "end_ms": 21140,
              "pieces": [
                " das"
              ]
            },
            {
              "text": " Video,",
              "start_ms": 21150,
              "end_ms": 21350,
              "pieces": [
                " Video",
                ","
              ]
            },
            {
              "text": " das",
              "start_ms": 21350,
              "end_ms": 21450,
              "pieces": [
                " das"
              ]
            },
            {
              "text": " Video,",
              "start_ms": 21450,
              "end_ms": 21600,
              "pieces": [
                " Video",
                ","
              ]
            },
            {
              "text": " das",
              "start_ms": 21670,
              "end_ms": 21730,
              "pieces": [
                " das"
              ]
            },
            {
              "text": " Video,",
              "start_ms": 21780,
              "end_ms": 21930,
              "pieces": [
                " Video",
                ","
              ]
            },
            {
              "text": " das",
              "start_ms": 21960,
              "end_ms": 22030,
              "pieces": [
                " das"
              ]
            },
            {
              "text": " Video,",
              "start_ms": 22060,
              "end_ms": 22260,
              "pieces": [
                " Video",
                ","
              ]
            },
            {
              "text": " das",
              "start_ms": 22260,
              "end_ms": 22350,
              "pieces": [
                " das"
              ]
            },
            {
              "text": " Video,",
              "start_ms": 22350,
              "end_ms": 22550,
              "pieces": [
                " Video",
                ","
              ]
            },
            {
              "text": " das",
              "start_ms": 22550,
              "end_ms": 22650,
              "pieces": [
                " das"
              ]
            },
            {
              "text": " Video,",
              "start_ms": 22650,
              "end_ms": 22860,
              "pieces": [
                " Video",
                ","
              ]
            },
            {
              "text": " das",
              "start_ms": 22860,
              "end_ms": 22940,
              "pieces": [
                " das"
              ]
            },
            {
              "text": " Video,",
              "start_ms": 22990,
              "end_ms": 23160,
              "pieces": [
                " Video",
                ","
              ]
            },
            {
              "text": " das",
              "start_ms": 23160,
              "end_ms": 23180,
              "pieces": [
                " das"
              ]
            },
            {
              "text": " Video,",
              "start_ms": 23260,
              "end_ms": 23460,
              "pieces": [
                " Video",
                ","
              ]
            },
            {
              "text": " das",
              "start_ms": 23460,
              "end_ms": 23550,
              "pieces": [
                " das"
              ]
            },
            {
              "text": " Video,",
              "start_ms": 23550,
              "end_ms": 23760,
              "pieces": [
                " Video",
                ","
              ]
            },
            {
              "text": " das",
              "start_ms": 23760,
              "end_ms": 23850,
              "pieces": [
                " das"
              ]
            },
            {
              "text": " Video,",
              "start_ms": 23850,
              "end_ms": 24060,
              "pieces": [
                " Video",
                ","
              ]
            },
            {
              "text": " das",
              "start_ms": 24060,
              "end_ms": 24140,
              "pieces": [
                " das"
              ]
            },
            {
              "text": " Video,",
              "start_ms": 24220,
              "end_ms": 24360,
              "pieces": [
                " Video",
                ","
              ]
            },
            {
              "text": " das",
              "start_ms": 24370,
              "end_ms": 24370,
              "pieces": [
                " das"
              ]
            },
            {
              "text": " Video,",
              "start_ms": 24480,
              "end_ms": 24660,
              "pieces": [
                " Video",
                ","
              ]
            },
            {
              "text": " das",
              "start_ms": 24660,
              "end_ms": 24750,
              "pieces": [
                " das"
              ]
            },
            {
              "text": " Video,",
              "start_ms": 24750,
              "end_ms": 24950,
              "pieces": [
                " Video",
                ","
              ]
            },
            {
              "text": " das",
              "start_ms": 24970,
              "end_ms": 25030,
              "pieces": [
                " das"
              ]
            },
            {
              "text": " Video,",
              "start_ms": 25060,
              "end_ms": 25260,
              "pieces": [
                " Video",
                ","
              ]
            },
            {
              "text": " das",
              "start_ms": 25260,
              "end_ms": 25340,
              "pieces": [
                " das"
              ]
            },
            {
              "text": " Video,",
              "start_ms": 25350,
              "end_ms": 25550,
              "pieces": [
                " Video",
                ","
              ]
            },
            {
              "text": " das",
              "start_ms": 25590,
              "end_ms": 25650,
              "pieces": [
                " das"
              ]
            },
            {
              "text": " Video,",
              "start_ms": 25650,
              "end_ms": 25860,
              "pieces": [
                " Video",
                ","
              ]
            },
            {
              "text": " das",
              "start_ms": 25860,
              "end_ms": 25940,
              "pieces": [
                " das"
              ]
            },
            {
              "text": " Video,",
              "start_ms": 25950,
              "end_ms": 26160,
              "pieces": [
                " Video",
                ","
              ]
            },
            {
              "text": " das",
              "start_ms": 26160,
              "end_ms": 26240,
              "pieces": [
                " das"
              ]
            },
            {
              "text": " Video,",
              "start_ms": 26260,
              "end_ms": 26460,
              "pieces": [
                " Video",
                ","
              ]
            },
            {
              "text": " das",
              "start_ms": 26460,
              "end_ms": 26540,
              "pieces": [
                " das"
              ]
            },
            {
              "text": " Video,",
              "start_ms": 26550,
              "end_ms": 26750,
              "pieces": [
                " Video",
                ","
              ]
            },
            {
              "text": " das",
              "start_ms": 26750,
              "end_ms": 26830,
              "pieces": [
                " das"
              ]
            },
            {
              "text": " Video,",
              "start_ms": 26840,
              "end_ms": 27050,
              "pieces": [
                " Video",
                ","
              ]
            },
            {
              "text": " das",
              "start_ms": 27150,
              "end_ms": 27150,
              "pieces": [
                " das"
              ]
            },
            {
              "text": " Video,",
              "start_ms": 27160,
              "end_ms": 27350,
              "pieces": [
                " Video",
                ","
              ]
            },
            {
              "text": " das",
              "start_ms": 27360,
              "end_ms": 27400,
              "pieces": [
                " das"
              ]
            },
            {
              "text": " Video,",
              "start_ms": 27460,
              "end_ms": 27660,
              "pieces": [
                " Video",
                ","
              ]
            },
            {
              "text": " das",
              "start_ms": 27660,
              "end_ms": 27730,
              "pieces": [
                " das"
              ]
            },
            {
              "text": " Video,",
              "start_ms": 27740,
              "end_ms": 27950,
              "pieces": [
                " Video",
                ","
              ]
            },
            {
              "text": " das",
              "start_ms": 27950,
              "end_ms": 28050,
              "pieces": [
                " das"
              ]
            },
            {
              "text": " Video,",
              "start_ms": 28050,
              "end_ms": 28260,
              "pieces": [
                " Video",
                ","
              ]
            },
            {
              "text": " das",
              "start_ms": 28260,
              "end_ms": 28350,
              "pieces": [
                " das"
              ]
            },
            {
              "text": " Video,",
              "start_ms": 28350,
              "end_ms": 28560,
              "pieces": [
                " Video",
                ","
              ]
            },
            {
              "text": " das",
              "start_ms": 28560,
              "end_ms": 28650,
              "pieces": [
                " das"
              ]
            },
            {
              "text": " Video,",
              "start_ms": 28650,
              "end_ms": 28860,
              "pieces": [
                " Video",
                ","
              ]
            },
            {
              "text": " das",
              "start_ms": 28860,
              "end_ms": 28950,
              "pieces": [
                " das"
              ]
            },
            {
              "text": " Video,",
              "start_ms": 29080,
              "end_ms": 29160,
              "pieces": [
                " Video",
                ","
              ]
            },
            {
              "text": " das",
              "start_ms": 29160,
              "end_ms": 29250,
              "pieces": [
                " das"
              ]
            },
            {
              "text": " Video,",
              "start_ms": 29250,
              "end_ms": 29460,
              "pieces": [
                " Video",
                ","
              ]
            },
            {
              "text": " das",
              "start_ms": 29460,
              "end_ms": 29550,
              "pieces": [
                " das"
              ]
            },
            {
              "text": " Video,",
              "start_ms": 29550,
              "end_ms": 29760,
              "pieces": [
                " Video",
                ","
              ]
            },
            {
              "text": " das",
              "start_ms": 29760,
              "end_ms": 29990,
              "pieces": [
                " das"
              ]
            },
            {
              "text": " Video",
              "start_ms": 29990,
              "end_ms": 29990,
              "pieces": [
                " Video"
              ]
            }
          ],
          "problems": [
            "nonpositive word interval: ' das'",
            "nonpositive word interval: ' das'",
            "nonpositive word interval: ' das'",
            "nonpositive word interval: ' Video'"
          ],
          "dtw_points": [
            {
              "text": " Das",
              "point_cs": -1
            },
            {
              "text": " ist",
              "point_cs": -1
            },
            {
              "text": " das",
              "point_cs": -1
            },
            {
              "text": " Video",
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
              "text": " ist",
              "point_cs": -1
            },
            {
              "text": " das",
              "point_cs": -1
            },
            {
              "text": " Video",
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
              "text": " Video",
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
              "text": " Video",
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
              "text": " Video",
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
              "text": " Video",
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
              "text": " Video",
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
              "text": " Video",
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
              "text": " Video",
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
              "text": " Video",
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
              "text": " Video",
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
              "text": " Video",
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
              "text": " Video",
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
              "text": " Video",
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
              "text": " Video",
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
              "text": " Video",
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
              "text": " Video",
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
              "text": " Video",
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
              "text": " Video",
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
              "text": " Video",
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
              "text": " Video",
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
              "text": " Video",
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
              "text": " Video",
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
              "text": " Video",
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
              "text": " Video",
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
              "text": " Video",
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
              "text": " Video",
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
              "text": " Video",
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
              "text": " Video",
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
              "text": " Video",
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
              "text": " Video",
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
              "text": " Video",
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
              "text": " Video",
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
              "text": " Video",
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
              "text": " Video",
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
              "text": " Video",
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
              "text": " Video",
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
              "text": " Video",
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
              "text": " Video",
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
              "text": " Video",
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
              "text": " Video",
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
              "text": " Video",
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
              "text": " Video",
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
              "text": " Video",
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
              "text": " Video",
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
              "text": " Video",
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
              "text": " Video",
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
              "text": " Video",
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
              "text": " Video",
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
              "text": " Video",
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
              "text": " Video",
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
              "text": " Video",
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
              "text": " Video",
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
              "text": " Video",
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
              "text": " Video",
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
              "text": " Video",
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
              "text": " Video",
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
              "text": " Video",
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
              "text": " Video",
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
              "text": " Video",
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
              "text": " Video",
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
              "text": " Video",
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
              "text": " Video",
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
              "text": " Video",
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
              "text": " Video",
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
              "text": " Video",
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
              "text": " Video",
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
              "text": " Video",
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
              "text": " Video",
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
              "text": " Video",
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
              "text": " Video",
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
              "text": " Video",
              "point_cs": -1
            }
          ],
          "command": [
            "/tmp/atrain-whisper-a/.whisper-cli-unpatched",
            "-m",
            "/tmp/atrain-whisper-a/.ggml-tiny.bin",
            "-f",
            "/tmp/atrain-whisper-a-cpu-results/audio/german.wav",
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
            "/tmp/atrain-whisper-a-cpu-results/upstream-ordinary-no-vad-german"
          ],
          "wall_s": 1.9687344080011826,
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
            "/tmp/atrain-whisper-a/.ggml-tiny.bin",
            "-f",
            "/tmp/atrain-whisper-a-cpu-results/audio/japanese.wav",
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
            "/tmp/atrain-whisper-a-cpu-results/upstream-ordinary-no-vad-japanese"
          ],
          "wall_s": 0.6154485789884347,
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
            5320,
            4320,
            4330,
            4070,
            4070,
            3610,
            3610,
            2250,
            1260,
            900,
            720,
            310,
            670,
            0,
            300,
            340,
            370,
            240,
            240,
            90,
            90,
            40,
            40,
            0,
            0,
            0,
            0,
            200,
            0,
            10,
            10,
            0,
            0,
            100,
            110,
            10,
            10,
            60,
            60,
            50,
            40,
            30,
            40,
            60
          ],
          "max_boundary_error_ms": 5320,
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
          "status": "passed"
        },
        "boundary": {
          "tolerance_ms": 50,
          "matched_words": 21,
          "unmatched_reference_words": 1,
          "unmatched_candidate_words": 1,
          "boundary_errors_ms": [
            25320,
            9840,
            260,
            80,
            80,
            120,
            120,
            240,
            240,
            310,
            20,
            0,
            0,
            40,
            510,
            140,
            230,
            190,
            190,
            240,
            240,
            330,
            240,
            150,
            150,
            60,
            40,
            30,
            30,
            10,
            150,
            50,
            50,
            130,
            130,
            130,
            130,
            110,
            120,
            80,
            90,
            20
          ],
          "max_boundary_error_ms": 25320,
          "status": "failed"
        },
        "internal-first": {
          "tolerance_ms": 50,
          "matched_words": 22,
          "unmatched_reference_words": 0,
          "unmatched_candidate_words": 0,
          "boundary_errors_ms": [
            0,
            30,
            20,
            200,
            60,
            140,
            140,
            80,
            80,
            900,
            0,
            0,
            0,
            0,
            0,
            40,
            0,
            0,
            0,
            140,
            140,
            180,
            180,
            120,
            210,
            400,
            340,
            770,
            790,
            50,
            200,
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
            500
          ],
          "max_boundary_error_ms": 900,
          "status": "failed"
        },
        "internal-second": {
          "tolerance_ms": 50,
          "matched_words": 22,
          "unmatched_reference_words": 0,
          "unmatched_candidate_words": 0,
          "boundary_errors_ms": [
            320,
            320,
            330,
            740,
            740,
            950,
            950,
            1590,
            1260,
            900,
            0,
            0,
            0,
            10,
            760,
            230,
            20,
            270,
            320,
            200,
            210,
            150,
            260,
            230,
            140,
            20,
            20,
            500,
            410,
            330,
            240,
            280,
            270,
            290,
            130,
            180,
            160,
            120,
            60,
            40,
            0,
            160,
            150,
            500
          ],
          "max_boundary_error_ms": 1590,
          "status": "failed"
        }
      }
    },
    "upstream-ordinary-vad": {
      "fixtures": {
        "base": {
          "text": " And so my fellow Americans ask not what your country can do for you ask what you can do for your country.",
          "words": [
            {
              "text": " And",
              "start_ms": 40,
              "end_ms": 250,
              "pieces": [
                " And"
              ]
            },
            {
              "text": " so",
              "start_ms": 390,
              "end_ms": 470,
              "pieces": [
                " so"
              ]
            },
            {
              "text": " my",
              "start_ms": 470,
              "end_ms": 660,
              "pieces": [
                " my"
              ]
            },
            {
              "text": " fellow",
              "start_ms": 660,
              "end_ms": 1230,
              "pieces": [
                " fellow"
              ]
            },
            {
              "text": " Americans",
              "start_ms": 1230,
              "end_ms": 1810,
              "pieces": [
                " Americans"
              ]
            },
            {
              "text": " ask",
              "start_ms": 2140,
              "end_ms": 2500,
              "pieces": [
                " ask"
              ]
            },
            {
              "text": " not",
              "start_ms": 2830,
              "end_ms": 3100,
              "pieces": [
                " not"
              ]
            },
            {
              "text": " what",
              "start_ms": 3430,
              "end_ms": 3590,
              "pieces": [
                " what"
              ]
            },
            {
              "text": " your",
              "start_ms": 3680,
              "end_ms": 3850,
              "pieces": [
                " your"
              ]
            },
            {
              "text": " country",
              "start_ms": 3990,
              "end_ms": 4440,
              "pieces": [
                " country"
              ]
            },
            {
              "text": " can",
              "start_ms": 4520,
              "end_ms": 4700,
              "pieces": [
                " can"
              ]
            },
            {
              "text": " do",
              "start_ms": 4720,
              "end_ms": 4880,
              "pieces": [
                " do"
              ]
            },
            {
              "text": " for",
              "start_ms": 4880,
              "end_ms": 5270,
              "pieces": [
                " for"
              ]
            },
            {
              "text": " you",
              "start_ms": 5270,
              "end_ms": 5520,
              "pieces": [
                " you"
              ]
            },
            {
              "text": " ask",
              "start_ms": 5900,
              "end_ms": 6190,
              "pieces": [
                " ask"
              ]
            },
            {
              "text": " what",
              "start_ms": 6340,
              "end_ms": 6460,
              "pieces": [
                " what"
              ]
            },
            {
              "text": " you",
              "start_ms": 6620,
              "end_ms": 6760,
              "pieces": [
                " you"
              ]
            },
            {
              "text": " can",
              "start_ms": 6760,
              "end_ms": 7000,
              "pieces": [
                " can"
              ]
            },
            {
              "text": " do",
              "start_ms": 7000,
              "end_ms": 7220,
              "pieces": [
                " do"
              ]
            },
            {
              "text": " for",
              "start_ms": 7220,
              "end_ms": 7440,
              "pieces": [
                " for"
              ]
            },
            {
              "text": " your",
              "start_ms": 7440,
              "end_ms": 7680,
              "pieces": [
                " your"
              ]
            },
            {
              "text": " country.",
              "start_ms": 7680,
              "end_ms": 8200,
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
            "/tmp/atrain-whisper-a/.ggml-tiny.bin",
            "-f",
            "/tmp/atrain-whisper-a-cpu-results/audio/base.wav",
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
            "/tmp/atrain-whisper-a-cpu-results/upstream-ordinary-vad-base",
            "--vad",
            "-vm",
            "/tmp/atrain-whisper-a/.ggml-silero-v5.1.2.bin"
          ],
          "wall_s": 0.8159598030033521,
          "status": "passed"
        },
        "leading": {
          "text": " And so my fellow Americans ask not what your country can do for you ask what you can do for your country.",
          "words": [
            {
              "text": " And",
              "start_ms": 20,
              "end_ms": 220,
              "pieces": [
                " And"
              ]
            },
            {
              "text": " so",
              "start_ms": 370,
              "end_ms": 470,
              "pieces": [
                " so"
              ]
            },
            {
              "text": " my",
              "start_ms": 470,
              "end_ms": 660,
              "pieces": [
                " my"
              ]
            },
            {
              "text": " fellow",
              "start_ms": 660,
              "end_ms": 1230,
              "pieces": [
                " fellow"
              ]
            },
            {
              "text": " Americans",
              "start_ms": 1230,
              "end_ms": 1790,
              "pieces": [
                " Americans"
              ]
            },
            {
              "text": " ask",
              "start_ms": 2150,
              "end_ms": 2510,
              "pieces": [
                " ask"
              ]
            },
            {
              "text": " not",
              "start_ms": 2870,
              "end_ms": 3140,
              "pieces": [
                " not"
              ]
            },
            {
              "text": " what",
              "start_ms": 3480,
              "end_ms": 3600,
              "pieces": [
                " what"
              ]
            },
            {
              "text": " your",
              "start_ms": 3600,
              "end_ms": 3900,
              "pieces": [
                " your"
              ]
            },
            {
              "text": " country",
              "start_ms": 4040,
              "end_ms": 4480,
              "pieces": [
                " country"
              ]
            },
            {
              "text": " can",
              "start_ms": 4480,
              "end_ms": 4790,
              "pieces": [
                " can"
              ]
            },
            {
              "text": " do",
              "start_ms": 4790,
              "end_ms": 4990,
              "pieces": [
                " do"
              ]
            },
            {
              "text": " for",
              "start_ms": 5080,
              "end_ms": 5420,
              "pieces": [
                " for"
              ]
            },
            {
              "text": " you",
              "start_ms": 5420,
              "end_ms": 5590,
              "pieces": [
                " you"
              ]
            },
            {
              "text": " ask",
              "start_ms": 5980,
              "end_ms": 6270,
              "pieces": [
                " ask"
              ]
            },
            {
              "text": " what",
              "start_ms": 6430,
              "end_ms": 6540,
              "pieces": [
                " what"
              ]
            },
            {
              "text": " you",
              "start_ms": 6700,
              "end_ms": 6900,
              "pieces": [
                " you"
              ]
            },
            {
              "text": " can",
              "start_ms": 6900,
              "end_ms": 7160,
              "pieces": [
                " can"
              ]
            },
            {
              "text": " do",
              "start_ms": 7160,
              "end_ms": 7340,
              "pieces": [
                " do"
              ]
            },
            {
              "text": " for",
              "start_ms": 7340,
              "end_ms": 7520,
              "pieces": [
                " for"
              ]
            },
            {
              "text": " your",
              "start_ms": 7520,
              "end_ms": 7680,
              "pieces": [
                " your"
              ]
            },
            {
              "text": " country.",
              "start_ms": 7680,
              "end_ms": 8240,
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
            "/tmp/atrain-whisper-a/.ggml-tiny.bin",
            "-f",
            "/tmp/atrain-whisper-a-cpu-results/audio/leading.wav",
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
            "/tmp/atrain-whisper-a-cpu-results/upstream-ordinary-vad-leading",
            "--vad",
            "-vm",
            "/tmp/atrain-whisper-a/.ggml-silero-v5.1.2.bin"
          ],
          "wall_s": 0.7661870339943562,
          "status": "passed"
        },
        "trailing": {
          "text": " And so my fellow Americans ask not what your country can do for you ask what you can do for your country.",
          "words": [
            {
              "text": " And",
              "start_ms": 40,
              "end_ms": 250,
              "pieces": [
                " And"
              ]
            },
            {
              "text": " so",
              "start_ms": 390,
              "end_ms": 470,
              "pieces": [
                " so"
              ]
            },
            {
              "text": " my",
              "start_ms": 470,
              "end_ms": 660,
              "pieces": [
                " my"
              ]
            },
            {
              "text": " fellow",
              "start_ms": 660,
              "end_ms": 1230,
              "pieces": [
                " fellow"
              ]
            },
            {
              "text": " Americans",
              "start_ms": 1230,
              "end_ms": 1810,
              "pieces": [
                " Americans"
              ]
            },
            {
              "text": " ask",
              "start_ms": 2140,
              "end_ms": 2500,
              "pieces": [
                " ask"
              ]
            },
            {
              "text": " not",
              "start_ms": 2830,
              "end_ms": 3100,
              "pieces": [
                " not"
              ]
            },
            {
              "text": " what",
              "start_ms": 3430,
              "end_ms": 3590,
              "pieces": [
                " what"
              ]
            },
            {
              "text": " your",
              "start_ms": 3680,
              "end_ms": 3850,
              "pieces": [
                " your"
              ]
            },
            {
              "text": " country",
              "start_ms": 3990,
              "end_ms": 4440,
              "pieces": [
                " country"
              ]
            },
            {
              "text": " can",
              "start_ms": 4520,
              "end_ms": 4700,
              "pieces": [
                " can"
              ]
            },
            {
              "text": " do",
              "start_ms": 4720,
              "end_ms": 4880,
              "pieces": [
                " do"
              ]
            },
            {
              "text": " for",
              "start_ms": 4880,
              "end_ms": 5270,
              "pieces": [
                " for"
              ]
            },
            {
              "text": " you",
              "start_ms": 5270,
              "end_ms": 5520,
              "pieces": [
                " you"
              ]
            },
            {
              "text": " ask",
              "start_ms": 5900,
              "end_ms": 6190,
              "pieces": [
                " ask"
              ]
            },
            {
              "text": " what",
              "start_ms": 6340,
              "end_ms": 6460,
              "pieces": [
                " what"
              ]
            },
            {
              "text": " you",
              "start_ms": 6620,
              "end_ms": 6760,
              "pieces": [
                " you"
              ]
            },
            {
              "text": " can",
              "start_ms": 6760,
              "end_ms": 7000,
              "pieces": [
                " can"
              ]
            },
            {
              "text": " do",
              "start_ms": 7000,
              "end_ms": 7220,
              "pieces": [
                " do"
              ]
            },
            {
              "text": " for",
              "start_ms": 7220,
              "end_ms": 7440,
              "pieces": [
                " for"
              ]
            },
            {
              "text": " your",
              "start_ms": 7440,
              "end_ms": 7680,
              "pieces": [
                " your"
              ]
            },
            {
              "text": " country.",
              "start_ms": 7680,
              "end_ms": 8200,
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
            "/tmp/atrain-whisper-a/.ggml-tiny.bin",
            "-f",
            "/tmp/atrain-whisper-a-cpu-results/audio/trailing.wav",
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
            "/tmp/atrain-whisper-a-cpu-results/upstream-ordinary-vad-trailing",
            "--vad",
            "-vm",
            "/tmp/atrain-whisper-a/.ggml-silero-v5.1.2.bin"
          ],
          "wall_s": 0.8161494980013231,
          "status": "passed"
        },
        "internal": {
          "text": " And so my fellow Americans ask not what your country can do for you ask what you can do for your country. And so my fellow Americans ask not what your country can do for you ask what you can do for your country.",
          "words": [
            {
              "text": " And",
              "start_ms": 40,
              "end_ms": 250,
              "pieces": [
                " And"
              ]
            },
            {
              "text": " so",
              "start_ms": 390,
              "end_ms": 450,
              "pieces": [
                " so"
              ]
            },
            {
              "text": " my",
              "start_ms": 450,
              "end_ms": 630,
              "pieces": [
                " my"
              ]
            },
            {
              "text": " fellow",
              "start_ms": 630,
              "end_ms": 1180,
              "pieces": [
                " fellow"
              ]
            },
            {
              "text": " Americans",
              "start_ms": 1180,
              "end_ms": 1810,
              "pieces": [
                " Americans"
              ]
            },
            {
              "text": " ask",
              "start_ms": 2140,
              "end_ms": 2500,
              "pieces": [
                " ask"
              ]
            },
            {
              "text": " not",
              "start_ms": 2830,
              "end_ms": 3100,
              "pieces": [
                " not"
              ]
            },
            {
              "text": " what",
              "start_ms": 3430,
              "end_ms": 3590,
              "pieces": [
                " what"
              ]
            },
            {
              "text": " your",
              "start_ms": 3680,
              "end_ms": 3850,
              "pieces": [
                " your"
              ]
            },
            {
              "text": " country",
              "start_ms": 3990,
              "end_ms": 4440,
              "pieces": [
                " country"
              ]
            },
            {
              "text": " can",
              "start_ms": 4520,
              "end_ms": 4700,
              "pieces": [
                " can"
              ]
            },
            {
              "text": " do",
              "start_ms": 4720,
              "end_ms": 4880,
              "pieces": [
                " do"
              ]
            },
            {
              "text": " for",
              "start_ms": 4880,
              "end_ms": 5360,
              "pieces": [
                " for"
              ]
            },
            {
              "text": " you",
              "start_ms": 5360,
              "end_ms": 5540,
              "pieces": [
                " you"
              ]
            },
            {
              "text": " ask",
              "start_ms": 5900,
              "end_ms": 6180,
              "pieces": [
                " ask"
              ]
            },
            {
              "text": " what",
              "start_ms": 6340,
              "end_ms": 6460,
              "pieces": [
                " what"
              ]
            },
            {
              "text": " you",
              "start_ms": 6620,
              "end_ms": 6800,
              "pieces": [
                " you"
              ]
            },
            {
              "text": " can",
              "start_ms": 6800,
              "end_ms": 7000,
              "pieces": [
                " can"
              ]
            },
            {
              "text": " do",
              "start_ms": 7000,
              "end_ms": 7220,
              "pieces": [
                " do"
              ]
            },
            {
              "text": " for",
              "start_ms": 7220,
              "end_ms": 7440,
              "pieces": [
                " for"
              ]
            },
            {
              "text": " your",
              "start_ms": 7440,
              "end_ms": 7680,
              "pieces": [
                " your"
              ]
            },
            {
              "text": " country.",
              "start_ms": 7680,
              "end_ms": 8360,
              "pieces": [
                " country",
                "."
              ]
            },
            {
              "text": " And",
              "start_ms": 8410,
              "end_ms": 8600,
              "pieces": [
                " And"
              ]
            },
            {
              "text": " so",
              "start_ms": 8760,
              "end_ms": 8960,
              "pieces": [
                " so"
              ]
            },
            {
              "text": " my",
              "start_ms": 8960,
              "end_ms": 9200,
              "pieces": [
                " my"
              ]
            },
            {
              "text": " fellow",
              "start_ms": 9200,
              "end_ms": 9920,
              "pieces": [
                " fellow"
              ]
            },
            {
              "text": " Americans",
              "start_ms": 9920,
              "end_ms": 10860,
              "pieces": [
                " Americans"
              ]
            },
            {
              "text": " ask",
              "start_ms": 11210,
              "end_ms": 11370,
              "pieces": [
                " ask"
              ]
            },
            {
              "text": " not",
              "start_ms": 11370,
              "end_ms": 11460,
              "pieces": [
                " not"
              ]
            },
            {
              "text": " what",
              "start_ms": 11790,
              "end_ms": 12130,
              "pieces": [
                " what"
              ]
            },
            {
              "text": " your",
              "start_ms": 12130,
              "end_ms": 12470,
              "pieces": [
                " your"
              ]
            },
            {
              "text": " country",
              "start_ms": 12600,
              "end_ms": 13160,
              "pieces": [
                " country"
              ]
            },
            {
              "text": " can",
              "start_ms": 13160,
              "end_ms": 13440,
              "pieces": [
                " can"
              ]
            },
            {
              "text": " do",
              "start_ms": 13440,
              "end_ms": 13620,
              "pieces": [
                " do"
              ]
            },
            {
              "text": " for",
              "start_ms": 13620,
              "end_ms": 13870,
              "pieces": [
                " for"
              ]
            },
            {
              "text": " you",
              "start_ms": 13890,
              "end_ms": 14050,
              "pieces": [
                " you"
              ]
            },
            {
              "text": " ask",
              "start_ms": 14260,
              "end_ms": 14440,
              "pieces": [
                " ask"
              ]
            },
            {
              "text": " what",
              "start_ms": 14440,
              "end_ms": 14740,
              "pieces": [
                " what"
              ]
            },
            {
              "text": " you",
              "start_ms": 14740,
              "end_ms": 14820,
              "pieces": [
                " you"
              ]
            },
            {
              "text": " can",
              "start_ms": 14980,
              "end_ms": 15180,
              "pieces": [
                " can"
              ]
            },
            {
              "text": " do",
              "start_ms": 15180,
              "end_ms": 15330,
              "pieces": [
                " do"
              ]
            },
            {
              "text": " for",
              "start_ms": 15330,
              "end_ms": 15550,
              "pieces": [
                " for"
              ]
            },
            {
              "text": " your",
              "start_ms": 15550,
              "end_ms": 15850,
              "pieces": [
                " your"
              ]
            },
            {
              "text": " country.",
              "start_ms": 15850,
              "end_ms": 16640,
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
            "/tmp/atrain-whisper-a/.ggml-tiny.bin",
            "-f",
            "/tmp/atrain-whisper-a-cpu-results/audio/internal.wav",
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
            "/tmp/atrain-whisper-a-cpu-results/upstream-ordinary-vad-internal",
            "--vad",
            "-vm",
            "/tmp/atrain-whisper-a/.ggml-silero-v5.1.2.bin"
          ],
          "wall_s": 1.0163926999957766,
          "status": "passed"
        },
        "boundary": {
          "text": " And so my fellow Americans ask not what your country can do for you ask what you can do for your country.",
          "words": [
            {
              "text": " And",
              "start_ms": 20,
              "end_ms": 220,
              "pieces": [
                " And"
              ]
            },
            {
              "text": " so",
              "start_ms": 370,
              "end_ms": 450,
              "pieces": [
                " so"
              ]
            },
            {
              "text": " my",
              "start_ms": 450,
              "end_ms": 630,
              "pieces": [
                " my"
              ]
            },
            {
              "text": " fellow",
              "start_ms": 630,
              "end_ms": 1180,
              "pieces": [
                " fellow"
              ]
            },
            {
              "text": " Americans",
              "start_ms": 1180,
              "end_ms": 1790,
              "pieces": [
                " Americans"
              ]
            },
            {
              "text": " ask",
              "start_ms": 2090,
              "end_ms": 2450,
              "pieces": [
                " ask"
              ]
            },
            {
              "text": " not",
              "start_ms": 2850,
              "end_ms": 3120,
              "pieces": [
                " not"
              ]
            },
            {
              "text": " what",
              "start_ms": 3390,
              "end_ms": 3550,
              "pieces": [
                " what"
              ]
            },
            {
              "text": " your",
              "start_ms": 3630,
              "end_ms": 3810,
              "pieces": [
                " your"
              ]
            },
            {
              "text": " country",
              "start_ms": 3950,
              "end_ms": 4360,
              "pieces": [
                " country"
              ]
            },
            {
              "text": " can",
              "start_ms": 4360,
              "end_ms": 4630,
              "pieces": [
                " can"
              ]
            },
            {
              "text": " do",
              "start_ms": 4680,
              "end_ms": 4880,
              "pieces": [
                " do"
              ]
            },
            {
              "text": " for",
              "start_ms": 4990,
              "end_ms": 5270,
              "pieces": [
                " for"
              ]
            },
            {
              "text": " you",
              "start_ms": 5270,
              "end_ms": 5480,
              "pieces": [
                " you"
              ]
            },
            {
              "text": " ask",
              "start_ms": 5890,
              "end_ms": 6180,
              "pieces": [
                " ask"
              ]
            },
            {
              "text": " what",
              "start_ms": 6340,
              "end_ms": 6450,
              "pieces": [
                " what"
              ]
            },
            {
              "text": " you",
              "start_ms": 6610,
              "end_ms": 6760,
              "pieces": [
                " you"
              ]
            },
            {
              "text": " can",
              "start_ms": 6760,
              "end_ms": 7000,
              "pieces": [
                " can"
              ]
            },
            {
              "text": " do",
              "start_ms": 7000,
              "end_ms": 7220,
              "pieces": [
                " do"
              ]
            },
            {
              "text": " for",
              "start_ms": 7220,
              "end_ms": 7440,
              "pieces": [
                " for"
              ]
            },
            {
              "text": " your",
              "start_ms": 7440,
              "end_ms": 7680,
              "pieces": [
                " your"
              ]
            },
            {
              "text": " country.",
              "start_ms": 7680,
              "end_ms": 8200,
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
            "/tmp/atrain-whisper-a/.ggml-tiny.bin",
            "-f",
            "/tmp/atrain-whisper-a-cpu-results/audio/boundary.wav",
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
            "/tmp/atrain-whisper-a-cpu-results/upstream-ordinary-vad-boundary",
            "--vad",
            "-vm",
            "/tmp/atrain-whisper-a/.ggml-silero-v5.1.2.bin"
          ],
          "wall_s": 0.8161275619931985,
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
            "/tmp/atrain-whisper-a/.ggml-tiny.bin",
            "-f",
            "/tmp/atrain-whisper-a-cpu-results/audio/silence.wav",
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
            "/tmp/atrain-whisper-a-cpu-results/upstream-ordinary-vad-silence",
            "--vad",
            "-vm",
            "/tmp/atrain-whisper-a/.ggml-silero-v5.1.2.bin"
          ],
          "wall_s": 0.6153690159990219,
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
            "/tmp/atrain-whisper-a/.ggml-tiny.bin",
            "-f",
            "/tmp/atrain-whisper-a-cpu-results/audio/noise.wav",
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
            "/tmp/atrain-whisper-a-cpu-results/upstream-ordinary-vad-noise",
            "--vad",
            "-vm",
            "/tmp/atrain-whisper-a/.ggml-silero-v5.1.2.bin"
          ],
          "wall_s": 0.1644257130101323,
          "status": "passed"
        },
        "german": {
          "text": "",
          "words": [],
          "problems": [
            "speech fixture returned no timed words"
          ],
          "dtw_points": [],
          "command": [
            "/tmp/atrain-whisper-a/.whisper-cli-unpatched",
            "-m",
            "/tmp/atrain-whisper-a/.ggml-tiny.bin",
            "-f",
            "/tmp/atrain-whisper-a-cpu-results/audio/german.wav",
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
            "/tmp/atrain-whisper-a-cpu-results/upstream-ordinary-vad-german",
            "--vad",
            "-vm",
            "/tmp/atrain-whisper-a/.ggml-silero-v5.1.2.bin"
          ],
          "wall_s": 0.16464515999541618,
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
            "/tmp/atrain-whisper-a/.ggml-tiny.bin",
            "-f",
            "/tmp/atrain-whisper-a-cpu-results/audio/japanese.wav",
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
            "/tmp/atrain-whisper-a-cpu-results/upstream-ordinary-vad-japanese",
            "--vad",
            "-vm",
            "/tmp/atrain-whisper-a/.ggml-silero-v5.1.2.bin"
          ],
          "wall_s": 0.6161057650024304,
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
            5030,
            5020,
            5000,
            5000,
            5000,
            5000,
            5000,
            5000,
            5020,
            4990,
            4990,
            4960,
            4960,
            4950,
            4990,
            5080,
            4950,
            4950,
            4960,
            5040,
            4910,
            4930,
            4890,
            4800,
            4850,
            4850,
            4930,
            4920,
            4920,
            4910,
            4920,
            4920,
            4860,
            4860,
            4840,
            4840,
            4880,
            4880,
            4920,
            4920,
            5000,
            5000,
            4960
          ],
          "max_boundary_error_ms": 5080,
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
          "status": "passed"
        },
        "boundary": {
          "tolerance_ms": 50,
          "matched_words": 22,
          "unmatched_reference_words": 0,
          "unmatched_candidate_words": 0,
          "boundary_errors_ms": [
            25020,
            25030,
            25020,
            25020,
            25020,
            25030,
            25030,
            25050,
            25050,
            25020,
            25050,
            25050,
            24980,
            24980,
            25040,
            25040,
            25050,
            25040,
            25040,
            25080,
            25160,
            25070,
            25040,
            25000,
            24890,
            25000,
            25000,
            25040,
            25010,
            25010,
            25000,
            25010,
            25010,
            25000,
            25000,
            25000,
            25000,
            25000,
            25000,
            25000,
            25000,
            25000,
            25000,
            25000
          ],
          "max_boundary_error_ms": 25160,
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
            20,
            20,
            30,
            30,
            50,
            50,
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
            90,
            90,
            20,
            0,
            10,
            0,
            0,
            0,
            40,
            40,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            160
          ],
          "max_boundary_error_ms": 160,
          "status": "failed"
        },
        "internal-second": {
          "tolerance_ms": 50,
          "matched_words": 0,
          "unmatched_reference_words": 22,
          "unmatched_candidate_words": 0,
          "boundary_errors_ms": [],
          "max_boundary_error_ms": null,
          "status": "failed"
        }
      }
    },
    "patched-ordinary-vad": {
      "fixtures": {
        "base": {
          "text": " And so my fellow Americans ask not what your country can do for you ask what you can do for your country.",
          "words": [
            {
              "text": " And",
              "start_ms": 330,
              "end_ms": 540,
              "pieces": [
                " And"
              ]
            },
            {
              "text": " so",
              "start_ms": 680,
              "end_ms": 760,
              "pieces": [
                " so"
              ]
            },
            {
              "text": " my",
              "start_ms": 760,
              "end_ms": 950,
              "pieces": [
                " my"
              ]
            },
            {
              "text": " fellow",
              "start_ms": 950,
              "end_ms": 1520,
              "pieces": [
                " fellow"
              ]
            },
            {
              "text": " Americans",
              "start_ms": 1520,
              "end_ms": 2100,
              "pieces": [
                " Americans"
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
              "end_ms": 4280,
              "pieces": [
                " not"
              ]
            },
            {
              "text": " what",
              "start_ms": 5410,
              "end_ms": 5570,
              "pieces": [
                " what"
              ]
            },
            {
              "text": " your",
              "start_ms": 5660,
              "end_ms": 5830,
              "pieces": [
                " your"
              ]
            },
            {
              "text": " country",
              "start_ms": 5970,
              "end_ms": 6420,
              "pieces": [
                " country"
              ]
            },
            {
              "text": " can",
              "start_ms": 6500,
              "end_ms": 6680,
              "pieces": [
                " can"
              ]
            },
            {
              "text": " do",
              "start_ms": 6700,
              "end_ms": 6860,
              "pieces": [
                " do"
              ]
            },
            {
              "text": " for",
              "start_ms": 6860,
              "end_ms": 7250,
              "pieces": [
                " for"
              ]
            },
            {
              "text": " you",
              "start_ms": 7250,
              "end_ms": 7500,
              "pieces": [
                " you"
              ]
            },
            {
              "text": " ask",
              "start_ms": 8190,
              "end_ms": 8480,
              "pieces": [
                " ask"
              ]
            },
            {
              "text": " what",
              "start_ms": 8630,
              "end_ms": 8750,
              "pieces": [
                " what"
              ]
            },
            {
              "text": " you",
              "start_ms": 8910,
              "end_ms": 9050,
              "pieces": [
                " you"
              ]
            },
            {
              "text": " can",
              "start_ms": 9050,
              "end_ms": 9290,
              "pieces": [
                " can"
              ]
            },
            {
              "text": " do",
              "start_ms": 9290,
              "end_ms": 9510,
              "pieces": [
                " do"
              ]
            },
            {
              "text": " for",
              "start_ms": 9510,
              "end_ms": 9730,
              "pieces": [
                " for"
              ]
            },
            {
              "text": " your",
              "start_ms": 9730,
              "end_ms": 9970,
              "pieces": [
                " your"
              ]
            },
            {
              "text": " country.",
              "start_ms": 9970,
              "end_ms": 10490,
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
            "/tmp/atrain-whisper-a/.ggml-tiny.bin",
            "-f",
            "/tmp/atrain-whisper-a-cpu-results/audio/base.wav",
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
            "/tmp/atrain-whisper-a-cpu-results/patched-ordinary-vad-base",
            "--vad",
            "-vm",
            "/tmp/atrain-whisper-a/.ggml-silero-v5.1.2.bin"
          ],
          "wall_s": 0.7659153139975388,
          "status": "passed"
        },
        "leading": {
          "text": " And so my fellow Americans ask not what your country can do for you ask what you can do for your country.",
          "words": [
            {
              "text": " And",
              "start_ms": 5330,
              "end_ms": 5530,
              "pieces": [
                " And"
              ]
            },
            {
              "text": " so",
              "start_ms": 5680,
              "end_ms": 5780,
              "pieces": [
                " so"
              ]
            },
            {
              "text": " my",
              "start_ms": 5780,
              "end_ms": 5970,
              "pieces": [
                " my"
              ]
            },
            {
              "text": " fellow",
              "start_ms": 5970,
              "end_ms": 6540,
              "pieces": [
                " fellow"
              ]
            },
            {
              "text": " Americans",
              "start_ms": 6540,
              "end_ms": 7100,
              "pieces": [
                " Americans"
              ]
            },
            {
              "text": " ask",
              "start_ms": 8290,
              "end_ms": 8650,
              "pieces": [
                " ask"
              ]
            },
            {
              "text": " not",
              "start_ms": 9010,
              "end_ms": 9280,
              "pieces": [
                " not"
              ]
            },
            {
              "text": " what",
              "start_ms": 10410,
              "end_ms": 10530,
              "pieces": [
                " what"
              ]
            },
            {
              "text": " your",
              "start_ms": 10530,
              "end_ms": 10830,
              "pieces": [
                " your"
              ]
            },
            {
              "text": " country",
              "start_ms": 10970,
              "end_ms": 11410,
              "pieces": [
                " country"
              ]
            },
            {
              "text": " can",
              "start_ms": 11410,
              "end_ms": 11720,
              "pieces": [
                " can"
              ]
            },
            {
              "text": " do",
              "start_ms": 11720,
              "end_ms": 11920,
              "pieces": [
                " do"
              ]
            },
            {
              "text": " for",
              "start_ms": 12010,
              "end_ms": 12350,
              "pieces": [
                " for"
              ]
            },
            {
              "text": " you",
              "start_ms": 12350,
              "end_ms": 12520,
              "pieces": [
                " you"
              ]
            },
            {
              "text": " ask",
              "start_ms": 13190,
              "end_ms": 13480,
              "pieces": [
                " ask"
              ]
            },
            {
              "text": " what",
              "start_ms": 13640,
              "end_ms": 13750,
              "pieces": [
                " what"
              ]
            },
            {
              "text": " you",
              "start_ms": 13910,
              "end_ms": 14110,
              "pieces": [
                " you"
              ]
            },
            {
              "text": " can",
              "start_ms": 14110,
              "end_ms": 14370,
              "pieces": [
                " can"
              ]
            },
            {
              "text": " do",
              "start_ms": 14370,
              "end_ms": 14550,
              "pieces": [
                " do"
              ]
            },
            {
              "text": " for",
              "start_ms": 14550,
              "end_ms": 14730,
              "pieces": [
                " for"
              ]
            },
            {
              "text": " your",
              "start_ms": 14730,
              "end_ms": 14890,
              "pieces": [
                " your"
              ]
            },
            {
              "text": " country.",
              "start_ms": 14890,
              "end_ms": 15450,
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
            "/tmp/atrain-whisper-a/.ggml-tiny.bin",
            "-f",
            "/tmp/atrain-whisper-a-cpu-results/audio/leading.wav",
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
            "/tmp/atrain-whisper-a-cpu-results/patched-ordinary-vad-leading",
            "--vad",
            "-vm",
            "/tmp/atrain-whisper-a/.ggml-silero-v5.1.2.bin"
          ],
          "wall_s": 0.7664251109963516,
          "status": "passed"
        },
        "trailing": {
          "text": " And so my fellow Americans ask not what your country can do for you ask what you can do for your country.",
          "words": [
            {
              "text": " And",
              "start_ms": 330,
              "end_ms": 540,
              "pieces": [
                " And"
              ]
            },
            {
              "text": " so",
              "start_ms": 680,
              "end_ms": 760,
              "pieces": [
                " so"
              ]
            },
            {
              "text": " my",
              "start_ms": 760,
              "end_ms": 950,
              "pieces": [
                " my"
              ]
            },
            {
              "text": " fellow",
              "start_ms": 950,
              "end_ms": 1520,
              "pieces": [
                " fellow"
              ]
            },
            {
              "text": " Americans",
              "start_ms": 1520,
              "end_ms": 2100,
              "pieces": [
                " Americans"
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
              "end_ms": 4280,
              "pieces": [
                " not"
              ]
            },
            {
              "text": " what",
              "start_ms": 5410,
              "end_ms": 5570,
              "pieces": [
                " what"
              ]
            },
            {
              "text": " your",
              "start_ms": 5660,
              "end_ms": 5830,
              "pieces": [
                " your"
              ]
            },
            {
              "text": " country",
              "start_ms": 5970,
              "end_ms": 6420,
              "pieces": [
                " country"
              ]
            },
            {
              "text": " can",
              "start_ms": 6500,
              "end_ms": 6680,
              "pieces": [
                " can"
              ]
            },
            {
              "text": " do",
              "start_ms": 6700,
              "end_ms": 6860,
              "pieces": [
                " do"
              ]
            },
            {
              "text": " for",
              "start_ms": 6860,
              "end_ms": 7250,
              "pieces": [
                " for"
              ]
            },
            {
              "text": " you",
              "start_ms": 7250,
              "end_ms": 7500,
              "pieces": [
                " you"
              ]
            },
            {
              "text": " ask",
              "start_ms": 8190,
              "end_ms": 8480,
              "pieces": [
                " ask"
              ]
            },
            {
              "text": " what",
              "start_ms": 8630,
              "end_ms": 8750,
              "pieces": [
                " what"
              ]
            },
            {
              "text": " you",
              "start_ms": 8910,
              "end_ms": 9050,
              "pieces": [
                " you"
              ]
            },
            {
              "text": " can",
              "start_ms": 9050,
              "end_ms": 9290,
              "pieces": [
                " can"
              ]
            },
            {
              "text": " do",
              "start_ms": 9290,
              "end_ms": 9510,
              "pieces": [
                " do"
              ]
            },
            {
              "text": " for",
              "start_ms": 9510,
              "end_ms": 9730,
              "pieces": [
                " for"
              ]
            },
            {
              "text": " your",
              "start_ms": 9730,
              "end_ms": 9970,
              "pieces": [
                " your"
              ]
            },
            {
              "text": " country.",
              "start_ms": 9970,
              "end_ms": 10490,
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
            "/tmp/atrain-whisper-a/.ggml-tiny.bin",
            "-f",
            "/tmp/atrain-whisper-a-cpu-results/audio/trailing.wav",
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
            "/tmp/atrain-whisper-a-cpu-results/patched-ordinary-vad-trailing",
            "--vad",
            "-vm",
            "/tmp/atrain-whisper-a/.ggml-silero-v5.1.2.bin"
          ],
          "wall_s": 0.76620109299256,
          "status": "passed"
        },
        "internal": {
          "text": " And so my fellow Americans ask not what your country can do for you ask what you can do for your country. And so my fellow Americans ask not what your country can do for you ask what you can do for your country.",
          "words": [
            {
              "text": " And",
              "start_ms": 330,
              "end_ms": 540,
              "pieces": [
                " And"
              ]
            },
            {
              "text": " so",
              "start_ms": 680,
              "end_ms": 740,
              "pieces": [
                " so"
              ]
            },
            {
              "text": " my",
              "start_ms": 740,
              "end_ms": 920,
              "pieces": [
                " my"
              ]
            },
            {
              "text": " fellow",
              "start_ms": 920,
              "end_ms": 1470,
              "pieces": [
                " fellow"
              ]
            },
            {
              "text": " Americans",
              "start_ms": 1470,
              "end_ms": 2100,
              "pieces": [
                " Americans"
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
              "end_ms": 4280,
              "pieces": [
                " not"
              ]
            },
            {
              "text": " what",
              "start_ms": 5410,
              "end_ms": 5570,
              "pieces": [
                " what"
              ]
            },
            {
              "text": " your",
              "start_ms": 5660,
              "end_ms": 5830,
              "pieces": [
                " your"
              ]
            },
            {
              "text": " country",
              "start_ms": 5970,
              "end_ms": 6420,
              "pieces": [
                " country"
              ]
            },
            {
              "text": " can",
              "start_ms": 6500,
              "end_ms": 6680,
              "pieces": [
                " can"
              ]
            },
            {
              "text": " do",
              "start_ms": 6700,
              "end_ms": 6860,
              "pieces": [
                " do"
              ]
            },
            {
              "text": " for",
              "start_ms": 6860,
              "end_ms": 7340,
              "pieces": [
                " for"
              ]
            },
            {
              "text": " you",
              "start_ms": 7340,
              "end_ms": 7520,
              "pieces": [
                " you"
              ]
            },
            {
              "text": " ask",
              "start_ms": 8190,
              "end_ms": 8470,
              "pieces": [
                " ask"
              ]
            },
            {
              "text": " what",
              "start_ms": 8630,
              "end_ms": 8750,
              "pieces": [
                " what"
              ]
            },
            {
              "text": " you",
              "start_ms": 8910,
              "end_ms": 9090,
              "pieces": [
                " you"
              ]
            },
            {
              "text": " can",
              "start_ms": 9090,
              "end_ms": 9290,
              "pieces": [
                " can"
              ]
            },
            {
              "text": " do",
              "start_ms": 9290,
              "end_ms": 9510,
              "pieces": [
                " do"
              ]
            },
            {
              "text": " for",
              "start_ms": 9510,
              "end_ms": 9730,
              "pieces": [
                " for"
              ]
            },
            {
              "text": " your",
              "start_ms": 9730,
              "end_ms": 9970,
              "pieces": [
                " your"
              ]
            },
            {
              "text": " country.",
              "start_ms": 9970,
              "end_ms": 10600,
              "pieces": [
                " country",
                "."
              ]
            },
            {
              "text": " And",
              "start_ms": 16350,
              "end_ms": 16450,
              "pieces": [
                " And"
              ]
            },
            {
              "text": " so",
              "start_ms": 16610,
              "end_ms": 16810,
              "pieces": [
                " so"
              ]
            },
            {
              "text": " my",
              "start_ms": 16810,
              "end_ms": 17050,
              "pieces": [
                " my"
              ]
            },
            {
              "text": " fellow",
              "start_ms": 17050,
              "end_ms": 17770,
              "pieces": [
                " fellow"
              ]
            },
            {
              "text": " Americans",
              "start_ms": 17770,
              "end_ms": 19610,
              "pieces": [
                " Americans"
              ]
            },
            {
              "text": " ask",
              "start_ms": 19970,
              "end_ms": 20120,
              "pieces": [
                " ask"
              ]
            },
            {
              "text": " not",
              "start_ms": 20120,
              "end_ms": 20210,
              "pieces": [
                " not"
              ]
            },
            {
              "text": " what",
              "start_ms": 21380,
              "end_ms": 21680,
              "pieces": [
                " what"
              ]
            },
            {
              "text": " your",
              "start_ms": 21680,
              "end_ms": 22020,
              "pieces": [
                " your"
              ]
            },
            {
              "text": " country",
              "start_ms": 22150,
              "end_ms": 22710,
              "pieces": [
                " country"
              ]
            },
            {
              "text": " can",
              "start_ms": 22710,
              "end_ms": 22990,
              "pieces": [
                " can"
              ]
            },
            {
              "text": " do",
              "start_ms": 22990,
              "end_ms": 23170,
              "pieces": [
                " do"
              ]
            },
            {
              "text": " for",
              "start_ms": 23170,
              "end_ms": 23420,
              "pieces": [
                " for"
              ]
            },
            {
              "text": " you",
              "start_ms": 23440,
              "end_ms": 23600,
              "pieces": [
                " you"
              ]
            },
            {
              "text": " ask",
              "start_ms": 24160,
              "end_ms": 24300,
              "pieces": [
                " ask"
              ]
            },
            {
              "text": " what",
              "start_ms": 24300,
              "end_ms": 24600,
              "pieces": [
                " what"
              ]
            },
            {
              "text": " you",
              "start_ms": 24600,
              "end_ms": 24680,
              "pieces": [
                " you"
              ]
            },
            {
              "text": " can",
              "start_ms": 24840,
              "end_ms": 25040,
              "pieces": [
                " can"
              ]
            },
            {
              "text": " do",
              "start_ms": 25040,
              "end_ms": 25190,
              "pieces": [
                " do"
              ]
            },
            {
              "text": " for",
              "start_ms": 25190,
              "end_ms": 25410,
              "pieces": [
                " for"
              ]
            },
            {
              "text": " your",
              "start_ms": 25410,
              "end_ms": 25710,
              "pieces": [
                " your"
              ]
            },
            {
              "text": " country.",
              "start_ms": 25710,
              "end_ms": 26500,
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
            "/tmp/atrain-whisper-a/.ggml-tiny.bin",
            "-f",
            "/tmp/atrain-whisper-a-cpu-results/audio/internal.wav",
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
            "/tmp/atrain-whisper-a-cpu-results/patched-ordinary-vad-internal",
            "--vad",
            "-vm",
            "/tmp/atrain-whisper-a/.ggml-silero-v5.1.2.bin"
          ],
          "wall_s": 0.9664142730034655,
          "status": "passed"
        },
        "boundary": {
          "text": " And so my fellow Americans ask not what your country can do for you ask what you can do for your country.",
          "words": [
            {
              "text": " And",
              "start_ms": 25330,
              "end_ms": 25530,
              "pieces": [
                " And"
              ]
            },
            {
              "text": " so",
              "start_ms": 25680,
              "end_ms": 25760,
              "pieces": [
                " so"
              ]
            },
            {
              "text": " my",
              "start_ms": 25760,
              "end_ms": 25940,
              "pieces": [
                " my"
              ]
            },
            {
              "text": " fellow",
              "start_ms": 25940,
              "end_ms": 26490,
              "pieces": [
                " fellow"
              ]
            },
            {
              "text": " Americans",
              "start_ms": 26490,
              "end_ms": 27100,
              "pieces": [
                " Americans"
              ]
            },
            {
              "text": " ask",
              "start_ms": 28290,
              "end_ms": 28650,
              "pieces": [
                " ask"
              ]
            },
            {
              "text": " not",
              "start_ms": 29010,
              "end_ms": 29280,
              "pieces": [
                " not"
              ]
            },
            {
              "text": " what",
              "start_ms": 30410,
              "end_ms": 30570,
              "pieces": [
                " what"
              ]
            },
            {
              "text": " your",
              "start_ms": 30650,
              "end_ms": 30830,
              "pieces": [
                " your"
              ]
            },
            {
              "text": " country",
              "start_ms": 30970,
              "end_ms": 31380,
              "pieces": [
                " country"
              ]
            },
            {
              "text": " can",
              "start_ms": 31380,
              "end_ms": 31650,
              "pieces": [
                " can"
              ]
            },
            {
              "text": " do",
              "start_ms": 31700,
              "end_ms": 31900,
              "pieces": [
                " do"
              ]
            },
            {
              "text": " for",
              "start_ms": 32010,
              "end_ms": 32290,
              "pieces": [
                " for"
              ]
            },
            {
              "text": " you",
              "start_ms": 32290,
              "end_ms": 32500,
              "pieces": [
                " you"
              ]
            },
            {
              "text": " ask",
              "start_ms": 33190,
              "end_ms": 33480,
              "pieces": [
                " ask"
              ]
            },
            {
              "text": " what",
              "start_ms": 33640,
              "end_ms": 33750,
              "pieces": [
                " what"
              ]
            },
            {
              "text": " you",
              "start_ms": 33910,
              "end_ms": 34060,
              "pieces": [
                " you"
              ]
            },
            {
              "text": " can",
              "start_ms": 34060,
              "end_ms": 34300,
              "pieces": [
                " can"
              ]
            },
            {
              "text": " do",
              "start_ms": 34300,
              "end_ms": 34520,
              "pieces": [
                " do"
              ]
            },
            {
              "text": " for",
              "start_ms": 34520,
              "end_ms": 34740,
              "pieces": [
                " for"
              ]
            },
            {
              "text": " your",
              "start_ms": 34740,
              "end_ms": 34980,
              "pieces": [
                " your"
              ]
            },
            {
              "text": " country.",
              "start_ms": 34980,
              "end_ms": 35500,
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
            "/tmp/atrain-whisper-a/.ggml-tiny.bin",
            "-f",
            "/tmp/atrain-whisper-a-cpu-results/audio/boundary.wav",
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
            "/tmp/atrain-whisper-a-cpu-results/patched-ordinary-vad-boundary",
            "--vad",
            "-vm",
            "/tmp/atrain-whisper-a/.ggml-silero-v5.1.2.bin"
          ],
          "wall_s": 0.8159452479885658,
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
            "/tmp/atrain-whisper-a/.ggml-tiny.bin",
            "-f",
            "/tmp/atrain-whisper-a-cpu-results/audio/silence.wav",
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
            "/tmp/atrain-whisper-a-cpu-results/patched-ordinary-vad-silence",
            "--vad",
            "-vm",
            "/tmp/atrain-whisper-a/.ggml-silero-v5.1.2.bin"
          ],
          "wall_s": 0.1645526620122837,
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
            "/tmp/atrain-whisper-a/.ggml-tiny.bin",
            "-f",
            "/tmp/atrain-whisper-a-cpu-results/audio/noise.wav",
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
            "/tmp/atrain-whisper-a-cpu-results/patched-ordinary-vad-noise",
            "--vad",
            "-vm",
            "/tmp/atrain-whisper-a/.ggml-silero-v5.1.2.bin"
          ],
          "wall_s": 0.16453907499089837,
          "status": "passed"
        },
        "german": {
          "text": "",
          "words": [],
          "problems": [
            "speech fixture returned no timed words"
          ],
          "dtw_points": [],
          "command": [
            "/tmp/atrain-whisper-a/.whisper-cli-patched",
            "-m",
            "/tmp/atrain-whisper-a/.ggml-tiny.bin",
            "-f",
            "/tmp/atrain-whisper-a-cpu-results/audio/german.wav",
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
            "/tmp/atrain-whisper-a-cpu-results/patched-ordinary-vad-german",
            "--vad",
            "-vm",
            "/tmp/atrain-whisper-a/.ggml-silero-v5.1.2.bin"
          ],
          "wall_s": 0.16438599400862586,
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
            "/tmp/atrain-whisper-a/.ggml-tiny.bin",
            "-f",
            "/tmp/atrain-whisper-a-cpu-results/audio/japanese.wav",
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
            "/tmp/atrain-whisper-a-cpu-results/patched-ordinary-vad-japanese",
            "--vad",
            "-vm",
            "/tmp/atrain-whisper-a/.ggml-silero-v5.1.2.bin"
          ],
          "wall_s": 0.6154936499951873,
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
            10,
            0,
            20,
            20,
            20,
            20,
            20,
            20,
            0,
            0,
            0,
            0,
            0,
            0,
            40,
            130,
            0,
            0,
            10,
            90,
            40,
            20,
            60,
            150,
            100,
            100,
            20,
            0,
            0,
            10,
            0,
            0,
            60,
            60,
            80,
            80,
            40,
            40,
            0,
            0,
            80,
            80,
            40
          ],
          "max_boundary_error_ms": 150,
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
            0,
            0,
            10,
            10,
            30,
            30,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            10,
            0,
            0,
            40,
            120,
            30,
            0,
            40,
            150,
            40,
            40,
            0,
            0,
            0,
            10,
            0,
            0,
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
            10
          ],
          "max_boundary_error_ms": 150,
          "status": "failed"
        },
        "internal-first": {
          "tolerance_ms": 50,
          "matched_words": 22,
          "unmatched_reference_words": 0,
          "unmatched_candidate_words": 0,
          "boundary_errors_ms": [
            0,
            0,
            0,
            20,
            20,
            30,
            30,
            50,
            50,
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
            90,
            90,
            20,
            0,
            10,
            0,
            0,
            0,
            40,
            40,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            110
          ],
          "max_boundary_error_ms": 110,
          "status": "failed"
        },
        "internal-second": {
          "tolerance_ms": 50,
          "matched_words": 22,
          "unmatched_reference_words": 0,
          "unmatched_candidate_words": 0,
          "boundary_errors_ms": [
            20,
            90,
            70,
            50,
            50,
            100,
            100,
            250,
            250,
            1510,
            680,
            470,
            110,
            70,
            30,
            110,
            20,
            190,
            180,
            290,
            210,
            310,
            290,
            310,
            310,
            170,
            190,
            100,
            30,
            180,
            330,
            150,
            310,
            370,
            210,
            250,
            250,
            320,
            320,
            320,
            320,
            260,
            260,
            10
          ],
          "max_boundary_error_ms": 1510,
          "status": "failed"
        }
      }
    },
    "upstream-dtw-vad": {
      "fixtures": {
        "base": {
          "text": " And so my fellow Americans ask not what your country can do for you ask what you can do for your country.",
          "words": [
            {
              "text": " And",
              "start_ms": 40,
              "end_ms": 250,
              "pieces": [
                " And"
              ]
            },
            {
              "text": " so",
              "start_ms": 390,
              "end_ms": 470,
              "pieces": [
                " so"
              ]
            },
            {
              "text": " my",
              "start_ms": 470,
              "end_ms": 660,
              "pieces": [
                " my"
              ]
            },
            {
              "text": " fellow",
              "start_ms": 660,
              "end_ms": 1230,
              "pieces": [
                " fellow"
              ]
            },
            {
              "text": " Americans",
              "start_ms": 1230,
              "end_ms": 1810,
              "pieces": [
                " Americans"
              ]
            },
            {
              "text": " ask",
              "start_ms": 2140,
              "end_ms": 2500,
              "pieces": [
                " ask"
              ]
            },
            {
              "text": " not",
              "start_ms": 2830,
              "end_ms": 3100,
              "pieces": [
                " not"
              ]
            },
            {
              "text": " what",
              "start_ms": 3430,
              "end_ms": 3590,
              "pieces": [
                " what"
              ]
            },
            {
              "text": " your",
              "start_ms": 3680,
              "end_ms": 3850,
              "pieces": [
                " your"
              ]
            },
            {
              "text": " country",
              "start_ms": 3990,
              "end_ms": 4440,
              "pieces": [
                " country"
              ]
            },
            {
              "text": " can",
              "start_ms": 4520,
              "end_ms": 4700,
              "pieces": [
                " can"
              ]
            },
            {
              "text": " do",
              "start_ms": 4720,
              "end_ms": 4880,
              "pieces": [
                " do"
              ]
            },
            {
              "text": " for",
              "start_ms": 4880,
              "end_ms": 5270,
              "pieces": [
                " for"
              ]
            },
            {
              "text": " you",
              "start_ms": 5270,
              "end_ms": 5520,
              "pieces": [
                " you"
              ]
            },
            {
              "text": " ask",
              "start_ms": 5900,
              "end_ms": 6190,
              "pieces": [
                " ask"
              ]
            },
            {
              "text": " what",
              "start_ms": 6340,
              "end_ms": 6460,
              "pieces": [
                " what"
              ]
            },
            {
              "text": " you",
              "start_ms": 6620,
              "end_ms": 6760,
              "pieces": [
                " you"
              ]
            },
            {
              "text": " can",
              "start_ms": 6760,
              "end_ms": 7000,
              "pieces": [
                " can"
              ]
            },
            {
              "text": " do",
              "start_ms": 7000,
              "end_ms": 7220,
              "pieces": [
                " do"
              ]
            },
            {
              "text": " for",
              "start_ms": 7220,
              "end_ms": 7440,
              "pieces": [
                " for"
              ]
            },
            {
              "text": " your",
              "start_ms": 7440,
              "end_ms": 7680,
              "pieces": [
                " your"
              ]
            },
            {
              "text": " country.",
              "start_ms": 7680,
              "end_ms": 8200,
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
              "point_cs": 18
            },
            {
              "text": " so",
              "point_cs": 76
            },
            {
              "text": " my",
              "point_cs": 104
            },
            {
              "text": " fellow",
              "point_cs": 138
            },
            {
              "text": " Americans",
              "point_cs": 192
            },
            {
              "text": " ask",
              "point_cs": 264
            },
            {
              "text": " not",
              "point_cs": 320
            },
            {
              "text": " what",
              "point_cs": 372
            },
            {
              "text": " your",
              "point_cs": 400
            },
            {
              "text": " country",
              "point_cs": 444
            },
            {
              "text": " can",
              "point_cs": 474
            },
            {
              "text": " do",
              "point_cs": 498
            },
            {
              "text": " for",
              "point_cs": 526
            },
            {
              "text": " you",
              "point_cs": 594
            },
            {
              "text": " ask",
              "point_cs": 632
            },
            {
              "text": " what",
              "point_cs": 668
            },
            {
              "text": " you",
              "point_cs": 694
            },
            {
              "text": " can",
              "point_cs": 716
            },
            {
              "text": " do",
              "point_cs": 742
            },
            {
              "text": " for",
              "point_cs": 760
            },
            {
              "text": " your",
              "point_cs": 780
            },
            {
              "text": " country",
              "point_cs": 818
            },
            {
              "text": ".",
              "point_cs": 818
            }
          ],
          "command": [
            "/tmp/atrain-whisper-a/.whisper-cli-unpatched",
            "-m",
            "/tmp/atrain-whisper-a/.ggml-tiny.bin",
            "-f",
            "/tmp/atrain-whisper-a-cpu-results/audio/base.wav",
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
            "/tmp/atrain-whisper-a-cpu-results/upstream-dtw-vad-base",
            "--vad",
            "-vm",
            "/tmp/atrain-whisper-a/.ggml-silero-v5.1.2.bin",
            "--dtw",
            "tiny"
          ],
          "wall_s": 0.816194455997902,
          "status": "passed"
        },
        "leading": {
          "text": " And so my fellow Americans ask not what your country can do for you ask what you can do for your country.",
          "words": [
            {
              "text": " And",
              "start_ms": 20,
              "end_ms": 220,
              "pieces": [
                " And"
              ]
            },
            {
              "text": " so",
              "start_ms": 370,
              "end_ms": 470,
              "pieces": [
                " so"
              ]
            },
            {
              "text": " my",
              "start_ms": 470,
              "end_ms": 660,
              "pieces": [
                " my"
              ]
            },
            {
              "text": " fellow",
              "start_ms": 660,
              "end_ms": 1230,
              "pieces": [
                " fellow"
              ]
            },
            {
              "text": " Americans",
              "start_ms": 1230,
              "end_ms": 1790,
              "pieces": [
                " Americans"
              ]
            },
            {
              "text": " ask",
              "start_ms": 2150,
              "end_ms": 2510,
              "pieces": [
                " ask"
              ]
            },
            {
              "text": " not",
              "start_ms": 2870,
              "end_ms": 3140,
              "pieces": [
                " not"
              ]
            },
            {
              "text": " what",
              "start_ms": 3480,
              "end_ms": 3600,
              "pieces": [
                " what"
              ]
            },
            {
              "text": " your",
              "start_ms": 3600,
              "end_ms": 3900,
              "pieces": [
                " your"
              ]
            },
            {
              "text": " country",
              "start_ms": 4040,
              "end_ms": 4480,
              "pieces": [
                " country"
              ]
            },
            {
              "text": " can",
              "start_ms": 4480,
              "end_ms": 4790,
              "pieces": [
                " can"
              ]
            },
            {
              "text": " do",
              "start_ms": 4790,
              "end_ms": 4990,
              "pieces": [
                " do"
              ]
            },
            {
              "text": " for",
              "start_ms": 5080,
              "end_ms": 5420,
              "pieces": [
                " for"
              ]
            },
            {
              "text": " you",
              "start_ms": 5420,
              "end_ms": 5590,
              "pieces": [
                " you"
              ]
            },
            {
              "text": " ask",
              "start_ms": 5980,
              "end_ms": 6270,
              "pieces": [
                " ask"
              ]
            },
            {
              "text": " what",
              "start_ms": 6430,
              "end_ms": 6540,
              "pieces": [
                " what"
              ]
            },
            {
              "text": " you",
              "start_ms": 6700,
              "end_ms": 6900,
              "pieces": [
                " you"
              ]
            },
            {
              "text": " can",
              "start_ms": 6900,
              "end_ms": 7160,
              "pieces": [
                " can"
              ]
            },
            {
              "text": " do",
              "start_ms": 7160,
              "end_ms": 7340,
              "pieces": [
                " do"
              ]
            },
            {
              "text": " for",
              "start_ms": 7340,
              "end_ms": 7520,
              "pieces": [
                " for"
              ]
            },
            {
              "text": " your",
              "start_ms": 7520,
              "end_ms": 7680,
              "pieces": [
                " your"
              ]
            },
            {
              "text": " country.",
              "start_ms": 7680,
              "end_ms": 8240,
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
              "point_cs": 18
            },
            {
              "text": " so",
              "point_cs": 74
            },
            {
              "text": " my",
              "point_cs": 102
            },
            {
              "text": " fellow",
              "point_cs": 136
            },
            {
              "text": " Americans",
              "point_cs": 190
            },
            {
              "text": " ask",
              "point_cs": 266
            },
            {
              "text": " not",
              "point_cs": 324
            },
            {
              "text": " what",
              "point_cs": 378
            },
            {
              "text": " your",
              "point_cs": 404
            },
            {
              "text": " country",
              "point_cs": 450
            },
            {
              "text": " can",
              "point_cs": 480
            },
            {
              "text": " do",
              "point_cs": 502
            },
            {
              "text": " for",
              "point_cs": 528
            },
            {
              "text": " you",
              "point_cs": 586
            },
            {
              "text": " ask",
              "point_cs": 640
            },
            {
              "text": " what",
              "point_cs": 676
            },
            {
              "text": " you",
              "point_cs": 702
            },
            {
              "text": " can",
              "point_cs": 724
            },
            {
              "text": " do",
              "point_cs": 750
            },
            {
              "text": " for",
              "point_cs": 768
            },
            {
              "text": " your",
              "point_cs": 788
            },
            {
              "text": " country",
              "point_cs": 822
            },
            {
              "text": ".",
              "point_cs": 822
            }
          ],
          "command": [
            "/tmp/atrain-whisper-a/.whisper-cli-unpatched",
            "-m",
            "/tmp/atrain-whisper-a/.ggml-tiny.bin",
            "-f",
            "/tmp/atrain-whisper-a-cpu-results/audio/leading.wav",
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
            "/tmp/atrain-whisper-a-cpu-results/upstream-dtw-vad-leading",
            "--vad",
            "-vm",
            "/tmp/atrain-whisper-a/.ggml-silero-v5.1.2.bin",
            "--dtw",
            "tiny"
          ],
          "wall_s": 0.8165271360048791,
          "status": "passed"
        },
        "trailing": {
          "text": " And so my fellow Americans ask not what your country can do for you ask what you can do for your country.",
          "words": [
            {
              "text": " And",
              "start_ms": 40,
              "end_ms": 250,
              "pieces": [
                " And"
              ]
            },
            {
              "text": " so",
              "start_ms": 390,
              "end_ms": 470,
              "pieces": [
                " so"
              ]
            },
            {
              "text": " my",
              "start_ms": 470,
              "end_ms": 660,
              "pieces": [
                " my"
              ]
            },
            {
              "text": " fellow",
              "start_ms": 660,
              "end_ms": 1230,
              "pieces": [
                " fellow"
              ]
            },
            {
              "text": " Americans",
              "start_ms": 1230,
              "end_ms": 1810,
              "pieces": [
                " Americans"
              ]
            },
            {
              "text": " ask",
              "start_ms": 2140,
              "end_ms": 2500,
              "pieces": [
                " ask"
              ]
            },
            {
              "text": " not",
              "start_ms": 2830,
              "end_ms": 3100,
              "pieces": [
                " not"
              ]
            },
            {
              "text": " what",
              "start_ms": 3430,
              "end_ms": 3590,
              "pieces": [
                " what"
              ]
            },
            {
              "text": " your",
              "start_ms": 3680,
              "end_ms": 3850,
              "pieces": [
                " your"
              ]
            },
            {
              "text": " country",
              "start_ms": 3990,
              "end_ms": 4440,
              "pieces": [
                " country"
              ]
            },
            {
              "text": " can",
              "start_ms": 4520,
              "end_ms": 4700,
              "pieces": [
                " can"
              ]
            },
            {
              "text": " do",
              "start_ms": 4720,
              "end_ms": 4880,
              "pieces": [
                " do"
              ]
            },
            {
              "text": " for",
              "start_ms": 4880,
              "end_ms": 5270,
              "pieces": [
                " for"
              ]
            },
            {
              "text": " you",
              "start_ms": 5270,
              "end_ms": 5520,
              "pieces": [
                " you"
              ]
            },
            {
              "text": " ask",
              "start_ms": 5900,
              "end_ms": 6190,
              "pieces": [
                " ask"
              ]
            },
            {
              "text": " what",
              "start_ms": 6340,
              "end_ms": 6460,
              "pieces": [
                " what"
              ]
            },
            {
              "text": " you",
              "start_ms": 6620,
              "end_ms": 6760,
              "pieces": [
                " you"
              ]
            },
            {
              "text": " can",
              "start_ms": 6760,
              "end_ms": 7000,
              "pieces": [
                " can"
              ]
            },
            {
              "text": " do",
              "start_ms": 7000,
              "end_ms": 7220,
              "pieces": [
                " do"
              ]
            },
            {
              "text": " for",
              "start_ms": 7220,
              "end_ms": 7440,
              "pieces": [
                " for"
              ]
            },
            {
              "text": " your",
              "start_ms": 7440,
              "end_ms": 7680,
              "pieces": [
                " your"
              ]
            },
            {
              "text": " country.",
              "start_ms": 7680,
              "end_ms": 8200,
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
              "point_cs": 18
            },
            {
              "text": " so",
              "point_cs": 76
            },
            {
              "text": " my",
              "point_cs": 104
            },
            {
              "text": " fellow",
              "point_cs": 138
            },
            {
              "text": " Americans",
              "point_cs": 192
            },
            {
              "text": " ask",
              "point_cs": 264
            },
            {
              "text": " not",
              "point_cs": 320
            },
            {
              "text": " what",
              "point_cs": 372
            },
            {
              "text": " your",
              "point_cs": 400
            },
            {
              "text": " country",
              "point_cs": 444
            },
            {
              "text": " can",
              "point_cs": 474
            },
            {
              "text": " do",
              "point_cs": 498
            },
            {
              "text": " for",
              "point_cs": 526
            },
            {
              "text": " you",
              "point_cs": 594
            },
            {
              "text": " ask",
              "point_cs": 632
            },
            {
              "text": " what",
              "point_cs": 668
            },
            {
              "text": " you",
              "point_cs": 694
            },
            {
              "text": " can",
              "point_cs": 716
            },
            {
              "text": " do",
              "point_cs": 742
            },
            {
              "text": " for",
              "point_cs": 760
            },
            {
              "text": " your",
              "point_cs": 780
            },
            {
              "text": " country",
              "point_cs": 818
            },
            {
              "text": ".",
              "point_cs": 818
            }
          ],
          "command": [
            "/tmp/atrain-whisper-a/.whisper-cli-unpatched",
            "-m",
            "/tmp/atrain-whisper-a/.ggml-tiny.bin",
            "-f",
            "/tmp/atrain-whisper-a-cpu-results/audio/trailing.wav",
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
            "/tmp/atrain-whisper-a-cpu-results/upstream-dtw-vad-trailing",
            "--vad",
            "-vm",
            "/tmp/atrain-whisper-a/.ggml-silero-v5.1.2.bin",
            "--dtw",
            "tiny"
          ],
          "wall_s": 0.8155537540005753,
          "status": "passed"
        },
        "internal": {
          "text": " And so my fellow Americans ask not what your country can do for you ask what you can do for your country. And so my fellow Americans ask not what your country can do for you ask what you can do for your country.",
          "words": [
            {
              "text": " And",
              "start_ms": 40,
              "end_ms": 250,
              "pieces": [
                " And"
              ]
            },
            {
              "text": " so",
              "start_ms": 390,
              "end_ms": 450,
              "pieces": [
                " so"
              ]
            },
            {
              "text": " my",
              "start_ms": 450,
              "end_ms": 630,
              "pieces": [
                " my"
              ]
            },
            {
              "text": " fellow",
              "start_ms": 630,
              "end_ms": 1180,
              "pieces": [
                " fellow"
              ]
            },
            {
              "text": " Americans",
              "start_ms": 1180,
              "end_ms": 1810,
              "pieces": [
                " Americans"
              ]
            },
            {
              "text": " ask",
              "start_ms": 2140,
              "end_ms": 2500,
              "pieces": [
                " ask"
              ]
            },
            {
              "text": " not",
              "start_ms": 2830,
              "end_ms": 3100,
              "pieces": [
                " not"
              ]
            },
            {
              "text": " what",
              "start_ms": 3430,
              "end_ms": 3590,
              "pieces": [
                " what"
              ]
            },
            {
              "text": " your",
              "start_ms": 3680,
              "end_ms": 3850,
              "pieces": [
                " your"
              ]
            },
            {
              "text": " country",
              "start_ms": 3990,
              "end_ms": 4440,
              "pieces": [
                " country"
              ]
            },
            {
              "text": " can",
              "start_ms": 4520,
              "end_ms": 4700,
              "pieces": [
                " can"
              ]
            },
            {
              "text": " do",
              "start_ms": 4720,
              "end_ms": 4880,
              "pieces": [
                " do"
              ]
            },
            {
              "text": " for",
              "start_ms": 4880,
              "end_ms": 5360,
              "pieces": [
                " for"
              ]
            },
            {
              "text": " you",
              "start_ms": 5360,
              "end_ms": 5540,
              "pieces": [
                " you"
              ]
            },
            {
              "text": " ask",
              "start_ms": 5900,
              "end_ms": 6180,
              "pieces": [
                " ask"
              ]
            },
            {
              "text": " what",
              "start_ms": 6340,
              "end_ms": 6460,
              "pieces": [
                " what"
              ]
            },
            {
              "text": " you",
              "start_ms": 6620,
              "end_ms": 6800,
              "pieces": [
                " you"
              ]
            },
            {
              "text": " can",
              "start_ms": 6800,
              "end_ms": 7000,
              "pieces": [
                " can"
              ]
            },
            {
              "text": " do",
              "start_ms": 7000,
              "end_ms": 7220,
              "pieces": [
                " do"
              ]
            },
            {
              "text": " for",
              "start_ms": 7220,
              "end_ms": 7440,
              "pieces": [
                " for"
              ]
            },
            {
              "text": " your",
              "start_ms": 7440,
              "end_ms": 7680,
              "pieces": [
                " your"
              ]
            },
            {
              "text": " country.",
              "start_ms": 7680,
              "end_ms": 8360,
              "pieces": [
                " country",
                "."
              ]
            },
            {
              "text": " And",
              "start_ms": 8410,
              "end_ms": 8600,
              "pieces": [
                " And"
              ]
            },
            {
              "text": " so",
              "start_ms": 8760,
              "end_ms": 8960,
              "pieces": [
                " so"
              ]
            },
            {
              "text": " my",
              "start_ms": 8960,
              "end_ms": 9200,
              "pieces": [
                " my"
              ]
            },
            {
              "text": " fellow",
              "start_ms": 9200,
              "end_ms": 9920,
              "pieces": [
                " fellow"
              ]
            },
            {
              "text": " Americans",
              "start_ms": 9920,
              "end_ms": 10860,
              "pieces": [
                " Americans"
              ]
            },
            {
              "text": " ask",
              "start_ms": 11210,
              "end_ms": 11370,
              "pieces": [
                " ask"
              ]
            },
            {
              "text": " not",
              "start_ms": 11370,
              "end_ms": 11460,
              "pieces": [
                " not"
              ]
            },
            {
              "text": " what",
              "start_ms": 11790,
              "end_ms": 12130,
              "pieces": [
                " what"
              ]
            },
            {
              "text": " your",
              "start_ms": 12130,
              "end_ms": 12470,
              "pieces": [
                " your"
              ]
            },
            {
              "text": " country",
              "start_ms": 12600,
              "end_ms": 13160,
              "pieces": [
                " country"
              ]
            },
            {
              "text": " can",
              "start_ms": 13160,
              "end_ms": 13440,
              "pieces": [
                " can"
              ]
            },
            {
              "text": " do",
              "start_ms": 13440,
              "end_ms": 13620,
              "pieces": [
                " do"
              ]
            },
            {
              "text": " for",
              "start_ms": 13620,
              "end_ms": 13870,
              "pieces": [
                " for"
              ]
            },
            {
              "text": " you",
              "start_ms": 13890,
              "end_ms": 14050,
              "pieces": [
                " you"
              ]
            },
            {
              "text": " ask",
              "start_ms": 14260,
              "end_ms": 14440,
              "pieces": [
                " ask"
              ]
            },
            {
              "text": " what",
              "start_ms": 14440,
              "end_ms": 14740,
              "pieces": [
                " what"
              ]
            },
            {
              "text": " you",
              "start_ms": 14740,
              "end_ms": 14820,
              "pieces": [
                " you"
              ]
            },
            {
              "text": " can",
              "start_ms": 14980,
              "end_ms": 15180,
              "pieces": [
                " can"
              ]
            },
            {
              "text": " do",
              "start_ms": 15180,
              "end_ms": 15330,
              "pieces": [
                " do"
              ]
            },
            {
              "text": " for",
              "start_ms": 15330,
              "end_ms": 15550,
              "pieces": [
                " for"
              ]
            },
            {
              "text": " your",
              "start_ms": 15550,
              "end_ms": 15850,
              "pieces": [
                " your"
              ]
            },
            {
              "text": " country.",
              "start_ms": 15850,
              "end_ms": 16640,
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
              "point_cs": 12
            },
            {
              "text": " so",
              "point_cs": 76
            },
            {
              "text": " my",
              "point_cs": 104
            },
            {
              "text": " fellow",
              "point_cs": 138
            },
            {
              "text": " Americans",
              "point_cs": 192
            },
            {
              "text": " ask",
              "point_cs": 266
            },
            {
              "text": " not",
              "point_cs": 320
            },
            {
              "text": " what",
              "point_cs": 374
            },
            {
              "text": " your",
              "point_cs": 402
            },
            {
              "text": " country",
              "point_cs": 444
            },
            {
              "text": " can",
              "point_cs": 474
            },
            {
              "text": " do",
              "point_cs": 500
            },
            {
              "text": " for",
              "point_cs": 526
            },
            {
              "text": " you",
              "point_cs": 596
            },
            {
              "text": " ask",
              "point_cs": 632
            },
            {
              "text": " what",
              "point_cs": 670
            },
            {
              "text": " you",
              "point_cs": 694
            },
            {
              "text": " can",
              "point_cs": 716
            },
            {
              "text": " do",
              "point_cs": 742
            },
            {
              "text": " for",
              "point_cs": 760
            },
            {
              "text": " your",
              "point_cs": 778
            },
            {
              "text": " country",
              "point_cs": 830
            },
            {
              "text": ".",
              "point_cs": 866
            },
            {
              "text": " And",
              "point_cs": 892
            },
            {
              "text": " so",
              "point_cs": 922
            },
            {
              "text": " my",
              "point_cs": 950
            },
            {
              "text": " fellow",
              "point_cs": 984
            },
            {
              "text": " Americans",
              "point_cs": 1032
            },
            {
              "text": " ask",
              "point_cs": 1110
            },
            {
              "text": " not",
              "point_cs": 1164
            },
            {
              "text": " what",
              "point_cs": 1216
            },
            {
              "text": " your",
              "point_cs": 1242
            },
            {
              "text": " country",
              "point_cs": 1290
            },
            {
              "text": " can",
              "point_cs": 1320
            },
            {
              "text": " do",
              "point_cs": 1344
            },
            {
              "text": " for",
              "point_cs": 1368
            },
            {
              "text": " you",
              "point_cs": 1426
            },
            {
              "text": " ask",
              "point_cs": 1476
            },
            {
              "text": " what",
              "point_cs": 1514
            },
            {
              "text": " you",
              "point_cs": 1538
            },
            {
              "text": " can",
              "point_cs": 1556
            },
            {
              "text": " do",
              "point_cs": 1586
            },
            {
              "text": " for",
              "point_cs": 1602
            },
            {
              "text": " your",
              "point_cs": 1626
            },
            {
              "text": " country",
              "point_cs": 1662
            },
            {
              "text": ".",
              "point_cs": 1662
            }
          ],
          "command": [
            "/tmp/atrain-whisper-a/.whisper-cli-unpatched",
            "-m",
            "/tmp/atrain-whisper-a/.ggml-tiny.bin",
            "-f",
            "/tmp/atrain-whisper-a-cpu-results/audio/internal.wav",
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
            "/tmp/atrain-whisper-a-cpu-results/upstream-dtw-vad-internal",
            "--vad",
            "-vm",
            "/tmp/atrain-whisper-a/.ggml-silero-v5.1.2.bin",
            "--dtw",
            "tiny"
          ],
          "wall_s": 1.0165697769989492,
          "status": "passed"
        },
        "boundary": {
          "text": " And so my fellow Americans ask not what your country can do for you ask what you can do for your country.",
          "words": [
            {
              "text": " And",
              "start_ms": 20,
              "end_ms": 220,
              "pieces": [
                " And"
              ]
            },
            {
              "text": " so",
              "start_ms": 370,
              "end_ms": 450,
              "pieces": [
                " so"
              ]
            },
            {
              "text": " my",
              "start_ms": 450,
              "end_ms": 630,
              "pieces": [
                " my"
              ]
            },
            {
              "text": " fellow",
              "start_ms": 630,
              "end_ms": 1180,
              "pieces": [
                " fellow"
              ]
            },
            {
              "text": " Americans",
              "start_ms": 1180,
              "end_ms": 1790,
              "pieces": [
                " Americans"
              ]
            },
            {
              "text": " ask",
              "start_ms": 2090,
              "end_ms": 2450,
              "pieces": [
                " ask"
              ]
            },
            {
              "text": " not",
              "start_ms": 2850,
              "end_ms": 3120,
              "pieces": [
                " not"
              ]
            },
            {
              "text": " what",
              "start_ms": 3390,
              "end_ms": 3550,
              "pieces": [
                " what"
              ]
            },
            {
              "text": " your",
              "start_ms": 3630,
              "end_ms": 3810,
              "pieces": [
                " your"
              ]
            },
            {
              "text": " country",
              "start_ms": 3950,
              "end_ms": 4360,
              "pieces": [
                " country"
              ]
            },
            {
              "text": " can",
              "start_ms": 4360,
              "end_ms": 4630,
              "pieces": [
                " can"
              ]
            },
            {
              "text": " do",
              "start_ms": 4680,
              "end_ms": 4880,
              "pieces": [
                " do"
              ]
            },
            {
              "text": " for",
              "start_ms": 4990,
              "end_ms": 5270,
              "pieces": [
                " for"
              ]
            },
            {
              "text": " you",
              "start_ms": 5270,
              "end_ms": 5480,
              "pieces": [
                " you"
              ]
            },
            {
              "text": " ask",
              "start_ms": 5890,
              "end_ms": 6180,
              "pieces": [
                " ask"
              ]
            },
            {
              "text": " what",
              "start_ms": 6340,
              "end_ms": 6450,
              "pieces": [
                " what"
              ]
            },
            {
              "text": " you",
              "start_ms": 6610,
              "end_ms": 6760,
              "pieces": [
                " you"
              ]
            },
            {
              "text": " can",
              "start_ms": 6760,
              "end_ms": 7000,
              "pieces": [
                " can"
              ]
            },
            {
              "text": " do",
              "start_ms": 7000,
              "end_ms": 7220,
              "pieces": [
                " do"
              ]
            },
            {
              "text": " for",
              "start_ms": 7220,
              "end_ms": 7440,
              "pieces": [
                " for"
              ]
            },
            {
              "text": " your",
              "start_ms": 7440,
              "end_ms": 7680,
              "pieces": [
                " your"
              ]
            },
            {
              "text": " country.",
              "start_ms": 7680,
              "end_ms": 8200,
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
              "point_cs": 20
            },
            {
              "text": " so",
              "point_cs": 74
            },
            {
              "text": " my",
              "point_cs": 102
            },
            {
              "text": " fellow",
              "point_cs": 136
            },
            {
              "text": " Americans",
              "point_cs": 190
            },
            {
              "text": " ask",
              "point_cs": 262
            },
            {
              "text": " not",
              "point_cs": 322
            },
            {
              "text": " what",
              "point_cs": 368
            },
            {
              "text": " your",
              "point_cs": 396
            },
            {
              "text": " country",
              "point_cs": 440
            },
            {
              "text": " can",
              "point_cs": 470
            },
            {
              "text": " do",
              "point_cs": 494
            },
            {
              "text": " for",
              "point_cs": 522
            },
            {
              "text": " you",
              "point_cs": 580
            },
            {
              "text": " ask",
              "point_cs": 632
            },
            {
              "text": " what",
              "point_cs": 668
            },
            {
              "text": " you",
              "point_cs": 692
            },
            {
              "text": " can",
              "point_cs": 712
            },
            {
              "text": " do",
              "point_cs": 740
            },
            {
              "text": " for",
              "point_cs": 758
            },
            {
              "text": " your",
              "point_cs": 780
            },
            {
              "text": " country",
              "point_cs": 818
            },
            {
              "text": ".",
              "point_cs": 818
            }
          ],
          "command": [
            "/tmp/atrain-whisper-a/.whisper-cli-unpatched",
            "-m",
            "/tmp/atrain-whisper-a/.ggml-tiny.bin",
            "-f",
            "/tmp/atrain-whisper-a-cpu-results/audio/boundary.wav",
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
            "/tmp/atrain-whisper-a-cpu-results/upstream-dtw-vad-boundary",
            "--vad",
            "-vm",
            "/tmp/atrain-whisper-a/.ggml-silero-v5.1.2.bin",
            "--dtw",
            "tiny"
          ],
          "wall_s": 0.8160151350020897,
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
            "/tmp/atrain-whisper-a/.ggml-tiny.bin",
            "-f",
            "/tmp/atrain-whisper-a-cpu-results/audio/silence.wav",
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
            "/tmp/atrain-whisper-a-cpu-results/upstream-dtw-vad-silence",
            "--vad",
            "-vm",
            "/tmp/atrain-whisper-a/.ggml-silero-v5.1.2.bin",
            "--dtw",
            "tiny"
          ],
          "wall_s": 0.1647027829894796,
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
            "/tmp/atrain-whisper-a/.ggml-tiny.bin",
            "-f",
            "/tmp/atrain-whisper-a-cpu-results/audio/noise.wav",
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
            "/tmp/atrain-whisper-a-cpu-results/upstream-dtw-vad-noise",
            "--vad",
            "-vm",
            "/tmp/atrain-whisper-a/.ggml-silero-v5.1.2.bin",
            "--dtw",
            "tiny"
          ],
          "wall_s": 0.16474084599758498,
          "status": "passed"
        },
        "german": {
          "text": "",
          "words": [],
          "problems": [
            "speech fixture returned no timed words"
          ],
          "dtw_points": [],
          "command": [
            "/tmp/atrain-whisper-a/.whisper-cli-unpatched",
            "-m",
            "/tmp/atrain-whisper-a/.ggml-tiny.bin",
            "-f",
            "/tmp/atrain-whisper-a-cpu-results/audio/german.wav",
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
            "/tmp/atrain-whisper-a-cpu-results/upstream-dtw-vad-german",
            "--vad",
            "-vm",
            "/tmp/atrain-whisper-a/.ggml-silero-v5.1.2.bin",
            "--dtw",
            "tiny"
          ],
          "wall_s": 0.16453778999857605,
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
              "point_cs": 74
            }
          ],
          "command": [
            "/tmp/atrain-whisper-a/.whisper-cli-unpatched",
            "-m",
            "/tmp/atrain-whisper-a/.ggml-tiny.bin",
            "-f",
            "/tmp/atrain-whisper-a-cpu-results/audio/japanese.wav",
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
            "/tmp/atrain-whisper-a-cpu-results/upstream-dtw-vad-japanese",
            "--vad",
            "-vm",
            "/tmp/atrain-whisper-a/.ggml-silero-v5.1.2.bin",
            "--dtw",
            "tiny"
          ],
          "wall_s": 0.6156251780048478,
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
            5030,
            5020,
            5000,
            5000,
            5000,
            5000,
            5000,
            5000,
            5020,
            4990,
            4990,
            4960,
            4960,
            4950,
            4990,
            5080,
            4950,
            4950,
            4960,
            5040,
            4910,
            4930,
            4890,
            4800,
            4850,
            4850,
            4930,
            4920,
            4920,
            4910,
            4920,
            4920,
            4860,
            4860,
            4840,
            4840,
            4880,
            4880,
            4920,
            4920,
            5000,
            5000,
            4960
          ],
          "max_boundary_error_ms": 5080,
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
          "status": "passed"
        },
        "boundary": {
          "tolerance_ms": 50,
          "matched_words": 22,
          "unmatched_reference_words": 0,
          "unmatched_candidate_words": 0,
          "boundary_errors_ms": [
            25020,
            25030,
            25020,
            25020,
            25020,
            25030,
            25030,
            25050,
            25050,
            25020,
            25050,
            25050,
            24980,
            24980,
            25040,
            25040,
            25050,
            25040,
            25040,
            25080,
            25160,
            25070,
            25040,
            25000,
            24890,
            25000,
            25000,
            25040,
            25010,
            25010,
            25000,
            25010,
            25010,
            25000,
            25000,
            25000,
            25000,
            25000,
            25000,
            25000,
            25000,
            25000,
            25000,
            25000
          ],
          "max_boundary_error_ms": 25160,
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
            20,
            20,
            30,
            30,
            50,
            50,
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
            90,
            90,
            20,
            0,
            10,
            0,
            0,
            0,
            40,
            40,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            160
          ],
          "max_boundary_error_ms": 160,
          "status": "failed"
        },
        "internal-second": {
          "tolerance_ms": 50,
          "matched_words": 0,
          "unmatched_reference_words": 22,
          "unmatched_candidate_words": 0,
          "boundary_errors_ms": [],
          "max_boundary_error_ms": null,
          "status": "failed"
        }
      }
    },
    "patched-dtw-vad": {
      "fixtures": {
        "base": {
          "text": " And so my fellow Americans ask not what your country can do for you ask what you can do for your country.",
          "words": [
            {
              "text": " And",
              "start_ms": 330,
              "end_ms": 540,
              "pieces": [
                " And"
              ]
            },
            {
              "text": " so",
              "start_ms": 680,
              "end_ms": 760,
              "pieces": [
                " so"
              ]
            },
            {
              "text": " my",
              "start_ms": 760,
              "end_ms": 950,
              "pieces": [
                " my"
              ]
            },
            {
              "text": " fellow",
              "start_ms": 950,
              "end_ms": 1520,
              "pieces": [
                " fellow"
              ]
            },
            {
              "text": " Americans",
              "start_ms": 1520,
              "end_ms": 2100,
              "pieces": [
                " Americans"
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
              "end_ms": 4280,
              "pieces": [
                " not"
              ]
            },
            {
              "text": " what",
              "start_ms": 5410,
              "end_ms": 5570,
              "pieces": [
                " what"
              ]
            },
            {
              "text": " your",
              "start_ms": 5660,
              "end_ms": 5830,
              "pieces": [
                " your"
              ]
            },
            {
              "text": " country",
              "start_ms": 5970,
              "end_ms": 6420,
              "pieces": [
                " country"
              ]
            },
            {
              "text": " can",
              "start_ms": 6500,
              "end_ms": 6680,
              "pieces": [
                " can"
              ]
            },
            {
              "text": " do",
              "start_ms": 6700,
              "end_ms": 6860,
              "pieces": [
                " do"
              ]
            },
            {
              "text": " for",
              "start_ms": 6860,
              "end_ms": 7250,
              "pieces": [
                " for"
              ]
            },
            {
              "text": " you",
              "start_ms": 7250,
              "end_ms": 7500,
              "pieces": [
                " you"
              ]
            },
            {
              "text": " ask",
              "start_ms": 8190,
              "end_ms": 8480,
              "pieces": [
                " ask"
              ]
            },
            {
              "text": " what",
              "start_ms": 8630,
              "end_ms": 8750,
              "pieces": [
                " what"
              ]
            },
            {
              "text": " you",
              "start_ms": 8910,
              "end_ms": 9050,
              "pieces": [
                " you"
              ]
            },
            {
              "text": " can",
              "start_ms": 9050,
              "end_ms": 9290,
              "pieces": [
                " can"
              ]
            },
            {
              "text": " do",
              "start_ms": 9290,
              "end_ms": 9510,
              "pieces": [
                " do"
              ]
            },
            {
              "text": " for",
              "start_ms": 9510,
              "end_ms": 9730,
              "pieces": [
                " for"
              ]
            },
            {
              "text": " your",
              "start_ms": 9730,
              "end_ms": 9970,
              "pieces": [
                " your"
              ]
            },
            {
              "text": " country.",
              "start_ms": 9970,
              "end_ms": 10490,
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
              "point_cs": 18
            },
            {
              "text": " so",
              "point_cs": 76
            },
            {
              "text": " my",
              "point_cs": 104
            },
            {
              "text": " fellow",
              "point_cs": 138
            },
            {
              "text": " Americans",
              "point_cs": 192
            },
            {
              "text": " ask",
              "point_cs": 264
            },
            {
              "text": " not",
              "point_cs": 320
            },
            {
              "text": " what",
              "point_cs": 372
            },
            {
              "text": " your",
              "point_cs": 400
            },
            {
              "text": " country",
              "point_cs": 444
            },
            {
              "text": " can",
              "point_cs": 474
            },
            {
              "text": " do",
              "point_cs": 498
            },
            {
              "text": " for",
              "point_cs": 526
            },
            {
              "text": " you",
              "point_cs": 594
            },
            {
              "text": " ask",
              "point_cs": 632
            },
            {
              "text": " what",
              "point_cs": 668
            },
            {
              "text": " you",
              "point_cs": 694
            },
            {
              "text": " can",
              "point_cs": 716
            },
            {
              "text": " do",
              "point_cs": 742
            },
            {
              "text": " for",
              "point_cs": 760
            },
            {
              "text": " your",
              "point_cs": 780
            },
            {
              "text": " country",
              "point_cs": 818
            },
            {
              "text": ".",
              "point_cs": 818
            }
          ],
          "command": [
            "/tmp/atrain-whisper-a/.whisper-cli-patched",
            "-m",
            "/tmp/atrain-whisper-a/.ggml-tiny.bin",
            "-f",
            "/tmp/atrain-whisper-a-cpu-results/audio/base.wav",
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
            "/tmp/atrain-whisper-a-cpu-results/patched-dtw-vad-base",
            "--vad",
            "-vm",
            "/tmp/atrain-whisper-a/.ggml-silero-v5.1.2.bin",
            "--dtw",
            "tiny"
          ],
          "wall_s": 0.8158041790011339,
          "status": "passed"
        },
        "leading": {
          "text": " And so my fellow Americans ask not what your country can do for you ask what you can do for your country.",
          "words": [
            {
              "text": " And",
              "start_ms": 5330,
              "end_ms": 5530,
              "pieces": [
                " And"
              ]
            },
            {
              "text": " so",
              "start_ms": 5680,
              "end_ms": 5780,
              "pieces": [
                " so"
              ]
            },
            {
              "text": " my",
              "start_ms": 5780,
              "end_ms": 5970,
              "pieces": [
                " my"
              ]
            },
            {
              "text": " fellow",
              "start_ms": 5970,
              "end_ms": 6540,
              "pieces": [
                " fellow"
              ]
            },
            {
              "text": " Americans",
              "start_ms": 6540,
              "end_ms": 7100,
              "pieces": [
                " Americans"
              ]
            },
            {
              "text": " ask",
              "start_ms": 8290,
              "end_ms": 8650,
              "pieces": [
                " ask"
              ]
            },
            {
              "text": " not",
              "start_ms": 9010,
              "end_ms": 9280,
              "pieces": [
                " not"
              ]
            },
            {
              "text": " what",
              "start_ms": 10410,
              "end_ms": 10530,
              "pieces": [
                " what"
              ]
            },
            {
              "text": " your",
              "start_ms": 10530,
              "end_ms": 10830,
              "pieces": [
                " your"
              ]
            },
            {
              "text": " country",
              "start_ms": 10970,
              "end_ms": 11410,
              "pieces": [
                " country"
              ]
            },
            {
              "text": " can",
              "start_ms": 11410,
              "end_ms": 11720,
              "pieces": [
                " can"
              ]
            },
            {
              "text": " do",
              "start_ms": 11720,
              "end_ms": 11920,
              "pieces": [
                " do"
              ]
            },
            {
              "text": " for",
              "start_ms": 12010,
              "end_ms": 12350,
              "pieces": [
                " for"
              ]
            },
            {
              "text": " you",
              "start_ms": 12350,
              "end_ms": 12520,
              "pieces": [
                " you"
              ]
            },
            {
              "text": " ask",
              "start_ms": 13190,
              "end_ms": 13480,
              "pieces": [
                " ask"
              ]
            },
            {
              "text": " what",
              "start_ms": 13640,
              "end_ms": 13750,
              "pieces": [
                " what"
              ]
            },
            {
              "text": " you",
              "start_ms": 13910,
              "end_ms": 14110,
              "pieces": [
                " you"
              ]
            },
            {
              "text": " can",
              "start_ms": 14110,
              "end_ms": 14370,
              "pieces": [
                " can"
              ]
            },
            {
              "text": " do",
              "start_ms": 14370,
              "end_ms": 14550,
              "pieces": [
                " do"
              ]
            },
            {
              "text": " for",
              "start_ms": 14550,
              "end_ms": 14730,
              "pieces": [
                " for"
              ]
            },
            {
              "text": " your",
              "start_ms": 14730,
              "end_ms": 14890,
              "pieces": [
                " your"
              ]
            },
            {
              "text": " country.",
              "start_ms": 14890,
              "end_ms": 15450,
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
              "point_cs": 18
            },
            {
              "text": " so",
              "point_cs": 74
            },
            {
              "text": " my",
              "point_cs": 102
            },
            {
              "text": " fellow",
              "point_cs": 136
            },
            {
              "text": " Americans",
              "point_cs": 190
            },
            {
              "text": " ask",
              "point_cs": 266
            },
            {
              "text": " not",
              "point_cs": 324
            },
            {
              "text": " what",
              "point_cs": 378
            },
            {
              "text": " your",
              "point_cs": 404
            },
            {
              "text": " country",
              "point_cs": 450
            },
            {
              "text": " can",
              "point_cs": 480
            },
            {
              "text": " do",
              "point_cs": 502
            },
            {
              "text": " for",
              "point_cs": 528
            },
            {
              "text": " you",
              "point_cs": 586
            },
            {
              "text": " ask",
              "point_cs": 640
            },
            {
              "text": " what",
              "point_cs": 676
            },
            {
              "text": " you",
              "point_cs": 702
            },
            {
              "text": " can",
              "point_cs": 724
            },
            {
              "text": " do",
              "point_cs": 750
            },
            {
              "text": " for",
              "point_cs": 768
            },
            {
              "text": " your",
              "point_cs": 788
            },
            {
              "text": " country",
              "point_cs": 822
            },
            {
              "text": ".",
              "point_cs": 822
            }
          ],
          "command": [
            "/tmp/atrain-whisper-a/.whisper-cli-patched",
            "-m",
            "/tmp/atrain-whisper-a/.ggml-tiny.bin",
            "-f",
            "/tmp/atrain-whisper-a-cpu-results/audio/leading.wav",
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
            "/tmp/atrain-whisper-a-cpu-results/patched-dtw-vad-leading",
            "--vad",
            "-vm",
            "/tmp/atrain-whisper-a/.ggml-silero-v5.1.2.bin",
            "--dtw",
            "tiny"
          ],
          "wall_s": 0.8160742189938901,
          "status": "passed"
        },
        "trailing": {
          "text": " And so my fellow Americans ask not what your country can do for you ask what you can do for your country.",
          "words": [
            {
              "text": " And",
              "start_ms": 330,
              "end_ms": 540,
              "pieces": [
                " And"
              ]
            },
            {
              "text": " so",
              "start_ms": 680,
              "end_ms": 760,
              "pieces": [
                " so"
              ]
            },
            {
              "text": " my",
              "start_ms": 760,
              "end_ms": 950,
              "pieces": [
                " my"
              ]
            },
            {
              "text": " fellow",
              "start_ms": 950,
              "end_ms": 1520,
              "pieces": [
                " fellow"
              ]
            },
            {
              "text": " Americans",
              "start_ms": 1520,
              "end_ms": 2100,
              "pieces": [
                " Americans"
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
              "end_ms": 4280,
              "pieces": [
                " not"
              ]
            },
            {
              "text": " what",
              "start_ms": 5410,
              "end_ms": 5570,
              "pieces": [
                " what"
              ]
            },
            {
              "text": " your",
              "start_ms": 5660,
              "end_ms": 5830,
              "pieces": [
                " your"
              ]
            },
            {
              "text": " country",
              "start_ms": 5970,
              "end_ms": 6420,
              "pieces": [
                " country"
              ]
            },
            {
              "text": " can",
              "start_ms": 6500,
              "end_ms": 6680,
              "pieces": [
                " can"
              ]
            },
            {
              "text": " do",
              "start_ms": 6700,
              "end_ms": 6860,
              "pieces": [
                " do"
              ]
            },
            {
              "text": " for",
              "start_ms": 6860,
              "end_ms": 7250,
              "pieces": [
                " for"
              ]
            },
            {
              "text": " you",
              "start_ms": 7250,
              "end_ms": 7500,
              "pieces": [
                " you"
              ]
            },
            {
              "text": " ask",
              "start_ms": 8190,
              "end_ms": 8480,
              "pieces": [
                " ask"
              ]
            },
            {
              "text": " what",
              "start_ms": 8630,
              "end_ms": 8750,
              "pieces": [
                " what"
              ]
            },
            {
              "text": " you",
              "start_ms": 8910,
              "end_ms": 9050,
              "pieces": [
                " you"
              ]
            },
            {
              "text": " can",
              "start_ms": 9050,
              "end_ms": 9290,
              "pieces": [
                " can"
              ]
            },
            {
              "text": " do",
              "start_ms": 9290,
              "end_ms": 9510,
              "pieces": [
                " do"
              ]
            },
            {
              "text": " for",
              "start_ms": 9510,
              "end_ms": 9730,
              "pieces": [
                " for"
              ]
            },
            {
              "text": " your",
              "start_ms": 9730,
              "end_ms": 9970,
              "pieces": [
                " your"
              ]
            },
            {
              "text": " country.",
              "start_ms": 9970,
              "end_ms": 10490,
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
              "point_cs": 18
            },
            {
              "text": " so",
              "point_cs": 76
            },
            {
              "text": " my",
              "point_cs": 104
            },
            {
              "text": " fellow",
              "point_cs": 138
            },
            {
              "text": " Americans",
              "point_cs": 192
            },
            {
              "text": " ask",
              "point_cs": 264
            },
            {
              "text": " not",
              "point_cs": 320
            },
            {
              "text": " what",
              "point_cs": 372
            },
            {
              "text": " your",
              "point_cs": 400
            },
            {
              "text": " country",
              "point_cs": 444
            },
            {
              "text": " can",
              "point_cs": 474
            },
            {
              "text": " do",
              "point_cs": 498
            },
            {
              "text": " for",
              "point_cs": 526
            },
            {
              "text": " you",
              "point_cs": 594
            },
            {
              "text": " ask",
              "point_cs": 632
            },
            {
              "text": " what",
              "point_cs": 668
            },
            {
              "text": " you",
              "point_cs": 694
            },
            {
              "text": " can",
              "point_cs": 716
            },
            {
              "text": " do",
              "point_cs": 742
            },
            {
              "text": " for",
              "point_cs": 760
            },
            {
              "text": " your",
              "point_cs": 780
            },
            {
              "text": " country",
              "point_cs": 818
            },
            {
              "text": ".",
              "point_cs": 818
            }
          ],
          "command": [
            "/tmp/atrain-whisper-a/.whisper-cli-patched",
            "-m",
            "/tmp/atrain-whisper-a/.ggml-tiny.bin",
            "-f",
            "/tmp/atrain-whisper-a-cpu-results/audio/trailing.wav",
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
            "/tmp/atrain-whisper-a-cpu-results/patched-dtw-vad-trailing",
            "--vad",
            "-vm",
            "/tmp/atrain-whisper-a/.ggml-silero-v5.1.2.bin",
            "--dtw",
            "tiny"
          ],
          "wall_s": 0.8160792170092463,
          "status": "passed"
        },
        "internal": {
          "text": " And so my fellow Americans ask not what your country can do for you ask what you can do for your country. And so my fellow Americans ask not what your country can do for you ask what you can do for your country.",
          "words": [
            {
              "text": " And",
              "start_ms": 330,
              "end_ms": 540,
              "pieces": [
                " And"
              ]
            },
            {
              "text": " so",
              "start_ms": 680,
              "end_ms": 740,
              "pieces": [
                " so"
              ]
            },
            {
              "text": " my",
              "start_ms": 740,
              "end_ms": 920,
              "pieces": [
                " my"
              ]
            },
            {
              "text": " fellow",
              "start_ms": 920,
              "end_ms": 1470,
              "pieces": [
                " fellow"
              ]
            },
            {
              "text": " Americans",
              "start_ms": 1470,
              "end_ms": 2100,
              "pieces": [
                " Americans"
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
              "end_ms": 4280,
              "pieces": [
                " not"
              ]
            },
            {
              "text": " what",
              "start_ms": 5410,
              "end_ms": 5570,
              "pieces": [
                " what"
              ]
            },
            {
              "text": " your",
              "start_ms": 5660,
              "end_ms": 5830,
              "pieces": [
                " your"
              ]
            },
            {
              "text": " country",
              "start_ms": 5970,
              "end_ms": 6420,
              "pieces": [
                " country"
              ]
            },
            {
              "text": " can",
              "start_ms": 6500,
              "end_ms": 6680,
              "pieces": [
                " can"
              ]
            },
            {
              "text": " do",
              "start_ms": 6700,
              "end_ms": 6860,
              "pieces": [
                " do"
              ]
            },
            {
              "text": " for",
              "start_ms": 6860,
              "end_ms": 7340,
              "pieces": [
                " for"
              ]
            },
            {
              "text": " you",
              "start_ms": 7340,
              "end_ms": 7520,
              "pieces": [
                " you"
              ]
            },
            {
              "text": " ask",
              "start_ms": 8190,
              "end_ms": 8470,
              "pieces": [
                " ask"
              ]
            },
            {
              "text": " what",
              "start_ms": 8630,
              "end_ms": 8750,
              "pieces": [
                " what"
              ]
            },
            {
              "text": " you",
              "start_ms": 8910,
              "end_ms": 9090,
              "pieces": [
                " you"
              ]
            },
            {
              "text": " can",
              "start_ms": 9090,
              "end_ms": 9290,
              "pieces": [
                " can"
              ]
            },
            {
              "text": " do",
              "start_ms": 9290,
              "end_ms": 9510,
              "pieces": [
                " do"
              ]
            },
            {
              "text": " for",
              "start_ms": 9510,
              "end_ms": 9730,
              "pieces": [
                " for"
              ]
            },
            {
              "text": " your",
              "start_ms": 9730,
              "end_ms": 9970,
              "pieces": [
                " your"
              ]
            },
            {
              "text": " country.",
              "start_ms": 9970,
              "end_ms": 10600,
              "pieces": [
                " country",
                "."
              ]
            },
            {
              "text": " And",
              "start_ms": 16350,
              "end_ms": 16450,
              "pieces": [
                " And"
              ]
            },
            {
              "text": " so",
              "start_ms": 16610,
              "end_ms": 16810,
              "pieces": [
                " so"
              ]
            },
            {
              "text": " my",
              "start_ms": 16810,
              "end_ms": 17050,
              "pieces": [
                " my"
              ]
            },
            {
              "text": " fellow",
              "start_ms": 17050,
              "end_ms": 17770,
              "pieces": [
                " fellow"
              ]
            },
            {
              "text": " Americans",
              "start_ms": 17770,
              "end_ms": 19610,
              "pieces": [
                " Americans"
              ]
            },
            {
              "text": " ask",
              "start_ms": 19970,
              "end_ms": 20120,
              "pieces": [
                " ask"
              ]
            },
            {
              "text": " not",
              "start_ms": 20120,
              "end_ms": 20210,
              "pieces": [
                " not"
              ]
            },
            {
              "text": " what",
              "start_ms": 21380,
              "end_ms": 21680,
              "pieces": [
                " what"
              ]
            },
            {
              "text": " your",
              "start_ms": 21680,
              "end_ms": 22020,
              "pieces": [
                " your"
              ]
            },
            {
              "text": " country",
              "start_ms": 22150,
              "end_ms": 22710,
              "pieces": [
                " country"
              ]
            },
            {
              "text": " can",
              "start_ms": 22710,
              "end_ms": 22990,
              "pieces": [
                " can"
              ]
            },
            {
              "text": " do",
              "start_ms": 22990,
              "end_ms": 23170,
              "pieces": [
                " do"
              ]
            },
            {
              "text": " for",
              "start_ms": 23170,
              "end_ms": 23420,
              "pieces": [
                " for"
              ]
            },
            {
              "text": " you",
              "start_ms": 23440,
              "end_ms": 23600,
              "pieces": [
                " you"
              ]
            },
            {
              "text": " ask",
              "start_ms": 24160,
              "end_ms": 24300,
              "pieces": [
                " ask"
              ]
            },
            {
              "text": " what",
              "start_ms": 24300,
              "end_ms": 24600,
              "pieces": [
                " what"
              ]
            },
            {
              "text": " you",
              "start_ms": 24600,
              "end_ms": 24680,
              "pieces": [
                " you"
              ]
            },
            {
              "text": " can",
              "start_ms": 24840,
              "end_ms": 25040,
              "pieces": [
                " can"
              ]
            },
            {
              "text": " do",
              "start_ms": 25040,
              "end_ms": 25190,
              "pieces": [
                " do"
              ]
            },
            {
              "text": " for",
              "start_ms": 25190,
              "end_ms": 25410,
              "pieces": [
                " for"
              ]
            },
            {
              "text": " your",
              "start_ms": 25410,
              "end_ms": 25710,
              "pieces": [
                " your"
              ]
            },
            {
              "text": " country.",
              "start_ms": 25710,
              "end_ms": 26500,
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
              "point_cs": 12
            },
            {
              "text": " so",
              "point_cs": 76
            },
            {
              "text": " my",
              "point_cs": 104
            },
            {
              "text": " fellow",
              "point_cs": 138
            },
            {
              "text": " Americans",
              "point_cs": 192
            },
            {
              "text": " ask",
              "point_cs": 266
            },
            {
              "text": " not",
              "point_cs": 320
            },
            {
              "text": " what",
              "point_cs": 374
            },
            {
              "text": " your",
              "point_cs": 402
            },
            {
              "text": " country",
              "point_cs": 444
            },
            {
              "text": " can",
              "point_cs": 474
            },
            {
              "text": " do",
              "point_cs": 500
            },
            {
              "text": " for",
              "point_cs": 526
            },
            {
              "text": " you",
              "point_cs": 596
            },
            {
              "text": " ask",
              "point_cs": 632
            },
            {
              "text": " what",
              "point_cs": 670
            },
            {
              "text": " you",
              "point_cs": 694
            },
            {
              "text": " can",
              "point_cs": 716
            },
            {
              "text": " do",
              "point_cs": 742
            },
            {
              "text": " for",
              "point_cs": 760
            },
            {
              "text": " your",
              "point_cs": 778
            },
            {
              "text": " country",
              "point_cs": 830
            },
            {
              "text": ".",
              "point_cs": 866
            },
            {
              "text": " And",
              "point_cs": 892
            },
            {
              "text": " so",
              "point_cs": 922
            },
            {
              "text": " my",
              "point_cs": 950
            },
            {
              "text": " fellow",
              "point_cs": 984
            },
            {
              "text": " Americans",
              "point_cs": 1032
            },
            {
              "text": " ask",
              "point_cs": 1110
            },
            {
              "text": " not",
              "point_cs": 1164
            },
            {
              "text": " what",
              "point_cs": 1216
            },
            {
              "text": " your",
              "point_cs": 1242
            },
            {
              "text": " country",
              "point_cs": 1290
            },
            {
              "text": " can",
              "point_cs": 1320
            },
            {
              "text": " do",
              "point_cs": 1344
            },
            {
              "text": " for",
              "point_cs": 1368
            },
            {
              "text": " you",
              "point_cs": 1426
            },
            {
              "text": " ask",
              "point_cs": 1476
            },
            {
              "text": " what",
              "point_cs": 1514
            },
            {
              "text": " you",
              "point_cs": 1538
            },
            {
              "text": " can",
              "point_cs": 1556
            },
            {
              "text": " do",
              "point_cs": 1586
            },
            {
              "text": " for",
              "point_cs": 1602
            },
            {
              "text": " your",
              "point_cs": 1626
            },
            {
              "text": " country",
              "point_cs": 1662
            },
            {
              "text": ".",
              "point_cs": 1662
            }
          ],
          "command": [
            "/tmp/atrain-whisper-a/.whisper-cli-patched",
            "-m",
            "/tmp/atrain-whisper-a/.ggml-tiny.bin",
            "-f",
            "/tmp/atrain-whisper-a-cpu-results/audio/internal.wav",
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
            "/tmp/atrain-whisper-a-cpu-results/patched-dtw-vad-internal",
            "--vad",
            "-vm",
            "/tmp/atrain-whisper-a/.ggml-silero-v5.1.2.bin",
            "--dtw",
            "tiny"
          ],
          "wall_s": 1.0665041469910648,
          "status": "passed"
        },
        "boundary": {
          "text": " And so my fellow Americans ask not what your country can do for you ask what you can do for your country.",
          "words": [
            {
              "text": " And",
              "start_ms": 25330,
              "end_ms": 25530,
              "pieces": [
                " And"
              ]
            },
            {
              "text": " so",
              "start_ms": 25680,
              "end_ms": 25760,
              "pieces": [
                " so"
              ]
            },
            {
              "text": " my",
              "start_ms": 25760,
              "end_ms": 25940,
              "pieces": [
                " my"
              ]
            },
            {
              "text": " fellow",
              "start_ms": 25940,
              "end_ms": 26490,
              "pieces": [
                " fellow"
              ]
            },
            {
              "text": " Americans",
              "start_ms": 26490,
              "end_ms": 27100,
              "pieces": [
                " Americans"
              ]
            },
            {
              "text": " ask",
              "start_ms": 28290,
              "end_ms": 28650,
              "pieces": [
                " ask"
              ]
            },
            {
              "text": " not",
              "start_ms": 29010,
              "end_ms": 29280,
              "pieces": [
                " not"
              ]
            },
            {
              "text": " what",
              "start_ms": 30410,
              "end_ms": 30570,
              "pieces": [
                " what"
              ]
            },
            {
              "text": " your",
              "start_ms": 30650,
              "end_ms": 30830,
              "pieces": [
                " your"
              ]
            },
            {
              "text": " country",
              "start_ms": 30970,
              "end_ms": 31380,
              "pieces": [
                " country"
              ]
            },
            {
              "text": " can",
              "start_ms": 31380,
              "end_ms": 31650,
              "pieces": [
                " can"
              ]
            },
            {
              "text": " do",
              "start_ms": 31700,
              "end_ms": 31900,
              "pieces": [
                " do"
              ]
            },
            {
              "text": " for",
              "start_ms": 32010,
              "end_ms": 32290,
              "pieces": [
                " for"
              ]
            },
            {
              "text": " you",
              "start_ms": 32290,
              "end_ms": 32500,
              "pieces": [
                " you"
              ]
            },
            {
              "text": " ask",
              "start_ms": 33190,
              "end_ms": 33480,
              "pieces": [
                " ask"
              ]
            },
            {
              "text": " what",
              "start_ms": 33640,
              "end_ms": 33750,
              "pieces": [
                " what"
              ]
            },
            {
              "text": " you",
              "start_ms": 33910,
              "end_ms": 34060,
              "pieces": [
                " you"
              ]
            },
            {
              "text": " can",
              "start_ms": 34060,
              "end_ms": 34300,
              "pieces": [
                " can"
              ]
            },
            {
              "text": " do",
              "start_ms": 34300,
              "end_ms": 34520,
              "pieces": [
                " do"
              ]
            },
            {
              "text": " for",
              "start_ms": 34520,
              "end_ms": 34740,
              "pieces": [
                " for"
              ]
            },
            {
              "text": " your",
              "start_ms": 34740,
              "end_ms": 34980,
              "pieces": [
                " your"
              ]
            },
            {
              "text": " country.",
              "start_ms": 34980,
              "end_ms": 35500,
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
              "point_cs": 20
            },
            {
              "text": " so",
              "point_cs": 74
            },
            {
              "text": " my",
              "point_cs": 102
            },
            {
              "text": " fellow",
              "point_cs": 136
            },
            {
              "text": " Americans",
              "point_cs": 190
            },
            {
              "text": " ask",
              "point_cs": 262
            },
            {
              "text": " not",
              "point_cs": 322
            },
            {
              "text": " what",
              "point_cs": 368
            },
            {
              "text": " your",
              "point_cs": 396
            },
            {
              "text": " country",
              "point_cs": 440
            },
            {
              "text": " can",
              "point_cs": 470
            },
            {
              "text": " do",
              "point_cs": 494
            },
            {
              "text": " for",
              "point_cs": 522
            },
            {
              "text": " you",
              "point_cs": 580
            },
            {
              "text": " ask",
              "point_cs": 632
            },
            {
              "text": " what",
              "point_cs": 668
            },
            {
              "text": " you",
              "point_cs": 692
            },
            {
              "text": " can",
              "point_cs": 712
            },
            {
              "text": " do",
              "point_cs": 740
            },
            {
              "text": " for",
              "point_cs": 758
            },
            {
              "text": " your",
              "point_cs": 780
            },
            {
              "text": " country",
              "point_cs": 818
            },
            {
              "text": ".",
              "point_cs": 818
            }
          ],
          "command": [
            "/tmp/atrain-whisper-a/.whisper-cli-patched",
            "-m",
            "/tmp/atrain-whisper-a/.ggml-tiny.bin",
            "-f",
            "/tmp/atrain-whisper-a-cpu-results/audio/boundary.wav",
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
            "/tmp/atrain-whisper-a-cpu-results/patched-dtw-vad-boundary",
            "--vad",
            "-vm",
            "/tmp/atrain-whisper-a/.ggml-silero-v5.1.2.bin",
            "--dtw",
            "tiny"
          ],
          "wall_s": 0.8157294270058628,
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
            "/tmp/atrain-whisper-a/.ggml-tiny.bin",
            "-f",
            "/tmp/atrain-whisper-a-cpu-results/audio/silence.wav",
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
            "/tmp/atrain-whisper-a-cpu-results/patched-dtw-vad-silence",
            "--vad",
            "-vm",
            "/tmp/atrain-whisper-a/.ggml-silero-v5.1.2.bin",
            "--dtw",
            "tiny"
          ],
          "wall_s": 0.16463689500233158,
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
            "/tmp/atrain-whisper-a/.ggml-tiny.bin",
            "-f",
            "/tmp/atrain-whisper-a-cpu-results/audio/noise.wav",
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
            "/tmp/atrain-whisper-a-cpu-results/patched-dtw-vad-noise",
            "--vad",
            "-vm",
            "/tmp/atrain-whisper-a/.ggml-silero-v5.1.2.bin",
            "--dtw",
            "tiny"
          ],
          "wall_s": 0.16480968399264384,
          "status": "passed"
        },
        "german": {
          "text": "",
          "words": [],
          "problems": [
            "speech fixture returned no timed words"
          ],
          "dtw_points": [],
          "command": [
            "/tmp/atrain-whisper-a/.whisper-cli-patched",
            "-m",
            "/tmp/atrain-whisper-a/.ggml-tiny.bin",
            "-f",
            "/tmp/atrain-whisper-a-cpu-results/audio/german.wav",
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
            "/tmp/atrain-whisper-a-cpu-results/patched-dtw-vad-german",
            "--vad",
            "-vm",
            "/tmp/atrain-whisper-a/.ggml-silero-v5.1.2.bin",
            "--dtw",
            "tiny"
          ],
          "wall_s": 0.16493086400441825,
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
              "point_cs": 74
            }
          ],
          "command": [
            "/tmp/atrain-whisper-a/.whisper-cli-patched",
            "-m",
            "/tmp/atrain-whisper-a/.ggml-tiny.bin",
            "-f",
            "/tmp/atrain-whisper-a-cpu-results/audio/japanese.wav",
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
            "/tmp/atrain-whisper-a-cpu-results/patched-dtw-vad-japanese",
            "--vad",
            "-vm",
            "/tmp/atrain-whisper-a/.ggml-silero-v5.1.2.bin",
            "--dtw",
            "tiny"
          ],
          "wall_s": 0.6157702409982448,
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
            10,
            0,
            20,
            20,
            20,
            20,
            20,
            20,
            0,
            0,
            0,
            0,
            0,
            0,
            40,
            130,
            0,
            0,
            10,
            90,
            40,
            20,
            60,
            150,
            100,
            100,
            20,
            0,
            0,
            10,
            0,
            0,
            60,
            60,
            80,
            80,
            40,
            40,
            0,
            0,
            80,
            80,
            40
          ],
          "max_boundary_error_ms": 150,
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
            0,
            0,
            10,
            10,
            30,
            30,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            10,
            0,
            0,
            40,
            120,
            30,
            0,
            40,
            150,
            40,
            40,
            0,
            0,
            0,
            10,
            0,
            0,
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
            10
          ],
          "max_boundary_error_ms": 150,
          "status": "failed"
        },
        "internal-first": {
          "tolerance_ms": 50,
          "matched_words": 22,
          "unmatched_reference_words": 0,
          "unmatched_candidate_words": 0,
          "boundary_errors_ms": [
            0,
            0,
            0,
            20,
            20,
            30,
            30,
            50,
            50,
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
            90,
            90,
            20,
            0,
            10,
            0,
            0,
            0,
            40,
            40,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            110
          ],
          "max_boundary_error_ms": 110,
          "status": "failed"
        },
        "internal-second": {
          "tolerance_ms": 50,
          "matched_words": 22,
          "unmatched_reference_words": 0,
          "unmatched_candidate_words": 0,
          "boundary_errors_ms": [
            20,
            90,
            70,
            50,
            50,
            100,
            100,
            250,
            250,
            1510,
            680,
            470,
            110,
            70,
            30,
            110,
            20,
            190,
            180,
            290,
            210,
            310,
            290,
            310,
            310,
            170,
            190,
            100,
            30,
            180,
            330,
            150,
            310,
            370,
            210,
            250,
            250,
            320,
            320,
            320,
            320,
            260,
            260,
            10
          ],
          "max_boundary_error_ms": 1510,
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

## german-left-diagnostic.json

Original file SHA-256: `76562039921a739569a62fa4d340b116973f1049fab2e45c9e7668e5b3c4fa91`

<details>
<summary>Complete recorded result</summary>

```json
{
	"systeminfo": "WHISPER : VITISAI = 0 | COREML = 0 | OPENVINO = 0 | CPU : SSE3 = 1 | SSSE3 = 1 | AVX = 1 | AVX2 = 1 | F16C = 1 | FMA = 1 | BMI2 = 1 | OPENMP = 1 | REPACK = 1 | ",
	"model": {
		"type": "tiny",
		"multilingual": true,
		"vocab": 51865,
		"audio": {
			"ctx": 1500,
			"state": 384,
			"head": 6,
			"layer": 4
		},
		"text": {
			"ctx": 448,
			"state": 384,
			"head": 6,
			"layer": 4
		},
		"mels": 80,
		"ftype": 1
	},
	"params": {
		"model": "/tmp/atrain-whisper-a/.ggml-tiny.bin",
		"language": "de",
		"translate": false
	},
	"result": {
		"language": "de"
	},
	"transcription": [
		{
			"timestamps": {
				"from": "00:00:00,710",
				"to": "00:00:07,900"
			},
			"offsets": {
				"from": 710,
				"to": 7900
			},
			"text": " Hierro, Kapitelacht, flach, halten, flach halten.",
			"tokens": [
				{
					"text": "[_BEG_]",
					"timestamps": {
						"from": "00:00:00,710",
						"to": "00:00:00,720"
					},
					"offsets": {
						"from": 710,
						"to": 720
					},
					"id": 50364,
					"p": 0.984346,
					"t_dtw": -1
				},
				{
					"text": " Hier",
					"timestamps": {
						"from": "00:00:00,750",
						"to": "00:00:01,090"
					},
					"offsets": {
						"from": 750,
						"to": 1090
					},
					"id": 10886,
					"p": 0.122684,
					"t_dtw": -1
				},
				{
					"text": "ro",
					"timestamps": {
						"from": "00:00:01,090",
						"to": "00:00:01,170"
					},
					"offsets": {
						"from": 1090,
						"to": 1170
					},
					"id": 340,
					"p": 0.536777,
					"t_dtw": -1
				},
				{
					"text": ",",
					"timestamps": {
						"from": "00:00:01,990",
						"to": "00:00:02,010"
					},
					"offsets": {
						"from": 1990,
						"to": 2010
					},
					"id": 11,
					"p": 0.486141,
					"t_dtw": -1
				},
				{
					"text": " Kap",
					"timestamps": {
						"from": "00:00:02,010",
						"to": "00:00:02,290"
					},
					"offsets": {
						"from": 2010,
						"to": 2290
					},
					"id": 21216,
					"p": 0.617088,
					"t_dtw": -1
				},
				{
					"text": "itel",
					"timestamps": {
						"from": "00:00:02,290",
						"to": "00:00:02,570"
					},
					"offsets": {
						"from": 2290,
						"to": 2570
					},
					"id": 38906,
					"p": 0.854188,
					"t_dtw": -1
				},
				{
					"text": "acht",
					"timestamps": {
						"from": "00:00:04,420",
						"to": "00:00:04,620"
					},
					"offsets": {
						"from": 4420,
						"to": 4620
					},
					"id": 3589,
					"p": 0.585773,
					"t_dtw": -1
				},
				{
					"text": ",",
					"timestamps": {
						"from": "00:00:04,620",
						"to": "00:00:04,820"
					},
					"offsets": {
						"from": 4620,
						"to": 4820
					},
					"id": 11,
					"p": 0.891997,
					"t_dtw": -1
				},
				{
					"text": " fl",
					"timestamps": {
						"from": "00:00:04,820",
						"to": "00:00:05,000"
					},
					"offsets": {
						"from": 4820,
						"to": 5000
					},
					"id": 932,
					"p": 0.345782,
					"t_dtw": -1
				},
				{
					"text": "ach",
					"timestamps": {
						"from": "00:00:05,010",
						"to": "00:00:05,190"
					},
					"offsets": {
						"from": 5010,
						"to": 5190
					},
					"id": 608,
					"p": 0.935528,
					"t_dtw": -1
				},
				{
					"text": ",",
					"timestamps": {
						"from": "00:00:05,290",
						"to": "00:00:05,450"
					},
					"offsets": {
						"from": 5290,
						"to": 5450
					},
					"id": 11,
					"p": 0.545878,
					"t_dtw": -1
				},
				{
					"text": " hal",
					"timestamps": {
						"from": "00:00:05,450",
						"to": "00:00:05,570"
					},
					"offsets": {
						"from": 5450,
						"to": 5570
					},
					"id": 7523,
					"p": 0.618921,
					"t_dtw": -1
				},
				{
					"text": "ten",
					"timestamps": {
						"from": "00:00:06,470",
						"to": "00:00:06,530"
					},
					"offsets": {
						"from": 6470,
						"to": 6530
					},
					"id": 1147,
					"p": 0.857003,
					"t_dtw": -1
				},
				{
					"text": ",",
					"timestamps": {
						"from": "00:00:06,530",
						"to": "00:00:06,710"
					},
					"offsets": {
						"from": 6530,
						"to": 6710
					},
					"id": 11,
					"p": 0.938428,
					"t_dtw": -1
				},
				{
					"text": " fl",
					"timestamps": {
						"from": "00:00:06,710",
						"to": "00:00:06,870"
					},
					"offsets": {
						"from": 6710,
						"to": 6870
					},
					"id": 932,
					"p": 0.951321,
					"t_dtw": -1
				},
				{
					"text": "ach",
					"timestamps": {
						"from": "00:00:06,980",
						"to": "00:00:07,160"
					},
					"offsets": {
						"from": 6980,
						"to": 7160
					},
					"id": 608,
					"p": 0.945777,
					"t_dtw": -1
				},
				{
					"text": " halten",
					"timestamps": {
						"from": "00:00:07,160",
						"to": "00:00:07,600"
					},
					"offsets": {
						"from": 7160,
						"to": 7600
					},
					"id": 27184,
					"p": 0.571397,
					"t_dtw": -1
				},
				{
					"text": ".",
					"timestamps": {
						"from": "00:00:07,750",
						"to": "00:00:07,900"
					},
					"offsets": {
						"from": 7750,
						"to": 7900
					},
					"id": 13,
					"p": 0.768618,
					"t_dtw": -1
				},
				{
					"text": "[_TT_227]",
					"timestamps": {
						"from": "00:00:07,900",
						"to": "00:00:07,910"
					},
					"offsets": {
						"from": 7900,
						"to": 7910
					},
					"id": 50591,
					"p": 0.0110748,
					"t_dtw": -1
				}
			]
		},
		{
			"timestamps": {
				"from": "00:00:07,900",
				"to": "00:00:17,450"
			},
			"offsets": {
				"from": 7900,
				"to": 17450
			},
			"text": " Die Junge, du wirst es nicht packen, das ist doch vergesse, vergesse seinfach, doch, das hast du gut gemacht.",
			"tokens": [
				{
					"text": " Die",
					"timestamps": {
						"from": "00:00:07,940",
						"to": "00:00:08,070"
					},
					"offsets": {
						"from": 7940,
						"to": 8070
					},
					"id": 3229,
					"p": 0.680708,
					"t_dtw": -1
				},
				{
					"text": " Jun",
					"timestamps": {
						"from": "00:00:08,070",
						"to": "00:00:08,130"
					},
					"offsets": {
						"from": 8070,
						"to": 8130
					},
					"id": 8492,
					"p": 0.442706,
					"t_dtw": -1
				},
				{
					"text": "ge",
					"timestamps": {
						"from": "00:00:08,130",
						"to": "00:00:09,260"
					},
					"offsets": {
						"from": 8130,
						"to": 9260
					},
					"id": 432,
					"p": 0.996841,
					"t_dtw": -1
				},
				{
					"text": ",",
					"timestamps": {
						"from": "00:00:09,260",
						"to": "00:00:09,280"
					},
					"offsets": {
						"from": 9260,
						"to": 9280
					},
					"id": 11,
					"p": 0.465669,
					"t_dtw": -1
				},
				{
					"text": " du",
					"timestamps": {
						"from": "00:00:09,490",
						"to": "00:00:09,500"
					},
					"offsets": {
						"from": 9490,
						"to": 9500
					},
					"id": 1581,
					"p": 0.892636,
					"t_dtw": -1
				},
				{
					"text": " w",
					"timestamps": {
						"from": "00:00:09,540",
						"to": "00:00:09,550"
					},
					"offsets": {
						"from": 9540,
						"to": 9550
					},
					"id": 261,
					"p": 0.468753,
					"t_dtw": -1
				},
				{
					"text": "irst",
					"timestamps": {
						"from": "00:00:09,550",
						"to": "00:00:09,770"
					},
					"offsets": {
						"from": 9550,
						"to": 9770
					},
					"id": 653,
					"p": 0.986056,
					"t_dtw": -1
				},
				{
					"text": " es",
					"timestamps": {
						"from": "00:00:09,770",
						"to": "00:00:09,880"
					},
					"offsets": {
						"from": 9770,
						"to": 9880
					},
					"id": 785,
					"p": 0.909835,
					"t_dtw": -1
				},
				{
					"text": " nicht",
					"timestamps": {
						"from": "00:00:09,880",
						"to": "00:00:10,160"
					},
					"offsets": {
						"from": 9880,
						"to": 10160
					},
					"id": 1979,
					"p": 0.99689,
					"t_dtw": -1
				},
				{
					"text": " pack",
					"timestamps": {
						"from": "00:00:10,160",
						"to": "00:00:10,290"
					},
					"offsets": {
						"from": 10160,
						"to": 10290
					},
					"id": 2844,
					"p": 0.841772,
					"t_dtw": -1
				},
				{
					"text": "en",
					"timestamps": {
						"from": "00:00:10,420",
						"to": "00:00:10,510"
					},
					"offsets": {
						"from": 10420,
						"to": 10510
					},
					"id": 268,
					"p": 0.991543,
					"t_dtw": -1
				},
				{
					"text": ",",
					"timestamps": {
						"from": "00:00:10,510",
						"to": "00:00:10,820"
					},
					"offsets": {
						"from": 10510,
						"to": 10820
					},
					"id": 11,
					"p": 0.0948045,
					"t_dtw": -1
				},
				{
					"text": " das",
					"timestamps": {
						"from": "00:00:10,820",
						"to": "00:00:11,080"
					},
					"offsets": {
						"from": 10820,
						"to": 11080
					},
					"id": 1482,
					"p": 0.930341,
					"t_dtw": -1
				},
				{
					"text": " ist",
					"timestamps": {
						"from": "00:00:11,080",
						"to": "00:00:11,380"
					},
					"offsets": {
						"from": 11080,
						"to": 11380
					},
					"id": 1418,
					"p": 0.997798,
					"t_dtw": -1
				},
				{
					"text": " doch",
					"timestamps": {
						"from": "00:00:11,380",
						"to": "00:00:11,630"
					},
					"offsets": {
						"from": 11380,
						"to": 11630
					},
					"id": 9243,
					"p": 0.99379,
					"t_dtw": -1
				},
				{
					"text": " ver",
					"timestamps": {
						"from": "00:00:11,990",
						"to": "00:00:12,080"
					},
					"offsets": {
						"from": 11990,
						"to": 12080
					},
					"id": 1306,
					"p": 0.216054,
					"t_dtw": -1
				},
				{
					"text": "ges",
					"timestamps": {
						"from": "00:00:12,080",
						"to": "00:00:12,320"
					},
					"offsets": {
						"from": 12080,
						"to": 12320
					},
					"id": 2880,
					"p": 0.893958,
					"t_dtw": -1
				},
				{
					"text": "se",
					"timestamps": {
						"from": "00:00:12,370",
						"to": "00:00:12,580"
					},
					"offsets": {
						"from": 12370,
						"to": 12580
					},
					"id": 405,
					"p": 0.862969,
					"t_dtw": -1
				},
				{
					"text": ",",
					"timestamps": {
						"from": "00:00:12,580",
						"to": "00:00:12,770"
					},
					"offsets": {
						"from": 12580,
						"to": 12770
					},
					"id": 11,
					"p": 0.496747,
					"t_dtw": -1
				},
				{
					"text": " ver",
					"timestamps": {
						"from": "00:00:12,890",
						"to": "00:00:13,070"
					},
					"offsets": {
						"from": 12890,
						"to": 13070
					},
					"id": 1306,
					"p": 0.629741,
					"t_dtw": -1
				},
				{
					"text": "ges",
					"timestamps": {
						"from": "00:00:13,070",
						"to": "00:00:13,120"
					},
					"offsets": {
						"from": 13070,
						"to": 13120
					},
					"id": 2880,
					"p": 0.987916,
					"t_dtw": -1
				},
				{
					"text": "se",
					"timestamps": {
						"from": "00:00:13,280",
						"to": "00:00:13,520"
					},
					"offsets": {
						"from": 13280,
						"to": 13520
					},
					"id": 405,
					"p": 0.999161,
					"t_dtw": -1
				},
				{
					"text": " sein",
					"timestamps": {
						"from": "00:00:13,860",
						"to": "00:00:13,890"
					},
					"offsets": {
						"from": 13860,
						"to": 13890
					},
					"id": 6195,
					"p": 0.643215,
					"t_dtw": -1
				},
				{
					"text": "fach",
					"timestamps": {
						"from": "00:00:13,890",
						"to": "00:00:14,250"
					},
					"offsets": {
						"from": 13890,
						"to": 14250
					},
					"id": 6749,
					"p": 0.858872,
					"t_dtw": -1
				},
				{
					"text": ",",
					"timestamps": {
						"from": "00:00:14,270",
						"to": "00:00:14,750"
					},
					"offsets": {
						"from": 14270,
						"to": 14750
					},
					"id": 11,
					"p": 0.303014,
					"t_dtw": -1
				},
				{
					"text": " doch",
					"timestamps": {
						"from": "00:00:14,750",
						"to": "00:00:14,990"
					},
					"offsets": {
						"from": 14750,
						"to": 14990
					},
					"id": 9243,
					"p": 0.527758,
					"t_dtw": -1
				},
				{
					"text": ",",
					"timestamps": {
						"from": "00:00:15,060",
						"to": "00:00:15,290"
					},
					"offsets": {
						"from": 15060,
						"to": 15290
					},
					"id": 11,
					"p": 0.45402,
					"t_dtw": -1
				},
				{
					"text": " das",
					"timestamps": {
						"from": "00:00:16,340",
						"to": "00:00:16,350"
					},
					"offsets": {
						"from": 16340,
						"to": 16350
					},
					"id": 1482,
					"p": 0.465663,
					"t_dtw": -1
				},
				{
					"text": " hast",
					"timestamps": {
						"from": "00:00:16,360",
						"to": "00:00:16,450"
					},
					"offsets": {
						"from": 16360,
						"to": 16450
					},
					"id": 6581,
					"p": 0.186023,
					"t_dtw": -1
				},
				{
					"text": " du",
					"timestamps": {
						"from": "00:00:16,450",
						"to": "00:00:16,520"
					},
					"offsets": {
						"from": 16450,
						"to": 16520
					},
					"id": 1581,
					"p": 0.936422,
					"t_dtw": -1
				},
				{
					"text": " gut",
					"timestamps": {
						"from": "00:00:16,520",
						"to": "00:00:16,640"
					},
					"offsets": {
						"from": 16520,
						"to": 16640
					},
					"id": 5228,
					"p": 0.49501,
					"t_dtw": -1
				},
				{
					"text": " gemacht",
					"timestamps": {
						"from": "00:00:16,710",
						"to": "00:00:17,060"
					},
					"offsets": {
						"from": 16710,
						"to": 17060
					},
					"id": 12293,
					"p": 0.95751,
					"t_dtw": -1
				},
				{
					"text": ".",
					"timestamps": {
						"from": "00:00:17,060",
						"to": "00:00:17,450"
					},
					"offsets": {
						"from": 17060,
						"to": 17450
					},
					"id": 13,
					"p": 0.857888,
					"t_dtw": -1
				},
				{
					"text": "[_TT_602]",
					"timestamps": {
						"from": "00:00:17,450",
						"to": "00:00:17,460"
					},
					"offsets": {
						"from": 17450,
						"to": 17460
					},
					"id": 50966,
					"p": 0.0415007,
					"t_dtw": -1
				}
			]
		},
		{
			"timestamps": {
				"from": "00:00:17,450",
				"to": "00:00:23,590"
			},
			"offsets": {
				"from": 17450,
				"to": 23590
			},
			"text": " Nein, so nicht, netz, netz, hat berührt, hat berührt.",
			"tokens": [
				{
					"text": " Nein",
					"timestamps": {
						"from": "00:00:17,490",
						"to": "00:00:17,850"
					},
					"offsets": {
						"from": 17490,
						"to": 17850
					},
					"id": 18878,
					"p": 0.875856,
					"t_dtw": -1
				},
				{
					"text": ",",
					"timestamps": {
						"from": "00:00:18,150",
						"to": "00:00:18,160"
					},
					"offsets": {
						"from": 18150,
						"to": 18160
					},
					"id": 11,
					"p": 0.72276,
					"t_dtw": -1
				},
				{
					"text": " so",
					"timestamps": {
						"from": "00:00:18,180",
						"to": "00:00:18,380"
					},
					"offsets": {
						"from": 18180,
						"to": 18380
					},
					"id": 370,
					"p": 0.966709,
					"t_dtw": -1
				},
				{
					"text": " nicht",
					"timestamps": {
						"from": "00:00:18,380",
						"to": "00:00:18,770"
					},
					"offsets": {
						"from": 18380,
						"to": 18770
					},
					"id": 1979,
					"p": 0.838731,
					"t_dtw": -1
				},
				{
					"text": ",",
					"timestamps": {
						"from": "00:00:19,040",
						"to": "00:00:19,200"
					},
					"offsets": {
						"from": 19040,
						"to": 19200
					},
					"id": 11,
					"p": 0.471159,
					"t_dtw": -1
				},
				{
					"text": " net",
					"timestamps": {
						"from": "00:00:19,200",
						"to": "00:00:19,550"
					},
					"offsets": {
						"from": 19200,
						"to": 19550
					},
					"id": 2533,
					"p": 0.217935,
					"t_dtw": -1
				},
				{
					"text": "z",
					"timestamps": {
						"from": "00:00:19,550",
						"to": "00:00:19,660"
					},
					"offsets": {
						"from": 19550,
						"to": 19660
					},
					"id": 89,
					"p": 0.971341,
					"t_dtw": -1
				},
				{
					"text": ",",
					"timestamps": {
						"from": "00:00:19,660",
						"to": "00:00:19,820"
					},
					"offsets": {
						"from": 19660,
						"to": 19820
					},
					"id": 11,
					"p": 0.896425,
					"t_dtw": -1
				},
				{
					"text": " net",
					"timestamps": {
						"from": "00:00:19,920",
						"to": "00:00:20,200"
					},
					"offsets": {
						"from": 19920,
						"to": 20200
					},
					"id": 2533,
					"p": 0.905281,
					"t_dtw": -1
				},
				{
					"text": "z",
					"timestamps": {
						"from": "00:00:20,350",
						"to": "00:00:20,360"
					},
					"offsets": {
						"from": 20350,
						"to": 20360
					},
					"id": 89,
					"p": 0.9964,
					"t_dtw": -1
				},
				{
					"text": ",",
					"timestamps": {
						"from": "00:00:20,520",
						"to": "00:00:20,580"
					},
					"offsets": {
						"from": 20520,
						"to": 20580
					},
					"id": 11,
					"p": 0.392199,
					"t_dtw": -1
				},
				{
					"text": " hat",
					"timestamps": {
						"from": "00:00:20,580",
						"to": "00:00:20,910"
					},
					"offsets": {
						"from": 20580,
						"to": 20910
					},
					"id": 2385,
					"p": 0.944244,
					"t_dtw": -1
				},
				{
					"text": " ber",
					"timestamps": {
						"from": "00:00:20,910",
						"to": "00:00:21,280"
					},
					"offsets": {
						"from": 20910,
						"to": 21280
					},
					"id": 5948,
					"p": 0.838323,
					"t_dtw": -1
				},
				{
					"text": "ührt",
					"timestamps": {
						"from": "00:00:21,280",
						"to": "00:00:21,690"
					},
					"offsets": {
						"from": 21280,
						"to": 21690
					},
					"id": 19647,
					"p": 0.987321,
					"t_dtw": -1
				},
				{
					"text": ",",
					"timestamps": {
						"from": "00:00:21,800",
						"to": "00:00:21,980"
					},
					"offsets": {
						"from": 21800,
						"to": 21980
					},
					"id": 11,
					"p": 0.864016,
					"t_dtw": -1
				},
				{
					"text": " hat",
					"timestamps": {
						"from": "00:00:21,980",
						"to": "00:00:22,310"
					},
					"offsets": {
						"from": 21980,
						"to": 22310
					},
					"id": 2385,
					"p": 0.984649,
					"t_dtw": -1
				},
				{
					"text": " ber",
					"timestamps": {
						"from": "00:00:22,440",
						"to": "00:00:22,680"
					},
					"offsets": {
						"from": 22440,
						"to": 22680
					},
					"id": 5948,
					"p": 0.989763,
					"t_dtw": -1
				},
				{
					"text": "ührt",
					"timestamps": {
						"from": "00:00:22,680",
						"to": "00:00:23,120"
					},
					"offsets": {
						"from": 22680,
						"to": 23120
					},
					"id": 19647,
					"p": 0.998588,
					"t_dtw": -1
				},
				{
					"text": ".",
					"timestamps": {
						"from": "00:00:23,160",
						"to": "00:00:23,590"
					},
					"offsets": {
						"from": 23160,
						"to": 23590
					},
					"id": 13,
					"p": 0.370676,
					"t_dtw": -1
				},
				{
					"text": "[_TT_909]",
					"timestamps": {
						"from": "00:00:23,590",
						"to": "00:00:23,600"
					},
					"offsets": {
						"from": 23590,
						"to": 23600
					},
					"id": 51273,
					"p": 0.0204415,
					"t_dtw": -1
				}
			]
		},
		{
			"timestamps": {
				"from": "00:00:23,590",
				"to": "00:00:29,610"
			},
			"offsets": {
				"from": 23590,
				"to": 29610
			},
			"text": " Verges alles, was man die gesagt hat, den wirst du nicht packen, das gut.",
			"tokens": [
				{
					"text": " Ver",
					"timestamps": {
						"from": "00:00:23,610",
						"to": "00:00:24,230"
					},
					"offsets": {
						"from": 23610,
						"to": 24230
					},
					"id": 4281,
					"p": 0.448982,
					"t_dtw": -1
				},
				{
					"text": "ges",
					"timestamps": {
						"from": "00:00:24,280",
						"to": "00:00:24,410"
					},
					"offsets": {
						"from": 24280,
						"to": 24410
					},
					"id": 2880,
					"p": 0.981824,
					"t_dtw": -1
				},
				{
					"text": " alles",
					"timestamps": {
						"from": "00:00:24,740",
						"to": "00:00:24,850"
					},
					"offsets": {
						"from": 24740,
						"to": 24850
					},
					"id": 7874,
					"p": 0.847722,
					"t_dtw": -1
				},
				{
					"text": ",",
					"timestamps": {
						"from": "00:00:24,890",
						"to": "00:00:25,050"
					},
					"offsets": {
						"from": 24890,
						"to": 25050
					},
					"id": 11,
					"p": 0.785704,
					"t_dtw": -1
				},
				{
					"text": " was",
					"timestamps": {
						"from": "00:00:25,050",
						"to": "00:00:25,280"
					},
					"offsets": {
						"from": 25050,
						"to": 25280
					},
					"id": 390,
					"p": 0.992585,
					"t_dtw": -1
				},
				{
					"text": " man",
					"timestamps": {
						"from": "00:00:25,280",
						"to": "00:00:25,480"
					},
					"offsets": {
						"from": 25280,
						"to": 25480
					},
					"id": 587,
					"p": 0.976945,
					"t_dtw": -1
				},
				{
					"text": " die",
					"timestamps": {
						"from": "00:00:25,600",
						"to": "00:00:25,770"
					},
					"offsets": {
						"from": 25600,
						"to": 25770
					},
					"id": 978,
					"p": 0.54172,
					"t_dtw": -1
				},
				{
					"text": " gesagt",
					"timestamps": {
						"from": "00:00:25,770",
						"to": "00:00:26,260"
					},
					"offsets": {
						"from": 25770,
						"to": 26260
					},
					"id": 12260,
					"p": 0.985105,
					"t_dtw": -1
				},
				{
					"text": " hat",
					"timestamps": {
						"from": "00:00:26,260",
						"to": "00:00:26,500"
					},
					"offsets": {
						"from": 26260,
						"to": 26500
					},
					"id": 2385,
					"p": 0.995661,
					"t_dtw": -1
				},
				{
					"text": ",",
					"timestamps": {
						"from": "00:00:26,500",
						"to": "00:00:26,650"
					},
					"offsets": {
						"from": 26500,
						"to": 26650
					},
					"id": 11,
					"p": 0.664552,
					"t_dtw": -1
				},
				{
					"text": " den",
					"timestamps": {
						"from": "00:00:26,650",
						"to": "00:00:27,140"
					},
					"offsets": {
						"from": 26650,
						"to": 27140
					},
					"id": 1441,
					"p": 0.872404,
					"t_dtw": -1
				},
				{
					"text": " w",
					"timestamps": {
						"from": "00:00:27,190",
						"to": "00:00:27,250"
					},
					"offsets": {
						"from": 27190,
						"to": 27250
					},
					"id": 261,
					"p": 0.535264,
					"t_dtw": -1
				},
				{
					"text": "irst",
					"timestamps": {
						"from": "00:00:27,410",
						"to": "00:00:27,590"
					},
					"offsets": {
						"from": 27410,
						"to": 27590
					},
					"id": 653,
					"p": 0.977715,
					"t_dtw": -1
				},
				{
					"text": " du",
					"timestamps": {
						"from": "00:00:27,590",
						"to": "00:00:27,740"
					},
					"offsets": {
						"from": 27590,
						"to": 27740
					},
					"id": 1581,
					"p": 0.995,
					"t_dtw": -1
				},
				{
					"text": " nicht",
					"timestamps": {
						"from": "00:00:27,740",
						"to": "00:00:28,150"
					},
					"offsets": {
						"from": 27740,
						"to": 28150
					},
					"id": 1979,
					"p": 0.994556,
					"t_dtw": -1
				},
				{
					"text": " pack",
					"timestamps": {
						"from": "00:00:28,150",
						"to": "00:00:28,470"
					},
					"offsets": {
						"from": 28150,
						"to": 28470
					},
					"id": 2844,
					"p": 0.996573,
					"t_dtw": -1
				},
				{
					"text": "en",
					"timestamps": {
						"from": "00:00:28,470",
						"to": "00:00:28,540"
					},
					"offsets": {
						"from": 28470,
						"to": 28540
					},
					"id": 268,
					"p": 0.999468,
					"t_dtw": -1
				},
				{
					"text": ",",
					"timestamps": {
						"from": "00:00:28,570",
						"to": "00:00:29,170"
					},
					"offsets": {
						"from": 28570,
						"to": 29170
					},
					"id": 11,
					"p": 0.528537,
					"t_dtw": -1
				},
				{
					"text": " das",
					"timestamps": {
						"from": "00:00:29,170",
						"to": "00:00:29,310"
					},
					"offsets": {
						"from": 29170,
						"to": 29310
					},
					"id": 1482,
					"p": 0.390479,
					"t_dtw": -1
				},
				{
					"text": " gut",
					"timestamps": {
						"from": "00:00:29,310",
						"to": "00:00:29,450"
					},
					"offsets": {
						"from": 29310,
						"to": 29450
					},
					"id": 5228,
					"p": 0.595327,
					"t_dtw": -1
				},
				{
					"text": ".",
					"timestamps": {
						"from": "00:00:29,580",
						"to": "00:00:29,610"
					},
					"offsets": {
						"from": 29580,
						"to": 29610
					},
					"id": 13,
					"p": 0.852394,
					"t_dtw": -1
				},
				{
					"text": "[_TT_1160]",
					"timestamps": {
						"from": "00:00:29,610",
						"to": "00:00:29,620"
					},
					"offsets": {
						"from": 29610,
						"to": 29620
					},
					"id": 51524,
					"p": 0.113862,
					"t_dtw": -1
				}
			]
		}
	]
}
```

</details>
