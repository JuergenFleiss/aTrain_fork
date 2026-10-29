# Job and queue review: implementation plan

Status: proposed implementation plan; no implementation is included in this document.
Repository baseline: `45db5aa`, reviewed on 2026-10-04.

Updated 2026-10-06. Since the baseline, the queue UI moved onto the transcribe page
(`95e6c05`: `aTrain/components/queue_status.py`, tested in
`tests/ui/test_transcribe_queue.py`), and the phase statuses were collapsed. A job is now
`QUEUED`, `RUNNING`, `DONE`, `FAILED` or `CANCELLED`. `QueueService._run_job` runs the
transcription child and then the speaker-detection child, and the children decide what
to reuse from their checkpoints. That removed `TRANSCRIBING`/`TRANSCRIBED`/`DIARIZING`,
the `ALLOWED` transition table, `resume_status`, `JobTranscribed` and `_current_step`,
and fixed R9. The phases below are updated to match.

Later the same day:
- Outputs are published by rename (part of Phase 4; see its status note).
- `progress` and `cancelling` moved from `JobState` onto the service; one boolean
  `cancelling` replaced `_cancel_requested`.
- The file input holds only paths. Browser files are uploaded into
  `queue/uploads/<job id>/` as soon as they are added, and desktop windows pick paths
  with their own dialogs. `QueueService.start` deletes upload folders that no job
  references (files added on a page that was closed before "Add to queue").
- Duplication was removed: one atomic JSON writer (`write_json_atomic` in `globals.py`), one `allowed_extensions()`,
  one `hms()` (also in `globals.py`), `seed_defaults` as the single source of the advanced defaults, shared button
  props, `EventProgress` as a `dict`, `pick_native` in `flatpak_portal`. The confirm bar is
  one awaited `confirm()`, and commands refresh the list through `update()`.
- Two bugs were fixed: the selection is kept when the jobs can't be added, and a cleared
  CPU-threads field no longer breaks adding jobs.
- Dead code was removed: the `/queue` redirect, the `zone.selection` test hook, the
  `QueueLock` context manager, the `clear_finished` return value, a stale re-export, and
  the model-grouping leftovers in `ModelKey`/`JobSpec.model_key`.

## Objective and scope

Resolve all nine findings from the job/queue review while reducing duplicated execution,
overlapping lifecycle state, and unnecessary persistence work. Preserve the sequential
queue, JSON persistence, OS ownership lock, checkpoints, and separate transcription and
speaker-detection processes. A database, queue framework, new background server, or a
general-purpose workflow abstraction is not needed.

The related [CLI worker implementation plan](cli-worker-implementation.md) changes the
process transport. These are coordinated plans, not two independent implementations:
the persistence, publication, ownership, UI, and recovery changes below apply to either
transport. If the CLI plan is selected, use its worker protocol and subprocess reader in
place of the multiprocessing-specific work in phase 5. Do not retain two production
runners, or build an elaborate transport abstraction merely to support the migration.

## Required invariants

1. One owner holds the same queue lock for GUI and public CLI execution. Workers do not
   acquire that lock independently or write `queue.json`.
2. A launched child remains owned, cancellable, and protected from removal until it has
   exited and been reaped. A saved job status does not establish that a child has exited.
3. State changes become visible only after their save succeeds. A persistence failure
   pauses scheduling, preserves recoverable artifacts, and cannot orphan a child.
4. No new phase starts while paused, stopping, or still responsible for an earlier child.
5. Checkpoints are reused only when their contents and source identity are valid.
6. The archive exposes completed directories. Incomplete outputs live outside its normal
   listing, and a crash cannot turn a completed result into disposable partial output.
7. Destructive confirmations apply to the IDs shown when the dialog opened. Original
   files outside queue-owned upload/work directories are never deleted.
8. There is one shared phase implementation, one current-phase owner, and one terminal
   result per phase. Process exit remains a separate fact that must be observed.

## Finding-to-delivery map

| ID | Review finding | Main delivery | Acceptance evidence |
| --- | --- | --- | --- |
| R1, P2 | Persistence failure loses a live child | Phases 2 and 3 | Inject event-save failure; cancel/reap works and removal stays blocked |
| R2, P2 | Clear finished exceeds confirmed selection | Done (Phase 1) | A job finishing during the dialog is retained with its upload |
| R3, P2 | Incomplete archive output and publication race | Phase 4 (partly done) | Archive stays readable; recovery succeeds at each publication boundary |
| R4, P2 | Store recovery mutates before lock; broad load exception | Phase 2 | Competing owner and access/schema errors leave queue bytes untouched |
| R5, P2 | CLI bypasses lock and duplicates execution | Phases 1 and 6 | Both entry points exclude each other and share execution |
| R6, P2 | Blocking pipe receive freezes event loop | Phase 5 or CLI plan | Delayed partial event does not prevent heartbeat/cancellation |
| R7, P2 | Invalid checkpoint poisons every retry | Phase 2 | Invalid structure recomputes; valid checkpoints avoid model loading |
| R8, P2 | Retry clears diagnostics before status save | Phase 2 | Failed retry commit leaves previous status and diagnostics intact |
| R9, P3 | Paused inter-phase job appears active | Done (status collapse) | A job paused between its children is `QUEUED` and counts as waiting |

## Phase 0 — Establish a focused regression baseline

Touchpoints: `tests/unit/test_job_store.py`, `tests/unit/test_queue_lock.py`,
`tests/core/test_queue_service.py`, `tests/core/test_runner_process.py`,
`tests/core/test_outputs.py`, `tests/ui/test_transcribe_queue.py`,
`tests/unit/test_archive.py`.

- Add a regression for each concrete failure as its fix is implemented. Use fake model
  loaders, temporary user directories, explicit synchronization gates, and injected save
  failures. Do not reproduce races with arbitrary multi-second sleeps.
- Record current CLI options, archive filenames/metadata, retry behavior, pause semantics,
  and cancellation behavior as compatibility requirements before changing the runner.
- Keep cancellation's existing useful precedence: a verified completed final output can
  win a racing cancellation; a raw transcription checkpoint alone does not authorize
  starting speaker detection after cancellation. State this explicitly in test names.
- Capture a small before/after count of production modules, event types, execution paths,
  lifecycle fields, and queue saves for a bulk action. Do not optimize solely for line count.

Exit criterion: every review finding has a named regression scenario and an assigned phase.

## Phase 1 — Ship small independent correctness fixes

Touchpoints: `aTrain/components/queue_status.py`,
`aTrain_core/queue_service.py`, `aTrain_core/jobs.py`, `aTrain_core/cli.py`,
`aTrain_core/globals.py`, and the corresponding queue UI/lock tests.

### Bind clear-finished confirmation to its selection (done)

Done: the dialog passes the ids it showed to `QueueService.clear_finished(ids)`, and the store
removes only those that are still final. `test_clear_finished_keeps_jobs_that_finished_while_asking`
covers it. The steps below are the original plan.

1. Snapshot finished job IDs and the upload warning from the same selected records.
2. Pass those IDs through `QueueService.clear_finished(ids)` to the store.
3. On confirmation, remove only selected IDs that still exist, are final, and are not
   owned by the current phase. Skip removed jobs and jobs retried while the dialog was open.
4. Save the filtered queue once, then clean only the removed IDs' owned files. Return
   actual removed IDs for tests and any feedback; do not recompute an unrestricted set.

### Correct the paused summary (done)

Fixed by the status collapse: pausing between a job's two children puts it back to
`QUEUED`, so the panel counts it as waiting and shows no device text or stop action.
`test_pause_during_transcription_does_not_start_phase_2` covers pausing during phase 1,
the return to `QUEUED`, and resuming through phase 1 (checkpoint reuse) into phase 2.

### Close CLI ownership immediately

- Centralize the queue root in core configuration instead of importing it from GUI code.
- Acquire `QueueLock` around the entire public CLI transcription operation, before output
  directory creation, model loading, or any queue recovery. Release it in `finally`.
- This is an interim safety fix until phase 6 moves CLI execution onto the shared service.
  The final CLI must not take a second nested lock around a service that already owns it.
- Test GUI-owner/CLI-contender and CLI-owner/GUI-contender using separate processes.

Exit criterion: R2 and R5's exclusion gap are fixed without changing process transport.

## Phase 2 — Make persistence and retry decisions atomic

Touchpoints: `aTrain_core/jobs.py`, `aTrain_core/queue_service.py`,
`aTrain_core/outputs.py`, `aTrain/utils/queue_ui.py`, `aTrain/pages/transcribe.py`,
and store/checkpoint/service tests.

### Load and recover only after ownership

1. Make `JobStore.__init__` establish paths and an empty in-memory collection without
   loading, renaming, or recovering `queue.json`.
2. In `QueueService.start`, acquire the lock, load, reconcile recoverable work, and only
   then start scheduling. Release the lock on every startup exception; publish the GUI
   singleton only after successful startup. Commands must not mutate an unstarted store.
3. Treat only an actually missing queue file as an empty queue. Distinguish unsupported
   schema, malformed JSON/validated record structure, and filesystem errors.
4. Propagate unsupported-version and permission/I/O errors with actionable messages;
   preserve the original bytes and do not silently replace them with an empty queue.
5. Preserve existing corruption recovery only for positively identified malformed data,
   under the acquired lock: move it to a unique, non-overwriting diagnostic backup and
   report that recovery occurred. If backup creation fails, fail startup without resetting.
6. Catch expected parse/validation exceptions narrowly. Programming errors must not be
   classified as corrupt user data. Keep schema version 1 unless an actual field change
   makes migration necessary; the proposed ownership refactor alone does not require one.
7. Surface expected startup/load failures on the transcribe page with their
   actual cause. Keep other pages usable and leave the singleton unset so a later attempt
   can retry. Do not present permission/schema failures as another-instance lock contention.

### Commit compound commands once

- Add a small store operation for validating and committing a batch of proposed state
  changes. Reuse `_save`; update live state references only after success. Avoid a public
  transaction framework or deferred mutation objects.
- Retry saves `QUEUED` together with diagnostic resets, timestamps, warnings, and any
  changed output identity in one write. No resume state is computed: the children
  decide what to reuse from the checkpoints. Failed save means
  the old failure and diagnostics remain available. Do not delete recovery files first.
- Cancel all updates waiting selected jobs in one save; cancellation of the active phase
  is captured separately and handled by phase ownership. No-op batches need no write.
- A failed bulk save pauses scheduling; still stop an explicitly cancelled active child.
  Report that waiting-job changes were not persisted rather than claiming full success.
- Persist removal before owned-file deletion. Cleanup errors do not roll back queue state;
  log them and allow safe subsequent cleanup without deleting sources outside owned roots.

### Reject unusable checkpoints

- Validate the top-level mapping, source size/mtime fields, finite nonnegative duration,
  transcript mapping, and `segments` list. Validate the fields consumed downstream:
  text and finite ordered timestamps, plus optional word/speaker structures when present.
- Allow empty transcripts and valid backend-specific optional fields. Reject booleans
  masquerading as numeric times and non-finite JSON numbers; do not require unused fields.
- Return a cache miss for malformed or stale content so phase 1 recomputes. A malformed
  diarized checkpoint reuses the valid raw transcript and reruns speaker detection.
- Keep source-stat comparison and changed-during-decode detection. Document whether an
  unreadable checkpoint is a cache miss or a reported I/O error; it must not loop on a
  known-invalid structure. Avoid a new schema-validation dependency for these few checks.

Exit criterion: R4, R7, and R8 pass; cancelling 100 waiting jobs performs one full save.

## Phase 3 — Consolidate ownership and failure handling

Touchpoints: `aTrain_core/queue_service.py`, `aTrain_core/runner.py`,
`tests/core/test_queue_service.py`, `tests/core/test_runner_process.py`.

1. Replace `_handle`, `_in_flight`, and `_phase_error` with one small current-phase
   context containing job ID, phase, handle, cancellation intent, and an optional
   outcome. The cancellation intent is already one boolean, the public
   `QueueService.cancelling` (only one child runs at a time). The phase is the public
   `QueueService.step`, which the UI reads for "Step x of 2".
   `_run_phase` currently reports a completed phase 1 by `_in_flight` still naming the
   job after the child ends; the context's outcome replaces that signal.
2. Done in part: `JobState` no longer has `cancelling` or `progress`. The UI reads
   `QueueService.cancelling` and `QueueService.progress`; derive them from the context
   rather than keeping a second authority.
3. Own the child from successful launch through event consumption, termination if needed,
   and confirmed reap. Receiving success/failure records does not clear ownership.
4. Handle event application, worker failure, and persistence failure explicitly inside
   `_run_phase`. Remove `_guarded` after converting its call sites to specific handling.
5. On save failure, pause scheduling immediately, retain ownership, terminate/reap the
   child if still running, preserve its files, and expose an in-memory error. A second
   failure while saving that error must not erase the first failure or start another job.
6. Have removal and clearing consult current ownership even if displayed status is final.
   Cancel and stop capture the owned handle before yielding; they cannot kill the next job.
7. Release the queue lock only after no child remains. A timeout while killing/reaping
   must be surfaced; do not silently clear ownership and unlock with a live worker.
8. Finalize one outcome after reconciling worker result, cancellation, artifacts, and exit.
   Clear the current context in one final cleanup path after reap and outcome handling.

Exit criterion: R1 passes, late events cannot affect another job, and repeated stop/cancel
does not orphan a process or release ownership too early.

## Phase 4 — Publish complete output through one recoverable path

Touchpoints: `aTrain_core/outputs.py`, `aTrain_core/runner.py`,
`aTrain_core/queue_service.py`, `aTrain_core/jobs.py`, `aTrain/utils/archive.py`,
`tests/core/test_output_steps.py`, `tests/core/test_outputs.py`, and archive/service tests.

Status, 2026-10-06: partly done.

- **Done:** the writers take an explicit directory (step 1). The phase child picks a free
  `file_id` (`outputs.free_file_id`), writes everything into
  `TRANSCRIPT_DIR/.pending/<file_id>/` (step 3; `read_directories` skips dot-folders), and
  moves the folder into the archive with one rename on the same file system
  (`outputs.publish`, which refuses an existing folder). `JobDone` carries the
  `file_id`. `JobFileId`, `_drop_incomplete_output` and the empty reserved archive folder
  are gone, so a crash can no longer leave a partial archive folder or delete a complete
  one.
- **Not done:** the parent doesn't reserve the `file_id` (step 2), and there is no
  readiness manifest or reconciliation (steps 6–8). A crash between the rename and saving
  `DONE` makes a retry publish a second folder. `.pending` is keyed by `file_id`, not job
  ID, and is emptied before each output write, which is safe while one owner writes.

### Prepare and publish

1. Replace implicit `TRANSCRIPT_DIR / file_id` writes with an explicit output directory
   passed through the existing metadata, JSON, text, subtitle, and log helpers. Keep
   formatting logic shared; temporary compatibility wrappers must have a deletion step.
2. The owner chooses a collision-free final `file_id` under the common execution lock and
   saves it before launching a phase that can write final output. Reserve by durable
   identity, not by creating an empty visible archive directory. Exclude both existing
   archive directories and IDs reserved by any persisted job, including unrelated jobs
   that public CLI run-one mode leaves untouched. Retain friendly naming.
3. Stage output in `TRANSCRIPT_DIR/.pending/<job_id>/`, with `.pending` explicitly excluded
   by `read_directories`. This guarantees publication stays on one filesystem even if
   queue work and archive roots are configured differently. Checkpoints stay in work.
4. Pass the target identity and staging directory to the worker. Write every archive file,
   final metadata, processing time, and log before declaring the directory ready.
5. Preserve optional export behavior as best effort. The worker attempts the copy from
   complete staging and collects warnings before declaring readiness. Copy failure is a
   warning; interruption before readiness preserves checkpoints so retry need not rerun
   inference. External partial copies are outside canonical archive publication. Retry may
   reuse this job's external target but must warn on unrelated targets without overwriting
   them. Export is not an exactly-once operation or an atomic filesystem transaction.
6. The worker writes a small readiness manifest last, atomically, containing owning job
   ID, file ID, result duration/warnings, and required artifact names. There is one manifest
   write with the completed export outcome; no separate export-pending state is needed.
7. After worker exit/reap, the owner validates identity, required files, and output/metadata
   structure, then atomically renames staging to the final directory. No recursive content
   hashing is needed. Never overwrite an unrelated destination: under the single
   owner, an existing destination must have this job's valid manifest or cause a conflict.
   (Done: the queue path no longer uses `claim_file_id`, and `JobFileId` is gone.)
8. Save `DONE`, final identity, duration, warnings, and finish time. Only after that save
   succeeds remove work checkpoints and uploaded input. Never rewrite published metadata.

The directory rename and `queue.json` update are two operations, not one filesystem
transaction. The manifest and persisted identity make the gap recoverable. Preserve
existing file flush/fsync guarantees; add directory sync where supported if promising
power-loss durability. Test process-crash recovery separately from power-loss guarantees.

### Reconcile startup, retry, and cancellation

| Durable artifacts at interruption | Recovery under the owner lock |
| --- | --- |
| Reserved ID, no ready staging | Keep checkpoints; remove only owned incomplete staging; resume |
| Ready staging, no final directory | Validate identity/artifacts; publish and mark done |
| Valid final directory, job not `DONE` | Adopt existing result and save `DONE`; do not delete or regenerate |
| `DONE`, owned upload/work remains | Finish idempotent owned-file cleanup |
| Existing target belongs to another job | Preserve both; report conflict without overwrite |
| Legacy non-final `file_id` without readiness proof | Preserve positively owned output under `.pending/legacy-<job_id>/` for inspection; resume into a fresh target |

- Run reconciliation before source-existence checks, requeueing, or cleanup. A ready
  result remains recoverable after the source has moved or a completed job's upload has
  already been deleted. (`_drop_incomplete_output` is already gone.)
- Reconciliation must also inspect cancelled jobs: verified complete final output wins a
  racing cancellation; raw checkpoints merely preserve work and do not trigger phase 2.
- Retain completed artifacts when saving `DONE` fails, pause the queue, and prevent a
  retry from deleting them. Reconcile again before retrying, removing, or clearing that job.
- The store no longer checks transitions (the `ALLOWED` table went with the phase
  statuses), so nothing blocks adopting a `FAILED` or `CANCELLED` job directly to `DONE`.
  Keep that adoption on the reconciliation path, after validated completion evidence;
  test that an incomplete directory cannot promote a failed/cancelled job.
- Done: `_phase_died` labels a crash with the current phase's `step`; nothing infers the
  output step from `file_id` any more. Failure results keep their explicit step.
- Preserve pre-existing completed archives without manifests. Do not scan and delete
  arbitrary archive directories or uploads merely because no queue record references them.

Exit criterion: R3 passes at every listed interruption point, with no partial archive
listing, duplicate completed result, destructive recovery, or lost upload before commit.

## Phase 5 — Simplify events and keep receives off the event loop

If implementing the CLI plan, use its JSON event stream and `asyncio` subprocess reader
instead of the following multiprocessing changes; retain these lifecycle acceptance rules.

Touchpoints: `aTrain_core/runner.py`, `aTrain_core/queue_service.py`,
`tests/fakes/runner.py`, runner/service/process/import-light tests.

- Use progress plus one terminal result representing transcribed, output-ready, or failed.
  Include the actual failed step and diagnostic text in failure results. Remove overlapping
  `PhaseFinished`, `PhaseError`, and job-specific completion layers once callers migrate.
  `JobFileId` is already gone; `JobDone` carries the `file_id`. Today a completed phase 1
  of a speaker-detection job sends no result: `JobTranscribed` went with the phase
  statuses, and `PhaseFinished` without `JobDone`/`JobFailed` means "transcribed".
  Removing `PhaseFinished` therefore needs the explicit transcribed result. It changes no
  saved status; `_run_job` uses it to start phase 2, or to requeue or cancel the job.
- Let the parent synthesize an unexpected-exit failure when no terminal result exists;
  exit code zero without a result is still incomplete. Reconcile ready artifacts for the
  small crash window after writing them but before delivering the result.
- Do not call `Connection.recv()` on the event loop after `poll()`. Perform blocking receive
  outside the loop, for example one awaited `asyncio.to_thread(conn.recv)` at a time, until
  EOF. Close unused pipe ends and reap/close consistently so death unblocks the reader.
- Continue reading through completion/EOF so the child cannot block on an undrained pipe.
  Handle partial/truncated payload, EOF, cancellation, and receiver failure explicitly.
- Associate a private channel with its job in the parent; remove redundant event job IDs.
  Remove unused wire `JobProgress.task`; retain any local progress mapping keys required
  by model APIs. Keep progress throttling to avoid an unnecessary traffic increase.
- Inline thin public/private phase wrappers and pass importable top-level loader callables
  instead of string-based factory resolution. Keep fake loader injection out of user settings.
- Preserve the parent-death watchdog and forced-exit workaround unless targeted process
  tests show a replacement provides the same behavior. Do not assume ordinary shutdown
  always releases model resources promptly.

Exit criterion: R6 passes with a delayed partial payload; cancellation, EOF, crash, and
parent death all leave no child running. There is one production event protocol.

## Phase 6 — Remove duplicated execution and GUI scaffolding

Touchpoints: `aTrain_core/cli.py`, `aTrain_core/transcribe.py`, `aTrain_core/runner.py`,
`aTrain/utils/queue_ui.py`, `aTrain/utils/transcription.py`,
`aTrain/components/splash_screen.py`, `aTrain/components/queue_status.py`, UI fixtures/tests.

- Route public CLI transcription through the shared queue/phase implementation. Use a
  narrowly scoped run-one mode so invoking one file does not unexpectedly execute other
  persisted queued jobs; preserve their order/state. The CLI plan specifies this integration.
  If retaining multiprocessing, use the same policy with its existing launcher.
- Preserve public CLI arguments, useful progress/errors, exit status, output formats, and
  checkpoint recovery. Remove legacy `prepare_transcription`/`transcribe` orchestration
  after migrating all call sites and tests; preserve genuinely shared output/engine helpers.
- Remove the old inference imports from the GUI splash. Check remaining real consumers
  before removing `torch` startup loading; keep lightweight capability checks if needed.
- Move event-loop test resets into fixtures that await service shutdown. Production must
  not inspect test loops or reach into another service's private `_lock`.
- Done: `build_spec_from_state` accepts `export_dir`, and the upload/path adapter is gone.
  Browser files are uploaded into `queue/uploads/<job id>/` as soon as they are added, so
  `FileSelection` holds only paths; desktop windows pick paths with their own dialogs.
  Keep the settings snapshot in `start_paths`.
- Keep the existing modest UI polling mechanism, initialize its signature after first
  render, and route command/timer refreshes through one signature check. Do not add a new
  reactive framework. Preserve the small sync/async confirmation adapter.
- Done: the scheduler no longer inspects checkpoints. Every resume, retry and restart
  goes through phase 1, which reuses a valid raw checkpoint and exits without loading
  Whisper. This costs one short process start on a diarization-only resume and removed
  two statuses, `resume_status` and the parent-side checkpoint read.

Exit criterion: one execution implementation serves GUI and CLI; imports and UI lifecycle
are simpler without changing upload handling or launching unrelated jobs.

## Phase 7 — Validate the integrated result and remove migration remnants

| Area | Required acceptance scenarios |
| --- | --- |
| Persistence | Save failures preserve old state; no pre-lock mutation; unsupported schema preserved; startup failure unlocks |
| Bulk commands | One write for many waiting cancellations; failed commit deletes no files; selected clear survives dialog races |
| Ownership | Save error with live child; cancellation during launch/result/reap; stop twice; child cannot survive owner death |
| Scheduling | Sequential jobs; no overlap between phase models; pause between phases; retry preserves queue order |
| Checkpoints | Empty valid transcript; null/wrong structure; invalid times; changed source; raw and diarized reuse independently |
| Publication | Fault after each reserve/write/ready/rename/save/cleanup boundary; collision; legacy output; export-copy warning |
| Transport | Large/partial event; EOF without result; worker load crash; result-before-cancel; no blocked UI heartbeat |
| Entry points | Lock exclusion both directions; CLI option/output parity; run-one leaves other jobs untouched; light GUI imports |
| UI | Correct running/waiting counts; captured clear selection; upload warning matches deletions; one initial render |

- The `ALLOWED` table and its computed matrix tests were removed with the phase statuses.
  Cover lifecycle rules with concrete scenario tests (cancel at each point, pause between
  the children, retry, restart, reconciliation) rather than reintroducing a table.
- Run targeted suites after each phase. At integration, run unit tests plus queue, runner,
  engine/output, import-light, and queue UI suites. Run lint and format checks for changed
  Python files. Planning alone does not require or claim a new test run.
- Use the existing real-model CPU runner/CLI comparison for output parity when models are
  available; run a GPU two-phase smoke test for resource release. The CLI transport route
  additionally requires the packaged-platform smoke checks in its sibling plan.
- Update end-to-end assertions that compare raw archive `iterdir()`/glob differences to
  use committed-output listing that excludes only the reserved `.pending` directory;
  do not hide arbitrary incomplete output folders to make the assertions pass.
- Delete obsolete event classes, wrappers, string loader lookup, duplicate orchestration,
  stale tests/comments/imports, and temporary compatibility branches after cutover.

Focused integration commands, from the repository root in the prepared development
environment (add the new regressions to these suites as each phase lands):

```bash
.venv/bin/python -m pytest tests/unit/test_jobs.py tests/unit/test_job_store.py tests/unit/test_queue_lock.py tests/unit/test_archive.py
.venv/bin/python -m pytest tests/core/test_queue_service.py tests/core/test_runner.py tests/core/test_runner_process.py tests/core/test_runner_import_light.py tests/core/test_engine.py tests/core/test_outputs.py tests/core/test_output_steps.py
.venv/bin/python -m pytest tests/ui/test_transcribe_queue.py tests/ui/test_startup_imports.py tests/ui/test_boot_serve.py
```

Run `tests/core/test_runner_e2e.py` and `tests/core/test_transcription_e2e.py` separately
when their real models and any required credentials are available. Do not label a
fake-model subprocess run as validation of GPU memory release or packaged execution.

## Delivery order and definition of done

Phases 1 and checkpoint validation in phase 2 can proceed independently. Phase 2's store
semantics precede phase 3 ownership/error cleanup. Phase 4 depends on phases 1–3, especially
CLI exclusion; it must be complete before removing the old output-identity event. Phase 5
or the CLI transport replacement follows the agreed ownership/result contract. Phase 6
finishes shared execution and deletes legacy paths; phase 7 gates delivery. Small fixes
may ship first; do not postpone correctness while waiting for the CLI migration.

The work is done when all R1–R9 regressions pass, both interfaces execute through one
implementation, the archive is recoverably published, queue saves are atomic per command,
and no cancellation/error/shutdown can release a live child from ownership. Preserve old
completed archives and schema-compatible queues. Document any required compatibility
change explicitly. Report production code removed and remaining intentional complexity;
do not claim a net line reduction before measuring the final implementation.
