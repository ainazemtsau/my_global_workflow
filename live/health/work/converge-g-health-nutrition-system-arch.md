---
# Converge-Arch — g-health-nutrition-system

> Produced by converge-arch session s-health-nutrition-converge-arch-001 on 2026-06-16.
> Writer-safe repaired by c-health-nutrition-converge-arch-writer-repair-001 on 2026-06-16 after writer bounce.
> Assembly surface only; not a Direction OS state file.
> Authority: signed nutrition WHAT in `live/health/work/converge-g-health-nutrition-system.md`
> + file-backed g-health-core evidence/history.
> Status: CLOSED ARCH, route to converge-verify.

## §READ / EVIDENCE

- E1 — Nutrition WHAT is signed and closed in `live/health/work/converge-g-health-nutrition-system.md`.
- E2 — Core corrected G5 binding is imported from file-backed evidence, not CALL-only import:
  `live/health/knowledge/health-core-corrected-g5-review.md`, corresponding history RESULT,
  and Health AI core evidence files (`acceptance/core/evidence-summary.md`,
  `acceptance/core/matrix.json`).
- E3 — Core attach contract: modules read `phase`, `week`, `day`, `weight_trend`,
  `adherence`, `biofeedback`; modules write only namespaced `x_<domain>_*` fields and never
  redefine core concepts.
- E4 — Core procedure template contract: procedures are declarative and never self-schedule;
  they run only when invoked by an operator.
- E5 — Core `day_type` file is a provenance contract only: a logged override beats a planned
  fallback when deriving coarse `day_type`; no nutrition target is implemented in core.
- E6 — Boundaries remain unchanged: no current vitrine/Mealie/UI/app/runtime/DB/server/cron/
  scheduler requirement; no Direction OS raw nutrition diary; no g-health-core rewrite.

## §BOUNDARIES

- Nutrition is an additive Health AI module on g-health-core.
- Nutrition consumes core profile, phase, week, day, metric/provenance, parse/materiality,
  procedure-template, schema/versioning, and attach surfaces.
- Nutrition writes only nutrition-namespaced artifacts/fields.
- Direction OS may hold strategy/artifacts but does not store raw daily food, weight,
  photo, or check-in logs.
- No current external app/vitrine/Mealie/Notion/UI/image-sync/shopping-app dependency.
- No runtime, DB, server, cron, scheduler, or automatic background job is required by this
  architecture surface.
- Nutrition does not diagnose, prescribe medically, or silently continue unsafe progression.

## §CONTRACTS

Status legend: all rows are `answered`.

### NCA0 — Starter-kit seed intake

status: answered

contract: |
  Nutrition may collect and normalize a starter-kit seed of nutrition owner facts only:
  allergies/intolerances, medical constraints/meds if owner-known, ethical/religious exclusions,
  hard dislikes, budget, cooking time, equipment, schedule constraints, household/social constraints,
  and sustainable tracking capacity.

acceptance: |
  The seed never asks expert variables as owner preferences. Meals/day, timing, macros, deficit,
  protein strategy, food selection, tracking precision, and review cadence are system-decided from
  evidence + owner facts + core profile/phase/metrics/feedback. Missing owner facts stay pending,
  reduced-mode, or documented revisable defaults where safe.

rejects: |
  "Tell me how many meals per day you want" as mandatory setup; fabricated owner facts; blocking
  first cycle because non-material owner facts are missing.

### NCA1 — Core attach / nutrition namespace

status: answered

contract: |
  Nutrition attaches as one Health AI domain/module over g-health-core. It reads core-owned shared
  concepts and writes only nutrition-namespaced artifacts/fields such as `x_nutrition_*`.

acceptance: |
  A future executor can add nutrition without editing core-owned concept definitions. Core remains
  authority for `phase`, `week`, `day`, `weight_trend`, `adherence`, `biofeedback`, parse/materiality,
  procedure template, schema/versioning, and attach contract.

rejects: |
  Standalone nutrition system that redefines profile, phase, metrics, review, logs, or core procedures.

### NCA2 — Personalized nutrition cycle derivation

status: answered

contract: |
  Nutrition produces an active nutrition cycle by resolving owner facts + core profile/phase/metrics
  + system-decided nutrition variables into menu-cycle/eating-plan, recipes/instructions, base-prep,
  grocery needs, fallback meals, tracking instructions, and review cadence.

acceptance: |
  First cycle is personalized and explains which owner facts/core facts/system decisions shaped it.
  It is not a generic diet sheet or quick menu detached from profile/process.

rejects: |
  Static diet forever; buffet of options the owner must manually choose; generic first menu without
  setup/run/review loop.

### NCA3 — Nutrition LOG / low-friction tracking

status: answered

contract: |
  Nutrition tracking lives in Health AI nutrition namespace as LOG entries sufficient for review:
  planned-vs-actual, substitutions, fallback use, skipped/off-plan events, rough food/portion
  descriptions, uncertainty/confidence, hunger/satiety, friction, and materially necessary estimates.

acceptance: |
  Owner can log via rough text/voice/photo. The system records confidence, asks only material
  non-blocking clarifiers, proceeds with safe/default estimates on non-answer, and does not require
  gram-level logging by default.

rejects: |
  Direction OS food diary; mandatory precise macro logging; tracking hidden inside review summary.

### NCA4 — LOG-to-review mutation path

status: answered

contract: |
  Nutrition review consumes nutrition LOGs + owner feedback + core metrics/phase/biofeedback/
  adherence and emits explicit decisions: hold, mutate dishes, rebuild menu-cycle, update fallback,
  update prep/base-prep/grocery rules, refresh evidence, or propose a braked change.

acceptance: |
  Hunger, prep friction, frequent fallback, off-plan pattern, disliked foods, poor adherence, bad
  body outcome, or safety signal produces a concrete artifact mutation/hold/rebuild/refresh/brake
  decision. Artifact mutation is part of the nutrition system, not a passive note.

rejects: |
  Review as passive summary; raw daily diary export to Direction OS; unreviewed drift.

### NCA5 — Recipes, base-prep/reuse, grocery correctness

status: answered

contract: |
  Recipes/instructions are executable process building blocks. They must represent ingredients,
  quantities or usable approximations, substitutions, equipment, time/friction notes, base-prep
  components, yields, reuse links, grocery derivation, and relation to menu/fallback/prep.

acceptance: |
  One shared prepared component can feed multiple meals without double-counting or omitting prep/
  grocery needs. Grocery/prep derivation must remain true when recipe instances reuse a base-prep
  batch.

rejects: |
  Vague prose-only recipe; treating every recipe as isolated; external recipe/shopping app as current
  authority.

### NCA6 — Bad-week mode and safety interaction

status: answered

contract: |
  Nutrition has a reduced bad-week mode with valid fallback/lazy-food minimums and relaxed-but-nonzero
  tracking. Safety flags or unsafe deterioration halt progression or switch to conservative mode and
  use non-diagnostic medical-check language.

acceptance: |
  Bad-week execution stays inside the nutrition process. Red flags cannot silently continue aggressive
  deficit or unsafe progression.

rejects: |
  Bad week as total system failure; cheat/free-for-all fallback; medical diagnosis/prescription.

### NCA7 — Future integration seam

status: answered

contract: |
  Nutrition artifacts are structured enough to be mirrored later by a vitrine/app/recipe/shopping/image
  surface, but Health AI nutrition remains canonical now and no external UI/app is required.

acceptance: |
  Executor/shape may not make current success depend on Mealie, Notion, recipe app, shopping-list app,
  weekly-menu UI, image sync, recipe-image generation, runtime, DB, server, cron, or scheduler.

rejects: |
  Chat-only dead end; current app/vitrine dependency.

### NCA8 — Regular nutrition procedure extension points

status: answered

contract: |
  Recurring/bounded nutrition procedures, if needed, are nutrition-namespaced declarative procedure
  specs conforming to core procedure template: purpose, trigger, inputs, stop condition, files it may
  touch, and files it must not touch. They run only when invoked by an operator.

acceptance: |
  Nutrition may define procedures such as cycle setup, review, grocery/prep derivation, or bad-week
  fallback refresh as operator-invoked seams. No procedure self-schedules; no runtime, cron, scheduler,
  background worker, server, DB, or automation loop is introduced by this architecture.

rejects: |
  Scheduler/runtime requirement; autonomous recurring jobs; rewriting core procedure template.

### NCA9 — day_type provenance, cross-module coupling, Direction OS visibility

status: answered

contract: |
  Core provides only day_type provenance: logged override beats planned fallback when deriving coarse
  `day_type`. Core does not own nutrition targets. Nutrition owns any future `x_nutrition_day_type`
  or `x_nutrition_target` if needed, and it must derive them through core provenance/attach surfaces
  rather than redefining core. Direction OS may read accepted artifacts/evidence for strategy but does
  not store raw nutrition logs.

acceptance: |
  Training/nutrition coupling, if later needed, travels through core-owned provenance/shared concepts
  and nutrition-namespaced fields only. No core nutrition target is implied. No raw daily nutrition data
  is duplicated into Direction OS.

rejects: |
  Core-owned nutrition day_type target; direct nutrition-training private coupling outside core;
  Direction OS as food log store.

## §ARCH DECISIONS

Q1. Nutrition source-of-truth
answer: |
  Health AI nutrition namespace/module is canonical for nutrition artifacts. Direction OS is strategy/
  review surface only. External apps may mirror later but are not authority now.
closes: W1, W12, W13, NCA1, NCA7, NCA9.

Q2. Owner facts vs expert variables
answer: |
  Owner facts are irreducible and non-blocking. Expert variables are system-decided from evidence +
  profile + feedback; missing owner facts create pending/reduced/default state where safe.
closes: W3, W4, NCA0, NCA2.

Q3. Personalized run loop
answer: |
  Active nutrition cycle loop is setup seed -> system decisions -> menu-cycle -> recipes/base-prep/
  grocery -> LOG/tracking -> review mutation.
closes: W4, W5, W8, W9, NCA2, NCA3, NCA4.

Q4. Tracking LOG shape
answer: |
  LOG entries are low-friction and review-sufficient, not maximal diaries. Confidence/materiality
  controls clarifiers and estimates.
closes: W8, NCA3.

Q5. Review mutation
answer: |
  Review must emit hold/mutate/rebuild/update/refresh/brake decisions that point to concrete nutrition
  artifacts.
closes: W9, NCA4.

Q6. Recipes/base-prep/grocery semantics
answer: |
  Recipes are structured process blocks with base-prep/yield/reuse/grocery derivation semantics.
closes: W6, W7, NCA5.

Q7. Bad-week and safety
answer: |
  Bad-week mode is reduced but valid; safety flags halt/switch conservative and surface non-diagnostic
  medical-check language.
closes: W10, W11, NCA6.

Q8. Procedure extension points
answer: |
  Regular nutrition procedures are declarative, nutrition-namespaced, and operator-invoked only. Core
  provides the reusable template; nutrition supplies domain-specific triggers/inputs/stop conditions/
  file boundaries.
closes: extension-points coverage, NCA8.

Q9. day_type / target ownership
answer: |
  Core provides provenance only. Nutrition owns any later nutrition target/day_type under
  `x_nutrition_*`; it must not move nutrition target semantics into core.
closes: B3, NCA9.

## §BLOCKER REPAIR

| blocker | corrected closure | rejected/conflicting reading |
|---|---|---|
| B1 — core review binding | Core corrected G5 is imported from file-backed knowledge/history/product evidence, not CALL-only assertion. | "Trust the CALL because the file was unavailable." |
| B2 — regular nutrition procedure extension points | Covered by core procedure template plus nutrition operator-invoked procedure seam. | Scheduler/runtime/cron/background recurring nutrition process. |
| B3 — day_type wording | Core provides provenance only; nutrition owns any later namespaced `x_nutrition_day_type` / `x_nutrition_target`. | Core-owned nutrition target or training/nutrition coupling outside core. |

## §COVERAGE

Signed WHAT coverage:
- W1 source-of-truth -> NCA1, NCA7, NCA9.
- W2 core attach -> NCA1, NCA9.
- W3 expert-variable boundary -> NCA0, NCA2.
- W4 personalized first process -> NCA2.
- W5 practical outputs -> NCA2, NCA5, NCA7.
- W6 detailed recipes -> NCA5.
- W7 base-prep/reuse correctness -> NCA5.
- W8 nutrition tracking -> NCA3.
- W9 tracking-to-review mutation -> NCA4.
- W10 bad-week mode -> NCA6.
- W11 safety boundary -> NCA6.
- W12 no current vitrine/app requirement -> NCA7.
- W13 future integration seam -> NCA7.

Core edge coverage:
- namespaced additive attach -> NCA1.
- core shared concepts consumed, not duplicated -> NCA1, NCA9.
- procedure/template extension points -> NCA8.
- day_type provenance only -> NCA9.
- raw data boundary -> NCA3, NCA9.

## §OPEN / DEFERRED CHECK

open rows: 0
deferred rows: 0
blocker rows: 0
owner decisions needed: 0

## §ROUTE

Next: converge-verify.

Reason:
- WHAT is closed and architecture/contract surface is closed on paper.
- Corrected B1-B3 are now stated in mechanically checkable terms.
- Verification must try to refute the architecture closure before any executor CALL.

---

END_OF_FILE: live/health/work/converge-g-health-nutrition-system-arch.md
