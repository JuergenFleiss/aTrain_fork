# Offline model install (issue #318): findings and fix plan

Status: decided, ready to implement; this document does not change application behavior.
Baseline: `aa9b316` (`feature/queue-ui`), reviewed on 2026-10-19, huggingface-hub 0.36.0 per `uv.lock`.
Issue: https://github.com/aTrainTranscription/aTrain/issues/318
Related PRs: #312 (`check_internet()` through the hub session), #286 (Transformers 5.17 /
huggingface-hub 1.33.0), #288 (Qwen3 models, model dependencies; stacked on #286).

## 1. What is reported

On Windows 11, aTrain 1.5.0-rc3 (MSIX, provisioned system-wide), with no access to
huggingface.co, the files of `aTrain-core/faster-whisper-large-v3-turbo` were downloaded
in a browser **from `tree/main`** and copied into
`%USERPROFILE%\Documents\aTrain\models\large-v3-turbo\`.

- aTrain still tries to contact Hugging Face.
- With Hugging Face disabled through an environment variable (probably
  `HF_HUB_OFFLINE=1`), the integrity check fails with a **hash mismatch**.
- On a mismatch, aTrain deletes the model folder, so every retry means copying again.

The tester's exact error text has not been posted yet (no comments on #318 as of 2026-10-19).

## 2. Findings

### 2.1 Mechanism with huggingface-hub 0.36.0 (current pin)

`get_model()` in `aTrain_core/load_resources.py`:

```text
folder missing or any manifest file missing?
  no  -> return the folder            (no hash check at all)
  yes -> download_model() -> snapshot_download(local_dir=..., revision=<commit>)
         verify_model()   -> on problems: shutil.rmtree(folder), raise ModelIntegrityError
```

1. A hand copy almost always misses a manifest file. Every manifest includes
   `.gitattributes` and `README.md`; `speaker-detection` also needs the subfolders
   `embedding/`, `plda/` and `segmentation/`, which a browser download flattens
   (`pytorch_model (1).bin`). `find_missing_files()` reports them, so
   `download_model()` runs. **This is the Hugging Face contact in the report.**
2. When hub 0.36.0's `snapshot_download` cannot reach the Hub (`HF_HUB_OFFLINE=1`, or
   simply no network) and `local_dir` is non-empty, it does not raise. It logs
   `Returning existing local_dir ... as remote repo cannot be accessed` and returns
   the folder unchanged. With an empty folder it raises `LocalEntryNotFoundError`,
   which nothing catches.
3. `verify_model()` then hashes what is there. Files that differ from the pin are
   reported as `expected sha256 ..., got ...`; absent ones as `missing`.
   **This is the hash mismatch in the report.**
4. `get_model()` deletes the whole folder, including the files that were correct.

Reproduced with the `tiny` manifest, `ATRAIN_USER_DIR` in a temp dir,
`HF_HUB_OFFLINE=1`, placeholder file contents and `README.md` left out:
`ModelIntegrityError` listing mismatches plus `README.md: missing`, and the model
folder was gone afterwards.

### 2.2 A complete folder is never verified

Same setup with **every** manifest file present (wrong contents): `get_model()`
returned the folder without error. The hash check only runs after a download, so a
complete hand copy with wrong bytes is used silently, and the mismatch only shows up
once some other file is missing. This contradicts the intent stated in
`aTrain_core/integrity.py` and the comment in `test_failed_verification_removes_the_model`.

### 2.3 The GUI deletes models on its own

`download_model()` in `aTrain/utils/models.py` (the Models page "Download" button)
calls `check_internet()` and then `get_model()`, and on **any** exception it calls
`remove_model(model)`, which deletes the whole folder. Offline, `check_internet()`
fails, so clicking "Download" deletes a hand-copied folder before `get_model()` is
even reached. A fix confined to `get_model()` does not cover this path.

With PR #312, `check_internet()` uses `huggingface_hub.utils.get_session()`. With
`HF_HUB_OFFLINE=1` that session mounts an `OfflineAdapter` and raises
`OfflineModeIsEnabled` (a `ConnectionError` subclass), so the path above always runs
offline.

### 2.4 A correct `speaker-detection` folder is listed as not downloaded

`read_downloaded_models()` counts a folder as downloaded when it has a `.bin` file at
its top level. `speaker-detection` keeps its `.bin` files in `embedding/` and
`segmentation/`, so a correctly installed copy shows a "Download" button on the Models
page, which leads into 2.3. A flattened (wrong) browser copy, by contrast, has
`pytorch_model.bin` at the top level and is listed as installed. PR #288 adds a
`find_missing_files()` check, but only for safetensors backends.

### 2.5 What PR #286 (huggingface-hub 1.33.0) changes

PR #286 only removes `local_dir_use_symlinks=False` from `download_model()`; the
`get_model()` logic is unchanged. Hub 1.33.0 was run in an isolated environment with
the same reproduction:

- `snapshot_download` raises `OfflineModeIsEnabled` (from the tree listing request).
  `get_model()` does not catch it, so the user gets an unhandled exception.
- The folder is **not** deleted, because `verify_model()` is never reached.
- Cause: our revisions are commit hashes. Hub 1.33 treats them as resolved, skips the
  repo lookup and with it the offline fallback, then needs the file tree from the
  network because no tree cache exists for a hand copy.

So the upgrade changes the symptom but does not fix the issue. The fix must work with
both hub versions.

### 2.6 Still unknown

Which of the tester's files mismatched. Most likely cause: the files come from `main`
(the issue says so) instead of the revision pinned in `models.json`. Other possible
causes: files renamed by flattening, or the browser saving an HTML page or an LFS
pointer instead of the file. The tester's error text settles this; the fix does not
depend on it.

## 3. Goals and non-goals

Goals:
- Models copied by hand at the pinned revision work fully offline.
- If files are missing or wrong, the error names them, the expected folder, the repo
  and the revision. It never ends in an unhandled hub exception.
- Correct files the user copied are not destroyed, neither by `get_model()` nor by the
  Models page.
- No model file is used without having passed the hash check once.
- Documented offline install for administrators.

Non-goals: changing the manifest format, dropping `README.md` / `.gitattributes` from
the manifests, a model import UI, bundling models into the MSIX.

## 4. Decisions

1. Complete folders are verified once and the result is recorded in a marker file
   (step 4). No full hash on every load.
2. On a mismatch only the failing files are deleted; matching files stay (step 3).
3. No connectivity probe in `get_model()`. Machines without network that do not set
   `HF_HUB_OFFLINE` are covered by translating the hub's exceptions (step 1).

## 5. Fix

Core changes are in `aTrain_core/load_resources.py` (helpers may go to
`aTrain_core/integrity.py`); GUI changes in `aTrain/utils/models.py`. Other callers
(`aTrain/app.py`, `aTrain_core/engine.py`, `aTrain_core/transcribe.py`,
`aTrain_core/cli.py`) keep calling `get_model()` unchanged; a `ModelIntegrityError`
there fails the job or the command with its message.

### Step 1: do not try to download when offline

Before `download_model()`, if `huggingface_hub.constants.HF_HUB_OFFLINE` is set and
files are missing, raise `ModelIntegrityError` right away with the missing file list.
Also wrap the `snapshot_download` call and translate `OfflineModeIsEnabled`,
`LocalEntryNotFoundError` and other `ConnectionError`s into the same message. That
covers machines without network that do not set the variable, an empty folder on hub
0.36, and hub 1.33's behavior.

### Step 2: actionable message

One helper builds the message for "missing" and "mismatch" cases:

```text
Model 'large-v3-turbo' is incomplete or does not match its pinned checksums.
Folder:   C:\Users\<user>\Documents\aTrain\models\large-v3-turbo
Source:   https://huggingface.co/aTrain-core/faster-whisper-large-v3-turbo/tree/df99141c...
Problems: README.md: missing
          model.bin: expected sha256 ..., got ...
```

The source link points to the pinned revision (`tree/<revision>`), not `main`. The
existing `_integrity_message()` (bundled vs. writable folder) stays and adds these
lines; its "will be removed" wording changes to "the files that failed were removed".

### Step 3: delete only the files that failed, not the folder

On a mismatch, remove the mismatched files only. Matching files stay. This keeps the
invariant that bad bytes never stay on disk (the reason for the current `rmtree`),
while an online retry re-downloads just those files and an offline retry reports
them as missing. Bundled models in the read-only `REQUIRED_MODELS_DIR` are left alone,
as today. `verify_model()` returns strings today; the code that deletes needs the
failing file names, so it either returns them in a structured form or a second
helper provides them.

### Step 4: verify complete folders once (marker)

When a folder is complete but has no valid marker, run `verify_model()` before
returning it. On success, write `.atrain-verified` in the model folder, containing the
revision and a digest of the manifest. The marker is also written right after a
successful download and verification, so a fresh download is not hashed twice. A
changed manifest (new revision) invalidates the marker. Writes are best-effort: a
folder that cannot be written is verified on every load instead of failing.

The bundled read-only folder cannot hold a marker. It ships inside the signed package
and is skipped as today.

Consequence: existing installs have no marker, so the first load after the update
hashes the model once (about 1.6 GB for `large-v3-turbo`). This runs in the worker
before transcription starts, with no progress bar, so mention it in the release notes.
With PR #288, dependencies of a model are loaded through `get_model()` too and get the
same check.

### Step 5: Models page does not delete on connection or integrity errors

In `aTrain/utils/models.py::download_model()`:

- `ConnectionError` (from `check_internet()`, including `OfflineModeIsEnabled` with
  #312) and `ModelIntegrityError`: show the error dialog, do **not** call
  `remove_model()`. `get_model()` has already removed the failing files itself.
- `BrokenProcessPool` and other exceptions: unchanged (a crashed worker may leave a
  partial download, which the missing-file check catches on the next call anyway).

`ModelIntegrityError` raised in the process pool reaches this code as a
`SubprocessException`; tell them apart by `e.original_type` or by the message rather
than by `isinstance`.

### Step 6: list `speaker-detection` correctly

In `read_downloaded_models()`, count a folder as downloaded when
`find_missing_files()` reports nothing for its manifest, instead of looking for a
top-level `.bin`. This is a cheap stat-only check. It fixes 2.4 and generalizes what
PR #288 does for safetensors backends, so whichever lands second resolves the conflict
by keeping the manifest check. Incomplete folders then show "Download", which after
step 5 no longer deletes anything offline.

### Step 7: documentation

`docs/deployment-windows.md` currently says machines without internet need the
bundled build. Add an offline install section instead. The MSIX has no app execution
alias, so `aTrain init` cannot be run from a shell there; the instructions use one of:

1. On a connected machine with a source checkout (PowerShell):
   `$env:ATRAIN_USER_DIR = "C:\temp\atrain"; uv run aTrain init`. This downloads the
   required models at the pinned revisions and verifies them.
2. Or, with the Hugging Face CLI, per required model:
   `hf download aTrain-core/faster-whisper-large-v3-turbo --revision <commit> --local-dir <dir>\large-v3-turbo`
   (and the same for `aTrain-core/speaker-detection` into `<dir>\speaker-detection`),
   with the commit hashes taken from `aTrain_core/data/models.json` of the installed
   version. The `.cache\huggingface\` folder this creates is harmless.

Then:

3. Copy the complete `speaker-detection` and `large-v3-turbo` folders, including
   subfolders, `.gitattributes` and `README.md`, to
   `%USERPROFILE%\Documents\aTrain\models\` on the target (or `ATRAIN_USER_DIR`).
4. Optionally set `HF_HUB_OFFLINE=1` so aTrain never tries the network.
5. Warn explicitly against downloading single files in the browser, and against
   `tree/main`: the files must come from the pinned revision.

The first start verifies the copied models once (step 4).

## 6. Tests (written first, failing on the baseline)

New file `tests/unit/test_get_model_offline.py`. Not `tests/unit/test_load_resources.py`,
which #286 and #288 both edit. Use a fake manifest and `MODELS_DIR` / `download_model`
monkeypatched as in `test_failed_verification_removes_the_model`:

| Test | Baseline result |
| --- | --- |
| Offline (`HF_HUB_OFFLINE` patched true), one file missing: `ModelIntegrityError` naming the file, `download_model` not called | fails: download is called |
| `download_model` raises `OfflineModeIsEnabled` / `LocalEntryNotFoundError`: translated into `ModelIntegrityError` with folder, repo and revision | fails: hub exception escapes |
| Mismatch after download: the mismatched file is removed, matching files remain | fails: whole folder removed |
| Complete folder with wrong bytes: `ModelIntegrityError`, wrong file removed | fails: returned silently |
| Complete, correct folder: verified once, marker written, the second call does not hash again | fails: no marker |
| Fresh download that verifies: marker written, next call does not hash | fails: no marker |
| Manifest changes (new revision): marker ignored, folder re-verified | fails: no marker |

GUI (`tests/ui`, the module imports nicegui):

| Test | Baseline result |
| --- | --- |
| `download_model()` with `check_internet` raising `ConnectionError`: folder still exists, error dialog shown | fails: folder removed |
| `download_model()` with `get_model` raising `ModelIntegrityError` (via the pool): `remove_model` not called | fails: folder removed |
| `read_downloaded_models()` lists a complete `speaker-detection` folder with subfolders | fails: not listed |
| `read_downloaded_models()` does not list a folder with manifest files missing | fails: listed if a top-level `.bin` exists |

`test_failed_verification_removes_the_model` changes meaning with step 3 and is
updated alongside it. Manual checks: the offline repro from 2.1 on Linux, then the
reporter's scenario on Windows MSIX with `HF_HUB_OFFLINE=1`, including clicking
"Download" on the Models page while offline.

## 7. Branch, PR and ordering

- The issue is in 1.5.0-rc3, so this is a bugfix: branch `bugfixes_offline_models`
  from `develop`. No `bugfixes_for_aTrain_1.x.x` branch exists as of 2026-10-19;
  check again before branching (CONTRIBUTING.md).
- Ordering with open PRs:
  - **#312** touches `check_internet()` in the same function as step 5. Merge #312
    first and rebase onto it, so step 5 is tested against the hub-session check.
  - **#286** removes the line next to the `snapshot_download` call that step 1 wraps.
    Keep the fix independent; whichever lands second rebases. #286 must keep the new
    offline tests green on hub 1.33.
  - **#288** changes `read_downloaded_models()` (step 6) and adds recursive
    dependency loading to `get_model()`. Conflicts are textual; resolve them by keeping
    the manifest-based check from step 6.
  - **#179** (queue) only touches `aTrain_core/globals.py` in this area; no conflict.
    A `ModelIntegrityError` in a queued job fails that job with the message.
- Comment on #318 with the findings in section 2 and ask for the error text.
