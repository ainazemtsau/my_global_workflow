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
  CALL c-health-nutrition-workflow-converge-verify-001
  to: session
  direction: health
  play: converge-verify
  node: g-health-nutrition-system
  goal: |
    Health AI nutrition workflow graph architecture closure has survived refutation and is
    ready for the next routing decision without restarting nutrition execution.
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
    - health-ai AGENTS.md
    - health-ai SYSTEM.md
    - health-ai x_nutrition/index.md
    - health-ai x_nutrition/procedures/operator-seams.md
    - health-ai x_nutrition/procedures/provider-continuation.md
    - health-ai x_nutrition/procedures/writer-handoff.md
    - health-ai x_nutrition/state/first-setup-pending.md
    - health-ai x_nutrition/programs/active-program.md
    - health-ai x_nutrition/cycles/first-cycle.md
    - health-ai x_nutrition/logs/YYYY-MM-DD.md
    - health-ai x_nutrition/reviews/first-cycle-review.md

    Closure claims to test:
    - WG1-WG14 all map to concrete Health AI state/procedure/file/operator obligations
      in WGA0-WGA15.
    - No open/deferred/blocker rows remain.
    - Architecture does not restart nutrition execution or produce menus, recipes,
      grocery lists, shopping instructions, daily plans, or food logs.
    - Existing Health AI nutrition artifacts are subordinated to the workflow graph
      as seeds/evidence, not accepted startup UX.
    - Direction OS raw-data boundary and Health AI free-form owner input boundary are preserved.
    - g-health-core ownership is preserved; nutrition owns only namespaced workflow/module state.
    - No app/UI/runtime/server/database/cron/scheduler/background-worker requirement is introduced.
  boundaries: |
    Do not start nutrition execution.
    Do not produce menus, recipes, grocery lists, shopping instructions, daily plans, or food logs.
    Do not move to training/activity.
    Do not edit product repo code.
    Do not ask owner to choose expert nutrition variables.
    Do not rewrite g-health-core or duplicate core-owned concepts.
  done_when: |
    Refutation finds no counterexample to the WG1-WG14 architecture closure, or names the exact
    blocker row and routes back to repair/converge-arch. Passing output must state open rows 0,
    deferred rows 0, blocker rows 0, and whether the set can route onward.
  return: |
    RESULT with refutation verdict, blocker rows if any, state_changes, and next CALL.
  budget: one focused converge-verify session; workflow graph architecture only
END_OF_FILE: live/health/NOW.md
