RESULT s-life-reset-tree-invalid-remap-repair-001 (call: owner-tree-invalid-remap-2026-06-20)
direction: life-reset   play: repair   node/task: g-lr-weekly-operating-graph

outcome: |
  The current life-reset TREE is no longer treated as valid active planning
  state. The old g-lr-weekly-operating-graph/runtime-architecture route is
  stopped, NOW has no active bet, and the next CALL is a map/replan session to
  produce an owner-approved replacement top-level TREE.

evidence: |
  Owner instruction in-session:
  - "дерево сейчас невалидное полностью, заново надо переделывать,
    перепланировать"

  Reconstructed drift:
  - 2026-06-20 shape made g-lr-weekly-operating-graph the first active weekly
    planning bet.
  - Later repairs moved the route from concrete Weekly Contract to runtime
    boundary, runtime substrate, runtime architecture skeleton and Data /
    Memory / Retrieval.
  - The active work therefore became whole-runtime/foundation work while the
    tree node still named only weekly operating graph.

state_changes: |
  TREE.md:
  - Add owner_approved evidence for the invalidation.
  - Add tree_validity.state: invalid_pending_remap.
  - Change g-lr-weekly-operating-graph status active -> parked.
  - Add repair_note explaining that this node/name is not the active first-node
    frame and must be reconsidered in remap.

  NOW.md:
  - Replace active_bet with status: none and repair_status:
    tree_invalid_pending_remap.
  - Preserve the old work/history artifacts as evidence only.
  - Replace tasks with [].
  - Replace open_calls with c-life-reset-remap-001.
  - Replace NOW.next with CALL c-life-reset-remap-001 using play: map.
  - Explicitly stop the old c-life-reset-runtime-architecture-001 route.

  LOG.md:
  - Append the tree-invalid repair line.

  os/FRICTION.md:
  - Append a watching line for wedge/scope drift after repeated repairs.

  history/:
  - Add this file:
    live/life-reset/history/2026-06-20-s-life-reset-tree-invalid-remap-repair-001.md.

captures: []

decisions_needed: []

play_check:
  - "1 Name the contradiction: done — TREE still presented g-lr-weekly-operating-graph as active, while owner said the current tree is invalid and must be redone."
  - "2 Reconstruct: done — the first weekly wedge drifted through repairs into whole-runtime/foundation architecture work; the node name/scope no longer matched reality."
  - "3 Propose corrected state: done — stop old work route, park the old active node, mark tree invalid_pending_remap, and set next to a map/replan CALL."
  - "4 Confirm: done — owner explicitly instructed: \"дерево сейчас невалидное полностью, заново надо переделывать, перепланировать\"."
  - "5 Friction: done — os/FRICTION.md records the repeated wedge/scope drift pattern."

log: "repair: owner invalidated the current life-reset TREE as active planning state; old weekly/runtime route is stopped and next is c-life-reset-remap-001."

next: |
  CALL c-life-reset-remap-001
  to: session
  direction: life-reset
  play: map
  node: g-life-reset-root
  goal: |
    Life-reset has an owner-approved replacement top-level TREE that reflects
    the real system scope.
  context: |
    Read live/life-reset/NOW.md and the files referenced by its next CALL.
  boundaries: |
    Do not run the old runtime-architecture work CALL.
    Do not create or accept a concrete Weekly Contract.
    Do not run daily operation.
    Do not assume the old six-node map is valid.
    Do not edit CHARTER.md in map; if the charter itself proves wrong, return a
    frame CALL instead.
  done_when: |
    TREE.md contains an owner-approved revised top-level map for life-reset, or
    the session returns an explicit frame CALL because the charter/root is the
    real problem. NOW.md carries the next valid shape CALL or awaiting_decision.
  return: |
    RESULT with owner-approved TREE replacement or frame route, state_changes,
    evidence and next CALL.
  budget: one map/replan session

END_OF_FILE: live/life-reset/history/2026-06-20-s-life-reset-tree-invalid-remap-repair-001.md
