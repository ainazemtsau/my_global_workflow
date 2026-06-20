RESULT s-life-reset-runtime-boundary-repair-001 (call: owner-repair-runtime-boundary-2026-06-20)
direction: life-reset   play: repair   node/task: g-lr-weekly-operating-graph

outcome: |
  NOW.md no longer routes directly from the Sunday planning packet into accepting
  the real Weekly Contract. The next CALL now repairs the architectural boundary:
  Direction OS is the control plane that creates, governs and evolves the
  life-reset runtime; it is not itself the ongoing weekly/daily runtime.

evidence: |
  Owner correction:
  - "я сейчас хочу уточнить ... архитектура процесса, именно она не должна быть в нашем workflow"
  - "Наш workflow вот создает такие процессы"
  - "Почини. Почини и потом дай мне next call правильный."

  Reconstructed state:
  - t-1 was genuinely completed by 2026-06-20-s-life-reset-weekly-graph-t1-packet-001.
  - live/life-reset/work/sunday-planning-packet-v0.md exists and is useful input.
  - The old NOW.next routed straight to c-life-reset-weekly-graph-t2-contract-001,
    accepting the first real Weekly Contract before the runtime substrate was
    defined.

state_changes: |
  NOW.md:
  - Keep active_bet id/status on g-lr-weekly-operating-graph.
  - Repair active_bet goal/done_when/cuts/lenses/assumptions so the bet first
    separates Direction OS control-plane ownership from the external/runtime
    weekly-daily process.
  - Keep t-1 status done, but clarify it is input evidence, not current route.
  - Replace t-2 with:
      Life-reset Runtime v0 has an approved boundary/substrate decision that
      separates Direction OS control-plane work from the actual weekly/daily
      operating process.
  - Replace t-3 with:
      The first real Weekly Contract is created in the approved runtime
      substrate, with Direction OS recording only summary/evidence and the next
      governing CALL.
  - Replace open_calls c-life-reset-weekly-graph-t2-contract-001 with
    c-life-reset-runtime-boundary-001.
  - Replace NOW.next with CALL c-life-reset-runtime-boundary-001.

  work/:
  - Add a repair note to live/life-reset/work/sunday-planning-packet-v0.md:
    it is input evidence only, and current authority is NOW.md.
  - Mark the packet's old Sunday-contract CALL section as superseded, so the
    artifact cannot be copied as the current route.

  LOG.md:
  - Append the repair line naming the divergence.

  history/:
  - Add this file:
    live/life-reset/history/2026-06-20-s-life-reset-runtime-boundary-repair-001.md.

captures:
  - Possible later maintenance: shape/work prompts for process-creating directions may need a stronger "control plane vs runtime/product" boundary check if this repeats.

decisions_needed: []

play_check:
  - "1 Name the contradiction: done — NOW.next said to accept the first real Weekly Contract, while the owner clarified that the runtime architecture should not live as ongoing weekly/daily operation inside Direction OS."
  - "2 Reconstruct: done — t-1 packet exists and is valid input evidence; the wrong part was routing directly to Sunday planning before defining runtime substrate."
  - "3 Propose corrected state: done — keep t-1 done, replace t-2 with runtime-boundary/substrate decision, move first contract creation to t-3 after the boundary."
  - "4 Confirm: done — owner explicitly requested repair: \"Почини. Почини и потом дай мне next call правильный.\""
  - "5 Friction: skipped — treated as direction-state repair, not yet a repeated OS rule defect; captured possible maintenance follow-up."

log: "repair: corrected g-lr-weekly-operating-graph next after owner clarified that Direction OS must govern/create a separate life-reset runtime, not become the weekly/daily runtime; t-1 packet remains input evidence, next is c-life-reset-runtime-boundary-001."

next: |
  CALL c-life-reset-runtime-boundary-001
  to: session
  direction: life-reset
  play: work
  node: g-lr-weekly-operating-graph
  task: t-2
  goal: |
    Life-reset Runtime v0 has an approved boundary/substrate decision that
    separates Direction OS control-plane work from the actual weekly/daily
    operating process.
  context: |
    Read live/life-reset/NOW.md and the files referenced by its next CALL.
  boundaries: |
    Do not run Sunday planning or accept the real Weekly Contract in this CALL.
    Do not continue Solmax/W0. Do not prescribe nutrition/training/medical care.
    Do not shape other life-reset nodes or build daily runtime/modules/backlog.
  done_when: |
    live/life-reset/work/life-reset-runtime-boundary-v0.md exists, records the
    runtime/control-plane split, compares v0 substrate options, records owner
    decision, and issues the next CALL.
  return: |
    RESULT with the boundary document path, owner decision, state_changes and
    next CALL.
  budget: one focused repair/work session

END_OF_FILE: live/life-reset/history/2026-06-20-s-life-reset-runtime-boundary-repair-001.md
