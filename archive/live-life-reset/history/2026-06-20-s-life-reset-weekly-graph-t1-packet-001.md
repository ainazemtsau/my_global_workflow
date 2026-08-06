RESULT s-life-reset-weekly-graph-t1-packet-001 (call: c-life-reset-weekly-graph-t1-packet-001)
direction: life-reset   play: work   node/task: g-lr-weekly-operating-graph/t-1

outcome: |
  The small Sunday planning packet v0 exists and is ready for owner use at
  live/life-reset/work/sunday-planning-packet-v0.md. It condenses the larger
  dry-run into the fields needed to accept the first real Weekly Contract for
  2026-06-22..2026-06-28 without selecting permanent tooling, building daily
  runtime/modules, resuming Solmax/W0, prescribing health care, or taking
  ownership of source-direction tasks.

evidence: |
  - live/life-reset/work/sunday-planning-packet-v0.md exists.
  - The packet contains Sunday inputs, source refresh fields, candidate/card
    fields, the contract skeleton, explicit cuts, change rule, session/writer
    rule and owner acceptance checklist.
  - It references live/life-reset/work/weekly-operating-graph-dry-run-v0.md as
    dry-run evidence instead of copying the full dry-run.
  - Self-check matched the task done_when by searching the packet for: Sunday
    inputs, source refresh, card fields, explicit cuts, change rule,
    session/writer flow, dry-run reference, Solmax/W0, permanent tooling,
    daily method/runtime, modules, full backlog and source-direction ownership
    boundaries.

state_changes: |
  work/:
  - Add live/life-reset/work/sunday-planning-packet-v0.md.

  NOW.md:
  - Set task t-1 status from open to done.
  - Replace open_calls entry c-life-reset-weekly-graph-t1-packet-001 with:
      id: c-life-reset-weekly-graph-t2-contract-001
      to: session
      for: t-2
      issued: 2026-06-20
      note: >
        Accept the first real Weekly Contract for 2026-06-22..2026-06-28 from
        the Sunday planning packet and refreshed owner/source inputs.
  - Set next to CALL c-life-reset-weekly-graph-t2-contract-001.

  LOG.md:
  - Append:
    - 2026-06-20 - work t-1: Sunday planning packet v0 prepared for the first real
      Weekly Contract; next c-life-reset-weekly-graph-t2-contract-001.

  history/:
  - Add this file:
    live/life-reset/history/2026-06-20-s-life-reset-weekly-graph-t1-packet-001.md.

captures: []

decisions_needed: []

play_check:
  - "1 Recite: done — active bet g-lr-weekly-operating-graph serves the first real Weekly Contract; t-1 done_when is the portable Sunday planning packet."
  - "2 Owner inputs (owner): done — owner CALL asks for \"A small Sunday planning packet v0 for the first real Weekly Contract\" and bounds \"Do not continue Solmax/W0\" / \"Do not prescribe nutrition/training/medical care\" / \"Do not choose permanent tooling\"; no new calendar, capacity or priority answers were guessed, they remain explicit Sunday inputs in the packet."
  - "3 Do the work: done — created live/life-reset/work/sunday-planning-packet-v0.md from NOW, CHARTER, TREE, the dry-run and the adapters."
  - "4 Self-check: done — packet satisfies each done_when line and stays within cuts; evidence is the artifact plus key-field search."
  - "5 Close: done — RESULT marks t-1 done, adds the artifact, appends LOG/history, and sets next to the t-2 Sunday contract CALL."

log: "work t-1: Sunday planning packet v0 prepared for the first real Weekly Contract; next c-life-reset-weekly-graph-t2-contract-001."

next: |
  CALL c-life-reset-weekly-graph-t2-contract-001
  to: session
  direction: life-reset
  play: work
  node: g-lr-weekly-operating-graph
  task: t-2
  goal: |
    The first real Weekly Contract for 2026-06-22..2026-06-28 is accepted by
    the owner.
  context: |
    Read:
    - live/life-reset/CHARTER.md
    - live/life-reset/TREE.md
    - live/life-reset/NOW.md
    - live/life-reset/work/sunday-planning-packet-v0.md
    - live/life-reset/work/weekly-operating-graph-dry-run-v0.md
    - os/adapters/SESSION_PAYLOAD.md
    - os/adapters/chatgpt-project.md
    - os/adapters/claude-project.md
    - os/adapters/coding-agent.md
    - os/KERNEL.md
    - os/plays/work.md

    Use the packet as the small Sunday form. Use the dry-run only as evidence
    and background. The real contract must use refreshed source snapshots and
    the owner's real Sunday inputs.
  boundaries: |
    Do not continue Solmax/W0.
    Do not prescribe nutrition, training, medical or psychiatric treatment.
    Do not select a permanent provider, chat, repo, board or external-tool
    architecture.
    Do not build daily runtime, process/activity modules, automation or a full
    backlog.
    Do not turn life-reset into the source of truth for health, game, Solmax or
    raw source-direction data.
  done_when: |
    - live/life-reset/work/week-2026-06-22-contract-v0.md exists.
    - It contains refreshed source snapshots, capacity assumptions, selected
      slices, explicit cuts, backlog/candidate handling and the change rule.
    - It records owner acceptance.
    - It does not choose permanent tooling or prescribe health/game/Solmax work
      outside their source directions.
  return: |
    RESULT with the contract path, evidence, state_changes and next CALL.
  budget: one focused Sunday planning session
  surface: any session surface; Codex/Claude Code may write only after RESULT

END_OF_FILE: live/life-reset/history/2026-06-20-s-life-reset-weekly-graph-t1-packet-001.md
