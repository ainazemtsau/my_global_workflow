# Life-reset Runtime Boundary v0

Date: 2026-06-20
Status: approved boundary/substrate decision for the first runtime v0

Owner decision:

> "отдельный репозиторий мы уже обсуждали с прошлым этим. В общем, отдельный репозиторий."

Decision: Life-reset Runtime v0 lives in a separate repository/workspace. The
exact repository/path is created or selected by the next CALL before the first
real Weekly Contract is accepted.

## 1. Boundary

Direction OS is the control plane. It owns:

- shaping the direction, active bets, tasks, CALLs and RESULTs;
- repairs, reviews, pulse, history and governance;
- state transitions in `live/life-reset/NOW.md`, `TREE.md`, `LOG.md`,
  `history/` and `knowledge/`;
- acceptance gates: evidence, owner decisions, cuts, source-direction
  boundaries and review outcomes;
- summary pointers imported from the runtime after a session closes.

Direction OS does not own:

- the running Weekly Contract as the surface the owner operates day by day;
- raw daily operation logs, check-ins, scratch notes or lightweight checkpoints;
- raw health/game/Solmax task data;
- process/activity modules or daily protocols before those nodes are shaped.

The Life-reset Runtime owns:

- Weekly Contracts after they are accepted;
- daily operation artifacts that serve the current Weekly Contract;
- lightweight logs/checkpoints needed for weekly review;
- runtime-local cards, backlog/candidate lists and process/technique registry
  candidates;
- provider-facing instructions for operating the runtime in ChatGPT Project,
  Claude Web, Codex, Claude Code or another chosen surface.

The runtime reports back to Direction OS through summaries, evidence pointers,
RESULTs or write requests. It does not directly mutate `live/**` state unless a
writer surface applies a valid RESULT through the normal Direction OS writer
rules.

## 2. Substrate comparison

### Temporary separated work substrate inside this repo

Example: `live/life-reset/work/runtime-v0/`.

Strengths:

- fastest to create;
- no new repository setup before the first week;
- easy to link from existing state and commit with the same writer flow;
- reversible by moving the folder later.

Risks:

- the physical proximity to Direction OS can blur the control-plane/runtime
  boundary;
- daily artifacts may start to look like Direction OS state;
- easy to accidentally grow daily operation inside `live/life-reset/`.

Best use:

- acceptable as an emergency fallback if the separate workspace blocks the
  first week.

### Separate repository/workspace

Example working name: `life-reset-runtime`, with the final name/path chosen in
the next CALL.

Strengths:

- strongest separation between governance state and operating artifacts;
- protects Direction OS from becoming a daily runtime surface;
- makes runtime provider instructions, Weekly Contracts and daily artifacts
  portable as their own workspace;
- makes it clearer that health, game and Solmax raw data remain outside
  life-reset.

Risks:

- setup overhead before the first Weekly Contract;
- could turn into a premature tooling architecture discussion;
- requires a pointer/summary discipline so Direction OS still knows enough to
  govern without copying runtime contents.

Why it is reversible enough for v0:

- the first runtime repository/workspace can be plain Markdown with no
  automation or permanent provider choice;
- if it proves too heavy, the runtime can be archived or folded into a smaller
  substrate after weekly review;
- Direction OS stores only the decision, summary and evidence pointers, so a
  later migration does not rewrite strategic state.

## 3. Recommendation and decision

Session recommendation before owner decision:

- temporary separated work substrate inside this repo is the lowest-friction
  v0 if no prior substrate decision exists;
- however, if the owner has already considered the split and wants a clean
  boundary, a separate repository/workspace better protects the control-plane
  distinction.

Owner decision:

- use a separate repository/workspace for Life-reset Runtime v0.

Interpretation:

- this is a v0 runtime substrate decision, not a permanent tooling, provider,
  automation or product architecture decision;
- the next session creates or selects the separate runtime workspace only as far
  as needed to accept the first real Weekly Contract;
- Sunday planning remains blocked until that substrate exists or is explicitly
  named.

## 4. Provider and writer surfaces

ChatGPT Project and Claude Web:

- can operate as session surfaces for planning, daily runtime conversation or
  review;
- do not write Direction OS state directly;
- emit RESULTs or write requests for a writer surface.

Codex and Claude Code:

- can operate as session surfaces when they read the Direction OS repo;
- can apply valid RESULT state_changes as writer surfaces under
  `os/adapters/coding-agent.md`;
- may also edit the separate runtime repository/workspace if the CALL for that
  repo explicitly asks them to do so.

All surfaces:

- treat chat history as interface context, not durable state;
- keep source directions as sources of truth;
- report only weekly-level summaries and evidence pointers back to Direction
  OS unless a later approved node changes that rule.

## 5. Imports and source boundaries

Life-reset imports summaries only:

- health may provide floors, constraints or review verdict summaries, but
  health remains source of truth for nutrition, training, body data, health
  metrics, protocols and medical questions;
- game development may provide current focus, blockers and accepted CALL/RESULT
  summaries, but game remains source of truth for game production and tasks;
- Solmax remains cut unless resumed through a valid Solmax route;
- raw data, detailed task lists and source-direction decisions do not move into
  the life-reset runtime.

## 6. What v0 explicitly does not build

This decision does not build or approve:

- daily runtime protocol;
- process/activity modules;
- full backlog system;
- automation;
- permanent provider/chat/repo/tool architecture beyond the separate v0
  substrate;
- nutrition, training, medical or psychiatric treatment;
- Solmax/W0 continuation;
- game production tasks authored by life-reset.

## 7. Superseded next wording

The original next wording combined runtime substrate setup with accepting the
first real Weekly Contract. That was repaired on 2026-06-20.

Current route:

1. Create, select or minimally initialize the separate Life-reset Runtime v0
   repository/workspace.
2. Only after that, create the first real Weekly Contract inside that runtime
   substrate.
3. Direction OS records only pointers, summaries, RESULTs and governance state.

Use `live/life-reset/NOW.md -> next` as the current authority.

END_OF_FILE: live/life-reset/work/life-reset-runtime-boundary-v0.md
