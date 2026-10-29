# CLI worker implementation plan

Status: proposed implementation; no runtime code is changed by this document.
Baseline: repository HEAD `45db5aa`, reviewed on 2026-10-04.

This plan replaces the queue's multiprocessing transport with a small command-line
phase worker. It also makes the public CLI use the same job execution and ownership
rules as the GUI. It does not turn the queue into a daemon or make UI commands shell
out. See [the review remediation plan](job-queue-review-implementation.md) for the
correctness changes shared by both approaches.

## 1. Intended result and scope

```text
NiceGUI views ──Python calls──> QueueService ──subprocess──> phase worker ──> engine
Public CLI ──single-job mode──> QueueService ──subprocess──> phase worker ──> engine
```

- One parent owns the queue lock, writes queue state, and owns the active child.
- A child runs one transcription or speaker-detection phase and exits.
- A transcription-only job uses one child; a speaker-detection job uses two,
  sequentially. Phase 1 must exit before phase 2 starts, releasing model memory.
- Checkpoints, archive formats, settings, retry behavior, and export warnings remain
  available through both entry points.
- The UI continues to call `enqueue`, `pause`, `resume`, `cancel`, and `retry` as
  ordinary Python methods. There is no queue command server or polling CLI process.
- The existing public `aTrain_core transcribe`, `load`, and `remove` commands remain.
  The internal machine protocol is separate from their human-facing output.

This is worthwhile only if the deployed builds can start and supervise the worker
reliably and the old execution paths are actually removed. JSON framing and process
launch support add code: replacing `Pipe` alone is not evidence of simplification.

## 2. Existing code and the smallest intended structure

| File | Planned responsibility/change |
| --- | --- |
| `aTrain_core/runner.py` | Keep the two phase functions, checkpoint reuse, progress adapter, and shared request/result types; remove multiprocessing entry points and pipe transport. |
| `aTrain_core/worker.py` — new | Minimal module entry point, bounded JSON request parsing, protocol writer, parent EOF watchdog, and dispatch to phase functions. |
| `aTrain_core/worker_process.py` — new | `asyncio` launch, bounded stream reading, stderr capture, cancellation, wait/reap, and platform command selection. |
| `aTrain_core/queue_service.py` | Sole queue owner; one current-phase context; apply phase results, publication, and recovery; expose a scoped single-job execution method for the public CLI. |
| `aTrain_core/jobs.py` | Lock-first load/recovery and atomic changes from the review plan; reuse `JobSpec.to_json`/`from_json` with explicit protocol validation. |
| `aTrain_core/outputs.py` | Explicit staging destination, checkpoint validation, completed-output publication/reconciliation shared with the review plan. |
| `aTrain_core/cli.py` | Build a `JobSpec`, validate inputs, run only that job through the service; lazy imports for command-specific dependencies. |
| `aTrain_core/transcribe.py` | Remove obsolete orchestration after migrating its callers; retain an adapter only if a supported external API is confirmed. |
| `aTrain/components/splash_screen.py` | Remove eager loading of the obsolete transcription module. |
| `aTrain/utils/queue_ui.py` | Retain direct service integration; remove obsolete lifecycle workarounds once fixtures manage lifecycle. |
| `freeze.py`, `freeze.spec`, `macos_freeze.spec` | Early worker dispatch and tested packaged worker launch/stdio support. |
| `aTrain/app.py`, `flatpak/run-atrain.sh` | Verify Windows event-loop compatibility and sandbox launch assumptions; change configuration only where the launch gate requires it. |
| `pyproject.toml` | Preserve public scripts; add no public worker script unless packaging proves it necessary. |
| `.github/workflows/ci.yml`, `.github/workflows/release.yml` | Subprocess and installed/build smoke checks. |

Do not introduce a transport framework, codec registry, dependency-injection
container, job daemon, general RPC client, or durable event log. The worker and parent
ship together; one versioned protocol and two phase choices are enough. If the
combined worker transport fits clearly in one file after implementation, merge the
two proposed new modules rather than preserving a split for its own sake.

## 3. Feasibility gate: launching the shipped application

Complete this small spike before replacing the production runner. Exercise a worker
that reads one request, writes one result, and sleeps while its parent is killed.
Use the real packaged entry path, not only `python -c`.

| Environment | Intended launch | Required evidence |
| --- | --- | --- |
| Source checkout / virtual environment | `[sys.executable, "-m", "aTrain_core.worker"]` | Works with absolute input paths and without depending on the current directory. |
| Installed wheel, headless dependencies | Same module invocation in the current interpreter | Worker module is included; no NiceGUI or webview dependency is imported. |
| Flatpak | Current in-sandbox interpreter/module or a bundled worker entry point | Same sandbox, `ATRAIN_USER_DIR`, model paths, document-portal paths, and permissions; no host escape or system Python lookup. |
| Windows frozen / MSIX | Bundled worker executable or verified early worker branch | Pipes work, no console window flashes, startup does not launch another GUI, kill/wait works. |
| macOS frozen app | Verified executable inside the app bundle, early worker branch | Bundle launch does not start GUI; signing/layout includes worker; stdout, stderr, stdin EOF and termination work. |

`freeze.py` currently calls `app.start()` unconditionally for normal execution.
Dispatch the internal worker before importing `aTrain.app`, model libraries, or
NiceGUI. `multiprocessing.freeze_support()` is not a CLI worker dispatcher.

`freeze.spec` uses `console=False`. In a windowed frozen process `sys.stdout` and
`sys.stderr` may be `None`, and usable descriptor 1/2 cannot be assumed. Merely passing
`stdout=PIPE` to that executable is insufficient evidence. The current
`macos_freeze.spec` uses `console=True`, but its actual app launch still needs a test.

Prefer a small console-capable worker executable sharing the bundled Python modules
if the GUI executable cannot reliably expose all three redirected streams. On Windows
launch it with the no-window creation flag. Keep the same Python worker entry point;
do not duplicate engine code or bundle a second model installation. Verify the extra
binary is collected, signed, and packaged by the release/MSIX path. A platform-specific
stdio-handle reconstruction layer is justified only if it is clearly smaller and
better tested than this companion executable.

Gate result: record the actual command per supported distribution and pass pipe,
parent-death, and no-GUI-start smoke checks. If a target fails, keep the existing
transport for that release; do not silently ship an untested fallback or claim the
migration is complete.

`flatpak/run-atrain.sh` always ends by launching `aTrain start`; do not use that wrapper
as the worker command. Launch the current in-sandbox interpreter directly and inherit
the wrapper's resolved environment. Include Windows normal/reload event-loop checks
from section 6 in this gate before selecting the subprocess implementation.

## 4. Request and event protocol

The parent starts one child with stdin/stdout/stderr pipes, writes one UTF-8 JSON
request followed by `\n`, drains the write, and leaves stdin open. It sends no further
commands. No shell is used. Paths and prompts are data, never command fragments.

An illustrative phase-1 request, shown pretty-printed for readability; the wire
representation is one line:

```json
{
  "version": 1,
  "phase": 1,
  "job": {
    "spec": {
      "id": "63993c049fc74a19a0f02fe7b5b6cda0",
      "source": "/recordings/interview.mp3",
      "display_name": "interview.mp3",
      "model": "large-v3-turbo",
      "language": "auto-detect",
      "device": "cpu",
      "compute_type": "int8",
      "cpu_threads": 4,
      "temperature": null,
      "initial_prompt": null,
      "speaker_detection": false,
      "speaker_count": null,
      "export_dir": null
    },
    "timestamp": "2026-10-04 09-00-00",
    "work_dir": "/atrain/queue/work/63993c049fc74a19a0f02fe7b5b6cda0"
  },
  "output": {
    "file_id": "2610040900-intervi",
    "staging_dir": "/atrain/transcriptions/.pending/63993c049fc74a19a0f02fe7b5b6cda0"
  }
}
```

The identifier is illustrative; preserve the application's existing naming format.
The parent chooses and durably records the output identity. (Today the child picks a
free `file_id` itself, writes into the archive's hidden `.pending` folder, publishes by
rename and reports the `file_id` in `JobDone`; see the review plan's Phase 4 status.)
For phase 1 of a job requiring speaker detection, `output` can be `null`; it is supplied
to the final phase.
Reuse the publication fields/marker established in the review plan rather than adding
a second receipt format. A child never acquires the queue lock or writes `queue.json`.

Stdout contains NDJSON: zero or more progress records, followed by exactly one result
under normal execution. Example alternatives, not a single valid combined stream:

```json
{"type":"progress","current":3.5,"total":12.0}
{"type":"result","status":"transcribed","audio_duration":12}
{"type":"result","status":"ready","audio_duration":12}
{"type":"result","status":"failed","step":"transcription","error":"Could not decode source","traceback":"...","truncated":false}
```

- `transcribed`: phase 1 wrote a reusable raw checkpoint; phase 2 remains. It changes
  no saved status (there is no `TRANSCRIBED` status any more): `_run_job` starts phase 2
  right after, or puts the job back to `QUEUED` when paused or stopping, or marks it
  `CANCELLED` when a cancel arrived. Today the multiprocessing runner signals this with
  `PhaseFinished` and no result; this record replaces that.
- `ready`: all required output files and the completion marker are in staging,
  and any requested best-effort export has been attempted with warnings recorded;
  the parent must publish and persist completion before the job becomes `DONE`.
- `failed`: the phase failed, with its specific step and bounded diagnostic text.
- Progress has finite, nonnegative numbers; clamp the displayed fraction safely when
  total is zero. Preserve the existing throttle, approximately five updates/second,
  plus a final flush. Do not send transcripts, audio, or model objects through stdout.
- No `job_id`, task string, filename-announcement event, separate `PhaseFinished`, or
  second error event is needed on a private per-phase stream. The parent knows the job.
- Result variants must match the requested phase/settings. Reject unknown versions,
  malformed records, incompatible result shapes, duplicate results, and records
  after a result; never skip an arbitrary stdout line as though it were a log.
- Use explicit small validation functions; no new runtime schema dependency.
  Validate types, enum values, finite numbers, and required fields rather than trusting
  the dataclass constructor to enforce annotations. Reject JSON NaN/Infinity.

Initial bounds: request at most 1 MiB; each event at most 64 KiB including newline;
error text at most 4 KiB; traceback at most 48 KiB; stderr retains only its final
64 KiB. Bound the final encoded JSON bytes as well as source strings, since escaping
can expand them. Include a truncation indicator and a useful tail in errors. Reject
an oversized user request with an actionable error; do not silently truncate a prompt.

## 5. Worker execution and parent-death behavior

Implement the following startup order in `worker.py`:

1. Obtain the binary stdio streams, preserve a dedicated protocol output descriptor,
   and redirect ordinary stdout to stderr before importing execution dependencies.
2. Read a bounded request line. Validate it and construct the existing job types.
   EOF before a complete request fails without launching a model.
3. Start a daemon thread watching the remaining stdin stream for EOF.
4. Dispatch phase 1 or phase 2 using normal Python callables and lazy model imports.
5. Flush progress; emit one terminal result; flush and close the protocol stream.
6. Exit explicitly with `os._exit`: 0 for successful phase work, 1 for phase failure,
   2 for invalid request/protocol setup, and 3 for lost parent.

The existing `multiprocessing.parent_process()` watchdog does not work here: an
ordinary CLI subprocess has no multiprocessing parent object. The stdin pipe is the
parent-liveness signal. Its write end remains held only by the supervising parent;
when that process dies, the watcher observes EOF and calls `os._exit(3)`, even while
model inference is busy. Read the initial line and remainder through the same stream
so buffering cannot hide bytes from the watcher. Reject additional input bytes.
Avoid leaking the stdin writer into grandchildren; use normal close-on-exec behavior
and test EOF with real processes. Closing stdin intentionally also ends the worker.

Do not use `process.communicate(input=request)`: it closes stdin, conflicting with
this liveness contract, and can accumulate unbounded output. Read streams separately.

Preserve the reason for the current explicit exit: faster-whisper can hang during
normal interpreter shutdown. Flush protocol data and close ordinary output/checkpoint
files before `os._exit`; never depend on `atexit` or buffered file destruction.

For stdout isolation, duplicate the original output descriptor for the protocol,
then redirect descriptor 1 to stderr using descriptor-level operations and rebuild
Python streams if necessary. `contextlib.redirect_stdout` alone cannot capture native
extension writes. Keep the protocol descriptor non-inheritable. Check this behavior
on Windows native handles in the feasibility spike. Unexpected writes bypassing the
redirection remain a protocol failure; the parent must not accept corrupted output.

## 6. Async parent transport and one child owner

`worker_process.py` launches through `asyncio.create_subprocess_exec`, passing argv
as a list and inheriting required model/cache/user-directory environment variables.
Do not require activation scripts, a PATH-resolved `python`, a repository working
directory, `shell=True`, or large command-line JSON arguments.

Check the actual NiceGUI/Uvicorn loop on Windows in both normal and `--reload` modes.
The locally installed Uvicorn selects a Selector loop when its subprocess/reload
setting is active; `asyncio` subprocess APIs need a compatible Windows loop. Recheck
that dependency behavior during implementation and configure one explicit compatible
loop factory if needed. Exercise real UI startup in both modes, rather than assuming
a standalone `asyncio.run()` subprocess test proves compatibility. Do not maintain a
second transport just to bypass an unverified loop configuration.

Read stdout and stderr concurrently from launch until EOF. Configure reader limits
and reject oversized or unterminated stdout records without growing an unbounded
buffer. Decode and parse only complete records. A partial line must yield control so
the UI heartbeat and cancellation continue. Drain stderr even after its retained tail
is full; discard old bytes rather than blocking or storing an unlimited list.

The transport exposes progress, one parsed result, and final process exit status.
It does not decide persistent job status. At most one terminal result is kept in
memory. The service holds a current-phase context containing job ID, process handle,
phase, cancellation intent, and any pending result until the process is reaped and
the durable outcome is resolved. Replace `_handle`, `_in_flight`, and `_phase_error`
with this single owner. The cancellation intent is already the one boolean the UI reads,
`QueueService.cancelling`; derive it from the context.

Reserve that active context before awaiting `create_subprocess_exec`: unlike the
existing launcher, spawning now yields. Cancel/stop while launch is pending records
intent; when the process arrives, terminate and reap it before sending the work request.
Shield/own the spawn task through cleanup so cancelling its caller cannot leave a
successfully created process unowned. Do not start another job until this settles.

Cancellation is asynchronous and idempotent: capture the current context, set intent,
close stdin, allow a short bounded grace period (initially two seconds), then kill and
await exit if needed. Drain both streams through EOF. Repeated cancellation and
shutdown must act on the captured child, never a subsequently launched child. Add a
short bounded post-result exit deadline as well: a child cannot hold the queue forever
after declaring completion. Do not run blocking `wait`, `join`, or `readline` on the
GUI event loop. Test whether backend descendants can outlive the phase worker; if
they can, use a narrowly scoped process-group/job-object cleanup strategy supported
by that platform, not broad process-name killing.

## 7. Completion, cancellation, and publication contract

Apply the review plan's staged publication/recovery changes before or together with
this transport migration. They solve correctness issues that changing launch APIs
does not solve.

- The parent persists its output ownership before launch. Allocate against both existing
  archive directories and output IDs reserved by other persisted jobs. Stage files outside
  the visible archive under `TRANSCRIPT_DIR/.pending/<job_id>`, on the archive filesystem
  so the final rename is atomic. Archive enumeration must exclude `.pending`.
- The worker finishes all output files, attempts any requested export from complete
  staging, and writes a completion marker last with identity, duration, and warnings.
  It never publishes directly into the canonical archive. The marker is also proof
  that the optional export attempt has finished, successfully or with a warning.
- Normal success needs the expected terminal result, a clean exit, and validated
  staged output/checkpoint. A success record alone does not prove a clean exit.
- The parent publishes the complete directory, saves `DONE`, then removes uploads and
  work files. A queue-save failure preserves recovery data and pauses scheduling.
- A restart can reconcile a completed directory/marker with the recorded identity
  after a crash between publication and the queue save. Never delete a completed
  archive solely because the last queue status is still running.
- Reconcile completed output before checking source existence or checkpoint validity;
  a missing original recording does not invalidate an already completed result.
- A preexisting destination is reusable only when its marker proves matching ownership;
  never overwrite an unrelated archive. Queue JSON and directory publication are two
  writes with recovery between them, not a filesystem-wide atomic transaction.
- Keep the best-effort export in the final worker phase so it adds no blocking copy,
  second manifest update, or export task lifecycle to the parent. No copy starts before
  staging files are complete. A copy error becomes a warning in the readiness marker.
  Killing the worker during the copy leaves no readiness proof; retain checkpoints and
  rebuild final output on retry without repeating valid inference. An external partial
  copy is not a committed archive and must not authorize overwriting unrelated files.

Preserve the intended cancellation race semantics explicitly: a completed final job
wins a late cancel; a completed phase 1 awaiting diarization can remain cancelled with
its raw checkpoint reusable. When cancellation/parent death cuts off the success
event, use the durable completion marker under the same review-plan reconciliation
rules. A partial checkpoint or staging directory never counts as completed work.
Unexpected nonzero exit after a result is reported as a process failure during live
execution; retain any valid completed artifacts for reconciliation rather than deleting
them. This prevents a transport anomaly from silently destroying valid work.

## 8. Public CLI uses the same executor without draining the queue

Refactor `aTrain_core/cli.py` after the new worker passes its process tests. Preserve
all current transcription options/defaults, input validation, human-readable progress,
success message, and `load`/`remove` behavior. Keep the real source path unchanged;
sanitize only display/output names. Inputs with spaces and non-ASCII names must work.

Add a narrow `QueueService.run_one(spec)` lifecycle path, backed by the same phase
execution and publication code as normal scheduling:

1. Acquire the same `QueueLock` used by the GUI before loading/recovering mutable state.
   On contention, report that another owner is active and exit without changes.
2. Load the store under the lock and durably add this CLI job. Do not start `_scheduler`
   and then pause it; that introduces a race with existing queued jobs.
3. Execute only this job through the same `_run_job` path, which runs its phases. Do not
   select `_head()`, resume unrelated interrupted jobs, or reorder existing entries.
4. Keep failure/checkpoints as ordinary queue records so a later GUI session can
   inspect or retry them. Successful CLI jobs use the same archive and cleanup rules.
5. Return an exit code based on this job's outcome; a failed export remains a warning.
   On Ctrl-C, await cancellation/reaping and preserve retryable work before release.
6. Release the lock in `finally`, after child cleanup. Share lock/open/close helpers
   with normal startup instead of implementing a second owner in the CLI module.

The public CLI is therefore an orchestrator for one submitted job; the internal
phase worker is an executor under that orchestrator. It must never call the old
`transcribe()` implementation, acquire a second queue lock, or create nested model
processes. Do not solve lock contention by quietly running outside the queue root.

## 9. Commit sequence and dependencies

1. **Prove packaged launch.** Add only the worker smoke entry path and test harness;
   record successful launch commands and stdio behavior for each build target.
2. **Land shared correctness foundations.** Lock-first loading, atomic retry, checkpoint
   validation, phase ownership, and publication/reconciliation from the review plan.
   Enforce CLI/GUI lock exclusion before relying on the parent to reserve output names.
   Skip its temporary `Pipe.recv` repair if the CLI migration lands in the same change.
3. **Separate phase work from transport.** Make phase functions return one structured
   result and emit only progress through a callback; consolidate thin wrappers and
   retain injected Python factories for direct tests. Do not retain two result models.
4. **Implement internal worker.** Request validation, bounded NDJSON, stdout isolation,
   EOF watchdog, explicit exit, and lazy imports; exercise with test-owned fake workers.
5. **Implement async transport and switch the queue.** Replace launch calls, remove pipe
   polling, integrate the single owner and cancellation contract, and run queue/UI tests.
6. **Move the public CLI.** Add scoped `run_one`, preserve options, prove lock exclusion
   in both directions, and prove existing queued jobs never execute incidentally.
7. **Remove duplication and ship.** Delete obsolete process/event/factory machinery,
   migrate remaining callers, remove splash preloading, update docs and packaging,
   then run the final cross-platform smoke matrix.

Use one reviewable migration branch or a short ordered series. Temporary adapters
must be removed in the last commit. Do not leave a permanent runtime switch selecting
between old and new transports. Resolve supported-distribution launch requirements
in the feasibility gate; unresolved support means the migration is not finished.

## 10. Failure and recovery matrix

| Trigger | Expected behavior |
| --- | --- |
| Launch raises / request write fails | Reap any started child, retain ownership until then, fail the job through one path; release no running work silently. |
| Cancel/stop arrives while async launch is pending | Retain the pending context, reap the eventual process before sending work, and start no successor until cleanup completes. |
| Invalid/oversized request | Worker emits a bounded failure when protocol setup permits, exits nonzero, loads no model. |
| Malformed/oversized/duplicate stdout event | Kill/reap child, include bounded stderr context, fail protocol; do not interpret log text as success. |
| Stderr flood or fragmented stdout line | Memory remains bounded; both streams drain; UI heartbeat/cancel still runs. |
| Valid result then nonzero exit / hang | Process failure or bounded forced termination; retain validated artifacts for reconciliation. |
| Zero exit without terminal result | Unexpected worker termination; checkpoint/marker recovery applies, not unconditional success. |
| Model load/inference error | One failed result with step and bounded traceback; keep earlier valid checkpoints. |
| Cancel before final output is complete | Reap child, persist cancelled, retain valid checkpoints, discard only known incomplete staging. |
| Cancel races with complete final output | Shared reconciliation determines completion; finished archive survives. |
| Parent is force-killed | Stdin EOF watcher exits busy child; next owner recovers from durable state and markers. |
| Queue save fails while processing result | Stop/reap child if necessary, keep context until exit, pause scheduling, preserve artifacts and diagnostics. |
| Publish succeeds, final queue save fails | Complete archive remains readable; restart recognizes its identity and finishes state reconciliation. |
| Export copy fails | Archive remains successful; persist/report a warning. |
| CLI starts while GUI owns lock, or vice versa | Second owner fails cleanly without loading models or mutating queue/work files. |

## 11. Meaningful validation

Adapt `tests/core/test_runner.py`, `test_runner_process.py`, `test_runner_import_light.py`,
`test_runner_e2e.py`, `tests/core/test_queue_service.py`, `tests/core/test_outputs.py`,
`tests/unit/test_queue_lock.py`, and the relevant queue UI tests. Add focused worker
protocol and public CLI tests where existing files do not cover these boundaries.

Use three complementary layers:

- Direct phase tests inject callable fake transcriber/diarizer factories and inspect
  real checkpoints/output files. Cover checkpoint reuse without loading a model.
- Real subprocess tests launch a test-only module under `tests/fakes/` that calls the
  production worker entry function with fake factories. The parent transport accepts
  a test command callable; production requests expose no `module:factory` escape hatch.
  Extend `tests/fakes/runner.py` or add a small adjacent entry module rather than
  depending on monkeypatches propagating into fresh interpreters.
- Real packaged smoke tests execute the installed/frozen worker through the actual
  command selector. Verify import-light startup, one successful tiny job, both phases,
  cancellation, parent kill, no window flash, and no accidental GUI startup.

Required behavioral cases include missing source, changed source, corrupt transcript
structure, malformed JSON, Unicode paths/prompts, progress with zero totals, failed
output/export writes, duplicate results, short writes/partial lines, stdout native
print contamination, stderr beyond its cap, all cancellation races, and a forced parent
kill while the child emits no progress. Assert no child remains and the next queued job
starts only after reaping the previous child.

Gate async process creation in a deterministic test and cancel/stop before it returns;
assert that the created process receives no work and is still reaped. Update existing
archive-directory-count E2E assertions to exclude reserved `.pending`, while retaining
strict checks that every visible archive has complete expected files and metadata.

Keep an asyncio heartbeat active while a test worker slowly emits a large split record;
assert the loop continues ticking without timing thresholds tight enough to flake on
CI. Use fault injection around publication and queue saves to verify recovery, not
merely mocked call ordering. Test the public CLI with preexisting queued jobs and
assert their state/work files remain unchanged. Test help/imports in a headless wheel.

Run the repository's existing targeted pytest commands and formatting/lint checks
for changed files. Reserve real-model/GPU runs for a small release smoke matrix:
transcription-only, transcription plus diarization, cancel, and checkpoint retry on
each supported backend/device family. Record unavailable platforms as unverified;
Linux subprocess success alone does not validate Windows or macOS packaging.

## 12. Removal checklist and definition of done

- Remove queue use of `multiprocessing`, `Connection`, `BaseProcess`, `POLL_INTERVAL`,
  `_drain`, `_load_factory`, `phase1_main`, `phase2_main`, and the multiprocessing parent
  watchdog. Keep unrelated multiprocessing usage only where it still serves a caller.
- Remove `PhaseFinished`, `PhaseError`, `PhaseDied`, and redundant job IDs from per-child
  events (`JobFileId` is already gone); keep a single phase result and process exit
  fallback.
- Remove duplicate legacy CLI inference/process code and obsolete imports after checking
  all repository callers/tests; preserve confirmed supported public compatibility only.
- No queue mutation occurs in workers; all user entry points obey the same lock.
- One active context owns cancellation and cleanup through process exit and commit.
- All required protocol, queue, UI, checkpoint, and publication failure tests pass.
- Installed and supported packaged builds pass the feasibility/smoke matrix.
- Transcription and diarization never hold model processes concurrently for one queue.
- Queue/UI imports and CLI `--help` do not load torch, faster-whisper, pyannote, or GUI
  libraries unnecessarily; execution loads those dependencies only where needed.
- All protocol/stderr buffers have tested bounds; no blocking process read/wait occurs
  on the GUI loop; no background child survives parent death in the tested matrix.
- Record before/after production line counts and the removed classes/event types/
  execution paths. Judge simplicity by fewer owners and duplicated paths as well as
  line count; do not remove recovery or process isolation merely to meet a number.

The transport/event work here supersedes the review plan's multiprocessing receive
fix and its event simplification. UI confirmation safety, batch mutations, and other
independent review fixes remain necessary (the paused-state display is already fixed). Implement shared
publication and checkpoint changes once, with both plans referring to that result.
