RESULT s-health-nutrition-converge-001 (call: c-health-nutrition-converge-001)
direction: health   play: converge   node/task: g-health-nutrition-system

outcome: |
  g-health-nutrition-system now has an owner-signed WHAT spec for a nutrition module on g-health-core.
  The spec rejects nutrition v1, dirty converge input, paused Define draft, Mealie/vitrine work, and prior
  architecture candidates as authority. It re-derives the nutrition requirements as a personalized process
  on core: expert-variable vs owner-fact boundary, nutrition source-of-truth, practical outputs, detailed
  recipe/instruction process, base-prep/reuse correctness, mandatory nutrition tracking, review mutation,
  bad-week mode, safety boundary, and future integration seam.

  It does NOT require a vitrine, Mealie, recipe app, weekly-menu UI, shopping-list integration, recipe-image
  generation, runtime, DB, server, cron, scheduler, product implementation, or training/activity module.

  Route: heavy node -> converge-arch, because the signed WHAT still has architecture-contract questions:
  artifact authority/derivation, tracking LOG shape, review mutation path, base-prep/reuse semantics,
  future external mirror seam, and nutrition-on-core attach boundary.

evidence: |
  Owner signoffs in this session:
  - Define signoff:
    Owner said: "A — да, подписываем"
    Meaning signed: nutrition inherits the core boundary — expert variables are system-decided; only
    irreducible owner facts are askable; questions are non-blocking.
  - WHAT/vitrine cut:
    Owner said: "все витрины, всё это будем обсуждать после того, как построим хороший процесс по питанию
    и по тренировкам потом... всё убираем витрины, то есть это не является требованием... просто...
    процесс был так построен, чтобы... можно было потом их подключить."
    Meaning signed: vitrine/Mealie/UI are not current requirements; only a future integration seam remains.
  - WHAT/tracking correction:
    Owner said: "не то, что быстро начать правильное питание... быстро стартануть процесс... не generic...
    засетапить нормально... Кстати... про трекинг... это охренеть какая важная часть..."
    Meaning signed: replace "quick correct eating" with a personalized, fully set up nutrition process;
    nutrition tracking is mandatory.
  - Final WHAT signoff:
    Owner said: "A"
    Meaning signed: revised WHAT with personalized process + mandatory tracking + no current vitrine requirement.

  Input evidence read/used:
  - live/health/CHARTER.md:
    Health AI System must keep Direction OS strategic, not a raw diary; nutrition must support weight,
    satiety, protein, repeatability, bad weeks, and safety.
  - live/health/TREE.md:
    g-health-nutrition-system done_when requires nutrition source-of-truth; practical outputs
    (menu, swaps, shopping needs, recipes, lazy food, prep plan, feedback corrections);
    nutrition review; extension points; no raw daily food logs in Direction OS; body outcome support.
  - live/health/NOW.md:
    active core bet context says nutrition module was cut from core and should attach later.
  - live/health/history/2026-06-13-s-health-nutrition-reset-001.md:
    v1 failed because it asked "сколько приёмов пищи в день" as an expert question; all v1 inputs
    became dirty evidence only.
  - live/health/history/2026-06-14-s-health-reframe-map-001.md:
    owner-approved core-first re-map: nutrition is a module attached to g-health-core.
  - live/health/work/converge-health-nutrition-input.md:
    dirty first-pass inventory only; used to refute/re-derive, not imported as authority.
  - live/health/work/converge-nutrition-define-draft.md:
    paused, never owner-signed Define draft; used as input evidence only, not authority.
  - live/health/work/converge-g-health-core.md and health-ai core evidence:
    core owns profile boundary, shared metrics/phase, PLAN-vs-LOG, parser/materiality,
    non-blocking questions, module attach contract, and external-read/Direction OS boundary.

state_changes: |
  work/: add file live/health/work/converge-g-health-nutrition-system.md with this exact content:

  ---
  # Converge — g-health-nutrition-system

  > Produced by converge session s-health-nutrition-converge-001 on 2026-06-16.
  > Assembly surface only; not a state file.
  > Authority: owner signoffs in this session + RESULT history.
  > Status: CLOSED WHAT, route to converge-arch.

  ## §TRIAGE

  triage: **heavy** — converge **ON** — because:
  - model-bearing: v1 failed structurally by asking an expert nutrition variable ("meals/day")
    as owner preference;
  - cross-cutting: nutrition must attach to g-health-core and consume core-owned shared concepts
    without redefining them;
  - decomposes into subsystems: nutrition source-of-truth, personalized nutrition process,
    practical outputs, recipes/instructions, base-prep/reuse, food tracking, nutrition review,
    bad-week mode, safety boundary, future integration seam.

  ## §IMPORTS

  Imported as born-closed only where owner-approved/core-reviewed:

  - I1 — g-health-core owns the expert-variable vs irreducible-owner-fact boundary:
    researchable-from-evidence+profile => system decides; irreducible owner fact => system may ask;
    all questions are non-blocking, with graceful defaults/reduced mode and no re-pestering.
  - I2 — g-health-core owns shared concepts: `phase`, `week`, `day`, `weight_trend`,
    `adherence`, `biofeedback`; nutrition consumes them and writes only namespaced nutrition fields.
  - I3 — g-health-core owns PLAN-vs-LOG separation, parse/materiality, definitions/library,
    value grammar, procedure/template contract, schema/versioning, and domain attach contract.
  - I4 — Direction OS is not a raw diary. Raw daily nutrition/weight/check-in/food data lives in
    Health AI System; Direction OS may read Health AI when needed for strategy/development but does
    not duplicate raw logs in its own state.
  - I5 — Per CALL context, c-health-core-review-002 returned corrected binding G5 met and owner
    approved d-health-core-close-and-next-bet with "approve". The exact file path
    `live/health/knowledge/health-core-corrected-g5-review.md` was not fetchable in this session;
    the fact is therefore carried from CALL context, not file import evidence.

  ## §DIRTY INPUT DISPOSITION

  - D1 — prior nutrition v1 product/repo artifacts: rejected as authority; retained only as failure evidence.
  - D2 — `work/converge-health-nutrition-input.md`: rejected as authority; used only as prompt inventory
    for re-derivation.
  - D3 — `work/converge-nutrition-define-draft.md`: rejected as authority because explicitly never
    owner-signed; overlapping terms were re-derived and owner-signed here.
  - D4 — prior architecture candidates A-E, including Mealie/vitrine ideas: not imported; architecture
    decisions route to converge-arch/PLAN if needed.
  - D5 — prior evidence-base magnitudes/gaps: not imported into WHAT; concrete numbers route to PLAN/evidence.
  - D6 — Mealie/recipe-app/vitrine research: rejected as current requirement after owner correction;
    retained only as future-capture context.

  ## §GLOSSARY

  | Term | meaning-here | load-bearing properties | rejected readings |
  |---|---|---|---|
  | nutrition module | Additive nutrition layer on g-health-core. It consumes core profile, phase, metrics, parse/library/procedure surfaces, and writes nutrition-specific artifacts only in nutrition namespace. | Prevents duplicating core; keeps nutrition attachable and replaceable. | Standalone nutrition system that redefines profile, phase, metrics, review, or logs. |
  | nutrition source-of-truth | Canonical Health AI nutrition artifacts: decided variables, rules, menu-cycles, recipes/instructions, grocery needs, meal-prep templates, fallback meals, tracking LOGs, review notes, and bounded process specs. Core remains authority for shared concepts. | Gives one authority for nutrition outputs while preserving core ownership. | Direction OS as diary; external recipe/meal-planning app as canonical truth; passive folder with no derivation rules. |
  | expert-variable | Nutrition variable a competent system decides from evidence + owner profile: meals/day, timing, macros, calorie/deficit policy, protein strategy, food selection, tracking precision, review cadence. | Eliminates the v1 bug. | Asking owner "how many meals per day?" as setup preference. |
  | owner-fact | Irreducible personal fact the system cannot research or infer safely: allergies, intolerances, meds/medical constraints, religious/ethical exclusions, dislikes, hard schedule, budget, real cooking time, equipment, social constraints, sustainable logging capacity. | Defines askable surface; may be pending without blocking. | Owner wishes about expert variables as facts; fabricated facts when owner does not know. |
  | personalized nutrition process | A set-up and run loop derived from owner facts + core profile/phase/metrics + system-decided nutrition variables. It produces a first nutrition cycle, tracking, feedback, and review mutation. | Prevents generic diet-sheet output. | "Quick menu" not grounded in owner profile/process. |
  | menu-cycle / eating plan | Bounded generated eating plan for the next cycle, resolved from core anchors + nutrition variables; can be re-solved when the day goes off-plan. | Makes nutrition executable without static diet drift. | Static diet forever; buffet of options the owner must manually choose from. |
  | recipe / instruction | Executable cooking/prep instruction detailed enough to buy, prepare, cook, substitute, reuse prep, and feed menu/prep/shopping needs. | Recipes are process building blocks, not prose-only ideas. | Vague "cook chicken" advice; app-specific recipe schema as WHAT. |
  | base-prep / reused ingredients | A prepared component or ingredient batch that can be reused across multiple meals/recipes and must not make prep/shopping logic lie. | Captures the owner's chicken-prep example without requiring Mealie. | Treating every recipe as isolated when shared prep exists. |
  | grocery needs | Derived statement of what needs to be bought or available for the current cycle, considering menu, recipes, fallback, meal-prep, and base-prep/reuse. | Supports execution even without a shopping-list app. | External shopping app as authority; shopping list detached from prep/menu reality. |
  | fallback / lazy food | Pre-designed low-effort meals that still count toward nutrition targets and are scored as valid execution. | Keeps bad weeks inside the system. | Fallback as cheat/lapse/off-plan free-for-all. |
  | nutrition tracking | Low-friction food LOG in Health AI via text/voice/photo: planned-vs-actual, substitutions, fallback use, skipped/off-plan events, uncertainty/confidence, hunger/satiety/friction signals, and estimates sufficient for review. | Makes nutrition a closed loop. | Direction OS food diary; mandatory gram logging; tracking hidden inside review. |
  | feedback | Owner report that something did not work: taste, hunger, difficulty, price, time, boredom, slip, social situation, prep friction, tracking burden, or missing data. | Input to artifact mutation. | Passive note that never changes menus/recipes/rules. |
  | nutrition review | Health AI mechanism that consumes feedback + nutrition tracking + core metrics/phase/biofeedback/adherence and emits a decision: hold, mutate dishes, rebuild menu-cycle, update fallback/prep/rules, refresh evidence, or propose a braked change. | Closes the loop between body outcome and food artifacts. | Direction OS strategic review; passive summary; raw daily diary export. |
  | bad-week mode | Reduced nutrition mode using valid fallback/lazy-food minimums and relaxed-but-nonzero tracking; still inside Health AI artifacts. | Protects repeatability under stress/absence. | Treating bad week as total system failure; importing training bad-week rules. |
  | safety / crash-diet boundary | Non-negotiable boundary: nutrition does not diagnose or prescribe medically; red flags halt progression or switch to conservative mode and use non-diagnostic medical-check language; concrete thresholds route to PLAN/evidence. | Preserves guarded risk posture. | Aggressive deficit held open-loop; silent relaxation of safety brakes. |
  | future integration seam | Nutrition artifacts are structured enough that a future vitrine/app can mirror them later, but no vitrine is required now. | Prevents lock-in to chat-only shape without delaying current nutrition process. | Mealie/Notion/UI/shopping app as current requirement. |

  ## §SIGNOFF — DEFINE

  §SIGNOFF: owner approved nutrition Define @ 2026-06-16 — "A — да, подписываем"

  Locked meaning:
  - expert nutrition variables are system-decided;
  - only irreducible owner facts are askable;
  - all questions are non-blocking;
  - no re-pestering; missing facts use pending/reduced mode or sensible revisable defaults.

  ## §WHAT

  Status legend: all rows are `answered`.

  W1. Nutrition source-of-truth
  status: answered
  requirement: |
    Health AI has canonical nutrition artifacts for rules, system-decided variables, menu-cycles,
    recipes/instructions, grocery needs, meal-prep, fallback meals, tracking LOGs, review notes,
    and bounded nutrition process specs.
  source: TREE nutrition source-of-truth criterion; CHARTER Direction OS boundary; GLOSSARY nutrition source-of-truth.
  acceptance: |
    A future executor can point to the Health AI nutrition layer and show where current nutrition decisions,
    outputs, logs, and review mutations live. Direction OS does not store raw daily nutrition data.

  W2. Nutrition attaches to core
  status: answered
  requirement: |
    Nutrition consumes g-health-core-owned profile, phase, metrics, parse/materiality, PLAN-vs-LOG,
    schema/versioning, and attach contract. Nutrition does not redefine core concepts.
  source: core-first re-map; g-health-core attach contract; GLOSSARY nutrition module.
  acceptance: |
    Nutrition writes only nutrition-namespaced artifacts/fields and uses core `phase`, `week`, `day`,
    `weight_trend`, `adherence`, and `biofeedback` instead of duplicating them.

  W3. Expert-variable vs owner-fact boundary
  status: answered
  requirement: |
    Nutrition asks only irreducible owner facts and decides expert variables itself from evidence +
    profile + phase + feedback. Meals/day, timing, macros, deficit, protein strategy, food selection,
    tracking precision, and review cadence are not setup preferences.
  source: reset evidence; owner Define signoff; GLOSSARY expert-variable and owner-fact.
  acceptance: |
    Initial intake has no mandatory expert-variable questions. Missing owner facts do not block:
    they remain pending/reduced-mode or receive documented revisable defaults where safe.

  W4. Personalized first nutrition process
  status: answered
  requirement: |
    The first nutrition cycle is not a generic diet sheet. It is derived from owner facts, core profile,
    phase/metrics, and system-decided nutrition variables, then run with tracking and review.
  source: owner correction "не generic... засетапить нормально"; GLOSSARY personalized nutrition process.
  acceptance: |
    The first cycle includes setup, eating structure, outputs, tracking instructions, feedback path,
    and first review loop; it explains which owner facts and system decisions shaped it.

  W5. Practical outputs
  status: answered
  requirement: |
    Nutrition can produce practical outputs in chat/Health AI without external UI: menu/eating plan,
    substitutions/swaps, recipes/instructions, grocery needs, fallback/lazy meals, meal-prep guidance,
    and post-feedback corrections.
  source: TREE practical outputs criterion; owner vitrine cut; GLOSSARY menu-cycle, recipe/instruction,
    grocery needs, fallback/lazy food.
  acceptance: |
    Owner can ask in chat what to eat/cook/buy/replace and receive executable outputs derived from
    current nutrition artifacts.

  W6. Detailed recipes/instructions
  status: answered
  requirement: |
    Recipes/instructions must be detailed enough to execute: what to buy, what to prep, steps, substitutions,
    time/friction notes, equipment constraints, base-prep use, and relation to menu/fallback/prep.
  source: TREE recipes criterion; owner Mealie example; GLOSSARY recipe/instruction.
  acceptance: |
    A recipe/instruction cannot be vague prose. It must be sufficient for actual cooking/prep and later
    derivation of grocery/prep needs.

  W7. Base-prep / reuse correctness
  status: answered
  requirement: |
    Nutrition must represent and reason about base-prep/reused ingredients so that prep and grocery needs
    do not lie when one prepared component is used across multiple meals.
  source: owner chicken/base-prep example; GLOSSARY base-prep/reused ingredients.
  acceptance: |
    A shared prepared component can be used by multiple meals without double-counting or omitting prep/grocery
    needs at the process level. Exact data model routes to converge-arch/PLAN.

  W8. Nutrition tracking
  status: answered
  requirement: |
    Nutrition tracking is mandatory and lives in Health AI. It supports low-friction text/voice/photo food
    logs capturing planned-vs-actual, substitutions, fallback use, skipped/off-plan events, rough food/portion
    descriptions, uncertainty/confidence, hunger/satiety/friction signals, and estimates sufficient for review.
  source: owner tracking correction; core parse/materiality and non-blocking question policy; GLOSSARY nutrition tracking.
  acceptance: |
    Owner can report a day/meals roughly; the system creates a usable nutrition LOG, marks confidence,
    asks only materially necessary clarifying questions, proceeds with safe/default estimates on non-answer,
    and does not require gram-level logging by default.

  W9. Tracking-to-review mutation
  status: answered
  requirement: |
    Nutrition tracking and feedback must change artifacts when needed: menu-cycle, recipes, fallback meals,
    prep rules, grocery needs, and system-decided nutrition variables.
  source: TREE nutrition review criterion; owner tracking correction; GLOSSARY nutrition review and feedback.
  acceptance: |
    If logs show hunger, prep friction, frequent fallback, off-plan pattern, disliked foods, poor adherence,
    or safety/body-outcome problems, review emits a concrete mutation/hold/rebuild/refresh/brake decision.

  W10. Bad-week mode
  status: answered
  requirement: |
    Nutrition has a bad-week mode using valid fallback/lazy-food minimums and relaxed-but-nonzero tracking,
    without treating the week as total failure.
  source: CHARTER adherence/relapse lens; TREE body outcome; GLOSSARY bad-week mode.
  acceptance: |
    There is a defined way to keep eating inside a reduced nutrition process during low time/stress/absence.

  W11. Safety boundary
  status: answered
  requirement: |
    Nutrition does not diagnose or prescribe medically. Red flags, symptoms, or unsafe deterioration halt
    progression or switch to conservative mode and recommend medical check in non-diagnostic language.
  source: CHARTER medical-safety lens; g-health-core red-flag halt; GLOSSARY safety/crash-diet boundary.
  acceptance: |
    Nutrition cannot silently continue aggressive deficit or unsafe progression when safety flags appear.

  W12. No current vitrine/app requirement
  status: answered
  requirement: |
    No external vitrine, Mealie, Notion, recipe app, shopping-list app, weekly-menu UI, image sync, or
    recipe-image generation is required in current nutrition WHAT.
  source: owner vitrine cut signoff; GLOSSARY future integration seam.
  acceptance: |
    Executor/shape may not make success depend on Mealie/UI/app integration for this nutrition process.

  W13. Future integration seam
  status: answered
  requirement: |
    Nutrition artifacts must not be designed as a chat-only dead end. They should be structured so a future
    vitrine/app can mirror recipes, menu, grocery needs, or images later without rewriting the core nutrition process.
  source: owner "процесс был так построен, чтобы... можно было потом их подключить"; GLOSSARY future integration seam.
  acceptance: |
    Current implementation remains chat-first and Health-AI-canonical, but does not block later external mirror work.

  ## §SIGNOFF — RESOLVE / WHAT

  §SIGNOFF: owner approved revised nutrition WHAT @ 2026-06-16 — "A"

  Owner-approved amendments before final signoff:
  - "не generic... засетапить нормально" => W4 personalized process, not generic quick menu.
  - "про трекинг... охренеть какая важная часть" => W8/W9 mandatory nutrition tracking.
  - "всё убираем витрины... не является требованием... можно было потом их подключить" => W12/W13.

  ## §COVERAGE

  TREE done_when coverage:
  - nutrition source-of-truth -> W1, W2.
  - practical outputs -> W5, W6, W7.
  - nutrition review -> W8, W9.
  - extension points -> W13 now only as future seam; bounded recurring nutrition processes route to converge-arch/PLAN if needed.
  - specialized apps allowed / Direction OS no raw logs -> W12, W13, W1, W8.
  - body outcome / no crash diet -> W9, W10, W11.

  Cross-node/core edge coverage:
  - consumes core-owned shared concepts without duplication -> W2.
  - expert-variable vs irreducible-owner-fact boundary -> W3.
  - PLAN-vs-LOG / parse / non-blocking questions -> W2, W3, W8.
  - raw daily data boundary -> W1, W8, W12.

  Dirty input coverage:
  - v1 failure "meals/day asked" -> refuted/re-derived as W3.
  - dirty first-pass recipe/app/architecture candidates -> rejected as authority; vitrine cut in W12.
  - paused Define glossary -> re-derived as signed glossary here; not imported.

  ## §OPEN / DEFERRED CHECK

  open rows: 0
  deferred rows: 0

  ## §ROUTE

  Next: converge-arch.

  Reason:
  - The WHAT is closed, but the node is heavy and has architecture-contract questions:
    artifact authority/derivation, exact nutrition attach contract on core, LOG shape,
    review mutation pathway, base-prep/reuse semantics, future integration seam,
    and bounded recurring nutrition procedures.
  - Do not emit executor CALL yet.
  ---

  NOW.md:
  - Add/replace decision d-health-nutrition-define-signoff-001 -> status resolved, owner_choice A,
    owner_words "A — да, подписываем".
  - Add decision d-health-nutrition-what-signoff-001 -> status resolved, owner_choice A,
    owner_words "A".
  - Add note:
    "2026-06-16 nutrition converge closed WHAT: personalized nutrition process on g-health-core,
    mandatory nutrition tracking, no current vitrine/Mealie/UI requirement, future integration seam only.
    Next = converge-arch."
  - Set next to CALL c-health-nutrition-converge-arch-001 below.
  - Do not add raw daily nutrition data.
  - Do not change TREE.md status yet; shape/review path will do that after architecture/verify.

  LOG.md:
  - Append:
    2026-06-16 — converge g-health-nutrition-system: owner-signed closed WHAT for nutrition module on core;
    personalized process + mandatory tracking; vitrine/Mealie cut; next converge-arch.
  history/:
  - Add this RESULT as live/health/history/2026-06-16-s-health-nutrition-converge-001.md.

captures:
  - Mealie remains a future candidate only after nutrition + training processes work; owner explicitly cut vitrine as current requirement.
  - Later research/spike candidate: whether Mealie can mirror recipes/menu/grocery needs, including base-prep/reuse and recipe-image metadata, without becoming source-of-truth.
  - Tracking quality is now a central acceptance risk; do not let implementation collapse it into passive notes or gram-level bureaucracy.

decisions_needed: []

play_check:
  - 1 Triage & import: done — triage heavy/converge ON; imported only core-approved shared-boundary facts; dirty v1, dirty input, paused Define, and prior architecture candidates rejected as authority.
  - 2 Define: done — disputed boundary signed by owner: "A — да, подписываем"; glossary closed around nutrition module, source-of-truth, expert-variable/owner-fact, tracking, review, bad-week, safety, and future seam.
  - 3 Resolve: done — flat WHAT W1-W13 closed; owner amended and signed: vitrine cut in his words, tracking required in his words, final approval "A"; open/deferred rows = 0.
  - 4 Close & route: done — coverage complete; canon proposed via glossary; next route is converge-arch because node is heavy and architecture contracts remain.

log: >
  converge nutrition: owner-signed closed WHAT for nutrition module on core; personalized process + mandatory
  tracking; vitrine/Mealie cut; next converge-arch.

next: |
  CALL c-health-nutrition-converge-arch-001
  to: session
  direction: health
  play: converge-arch
  node: g-health-nutrition-system
  goal: |
    g-health-nutrition-system has a closed architecture/contract surface for implementing the signed nutrition
    WHAT on g-health-core without duplicating core, without current vitrine/app requirements, and with mandatory
    nutrition tracking/review/base-prep semantics.
  context: |
    Read:
    - live/health/CHARTER.md
    - live/health/TREE.md
    - live/health/NOW.md
    - live/health/work/converge-g-health-nutrition-system.md
    - live/health/work/converge-g-health-core.md
    - health-ai core files/evidence as needed:
      acceptance/core/evidence-summary.md
      acceptance/core/matrix.json
      core/metrics.md
      core/extensions/attach-contract.md
      core/profile/owner-facts.md
      core/profile/derived-anchors.md
      core/intake/non-blocking-questions.md
      core/parser/materiality.md
      core/principles/minimum-tracked-signals.md
      core/phases.md

    Owner-signed nutrition WHAT highlights:
    - nutrition is a module on g-health-core;
    - expert variables are system-decided; owner facts only are askable and non-blocking;
    - first cycle must be personalized, not generic quick menu;
    - nutrition tracking is mandatory and low-friction via text/voice/photo;
    - tracking must feed review and artifact mutation;
    - recipes/instructions must support base-prep/reuse and grocery/prep correctness;
    - no current Mealie/vitrine/UI/app/image-sync requirement;
    - keep only future integration seam.
  boundaries: |
    Do not build implementation.
    Do not create product repo code.
    Do not require Mealie, UI, app integration, recipe image generation, runtime, DB, server, cron, or scheduler.
    Do not build training/activity.
    Do not store raw daily food, weight, photo, or check-in logs in Direction OS.
    Do not make medical prescriptions.
    Do not rewrite g-health-core; nutrition consumes it.
  done_when: |
    - Architecture/contract surface decomposes each signed WHAT mechanism into build-deciding contracts:
      nutrition artifacts, attach namespace, tracking LOG shape, review mutation path, base-prep/reuse semantics,
      grocery/prep derivation, bad-week mode, safety interaction, and future integration seam.
    - Every architecture decision is either answered with citation to signed WHAT/core contract or routed to PLAN.
    - No open/deferred rows remain, or genuine owner decisions are batched with options and recommendation.
    - Next route is converge-verify if closed; otherwise awaiting_decision.
  return: |
    RESULT with architecture artifact path, coverage evidence, state_changes, decisions_needed, and next CALL.
  budget: one focused converge-arch movement
  surface: any capable session
END_OF_FILE: live/health/history/2026-06-16-s-health-nutrition-converge-001.md
