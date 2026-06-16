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

## §CONTRACTS — converge-arch

> Produced by converge-arch session s-health-nutrition-converge-arch-001 on 2026-06-16.
> Detailed architecture-on-paper lives in work/converge-g-health-nutrition-system-arch.md.
> Contract rows are behavioral; HOW details stay `→ PLAN`.

- NCA0 — starter-kit seed intake, not authority:
  consumer g-health-nutrition-system; producer g-health-starter-kit; flow = starter nutrition material may seed the first nutrition source-of-truth only after re-validation against signed nutrition WHAT, core contracts, current owner facts, phase, and metrics. Producer exists/done. Exact promotion mechanics `→ PLAN`.

- NCA1 — nutrition module attach and canonical nutrition source-of-truth:
  consumer g-health-nutrition-system; producer g-health-core; flow = nutrition consumes core-owned profile/anchors, phase/week/day, metric trio, PLAN-vs-LOG, parser/library/procedure surface, schema/versioning, and attach contract; writes only nutrition-namespaced artifacts/fields; never redefines core concepts. Exact domain layout and registry shape `→ PLAN`.

- NCA2 — personalized nutrition cycle derivation:
  consumer owner-facing nutrition outputs and nutrition review; producer core profile/anchors + nutrition source-of-truth; flow = active nutrition cycle is derived from owner facts, pending/reduced-mode facts, system-decided variables, core phase/metrics, nutrition rules, recipes, fallback, prep state, and prior review decisions; never a generic menu or static diet sheet. Resolver details `→ PLAN`.

- NCA3 — nutrition tracking LOG:
  consumer nutrition review, nutrition outputs, and core-derived reads; producer owner text/voice/photo input parsed through core parser/library/materiality surface; flow = Health AI nutrition LOG records planned-vs-actual, substitutions, fallback use, skipped/off-plan events, rough portion descriptions, uncertainty/confidence, hunger/satiety/friction signals, and review-sufficient estimates. LOG schema/tokens `→ PLAN`.

- NCA4 — tracking-to-review mutation path:
  consumer nutrition artifacts; producer nutrition review using nutrition LOG + feedback + core phase/metrics/biofeedback/adherence; flow = review emits hold/mutate/rebuild/update/fallback/prep/grocery/variable/evidence-refresh/brake decision. Braked/safety changes require ratification or conservative default. Mutation packet shape `→ PLAN`.

- NCA5 — recipes, base-prep/reuse, grocery/prep correctness:
  consumer menu-cycle, grocery needs, prep plan, fallback outputs, and review; producer recipes/instructions + base-prep/reused components; flow = executable recipes connect to menu, prep, substitutions, fallback, and grocery derivation; base-prep/reused ingredients are first-class reusable components so grocery/prep needs do not double-count or omit shared preparation. Exact quantity math/model `→ PLAN`.

- NCA6 — bad-week mode and safety interaction:
  consumer owner-facing nutrition process and review; producer nutrition fallback/lazy-food library + core safety/red-flag policy + minimum tracked-signal principle; flow = valid reduced nutrition process with fallback/lazy-food minimums, relaxed-but-nonzero tracking, and conservative safety brakes. Thresholds/minimums `→ PLAN`.

- NCA7 — future integration seam, not current app requirement:
  consumer future external mirror/vitrine/app if later built; producer canonical nutrition artifacts; flow = artifacts remain structured enough to mirror recipes, menu-cycles, grocery needs, prep plans, images, or app displays later; external apps are not current requirement and not source-of-truth. Mirror/export shape `→ PLAN`.

- NCA8 — training day_type / cross-module nutrition coupling via core only:
  consumer g-health-nutrition-system; producer core day_type contract now and future training logged day_type later through core CA5; flow = nutrition reads coarse day_type to adjust carb targets; current planned source is core; future logged source overrides planned fallback when training exists; nutrition never writes day_type back; no direct module-to-module dependency. Tier labels/magnitudes `→ PLAN`.

- NCA9 — Direction OS visibility and raw-data ownership boundary:
  consumer Direction OS for development/strategy/review; producer Health AI nutrition artifacts and LOGs; flow = Direction OS may read all nutrition data on demand but does not duplicate raw daily food/weight/photo/check-in logs into its own state; Health AI nutrition carries zero reference/dependency upward. Read mechanism `→ PLAN`.

§CONTRACTS completeness:
- g-health-starter-kit -> nutrition seed: NCA0.
- g-health-core -> nutrition module attach/shared concepts/parser/library/procedure/schema: NCA1, NCA3, NCA4, NCA8.
- nutrition internal output loop: NCA2, NCA3, NCA4, NCA5, NCA6.
- g-health-training-activity-system interaction: NCA8 only through core CA5; no direct module-to-module dependency.
- Direction OS boundary: NCA9.
- future specialized apps/vitrine: NCA7 only; no current requirement.
- root body outcome / no crash diet / bad weeks: NCA2, NCA4, NCA6.
- dangling producer check: PASS. Future training logged day_type is named but not required for current nutrition; planned day_type comes from core.
- HOW leakage check: PASS. Concrete file paths, schemas, enum tokens, app integration, UI, runtime, DB, scheduler, cron, formula magnitudes, and sync mechanisms route `→ PLAN`.

§SIGNOFF — DECLARE:
closed @ 2026-06-16 by signed nutrition WHAT + reviewed core contracts.
owner_gate_batch: [].

## §ARCH

Heavy architecture-on-paper lives in:
- live/health/work/converge-g-health-nutrition-system-arch.md

Closed high-risk questions:
- Q1 source-of-truth = Health AI nutrition namespace/module attached to core.
- Q2 nutrition-specific owner facts = core owner_facts plus namespaced nutrition extensions; expert variables remain system-decided.
- Q3 active nutrition process = setup -> system-decided variables -> cycle -> recipes/base-prep/grocery -> LOG -> review mutation.
- Q4 nutrition LOG = low-friction append-only Health AI LOG through core parser/library/materiality.
- Q5 review = explicit mutation decision/bundle with brakes.
- Q6 base-prep/grocery = first-class reusable components feeding derivation.
- Q7 bad-week/safety = reduced valid process with conservative safety override.
- Q8 future integration = mirror seam only, no current app authority.
- Q9 training interaction = coarse day_type through core CA5, no direct module coupling.
- gap-hunt closure = starter-kit seed intake is seed-only, not authority.

arch_open: 0.
arch_in_context_only: PASS — these architecture picks ride PLAN/implementation context only and must not be copied as standalone done_when.

## §ROUTE

Next: converge-verify.

Reason:
- The WHAT is closed and converge-arch is now closed.
- §CONTRACTS NCA0-NCA9 cover all TREE/core/starter/training/Direction OS/future seam interactions.
- Architecture-on-paper Q1-Q9 is closed with no open high-risk questions and no owner decision batch.
- Do not emit executor CALL yet; verify/refutation must run first.

---

END_OF_FILE: live/health/work/converge-g-health-nutrition-system.md
