# NOW — health

active_bet:
  status: none
  note: >
    No active bet after owner-approved close of g-health-nutrition-system. Binding G5 verdict
    was met in s-health-nutrition-t4-review-tomorrow-start-001; owner approved recommendation A
    with "Согласен с а", closing nutrition system and shaping first real nutrition execution next.

tasks: []

open_calls: []

recurring: []

decisions: []

next: |
  CALL c-health-first-nutrition-cycle-shape-001
  to: session
  direction: health
  play: shape
  node: g-health-first-nutrition-cycle
  goal: |
    The first real Health AI nutrition execution cycle is ready as the next health bet.
  context: |
    Owner approved decision d-health-nutrition-close-and-next-bet-001 with: "Согласен с а".
    This closes g-health-nutrition-system as done and selects recommendation A:
    add/shape first real Health AI nutrition execution cycle next.

    Nutrition review evidence:
    - s-health-nutrition-t4-review-tomorrow-start-001 returned binding G5 verdict met.
    - blocker_gaps=0.
    - tomorrow-start packet was produced in
      live/health/history/2026-06-17-s-health-nutrition-t4-review-tomorrow-start-001.md.
    - durable fact: live/health/knowledge/health-nutrition-system-g5-review.md.

    Tree state:
    - g-health-nutrition-system is done.
    - g-health-first-nutrition-cycle is parked and ready to shape.

    Health AI source files:
    - health-ai x_nutrition/programs/active-program.md
    - health-ai x_nutrition/cycles/first-cycle.md
    - health-ai x_nutrition/menus/current-menu-cycle.md
    - health-ai x_nutrition/grocery/current-grocery-needs.md
    - health-ai x_nutrition/fallbacks/fallback-meals.md
    - health-ai x_nutrition/logs/YYYY-MM-DD.md
    - health-ai x_nutrition/reviews/first-cycle-review.md
  boundaries: |
    Do not store raw daily food logs, photos, or check-ins in Direction OS.
    Do not rebuild the nutrition architecture.
    Do not build product repo code unless a later executor CALL asks for it.
    Do not ask owner to choose expert nutrition variables.
    Do not make medical diagnoses or prescriptions.
  done_when: |
    g-health-first-nutrition-cycle is shaped as an approved bet, and NOW has the next ready CALL.
  return: |
    RESULT with shaped bet, state_changes, decisions_needed, and next CALL.
  budget: one focused shape session

END_OF_FILE: live/health/NOW.md
