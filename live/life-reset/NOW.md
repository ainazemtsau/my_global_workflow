# NOW — life-reset

active_bet:
  status: none
  repair_status: tree_invalid_pending_remap
  note: |
    2026-06-20: owner invalidated the current TREE as the active planning
    frame: "дерево сейчас невалидное полностью, заново надо переделывать,
    перепланировать".

    Do not run the previous runtime-architecture CALL
    c-life-reset-runtime-architecture-001 and do not continue work under
    g-lr-weekly-operating-graph before remap.

    The root charter remains input unless the remap session finds it wrong and
    explicitly routes to frame. Existing work/history artifacts remain evidence,
    not authority.
  preserved_evidence:
    - live/life-reset/work/weekly-operating-graph-dry-run-v0.md
    - live/life-reset/work/sunday-planning-packet-v0.md
    - live/life-reset/work/life-reset-runtime-boundary-v0.md
    - live/life-reset/work/life-reset-runtime-data-memory-retrieval-requirements-v0.md
    - live/life-reset/history/2026-06-20-s-life-reset-weekly-operating-graph-shape-001.md
    - live/life-reset/history/2026-06-20-s-life-reset-runtime-boundary-001.md
    - live/life-reset/history/2026-06-20-s-life-reset-runtime-route-reset-001.md
    - live/life-reset/history/2026-06-20-s-life-reset-runtime-architecture-route-repair-001.md
    - live/life-reset/history/2026-06-20-s-life-reset-runtime-memory-route-repair-001.md
  blocked_reason: |
    The current tree names and structures the first active path as weekly
    operating graph, but the owner clarified that the actual next structure
    must represent the whole life-reset runtime/system foundation, not merely a
    weekly planning component.

tasks: []

recurring: []

open_calls:
  - id: c-life-reset-remap-001
    to: session
    for: g-life-reset-root
    issued: 2026-06-20
    note: >
      Rebuild the life-reset top-level tree with the owner. Current TREE is
      invalid as active planning state; old runtime/weekly artifacts are input
      evidence only.

decisions: []

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
    Read:
    - live/life-reset/CHARTER.md
    - live/life-reset/TREE.md
    - live/life-reset/NOW.md
    - live/life-reset/LOG.md
    - live/life-reset/history/2026-06-19-s-life-reset-map-evidence-001.md
    - live/life-reset/history/2026-06-19-s-life-reset-map-001.md
    - live/life-reset/history/2026-06-20-s-life-reset-weekly-operating-graph-shape-001.md
    - live/life-reset/history/2026-06-20-s-life-reset-runtime-route-reset-001.md
    - live/life-reset/history/2026-06-20-s-life-reset-runtime-architecture-route-repair-001.md
    - live/life-reset/history/2026-06-20-s-life-reset-runtime-memory-route-repair-001.md
    - live/life-reset/work/life-reset-runtime-boundary-v0.md
    - live/life-reset/work/life-reset-runtime-data-memory-retrieval-requirements-v0.md
    - live/life-reset/work/weekly-operating-graph-dry-run-v0.md
    - live/life-reset/work/sunday-planning-packet-v0.md
    - os/KERNEL.md
    - os/plays/map.md
    - os/plays/research.md
    - os/adapters/coding-agent.md

    Owner instruction:
    - "дерево сейчас невалидное полностью, заново надо переделывать,
      перепланировать"

    Diagnosis to carry forward:
    - The old first node name/scope "weekly operating graph" was too narrow.
    - The actual system needs a coherent life-reset runtime/foundation framing:
      operating surface, durable state, data/memory/retrieval, weekly planning,
      daily operation, intake/backlog, process/technique lifecycle, review and
      source-direction boundaries.
    - Existing work artifacts may be mined as evidence, but they are not the
      active route and must not force the new tree.
  boundaries: |
    Do not run the old runtime-architecture work CALL.
    Do not create or accept a concrete Weekly Contract.
    Do not run daily operation.
    Do not assume the old six-node map is valid.
    Do not preserve "weekly operating graph" as the first active node unless
    the owner explicitly re-approves it during map.
    Do not edit CHARTER.md in map; if the charter itself proves wrong, return a
    frame CALL instead.
    Do not store raw health/game/Solmax data in life-reset.
    Do not prescribe nutrition, training, medical or psychiatric treatment.
  done_when: |
    - TREE.md contains an owner-approved revised top-level map for life-reset,
      or the session returns an explicit frame CALL because the charter/root is
      the real problem.
    - Every non-root node has goal, done_when, status and why.
    - The revised tree explicitly resolves whether runtime foundation is a
      top-level node, a first active node, or part of another structure.
    - The revised tree explicitly places weekly planning/Weekly Contract,
      daily runtime, data/memory/retrieval, intake/backlog,
      process/technique lifecycle, review/evolution and source-boundaries.
    - NOW.md no longer presents the old g-lr-weekly-operating-graph route as
      executable unless the new map explicitly approves it.
    - A next shape CALL is ready for the newly recommended first node, or an
      awaiting_decision state explains the unresolved owner decision.
  return: |
    RESULT with owner-approved TREE replacement or frame route, state_changes,
    evidence and next CALL.
  budget: one map/replan session

END_OF_FILE: live/life-reset/NOW.md
