# DRAFT CALL c-exec-023 — Sc-kernel: SPARSE TICK KERNEL / ACTIVE-FRONT ITERATION (ENGINE-ONLY)

> ⚠ **DRAFT (2026-07-02, s-repair-review-reconcile-001).** Fires ONLY after: (1) owner signs
> d-sparse-tick-kernel-001 «да»; (2) Sc-rep passes fresh G5 + owner-eye and merges dev→main. At framing this
> draft gets the standard adversarial hardening pass (like c-018/c-021/c-022) — it is a solid draft, not a
> hardened CALL. Slice position: AFTER Sc-rep, BEFORE Sc-reactions (c-exec-021 stays HELD behind it).

Direction: indie-game-development / g-9c41 / Sc-kernel. Base = post-Sc-rep-merge GasCoopGame `main`.
Executor: a FRESH `C:\projects\Unity\GasCoopGame_dev` session. Opens with a PLAN (**owner present — the
c-exec-022 deviation must not repeat**). Canon = knowledge/g9c41-gas-engine-SPEC.md (Факт-4 «главная экономия —
sparse-awake через активный фронт»; §6 п.3 hangar; Факт-1 weakest-peer CPU; ADR-0002 determinism).
Evidence base = docs/measurements/sc-rep-hangar-real-measurement-2026-07-02.md (dev @8db3ee1) +
docs/measurements/c-exec-014-benchmark-readout.md (its point 2 already named this «the #1 optimization»).

## why (measured, not argued)

Sc-rep delivered the sparse-dominant STORE but the tick kernel still expands it into dense per-species planes
every tick (`OldMassScratch`/`CopyPlane` over ALL cells per REGISTERED species → dense face-flow over all open
faces per species → `ReplaceFromPlaneMassesValidated` rebuild). Measured cost ∝ roster × domain cells,
independent of actual gas: hangar (196,608 cells, 1,562 active) = 18 ms/tick @roster-1 → 587 ms @roster-64
(~9 ms per registered type); roster-128 ≈ 1.16 s vs the 50–100 ms tick budget; weak peer 2–4× worse. This
breaks the lockstep weakest-peer premise (Факт-1) before reactions/typing add their own cost.

## goal (outcome, not method)

The authoritative tick computes over the SPARSE store / ACTIVE cells directly: per-tick cost scales with
ACTIVE cells (+ their open faces + bounded co-resident types), NOT with registered roster × domain cells.
Behavior byte-identical to the post-Sc-rep goldens. Determinism preserved (ADR-0002). ENGINE-ONLY.

**approach token = `active-front-tick-kernel-over-sparse-store` (no per-tick dense plane expansion on the
authoritative path).** Keeping the dense expand/rebuild round-trip as the authority = approach substitution →
STOP-escalate.

## done_when (verifiable; PLAN, owner present, decides the exact kernel shape)

1. **PLAN (owner present):** §Re-sync contract at tip; ingest SPEC Факт-4/§6 п.3 + the two measurement docs +
   the Sc-rep RESULT; DECIDE+RECORD: active-set/front data structure + canonical iteration order (deterministic,
   pinned); how dormant saturated gas byte-sleeps (Факт-4); scratch strategy (no roster-sized dense planes on
   the hot path); ADR = next free **ADR-E-*** per ADR-P-0001 (verify at tip — OS docs do not pre-assign).
2. **Scaling gates (the point of the slice; same harness as 2026-07-02):**
   (a) roster-independence — hangar ms/tick at roster 1 vs 64 differs by ≤ ~10-20% (was 32.5×);
   (b) active-scaling — hangar with 1,562 active cells costs a small fraction of the 2026-07-02 dense-kernel
   number (target class: single-digit ms on the owner machine; PLAN sets the recorded threshold);
   (c) adversarial **«hangar flooded»** — ALL ~196k cells active: measured and recorded vs the 50–100 ms
   budget with the weak-peer ×2–4 caveat (this is the SPEC's real worst case — «cost ∝ active fronts is FALSE»
   was about exactly this; no silent pass).
3. **Measurement matrix re-run before/after** (TYPICAL + HANGAR × roster 1/4/16/64, 40 timed + 5 warmup) —
   recorded in docs/measurements/ side-by-side; PLUS a Unity-runtime capture (the 2026-07-02 numbers were
   CoreCLR console — the owner-run Editor/PlayMode capture is the honest absolute; an owner-run step is not
   done until the owner confirms).
4. **No-regression:** single-type AND multi-type runs byte-identical to the post-Sc-rep committed goldens;
   loopback two-endpoint MeaningChecksum green over a multi-type sparse run; no golden rebaselining.
5. **Determinism (ADR-0002):** integer-only; new code under BOTH zero-float + int-overflow scan roots (kept
   paired); planted float / order-dependence / awake-set-order RED controls trip. **Close the Coarse/ scan-root
   hole here** (add Coarse/ to both root lists + a planted-violation self-test) — folded from the 2026-06-29
   plan-audit so it stops floating.
6. **GC-zero steady-state** holds on the new hot path (no per-tick roster-sized allocations; a planted
   per-tick `new int[cells]` MUST trip).
7. **check.ps1 -Deliver GREEN** (full battery: build + headless + scans + mutation ≥70 on new Core +
   spec-silence + deliverable-coverage + escape-class walk) + independent-author REDs (builder cannot edit) +
   **fresh-session G5** + owner-eye (owner sees the same scenes + the before/after table).
8. **ZERO-LEGACY:** the per-tick dense expand/rebuild path removed at completion (git is rollback); dense
   remains ONLY where it is a one-time migration/test-oracle input, never per-tick authority.

## boundaries / STOP

- NO reactions / typing / waves / damage / temperature. NO S4 rollup build (seam preserved). NO visual hookup,
  NO dev2 edits. NO K/overflow policy change (that is the c-exec-021 shape's named fork, banner item 13).
- NO float, no unseeded RNG, no wall-clock on the authoritative path; ADR-0002 not reopened.
- If byte-identity vs the post-Sc-rep goldens cannot hold with a sparse kernel (ordering!), STOP and surface —
  do NOT rebaseline silently.
- Split-trip BY MACHINERY if oversized: leg1 = the active-front kernel + roster-independence + no-regression +
  determinism; leg2 = the flooded-hangar adversarial capture + Coarse/ scan-root closure + Unity-runtime capture.

## return

RESULT routed HOME: commits/PR, -Deliver transcript, mutation json, before/after measurement table (+ flooded
hangar + Unity capture), independent RED list, fresh G5 verdict, owner-eye note, chosen ADR-E number. dev→main
merge + push owner-gated. On GREEN the road rolls to Sc-reactions (re-harden c-exec-021 per its banner 11-14).

END_OF_FILE: live/indie-game-development/work/c-exec-023-draft-call.md
