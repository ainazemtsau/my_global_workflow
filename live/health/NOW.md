# NOW — health

active_bet:
  status: none
  note: >
    2026-06-20 owner rejected the current Health AI nutrition / first-cycle
    work as not accepted. The problem is not a narrow repair: menu, recipes,
    grocery/prep, first-cycle execution, and the current interaction/writer
    flow were produced without enough owner co-creation, approval, and
    one-chat-one-job handoff. The previous Health AI nutrition files may be
    used only as dirty prototype/evidence, not as authority or accepted
    execution content. Rebuild starts from a new owner-approved structure.

tasks: []

open_calls:
  - id: c-health-nutrition-system-rebuild-converge-001
    status: ready
    note: >
      Restart g-health-nutrition-system from scratch. First produce an
      owner-approved structure/WHAT/process contract before any product repo
      cleanup, rebuild, menu, recipe, grocery, or execution work proceeds.

recurring: []

decisions: []

next: |
  CALL c-health-nutrition-system-rebuild-converge-001
  to: session
  direction: health
  play: converge
  node: g-health-nutrition-system
  goal: |
    A new owner-approved Health AI nutrition structure exists before any rebuild,
    cleanup, menu, recipe, grocery, or execution work proceeds.
  context: |
    Owner rejection on 2026-06-20:
    - Current Health AI nutrition work is rejected completely, not accepted as
      a working node.
    - "Хелс ничего чинить не надо"; the current files are to be archived or
      deleted by a later bounded product task, not repaired in place.
    - Existing work may be used only as evidence/dirty prototype.
    - Menu, recipes, grocery/prep, first-cycle execution, and writer/ChatGPT
      continuation were not co-created with the owner and must not be treated
      as accepted authority.
    - The new solution must be designed like software architecture: roles,
      process graph, artifact contracts, owner approval gates, writer gates,
      one chat = one job, and next CALL/card after each job.
    - Until the owner accepts the structure, no rebuild/execution should start.

    Current Direction OS repair result:
    - g-health-nutrition-system is parked for rebuild from scratch.
    - g-health-first-nutrition-cycle is dropped as a rejected execution bet.
    - There is no active bet.

    Dirty/non-authoritative Health AI product families observed:
    - health-ai/x_nutrition/program-synthesis/active-program-synthesis.md
    - health-ai/x_nutrition/programs/active-program.md
    - health-ai/x_nutrition/cycles/first-cycle.md
    - health-ai/x_nutrition/menus/current-menu-cycle.md
    - health-ai/x_nutrition/recipes/first-cycle-base-recipes.md
    - health-ai/x_nutrition/grocery/current-grocery-needs.md
    - health-ai/x_nutrition/fallbacks/fallback-meals.md
    - health-ai/x_nutrition/reviews/first-cycle-review.md
    - health-ai/x_nutrition/logs/YYYY-MM-DD.md

    Potentially reusable only as evidence/control-plane references, not as
    accepted nutrition content:
    - health-ai/x_nutrition/workflow/graph.md
    - health-ai/x_nutrition/state/current-workflow.md
    - health-ai/x_nutrition/procedures/*
    - health-ai/acceptance/x_nutrition/*
    - prior research/report/check evidence, if explicitly re-imported into the
      new owner-approved process.
  boundaries: |
    Do not continue the current first-cycle execution.
    Do not repair the existing menu/recipe/cycle content in place.
    Do not treat any existing x_nutrition owner-facing content as accepted.
    Do not emit or save menu, recipes, grocery/prep, daily plan, or execution
    artifacts before owner-approved structure and explicit later task.
    Do not ask the owner to choose expert nutrition variables as a substitute
    for system design.
    Do not store raw daily food logs/photos/check-ins in Direction OS.
    Do not delete or archive product repo files in this converge session; that
    must be a later bounded executor CALL after the reset structure is accepted.
  done_when: |
    Owner has approved a new Health AI nutrition WHAT/process structure that
    defines roles, artifact families, approval gates, recipe/menu/grocery
    lifecycle, writer behavior, one-chat-one-job handoff, and cleanup/rebuild
    boundaries; all open design terms are closed or routed to explicit owner
    decisions, with no execution content produced.
  return: |
    RESULT with the owner-approved structure, open decisions if any, state_changes,
    and next CALL. The next CALL should not rebuild product files until the owner
    has accepted the structure.
  budget: one focused converge session

END_OF_FILE: live/health/NOW.md
