RESULT s-health-nutrition-shape-001 (call: c-health-nutrition-shape-001)
direction: health   play: shape   node/task: g-health-nutrition-system

outcome: |
  g-health-nutrition-system shaped as a full-functionality, 1-focused-day implementation bet:
  a chat-first Health AI nutrition system on top of g-health-core, with no nutrition feature cuts,
  broad Deep Research, personalized active nutrition program, full W1-W13/NCA0-NCA9 coverage,
  provider-independent continuation, writer handoff, and a tomorrow-start packet.

  Owner approved the revised shape in-session:
  "Ну, в принципе, согласен. Можно ожидать обновлённую эту карточку T1, T2 реально можешь объединить. С остальным согласен по твоим рекомендациям."

  Bet:
    id: b-health-nutrition-system-full-001
    node: g-health-nutrition-system
    goal: |
      Full chat-first nutrition functionality is implemented in Health AI as an additive module on top of
      g-health-core. The system has a broad evidence-backed nutrition method landscape, personalized active
      nutrition program, first executable nutrition cycle, practical menus/recipes/grocery/prep/fallback outputs,
      low-friction food tracking, nutrition review and mutation, bad-week/safety behavior, provider-independent
      continuation, writer handoff, and future app/vitrine integration seam.
    appetite: 1 focused day
    kill_by: |
      2026-06-18 12:00 Europe/Amsterdam:
      if there is not a research-backed personalized nutrition program encoded into Health AI nutrition,
      a full W1-W13/NCA0-NCA9 implementation/evidence surface, provider-independent continuation + writer
      handoff proof, and a tomorrow-start packet that lets the owner begin nutrition without another architecture
      session, stop and review/repair instead of extending.
    forecast: |
      AI executor can complete this within one focused day because the work is primarily structured text,
      conventions, evaluator evidence, and file-based module design, not human-scale manual engineering or app buildout.
    against: |
      The bet fails if implementation becomes a reduced MVP/skeleton, skips the broad research landscape,
      hardcodes a narrow diet answer, requires UI/app/runtime/server/DB/cron/scheduler/background-worker,
      rewrites g-health-core, stores raw nutrition logs in Direction OS, or lacks a writer/continuation path.
    next_if_true: |
      Review closes the implementation bet, then run the owner through the first nutrition cycle and daily logging.
    next_if_false: |
      Stop; do not extend automatically. Route to review/repair: either the research/program surface is insufficient,
      the nutrition functionality must be split, or the provider/writer continuation contract is not reliable.

  Recite:
    parent_goal: |
      g-health-root: sustainable health/weight/strength/energy system works; Health AI helps run tracking,
      recipes, food, training and continuation without polluting Direction OS with daily raw data.
    node_goal: |
      Nutrition is implemented in Health AI System as a module on g-health-core: menus, recipes, grocery/meal-prep,
      fallback food, nutrition reviews and regular research/processes work on core programs/tracking/metrics/phases
      from one source-of-truth, while specialized apps remain optional mirrors.
    node_done_when_covered_by_bet: |
      Nutrition source-of-truth, practical outputs, nutrition review, extension points, optional specialized-app seam,
      no Direction OS daily logs, body outcome support, and future continuation across providers are covered.

  Appetite calibration:
    decision: |
      Set appetite to 1 focused day, not 5 focused half-days.
    rationale: |
      Owner explicitly corrected the appetite: AI, not a human, will execute most of this as structured text,
      instructions, evaluator surface, and repo-file work; the owner also wants to prioritize this today and
      start nutrition by tomorrow.
    owner_words: |
      "наша задача – это один полудень ... это не человек пишет, это пишет ИИ ... я сегодня вот именно на эту задачу буду делать приоритет"
    final_appetite: |
      1 focused day, with kill_by on 2026-06-18 12:00 Europe/Amsterdam.

  Approaches considered:
    chosen:
      name: full-functionality research-backed chat-first module
      assumption: |
        AI can produce the full nutrition functionality as a file-based Health AI module in one focused day:
        broad research, active program, first cycle, outputs, tracking, review, persistence/writer handoff,
        and evaluator evidence, without external app/runtime infrastructure.
      why_over_others: |
        It matches owner intent: no functionality cuts, no slow human-scale appetite, and practical ability
        to start nutrition tomorrow.
      minimal_solution: |
        Not a reduced MVP. The smallest acceptable version is a complete chat-first nutrition system:
        broad evidence landscape -> personalized active nutrition program -> first cycle -> menus/recipes/grocery/
        prep/fallback -> LOG -> review/mutation -> bad-week/safety -> writer/continuation contract -> tomorrow-start packet.
      explicitly_not_included: |
        No current UI/app/vitrine/Mealie/Notion/shopping-app dependency; no server/DB/runtime/cron/scheduler/background
        worker; no raw Direction OS food diary; no training/activity module implementation; no polished content database
        of hundreds of recipes; no image sync/generation.
    rejected:
      - name: reduced MVP / skeleton-first nutrition module
        reason: |
          Rejected after owner correction. The owner wants full nutrition functionality, not a simplified skeleton.
      - name: external app/vitrine first
        reason: |
          Conflicts with signed W12 and current boundaries. Future app/vitrine remains a mirror seam only.
      - name: narrow hardcoded Deep Research
        reason: |
          Rejected after owner correction. Deep Research must discover and evaluate the method landscape, not just
          check a preselected list such as protein/calories/IF.

  Cut list:
    - cut: current Mealie/Notion/recipe-app/shopping-app/weekly-menu UI/vitrine dependency
      type: delivery-surface cut, not nutrition-functionality cut
      why_cut: |
        Signed W12 says current success cannot depend on external app/UI integration.
      parking: |
        Future integration seam under W13/NCA7.
    - cut: server, database, runtime, cron, scheduler, background-worker, autonomous recurring jobs
      type: infrastructure cut, not functionality cut
      why_cut: |
        NCA8/B2 require declarative operator-invoked procedures only.
      parking: |
        Later automation research only after file-based process works.
    - cut: full polished recipe/content database
      type: content-volume cut, not functionality cut
      why_cut: |
        Full functionality needs recipe/instruction semantics and enough first-cycle content, not hundreds of recipes.
      parking: |
        Later recipe-library/content-growth bet.
    - cut: exact macro/gram logging as default
      type: precision-default cut, not tracking cut
      why_cut: |
        W8/NCA3 require low-friction review-sufficient logs by default.
      parking: |
        Optional precision mode if later evidence/review justifies it.
    - cut: training/activity module implementation
      type: separate-module cut, not nutrition adaptability cut
      why_cut: |
        Training/activity is a separate node. Nutrition must adapt when training starts, but not implement training.
      parking: |
        Later g-health-training-activity-system shape.
    - cut: Direction OS storage of raw daily food logs/photos/check-ins
      type: boundary cut
      why_cut: |
        Violates Direction OS strategic boundary and W1/W8/NCA9.
      parking: |
        Raw data lives in Health AI nutrition only.

  Lens sweep:
    - lens: weight-nutrition
      verdict: task
      tasks: [t-1, t-2, t-4]
      reason: |
        Core functionality: research-backed nutrition strategy, active program, first cycle, menus, recipes,
        grocery/prep, fallback, tracking, review and mutation.
    - lens: strength-body-composition
      verdict: task-light
      tasks: [t-1, t-2]
      reason: |
        Nutrition program must protect muscle/strength and adapt when training starts, but training implementation
        remains out of this bet.
    - lens: activity-conditioning
      verdict: not_needed_for_implementation
      reason: |
        Activity/conditioning module is separate. Nutrition must be phase-aware and training-adaptable, not implement activity.
    - lens: adherence-relapse
      verdict: task
      tasks: [t-1, t-2, t-4]
      reason: |
        Deep Research and implementation must cover adherence, fallback/lazy meals, bad-week mode, friction, and review mutation.
    - lens: medical-safety
      verdict: task
      tasks: [t-1, t-2, t-4]
      reason: |
        Program and review must include safety boundaries, non-diagnostic medical-check language, and conservative branch.
    - lens: ai-system-data-architecture
      verdict: task
      tasks: [t-2, t-3, t-4]
      reason: |
        Nutrition must be provider-independent, file-based, namespaced on core, writer-compatible, and continuable across chats.

  Riskiest assumptions ranked:
    - rank: 1
      assumption: |
        Broad Deep Research can be converted into an actionable personalized nutrition program without hardcoding a narrow diet
        answer or leaving a dead research report.
      kill_power: high
      tested_by: t-1
    - rank: 2
      assumption: |
        Full nutrition functionality can be represented as a chat-first file-based Health AI module on g-health-core without
        external app/runtime infrastructure or core rewrite.
      kill_power: high
      tested_by: t-2
    - rank: 3
      assumption: |
        Generated menus/cycles/logs/reviews can persist reliably across ChatGPT/Claude/Codex sessions through GitHub-state and
        writer-compatible validation.
      kill_power: high
      tested_by: t-3
    - rank: 4
      assumption: |
        Owner can start tomorrow from the first cycle without needing another architecture or planning session.
      kill_power: medium-high
      tested_by: t-4
    - rank: 5
      assumption: |
        Nutrition can adapt when structured training appears later while keeping training implementation out of scope.
      kill_power: medium
      tested_by: t-1, t-2

  Tasks:
    - id: t-1
      kind: guide
      surface: ChatGPT Deep Research
      goal: |
        Run broad Deep Research and normalize it into a personalized active nutrition program for the owner.
      riskiest_assumption_test: true
      done_when: |
        - Deep Research does not assume a preselected diet or narrow hardcoded answer.
        - It first maps the current evidence landscape of nutrition strategies relevant to:
          male, 35, 182 cm, 125 kg, sustainable fat loss toward 90-95 kg, strength/muscle protection,
          energy, adherence, safety, no structured training initially, structured training likely later.
        - It considers method families broadly, including but not limited to:
          daily deficit, weekly calorie budgeting, calorie cycling, diet breaks, refeeds, time-restricted eating/
          intermittent fasting, meal frequency, meal timing, nutrition around future training, high-protein strategies,
          high-satiety/high-volume eating, Mediterranean-style/whole-food patterns, low-carb/moderate-carb patterns,
          meal replacements, flexible dieting, tracking precision strategies, fallback/lazy-food systems,
          bad-week strategy, and maintenance transition.
        - For each relevant method family, it records:
          evidence strength, uncertainty, when it works, when it fails, risks/contraindications, adherence cost,
          relevance to owner profile, use_now / later_option / reject, and signals that would change the decision.
        - It synthesizes:
          evidence-backed research brief, method landscape/reference, personalized active nutrition program,
          initial no-training phase rules, adaptation rules when training starts, system-decided expert variables,
          genuinely askable owner facts, first-cycle design rules, tracking/review framework, safety boundaries,
          research refresh triggers, and implementation handoff for Health AI nutrition.
        - It does not ask expert variables as owner preferences; it asks only irreducible owner facts where necessary
          and marks missing facts pending/default/reduced-mode where safe.
      evidence_expected: |
        Research brief with source citations, method landscape/reference, personalized program spec, decision framework,
        uncertainty notes, refresh triggers, and implementation handoff artifact suitable for t-2.
      boundaries: |
        Do not prescribe medically or diagnose.
        Do not assume an app/UI/Mealie/Notion dependency.
        Do not make owner choose expert variables such as meals/day, deficit, protein, timing, tracking precision,
        IF/TRE, calorie cycling, or diet breaks as setup preferences.
        Do not produce only a generic menu.

    - id: t-2
      kind: executor
      repo: ainazemtsau/health-ai
      goal: |
        Implement the full chat-first Health AI nutrition system as an additive module on g-health-core,
        using the t-1 research/program output.
      done_when: |
        - Health AI nutrition contains the full functional surface:
          evidence/reference layer, method landscape, active personalized nutrition program, decision framework,
          owner facts known/pending/defaults, initial no-training phase rules, adaptation rules for when training starts,
          first nutrition cycle, menu/eating plan, substitutions/swaps, executable recipes/instructions,
          grocery needs, meal-prep/base-prep/reuse, fallback/lazy meals, low-friction food LOG shape,
          nutrition review procedure, artifact mutation decisions, bad-week mode, safety behavior,
          regular operator-invoked procedure seams, and future integration seam.
        - The implementation preserves signed WHAT W1-W13 acceptance:
          W1 source-of-truth, W2 core attach, W3 expert-variable boundary, W4 personalized first process,
          W5 practical outputs, W6 detailed recipes/instructions, W7 base-prep/reuse correctness,
          W8 nutrition tracking, W9 tracking-to-review mutation, W10 bad-week mode, W11 safety boundary,
          W12 no current vitrine/app requirement, W13 future integration seam.
        - The implementation preserves corrected NCA0-NCA9:
          NCA0 starter owner-fact seed only; NCA1 additive nutrition namespace; NCA2 personalized cycle derivation;
          NCA3 low-friction nutrition LOG; NCA4 LOG-to-review mutation; NCA5 recipes/base-prep/grocery correctness;
          NCA6 bad-week/safety; NCA7 future integration seam; NCA8 operator-invoked procedure extension points;
          NCA9 day_type provenance/cross-module coupling/Direction OS visibility.
        - Corrected blockers B1-B3 are preserved:
          B1 file-backed core review binding, B2 no scheduler/runtime/cron/background jobs, B3 core day_type provenance only.
        - Nutrition consumes core-owned profile/phase/week/day/weight_trend/adherence/biofeedback/parse/materiality/
          procedure/schema/versioning surfaces and writes only nutrition-namespaced fields/artifacts.
        - No g-health-core concept definitions are rewritten.
        - No UI/app/vitrine/Mealie/Notion/shopping-app/runtime/DB/server/cron/scheduler/background-worker is introduced.
        - Direction OS does not store raw daily food/weight/photo/check-in logs.
      evidence_expected: |
        Commit/PR, file list, evidence summary, evaluator/check output mapping implementation to W1-W13/NCA0-NCA9/B1-B3,
        and first-cycle artifacts showing owner can begin nutrition.

    - id: t-3
      kind: executor
      repo: ainazemtsau/health-ai
      goal: |
        Add provider-independent continuation and writer handoff for nutrition so new ChatGPT/Claude/Codex sessions
        can resume from GitHub-state and durable changes pass writer validation.
      done_when: |
        - AGENTS.md is the canonical agent contract for Health AI nutrition operation and persistence.
        - CLAUDE.md points to AGENTS.md and does not fork conflicting rules.
        - A portable SYSTEM/project prompt or equivalent convention explains how non-code chat sessions resume from repo state.
        - Roles are explicit:
          operator session proposes changes; writer applies exact changes, validates and can reject; executor performs repo work;
          reviewer/refuter checks evidence.
        - Every generated nutrition program/menu/cycle/log/review mutation can be represented as file changes in the Health AI
          nutrition namespace.
        - Writer-compatible packets/patches include active program/cycle references, exact files to change, rationale,
          and checks to run.
        - Writer validates:
          schema/frontmatter, nutrition namespace, PLAN-vs-LOG boundary, active program/cycle continuity,
          W1-W13/NCA0-NCA9/B1-B3, no core rewrite, no forbidden infrastructure, and no Direction OS raw diary.
        - Invalid write attempts are rejected with reasons, including examples for:
          expert variable asked as owner preference; raw Direction OS food log; core rewrite; scheduler/cron/background job.
        - Fresh-chat dry-run passes:
          with no conversational memory, an agent reads repo instructions/state, identifies the active nutrition program,
          creates a next menu or next step, and emits writer-compatible changes or applies them if acting as writer.
      evidence_expected: |
        Commit/PR; AGENTS/CLAUDE/SYSTEM or equivalent carrier changes; writer handoff examples; rejection examples;
        fresh-chat continuation dry-run evidence.

    - id: t-4
      kind: session
      play: review
      goal: |
        Refute or verify the full nutrition system against the shaped bet, then produce the tomorrow-start packet.
      done_when: |
        - A separate review/refutation session checks t-1 through t-3 evidence.
        - Verdict reports pass/fail for:
          broad Deep Research quality, personalized active nutrition program, full W1-W13 functionality,
          NCA0-NCA9 constraints, B1-B3 corrected blockers, no functionality cuts, no core rewrite,
          no forbidden app/runtime/server/DB/cron/scheduler/background-worker, no raw Direction OS nutrition diary,
          and provider-independent continuation + writer handoff.
        - If blocker_gaps=0, the review produces a tomorrow-start packet for the owner:
          what to eat tomorrow, what to buy/prep, fallback if no time/energy, how to log food,
          what to write to AI in the evening, and when/how first nutrition review happens.
        - If any blocker remains, the bet stops for review/repair rather than extending appetite.
      evidence_expected: |
        RESULT from review session with refutation evidence, pass/fail verdict, blocker_gaps,
        tomorrow-start packet if passed, state_changes, and next CALL.

  Acceptance/evaluator surface copied from signed nutrition WHAT:
    - W1 Nutrition source-of-truth:
        acceptance: |
          Future executor can point to the Health AI nutrition layer and show where current nutrition decisions,
          outputs, logs, and review mutations live. Direction OS does not store raw daily nutrition data.
    - W2 Nutrition attaches to core:
        acceptance: |
          Nutrition writes only nutrition-namespaced artifacts/fields and uses core phase/week/day/weight_trend/
          adherence/biofeedback instead of duplicating them.
    - W3 Expert-variable vs owner-fact boundary:
        acceptance: |
          Initial intake has no mandatory expert-variable questions. Missing owner facts do not block:
          they remain pending/reduced-mode or receive documented revisable defaults where safe.
    - W4 Personalized first nutrition process:
        acceptance: |
          First cycle includes setup, eating structure, outputs, tracking instructions, feedback path,
          and first review loop; it explains which owner facts and system decisions shaped it.
        shaped_expectation: |
          Implementation must include an evidence-backed active nutrition program, not just a menu-cycle.
    - W5 Practical outputs:
        acceptance: |
          Owner can ask in chat what to eat/cook/buy/replace and receive executable outputs derived from
          current nutrition artifacts.
    - W6 Detailed recipes/instructions:
        acceptance: |
          Recipe/instruction cannot be vague prose. It must be sufficient for actual cooking/prep and later
          derivation of grocery/prep needs.
    - W7 Base-prep / reuse correctness:
        acceptance: |
          Shared prepared component can be used by multiple meals without double-counting or omitting prep/grocery
          needs at the process level.
    - W8 Nutrition tracking:
        acceptance: |
          Owner can report a day/meals roughly; the system creates a usable nutrition LOG, marks confidence,
          asks only materially necessary clarifying questions, proceeds with safe/default estimates on non-answer,
          and does not require gram-level logging by default.
    - W9 Tracking-to-review mutation:
        acceptance: |
          If logs show hunger, prep friction, frequent fallback, off-plan pattern, disliked foods, poor adherence,
          or safety/body-outcome problems, review emits a concrete mutation/hold/rebuild/refresh/brake decision.
    - W10 Bad-week mode:
        acceptance: |
          There is a defined way to keep eating inside a reduced nutrition process during low time/stress/absence.
    - W11 Safety boundary:
        acceptance: |
          Nutrition cannot silently continue aggressive deficit or unsafe progression when safety flags appear.
    - W12 No current vitrine/app requirement:
        acceptance: |
          Executor/shape may not make success depend on Mealie/UI/app integration for this nutrition process.
    - W13 Future integration seam:
        acceptance: |
          Current implementation remains chat-first and Health-AI-canonical, but does not block later external
          mirror work.

  Implementation constraints copied from corrected NCA0-NCA9:
    - NCA0 Starter-kit seed intake:
        constraint: |
          Nutrition may collect only irreducible nutrition owner facts. Expert variables remain system-decided.
          Missing owner facts stay pending, reduced-mode, or documented revisable defaults where safe.
        rejects: |
          Mandatory "how many meals per day do you want"; fabricated owner facts; blocking first cycle on non-material gaps.
    - NCA1 Core attach / nutrition namespace:
        constraint: |
          Nutrition attaches as one Health AI domain/module over g-health-core, reads core-owned shared concepts,
          and writes only nutrition-namespaced artifacts/fields such as x_nutrition_*.
        rejects: |
          Standalone nutrition system redefining profile, phase, metrics, review, logs, or core procedures.
    - NCA2 Personalized nutrition cycle derivation:
        constraint: |
          Active nutrition cycle resolves owner facts + core profile/phase/metrics + system-decided variables
          into menu-cycle/eating-plan, recipes/instructions, base-prep, grocery needs, fallback meals,
          tracking instructions, and review cadence.
        shaped_expectation: |
          Active cycle is derived from a research-backed active nutrition program and method decision framework.
        rejects: |
          Static diet forever; buffet of options owner must manually choose; generic first menu without setup/run/review loop.
    - NCA3 Nutrition LOG / low-friction tracking:
        constraint: |
          Nutrition tracking lives in Health AI nutrition namespace as review-sufficient LOG entries with planned-vs-actual,
          substitutions, fallback, skipped/off-plan events, rough portions, uncertainty/confidence, hunger/satiety,
          friction, and materially necessary estimates.
        rejects: |
          Direction OS food diary; mandatory precise macro logging; tracking hidden inside review summary.
    - NCA4 LOG-to-review mutation path:
        constraint: |
          Nutrition review consumes nutrition LOGs + owner feedback + core metrics/phase/biofeedback/adherence and emits
          explicit hold/mutate/rebuild/update/refresh/brake decisions.
        rejects: |
          Passive summary; raw daily diary export to Direction OS; unreviewed drift.
    - NCA5 Recipes, base-prep/reuse, grocery correctness:
        constraint: |
          Recipes/instructions are executable process blocks with ingredients, quantities or approximations,
          substitutions, equipment, time/friction notes, base-prep components, yields, reuse links,
          grocery derivation, and relation to menu/fallback/prep.
        rejects: |
          Vague prose-only recipe; isolated recipes when prep is shared; external recipe/shopping app as current authority.
    - NCA6 Bad-week mode and safety interaction:
        constraint: |
          Nutrition has reduced bad-week mode with valid fallback/lazy-food minimums and relaxed-but-nonzero tracking.
          Safety flags halt progression or switch conservative with non-diagnostic medical-check language.
        rejects: |
          Bad week as total failure; cheat/free-for-all fallback; medical diagnosis/prescription.
    - NCA7 Future integration seam:
        constraint: |
          Nutrition artifacts are structured enough to be mirrored later by app/recipe/shopping/image surfaces,
          but Health AI nutrition remains canonical now and no external UI/app is required.
        rejects: |
          Chat-only dead end; current app/vitrine dependency.
    - NCA8 Regular nutrition procedure extension points:
        constraint: |
          Recurring/bounded nutrition procedures, if needed, are nutrition-namespaced declarative procedure specs
          conforming to core procedure template and run only when invoked by an operator.
        rejects: |
          Scheduler/runtime requirement; autonomous recurring jobs; rewriting core procedure template.
    - NCA9 day_type provenance, cross-module coupling, Direction OS visibility:
        constraint: |
          Core provides only day_type provenance. Core does not own nutrition targets. Nutrition owns any future
          x_nutrition_day_type/x_nutrition_target if needed, derives through core surfaces, and Direction OS
          does not store raw nutrition logs.
        rejects: |
          Core-owned nutrition target; direct nutrition-training private coupling outside core; Direction OS food-log store.

  Corrected blockers preserved:
    - B1: |
        Core review binding must be file-backed by knowledge/history/product evidence, not CALL-only import.
    - B2: |
        Regular nutrition procedure extension points are core procedure template plus nutrition-namespaced
        operator-invoked procedure seam, with no scheduler/runtime/cron/background job.
    - B3: |
        Core day_type is provenance only; nutrition owns any later namespaced x_nutrition_day_type/x_nutrition_target.

evidence: |
  Source files read and used:
  - os/KERNEL.md:
    session/result protocol, no direct state writes, RESULT/state_changes writer handoff, G1-G10 gates.
  - os/plays/shape.md:
    shape steps, appetite, approaches, cut list, lens sweep, riskiest assumption, task sizing, kill_by, approval close.
  - os/schema/packets.md:
    CALL/RESULT schema and executor/writer expectations.
  - live/health/CHARTER.md:
    mission, Health AI boundary, product repo, lenses, guarded risk posture, no Direction OS daily diary,
    provider-independent architecture constraint.
  - live/health/TREE.md:
    parent g-health-root and node g-health-nutrition-system goal/done_when.
  - live/health/NOW.md:
    active_bet none, tasks empty, resolved owner signoffs for nutrition Define and WHAT.
  - live/health/work/converge-g-health-nutrition-system.md:
    signed nutrition WHAT W1-W13; owner signoff "A"; dirty inputs rejected; corrected contract index.
  - live/health/work/converge-g-health-nutrition-system-arch.md:
    corrected NCA0-NCA9; B1-B3 closure; open/deferred/blocker rows 0; no forbidden runtime/app requirements.
  - live/health/knowledge/health-core-corrected-g5-review.md:
    g-health-core corrected G5 met; zero blocker gaps across WA1-WA12 + W69/W70/W72/W73/W74 + CA1-CA9.
  - health-ai acceptance/core/evidence-summary.md:
    core checks PASS; blocker gaps 0; module attach additive-only; day_type provenance; no module/runtime dirs.
  - health-ai acceptance/core/matrix.json:
    acceptance/contract matrix with blocker_gaps=[] and core WA/CA target mappings.
  - health-ai core/extensions/attach-contract.md:
    modules read phase/week/day/weight_trend/adherence/biofeedback and write only x_<domain>_* fields.
  - health-ai core/procedures/template-contract.md:
    procedures are declarative and never self-schedule; operator-invoked only.
  - health-ai core/provenance/day-type.md:
    day_type is provenance only; no nutrition target implemented in core.
  - health-ai core/review.md:
    review reads PLAN/LOG/shared metrics/anchors/safety/cadence and outputs proposals/applied changes;
    it does not silently mutate raw facts or override red-flag halts.

  Owner approval evidence:
  - Owner corrected appetite and no-feature-cut interpretation across the approval discussion.
  - Owner approved final revised recommendations:
    "Ну, в принципе, согласен. Можно ожидать обновлённую эту карточку T1, T2 реально можешь объединить. С остальным согласен по твоим рекомендациям."

  Gate notes:
  - G1 passes in current state: NOW active_bet is none and tasks are empty.
  - G3 passes: appetite fixed before final task surface as 1 focused day.
  - G4 passes: done_when and kill_by are explicit.
  - G6 passes: cut list has real cuts, lens sweep has verdict per lens, and t-1 tests the top riskiest assumption.
  - G9 passes: owner approved the revised bet/task surface in-session with quoted words.
  - No product repo code was implemented by this session.

state_changes: |
  Apply the following exact Direction OS state changes.

  1) TREE.md

  In live/health/TREE.md, update node g-health-nutrition-system:

    status: active
    appetite: 1 focused day
    kill_by: >
      2026-06-18 12:00 Europe/Amsterdam: if there is not a research-backed personalized
      nutrition program encoded into Health AI nutrition, a full W1-W13/NCA0-NCA9 implementation/
      evidence surface, provider-independent continuation + writer handoff proof, and a tomorrow-start
      packet that lets the owner begin nutrition without another architecture session, stop and review/
      repair instead of extending.

  Do not change the node goal, why, or done_when text.

  2) NOW.md

  Replace current active_bet/status-none, tasks: [], and next with:

  active_bet:
    id: b-health-nutrition-system-full-001
    node: g-health-nutrition-system
    status: active
    appetite: 1 focused day
    started_from_call: c-health-nutrition-shape-001
    owner_approved: >
      Ну, в принципе, согласен. Можно ожидать обновлённую эту карточку T1, T2 реально можешь
      объединить. С остальным согласен по твоим рекомендациям.
    goal: >
      Full chat-first nutrition functionality is implemented in Health AI as an additive module on top of
      g-health-core: broad evidence-backed method landscape, personalized active nutrition program,
      first executable cycle, menus/recipes/grocery/prep/fallback outputs, low-friction food tracking,
      nutrition review/mutation, bad-week/safety behavior, provider-independent continuation, writer handoff,
      and future app/vitrine integration seam.
    kill_by: >
      2026-06-18 12:00 Europe/Amsterdam: if there is not a research-backed personalized nutrition program
      encoded into Health AI nutrition, a full W1-W13/NCA0-NCA9 implementation/evidence surface,
      provider-independent continuation + writer handoff proof, and a tomorrow-start packet that lets the
      owner begin nutrition without another architecture session, stop and review/repair instead of extending.
    forecast: >
      AI executor can complete this within one focused day because the work is primarily structured text,
      conventions, evaluator evidence, and file-based module design, not a human-scale app buildout.
    against: >
      The bet fails if implementation becomes a reduced MVP/skeleton, skips the broad research landscape,
      hardcodes a narrow diet answer, requires UI/app/runtime/server/DB/cron/scheduler/background-worker,
      rewrites g-health-core, stores raw nutrition logs in Direction OS, or lacks writer/continuation path.
    cut_list:
      - current Mealie/Notion/recipe-app/shopping-app/weekly-menu UI/vitrine dependency
      - server, database, runtime, cron, scheduler, background-worker, autonomous recurring jobs
      - full polished recipe/content database
      - exact macro/gram logging as default
      - training/activity module implementation
      - Direction OS storage of raw daily food logs/photos/check-ins
    lens_sweep:
      weight-nutrition: task via t-1/t-2/t-4
      strength-body-composition: task-light via t-1/t-2; nutrition adapts when training starts, but training implementation is out
      activity-conditioning: not_needed_for_implementation; later training/activity module
      adherence-relapse: task via t-1/t-2/t-4
      medical-safety: task via t-1/t-2/t-4
      ai-system-data-architecture: task via t-2/t-3/t-4
    riskiest_assumption: >
      Broad Deep Research can be converted into an actionable personalized nutrition program without hardcoding
      a narrow diet answer or leaving a dead research report.
    acceptance_evaluator_surface:
      what_rows: W1-W13 copied from signed nutrition WHAT in work/converge-g-health-nutrition-system.md
      contract_rows: NCA0-NCA9 copied from corrected architecture in work/converge-g-health-nutrition-system-arch.md
      corrected_blockers: B1-B3 preserved
      provider_continuation: >
        Nutrition outputs must persist in GitHub-state and resume across ChatGPT/Claude/Claude Code/Codex
        through AGENTS/CLAUDE/SYSTEM-style conventions and writer-compatible validation.

  tasks:
    - id: t-1
      kind: guide
      surface: ChatGPT Deep Research
      status: active
      goal: >
        Run broad Deep Research and normalize it into a personalized active nutrition program for the owner.
      done_when: >
        Deep Research maps the current evidence landscape without assuming a preselected diet; compares relevant
        method families; synthesizes evidence brief, method reference, personalized active program, no-training
        initial phase, training-start adaptation rules, system-decided expert variables, askable owner facts,
        first-cycle design rules, tracking/review framework, safety boundaries, refresh triggers, and implementation
        handoff for Health AI nutrition.
      evidence_expected: >
        Research brief with source citations, method landscape/reference, personalized program spec, decision framework,
        uncertainty notes, refresh triggers, and implementation handoff artifact suitable for t-2.
    - id: t-2
      kind: executor
      repo: ainazemtsau/health-ai
      status: queued
      goal: >
        Implement the full chat-first Health AI nutrition system as an additive module on g-health-core,
        using the t-1 research/program output.
      done_when: >
        Health AI nutrition contains the full functional surface: evidence/reference layer, method landscape,
        active personalized program, decision framework, owner facts known/pending/defaults, phase rules,
        first cycle, menu/eating plan, substitutions/swaps, executable recipes/instructions, grocery/prep/base-prep,
        fallback/lazy meals, food LOG shape, review procedure, mutation decisions, bad-week mode, safety behavior,
        operator-invoked procedure seams, future integration seam; passes W1-W13/NCA0-NCA9/B1-B3 with no core rewrite,
        no forbidden infrastructure, and no raw Direction OS nutrition diary.
      evidence_expected: >
        Commit/PR, file list, evidence summary, evaluator/check output mapping implementation to W1-W13/NCA0-NCA9/B1-B3,
        and first-cycle artifacts showing owner can begin nutrition.
    - id: t-3
      kind: executor
      repo: ainazemtsau/health-ai
      status: queued
      goal: >
        Add provider-independent continuation and writer handoff for nutrition so new ChatGPT/Claude/Codex sessions
        can resume from GitHub-state and durable changes pass writer validation.
      done_when: >
        AGENTS.md is canonical; CLAUDE.md points to AGENTS.md without conflicting fork; portable SYSTEM/project prompt
        or equivalent convention explains non-code chat operation; operator/writer/executor/reviewer roles are explicit;
        generated program/menu/cycle/log/review changes can be represented as file changes; writer-compatible packets/
        patches include exact files, rationale, active program/cycle references, and checks; writer validates schema,
        namespace, PLAN-vs-LOG, continuity, W1-W13/NCA0-NCA9/B1-B3, no core rewrite, no forbidden infrastructure,
        no Direction OS raw diary; bad write attempts are rejected with examples; fresh-chat continuation dry-run passes.
      evidence_expected: >
        Commit/PR; AGENTS/CLAUDE/SYSTEM or equivalent carrier changes; writer handoff examples; rejection examples;
        fresh-chat continuation dry-run evidence.
    - id: t-4
      kind: session
      play: review
      status: queued
      goal: >
        Refute or verify the full nutrition system against the shaped bet, then produce the tomorrow-start packet.
      done_when: >
        Separate review checks t-1 through t-3 evidence; reports pass/fail for broad Deep Research quality,
        personalized active nutrition program, full W1-W13 functionality, NCA0-NCA9, B1-B3, no functionality cuts,
        no core rewrite, no forbidden app/runtime/server/DB/cron/scheduler/background-worker, no raw Direction OS diary,
        and provider-independent continuation + writer handoff; if blocker_gaps=0, produces tomorrow-start packet with
        what to eat tomorrow, what to buy/prep, fallback, how to log, what to write AI in the evening, and when/how first
        nutrition review happens.
      evidence_expected: >
        RESULT from review session with refutation evidence, pass/fail verdict, blocker_gaps, tomorrow-start packet
        if passed, state_changes, and next CALL.

  next: |
    CALL c-health-nutrition-t1-deep-research-program-001
    to: session
    direction: health
    play: guide
    node: g-health-nutrition-system  task: t-1
    goal: |
      Produce and run/prepare the broad ChatGPT Deep Research work needed to create an evidence-backed,
      personalized active nutrition program for the owner.
    context: |
      Read:
      - live/health/CHARTER.md
      - live/health/TREE.md
      - live/health/NOW.md
      - live/health/work/converge-g-health-nutrition-system.md
      - live/health/work/converge-g-health-nutrition-system-arch.md
      - live/health/knowledge/health-core-corrected-g5-review.md
      - health-ai acceptance/core/evidence-summary.md
      - health-ai core/extensions/attach-contract.md
      - health-ai core/procedures/template-contract.md
      - health-ai core/provenance/day-type.md

      Owner profile known from charter:
      male, 35, 182 cm, 125 kg, BMI about 37.7; goal is sustainable weight loss toward 90-95 kg,
      strength/muscle/energy protection, long-term adherence and maintenance. Owner has sport/diet experience,
      cooking infrastructure, scale, willingness to use AI tracking; no stated restrictions yet.

      Shape requirements:
      - No nutrition feature cuts.
      - Use broad Deep Research, not a hardcoded narrow diet prompt.
      - Do not assume a preselected diet.
      - Produce research brief + method landscape/reference + personalized active nutrition program +
        implementation handoff for Health AI nutrition.
      - Program must support no structured training initially and adaptation when training starts later.
      - Expert variables are system-decided; ask only irreducible owner facts.
      - Output must be suitable for t-2 implementation as Health AI nutrition module on g-health-core.
    boundaries: |
      Do not implement product repo code.
      Do not create a generic menu-only answer.
      Do not ask owner to choose expert variables such as meals/day, deficit, protein, timing,
      tracking precision, intermittent fasting, calorie cycling, diet breaks, or refeeds.
      Do not prescribe medically or diagnose.
      Do not add UI/app/vitrine/Mealie/Notion/runtime/DB/server/cron/scheduler/background-worker requirements.
      Do not store raw daily nutrition logs in Direction OS.
    done_when: |
      - A self-contained Deep Research prompt/work packet exists and is broad enough to discover the relevant
        method landscape rather than confirm a preselected approach.
      - Deep Research output or ready-to-run packet covers:
        evidence landscape, method comparison, applicability to owner, use_now/later_option/reject decisions,
        personalized active nutrition program, no-training initial phase, training-start adaptation rules,
        system-decided expert variables, askable owner facts, first-cycle design rules, tracking/review framework,
        safety boundaries, refresh triggers, and Health AI implementation handoff.
      - If actual Deep Research cannot be run inside this session/surface, return the exact ready-to-run Deep Research
        prompt plus expected output schema and next CALL for implementation after owner supplies the report.
    return: |
      RESULT with Deep Research prompt/report, normalized program spec, method landscape, implementation handoff,
      state_changes, and next CALL.
    budget: one tight guide/research movement
    surface: ChatGPT Deep Research

  3) LOG.md

  Append one line:
  2026-06-17 — shape g-health-nutrition-system: approved 1-focused-day full-functionality nutrition bet with Deep Research, Health AI module implementation, provider-independent writer handoff, and tomorrow-start review packet.

captures:
  - Future mirror: external app/vitrine/Mealie/recipe/shopping/image surface may be shaped later under W13/NCA7 after Health AI canonical nutrition works.
  - Future content-growth bet: expand recipe/fallback library after minimal full-functionality semantics and review loop pass.
  - Future automation research: operator-invoked procedures can later be evaluated for automation, but scheduler/runtime is explicitly out for this bet.
  - Alternative rejected: reduced MVP/skeleton-first nutrition module; owner explicitly wants no nutrition functionality cuts.
  - Alternative rejected: narrow hardcoded Deep Research prompt; owner wants broad expert evidence landscape and method evaluation.

decisions_needed: []

play_check:
  - 1 Recite: done
  - 2 Appetite first: done; owner corrected appetite to AI-scale 1 focused day and approved final revised appetite
  - 3 Approaches, then minimal solution: done; chose full-functionality research-backed chat-first module; rejected reduced MVP and external-app-first approaches
  - 4 Scope hammer: done; real cuts recorded as delivery/infrastructure/content-volume cuts, not nutrition functionality cuts
  - 5 Lens sweep: done; verdict per CHARTER lens recorded
  - 6 Riskiest assumption: done; ranked assumptions and t-1 tests the top research-to-program assumption
  - 7 Tasks: done; 4 tasks, each ≤ half-day in AI-executed mode; t-1/t-2 research design/run combined per owner instruction
  - 8 Kill criteria: done; kill_by set to 2026-06-18 12:00 Europe/Amsterdam with next_if_true/next_if_false
  - 9 Close: done; owner approved revised bet/task surface: "Ну, в принципе, согласен. Можно ожидать обновлённую эту карточку T1, T2 реально можешь объединить. С остальным согласен по твоим рекомендациям."

log: |
  shape g-health-nutrition-system: owner approved 1-focused-day full-functionality nutrition bet with broad Deep Research,
  Health AI module implementation, provider-independent writer handoff, and tomorrow-start review packet.

next: |
  CALL c-health-nutrition-t1-deep-research-program-001
  to: session
  direction: health
  play: guide
  node: g-health-nutrition-system  task: t-1
  goal: |
    Produce and run/prepare the broad ChatGPT Deep Research work needed to create an evidence-backed,
    personalized active nutrition program for the owner.
  context: |
    Read:
    - live/health/CHARTER.md
    - live/health/TREE.md
    - live/health/NOW.md
    - live/health/work/converge-g-health-nutrition-system.md
    - live/health/work/converge-g-health-nutrition-system-arch.md
    - live/health/knowledge/health-core-corrected-g5-review.md
    - health-ai acceptance/core/evidence-summary.md
    - health-ai core/extensions/attach-contract.md
    - health-ai core/procedures/template-contract.md
    - health-ai core/provenance/day-type.md

    Owner profile known from charter:
    male, 35, 182 cm, 125 kg, BMI about 37.7; goal is sustainable weight loss toward 90-95 kg,
    strength/muscle/energy protection, long-term adherence and maintenance. Owner has sport/diet experience,
    cooking infrastructure, scale, willingness to use AI tracking; no stated restrictions yet.

    Shape requirements:
    - No nutrition feature cuts.
    - Use broad Deep Research, not a hardcoded narrow diet prompt.
    - Do not assume a preselected diet.
    - Produce research brief + method landscape/reference + personalized active nutrition program +
      implementation handoff for Health AI nutrition.
    - Program must support no structured training initially and adaptation when training starts later.
    - Expert variables are system-decided; ask only irreducible owner facts.
    - Output must be suitable for t-2 implementation as Health AI nutrition module on g-health-core.
  boundaries: |
    Do not implement product repo code.
    Do not create a generic menu-only answer.
    Do not ask owner to choose expert variables such as meals/day, deficit, protein, timing,
    tracking precision, intermittent fasting, calorie cycling, diet breaks, or refeeds.
    Do not prescribe medically or diagnose.
    Do not add UI/app/vitrine/Mealie/Notion/runtime/DB/server/cron/scheduler/background-worker requirements.
    Do not store raw daily nutrition logs in Direction OS.
  done_when: |
    - A self-contained Deep Research prompt/work packet exists and is broad enough to discover the relevant
      method landscape rather than confirm a preselected approach.
    - Deep Research output or ready-to-run packet covers:
      evidence landscape, method comparison, applicability to owner, use_now/later_option/reject decisions,
      personalized active nutrition program, no-training initial phase, training-start adaptation rules,
      system-decided expert variables, askable owner facts, first-cycle design rules, tracking/review framework,
      safety boundaries, refresh triggers, and Health AI implementation handoff.
    - If actual Deep Research cannot be run inside this session/surface, return the exact ready-to-run Deep Research
      prompt plus expected output schema and next CALL for implementation after owner supplies the report.
  return: |
    RESULT with Deep Research prompt/report, normalized program spec, method landscape, implementation handoff,
    state_changes, and next CALL.
  budget: one tight guide/research movement
  surface: ChatGPT Deep Research

END_OF_FILE: live/health/history/2026-06-17-s-health-nutrition-shape-001.md
