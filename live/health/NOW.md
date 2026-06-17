# NOW — health

active_bet:
  status: none
  note: >
    No active bet. g-health-nutrition-system remains closed by prior binding G5 file/functionality
    evidence, but the first owner-facing nutrition startup attempt exposed a workflow defect:
    Health AI nutrition has artifacts, yet no strict owner-approved operating graph for program,
    cycle, week, day, review, and mutation flow. Do not shape/start the first real nutrition
    execution cycle or move to training until the nutrition workflow contract is converged.

tasks: []

open_calls: []

recurring: []

decisions: []

next: |
  CALL c-health-nutrition-workflow-converge-arch-001
  to: session
  direction: health
  play: converge-arch
  node: g-health-nutrition-system
  goal: |
    Health AI nutrition has an architecture/contract surface for the newly closed workflow graph
    WHAT so startup, program, cycle, week plan, day loop, review, and mutation can be implemented
    without recreating the rejected wall-of-content UX.
  context: |
    Read:
    - live/health/CHARTER.md
    - live/health/TREE.md
    - live/health/NOW.md
    - live/health/work/converge-g-health-nutrition-workflow-graph.md
    - live/health/work/converge-g-health-nutrition-system.md
    - live/health/work/converge-g-health-nutrition-system-arch.md
    - live/health/knowledge/health-nutrition-system-g5-review.md
    - health-ai AGENTS.md
    - health-ai SYSTEM.md
    - health-ai x_nutrition/index.md
    - health-ai x_nutrition/procedures/operator-seams.md
    - health-ai x_nutrition/programs/active-program.md
    - health-ai x_nutrition/cycles/first-cycle.md
    - health-ai x_nutrition/logs/YYYY-MM-DD.md
    - health-ai x_nutrition/reviews/first-cycle-review.md

    Current contradiction:
    - Nutrition artifacts exist and previously passed G5, but owner rejected the startup UX because
      it produced a wall of menu/recipe/shopping/log content instead of a strict workflow.
    - The converge session closed WG1-WG14 as the WHAT overlay for the missing workflow graph.
    - Existing Health AI nutrition artifacts are seeds/evidence only, not accepted owner-facing
      workflow UX.

    Required architecture outcome:
    - Map WG1-WG14 to Health AI file/procedure/operator contracts.
    - Define how the operator resolves current workflow state and routes one-chat-one-task.
    - Define architecture boundaries for startup/router, program, cycle, week plan, day loop,
      review, mutation, block conditions, and writer handoff.
    - Preserve Direction OS raw-data boundary and Health AI free-form owner input boundary.
  boundaries: |
    Do not start nutrition execution.
    Do not produce menus, recipes, grocery lists, shopping instructions, daily plans, or food logs.
    Do not move to training/activity.
    Do not edit product repo code in this session.
    Do not ask owner to choose expert nutrition variables.
    Do not add UI/app/runtime/server/database/cron/scheduler/background-worker requirements.
    Do not rewrite g-health-core or duplicate core-owned concepts.
    Keep owner-facing output compact; if too large, close with a checkpoint and next CALL.
  done_when: |
    A closed architecture/contract surface exists for the nutrition workflow graph WHAT:
    every WG1-WG14 row is mapped to concrete Health AI state/procedure/file/operator contract
    obligations or explicitly rejected as HOW, with open/deferred/blocker rows equal to zero,
    and the set is ready for converge-verify.
  return: |
    RESULT with architecture artifact changes, coverage WG1-WG14, state_changes, and next CALL.
  budget: one focused converge-arch session; workflow graph only
END_OF_FILE: live/health/NOW.md
