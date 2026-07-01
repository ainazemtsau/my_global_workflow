# Adapter: runtime control-plane

Purpose: define the optional automation layer that can run Direction OS jobs
through Codex, Claude Code, GitHub Actions, n8n, Activepieces, or a small local
service without moving authority out of Markdown/Git.

The runtime changes the relay, not the OS. Packets, plays, gates, and `live/**`
remain authoritative.

## Authority

1. `live/**`, `os/**`, product repos, and committed artifacts are the source of
   truth. A runtime database is a cache, queue, or UI state only.
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

Runtime jobs are derived from CALLs, RESULTs, product-repo evidence, and owner
actions. A job may store logs outside `live/**`, but the closing fact returns
through RESULT/history.

Statuses:

`queued` -> `running` -> `returned` -> `reviewing` -> `approved` -> `applying`
-> `next_ready`

Side exits:

- `rework`: review found a bounded fix; route back to the executor.
- `blocked`: cannot proceed within budget or lacks required owner input.
- `failed`: runtime/tool failure; no state claim.
- `cancelled`: superseded by an explicit owner or repair decision.

The first high-value loop is:

1. executor CALL runs in a product repo;
2. executor returns RESULT plus commit/PR/check evidence;
3. a fresh review session tries to refute the proof against the CALL;
4. PASS routes to writer apply; FAIL routes to rework or blocked;
5. writer serially applies state and emits the next CALL.

## Locks

- One writer apply per direction at a time.
- Product executor jobs use separate branches/worktrees or an explicit
  owner-approved shared worktree.
- Runtime must not start two agents that can edit overlapping files
  concurrently.
- A stuck lock is resolved by repair or owner decision, not by force.

## Core command surface

A future `osctl` or equivalent wrapper should expose small JSON-friendly
commands:

- `status`: derive directions, active bets, open calls, decisions, and next.
- `collect`: render a paste-ready CALL/context packet.
- `run`: start an allowlisted session/executor/research command.
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
5. only then consider auto-running the next CALL.

Go/no-go: keep the slice only if it reduces owner relay work, preserves
reproducible Git evidence, and produces no new protocol violations.

END_OF_FILE: os/adapters/runtime.md
