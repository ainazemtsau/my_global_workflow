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
  CALL c-health-nutrition-workflow-shape-001
  to: session
  direction: health
  play: shape
  node: g-health-nutrition-system
  goal: |
    Health AI nutrition workflow graph implementation is shaped as the next bounded bet without
    starting nutrition execution.
  context: |
    Read:
    - live/health/CHARTER.md
    - live/health/TREE.md
    - live/health/NOW.md
    - live/health/work/converge-g-health-nutrition-workflow-graph.md
    - live/health/work/converge-g-health-nutrition-workflow-graph-arch.md
    - live/health/work/converge-g-health-nutrition-system.md
    - live/health/work/converge-g-health-nutrition-system-arch.md
    - live/health/knowledge/health-nutrition-system-g5-review.md
    - health-ai/AGENTS.md
    - health-ai/SYSTEM.md
    - health-ai/x_nutrition/index.md
    - health-ai/x_nutrition/procedures/operator-seams.md
    - health-ai/x_nutrition/procedures/provider-continuation.md
    - health-ai/x_nutrition/procedures/writer-handoff.md
    - health-ai/x_nutrition/state/first-setup-pending.md
    - health-ai/x_nutrition/programs/active-program.md
    - health-ai/x_nutrition/cycles/first-cycle.md
    - health-ai/x_nutrition/logs/YYYY-MM-DD.md
    - health-ai/x_nutrition/reviews/first-cycle-review.md

    Verified closure to preserve:
    - converge-verify passed on 2026-06-17.
    - open rows: 0
    - deferred rows: 0
    - blocker rows: 0
    - WG1-WG14 WHAT rows and WGA0-WGA15 architecture contracts survived refutation.

    Acceptance rows / contracts to copy into any executor done_when:
    - WG1-WG14 acceptance rows from `converge-g-health-nutrition-workflow-graph.md`.
    - WGA0-WGA15 contract + acceptance rows from
      `converge-g-health-nutrition-workflow-graph-arch.md`.
    - Especially preserve:
      - WGA0 workflow authority surface
      - WGA1 startup/router operator contract
      - WGA2 state descriptor completeness
      - WGA3 canonical transition contract
      - WGA10 one-chat-one-task output contract
      - WGA12 Direction OS boundary contract
      - WGA13 seed artifact authority contract
      - WGA14 safety and block routing contract
      - WGA15 writer handoff / validation contract

    PLAN-agenda:
    - Shape only the implementation routing for workflow graph authority, current workflow cursor,
      workflow router, and writer validation.
    - Exact serialization, prompt wording, per-state file split, scheduling, UI/app/runtime/server/DB/cron,
      external recipe/shopping integrations, and nutrition content generation are not accepted requirements
      unless a later owner-approved shape explicitly scopes them.
    - Existing active program/cycle/menu/grocery/fallback/LOG/review files are seed/evidence only until the
      workflow router selects a bounded state.
  boundaries: |
    Do not start nutrition execution.
    Do not produce menus, recipes, grocery lists, shopping instructions, daily plans, or food logs.
    Do not move to training/activity.
    Do not edit product repo code.
    Do not ask owner to choose expert nutrition variables.
    Do not rewrite g-health-core or duplicate core-owned concepts.
    Do not introduce app UI, runtime, server, database, cron, scheduler, background worker,
    recipe service, shopping service, or external automation as a requirement.
  done_when: |
    A bounded implementation bet/task set is ready for owner approval or an explicit park/review route is
    recorded. Any executor done_when copies WG1-WG14 acceptance plus WGA0-WGA15 contracts as binding
    acceptance, and explicitly blocks nutrition execution until the workflow authority surface, current-state
    cursor, workflow router, and writer-validation gates are implemented or consciously re-routed.
  return: |
    RESULT with shaped bet/task proposal, owner approvals required by shape, state_changes, and next CALL.
  budget: one focused shape session; workflow graph implementation routing only
END_OF_FILE: live/health/NOW.md
