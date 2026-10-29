# whisper.cpp: macOS CPU and Metal capability

[Apple hardware acceleration tests](../apple-hardware-acceleration-tests.md)

Archived on 23 October 2026. The JSON below preserves the complete aggregate
results and listed supporting diagnostics without altering values. Absolute
paths inside these historical records identify the original run environment.
Audio, model binaries and raw execution logs are not embedded. See the index
for interpretation, limitations and links to the original artifacts.

## result.json

Original file SHA-256: `bbf8403c6963e8eacbf7cefbc51789246c52870699ea624a71fdef7c85053b9d`

<details>
<summary>Complete recorded result</summary>

```json
{
  "source_revision": "d1be6fde11ac6e0407606b4e42fe72d34add8037",
  "model_url": "https://huggingface.co/ggerganov/whisper.cpp/resolve/5359861c739e955e79d9a303bcbc70fb988958b1/ggml-tiny.bin",
  "model_sha256": "be07e048e1e599ad46341c8d2a135645097a538221678b7acdd1b1919c6e1b21",
  "runner_label": "macos-15",
  "image_os": "macos15",
  "image_version": "20260907.0337.1",
  "runner_arch": "ARM64",
  "run_url": "https://github.com/JuergenFleiss/aTrain_fork/actions/runs/39921131494",
  "diagnostic_build": "Release; WHISPER_DEBUG; Metal embedded; Core ML OFF; target macOS 14",
  "os": {
    "exit_code": 0,
    "wall_seconds": 0.02126712500000849
  },
  "architecture": {
    "exit_code": 0,
    "wall_seconds": 0.009891166000016938
  },
  "cpu_memory": {
    "exit_code": 0,
    "wall_seconds": 0.008092417000000296
  },
  "xcode": {
    "exit_code": 0,
    "wall_seconds": 0.07150408399999719
  },
  "sdk": {
    "exit_code": 0,
    "wall_seconds": 0.45354891599998837
  },
  "compiler": {
    "exit_code": 0,
    "wall_seconds": 0.01840587500001334
  },
  "display": {
    "exit_code": 0,
    "wall_seconds": 0.2518498329999943
  },
  "metal_compile": {
    "exit_code": 0,
    "wall_seconds": 9.696084374999998
  },
  "metal_compute": {
    "exit_code": 0,
    "wall_seconds": 0.6298488330000112
  },
  "voices": {
    "exit_code": 0,
    "wall_seconds": 0.4469153750000032
  },
  "fixture": {
    "text": "The quick brown fox jumps over the lazy dog. This is a local transcription test.",
    "voice": "Samantha",
    "words_per_minute": 170,
    "format": "16000 Hz mono PCM16 WAV",
    "sha256": "6166be0c8657eff2a6344cfc8457d50c8f12c3b61915d6604e5b30dfdbd893c3",
    "purpose": "capability smoke only; generated voice may vary with runner image"
  },
  "helper_sha256": "9621b03d8c8177d0cacce1372daf55f0875c6b88e3ab575402fba67fe284ff22",
  "cpu": {
    "exit_code": 0,
    "wall_seconds": 20.99831766700001
  },
  "metal": {
    "exit_code": 0,
    "wall_seconds": 2.9558062079999843
  },
  "statuses": {
    "cpu": "passed",
    "metal": "passed",
    "metal_compute": "passed"
  }
}
```

</details>

## cpu.json

Original file SHA-256: `9d418addeca5a21246e905c5d996086c68fcbfaf5be9681f92e7f0c685498d7e`

<details>
<summary>Complete recorded result</summary>

```json
{
	"systeminfo": "WHISPER : VITISAI = 0 | COREML = 0 | OPENVINO = 0 | MTL : EMBED_LIBRARY = 1 | CPU : NEON = 1 | ARM_FMA = 1 | FP16_VA = 1 | DOTPROD = 1 | ACCELERATE = 1 | REPACK = 1 | ",
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
		"model": "/Users/runner/work/_temp/atrain-probe-hf/ggml-tiny.bin",
		"language": "en",
		"translate": false
	},
	"result": {
		"language": "en"
	},
	"transcription": [
		{
			"timestamps": {
				"from": "00:00:00,000",
				"to": "00:00:04,800"
			},
			"offsets": {
				"from": 0,
				"to": 4800
			},
			"text": " the quick brown fox jumps over the lazy dog, this is a local transcription test.",
			"tokens": [
				{
					"text": "[_BEG_]",
					"timestamps": {
						"from": "00:00:00,000",
						"to": "00:00:00,000"
					},
					"offsets": {
						"from": 0,
						"to": 0
					},
					"id": 50364,
					"p": 0.993235,
					"t_dtw": -1
				},
				{
					"text": " the",
					"timestamps": {
						"from": "00:00:00,010",
						"to": "00:00:00,220"
					},
					"offsets": {
						"from": 10,
						"to": 220
					},
					"id": 264,
					"p": 0.502436,
					"t_dtw": -1
				},
				{
					"text": " quick",
					"timestamps": {
						"from": "00:00:00,220",
						"to": "00:00:00,580"
					},
					"offsets": {
						"from": 220,
						"to": 580
					},
					"id": 1702,
					"p": 0.639155,
					"t_dtw": -1
				},
				{
					"text": " brown",
					"timestamps": {
						"from": "00:00:00,580",
						"to": "00:00:00,920"
					},
					"offsets": {
						"from": 580,
						"to": 920
					},
					"id": 6292,
					"p": 0.608595,
					"t_dtw": -1
				},
				{
					"text": " fox",
					"timestamps": {
						"from": "00:00:01,090",
						"to": "00:00:01,160"
					},
					"offsets": {
						"from": 1090,
						"to": 1160
					},
					"id": 21026,
					"p": 0.730789,
					"t_dtw": -1
				},
				{
					"text": " jumps",
					"timestamps": {
						"from": "00:00:01,160",
						"to": "00:00:01,510"
					},
					"offsets": {
						"from": 1160,
						"to": 1510
					},
					"id": 16704,
					"p": 0.973938,
					"t_dtw": -1
				},
				{
					"text": " over",
					"timestamps": {
						"from": "00:00:01,540",
						"to": "00:00:01,810"
					},
					"offsets": {
						"from": 1540,
						"to": 1810
					},
					"id": 670,
					"p": 0.996767,
					"t_dtw": -1
				},
				{
					"text": " the",
					"timestamps": {
						"from": "00:00:01,810",
						"to": "00:00:02,030"
					},
					"offsets": {
						"from": 1810,
						"to": 2030
					},
					"id": 264,
					"p": 0.992589,
					"t_dtw": -1
				},
				{
					"text": " lazy",
					"timestamps": {
						"from": "00:00:02,030",
						"to": "00:00:02,320"
					},
					"offsets": {
						"from": 2030,
						"to": 2320
					},
					"id": 14847,
					"p": 0.888795,
					"t_dtw": -1
				},
				{
					"text": " dog",
					"timestamps": {
						"from": "00:00:02,320",
						"to": "00:00:02,420"
					},
					"offsets": {
						"from": 2320,
						"to": 2420
					},
					"id": 3000,
					"p": 0.978694,
					"t_dtw": -1
				},
				{
					"text": ",",
					"timestamps": {
						"from": "00:00:02,710",
						"to": "00:00:02,720"
					},
					"offsets": {
						"from": 2710,
						"to": 2720
					},
					"id": 11,
					"p": 0.397882,
					"t_dtw": -1
				},
				{
					"text": " this",
					"timestamps": {
						"from": "00:00:02,720",
						"to": "00:00:03,000"
					},
					"offsets": {
						"from": 2720,
						"to": 3000
					},
					"id": 341,
					"p": 0.90093,
					"t_dtw": -1
				},
				{
					"text": " is",
					"timestamps": {
						"from": "00:00:03,000",
						"to": "00:00:03,140"
					},
					"offsets": {
						"from": 3000,
						"to": 3140
					},
					"id": 307,
					"p": 0.995737,
					"t_dtw": -1
				},
				{
					"text": " a",
					"timestamps": {
						"from": "00:00:03,140",
						"to": "00:00:03,210"
					},
					"offsets": {
						"from": 3140,
						"to": 3210
					},
					"id": 257,
					"p": 0.975803,
					"t_dtw": -1
				},
				{
					"text": " local",
					"timestamps": {
						"from": "00:00:03,210",
						"to": "00:00:03,520"
					},
					"offsets": {
						"from": 3210,
						"to": 3520
					},
					"id": 2654,
					"p": 0.982362,
					"t_dtw": -1
				},
				{
					"text": " transcription",
					"timestamps": {
						"from": "00:00:03,560",
						"to": "00:00:04,470"
					},
					"offsets": {
						"from": 3560,
						"to": 4470
					},
					"id": 35288,
					"p": 0.914677,
					"t_dtw": -1
				},
				{
					"text": " test",
					"timestamps": {
						"from": "00:00:04,470",
						"to": "00:00:04,620"
					},
					"offsets": {
						"from": 4470,
						"to": 4620
					},
					"id": 1500,
					"p": 0.985678,
					"t_dtw": -1
				},
				{
					"text": ".",
					"timestamps": {
						"from": "00:00:04,760",
						"to": "00:00:04,780"
					},
					"offsets": {
						"from": 4760,
						"to": 4780
					},
					"id": 13,
					"p": 0.823774,
					"t_dtw": -1
				},
				{
					"text": "[_TT_240]",
					"timestamps": {
						"from": "00:00:04,800",
						"to": "00:00:04,800"
					},
					"offsets": {
						"from": 4800,
						"to": 4800
					},
					"id": 50604,
					"p": 0.130727,
					"t_dtw": -1
				}
			]
		}
	]
}
```

</details>

## metal.json

Original file SHA-256: `5d98146d6b6d6f62f92d67bd3ee3f6a903a9a35e574f6dbf10a1b9f423b2952f`

<details>
<summary>Complete recorded result</summary>

```json
{
	"systeminfo": "WHISPER : VITISAI = 0 | COREML = 0 | OPENVINO = 0 | MTL : EMBED_LIBRARY = 1 | CPU : NEON = 1 | ARM_FMA = 1 | FP16_VA = 1 | DOTPROD = 1 | ACCELERATE = 1 | REPACK = 1 | ",
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
		"model": "/Users/runner/work/_temp/atrain-probe-hf/ggml-tiny.bin",
		"language": "en",
		"translate": false
	},
	"result": {
		"language": "en"
	},
	"transcription": [
		{
			"timestamps": {
				"from": "00:00:00,000",
				"to": "00:00:04,800"
			},
			"offsets": {
				"from": 0,
				"to": 4800
			},
			"text": " the quick brown fox jumps over the lazy dog, this is a local transcription test.",
			"tokens": [
				{
					"text": "[_BEG_]",
					"timestamps": {
						"from": "00:00:00,000",
						"to": "00:00:00,000"
					},
					"offsets": {
						"from": 0,
						"to": 0
					},
					"id": 50364,
					"p": 0.993187,
					"t_dtw": -1
				},
				{
					"text": " the",
					"timestamps": {
						"from": "00:00:00,010",
						"to": "00:00:00,220"
					},
					"offsets": {
						"from": 10,
						"to": 220
					},
					"id": 264,
					"p": 0.50186,
					"t_dtw": -1
				},
				{
					"text": " quick",
					"timestamps": {
						"from": "00:00:00,220",
						"to": "00:00:00,580"
					},
					"offsets": {
						"from": 220,
						"to": 580
					},
					"id": 1702,
					"p": 0.641422,
					"t_dtw": -1
				},
				{
					"text": " brown",
					"timestamps": {
						"from": "00:00:00,580",
						"to": "00:00:00,920"
					},
					"offsets": {
						"from": 580,
						"to": 920
					},
					"id": 6292,
					"p": 0.608404,
					"t_dtw": -1
				},
				{
					"text": " fox",
					"timestamps": {
						"from": "00:00:01,090",
						"to": "00:00:01,160"
					},
					"offsets": {
						"from": 1090,
						"to": 1160
					},
					"id": 21026,
					"p": 0.731925,
					"t_dtw": -1
				},
				{
					"text": " jumps",
					"timestamps": {
						"from": "00:00:01,160",
						"to": "00:00:01,510"
					},
					"offsets": {
						"from": 1160,
						"to": 1510
					},
					"id": 16704,
					"p": 0.973831,
					"t_dtw": -1
				},
				{
					"text": " over",
					"timestamps": {
						"from": "00:00:01,540",
						"to": "00:00:01,810"
					},
					"offsets": {
						"from": 1540,
						"to": 1810
					},
					"id": 670,
					"p": 0.996736,
					"t_dtw": -1
				},
				{
					"text": " the",
					"timestamps": {
						"from": "00:00:01,810",
						"to": "00:00:02,030"
					},
					"offsets": {
						"from": 1810,
						"to": 2030
					},
					"id": 264,
					"p": 0.992634,
					"t_dtw": -1
				},
				{
					"text": " lazy",
					"timestamps": {
						"from": "00:00:02,030",
						"to": "00:00:02,320"
					},
					"offsets": {
						"from": 2030,
						"to": 2320
					},
					"id": 14847,
					"p": 0.889626,
					"t_dtw": -1
				},
				{
					"text": " dog",
					"timestamps": {
						"from": "00:00:02,320",
						"to": "00:00:02,420"
					},
					"offsets": {
						"from": 2320,
						"to": 2420
					},
					"id": 3000,
					"p": 0.978607,
					"t_dtw": -1
				},
				{
					"text": ",",
					"timestamps": {
						"from": "00:00:02,710",
						"to": "00:00:02,720"
					},
					"offsets": {
						"from": 2710,
						"to": 2720
					},
					"id": 11,
					"p": 0.398777,
					"t_dtw": -1
				},
				{
					"text": " this",
					"timestamps": {
						"from": "00:00:02,720",
						"to": "00:00:03,000"
					},
					"offsets": {
						"from": 2720,
						"to": 3000
					},
					"id": 341,
					"p": 0.900332,
					"t_dtw": -1
				},
				{
					"text": " is",
					"timestamps": {
						"from": "00:00:03,000",
						"to": "00:00:03,140"
					},
					"offsets": {
						"from": 3000,
						"to": 3140
					},
					"id": 307,
					"p": 0.99579,
					"t_dtw": -1
				},
				{
					"text": " a",
					"timestamps": {
						"from": "00:00:03,140",
						"to": "00:00:03,210"
					},
					"offsets": {
						"from": 3140,
						"to": 3210
					},
					"id": 257,
					"p": 0.976105,
					"t_dtw": -1
				},
				{
					"text": " local",
					"timestamps": {
						"from": "00:00:03,210",
						"to": "00:00:03,520"
					},
					"offsets": {
						"from": 3210,
						"to": 3520
					},
					"id": 2654,
					"p": 0.982452,
					"t_dtw": -1
				},
				{
					"text": " transcription",
					"timestamps": {
						"from": "00:00:03,560",
						"to": "00:00:04,470"
					},
					"offsets": {
						"from": 3560,
						"to": 4470
					},
					"id": 35288,
					"p": 0.914955,
					"t_dtw": -1
				},
				{
					"text": " test",
					"timestamps": {
						"from": "00:00:04,470",
						"to": "00:00:04,620"
					},
					"offsets": {
						"from": 4470,
						"to": 4620
					},
					"id": 1500,
					"p": 0.985481,
					"t_dtw": -1
				},
				{
					"text": ".",
					"timestamps": {
						"from": "00:00:04,760",
						"to": "00:00:04,780"
					},
					"offsets": {
						"from": 4760,
						"to": 4780
					},
					"id": 13,
					"p": 0.82351,
					"t_dtw": -1
				},
				{
					"text": "[_TT_240]",
					"timestamps": {
						"from": "00:00:04,800",
						"to": "00:00:04,800"
					},
					"offsets": {
						"from": 4800,
						"to": 4800
					},
					"id": 50604,
					"p": 0.130673,
					"t_dtw": -1
				}
			]
		}
	]
}
```

</details>
