RESULT s-life-reset-runtime-route-reset-001 (call: owner-repair-runtime-route-2026-06-20)
direction: life-reset   play: repair   node/task: g-lr-weekly-operating-graph

outcome: |
  The life-reset route is reset so the next step is no longer a Weekly Contract.
  The architecture evidence from t-1/t-2 is preserved, but active work now starts
  with creating, selecting or minimally initializing the separate Life-reset
  Runtime v0 repository/workspace.

evidence: |
  Owner correction:
  - "я хочу ... чтобы я не потерял то, что мы говорили, нашу архитектуру условную, но чтобы ресетнулось вот эти T1, T2"
  - "где мой репозиторий создания?"
  - "Последняя попытка..."

  Independent read-only checks:
  - Architect subagent: t-2 proved only boundary decision, not runtime substrate;
    corrected route should make separate repo/workspace creation the next task.
  - Reviewer subagent: NOW.next, Sunday packet and boundary §7 still allowed a
    fresh chat to jump to Weekly Contract before runtime substrate existed.

  Preserved evidence:
  - live/life-reset/work/weekly-operating-graph-dry-run-v0.md
  - live/life-reset/work/sunday-planning-packet-v0.md
  - live/life-reset/work/life-reset-runtime-boundary-v0.md
  - live/life-reset/history/2026-06-20-s-life-reset-runtime-boundary-001.md

state_changes: |
  TREE.md:
  - Add owner_approved evidence for the 2026-06-20 repair.
  - Update g-lr-weekly-operating-graph appetite/kill_by so the bet is
    runtime-substrate-first and explicitly forbids compensating by running
    weekly/daily operation inside Direction OS.

  NOW.md:
  - Keep active_bet id/status on g-lr-weekly-operating-graph.
  - Replace active_bet goal/done_when/cuts/lenses/assumptions with the
    runtime-substrate-first route.
  - Preserve work/ and history evidence pointers.
  - Reset active tasks to:
      t-1 open: create/select/minimally initialize separate runtime
        repository/workspace; no Weekly Contract accepted.
      t-2 open: add minimal runtime/provider instructions.
      t-3 open: create first Weekly Contract inside the initialized runtime
        substrate.
  - Replace open_calls c-life-reset-weekly-contract-runtime-001 with
    c-life-reset-runtime-substrate-001.
  - Replace NOW.next with CALL c-life-reset-runtime-substrate-001.

  work/:
  - Mark live/life-reset/work/life-reset-runtime-boundary-v0.md §7 as
    superseded: setup first, contract later.
  - Mark live/life-reset/work/sunday-planning-packet-v0.md as template/input
    only; contract output belongs in the separate runtime workspace, not
    live/life-reset/work/.

  LOG.md:
  - Append the 2026-06-20 repair line for this route reset.

  history/:
  - Add this file:
    live/life-reset/history/2026-06-20-s-life-reset-runtime-route-reset-001.md.

captures:
  - Possible OS maintenance: a shape/work result that selects an external runtime/product substrate should not set next to domain operation until the substrate exists or has its own setup CALL.

decisions_needed: []

play_check:
  - "1 Name the contradiction: done — current NOW.next asked for a Weekly Contract even though the owner-approved separate runtime repository/workspace did not exist yet."
  - "2 Reconstruct: done — t-1/t-2 artifacts exist and are useful evidence, but t-2 proved only a boundary decision; it did not create the substrate."
  - "3 Propose corrected state: done — reset active tasks so t-1 is runtime repository/workspace creation/init, t-2 is minimal runtime instructions, t-3 is the first contract inside that substrate."
  - "4 Confirm: done — owner explicitly ordered repair/reset: \"ресетнулось вот эти T1, T2\" and \"где мой репозиторий создания?\"."
  - "5 Friction: skipped — captured maintenance candidate; this repair fixes direction state without editing os/**."

log: "repair: reset g-lr-weekly-operating-graph route after t-2 wrongly jumped to Weekly Contract before a separate runtime repository/workspace existed; architecture artifacts preserved as evidence, tasks reset to runtime substrate first; next c-life-reset-runtime-substrate-001."

next: |
  CALL c-life-reset-runtime-substrate-001
  to: session
  direction: life-reset
  play: work
  node: g-lr-weekly-operating-graph
  task: t-1
  goal: |
    The separate Life-reset Runtime v0 repository/workspace exists or is
    selected, is minimally initialized, and is ready to host the first Weekly
    Contract.
  context: |
    Read live/life-reset/NOW.md and the files referenced by its next CALL.
  boundaries: |
    Do not create or accept the first Weekly Contract in this CALL.
    Do not run daily operation.
    Do not store runtime contracts, daily logs, cards or checkpoints in
    Direction OS.
  done_when: |
    A concrete runtime repository/workspace path or URL is recorded; the
    substrate exists or has an exact setup blocker; it states the
    control-plane/runtime split and has minimal Markdown locations for Weekly
    Contracts, runtime evidence/checkpoints and provider-facing instructions.
  return: |
    RESULT with runtime substrate pointer, initialized artifact list or exact
    blocker, state_changes and next CALL.
  budget: one focused setup session

END_OF_FILE: live/life-reset/history/2026-06-20-s-life-reset-runtime-route-reset-001.md
