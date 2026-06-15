# NOW — health

active_bet:
  status: none
  note: >
    No active bet after owner-approved close of g-health-core. Corrected G5 verdict
    was met in c-health-core-review-002; owner approved closing the node and taking
    recommendation A, shaping g-health-nutrition-system next.

tasks: []

recurring: []

open_calls: []

decisions: []

next: |
  CALL c-health-nutrition-shape-001
  to: session
  direction: health
  play: shape
  node: g-health-nutrition-system
  goal: |
    g-health-nutrition-system is shaped as the first module-on-core bet after g-health-core closure.
  context: |
    Owner approved decision d-health-core-close-and-next-bet with: "approve".
    This closes g-health-core as done and selects recommendation A: shape g-health-nutrition-system next.

    c-health-core-review-002 returned corrected binding G5 verdict met for g-health-core.

    Read:
    - live/health/CHARTER.md
    - live/health/TREE.md
    - live/health/NOW.md
    - live/health/knowledge/health-core-corrected-g5-review.md
    - health-ai commit 8bc980ad21d3f54cbd27b28dcb363e0198c46751
    - acceptance/core/evidence-summary.md
    - acceptance/core/matrix.json

    Core contract to consume:
    - nutrition is a module on g-health-core, not a duplicate core
    - consume core-owned metrics, phase, PLAN-vs-LOG, review, parser/library, value grammar, and safety floor
    - raw daily food/weight data stays in Health AI, not Direction OS
  boundaries: |
    Do not store raw daily food, weight, or check-in logs in Direction OS.
    Do not build product repo implementation during shape.
    Do not build training/activity module.
    Do not build app UI, runtime, DB, server, cron, or scheduler.
    Do not make medical prescriptions.
    Do not rewrite g-health-core; nutrition consumes it.
  done_when: |
    - One shaped g-health-nutrition-system bet draft exists with appetite, kill_by, cut list, lens sweep, and tasks.
    - The first task tests the riskiest nutrition-module assumption on top of g-health-core.
    - TREE/NOW state_changes only enter after explicit owner approval under G9.
  return: |
    RESULT with shaped bet draft, proposed state_changes, decisions_needed, and next CALL/awaiting_decision.
  budget: one focused shape session
  surface: any capable session

END_OF_FILE: live/health/NOW.md
