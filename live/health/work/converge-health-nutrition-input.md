# Converge INPUT — g-health-nutrition-system (DIRTY, first pass)

> **STATUS: UN-RATIFIED INPUT EVIDENCE. EVERYTHING HERE IS A DIRTY CANDIDATE.**
> Produced by two analysis agents in the chat that RESET this node (2026-06-13). The converge run
> must treat NOTHING here as decided — re-derive, refute, and re-confirm with the owner. Do NOT
> import any of this as born-closed. Auto-fill no answers. This exists only to save the converge
> chat from a cold start, not to pre-decide anything.

## Why the node was reset (the located trouble)
v1 (product repo health-ai, director + flat setup-gate) asked the owner **"сколько приёмов пищи в день"**
on the live test. That question sits in 4 places (`nutrition/domain.md` setup_gate, `program/domains.md`,
`SYSTEM.md` СЕТАП step, `state/preferences.md`). **Root cause (structural):** there is no typed boundary
between *owner-only facts* (must be asked) and *system-decided expert variables* (must be researched and
decided). A flat gate makes the director rationally ask the owner expert questions. Cannot be fixed by
prompt wording — it's architecture.

## The owner's bar (the standard converge must hit)
A super-professional health/nutrition agent that **researches and decides** everything expert (meals/day,
timing, macros, food choice, deficit, tracking precision) and asks the owner ONLY irreducible personal
facts — minimal, skippable. Every process deeply, professionally worked out (not a shallow prompt).
Chat-first; GitHub = single source of truth; owner never edits files. Extensible to training/water/etc.
Must not become procrastination; tracking stays light; guarded safety, non-prescriptive.

---

## Disputed-term glossary (candidates — re-confirm)
- **plan (план)** = a generated MENU CYCLE (week or 3-day, to next checkpoint); NOT the long-arc program; NOT a static diet sheet.
- **program (программа)** = the long arc (start_date, 2–3 phases ~12 wk, checkpoint dates). Keep program=arc, plan=menu-cycle.
- **menu (меню)** = the single day pulled from the active plan, re-solved if the day went off-rail. NOT a buffet of options the owner picks from.
- **tracking / log** = deliberately COARSE capture (photo/voice/text → portions, not grams). Precision level is itself an open SYSTEM question.
- **review / checkpoint** = a date/signal-triggered DECISION moment (hold / recalc / diet-break / change dishes / refresh evidence / rebuild). NOT a passive summary; NOT the strategic Direction OS review.
- **leads / "leader with brakes"** = the system DRIVES (decides routine silently); asks only on a short brakes-list. The trigger complaint = it behaved as asker, not leader.
- **preference** = owner-only fact that CANNOT be researched (dislikes, allergies, equipment, budget, real cooking-time, medical). "meals/day" is NOT a preference — that conflation is the bug.
- **setup_gate** = the minimal must-collect before a first plan — must contain ONLY true preferences.
- **fallback / "lazy food"** = pre-DESIGNED low-effort meals that still hit protein/calorie; NOT a cheat/lapse.

## The "who decides" principle (candidate — recommend ratify)
**Research-and-decide by default.** If a top professional nutritionist would decide it from evidence +
the owner's profile, the SYSTEM decides it (and records it with a one-line rationale + evidence tag).
Only genuinely personal, unresearchable facts are asked — once, briefly, skippably. Move meals/day (and
every expert parameter) OUT of the gate into the system-decided set. Asking is low-cost confirmation,
never a blocker.

---

## Candidate §WHAT question set (~67, tagged) — re-derive, don't adopt
Tags: **[SYS]** system researches+decides · **[OWN]** irreducible owner-only · **[PLAN]** implementation/HOW.

**A. Eating-pattern engine** (decompose "system decides the eating pattern")
1.[SYS] meals/day (THE trigger) · 2.[SYS] snacks (count, distinct from meals) · 3.[SYS] meal timing / eating window ·
4.[SYS] per-meal calorie distribution · 5.[SYS] per-meal protein distribution · 6.[SYS] daily calorie target + method ·
7.[SYS] deficit size (~20% fork; "too soft = adherence risk") · 8.[SYS] daily protein target (g/kg of which weight) + floor ·
9.[SYS] carb/fat split or protein+calorie only · 10.[SYS] fiber/satiety strategy · 11.[SYS] calorie floor (brakes trigger) ·
12.[SYS] hydration baseline affecting satiety (seam→water) · 13.[OWN] disliked foods · 14.[OWN] allergies/intolerances ·
15.[OWN] medical constraints/meds · 16.[OWN] budget ceiling · 17.[OWN] real cooking time/week · 18.[OWN] equipment (known) ·
19.[SYS] food/dish SELECTION from 13–18 · 20.[PLAN] display units (grams/portions/hand).

**B. Weekly/3-day menu-cycle** (decompose "plan")
21.[SYS] horizon week vs 3-day + rule (to next checkpoint) · 22.[SYS] variety vs repetition policy · 23.[SYS] meal-prep/batch to equipment ·
24.[SYS] count+selection of fallback meals (≥1) · 25.[SYS] shopping-list generation (seam→shopping) · 26.[SYS] leftovers roll-forward ·
27.[SYS] re-solve rule when a day goes off-plan · 28.[PLAN] active-plan artifact shape · 29.[PLAN] mirror to app (HomeLab/recipe).

**C. Food-logging / tracking** (decompose "log by photo/voice/text")
30.[SYS] minimum sufficient precision (coarse/grams/photo) — evidence gap · 31.[SYS] WHAT must be logged (weight? meals? protein? deviations?) ·
32.[SYS] cadence + what counts as "slipped" · 33.[SYS] confidence-tagging → checkpoint · 34.[SYS] max clarifying Qs per log (aim ~0) ·
35.[SYS] same-day corrective-advice rule · 36.[OWN] sustainable weigh-in cadence · 37.[PLAN] capture plumbing (photo/voice vendor).

**D. Checkpoint-review** (decompose "checkpoint")
38.[SYS] cadence (weekly + cycle?) · 39.[SYS] off-schedule trigger set (signal/slip/pain/absence) · 40.[SYS] inputs + moving-average window ·
41.[SYS] decision menu + rule per branch · 42.[SYS] recalc trigger (~5 kg vs time vs stall) · 43.[SYS] diet-break cadence (gap) ·
44.[SYS] plateau diagnosis order (intake-creep first) · 45.[SYS] upward-to-Direction-OS = summary/decision only · 46.[SYS] re-onboard after absence (soft restart).

**E. Long-arc program** (decompose "setup/program")
47.[SYS] phase structure (2–3 / ~12 wk; phase-1 = prove the system) + done_when · 48.[SYS] first-milestone target (−5–10%/−8–12 kg) ·
49.[SYS] maintenance-phase design (regain is default) · 50.[SYS] maintenance-vs-regain predictors (gap) · 51.[OWN] "старт" trigger + hard calendar constraints.

**F. Decide-vs-ask boundary** (decompose "leader with brakes")
52.[SYS] explicit silent-decision list (= the "professional" definition) · 53.[OWN] brakes-list needing "ok" (↑intensity, below floor, sharp course change, safety) ·
54.[SYS] when to research vs use stored evidence base · 55.[SYS] honesty: 📊/⚠️/🔲 tags into owner-facing advice.

**G. Safety & medical** (charter: safety > pace)
56.[SYS] calorie floor + red-flag list (gap) · 57.[SYS] red-flag → stop-and-see-doctor; no diagnosis/prescription · 58.[SYS] "bad-week minimum" nutrition protocol.

**H. Persistence / chat-first / source-of-truth**
59.[SYS/PLAN] write-back path: chat action → GitHub WITHOUT owner editing files (the central unbuilt mechanism) · 60.[SYS] context-continuity from GitHub (no chat-memory dependence) ·
61.[SYS] Direction-OS boundary: no raw daily data leaks · 62.[PLAN] connector specifics (ChatGPT/Claude, GitHub vs upload).

**I. Extensibility seams**
63.[SYS] recipe sub-system contract · 64.[SYS] recurring nutrition jobs ("new dish Tuesdays", refresh fallbacks, recipes-from-home-food, low-time week) + triggers ·
65.[SYS/PLAN] shopping-list domain seam · 66.[OWN/SYS] training↔nutrition coupling (protein/calorie supports parallel strength) · 67.[PLAN] new-domain mechanism (folder + registry line).

---

## Candidate architectures (refute in converge-arch — do NOT adopt)
- **A. Current** (fat SYSTEM.md director prompt + spine + domain modules + evidence-base). **Mechanically rejected** on research-and-decide: flat gate structurally forces asking meals/day.
- **B. Generated plan artifact** ("compile, then run"): heavy decide-pass at старт/checkpoint emits a dated program artifact; day-to-day is lookup. Survives.
- **C. Per-process spec files** (thin router + rich versioned process specs, like Direction OS plays). Strongest, auditable depth. Survives.
- **D. Periodic research/refresh job** (needs always-on runtime). **Rejected** — v1 forbids a runtime.
- **E. Hybrid (RECOMMENDED candidate):** (1) typed split `personal-facts` (only askable) vs `decided-variables` (system decides + records rationale + evidence tag) — the **non-negotiable core fix**; (2) generated plan artifact (depth + kills per-chat drift); (3) thin per-process depth specs + SYSTEM.md as router. Evolve the existing repo, keep evidence-base + spine. Minimal fallback = change (1) only.

## High-risk architecture questions for converge-arch (candidates)
1. **The boundary RULE (crux):** exact membership test for personal-fact vs decided-variable (e.g. is cooking-time a personal constraint or a decided cadence?).
2. Artifact vs live-decision split: which decisions freeze into the plan artifact vs decided live each chat.
3. Regen trigger + cost (anti-procrastination guard): what triggers a plan regeneration and how to keep it cheap.
4. Spec depth vs sprawl: per-spec depth contract + cap on spec count per domain.
5. Extension recursion: does a new domain (training) get its own artifact+decided-variables+specs, or share nutrition's? Is nutrition genuinely the reusable template?
6. Where the safety gate lives under the split: a non-overridable safety layer the decide-pass cannot relax.
7. now.md cache vs artifact authority: source-of-truth precedence (program → artifact → now-cache) and drift healing.

## Open evidence-base gaps (round-2 research inside converge)
- minimum sufficient tracking precision · maintenance-vs-regain predictors (NWCR primary lit) · calorie floor + full red-flag list · optimal recalc / diet-break cadence over 18–30 mo.

END_OF_FILE: live/health/work/converge-health-nutrition-input.md
