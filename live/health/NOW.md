# NOW — health

active_bet:
  id: b-health-nutrition-workflow-authority-gate
  node: g-health-nutrition-system
  status: active
  appetite: 1 focused implementation day
  approved_by_owner: "A"
  approved_at: 2026-06-17
  goal: >
    Health AI nutrition cannot start or continue owner-facing nutrition execution until
    a product-side workflow authority surface, current workflow cursor, workflow router,
    and writer-validation gate enforce the accepted workflow graph contracts.
  forecast: >
    Likely bounded because this is a routing/validation gate over the existing nutrition namespace
    and accepted workflow contracts, not a nutrition content rebuild.
  against: >
    Main risk is prose-only compliance: files/checks may exist but startup still loads output-heavy
    seed artifacts or writer validation ignores WG/WGA.
  kill_by: >
    2026-06-20 12:00 Europe/Amsterdam: if there is no committed Health AI implementation
    with workflow graph authority, current workflow cursor, workflow-router startup path,
    WG1-WG14 + WGA0-WGA15 writer validation evidence, passing checks, and zero nutrition
    execution output produced during implementation/review, stop and route to review/repair
    instead of extending.
  next_if_true: >
    Route to fresh review/refutation. If review passes, next planning route may shape
    g-health-first-nutrition-cycle or run a separate workflow-router startup CALL; this bet
    itself does not start nutrition execution.
  next_if_false: >
    Route to review/repair/converge-arch with exact failed WG/WGA row; do not extend appetite.

tasks:
  - id: t-1
    kind: executor
    repo: ainazemtsau/health-ai
    goal: >
      Implement the Health AI nutrition workflow authority surface and current-state cursor so
      nutrition startup has a file-backed graph and current workflow state before execution.
    done_when: >
      Commit/PR evidence shows Health AI nutrition has an explicit workflow authority surface,
      including the WGA0-required graph/cursor/procedure surface or equivalent stricter product
      implementation; startup cannot proceed if graph or current-state cursor is missing, stale,
      or contradictory; no nutrition execution content is produced. Binding acceptance includes
      all WG1-WG14 acceptance rows and WGA0-WGA15 contract+acceptance rows copied in the executor CALL.
    status: done

  - id: t-2
    kind: executor
    repo: ainazemtsau/health-ai
    goal: >
      Implement the workflow-router startup/continuation route so one nutrition chat resolves exactly
      one workflow state and returns one bounded task/question/action before reading or emitting any
      output-heavy nutrition artifact.
    done_when: >
      Commit/PR evidence shows startup/continuation is subordinated to workflow-router/current-workflow;
      active program/cycle/menu/grocery/fallback/LOG/review files are seeds/evidence until their state
      is selected; router blocks prompt-only, all-artifacts-at-once, raw diary, expert-variable questionnaire,
      core rewrite, and forbidden infrastructure paths. No nutrition execution content is produced.
      Binding acceptance includes all WG1-WG14 acceptance rows and WGA0-WGA15 contract+acceptance rows
      copied in the executor CALL.
    status: pending

  - id: t-3
    kind: executor
    repo: ainazemtsau/health-ai
    goal: >
      Extend nutrition writer handoff and validation checks so any workflow-affecting write validates
      WG1-WG14 and WGA0-WGA15 in addition to W1-W13, NCA0-NCA9, and B1-B3.
    done_when: >
      Commit/PR evidence shows writer validation rejects packets that preserve old nutrition acceptance
      rows but violate workflow graph obligations, especially startup/router, one-chat-one-task,
      seed artifact authority, Direction OS diary boundary, block routing, and workflow-affecting writes
      without resolved state/target artifact family/source graph rows/boundary statement. Required checks
      pass or exact failing check output is reported. No nutrition execution content is produced.
      Binding acceptance includes all WG1-WG14 acceptance rows and WGA0-WGA15 contract+acceptance rows
      copied in the executor CALL.
    status: pending

  - id: t-4
    kind: session
    play: review
    goal: >
      Freshly refute the implementation claim against WG1-WG14 and WGA0-WGA15 before any nutrition execution.
    done_when: >
      A separate review session verifies from repo evidence and check output that workflow authority surface,
      current-state cursor, workflow-router, and writer-validation gates are implemented; open/deferred/blocker
      rows remain zero or the exact failed row is named; no menus, recipes, grocery lists, shopping instructions,
      daily plans, food logs, training/activity work, core rewrite, or forbidden infrastructure were introduced.
    status: pending

open_calls: []

recurring: []

decisions: []

next: |
  CALL c-health-nutrition-workflow-authority-executor-002
  to: executor
  direction: health
  node: g-health-nutrition-system
  task: t-2
  repo: ainazemtsau/health-ai
  kind: engineering
  goal: |
    Health AI nutrition startup and continuation resolve exactly one current workflow state
    and one bounded next task/question/action before any output-heavy nutrition artifact can
    be read or emitted.
  context: |
    Product evidence already committed by t-1:
    - health-ai commit bc1680533952c2e10ee5b61795a792470bc3d7ba
    - Added x_nutrition/workflow/graph.md
    - Added x_nutrition/state/current-workflow.md
    - Added x_nutrition/procedures/workflow-router.md
    - Extended x_nutrition/procedures/provider-continuation.md and writer-handoff validation.
    - Extended acceptance/x_nutrition/provider-continuation-matrix.json with WG1-WG14 and
      WGA0-WGA15 rows.
    - Full product write barrier passed on 2026-06-18.

    Read in Direction OS:
    - live/health/CHARTER.md
    - live/health/TREE.md
    - live/health/NOW.md
    - live/health/work/converge-g-health-nutrition-workflow-graph.md
    - live/health/work/converge-g-health-nutrition-workflow-graph-arch.md
    - live/health/knowledge/health-nutrition-system-g5-review.md

    Read in product repo:
    - AGENTS.md
    - SYSTEM.md
    - x_nutrition/index.md
    - x_nutrition/workflow/graph.md
    - x_nutrition/state/current-workflow.md
    - x_nutrition/procedures/workflow-router.md
    - x_nutrition/procedures/provider-continuation.md
    - x_nutrition/procedures/writer-handoff.md
    - x_nutrition/state/first-setup-pending.md
    - acceptance/x_nutrition/provider-continuation-matrix.json
    - tools/check_nutrition_continuation.py
  boundaries: |
    Do not start nutrition execution.
    Do not produce menus, recipes, grocery lists, shopping instructions, daily plans, or food logs.
    Do not move to training/activity.
    Do not ask owner to choose expert nutrition variables.
    Do not rewrite g-health-core or duplicate core-owned concepts.
    Do not introduce app UI, runtime, server, database, cron, scheduler, background worker,
    recipe service, shopping service, or external automation as a requirement.
    Keep nutrition changes namespaced under x_nutrition/ unless an existing product check requires
    an acceptance/check file update.
  done_when: |
    Commit/PR evidence shows startup/continuation is subordinated to workflow-router/current-workflow;
    active program/cycle/menu/grocery/fallback/LOG/review files are seeds/evidence until their state
    is selected; router blocks prompt-only, all-artifacts-at-once, raw diary, expert-variable
    questionnaire, core rewrite, and forbidden infrastructure paths. No nutrition execution content is
    produced. Binding acceptance includes WG1-WG14 acceptance rows and WGA0-WGA15 contract+acceptance
    rows in product acceptance/x_nutrition/provider-continuation-matrix.json.
  return: |
    RESULT with commit/PR evidence, checks run and outputs, exact files changed, whether WG1-WG14 and
    WGA0-WGA15 pass, proof that no nutrition execution content was produced, and next CALL for t-3 or review.
  budget: one focused implementation day

END_OF_FILE: live/health/NOW.md
