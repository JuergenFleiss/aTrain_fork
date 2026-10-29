# Shared job API and HTTP access: implementation plan

Status: proposed implementation; this document does not change application behavior.
Repository baseline: `45db5aa`, reviewed on 2026-10-04.

## 1. Objective and initial scope

Make one framework-neutral application API serve the existing UI, local CLI, and an
optional HTTP interface. Preserve process isolation and the existing small queue.
The HTTP interface supports running aTrain on another machine without requiring the
client to invoke a server-side CLI or share the server's filesystem.

```text
NiceGUI callbacks ──direct calls──┐
HTTP routes ─────────────────────┼──> QueueService ──> phase processes ──> engine
Standalone CLI ──run_one─────────┘
Remote CLI ──HTTP──> the same HTTP routes
```

The first release has one application process, one queue owner, and one trusted shared
workspace. Authenticated clients can see and operate all jobs and results in that
workspace. This is suitable for one user or cooperating users sharing recordings;
it does not provide private jobs between mutually untrusted users.

The [review implementation plan](job-queue-review-implementation.md) supplies mandatory
ownership, persistence, checkpoint, cancellation, and publication fixes. Retain its
repaired multiprocessing phase runner for this plan. The
[CLI worker plan](cli-worker-implementation.md) is an optional, independent transport
replacement; HTTP does not require it and does not replace child processes.

This plan supersedes [the earlier E8 proposal](future_extension.md#e8-http-api--server-mode)
for current implementation scope. Retain its opt-in, upload-only `/api/v1` direction;
do not carry forward group scheduling, nested ASR specs, `origin`/`delete_source_after`,
raw `JobSpec` responses, batches, partial outputs, rerendering, or automatic seven-day
archive deletion. Its one-release wait is an optional rollout milestone; passing the
review lifecycle/recovery tests before exposure is the required technical gate here.

Non-goals: multi-tenant accounts, billing, distributed execution, parallel GPU jobs,
Redis/Celery, a database migration, webhook delivery, live event history, and a public
model-management API. Add those only when an actual use case requires them.

## 2. Required invariants and decisions

1. One service owns the OS queue lock and every phase child; only it writes `queue.json`.
2. UI, local CLI, and HTTP invoke the same command validation and state transitions.
3. Accepted jobs outlive requests, browser sessions, and network connections.
4. HTTP accepts uploaded content and settings, never arbitrary server filesystem paths.
5. Responses are immutable snapshots; no mutable `JobState` or `JobSpec` escapes the
   application boundary. Worker progress is in-memory and need not force queue saves.
6. An HTTP submission is accepted only after both its input and queue record are saved.
7. Completed results are archive resources independent of queue rows; clearing the queue
   cannot silently revoke downloads or delete completed transcriptions.
8. A service shutdown retains child ownership and the queue lock until all children exit.
9. The initial API is disabled by default, including in local desktop builds. Enabling it
   requires authentication; loopback origin or a browser cookie is not implicit API trust.
10. Keep business rules and future workspace/ownership checks at the shared application
    boundary, not only in HTTP dependencies that direct UI calls bypass.

## 3. Smallest intended module structure

| File | Responsibility/change |
| --- | --- |
| `aTrain_core/queue_service.py` | Shared commands, snapshot queries, caller/workspace context, readiness, scoped local `run_one`, and phase ownership. |
| `aTrain_core/jobs.py` | Durable store, optional submission deduplication metadata, versioned migration, immutable snapshot projection helpers if small. |
| `aTrain_core/settings.py` | Typed complete submission settings and common validation; GUI storage shape is not the domain model. |
| `aTrain_core/submissions.py` — new | Framework-neutral staged-upload acceptance and cleanup; adapters provide bounded chunks/metadata. |
| `aTrain_core/results.py` — new | Safe completed-result listing/metadata/artifact lookup, shared with archive UI; no NiceGUI imports. |
| `aTrain_core/globals.py` | One queue-root configuration used by GUI, API, and local CLI. |
| `aTrain/api.py` — new | FastAPI router, HTTP DTOs, auth dependency, request limits, error mapping, and headless app factory; split only if it becomes difficult to read. |
| `aTrain/server.py` — new if needed | Minimal headless server command/ASGI factory; omit if the CLI and `api.py` already provide a clear entry point. |
| `aTrain/app.py` | Explicit API opt-in, route registration, single owner startup/shutdown wiring, headless `serve` command. |
| `aTrain/utils/queue_ui.py` | Retrieve the lifespan-owned service; no second lazy service startup or private lock access. |
| `aTrain/utils/transcription.py` | Thin NiceGUI upload/native-file adapters into shared submission methods; pass an explicit settings snapshot. |
| `aTrain/components/settings/*.py`, `aTrain/pages/transcribe.py`, `aTrain/pages/advanced.py` | Bind settings to client/user state rather than `app.storage.general`. |
| `aTrain/utils/archive.py`, `aTrain/pages/archive.py` | Reuse result queries and safe artifact selection; retain UI-specific download/open-folder behavior separately. |
| `aTrain_core/cli.py` | Local shared execution and explicit remote HTTP client mode; no legacy inference path. |
| `pyproject.toml`, `uv.lock` | Direct optional server/client dependencies, compatible pins, and installed-wheel coverage. |
| `README.md`, `docs/linux/service.md`, `docs/installation.md`, CI workflows | Explain modes, exposure/auth configuration, one-process deployment, and validation. |

Reuse the existing service instead of adding a parallel `JobManager`, repository layer,
HTTP-specific scheduler, or general command bus. Small frozen dataclasses and explicit
methods suffice. FastAPI/Pydantic types stay at the HTTP boundary; core tests and local
CLI imports must work without the server extra.

## 4. Shared application API and settings

Expose explicit operations on the existing service: submit a staged upload or trusted
local source, query jobs/queue status, cancel selected IDs, retry, remove unowned rows,
pause/resume, and run one submitted local CLI job. A small caller context identifies
the shared workspace and whether local filesystem submission is permitted. HTTP and
remote UI adapters cannot construct a privileged local-source operation from user input.
There is no role hierarchy or generic policy engine in this release.

Keep command decisions on the owning asyncio loop. Snapshot queries copy scalar values,
settings, warnings, and nested collections into frozen DTOs/serialized values before
returning; UI code must stop changing store-backed state references directly. Copying
does not imply a second mutable cache or a second persistence model.
Use `async def` route handlers for service calls; FastAPI's synchronous handlers run in
a threadpool and must not mutate the loop-owned service from that thread.

Every submission captures all effective settings: model, language, device, compute type,
CPU threads, temperature, initial prompt, speaker detection, and speaker count. Validate
supported values/ranges and model-language combinations before accepting the job.
Avoid importing torch/model libraries merely to parse HTTP requests or answer health
checks: perform actual device/model availability checks in the phase worker, or use a
cached startup capability check that does not block the request loop.

Replace per-submission use of `app.storage.general` with an explicit client/user settings
object. Pass that object into settings components and `start_uploads`/`start_paths`, then
snapshot it when Start is clicked. Preserve separate-browser settings across navigation
with NiceGUI's appropriately configured per-user storage; use page/client state for
transient values. Supply the required storage secret through configuration. Global
model inventory can remain shared. Test two clients changing different models/prompts.

The application boundary is the future place for ownership checks. If private accounts
are added, every UI/HTTP/CLI operation and result lookup must use an authenticated owner
context; adding authorization only to HTTP routes is insufficient.

## 5. HTTP contract: `/api/v1`

Use a small versioned router and JSON DTOs with explicit fields. Initially use polling;
do not add WebSockets or SSE solely to relay a progress percentage.

| Method/path | Request | Success semantics |
| --- | --- | --- |
| `POST /jobs` | Multipart: exactly one `file`, one JSON `settings` field; optional `Idempotency-Key` | `202`, accepted job snapshot and `Location: /api/v1/jobs/{id}` only after durable acceptance. |
| `GET /jobs` | `offset`/`limit`, optional status filter | `200`, bounded page of snapshots in queue order, total, current queue flags, next offset. |
| `GET /jobs/{id}` | None | `200`, latest job snapshot; `404` if absent. |
| `GET /submissions/{request_key}` | UUID key | `200`, retained job snapshot for lost-response reconciliation; `404` after its queue row/key is absent. |
| `POST /jobs/{id}/cancel` | Empty body | `202` if stopping a live phase; `200` if already final/cancelled or cancellation completed; return actual state. |
| `POST /jobs/{id}/retry` | Empty body | `202` after atomic reset/resume save; only failed/cancelled jobs; otherwise `409`. |
| `DELETE /jobs/{id}` | None | `204` after removing an unowned waiting or final queue row and its owned input/work files; preserve completed results. `409` while running/owned; absent row also `204`. |
| `GET /queue` | None | `200`, ready/paused/stopping, active job ID, counts, and sanitized service error if unavailable. |
| `POST /queue/pause`, `POST /queue/resume` | Empty body | `200`, idempotent queue control; pause allows the current phase to finish. |
| `GET /results` | `offset`/`limit` | `200`, completed archive resources independent of queue rows. |
| `GET /results/{result_id}` | None | `200`, safe metadata and allowlisted available artifact names; `404` if not completed/absent. |
| `GET /results/{result_id}/files/{artifact}` | One allowlisted name | Stream complete artifact with safe download headers; `404` if absent/disallowed. |

Also provide `/health/live` and `/health/ready`: minimal process liveness versus usable
queue ownership/recovery. Liveness can be unauthenticated without paths/version details;
protect readiness or return only its boolean status. Readiness returns `503` when startup
failed, ownership is unavailable, shutdown began, or persistence failure prevents work.
A deliberately paused healthy queue is ready to accept durable submissions.

Leave bulk clear, reorder, model downloads/removal, archive deletion, and raw log access
out of v1 HTTP. Existing local UI features remain. If exposing bulk deletion later,
accept an explicit list of selected IDs, never a moving "all finished" predicate.

Example settings field, containing every effective setting:

```json
{
  "model": "large-v3-turbo",
  "language": "auto-detect",
  "device": "cpu",
  "compute_type": "int8",
  "cpu_threads": 4,
  "temperature": null,
  "initial_prompt": null,
  "speaker_detection": true,
  "speaker_count": null
}
```

Job snapshots include ID, sanitized display name, effective settings, status, phase and
finite progress (for the running job, from `QueueService.step` and
`QueueService.progress`; the status no longer encodes the phase), timestamps, duration,
warnings, a safe error code/message, and optional `result_id`. Include neither `source`, `work_dir`, `export_dir`, nor raw tracebacks.
Do not serialize `JobSpec` wholesale. The HTTP upload path sets `export_dir=None`;
clients download results instead of requesting arbitrary server-side copies.

List requests default to 50 entries, with a maximum of 200; reject negative offsets or
larger limits. Each response is one consistent snapshot, with a server observation
timestamp. Pagination across multiple requests is explicitly a live view: inserts,
deletes, or reordering may shift offsets. Clients deduplicate by ID and restart polling
from the first page after mutations. No promised event ordering or historical progress.
Poll active jobs about once per second with backoff when idle/unavailable. Send
`Cache-Control: no-store` for queue/job responses; do not cache authenticated responses
in a shared proxy. Introduce cursors only if actual list sizes justify them.

## 6. Durable upload acceptance and bounded resources

Build a common staged-submission helper and keep framework uploads at the adapter edge.
The server does not process an entire recording in RAM or schedule inference as an HTTP
background task. Initial configurable limits: one file, one settings part at most 64 KiB,
file size at most 2 GiB, maximum two concurrent upload parsers/writers, and a server-wide
10 GiB budget covering incoming, parser-spooled, and retained queued uploads together.
Expose effective limits in docs/errors;
large installations can raise them explicitly.

Apply authentication and concurrency admission before multipart parsing. Enforce body
size while reading actual bytes, even with no/incorrect `Content-Length` or chunked
transfer encoding. Cap headers, field count, field sizes, and filename length. Configure
or wrap the installed multipart parser so its spool directory and limits are controlled;
checking `UploadFile.size` after parsing alone permits excessive disk use. Count parser
spooling and final copies against the disk budget, or consume into owned staging without
an extra full-size copy. Use the framework's streaming/parser facilities rather than
writing a multipart parser. Verify their actual version-specific limits in the first spike.
Use pre-parser ASGI admission/auth middleware or an equivalent verified gateway plus
application byte counter: an `UploadFile`/`Form` route dependency may run only after the
body has already been spooled. A dependency-level token check alone is insufficient.

Acceptance order:

1. Check caller, readiness, the header submission key, upload admission, and budget
   before parsing the body. Parse the bounded multipart body, then validate its settings
   and file metadata before enqueueing or moving input into its accepted location.
   Multipart parts can arrive in either order; validation of a form settings field
   cannot be promised before file bytes arrive. Permit bounded framework spooling
   rather than inventing a custom parser or trusting client part order.
2. Allocate a server-generated job ID and create only that request's directory beneath
   queue-owned uploads. Sanitize display filenames and store under a safe internal name;
   client filenames never select directories. Stream bounded chunks, counting bytes and
   computing a content digest when idempotency is requested. Offload blocking disk writes.
3. Close/flush the completed file and atomically mark/rename it out of its incomplete
   filename; preserve the review plan's durability guarantees before queue acceptance.
4. Recheck service readiness, then durably enqueue the immutable spec/settings. Commit
   idempotency metadata in the same queue save. Recheck the key/fingerprint and enqueue
   without an intervening await; wake the scheduler only after that save.
5. Set a committed flag owned by the submission operation, then return `202`/Location.
6. On failure before commit, delete only this operation's new uncommitted staging and
   release reservations. After commit, preserve the upload even if sending the response
   fails. Keep commit plus committed-flag update in a cancellation-safe no-await section,
   or shield and await the committing operation before deciding whether cleanup is safe.

Disconnect during upload cleans uncommitted staging. Disconnect after acceptance does
not cancel a job; cancellation requires the explicit endpoint. On restart under the
owner lock, remove orphan incomplete uploads only when no persisted job references
them. Never run an age-only cleanup against potentially accepted/running uploads.
Persisted jobs count against the upload budget across restart; release their accounted
bytes after actual owned-file cleanup, not merely after an HTTP request finishes.

Use best-effort cleanup with visible diagnostics on disk errors. A `507`/`503` response
must not hide a successfully committed job: reconciliation and idempotent replay cover
an indeterminate response rather than deleting a job whose acceptance may have succeeded.

## 7. Idempotency: cover a lost acceptance response without a second registry

Support an optional client-generated UUID `Idempotency-Key` for submissions. Remote CLI
generates one per requested job and retains it across transport retries. Persist two
optional fields with the accepted job: key and a fingerprint of uploaded bytes plus
canonical settings/display name. Compute SHA-256 while streaming; exclude temporary
paths/generated IDs. Do not deduplicate different keys by file contents.

- Same key and fingerprint returns the original job ID/snapshot (`200` on replay),
  without enqueueing again. Different content/settings for an existing key returns `409`.
- A second submission using a key still uploading returns `409 request_in_progress`
  with `Retry-After`; use a small in-memory key reservation, released in `finally`.
- Stream and fingerprint replay uploads under the same limits before accepting their
  equivalence; then delete only the replay's new staging. Do not silently return a prior
  job for arbitrary new content merely because the header matches.
- On restart, rebuild lookups from job records or scan the small store; no idempotency
  database, separate journal, or durable pending-upload registry is needed.
- Key uniqueness covers all retained statuses, including done, failed, and cancelled.
  Every concurrent attempt gets distinct request staging; a losing replay cleans only
  its own directory and never overwrites a source an accepted worker may be reading.
- The guarantee lasts while the job row exists. Removing/clearing that row deliberately
  ends key retention. Document that clients must not replay after deletion; long-lived
  deduplication tombstones are a later requirement, not an implied forever guarantee.
- Without a key, automatic retry after an uncertain `POST` may create a duplicate;
  clients must opt into the key mechanism for that recovery behavior.

Introduce schema 2 for the optional persisted fields and migrate schema 1 with absent-field
defaults under the lock; `JobSpec` rejects unknown fields. Test v1 import, new persistence,
restart replay, and unsupported newer schema preservation. Never reset old queue files.

## 8. Results, errors, and publication

Use the review plan's unchanged publication sequence: worker writes complete staging,
attempts optional export, writes one ready manifest including warnings; parent reaps,
validates, renames into the archive, saves `DONE`, then removes checkpoints/uploads.
The API reports a result only after that reconciliation/publication; `.pending` is never
listed or downloadable. Source disappearance does not invalidate already finished output.

`result_id` is the canonical archive identifier. `GET /results/...` resolves it against
validated completed archive resources, not through a queue lookup, so clear-finished
does not break downloads. Define a cautious compatibility path for legacy completed
archives without new manifests; require expected files/valid metadata, never classify
an arbitrary directory as completed. Reuse one core result reader in UI and HTTP.
The existing archive helper imports desktop `showinfm`/NiceGUI functionality; extract
plain filesystem/result logic into core rather than importing that helper in HTTP code.

Allow only known artifacts such as `transcription.json`, `transcription.txt`,
`transcription_timestamps.txt`, `transcription_nvivo.txt`, `transcription_maxqda.txt`,
and `transcription.srt`; expose safe metadata as JSON through the result endpoint.
Do not serve `log.txt`, raw queue files, readiness manifests, or arbitrary relative paths.
Reject separators, dot traversal, encoded traversal, symlink escapes, and unknown names;
resolve within the archive root and open a verified regular file. Keep ownership/access
checks in the shared result boundary. Stream downloads off the event loop, including
safe handling if the local archive UI deletes a result concurrently.

| Condition | HTTP response |
| --- | --- |
| Invalid JSON/multipart/settings or unsupported model-language combination | `422` with bounded field errors; no paths or reflected input blob. |
| Missing/invalid credential | `401`; no queue metadata; no redirect to a login HTML page for API requests. |
| Known caller lacks an operation capability | `403`; future private-resource lookups can use non-disclosing `404`. |
| Missing job/result/artifact | `404`. |
| Invalid transition, active-row delete, changed idempotency payload | `409` with stable machine code and current safe state where appropriate. |
| Too-large request / unsupported upload type | `413` / `415`. |
| Upload concurrency limit reached | `429` plus `Retry-After`, before consuming the upload. |
| Not ready, stopping, owner unavailable, persistence unavailable | `503` plus retry guidance; no accepted-work claim. |
| Insufficient owned staging budget/disk | `507`, with uncommitted staging cleanup. |
| Unexpected application error | `500` with opaque error ID; full traceback stays in server diagnostics. |

An accepted job later failing inference still returns `200` from its GET endpoint with
`status=failed`; it does not retroactively become an HTTP submission error. Map raw
worker exceptions into stable safe messages; path-bearing exception strings are not
automatically safe just because tracebacks were removed. Do not log bearer tokens,
upload bodies, or prompts in routine access/error logs.

## 9. Ownership, lifespan, and deployment modes

One coordinator constructs `QueueService` from core configuration, acquires the lock,
loads/reconciles, starts scheduling, and marks ready. Both a headless FastAPI app factory
and NiceGUI startup call that lifecycle, with exactly one service stored in application
state. Remove the current separate lazy startup in `queue_ui.py`; route registration
and imports must not acquire locks or start tasks. Do not attach a second independent
ASGI lifespan that accidentally bypasses NiceGUI's own startup/shutdown hooks.
NiceGUI's current `safe_invoke` schedules async startup handlers: registering one does
not itself await readiness. The headless lifespan explicitly awaits service startup;
co-hosted adapters share an initialization future/readiness gate checked by both UI and
API before access. An included router never starts its own owner, and mounting a child
FastAPI app is not proof that its lifespan will execute.

Headless startup failure exits nonzero without serving an apparently usable API. In a
desktop/co-hosted UI that keeps informational pages open, readiness remains false and
mutations return `503` with the real sanitized startup cause. Stop admission on shutdown,
resolve/cancel uncommitted uploads safely, stop/reap the active phase, save recoverable
state, and release ownership last. A kill/reap timeout keeps the failure visible; never
silently unlock while a child still owns the GPU.

Proposed commands, implemented with lazy command-specific imports:

```bash
aTrain start                         # existing desktop UI; API disabled
aTrain start --api --api-token-file /path/to/token
aTrain serve --host 127.0.0.1 --port 8081 --api-token-file /path/to/token
aTrain_core transcribe recording.mp3 # existing local semantics; shared run_one
aTrain_core transcribe recording.mp3 --server https://atrain.example
```

`serve` is headless and requires the new server extra; `start --api` requires GUI plus
server extras. Declare FastAPI, Uvicorn, and python-multipart as direct server dependencies,
and any directly imported validation library explicitly; choose versions compatible
with the locked NiceGUI stack. Remote CLI uses a declared client extra (for example,
httpx) with bounded streaming upload/download and timeout handling. No NiceGUI imports
are needed for headless API startup/help. Avoid relying on a transitive GUI dependency.

Use exactly one ASGI worker, disable production autoreload, and document local-disk
requirements for queue locking/atomic publication. Guard the application-level owner
against accidental multiple workers; the contender must fail clearly. A reverse proxy
can terminate TLS without becoming another scheduler. Do not run `uvicorn --workers 4`
and expect a file lock to route requests to the one service that acquired ownership.

## 10. Authentication and client boundaries

Require a configured high-entropy shared bearer token for API opt-in, read from a file
or environment variable rather than a command-line token value. Compare safely, keep
it out of response/log/URL data, and require it on every job, result, control, and schema
endpoint. Disable public interactive API docs or protect them with the same policy.
Token rotation initially requires restart; no account/token database is needed.

Bind to loopback by default. Remote headless exposure is explicit and requires TLS at
the server/proxy boundary. Disable CORS by default; if a separate browser client is
later enabled, configure exact allowed origins/hosts and bearer requests explicitly.
Loopback addresses do not make hostile web origins trusted; validate Host/Origin where
applicable and never put the shared token into a URL or public UI JavaScript.

The existing NiceGUI UI uses direct service calls and must have its own complete access
boundary when exposed remotely. Initial co-hosted remote deployment requires a trusted
authentication proxy covering the entire UI, upload/download paths, and WebSocket
handshake, with the application bound behind that proxy. Protect the UI and API together;
adding bearer checks only to `/api/v1` leaves UI actions as a bypass. Do not trust arbitrary
forwarded identity headers from direct clients. Verify that the backend is not directly
reachable and that authenticated context reaches UI service calls. If this deployment
cannot be verified, support headless remote API only and keep the UI local.

Cookie-authenticated UI actions require the same-origin/CSRF and WebSocket-origin policy
of the chosen gateway/session integration. API v1 accepts bearer headers, not ambient
UI cookies, keeping its mutation policy explicit. Test rejected cross-origin requests,
unauthenticated UI/socket/download access, and proxy bypass—not just an API 401 test.

## 11. Local and remote CLI behavior

Local transcription uses `QueueService.run_one` under the same lock and shared execution
path, without starting the normal scheduler or processing unrelated queued GUI jobs.
Preserve existing options, output formats, and success/error exit behavior. It does not
silently connect to a server when lock acquisition fails.

An explicit `--server` selects remote mode: upload the local file with a full settings
snapshot and one retained idempotency key, poll the returned job URL, and download the
selected completed artifacts to an explicit client-side output directory. A remote
client path is never sent as a server `source`/`export_dir`. Default to waiting like the
local command; an optional `--no-wait` returns the accepted job ID for automation.
Do not start a hidden local server or fall back to local inference after network failure.

Persist the request key before submission and print/persist the accepted ID when known.
After a lost response, query `GET /submissions/{request_key}` before retrying the upload
with the same key. A missing result does not prove that an earlier in-flight request
will never commit; honor `request_in_progress` and the documented key-retention scope.
Initial Ctrl-C in remote wait stops waiting without cancelling accepted work;
print the job ID and an explicit cancel command. Add a narrow remote cancel subcommand
using the endpoint rather than making disconnect equivalent to cancellation. Bound
retries to network/transient failures; never retry a changed upload under the same key.

## 12. Delivery sequence and validation

1. **Core prerequisites:** implement required review fixes and shared local CLI execution;
   retain one fixed runner. Verify existing queue/UI behavior before adding HTTP.
2. **Boundary/settings:** add immutable snapshots, shared submission/result helpers,
   context checks, per-client UI settings, and centralized lifecycle/root configuration.
3. **Thin read/control API:** add authenticated router/app factory, readiness, job/result
   queries, cancel/retry/pause/remove, and exact HTTP error mappings.
4. **Durable uploads:** implement pre-parser limits/admission, disconnect-safe acceptance,
   byte budgets, optional persisted idempotency metadata, and recovery/migration tests.
5. **Headless/co-host wiring:** add explicit commands/extras, attach the one lifecycle,
   validate auth across exposed surfaces, and document supported proxy deployment.
6. **Remote CLI:** stream uploads/downloads, preserve request keys, poll/cancel explicitly,
   and document local/remote differences without changing standalone defaults.
7. **Release:** remove duplicate adapters/startup paths, update installed/deployment docs,
   run the targeted and platform smoke suites, and record remaining unsupported modes.

Add `tests/api/test_jobs_api.py`, `test_uploads_api.py`, `test_results_api.py`,
`test_api_lifecycle.py`, and `tests/core/test_api_import_light.py`; use temporary roots
and injected fake models. Keep real process tests for ownership, cancellation, and
parent death. Use a real HTTP server for streaming/disconnect/backpressure tests;
in-process ASGI tests alone can hide body-buffering and lifespan differences.

Required scenarios: two clients' settings remain isolated; UI/API share the same service;
lost `202` retries return one job; duplicate active keys; conflicting retries; restart
replay; failed queue save; disconnect before/after commit; oversized/chunked/spooled
uploads; parser flood/concurrency cap; disk exhaustion; upload cancellation during
shutdown; auth failures before body parsing; path/symlink attacks; safe error redaction;
download after queue clear; archive deletion during download; every review recovery
boundary; startup lock contention; and shutdown with a live worker.

Suggested commands, after implementing the new files and installing test dependencies:

```bash
uv run --no-sync pytest tests/unit/test_jobs.py tests/unit/test_job_store.py tests/unit/test_queue_lock.py tests/core/test_queue_service.py tests/core/test_runner_process.py tests/core/test_output_steps.py -q
uv run --no-sync pytest tests/api tests/core/test_api_import_light.py -q
uv run --no-sync pytest tests/ui/test_transcribe_queue.py tests/ui/test_click_through.py tests/ui/test_settings_components.py tests/ui/test_advanced_settings.py tests/ui/test_boot_serve.py -q
uv run --no-sync ruff check aTrain aTrain_core tests/api
```

Add an installed-wheel server-extra CI job without NiceGUI/webview, using a non-repository
working directory. Smoke-test actual Linux service startup/restart and a tiny real-model
upload/download. Verify Windows/macOS desktop startup stays unchanged, API remains off
by default, and frozen/Flatpak builds opt in only when their server dependencies and
startup modes are packaged/tested. No subprocess CLI launch changes are required here.
Use the existing browser suite for settings isolation and authenticated co-host routing.

## 13. Definition of done and later expansion gates

- UI, local CLI, and HTTP share one command implementation and one execution owner.
- No API request starts inference in the HTTP process or loses a committed job on disconnect.
- Upload/parser memory, temporary disk, concurrency, and queued-upload budgets are enforced
  and tested; no arbitrary path/export or diagnostic-file endpoint is exposed.
- Queue rows and completed results have distinct tested lifetimes; clear-finished preserves
  retrievable results. Error DTOs contain no raw exceptions, tracebacks, or local paths.
- API-only installation starts without GUI dependencies; local defaults remain compatible.
- Direct UI callbacks and HTTP routes obey the declared shared-workspace access boundary.
- Schema upgrade, idempotent replay, crash recovery, clean shutdown, and lock contention
  tests pass, as do focused existing queue/UI/process regressions.
- Document one-worker deployment, limits, token/proxy setup, key retention, and unsupported
  private multi-user semantics. Record added/removed modules and execution paths rather
  than claiming API access necessarily reduces total line count.

Private multi-user deployment requires a separate ownership migration for jobs, archives,
settings, upload accounting, and every operation—including direct UI calls and legacy
results. Multiple web workers require a real shared coordinator interface; multiple
machines require shared durable storage and an explicit executor protocol. A database
or broker becomes justified by those measured requirements, not by HTTP itself.
