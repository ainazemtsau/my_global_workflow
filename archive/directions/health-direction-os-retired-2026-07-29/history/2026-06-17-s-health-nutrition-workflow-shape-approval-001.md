RESULT s-health-nutrition-workflow-shape-approval-001 (call: c-health-nutrition-workflow-shape-001)
direction: health   play: shape   node/task: g-health-nutrition-system / decision
outcome: |
  Owner approved option A: activate the recommended one-day Health AI nutrition workflow authority
  implementation bet.

  Approved bet:
    id: b-health-nutrition-workflow-authority-gate
    node: g-health-nutrition-system
    goal: >
      Health AI nutrition cannot start or continue owner-facing nutrition execution until
      a product-side workflow authority surface, current workflow cursor, workflow router,
      and writer-validation gate enforce the accepted workflow graph contracts.
    appetite: 1 focused implementation day
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

evidence: |
  Owner approval in this session: "A".

  Decision brief presented:
  - A: approve recommended bet.
  - B: split before executor.
  - C: park/review.
  Recommendation was A.

  Preserved verified closure:
  - converge-verify passed on 2026-06-17.
  - open rows: 0.
  - deferred rows: 0.
  - blocker rows: 0.
  - WG1-WG14 WHAT rows and WGA0-WGA15 architecture contracts remain binding.
  - Existing Health AI nutrition artifacts remain seed/evidence only until workflow-router selects a bounded state.

state_changes: |
  Apply these exact state changes.

  1) live/health/NOW.md

  Replace current active_bet block:

    active_bet:
      status: none
      note: >
        No active bet. g-health-nutrition-system remains closed by prior binding G5 file/functionality
        evidence, but the first owner-facing nutrition startup attempt exposed a workflow defect:
        Health AI nutrition has artifacts, yet no strict owner-approved operating graph for program,
        cycle, week, day, review, and mutation flow. Do not shape/start the first real nutrition
        execution cycle or move to training until the nutrition workflow contract is converged.

  with:

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

  Replace:

    tasks: []

  with:

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
        status: pending

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

  Keep:
    open_calls: []
    recurring: []
    decisions: []

  Replace NOW.md next block with:

    next: |
      CALL c-health-nutrition-workflow-authority-executor-001
      to: executor
      direction: health
      node: g-health-nutrition-system
      task: t-1
      repo: ainazemtsau/health-ai
      kind: engineering
      goal: |
        Health AI nutrition has a file-backed workflow authority gate: workflow graph authority,
        current workflow cursor, workflow-router startup path, and writer validation enforce the
        accepted WG1-WG14 / WGA0-WGA15 contracts before any nutrition execution can start.
      context: |
        Read in Direction OS:
        - live/health/CHARTER.md
        - live/health/TREE.md
        - live/health/NOW.md
        - live/health/work/converge-g-health-nutrition-workflow-graph.md
        - live/health/work/converge-g-health-nutrition-workflow-graph-arch.md
        - live/health/work/converge-g-health-nutrition-system.md
        - live/health/work/converge-g-health-nutrition-system-arch.md
        - live/health/knowledge/health-nutrition-system-g5-review.md

        Read in product repo:
        - AGENTS.md
        - SYSTEM.md
        - x_nutrition/index.md
        - x_nutrition/procedures/operator-seams.md
        - x_nutrition/procedures/provider-continuation.md
        - x_nutrition/procedures/writer-handoff.md
        - x_nutrition/state/first-setup-pending.md
        - x_nutrition/programs/active-program.md
        - x_nutrition/cycles/first-cycle.md
        - x_nutrition/logs/YYYY-MM-DD.md
        - x_nutrition/reviews/first-cycle-review.md

        Verified closure to preserve:
        - converge-verify passed on 2026-06-17.
        - open rows: 0
        - deferred rows: 0
        - blocker rows: 0
        - WG1-WG14 WHAT rows and WGA0-WGA15 architecture contracts survived refutation.

        Product evidence before this bet:
        - Existing active program/cycle/menu/grocery/fallback/LOG/review files are seed/evidence only.
        - They cannot define accepted startup UX until workflow-router selects a bounded state.
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
        Implementation evidence:
        - Health AI nutrition startup has a file-backed workflow authority surface.
        - Current nutrition workflow state has a cursor/evidence surface.
        - Workflow-router is the first nutrition-facing operator path and returns exactly one current
          state plus one bounded next task/question/action.
        - Provider continuation/startup load order is subordinated to workflow-router before output-heavy
          active program/cycle/menu/grocery/fallback/LOG/review artifacts.
        - Writer handoff/validation rejects workflow-affecting writes that violate WG1-WG14 or WGA0-WGA15,
          even if old W1-W13/NCA0-NCA9/B1-B3 rows remain satisfied.
        - Required product checks pass, or exact failing check output is reported.
        - No nutrition execution content is produced.

        Binding WG1-WG14 acceptance rows:
        WG1 acceptance: A nutrition startup response can be checked mechanically: it has exactly one
        current state and one bounded next action, and it contains no menu, recipe, grocery list,
        shopping instruction, daily plan, or raw LOG dump unless the selected state specifically
        authorizes that exact artifact.
        WG2 acceptance: A future architect/executor can inspect each state and find purpose, inputs,
        owner-provided facts, AI-decided facts, output artifact, next state, stop/block conditions,
        and review trigger. If any field is missing, workflow execution is blocked.
        WG3 acceptance: Health AI can name the current nutrition state and the only allowed next state(s).
        It does not jump from startup directly into multi-artifact execution content.
        WG4 acceptance: Program setup/update produces or updates only the program-level artifact/packet.
        It does not produce menus, grocery lists, recipes, or daily plans in the same chat.
        WG5 acceptance: Cycle setup/update produces or updates only a cycle-level artifact/packet and
        names the next state, normally WEEK_PLAN. It does not start daily execution by itself.
        WG6 acceptance: Week planning is a bounded workflow task. If menu/recipe/grocery/prep artifacts
        are needed, they are produced inside this state or as writer packets, not dumped by the startup/router
        or by unrelated states.
        WG7 acceptance: Owner is never asked to fill a LOG template or fixed checklist. Raw daily
        food/photo/check-in data stays inside Health AI nutrition, not Direction OS.
        WG8 acceptance: A review cannot be only a passive summary. It must either hold explicitly or
        name the mutation/rebuild/brake target and the next graph state.
        WG9 acceptance: Mutation does not regenerate the whole nutrition system. If multiple unrelated
        changes are needed, they split into separate bounded tasks/CALLs.
        WG10 acceptance: The owner-facing surface is compact: state, why it matters, what is blocked,
        one output or one question, and one recommended next action. No scattershot multi-artifact answer.
        WG11 acceptance: No state asks "how many meals per day?", macro targets, deficit, timing,
        tracking precision, or review cadence as owner preferences. Missing owner facts create pending/
        reduced/default states where safe.
        WG12 acceptance: No workflow transition writes raw daily nutrition diary content into
        live/health/NOW.md, LOG.md, TREE.md, knowledge/, or history except as summarized RESULT evidence.
        WG13 acceptance: A future session cannot justify the rejected startup wall by pointing to active
        program/menu/grocery/fallback/LOG/review files. It must route through the workflow graph first.
        WG14 acceptance: The graph has explicit stop/block conditions. It does not silently continue
        nutrition execution through red flags or material uncertainty, and it does not make diagnoses
        or prescriptions.

        Binding WGA0-WGA15 contract + acceptance rows:
        WGA0 contract: Health AI nutrition must add a concrete workflow authority surface before execution:
        x_nutrition/workflow/graph.md as static state graph contract, x_nutrition/state/current-workflow.md
        as current-state cursor/evidence surface, and x_nutrition/procedures/workflow-router.md as
        operator-invoked router procedure.
        WGA0 acceptance: Startup reads workflow graph and current-state evidence before reading output-heavy
        nutrition artifacts. If either authority surface is missing, stale, or contradictory, startup blocks
        to repair/writer packet or Direction OS CALL and produces no nutrition execution content.

        WGA1 contract: workflow-router is the first nutrition-facing operator step. It resolves current
        workflow state from current-workflow, checks it against graph rules and current artifacts, then
        returns only current state, one bounded next task/question, whether owner input is needed, and next
        action or CALL.
        WGA1 acceptance: Startup response is mechanically rejectable if it emits more than one current state,
        more than one bounded task/question, or any menu/recipe/grocery/shopping/daily-plan/LOG/review wall
        before selected state authorizes that artifact class.

        WGA2 contract: graph.md must list each state with purpose, inputs, owner-provided irreducible facts,
        AI-decided facts, allowed output artifact class, allowed next state(s), stop/block conditions,
        and review trigger.
        WGA2 acceptance: Execution is blocked if any selected state lacks one of those fields. The graph may
        point to existing product files as seed/output families, but the graph row remains authority.

        WGA3 contract: Default transition path is STARTUP_ROUTER -> PROGRAM -> CYCLE -> WEEK_PLAN ->
        DAY_LOOP -> REVIEW -> MUTATION. MUTATION returns to DAY_LOOP, WEEK_PLAN, CYCLE, or PROGRAM by
        named mutation scope.
        WGA3 acceptance: Router can name the only allowed next states from the graph. Any jump from
        STARTUP_ROUTER directly into multiple output artifacts is a contract failure unless current state was
        already resolved to that one output-producing state.

        WGA4 contract: PROGRAM consumes core profile/phase/metrics and nutrition owner-fact/system-decision
        boundaries, then produces or updates only x_nutrition/programs/* or one writer packet for that
        program-level change.
        WGA4 acceptance: PROGRAM may define objectives, success criteria, safety constraints, assumptions,
        behavioral review triggers, and mutation policy. It must not produce menu, recipe, grocery,
        daily plan, raw LOG, or review output in the same owner-facing step.

        WGA5 contract: CYCLE consumes active program + core phase/week/day/metrics + known/pending owner
        facts, then produces or updates only x_nutrition/cycles/* or a writer packet for that cycle-level
        change.
        WGA5 acceptance: CYCLE names objective, bounded execution loop, checkpoints/triggers, tracking
        precision policy, and conditions for continuation, rebuild, or brake. It names next state, normally
        WEEK_PLAN, and does not start daily execution by itself.

        WGA6 contract: WEEK_PLAN consumes active cycle and may produce exact plan artifact families needed
        for execution: x_nutrition/menus/*, x_nutrition/recipes/*, x_nutrition/grocery/*,
        x_nutrition/fallbacks/*, and related writer packets. It is the only normal state that may authorize
        menu/recipe/grocery/prep output.
        WGA6 acceptance: WEEK_PLAN output is one bounded planning task at a time. If multiple artifacts must
        be created, router sequences them through writer packets or follow-up states rather than printing an
        unbounded owner-facing wall.

        WGA7 contract: DAY_LOOP accepts messy owner text/voice/photo updates or near-term food questions and
        writes only x_nutrition/logs/* or a writer-compatible LOG packet, plus bounded owner-facing decision
        needed now.
        WGA7 acceptance: Owner never fills LOG templates or fixed checklists. LOG confidence and materiality
        decide whether operator asks at most one clarifier. Raw daily nutrition data remains in Health AI
        nutrition only.

        WGA8 contract: REVIEW consumes Health AI nutrition LOG summaries, owner feedback, and core metrics/
        phase/biofeedback/adherence, then emits exactly one decision class: hold, mutate, rebuild, update,
        refresh, brake, or non-diagnostic medical-check language.
        WGA8 acceptance: REVIEW output either explicitly holds or names mutation/rebuild/brake target and
        next graph state. It may update x_nutrition/reviews/* and may create exactly one mutation packet if
        artifact changes are needed.

        WGA9 contract: MUTATION applies or packets one bounded change to nutrition artifacts/rules/state
        after REVIEW or material trigger. It names target artifact(s), reason, expected effect, and next
        review trigger.
        WGA9 acceptance: If several unrelated changes are needed, MUTATION splits them into separate bounded
        tasks or CALLs. Current workflow cursor records selected mutation scope and next state after write
        is accepted.

        WGA10 contract: Every nutrition chat begins by stating one resolved workflow state and returns one
        bounded output/question/action. Extra needed outputs become sequenced states, writer packets, or a
        next CALL.
        WGA10 acceptance: Owner-facing content remains compact: state, why it matters, what is blocked if
        anything, one output or question, and one recommended next action. File-heavy details belong in Health
        AI artifacts or writer packets.

        WGA11 contract: Every workflow state must distinguish irreducible owner facts from system-decided
        nutrition variables. Operator asks only material irreducible facts and decides expert variables from
        evidence, profile, phase, feedback, and review state.
        WGA11 acceptance: Missing irreducible facts produce pending/reduced/default-safe state. No state asks
        owner to choose meals/day, macro targets, deficit, timing, tracking precision, or review trigger policy
        as preferences.

        WGA12 contract: Direction OS may receive only summary, decision, problem, and next CALL. Raw food logs,
        photos, daily check-ins, and meal details stay under Health AI nutrition LOG/state.
        WGA12 acceptance: A writer packet or RESULT is invalid if it asks to copy raw daily nutrition data into
        live/health/NOW.md, LOG.md, TREE.md, knowledge/, or history, except as summarized evidence.

        WGA13 contract: Existing active program, first cycle, menu, grocery, fallback, LOG template, review
        template, and first-setup-pending.md are seeds/evidence until workflow graph selects their state.
        WGA13 acceptance: first-setup-pending.md and provider-continuation load order must be subordinated to
        workflow-router. They cannot authorize "use all generated artifacts" as startup UX until STARTUP_ROUTER
        has selected a single state and output family.

        WGA14 contract: Graph must define block routes for red flags, medical uncertainty, unsafe deterioration,
        material missing allergy/medical facts, stale or contradictory current workflow cursor, and workflow
        ambiguity.
        WGA14 acceptance: Red flags route to conservative mode or non-diagnostic medical-check language.
        Material missing facts route to one clarifier or reduced mode. Workflow ambiguity routes to repair/writer
        packet or Direction OS CALL. Normal progression does not continue silently through a block.

        WGA15 contract: Nutrition writer handoff must be extended so any workflow-affecting write validates
        WG1-WG14 in addition to W1-W13, NCA0-NCA9, and B1-B3. Packets must name resolved workflow state,
        target artifact family, source graph row(s), and boundary statement.
        WGA15 acceptance: A writer rejects packets that preserve old nutrition acceptance rows but violate
        workflow graph obligations, especially startup/router, one-chat-one-task, seed artifact authority,
        Direction OS diary boundary, or block routing.
      return: |
        RESULT with commit/PR evidence, checks run and outputs, exact files changed, whether WG1-WG14 and
        WGA0-WGA15 pass, proof that no nutrition execution content was produced, and next CALL for fresh review.
      budget: one focused implementation day

  2) live/health/LOG.md
  Append one line:
    2026-06-17 — shape approval: owner approved b-health-nutrition-workflow-authority-gate; next is Health AI executor for workflow graph authority/current cursor/router/writer validation; nutrition execution remains blocked.

  3) live/health/history/
  Add this RESULT as:
    live/health/history/2026-06-17-s-health-nutrition-workflow-shape-approval-001.md

captures: []
decisions_needed: []
play_check:
  - 1 Recite: done in prior shape brief; node is g-health-nutrition-system under g-health-root.
  - 2 Appetite first: done; 1 focused implementation day.
  - 3 Approaches, then minimal solution: done; owner approved option A after readable decision brief.
  - 4 Scope hammer: done; nutrition execution, training/activity, core rewrite, UI/runtime/DB/scheduler/services, and expert-variable questionnaire remain cut.
  - 5 Lens sweep: done; implementation gate serves AI-system/data architecture, adherence/relapse, nutrition boundary, and medical-safety block routing; other lenses not needed for this bet.
  - 6 Riskiest assumption: done; tested by executor implementation plus fresh review/refutation.
  - 7 Tasks: done; 3 executor tasks plus 1 fresh review task.
  - 8 Kill criteria: done; kill_by has date, threshold, and next_if_true/next_if_false.
  - 9 Close: done; owner approved option A with exact words: "A". RESULT activates bet and prepares next executor CALL.

log: >
  shape approval: owner approved Health AI nutrition workflow authority gate bet; next executor CALL ready;
  nutrition execution remains blocked.

next: |
  CALL c-health-nutrition-workflow-authority-executor-001
  to: executor
  direction: health
  node: g-health-nutrition-system
  task: t-1
  repo: ainazemtsau/health-ai
  kind: engineering
  goal: |
    Health AI nutrition has a file-backed workflow authority gate: workflow graph authority,
    current workflow cursor, workflow-router startup path, and writer validation enforce the
    accepted WG1-WG14 / WGA0-WGA15 contracts before any nutrition execution can start.
  context: |
    Read in Direction OS:
    - live/health/CHARTER.md
    - live/health/TREE.md
    - live/health/NOW.md
    - live/health/work/converge-g-health-nutrition-workflow-graph.md
    - live/health/work/converge-g-health-nutrition-workflow-graph-arch.md
    - live/health/work/converge-g-health-nutrition-system.md
    - live/health/work/converge-g-health-nutrition-system-arch.md
    - live/health/knowledge/health-nutrition-system-g5-review.md

    Read in product repo:
    - AGENTS.md
    - SYSTEM.md
    - x_nutrition/index.md
    - x_nutrition/procedures/operator-seams.md
    - x_nutrition/procedures/provider-continuation.md
    - x_nutrition/procedures/writer-handoff.md
    - x_nutrition/state/first-setup-pending.md
    - x_nutrition/programs/active-program.md
    - x_nutrition/cycles/first-cycle.md
    - x_nutrition/logs/YYYY-MM-DD.md
    - x_nutrition/reviews/first-cycle-review.md

    Verified closure to preserve:
    - converge-verify passed on 2026-06-17.
    - open rows: 0
    - deferred rows: 0
    - blocker rows: 0
    - WG1-WG14 WHAT rows and WGA0-WGA15 architecture contracts survived refutation.

    Product evidence before this bet:
    - Existing active program/cycle/menu/grocery/fallback/LOG/review files are seed/evidence only.
    - They cannot define accepted startup UX until workflow-router selects a bounded state.
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
    Implementation evidence:
    - Health AI nutrition startup has a file-backed workflow authority surface.
    - Current nutrition workflow state has a cursor/evidence surface.
    - Workflow-router is the first nutrition-facing operator path and returns exactly one current
      state plus one bounded next task/question/action.
    - Provider continuation/startup load order is subordinated to workflow-router before output-heavy
      active program/cycle/menu/grocery/fallback/LOG/review artifacts.
    - Writer handoff/validation rejects workflow-affecting writes that violate WG1-WG14 or WGA0-WGA15,
      even if old W1-W13/NCA0-NCA9/B1-B3 rows remain satisfied.
    - Required product checks pass, or exact failing check output is reported.
    - No nutrition execution content is produced.

    Binding WG1-WG14 and WGA0-WGA15 acceptance rows from the workflow graph WHAT/ARCH artifacts are mandatory.
    Especially preserve WGA0, WGA1, WGA2, WGA3, WGA10, WGA12, WGA13, WGA14, and WGA15.
  return: |
    RESULT with commit/PR evidence, checks run and outputs, exact files changed, whether WG1-WG14 and
    WGA0-WGA15 pass, proof that no nutrition execution content was produced, and next CALL for fresh review.
  budget: one focused implementation day
END_OF_FILE: live/health/history/2026-06-17-s-health-nutrition-workflow-shape-approval-001.md
