# Life-reset — v1 Plan Audit (t-1, re-scoped)

Date: 2026-06-21
Session: s-life-reset-run-v1-t1-plan-audit-001 (play: work, node g-lr-run, task t-1)
CALL: c-life-reset-run-v1-t1-recovery-slide-001 — RE-SCOPED by live owner instruction.
Status: durable AUDIT product. The original narrated back-test was dropped by the owner as
self-graded theater ("Это нахуй не проверка, так это еботня… проверяй на консистентность
данных, на план проверяй, что всё покрыто, каждая процедура"). Replaced by a coverage +
consistency + data-flow audit of the v1 plan BEFORE building the 2 files.

Method: one multi-agent pass (workflow wf_35ccf508, 24 agents):
  1. Enumerate — required procedures/invariants from CHARTER.md (operating_model, R11/R12/R22,
     G1-G4, principles, lenses, success_criteria) + from research §3 (thin slice A-G) and §4
     (gaps); separately, what the 5 tasks + 2 files actually DELIVER (NOW.md done_when).
  2. Check — coverage (every required item → covered-by or GAP), consistency (contradictions),
     data-flow (the 4 v1 flows traced end to end).
  3. Verify — every candidate defect adversarially refuted (default = refuted unless it holds).
  4. Synthesize — build-readiness verdict + ranked fixes.

---

## Verdict: BUILD-READY (with one load-bearing fix, now applied)

- 62 required procedures/invariants — ALL covered by some task/file in the plan.
- The recovery-vs-slide rule (3 signs) + the 4 floor-tripwires — concrete enough to author
  the sealed core (t-2). Nothing missing.
- No contradictions survived refutation.
- All four v1 data-flows close: (1) week → day → day-review → weekly-review → decision →
  next week; (2) sealed-core → 4 tripwires → protect; (3) neighbor summary → integrate →
  conflict → route (no raw); (4) durable state → chat restart → delta re-entry.

## The one confirmed defect (load-bearing, safety) — FIXED

The sealed-core file (t-2) restated every runtime safety invariant EXCEPT the charter's
clinical-risk routing rule. The charter holds it (authority_and_boundaries: "При признаках
клинического риска life-reset не усиливает дисциплину и не назначает лечение, а
маршрутизирует к профессиональной поддержке"; safety lens) and the v0 dry-run carried it,
but t-2's done_when dropped it. It is distinct from the recovery carve-out — three altitudes:
  - default → treat-as-recovery (never punished);
  - fallen FLOOR → in-system PROTECT reach-in (name the falling pillar);
  - pre-named CLINICAL-RISK sign → route OUT to professional support, never intensify
    discipline or prescribe treatment (sealed class, no numbers).
The 4 v1 tripwires (sleep / not-smoking / no-binge / not-vanishing) are exactly where a
clinical sign would surface → live from run 1.

Fix applied (this RESULT):
  - t-2 goal + done_when: the sealed core must list clinical-risk routing; its specific
    signs are co-created with the owner when authoring the file (owner-content).
  - resolved_gaps.recovery_vs_slide: the THREE response altitudes recorded.
  - lens_sweep safety: clinical-risk routing restored.

## Owner real data captured (not acted on)

The owner reported a LIVE slide: binge-eating sweets after breakfast ~1.5 weeks, onset after
quitting smoking + stopping daytime strength training. Under the rule this reads as a slide
(not named-as-rest · the eating floor is down · not bounded-with-return). Preserved as the
natural real test case for t-4 (the real run). Design note: the trigger was removing TWO
pillars at once (smoking + training) — stopping a bad habit can itself destabilize.

END_OF_FILE: live/life-reset/work/life-reset-v1-plan-audit-001.md
