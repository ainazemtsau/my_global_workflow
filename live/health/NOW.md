# NOW — health

active_bet:
  status: none
  note: >
    No active bet. The workflow authority gate bet met review/refutation in
    s-health-nutrition-workflow-authority-review-004 on 2026-06-18:
    health-ai graph/current-workflow/router/writer validation passed WG1-WG14
    and WGA0-WGA15 checks with blocker_gaps=0, and no nutrition execution
    content was introduced. Nutrition execution remains not started here; next
    health bet choice is awaiting owner decision.

tasks: []

open_calls: []

recurring: []

decisions:
  - id: d-health-workflow-authority-next-bet-001
    status: awaiting_owner
    question: >
      Workflow authority review passed. Choose the next health bet posture before
      any nutrition execution starts?
    options:
      - id: A
        label: Shape first real Health AI nutrition execution cycle next
        why_now: >
          This turns the accepted workflow gate into body-value: a bounded first
          cycle can use the router, Health AI-only LOG, day-3 safety/friction
          check, and day-8 review without making Direction OS a raw diary.
        bad_because: >
          It delays training/activity architecture and starts with behavior proof
          before every health module exists.
      - id: B
        label: Shape training/activity system next
        why_now: >
          This attacks strength, body composition, activity, and conditioning
          while nutrition remains gated and ready.
        bad_because: >
          It risks more system-building before the already-built nutrition loop
          has survived first real use.
      - id: C
        label: Pause new Direction OS bets
        why_now: >
          Honest option if the owner wants to operate directly in Health AI for
          now and avoid another planning bet.
        bad_because: >
          Direction OS will not actively manage whether the first nutrition cycle
          produces a usable day-3/day-8 review.
    recommendation: A
    recommendation_reason: >
      Pick A because the highest-risk remaining assumption is no longer workflow
      authority; it is whether the owner can run the first nutrition cycle with
      Health AI-only logs and no Direction OS diary.

next: |
  awaiting_decision d-health-workflow-authority-next-bet-001

  recommended_next_on_A:
    CALL c-health-first-nutrition-cycle-shape-002
    to: session
    direction: health
    play: shape
    node: g-health-first-nutrition-cycle
    goal: |
      g-health-first-nutrition-cycle is ready as the next bounded health bet.
    context: |
      Requires owner decision A from d-health-workflow-authority-next-bet-001.

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
