RESULT s-life-reset-runtime-boundary-001 (call: c-life-reset-runtime-boundary-001)
direction: life-reset   play: work   node/task: g-lr-weekly-operating-graph/t-2
outcome: |
  Life-reset Runtime v0 boundary/substrate decision is approved. Direction OS
  remains the control plane, while the runtime owns Weekly Contracts, daily
  operation artifacts, lightweight checkpoints, process/technique candidates and
  provider-facing runtime instructions. Owner decision: use a separate
  repository/workspace for the runtime v0 substrate.
evidence: |
  Boundary document:
  live/life-reset/work/life-reset-runtime-boundary-v0.md

  Owner decision recorded from this session:
  "отдельный репозиторий мы уже обсуждали с прошлым этим. В общем, отдельный репозиторий."

  Self-check:
  - Document states Direction OS ownership.
  - Document states runtime ownership.
  - Document compares temporary separated work substrate inside this repo with a
    separate repository/workspace.
  - Document records recommendation, owner decision, tradeoffs and reversibility.
  - Document states ChatGPT Project/Claude Web as session surfaces and
    Codex/Claude Code as writer-capable surfaces.
  - Document produces a next CALL for the first real Weekly Contract in the
    approved separate runtime substrate.
state_changes: |
  Add file:
  - live/life-reset/work/life-reset-runtime-boundary-v0.md

  NOW.md:
  - t-2 status: open -> done.
  - Add t-2 result_note pointing to the boundary document and recording the
    separate repository/workspace substrate decision.
  - Remove open call c-life-reset-runtime-boundary-001.
  - Add open call c-life-reset-weekly-contract-runtime-001 for t-3.
  - Replace NOW.next with CALL c-life-reset-weekly-contract-runtime-001.

  LOG.md:
  - Append:
    2026-06-20 - work t-2: Life-reset Runtime v0 boundary approved with
    separate repository/workspace as substrate; next
    c-life-reset-weekly-contract-runtime-001.

  history/:
  - Save this RESULT as
    live/life-reset/history/2026-06-20-s-life-reset-runtime-boundary-001.md.
captures: []
decisions_needed: []
play_check:
  - 1 Recite: done; task t-2 serves active bet g-lr-weekly-operating-graph and its done_when requires an approved boundary/substrate document plus next CALL.
  - 2 Owner inputs (owner): done; owner decision quoted: "отдельный репозиторий мы уже обсуждали с прошлым этим. В общем, отдельный репозиторий."
  - 3 Do the work: done; produced the boundary document without running Sunday planning, building daily runtime, continuing Solmax/W0 or prescribing health/game work.
  - 4 Self-check: done; evidence document matches every t-2 done_when bullet.
  - 5 Close: done; t-2 marked done, next CALL routes to t-3, and because t-3 remains open this is not yet a review CALL.
log: work t-2: Life-reset Runtime v0 boundary approved with separate repository/workspace as substrate; next c-life-reset-weekly-contract-runtime-001.
next: |
  CALL c-life-reset-weekly-contract-runtime-001
  to: session
  direction: life-reset
  play: work
  node: g-lr-weekly-operating-graph
  task: t-3
  goal: |
    The first real Weekly Contract exists in the approved separate runtime
    substrate, with Direction OS holding only the governance summary and
    evidence pointer.
  context: |
    Read:
    - live/life-reset/NOW.md
    - live/life-reset/CHARTER.md
    - live/life-reset/TREE.md
    - live/life-reset/work/life-reset-runtime-boundary-v0.md
    - live/life-reset/work/sunday-planning-packet-v0.md
    - live/life-reset/work/weekly-operating-graph-dry-run-v0.md
    - os/adapters/SESSION_PAYLOAD.md
    - os/adapters/chatgpt-project.md
    - os/adapters/claude-project.md
    - os/adapters/coding-agent.md
    - os/KERNEL.md
    - os/plays/work.md

    Owner decision in t-2: Life-reset Runtime v0 uses a separate
    repository/workspace. Direction OS remains the control plane and should not
    host weekly/daily runtime operation. The Sunday planning packet remains
    useful input evidence for the first Weekly Contract, not permanent runtime
    architecture.
  boundaries: |
    Do not run daily operation.
    If the separate runtime repository/workspace cannot be created or selected
    inside budget, close blocked with the exact missing substrate decision or
    setup blocker.
    Do not continue Solmax/W0.
    Do not prescribe nutrition, training, medical or psychiatric treatment.
    Do not shape other life-reset nodes.
    Do not build daily runtime, process/activity modules, automation or a full
    backlog.
    Do not turn life-reset into the source of truth for health, game, Solmax or
    raw source-direction data.
  done_when: |
    - The first Weekly Contract exists in the approved separate runtime
      repository/workspace.
    - It contains refreshed source snapshots, capacity assumptions, selected
      slices, explicit cuts, backlog/candidate handling and the change rule.
    - It records owner acceptance.
    - Direction OS stores only a summary/pointer/RESULT, not raw daily runtime
      logs.
    - It does not choose permanent tooling or prescribe health/game/Solmax work
      outside their source directions.
  return: |
    RESULT with runtime substrate pointer, Weekly Contract pointer/summary,
    owner acceptance, state_changes and next CALL.
  budget: one focused planning session
  surface: Codex or Claude Code preferred if runtime repo/workspace setup is
    needed; ChatGPT/Claude Web may run as session-only and emit RESULT/write
    request.

END_OF_FILE: live/life-reset/history/2026-06-20-s-life-reset-runtime-boundary-001.md
