# Health CORE — best-practice recon research (INPUT EVIDENCE — decides nothing)

> Reconnaissance for re-architecting g-health-core. Produced 2026-06-14 by a 7-agent web-research
> workflow (real sources cited). This is INPUT EVIDENCE for the core converge — refute/confirm,
> import nothing as authority, auto-fill no answers. Separates evidence-based practice from marketing.

## Transferable patterns (tagged: core / nutrition / training / cross-module · confidence)

**[core, high] Anchors-vs-derived (the keystone + the v1 fix).** A `profile`/anchors file holds
durable owner FACTS (sex, height, current/goal weight, protect-strength) separately from system-derived
ANCHORS (estimated expenditure, per-lift training-max/e1RM, protein g/kg + chosen reference weight,
target rate-of-change). All daily numbers are FORMULAS off the anchors; revision = editing a few anchors.
This split is the cleanest structural fix for the v1 defect — it forces a typed boundary between
owner-only facts and system-decided variables.

**[core, high] PLANNED vs LOGGED as two file families.** Plan/program/template holds intent (ranges, %,
RPE, target macros), edited rarely; the dated log holds actuals, append-only. Never overwrite the plan to
record a result. Adherence and trends are DERIVED at read time, never stored as source-of-truth → review
is a no-mutation reconciliation (IaC/Beancount desired-vs-observed). Conflating the two is "the most
common modeling mistake."

**[core, high] Trend weight via 7-day / exponential moving average.** Store RAW daily readings; derive the
trend on read; never act on a single reading (daily ±1–2.5 kg noise dwarfs ~0.5–1 kg/wk real change).
Deterministic, reproducible across providers. The single metric BOTH modules consume.

**[core, high] Adaptive (back-calculated) expenditure.** Treat TDEE as an unknown solved from logged
intake + smoothed weight trend (expenditure = intake ± stored-energy-change, ~7700 kcal/kg), recalibrated
at review cadence — never a static formula. Public arithmetic; the two inputs are exactly what a
file-based system already holds. Self-corrects for metabolic adaptation over a 125→90 kg cut.

**[core, high] Reference-by-stable-ID + definition library.** Foods/exercises each defined once with
structured fields (per-100g for food), plan and log point by slug + quantity; namespaced extension keys
(`x_<domain>_*`) keep the core schema tiny → "new domain = 1 folder + 1 registry line." Gives the LLM a
closed vocabulary to match against (sharply reduces hallucinated values).

**[core, high] Append-only dated log as system of record.** One file per day (YYYY-MM-DD); process by the
entry's date field, not file position; corrections are new dated entries; git is the audit trail.
Append-only is the most reliable LLM write (no clobbering/line-drift).

**[core, high] Value-type grammar reused by every leaf field.** `fixed{value,unit}` | `range{min,max,unit}`
| `relative{pct, of:<anchor>}` | `amrap`, with a constrained unit vocabulary. Sparse "only the keys that
apply" maps are what an LLM emits/parses reliably and what lets one schema serve lifting, timed, cardio, food.

**[core, high] Three autonomy levels (Coached / Collaborative / Manual).** The SAME engine PROPOSES
adjustments at a cadence and requires explicit ratification before the targets file changes; guardrails
(calorie/protein floors, min fat) are declarative pre-checks. Each applied change is a dated git diff →
file history IS the check-in log. The autonomy level is a config flag for how much the review may auto-apply.

**[core, high] Consistency-of-logging as a first-class derived metric.** Days logged, days with ≥2 eating
occasions, % targets met. Combined RCT analysis: "days tracking ≥2 eating occasions" explained the most
variance in 6-month weight loss (R²=0.27) — more than completeness/accuracy. Justifies the low-friction
NL-logging thesis: optimize for logging SOMETHING daily.

**[core, high] Tiered metric cadence (signal-vs-noise).** Daily (weight, intake, subjective 0–5
sleep/energy/hunger/stress, steps), weekly (avg weight, circumference), monthly (photos, full
measurements). Subjective 0–5 biofeedback is what coaches use and is trivial YAML; objective
HRV/readiness was NOT independently validated (WHOOP-marketing-dominated) → exclude until separately researched.

**[core, high] Plain MD/YAML in git + AGENTS.md-style conventions = provider-independence.** The lowest
common denominator across ChatGPT/Claude/Claude Code/Codex is reading/writing UTF-8 Markdown + ingesting
text+images. Every rule/schema/convention lives in plain Markdown (AGENTS.md is an open standard, read
natively by Codex/Cursor/Aider, fallback in Claude Code), zero reliance on proprietary memory/threads/
vector store. The durable asset is the files; the agent is swappable.

**[core, high] Robust-edit discipline (YAML is the riskiest surface).** Prefer append over in-place edit;
one entity per small file; quote string scalars; keep frontmatter shallow/flat; target by stable
anchor/heading not line number; parse/lint after write before commit. (Unquoted scalars coerce silently:
no→false, 1.0→float, bare date→date.)

**[cross-module, high] PARSE vs VALUES firewall.** The LLM parses messy NL/voice/photo into a PROPOSED
structured draft and maps each item to a real food/exercise entry; numbers come from files; the human
ratifies before the entry is written. Raw photo→calorie is still beta (image-only MAPE ~30%; +text
description ~14%). The active program/menu is a strong disambiguation signal. Directly fixes the v1
over-asking defect.

**[cross-module, high] Clarify-only-on-material-ambiguity.** Log a best-effort entry silently when
confident; ask only when interpretations genuinely diverge AND the gap is nutritionally material; portion
question first (empirical gap order: portion ~34%, food-type ~32%, prep ~20%). SnappyMeal: unnecessary
questions were the main usability complaint and follow-ups can DEGRADE accuracy.

**[cross-module, high] Program-as-relative-prescription parameterized by a stored anchor.** Training Max /
TDEE / bodyweight + a documented progression rule; daily concrete numbers resolved on read; revision =
editing a few anchors, not rewriting every day. (5/3/1 stores ONE TM per lift; Liftosaur Liftoscript is a
working flat-text program+progression DSL — the LLM is the runtime.) Maps 1:1 to nutrition.

**[cross-module, high] Phase as a first-class shared lever.** cut/maintain/build/deload/diet-break carried
as plan metadata, gating BOTH modules' targets; day-log frontmatter back-references {phase, week, day}.
This is where the genuine nutrition↔training contract lives at low frequency.

**[cross-module, high] Carb-with-training-load = the one genuine high-frequency cross-link.** A coarse
day_type tag (rest/easy/moderate/hard) from the training session sets that day's carb target. Keep COARSE
(a few tiers), not per-minute timing (the 30-min "anabolic window" is largely myth for once-daily trainees).

**[nutrition, high] Energy decoupled from macro derivation; protein anchored absolutely; nutrients as
{min,max} bands.** Protein g/kg fixed, carbs/fat as the energy remainder (4/4/9 constants → deterministic).
One weekly energy change cascades without re-specifying everything.

**[nutrition, high] Protein ~1.6–2.4 g/kg held high through the deficit (~2.0–2.4 g/kg of goal/lean weight)
to preserve strength.** Peer-reviewed (2.3 g/kg lost ~0.3 kg muscle vs 1.6 kg at 1.0 g/kg). CAVEAT: at 125
kg targeting 90 kg, anchoring to full current bodyweight over-prescribes — goal/lean weight is
literature-consistent (a real decision, not a default).

**[nutrition, high] Canonical per-100g food record + portion multiplier.** food_id × grams scaled
arithmetically; values from USDA FDC, never invented. Obsidian Food Tracker is a working flat-file proof.

**[nutrition, high] Confidence + source metadata on every parsed estimate.** `estimate_confidence:
low|med|high`, `source: photo|photo+desc|text|barcode|verified-db`. Calories+protein are the trusted
fields; carb/fat softer. Lets the review resurface low-confidence days.

**[training, high] e1RM as the per-lift strength state variable** (Epley/Brzycki/RPE table). Converts noisy
weight×reps into one comparable number; a drop in working-set performance is often the fastest readable
sign the cut is too aggressive (serves "protect strength"). Round to plate increments.

**[training, medium] Progression keys off WORK ACTUALLY DONE (last log), not the calendar** — so missed
sessions need no special handling. Readiness (sleep/soreness) is a small daily nudge.

**[training, medium] Competing progression engines** to choose among in the (later) training converge:
AMRAP-driven training-max blocks (5/3/1 — one anchor/lift, simplest) vs volume-landmark+RIR-ramp (RP —
richer but population-estimate numbers, unpublished algorithm, RIR unreliable for novices) vs per-muscle
recovery (Fitbod — proprietary). Not a default.

## Core implications (what the core must support)
- A PROFILE/ANCHORS file as the compute root (owner-facts typed separately from derived anchors).
- PLANNED-vs-LOGGED and TEMPLATE-vs-INSTANTIATION as separate file families; adherence/trends derived, never stored.
- Core OWNS the shared metrics (raw weight series→trend, biofeedback 0–5, adherence), not the modules.
- A PHASE concept as a first-class shared lever; carb-by-day_type as the one coarse high-frequency link.
- A tiny VALUE-TYPE grammar + constrained unit vocabulary reused by every leaf field.
- PARSE-vs-VALUES firewall + clarify-on-material-ambiguity for NL/voice/photo input.
- A definition LIBRARY (foods/, exercises/) by stable slug + namespaced extension keys.
- REVIEW that PROPOSES changes (rationale + rule cited) and requires ratification; declarative guardrails;
  a minimum-data rule (never re-issue targets faster than the ~2–3 wk window the expenditure estimate needs).
- Storage as a corruption-control surface (append-only, one-entity-per-file, shallow/quoted YAML, lint-before-commit).
- All conventions in plain Markdown (AGENTS.md/CLAUDE.md style); thin always-loaded index + lazy load.

## Program/tracking model sketch (ILLUSTRATIVE — for the converge to refute/confirm)
Two file families: dateless PLAN/definitions vs dated append-only LOGS. Markdown body for humans; shallow,
quoted YAML frontmatter for the structured leaves.
- `profile.md` — owner_facts (asked once) + derived_anchors (system-decided, updated only at review with rationale).
- `programs/<id>.md` — PLAN: phases, per-phase decision_interval_days, targets as fixed/range/remainder, guardrails.
- `foods/<slug>.md` — per-100g canonical, source id (USDA-FDC-...), portions.
- `log/YYYY-MM-DD.md` — observed: body_weight (raw), biofeedback, day_type, nutrition entries (food×grams,
  source, estimate_confidence, confirmed), training sets (weight/reps/rpe). Append-only.
- `reviews/<week-id>.md` — no-mutation reconciliation: trend weight, weekly slope vs target, inferred
  expenditure, adherence %, proposed_changes (each owner_approval_required, status pending).
Shared shape both domains: anchor/definition → prescription(plan) → resolved-on-read day → logged actual →
review reconciliation. Daily totals = sum of scaled nutrients; e1RM/volume/trend/adherence all DERIVED.

## Provider-independence notes
(1) Every rule/schema in plain Markdown (AGENTS.md/CLAUDE.md), zero proprietary memory/runtime. (2)
Determinism via numbers-in-files + arithmetic-in-documented-formulas (per-100g×grams, 4/4/9, 7-day EMA,
energy back-calc ~7700 kcal/kg, e1RM, %-of-anchor) → two providers reading the same files reach the same
answer. (3) A constrained documented vocabulary is mandatory (value-type grammar, unit enum, stable
slug/ID convention pinned in core docs, RPE half-point enum, namespaced extension keys). (4) Git as the
cross-provider audit/sync layer; append-only + small files = corruption-safe writes. (5) Residual risks to
name (not assume away): AGENTS.md discovery/auto-load differs per tool (put convention in file CONTENT,
never assume auto-load); YAML coercion/indentation is the weakest write surface; single-writer assumption
breaks if two providers write the same file concurrently. Keep the instruction file instruction-dense (~150–300).

## Review cadence findings
Dominant pattern: LOG daily, DECIDE weekly. A week is the shortest window over which trend noise cancels;
daily reaction is discouraged (whipsaw). BUT cadence should be PER-PROGRAM/PER-PHASE, not globally fixed
(cut at 0.5–1%/wk → weekly decisions fine; deload/lean-gain → biweekly–monthly is honest). Adjustment is a
rate-deviation rule, not a calendar tick: change a lever only when observed slope deviates from target_rate
beyond noise AND persists N weeks. The expenditure engine needs ~2–3 weeks of consistent logging before its
estimate stabilizes; never re-issue targets faster (the classic failure of naive "adaptive" logic). The
"100–200 kcal cut after ~3 stalled weeks" step is a practitioner heuristic ("plausible"), not a cited RCT.

## Open questions for the core converge
1. Protein reference weight — current (125) / goal (90) / estimated lean mass? (full-bodyweight over-prescribes; needs a lean-mass estimate, then owner ratifies).
2. Autonomy level (coached/collaborative/manual) — how much may the weekly review auto-apply vs only propose?
3. Template-as-source vs materialized dated day-files — resolve-on-read (recommended for flat files) or generate days at program start? Determines the whole file layout and missed-session/edit semantics.
4. Day-level cross-module coupling depth — how coarse the carb-by-day_type link; day_type from PLANNED or LOGGED training; any other high-frequency flow worth modeling?
5. Food/exercise DB seeding & provenance — USDA FDC as authoritative seed; grow the foods/ library lazily from recurring foods; how barcodes/labels become new entries; the concrete FDC field-level schema.
6. Photo→nutrition trust boundary — confirm the firewall; is a low-confidence photo entry recorded-with-flag or always triggers one portion question?
7. Objective recovery metrics (HRV/RHR/sleep-device) — deferred (marketing-dominated evidence); decide whether to scope in at all (needs a separate clean-evidence pass).
8. Concurrent-write / merge-conflict policy — locking/partitioning if two providers ever write the same files concurrently (low urgency for a solo owner).
9. Decision-cadence policy — confirm weekly default for the cut; define per-phase decision_interval, multi-week confirmation count N, rate-deviation threshold, minimum-data window; which are owner-signed vs HOW→PLAN.
10. Self-extensibility mechanism — how a new global procedure is authored via workflow and registered (the R13 requirement); what the procedure-definition contract is.

## Key sources
- MacroFactor adaptive expenditure & AI logging: macrofactor.com/algorithm-accuracy/, macrofactorapp.com/expenditure-v3/, help.macrofactorapp.com (food logging, program styles)
- Cronometer nutrient targets (ratio/fixed/remainder, min/max): support.cronometer.com
- USDA FoodData Central (per-100g canonical): fdc.nal.usda.gov/data-documentation.html, /api-spec
- Protein in a deficit (peer-reviewed): examine.com/guides/protein-intake/, ncbi.nlm.nih.gov/pmc/articles/PMC5522839/
- Hevy OpenAPI (training entity model) & Liftosaur Liftoscript (flat-text program DSL): github hevy-mcp openapi-spec, liftosaur.com/doc/liftoscript
- Wendler 5/3/1 anchor+percentage: typeatraining.com, arvo.guru/resources/methods/wendler-531
- OpenSet/OpenWeight open formats (planned-vs-logged, value-types): openset.dev/docs/spec/set-dimensions, medium @radupana OpenWeight
- RIR/RPE autoregulation & deload (peer-reviewed): pmc PMC7575491, PMC10948666, frontiersin 2022.1073223
- Daily weighing / trend weight / self-monitoring (RCT/cohort/review): pubmed 25683820, pmc PMC8277333, pubmed 31155473, rippedbody.com/diet-progress-tracking/
- SnappyMeal multimodal capture / clarify-when-necessary / confidence: arxiv 2511.03907v1, aclanthology 2025.findings-naacl.306, pmc PMC12513282
- Flat-file / local-first / agent-managed files: obsidianstats.com/plugins/food-tracker, beancount.io/docs, inkandswitch.com/essay/local-first/, agents.md, sumitgouthaman.com file-editing-for-llms
- Cross-domain energy balance / carb periodization / deload nutrition / RED-S: pmc PMC5596471, PMC5889771, PMC5477153, strongerbyscience.com/metabolic-adaptation/

END_OF_FILE: live/health/work/health-core-recon-research.md
