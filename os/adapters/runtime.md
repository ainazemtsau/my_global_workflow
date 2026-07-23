# Adapter: runtime control-plane

Purpose: define the optional automation layer that can run Direction OS jobs
through Codex, Claude Code, GitHub Actions, n8n, Activepieces, or a small local
service without moving authority out of Markdown/Git.

The runtime changes the relay, not the OS. Packets, plays, gates, and `live/**`
remain authoritative.

## Authority

1. `live/**`, `os/**`, product repos, and committed artifacts are the source of
   truth. A runtime database is a cache, queue, or UI state only; a Direction
   CALL's durable launch claim is its `open_calls.status: running` receipt.
2. Durable changes enter Direction OS only as RESULTs applied by the writer.
   No runtime step edits `live/**` directly.
3. No-code tools are clients. They may display status, trigger allowlisted
   commands, collect owner decisions, and notify; they do not interpret plays,
   decide strategy, or rewrite packets.
4. Shell access is wrapped by named commands (`osctl ...` or equivalent), never
   arbitrary command text stored in a visual node.
5. Owner gates remain gates: CHARTER/TREE approval, external/irreversible
   effects, merge/push gates, and any play `(owner)` step require the owner's
   explicit words or an owner-ack token.

## Job lifecycle

Runtime jobs are derived from tracked open calls, RESULTs, product-repo evidence,
and owner actions. Queue identity is `(direction, track, call)`; for a v30/v31
engineering root this identity survives every product stage. A job may store
logs outside `live/**`, but the closing fact returns through RESULT/history.

Statuses:

`queued` -> `running` -> `returned` -> `reviewing` -> `approved` -> `applying`
-> `next_ready`

Side exits:

- `rework`: review found a bounded fix; route back to the executor.
- `blocked`: cannot proceed within budget or lacks required owner input.
- `failed`: runtime/tool failure; no state claim.
- `cancelled`: superseded by an explicit owner or repair decision.

The v29/legacy stage loop is:

1. executor CALL runs in a product repo;
2. executor returns RESULT plus commit/PR/check evidence;
3. a fresh review session tries to refute the proof against the CALL;
4. PASS routes to writer apply; FAIL routes to rework or blocked;
5. writer serially applies state and emits the local continuation or fresh frontier.

The v30/v31 root loop removes those intermediate Direction applies:

1. claim one integer-pinned root and keep its `open_calls` row open;
2. launch PLAN, PAIR-CANDIDATE, binding PAIR-FREEZE, BUILD and validation as
   separate fresh API/CLI sessions, never in-session substitutes;
3. after each stage, verify its compact committed receipt against the pinned
   repo route and launch only the declared eligible stage;
4. bounded in-scope rework stays inside that root; REPORT or ESCALATE returns
   one HOME to the Direction writer.

Internal identity `(root, stage, attempt)` is runtime cache only. The durable
receipt lives in product progress/evidence; no internal transition edits
`live/**` or creates a Direction CALL.

### V31 root control

Every durable receipt names one shared lifecycle:

- `ACTIVE`: the named stage may run when its eligibility is green;
- `PRESERVED-PAUSED`: retained history/custody only; it cannot drive discovery,
  apply, mutation or Deliver until a new committed ACTIVE admission;
- `RELEASED`: publication/readback completed; the root is terminal and immutable.

Receipts record stage, exact product/process input manifests, outputs, verdict,
evidence, retry class/count, eligibility and closing lease. Product inputs and
process inputs are separate: a process-only change reruns the process proof it
governs, never an unchanged product review. A `fixed <sha>` is eligible only when
Git resolves it as a commit and it accounts for the changed product input.
Boolean receipt/config fields require JSON booleans; truthy strings fail.

Before retry, classify what invalidated the receipt and return only to the
earliest affected stage:

- owner-locked plan/spec/scope or out-of-plan behavior -> ESCALATE;
- frozen carrier/RED -> PAIR-CANDIDATE then binding PAIR-FREEZE;
- implementation -> BUILD then affected validation;
- process/tool/config -> its process proof and dependent evidence;
- closing evidence/register/citation -> closing checks only.

Closing has one control lease for the root. Its checkout must be clean and
committed before acquisition; drafts never transfer between sessions. The owner
of that lease performs one recoverable order: evidence commits (including an
atomic finding + REFUTED row + citation) -> RESULT/mirrors -> gates -> RELEASED
commit -> publish/readback. Failure leaves the root ACTIVE at the last verified
receipt; an un-read-back RELEASED commit is ineffective. Only read-back RELEASED
yields REPORT HOME; a genuine decision/blocker yields ESCALATE HOME.

## Locks

- One writer apply per direction at a time.
- One runtime claim per `(direction, track, call)`; retry resumes that identity instead of launching a duplicate.
- A claim passes through the writer as `ready -> running` with its receipt before dispatch. The runtime refuses an already-`running` call; only an explicit cancel/lost receipt may reset it to `ready`.
- One v31 closing-control lease per root; only its clean committed checkout may stage closing files.
- Product executor jobs use separate branches/worktrees or an explicit
  owner-approved shared worktree.
- Runtime must not start two agents that can edit overlapping files
  concurrently.
- A stuck lock is resolved by repair or owner decision, not by force.

## Core command surface

A future `osctl` or equivalent wrapper should expose small JSON-friendly
commands:

- `status`: derive directions, active bets, track WIP limit/occupancy, calls grouped by track/status including `running`, and decisions.
- `collect`: render a paste-ready packet for one explicit/sole actionable call; several return choices.
- `run`: claim one ready call through the writer, then start it; a v30/v31 engineering root also drives its declared fresh product stages.
- `review`: run a fresh refutation pass over an executor RESULT.
- `apply`: invoke the writer on one RESULT with direction lock.
- `notify`: send owner batches without changing state.

n8n, Activepieces, GitHub Actions, or Codex Automations call these commands.
They are replaceable UI/scheduling shells around the same contract.

## Boundaries

The runtime must not:

- store canonical direction state in its own database;
- choose the next strategic bet;
- auto-approve owner decisions;
- merge or push when the active CALL says owner-gated;
- continue after a failed writer validation;
- hide tool failures behind a green dashboard status.

## Adoption

Adopt by vertical slices, not migration:

1. read-only status dashboard;
2. executor-return -> fresh Codex/Claude review;
3. one-direction writer apply with lock;
4. rework routing on review failure;
5. only then auto-run the next Direction CALL or a v30/v31 root's repo-local stages.

Go/no-go: keep the slice only if it reduces owner relay work, preserves
reproducible Git evidence, and produces no new protocol violations.

END_OF_FILE: os/adapters/runtime.md
