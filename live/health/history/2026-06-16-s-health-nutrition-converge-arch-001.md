RESULT s-health-nutrition-converge-arch-001 (call: c-health-nutrition-converge-arch-001)
direction: health   play: converge-arch   node/task: g-health-nutrition-system

outcome: |
  g-health-nutrition-system has a closed contract/architecture-on-paper surface for implementation planning:
  - §CONTRACTS NCA0-NCA9 cover starter seed intake, core attach, personalized cycle derivation, nutrition LOG/tracking, review mutation, recipe/base-prep/grocery semantics, bad-week+safety, future integration seam, training day_type via core, and Direction OS visibility/no-raw-duplication.
  - §ARCH Q1-Q9 close all high-risk nutrition architecture questions with refuted alternatives.
  - No current vitrine/Mealie/UI/app/runtime/DB/scheduler requirement was introduced.
  - No g-health-core concept was duplicated; nutrition remains an additive namespaced module consuming core-owned profile, phase/week/day, metrics, parser/library/procedure/schema/version surfaces.
  - No genuine owner decision remains; route is converge-verify before shape.

evidence: |
  Primary state/spec evidence:
  - live/health/NOW.md says nutrition converge closed WHAT on 2026-06-16 and next route is converge-arch; signed highlights include module-on-core, system-decided expert variables, mandatory low-friction tracking, review mutation, base-prep/reuse, no current Mealie/vitrine/UI/app/image-sync requirement, future integration seam only.
  - live/health/work/converge-g-health-nutrition-system.md has CLOSED WHAT with W1-W13 answered and owner signoffs:
    W1 source-of-truth, W2 core attach, W3 expert-variable boundary, W4 personalized first process, W5 outputs, W6 recipes/instructions, W7 base-prep/reuse, W8 tracking, W9 tracking-to-review mutation, W10 bad-week mode, W11 safety, W12 no current vitrine/app, W13 future seam.
  - live/health/work/converge-g-health-core.md §CONTRACTS CA3-CA7 and §WHAT WA9-WA12 establish module attach, phase/week/day, metric trio, day_type provenance, core-owned reusable template, parser/library/procedure surface.
  - health-ai core/extensions/attach-contract.md confirms modules read phase/week/day/weight_trend/adherence/biofeedback and write only namespaced x_<domain>_* fields without redefining core.
  - health-ai acceptance/core/evidence-summary.md reports PASS: acceptance matrix, core slice, core evidence, 26/26 acceptance/contract rows, blocker gaps 0; CA1-CA9 pass.
  Done_when coverage:
  - nutrition artifacts: NCA1/NCA2 + Q1/Q3.
  - attach namespace: NCA1 + Q1/Q2.
  - tracking LOG shape: NCA3 + Q4.
  - review mutation path: NCA4 + Q5.
  - base-prep/reuse: NCA5 + Q6.
  - grocery/prep derivation: NCA5 + Q6.
  - bad-week mode: NCA6 + Q7.
  - safety interaction: NCA6 + Q7.
  - future integration seam: NCA7 + Q8.
  - cross-module/training interaction: NCA8 + Q9.
  - Direction OS raw-data boundary: NCA9.
  Closure evidence:
  - contract_coverage: every TREE interaction named and covered.
  - arch_open: 0.
  - arch_in_context_only: PASS; architecture-on-paper routes as input evidence for PLAN/implementation, not executor done_when.
  - owner_gate_batch: [].

state_changes: |
  1) Create file: live/health/work/converge-g-health-nutrition-system-arch.md

  BEGIN_FILE live/health/work/converge-g-health-nutrition-system-arch.md
  ---
  # Converge-Arch — g-health-nutrition-system

  > Produced by converge-arch session s-health-nutrition-converge-arch-001 on 2026-06-16.
  > Assembly surface only; not a state file.
  > Status: CLOSED CONTRACTS + ARCHITECTURE-ON-PAPER; route to converge-verify.
  > Authority: signed nutrition WHAT + reviewed g-health-core contracts/evidence.
  > Firewall: HOW file layout, exact schemas, field tokens, app mirrors, UI, runtime, DB, scheduler, cron, concrete formula magnitudes, and literal recipe formats stay `→ PLAN`.

  ## §SOURCE LOCK

  Closed sources consumed:
  - live/health/work/converge-g-health-nutrition-system.md:
    signed nutrition WHAT W1-W13; owner approved Define @ 2026-06-16 ("A — да, подписываем") and WHAT @ 2026-06-16 ("A").
  - live/health/work/converge-g-health-core.md:
    core §CONTRACTS CA1-CA9 and shared concepts: profile/anchors, phase/week/day, metric trio, PLAN-vs-LOG, parser/library/procedure surface, attach contract, schema/versioning.
  - live/health/knowledge/health-core-corrected-g5-review.md:
    g-health-core met corrected G5; product evidence had zero blocker gaps across WA1-WA12 + W69/W70/W72/W73/W74 + CA1-CA9.
  - health-ai core files:
    core/extensions/attach-contract.md, core/metrics.md, core/profile/owner-facts.md, core/profile/derived-anchors.md, core/intake/non-blocking-questions.md, core/parser/materiality.md, core/principles/minimum-tracked-signals.md, core/phases.md.
  - health-ai acceptance:
    acceptance/core/evidence-summary.md and acceptance/core/matrix.json.

  Owner-gate status:
  - owner_gate_batch: []
  - Reason: no new owner-owned value fork appeared. Contract and architecture picks are mechanically derived from signed nutrition WHAT plus already-reviewed core contracts. Low-level formats and magnitudes are `→ PLAN`.

  ## §CONTRACTS — Declare

  Contract style:
  - Consumer-driven and behavioral.
  - Each row states consumer, producer, flow, direction, trigger, status.
  - HOW details stay `→ PLAN`.

  ### NCA0 — starter-kit seed intake, not authority

  consumer: g-health-nutrition-system.
  producer: g-health-starter-kit.
  flow: any starter-kit nutrition artifact or feedback may be read as seed/input evidence for the first nutrition source-of-truth, but it is never authority by itself. The nutrition module re-validates seed material against signed nutrition WHAT, g-health-core contracts, current owner facts, phase, and metrics before promotion.
  direction: g-health-starter-kit -> g-health-nutrition-system.
  trigger: initial nutrition source-of-truth seeding or later migration from starter material.
  status: closed. Producer node exists and is done. Exact seed file path and promotion mechanics `→ PLAN`.

  ### NCA1 — nutrition module attach and canonical nutrition source-of-truth

  consumer: g-health-nutrition-system.
  producer: g-health-core.
  flow: nutrition attaches as an additive module on Health AI core. It consumes core-owned profile/anchors, phase/week/day, metric trio, PLAN-vs-LOG, parser/library/procedure surface, schema/versioning, and attach contract. Nutrition writes only nutrition-namespaced artifacts/fields and never redefines core concepts.
  direction: g-health-core -> nutrition for shared concepts; nutrition -> nutrition namespace only for module artifacts.
  trigger: module registration, nutrition computation, nutrition logging, nutrition review, or nutrition output generation.
  status: closed. Exact domain layout, registry line, literal tokens, and file shapes `→ PLAN`.

  ### NCA2 — personalized nutrition cycle derivation

  consumer: owner-facing nutrition outputs and nutrition review.
  producer: g-health-core profile/anchors + current nutrition source-of-truth.
  flow: the active nutrition cycle is derived from owner facts, pending/reduced-mode facts, system-decided nutrition variables, core phase/week/day, core metrics, nutrition rules, recipes, fallback meals, prep state, and prior review decisions. It must explain which owner facts and system decisions shaped the cycle. It is not a generic menu and not a static diet sheet.
  direction: core+nutrition source-of-truth -> active menu-cycle/eating plan outputs.
  trigger: first nutrition setup, cycle start, owner asks what to eat/cook/buy/replace, review mutation, bad-week mode, or re-solve after off-plan events.
  status: closed. Exact resolver algorithm, cycle length, and formula magnitudes `→ PLAN`.

  ### NCA3 — nutrition tracking LOG

  consumer: nutrition review, nutrition outputs, and core-derived adherence/biofeedback read paths.
  producer: owner text/voice/photo input parsed through core parser/library/materiality surface and mapped to nutrition artifacts.
  flow: nutrition tracking creates Health AI LOG records sufficient for review: planned-vs-actual, substitutions, fallback use, skipped/off-plan events, rough food/portion descriptions, uncertainty/confidence, hunger/satiety/friction signals, and estimates. It does not require gram-level logging by default. It asks only materially necessary questions; unanswered/declined data becomes a revisable default or pending/reduced-mode fact under core policy.
  direction: owner input -> Health AI nutrition LOG; LOG -> review/core-derived reads.
  trigger: meal/day update, photo/voice/text food report, skipped/off-plan event, or feedback report.
  status: closed. LOG schema, confidence tokens, source tokens, and portion-estimation rules `→ PLAN`.

  ### NCA4 — tracking-to-review mutation path

  consumer: nutrition source-of-truth artifacts.
  producer: nutrition review using nutrition LOG + feedback + core phase/metrics/biofeedback/adherence.
  flow: review emits a concrete decision: hold, mutate dishes, rebuild menu-cycle, update fallback meals, update prep rules, update grocery needs, update system-decided nutrition variables, refresh evidence, or brake/safety-halt. Non-braked changes may be applied by the Health AI writer under decide-and-inform; braked/safety changes require owner ratification or conservative default.
  direction: LOG+feedback+core metrics -> review decision -> nutrition artifact mutation.
  trigger: owner reports a problem, logs reveal pattern, a configured review point is reached when invoked, or safety/body-outcome signals require review.
  status: closed. Patch shape, review checklist, and mutation application mechanics `→ PLAN`.

  ### NCA5 — recipes, base-prep/reuse, grocery/prep correctness

  consumer: menu-cycle, grocery needs, prep plan, fallback outputs, and review.
  producer: recipes/instructions + base-prep/reused component artifacts.
  flow: recipes/instructions must be executable and connected to menu, prep, substitutions, fallback, and grocery derivation. A base-prep/reused ingredient is a first-class reusable component with planned production and planned uses, so grocery/prep needs neither double-count nor omit shared preparation when one component feeds multiple meals.
  direction: recipes/base-prep -> menu/prep/grocery/review outputs.
  trigger: recipe creation/update, menu-cycle build, grocery derivation, prep-plan generation, fallback update, or review mutation.
  status: closed. Exact component data model, quantity math, pantry assumptions, and grocery list shape `→ PLAN`.

  ### NCA6 — bad-week mode and safety interaction

  consumer: owner-facing nutrition process and review.
  producer: nutrition fallback/lazy-food library + core safety/red-flag policy + core minimum tracked-signal principle.
  flow: bad-week mode is a valid reduced nutrition process: fallback/lazy-food minimums, relaxed-but-nonzero tracking, fewer decisions, and safe defaults. Safety/crash-diet boundary overrides nutrition progression: red flags, symptoms, unsafe deterioration, or below-floor proposals halt progression or switch to conservative mode with non-diagnostic medical-check language.
  direction: safety/fallback rules -> active reduced process and review constraints.
  trigger: low time, stress, absence, repeated adherence drop, owner asks for lazy mode, safety flag, or braked nutrition proposal.
  status: closed. Fallback minimums, red-flag threshold list, calorie/protein floors, and bad-week entry/exit mechanics `→ PLAN`.

  ### NCA7 — future integration seam, not current app requirement

  consumer: future external mirror/vitrine/app, if later built; current chat/Health AI outputs remain primary.
  producer: canonical nutrition artifacts.
  flow: nutrition artifacts remain structured enough for future mirroring of recipes, menu-cycles, grocery needs, prep plans, images, or app displays. External apps are mirrors/interfaces only; they are not current requirements and not source-of-truth.
  direction: nutrition artifacts -> future mirror/interface.
  trigger: a future direction/bet chooses to add a vitrine/app/mirror; no current trigger is required.
  status: closed. Mirror/API/export shape and any image/app/UI sync `→ PLAN` and out of current scope.

  ### NCA8 — training day_type / cross-module nutrition coupling via core only

  consumer: g-health-nutrition-system.
  producer: g-health-core day_type contract now; future g-health-training-activity-system logged day_type later through the already-closed core CA5 provenance rule.
  flow: nutrition may read a coarse day_type for a date to adjust carb targets. Current producer is the core planned day_type. When training exists and logs actuals, logged day_type overrides planned fallback under core CA5. Nutrition never writes day_type back. There is no direct nutrition -> training file dependency and no training -> nutrition private contract outside core.
  direction: core/training day_type -> nutrition carb-target derivation through core-owned contract.
  trigger: nutrition resolves a date's carb target.
  status: closed. No build-order blocker for current nutrition because planned core day_type exists. Future logged producer is named and consumes CA5 unchanged. Tier labels and magnitudes `→ PLAN`.

  ### NCA9 — Direction OS visibility and raw-data ownership boundary

  consumer: Direction OS when doing development, strategy, or review.
  producer: Health AI nutrition artifacts and LOGs.
  flow: Direction OS may read nutrition artifacts and raw nutrition LOGs on demand, but Direction OS does not duplicate raw daily food/weight/photo/check-in logs into its own state. Health AI nutrition carries zero reference to Direction OS and writes no upward dependency.
  direction: Health AI nutrition -> Direction OS read visibility; no reverse dependency.
  trigger: development, feature work, strategy review, or Direction OS session needing Health AI evidence.
  status: closed. Read mechanism and auth/path/connector details `→ PLAN`.

  ### §CONTRACTS COMPLETENESS

  TREE/core interaction coverage:
  - g-health-starter-kit -> nutrition seed: NCA0.
  - g-health-core -> nutrition module attach/shared concepts/parser/library/procedure/schema: NCA1, NCA3, NCA4, NCA8.
  - nutrition internal output loop: NCA2, NCA3, NCA4, NCA5, NCA6.
  - g-health-training-activity-system interaction: NCA8 only, through core CA5; no direct module-to-module dependency.
  - Direction OS boundary: NCA9.
  - future specialized apps/vitrine: NCA7 only, mirror/interface later; no current requirement.
  - root body outcome / no crash diet / bad weeks: NCA2, NCA4, NCA6.

  Dangling-producer check:
  - no dangling current producer.
  - future training logged day_type is named but not required for current nutrition; current planned day_type comes from core. The later training converge consumes CA5/NCA8 unchanged.

  HOW leakage check:
  - concrete file paths, schema keys, enum tokens, app integration, UI, runtime, DB, scheduler, cron, exact formula magnitudes, and external sync mechanisms are not fixed here; all route `→ PLAN`.

  §SIGNOFF — DECLARE:
  closed @ 2026-06-16 by signed nutrition WHAT + reviewed core contracts.
  owner_gate_batch: [].

  ## §DECOMPOSE

  Nutrition decomposes into 11 internal sub-systems:
  1. nutrition namespace/attach layer;
  2. nutrition owner-fact/profile extension surface;
  3. system-decided nutrition variables/rules;
  4. active menu-cycle/eating-plan resolver;
  5. recipe/instruction library;
  6. base-prep/reused-component model;
  7. grocery/prep derivation;
  8. nutrition tracking LOG surface;
  9. nutrition review/mutation engine;
  10. fallback/bad-week/safety layer;
  11. future integration mirror seam.

  Sub-nodes:
  - none now. The node remains one implementation bet candidate after converge-verify/shape.
  - training/activity remains separate sibling node; no nutrition child is created here.
  - future vitrine/app remains out of current scope and can be shaped later as a separate node if the owner wants.

  Internal seams recorded as contracts:
  - attach/source authority: NCA1;
  - cycle derivation: NCA2;
  - tracking: NCA3;
  - review mutation: NCA4;
  - base-prep/grocery: NCA5;
  - bad-week/safety: NCA6;
  - future mirror: NCA7;
  - cross-module day_type via core: NCA8.

  ## §ARCH — high-risk architecture questions

  Architecture-on-paper only. These picks ride PLAN/implementation CALL context as input evidence. They do not become done_when by themselves.

  ### Q1 — Where is nutrition source-of-truth?

  pick: Health AI nutrition namespace/module attached to core is canonical.
  refuted:
  - external recipe/meal-planning app as authority: bad because signed WHAT removed current app/vitrine requirement and external authority would bypass core attach/review/log contracts.
  - Direction OS as nutrition diary/source: bad because Direction OS is strategic/development layer, not raw daily diary.
  - chat-only transient answers: bad because future sessions cannot inspect/update stable artifacts and future app seam becomes a dead end.
  signed basis: nutrition W1/W2/W12/W13 + core WA9/WA10/CA4.
  routes: NCA1, NCA7, NCA9.
  PLAN slots: P-N1 nutrition domain layout; P-N2 artifact schema and IDs.

  ### Q2 — Where do nutrition-specific owner facts live without duplicating core?

  pick: global irreducible facts stay in core profile owner_facts; nutrition-specific irreducible facts attach as namespaced profile extensions or nutrition artifacts under core attach rules; expert variables are recorded as system-decided nutrition variables with rationale/evidence, not asked preferences.
  refuted:
  - separate nutrition shadow profile: bad because it duplicates core owner-fact boundary and creates drift.
  - asking owner for expert variables at setup: bad because it reopens the v1 defect.
  - forcing all nutrition facts into frozen core schema: bad because it widens core for a module and violates additive attach.
  signed basis: nutrition W2/W3/W4 + core W13-W22/CA4.
  routes: NCA1, NCA2.
  PLAN slots: P-N3 nutrition fact extension surface; P-N4 nutrition variable evidence/rationale structure.

  ### Q3 — What is the active nutrition process topology?

  pick: active cycle loop = setup/facts -> system-decided variables -> menu-cycle/eating plan -> recipes/base-prep/grocery -> low-friction LOG -> review mutation -> next cycle/re-solve.
  refuted:
  - one-time static diet sheet: bad because it cannot mutate from tracking/review and fails bad weeks.
  - buffet of options owner manually chooses from: bad because it turns expert-variable solving into owner labor.
  - pure daily improvisation: bad because grocery/prep/base-prep correctness cannot be guaranteed.
  signed basis: nutrition W4/W5/W6/W7/W8/W9.
  routes: NCA2, NCA5.
  PLAN slots: P-N5 cycle resolver and rebuild rules.

  ### Q4 — What is the nutrition LOG architecture?

  pick: append-only Health AI nutrition LOG entries using core parse/materiality/library and nutrition-namespaced details sufficient for review.
  refuted:
  - mandatory gram/calorie ledger by default: bad because signed tracking requires low-friction and adherence-biased signal, not friction-maximal precision.
  - photo-only memory or chat summary: bad because review cannot inspect structured planned-vs-actual/substitution/fallback/friction signals.
  - Direction OS food diary: bad because raw nutrition logs belong in Health AI.
  signed basis: nutrition W8/W9 + core WA6/WA7/W43-W52 + minimum-tracked-signals.
  routes: NCA3, NCA4, NCA9.
  PLAN slots: P-N9 nutrition LOG schema, confidence/source tokens, portion materiality rules.

  ### Q5 — How does review mutate artifacts?

  pick: nutrition review emits an explicit mutation decision/bundle affecting menu-cycle, recipes, fallback, prep/grocery, or nutrition variables; braked/safety changes require ratification or conservative default; non-braked changes may proceed under decide-and-inform.
  refuted:
  - passive summary-only review: bad because signed WHAT requires tracking/feedback to change artifacts.
  - silent mutation with no decision record: bad because future sessions cannot audit why artifacts changed.
  - every small change waits for owner approval: bad because it recreates over-asking and blocks the system on non-critical details.
  signed basis: nutrition W9/W10/W11 + core W36-W42/G7-2.
  routes: NCA4, NCA6.
  PLAN slots: P-N10 review decision/mutation packet; P-N11 braked-change list.

  ### Q6 — How should base-prep and grocery correctness work?

  pick: base-prep/reused ingredients are first-class prepared components used by recipes/meals, with planned production and planned uses feeding grocery/prep derivation.
  refuted:
  - recipe-local notes only: bad because shared chicken/prep can be double-counted or omitted across recipes.
  - free-text prep advice: bad because grocery/prep derivation cannot prove correctness.
  - external shopping app as authority: bad because external app is not current source-of-truth.
  signed basis: nutrition W6/W7/W5 + owner base-prep correction in signed WHAT.
  routes: NCA5.
  PLAN slots: P-N6 recipe/instruction schema; P-N7 base-prep allocation math; P-N8 grocery derivation rules.

  ### Q7 — What is bad-week mode relative to safety?

  pick: bad-week mode is a reduced but valid nutrition mode with fallback/lazy-food minimums, relaxed tracking, and safety/conservative brakes above nutrition goals.
  refuted:
  - bad week as off-system failure: bad because it breaks repeatability and relapse handling.
  - normal plan unchanged under stress: bad because it ignores friction and increases failure probability.
  - aggressive crash-diet catch-up: bad because safety and maintenance constraints forbid unsafe compensation.
  signed basis: nutrition W10/W11 + CHARTER safety/adherence lenses + core safety/red-flag halt.
  routes: NCA6.
  PLAN slots: P-N11 safety thresholds; P-N12 bad-week entry/exit and minimums.

  ### Q8 — What is the future integration seam?

  pick: future app/vitrine mirrors canonical nutrition artifacts; it never becomes current authority and is not required now.
  refuted:
  - build Mealie/vitrine now: bad because owner explicitly cut current app/vitrine requirement.
  - no structure because chat-first: bad because it blocks later mirroring and makes artifacts dead-end.
  - external app owns recipes/menu/grocery: bad because it bypasses nutrition review mutation and core attach.
  signed basis: nutrition W12/W13.
  routes: NCA7.
  PLAN slots: P-N13 mirror/export concept, when future node is shaped.

  ### Q9 — How does nutrition interact with training/activity?

  pick: no direct nutrition<->training file coupling now. Nutrition consumes coarse day_type through core CA5. Current source is core planned day_type; future training logged day_type can override planned fallback when training module exists.
  refuted:
  - direct training reads nutrition files or nutrition reads training private files: bad because core CA6 says reusable template is core-owned and removes module-to-module dependency.
  - block nutrition until training exists: bad because core planned day_type is enough for current nutrition and signed nutrition should proceed.
  - ignore training day_type forever: bad because TREE expects cross-module nutrition/training interaction for protein/calories under volume.
  signed basis: core CA5/CA6 + nutrition W2/W13 + TREE training cross-module edge.
  routes: NCA8.
  PLAN slots: P-N14 day_type-to-nutrition target mapping, using core CA5 provenance.

  ### Gap-hunt

  Question asked after decomposition: "which architecture question did we not ask?"
  Found gap: starter-kit seed ingestion could quietly become authority or get dropped.
  Closure: NCA0 makes starter-kit output seed-only, not authority; nutrition re-validates it against signed WHAT/core before promotion.

  ## §PLAN-AGENDA — nutrition HOW slots

  Values are not decided here:
  - P-N1 nutrition domain layout and registration surface.
  - P-N2 artifact schema/IDs for rules, variables, cycles, recipes, grocery, fallback, review notes.
  - P-N3 nutrition-specific owner-fact extension surface.
  - P-N4 evidence/rationale structure for system-decided nutrition variables.
  - P-N5 active cycle resolver and rebuild/re-solve rules.
  - P-N6 recipe/instruction schema.
  - P-N7 base-prep allocation and remaining-availability math.
  - P-N8 grocery derivation rules and pantry assumptions.
  - P-N9 nutrition LOG shape, confidence/source tokens, portion materiality.
  - P-N10 review decision/mutation packet and application mechanics.
  - P-N11 safety floor/red-flag/brake thresholds.
  - P-N12 bad-week minimums and entry/exit rules.
  - P-N13 future mirror/export shape.
  - P-N14 day_type-to-nutrition target mapping.

  ## §OPEN / DEFERRED CHECK

  open high-risk architecture questions: 0.
  deferred rows: 0.
  low-risk HOW slots: P-N1 through P-N14, all `→ PLAN`.

  ## §SIGNOFF — ARCHITECT

  closed @ 2026-06-16 by signed nutrition WHAT + reviewed g-health-core contracts/evidence.
  owner_gate_batch: [].
  arch_in_context_only: PASS — Q1-Q9 are input evidence for PLAN/implementation only and must not be copied as standalone done_when.
  next: converge-verify.

  END_OF_FILE: live/health/work/converge-g-health-nutrition-system-arch.md
  END_FILE

  2) Update file: live/health/work/converge-g-health-nutrition-system.md

  Insert the following exact section immediately before the existing line "## §ROUTE":

  BEGIN_INSERT
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
  END_INSERT

  3) In live/health/work/converge-g-health-nutrition-system.md, replace the existing §ROUTE section body with:

  BEGIN_REPLACE_ROUTE_BODY
  Next: converge-verify.

  Reason:
  - The WHAT is closed and converge-arch is now closed.
  - §CONTRACTS NCA0-NCA9 cover all TREE/core/starter/training/Direction OS/future seam interactions.
  - Architecture-on-paper Q1-Q9 is closed with no open high-risk questions and no owner decision batch.
  - Do not emit executor CALL yet; verify/refutation must run first.
  END_REPLACE_ROUTE_BODY

  4) Update live/health/NOW.md:

  Replace active_bet.note with:
  BEGIN_NOTE
    2026-06-16 nutrition converge-arch closed contract/architecture-on-paper surface:
    NCA0-NCA9 cover starter seed, core attach, tracking LOG, review mutation,
    base-prep/grocery, bad-week/safety, future seam, training day_type via core,
    and Direction OS raw-data boundary. Next = converge-verify.
  END_NOTE

  Replace the entire "next: |" block with:
  BEGIN_NEXT
  next: |
    CALL c-health-nutrition-converge-verify-001
    to: session
    direction: health
    play: converge-verify
    node: g-health-nutrition-system
    goal: |
      g-health-nutrition-system contract/architecture closure is independently refuted and either
      passed clean for shape or bounced with exact blockers.
    context: |
      Read:
      - live/health/CHARTER.md
      - live/health/TREE.md
      - live/health/NOW.md
      - live/health/work/converge-g-health-nutrition-system.md
      - live/health/work/converge-g-health-nutrition-system-arch.md
      - live/health/work/converge-g-health-core.md
      - live/health/knowledge/health-core-corrected-g5-review.md
      - health-ai acceptance/core/evidence-summary.md
      - health-ai acceptance/core/matrix.json
      - health-ai core/extensions/attach-contract.md
      - health-ai core/metrics.md
      - health-ai core/profile/owner-facts.md
      - health-ai core/profile/derived-anchors.md
      - health-ai core/intake/non-blocking-questions.md
      - health-ai core/parser/materiality.md
      - health-ai core/principles/minimum-tracked-signals.md
      - health-ai core/phases.md

      Verify specifically:
      - §CONTRACTS NCA0-NCA9 cover every TREE/core/starter/training/Direction OS/future seam interaction.
      - There is no dangling current producer; future training logged day_type is correctly non-blocking.
      - Nutrition consumes core; it does not duplicate core profile, phase, metrics, parser/library/procedure, review, schema/versioning, or Direction OS boundary.
      - Mandatory tracking, tracking-to-review mutation, base-prep/reuse, grocery/prep derivation, bad-week mode, safety, and future integration seam are covered.
      - Architecture questions Q1-Q9 are closed with refuted alternatives and no open/deferred high-risk rows.
      - No HOW leakage appears in §CONTRACTS; HOW is routed to PLAN.
      - Architecture-on-paper is context-only and does not leak into executor done_when.
    boundaries: |
      Do not shape the node.
      Do not create executor CALL.
      Do not build implementation.
      Do not add UI/app/Mealie/runtime/DB/server/cron/scheduler requirements.
      Do not rewrite g-health-core.
      Do not store raw daily food/weight/photo/check-in logs in Direction OS.
      If blockers are found, return exact blockers; do not patch them silently unless they are purely mechanical wording fixes inside the verify result.
    done_when: |
      Independent verdict is pass/fail with evidence.
      Pass only if contract coverage is complete, no current producer dangles, no line cites an open WHAT/term,
      no HOW leaks into contract rows, mandatory nutrition tracking/review/base-prep semantics are covered,
      and architecture-on-paper remains input evidence only.
      If pass, next route is shape. If fail, next route is repair/converge-arch correction with exact blockers.
    return: |
      RESULT with verdict, evidence table, blocker list if any, state_changes, play_check, and next CALL.
    budget: one focused verify movement
    surface: any capable session
  END_NEXT

  5) Update live/health/LOG.md:

  Insert before END_OF_FILE:
  BEGIN_LOG_LINE
  - 2026-06-16 — health/g-health-nutrition-system converge-arch: closed §CONTRACTS NCA0-NCA9 and architecture-on-paper Q1-Q9 for nutrition module on g-health-core; no owner decision batch; no current app/UI/Mealie requirement; next converge-verify. → history/2026-06-16-s-health-nutrition-converge-arch-001.md
  END_LOG_LINE

  6) Create history file:
  - live/health/history/2026-06-16-s-health-nutrition-converge-arch-001.md
  - Content: this RESULT packet exactly.

captures:
  - Future candidate, not current scope: shape a separate app/vitrine/mirror node only after the chat-first Health AI nutrition module is implemented and verified as usable.
  - Future verifier should specifically attack NCA8 because training is parked and day_type has a planned-now/logged-later producer split.

decisions_needed: []

play_check:
  - 1 Declare: done. Consumer-driven contracts NCA0-NCA9 cover starter-kit seed, g-health-core, nutrition internal seams, future training via core, Direction OS boundary, and future integration seam; no current producer dangles; HOW routed to PLAN; owner_gate_batch=[] because contracts derive from signed WHAT/core.
  - 2 Decompose: done. Heavy node decomposed into 11 internal sub-systems; no sub-node split proposed; seams mapped to NCA rows.
  - 3 Architect: done. High-risk architecture questions Q1-Q9 closed with refuted alternatives; gap-hunt closed starter-kit seed authority risk; owner_gate_batch=[]; no open architecture rows.
  - 4 Close & route: done. contract_coverage=PASS; arch_open=0; arch_in_context_only=PASS; next=converge-verify.

log: |
  health/g-health-nutrition-system converge-arch: closed §CONTRACTS NCA0-NCA9 + §ARCH Q1-Q9; no owner decision batch; next converge-verify.

next: |
  CALL c-health-nutrition-converge-verify-001
  to: session
  direction: health
  play: converge-verify
  node: g-health-nutrition-system
  goal: |
    g-health-nutrition-system contract/architecture closure is independently refuted and either
    passed clean for shape or bounced with exact blockers.
  context: |
    Read live/health/CHARTER.md, TREE.md, NOW.md,
    live/health/work/converge-g-health-nutrition-system.md,
    live/health/work/converge-g-health-nutrition-system-arch.md,
    live/health/work/converge-g-health-core.md,
    live/health/knowledge/health-core-corrected-g5-review.md,
    and health-ai core/evidence files listed in NOW.next.
  boundaries: |
    Do not shape, do not implement, do not add UI/app/runtime requirements, do not rewrite core.
  done_when: |
    Independent pass/fail verdict with exact blockers or shape route.
  return: |
    RESULT with verdict, evidence, state_changes, play_check, and next CALL.
  budget: one focused verify movement
  surface: any capable session
END_OF_FILE: live/health/history/2026-06-16-s-health-nutrition-converge-arch-001.md
