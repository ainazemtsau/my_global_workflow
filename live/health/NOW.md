# NOW — health

active_bet:
  status: none
  note: >
    No active bet. The workflow authority gate bet met review/refutation in
    s-health-nutrition-workflow-authority-review-004 on 2026-06-18:
    health-ai graph/current-workflow/router/writer validation passed WG1-WG14
    and WGA0-WGA15 checks with blocker_gaps=0, and no nutrition execution
    content was introduced. Owner chose A on 2026-06-18, selecting first real
    Health AI nutrition execution cycle shaping next.

tasks: []

open_calls: []

recurring: []

decisions: []

next: |
  CALL c-health-first-nutrition-cycle-shape-002
  to: session
  direction: health
  play: shape
  node: g-health-first-nutrition-cycle
  goal: |
    g-health-first-nutrition-cycle is ready as the next bounded health bet.
  context: |
    Owner chose A from d-health-workflow-authority-next-bet-001 with: "A".
    This selects: shape first real Health AI nutrition execution cycle next.

    Workflow authority review evidence:
    - s-health-nutrition-workflow-authority-review-004 returned verdict met.
    - health-ai commits reviewed:
      - bc1680533952c2e10ee5b61795a792470bc3d7ba
      - 50d70b66c922725888c2353bc6018387874fc27c
      - 1933375079372fb18d422103ff62b8e7620dce31
    - tools/check_nutrition_continuation.py passed: 40 rows pass, 0 fail,
      blocker gaps 0.
    - WG1-WG14 and WGA0-WGA15 are present in
      acceptance/x_nutrition/provider-continuation-matrix.json.
    - Writer negative fixtures reject legacy-W/NCA/B-preserving WG/WGA
      violations.
    - Durable fact:
      live/health/knowledge/health-nutrition-workflow-authority-g5-review.md.

    Tree state:
    - g-health-nutrition-system is done.
    - g-health-first-nutrition-cycle is parked and ready to shape.

    Health AI workflow authority files:
    - health-ai x_nutrition/workflow/graph.md
    - health-ai x_nutrition/state/current-workflow.md
    - health-ai x_nutrition/procedures/workflow-router.md
    - health-ai x_nutrition/procedures/provider-continuation.md
    - health-ai x_nutrition/procedures/writer-handoff.md
  boundaries: |
    Do not store raw daily food logs, photos, or check-ins in Direction OS.
    Do not bypass the Health AI workflow-router/current-workflow gate.
    Do not rebuild the nutrition architecture.
    Do not build product repo code unless a later executor CALL asks for it.
    Do not ask owner to choose expert nutrition variables.
    Do not move into training/activity in this nutrition-cycle bet.
    Do not make medical diagnoses or prescriptions.
  done_when: |
    g-health-first-nutrition-cycle is shaped as an approved bounded bet, and
    NOW has the next ready CALL.
  return: |
    RESULT with shaped bet, state_changes, decisions_needed, and next CALL.
  budget: one focused shape session

END_OF_FILE: live/health/NOW.md
