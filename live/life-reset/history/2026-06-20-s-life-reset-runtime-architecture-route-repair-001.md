RESULT s-life-reset-runtime-architecture-route-repair-001 (call: owner-repair-runtime-architecture-route-2026-06-20)
direction: life-reset   play: repair   node/task: g-lr-weekly-operating-graph

outcome: |
  The active life-reset route no longer asks for a provider-instruction task or
  a concrete Weekly Contract as near-term work. The next CALL now asks for a
  separate runtime repository/workspace containing the actual runtime
  architecture skeleton. Weekly Contract is explicitly defined as a later
  concrete accepted plan for a real week, not the architecture itself.

evidence: |
  Owner correction:
  - "Что за минимал provide instruction?"
  - "Что за виклик контракт?"
  - "У нас есть комплексная архитектура"
  - "сначала делать, потом все виклик контракты"

  Current files updated:
  - live/life-reset/NOW.md next -> c-life-reset-runtime-architecture-001.
  - live/life-reset/TREE.md appetite/kill_by now say runtime architecture
    skeleton before concrete Weekly Contracts.
  - live/life-reset/work/life-reset-runtime-boundary-v0.md route now says
    architecture skeleton, then audit, then concrete Weekly Contract later.
  - live/life-reset/work/sunday-planning-packet-v0.md marked as not runtime
    architecture and not current route.

state_changes: |
  TREE.md:
  - Add owner_approved evidence for the correction.
  - Update g-lr-weekly-operating-graph appetite/kill_by to runtime-architecture
    skeleton first; concrete Weekly Contracts later.

  NOW.md:
  - Replace active_bet wording with runtime-architecture-first route.
  - Replace active tasks with:
      t-1 open: separate runtime repository/workspace exists or is selected and
        contains the runtime architecture skeleton.
      t-2 open: runtime architecture skeleton is audited against owner-discussed
        cases without running a real week.
      t-3 open: first pilot-planning CALL is ready only after architecture is
        accepted.
  - Replace open_calls with c-life-reset-runtime-architecture-001.
  - Replace NOW.next with CALL c-life-reset-runtime-architecture-001.

  work/:
  - Update life-reset-runtime-boundary-v0.md superseded route to skeleton ->
    audit -> concrete contract later.
  - Add third repair note to sunday-planning-packet-v0.md: it is not runtime
    architecture and must not be used before the runtime skeleton exists.

  LOG.md:
  - Append the route repair line.

  history/:
  - Add this file:
    live/life-reset/history/2026-06-20-s-life-reset-runtime-architecture-route-repair-001.md.

captures:
  - Possible OS maintenance: when a direction creates a separate runtime/product,
    do not split architecture into an arbitrary provider-instruction task unless
    the owner approved that cut.

decisions_needed: []

play_check:
  - "1 Name the contradiction: done — state still named a provider-instruction task and a concrete Weekly Contract as near-term work, while owner required the full runtime architecture first."
  - "2 Reconstruct: done — Weekly Contract is a term from CHARTER/TREE for a later concrete week plan; it was incorrectly promoted into the active next route."
  - "3 Propose corrected state: done — next is runtime repository/workspace plus architecture skeleton; provider behavior is only one component; concrete contracts come later."
  - "4 Confirm: done — owner correction quoted in evidence, including \"сначала делать, потом все виклик контракты\"."
  - "5 Friction: skipped — captured maintenance candidate; no os/** edit in this direction repair."

log: "repair: removed premature provider-instruction task and concrete Weekly Contract from the active route; next is full runtime architecture skeleton in the separate runtime repository/workspace."

next: |
  CALL c-life-reset-runtime-architecture-001
  to: session
  direction: life-reset
  play: work
  node: g-lr-weekly-operating-graph
  task: t-1
  goal: |
    The separate Life-reset Runtime v0 repository/workspace exists or is
    selected and contains the runtime architecture skeleton.
  context: |
    Read live/life-reset/NOW.md and the files referenced by its next CALL.
  boundaries: |
    Do not create or accept a concrete Weekly Contract in this CALL.
    Do not run daily operation.
    Do not reduce the task to provider-facing instructions alone.
  done_when: |
    A concrete runtime repository/workspace path or URL is recorded, and the
    runtime substrate contains architecture files or documents covering the v0
    runtime skeleton listed in NOW.md.
  return: |
    RESULT with runtime substrate pointer, architecture artifact list or exact
    blocker, state_changes and next CALL.
  budget: one focused architecture/bootstrap session

END_OF_FILE: live/life-reset/history/2026-06-20-s-life-reset-runtime-architecture-route-repair-001.md
