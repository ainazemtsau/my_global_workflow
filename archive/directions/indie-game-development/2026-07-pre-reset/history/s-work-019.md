# RESULT — s-work-019 (work · g-9c41/S0 · apply c-exec-014 RETURN → close S0 → frame S1)

play: work
direction: indie-game-development
node: g-9c41
task: S0 (FOUNDATION SLICE, layered) → done; rolls to S1
date: 2026-06-26

## outcome

The S0 FOUNDATION SLICE is DELIVERED and CLOSED, and the bet rolls to S1. c-exec-014 (the layered-reshape S0,
superseding c-exec-013) returned GREEN and was merged + pushed to GasCoopGame `main` @824948d. The five test/benchmark
findings the builder routed home are all dispositioned by the planner; the next slice S1 (выброс-при-спауне +
выдавливание телом) is framed as a build-ready executor CALL.

S0 in fact delivered roadmap steps 1–4 (reader→grid, gas fills a room by face-flow, determinism + lockstep loopback,
a clickable Unity benchmark harness) INCLUDING the HANGAR PROBE — the architecture's #1 previously-unmeasured number.

## evidence

- **Product repo verified FIRST-HAND** (not trusting the RESULT narrative): GasCoopGame `main` HEAD = `origin/main` =
  `824948d` ("Merge dev into main: c-exec-014 … DELIVERED"); named artifacts all exist
  (`docs/measurements/c-exec-014-benchmark-readout.md`,
  `docs/measurements/mutation-c-exec-014-s0-foundation-slice-layered.json`,
  `docs/c-exec-014-transitional-debt.md`); openspec change `c-exec-014-s0-foundation-slice-layered/` present.
- **Source-of-truth RESULT read in full:** `GasCoopGame/RESULT.md`. `tools/check.ps1 -Deliver` GREEN — headless tests
  0 failed, mutation 77.6 % (665/857) ≥ 70 floor, zero-float scan over both grids, spec-silence audit,
  deliverable-coverage v8 (9/9). Ledger F0a–F12 + Fz/Fcarry/Fg/Fo closed with opened evidence.
- **Binding engineering G5** = the in-leg FRESH-SESSION refutation by a DIFFERENT MODEL FAMILY (Sonnet),
  COULD-NOT-REFUTE on all 6 targets (determinism-by-construction, STOP-v8 substitutions absent, tests
  non-vacuous/value-EQUAL, atomicity-under-throw, T6 soundness, ledger honesty). Plus a 5-vector determinism audit
  (SOUND) and a 3-lens zero-legacy re-audit (CLEAN). The OS-level review is DISCHARGED by these in-leg adversarial
  passes (they exceed a review-play bar) + the first-hand merge/artifact confirmation; «весело», the only owner-intent
  axis, is owner-EXCLUDED — so no separate OS review session is warranted.
- **Hangar probe readout:** TYPICAL 3,456 cells / 0.525 ms/tick; HANGAR 196,608 cells / 24.5 ms-avg-tick (65.5 max),
  only 1,562 active cells. Run on a STRONG CPU (Ryzen 9 7950X3D) → optimistic for a single-threaded CPU sim.

## planner decisions on the 5 routed-home findings

- **d-sparse-solver-defer-001** (sparse active-front solver #1 + weak-CPU re-measure #2 + GC pooling #3) — **DEFER**
  to the big-hall gate. The sparse solver matters ONLY for BIG OPEN VOLUMES (hangars), which are explicitly
  DEFERRED-RESERVED (d-cellsize-split-001). The near room-scale slices S1–S5 run on the DENSE solver, which is
  measured fine (TYPICAL 0.525 ms/tick, ~50× under a generous budget). The sparse solver + GC pooling + a weak-CPU
  re-measure are a NAMED, ready optimization leg that FIRES before any big-hall feature is committed; the big-hall
  viability verdict is now explicitly GATED on it. Surfaced loudly: at full 196k the dense hangar is already marginal
  on a strong CPU (24.5 ms) and ~2–4× worse on weak hardware, so big-hall viability is UNPROVEN until that leg shows
  the ~100× headroom — but nothing near-term depends on it. Owner-vetoable.
- **d-overflow-guard-001** (recurring `int*int` overflow class #4 + extreme-coordinate spec-silence row #5) — **BUILD
  the class-wide guard**. The invariant recurred 3× → per "same class twice = stop", a build-scan tripwire that
  auto-discovers unguarded `int*int` on the authoritative path (RED-first, planted control) beats a 4th per-site
  patch. Paired with the PLANNER-AUTHORIZED extreme-coordinate spec-silence amendment (the builder may not self-edit
  the frozen spec). Both folded into c-exec-015 as carried hardening H1/H2.

## state_changes

- NOW.md `active_tasks` S0: `status: active → done` (evidence above); ADD task S1 (status active) — the dynamic-gas
  slice, framed as c-exec-015.
- NOW.md `open_calls` c-exec-014: `status: queued → done` (merged @824948d, evidence above); ADD c-exec-015
  (status queued; work/c-exec-015-call.md).
- NOW.md `decision_inbox`: ADD d-sparse-solver-defer-001 (answered) + d-overflow-guard-001 (answered).
- NOW.md `phase`: prepend the s-work-019 entry. NOW.md `next`: replaced (S1 / c-exec-015 + deferrals + pending
  maintenance + push note).
- LOG.md: one line appended. work/c-exec-015-call.md: created. work/gas-engine-build-roadmap-2026-06-26.md: a
  post-c-exec-014 section appended (hangar result + the two decisions + S1 next).

## captures

- KNOWLEDGE-PROMOTION CANDIDATE (for review/pulse): "Big-hall viability is gated on the sparse active-front solver —
  the dense S0 solver does ~125× redundant work at hangar scale (measured 24.5 ms strong-CPU / 1,562 active of
  196,608). Near room-scale slices are unaffected." → feeds the eventual big-hall optimization leg.
- The os/engineering MAINTENANCE request (anti-substitution over-rotation + resolution conflation) is drafted at
  work/MAINTENANCE-os-engineering-scope-guard-2026-06-26.md, awaiting a SEPARATE maintenance session (os/** untouched
  in a live-direction session).

## decisions_needed

None blocking. Both routed-home decisions were delegated to the planner ("решение и формулировка за тобой") and are
DECIDED above (owner-vetoable). One veto opening offered: if the owner prefers to front-load the sparse-solver / perf
de-risk instead of S1, the next CALL swaps — but S1 is the recommended (and roadmap-aligned) next.

## play_check (play: work)

1. Recite — DONE: restated S0 goal/done_when + the g-9c41 bet; confirmed S0's done_when met by the c-exec-014 RESULT.
2. Owner inputs (owner) — N/A: the artifacts (the S1 CALL + the routed-home dispositions) are machine/planning
   artifacts, not owner-content (food/voice/money/schedule). No owner-input drafting required; the one owner-judgment
   axis («весело») is owner-excluded as a gate. The sequencing call was explicitly delegated by the owner this turn.
3. Do the work — DONE: applied the c-exec-014 RETURN, decided the 5 routed-home findings (2 decision entries), and
   framed the next task via `call:executor` (c-exec-015, work/c-exec-015-call.md).
4. Self-check — DONE: compared against S0 done_when point-by-point; verified product `main` @824948d + artifacts
   first-hand; accepted the in-leg different-family fresh-session G5 as the binding engineering verification.
5. Close — DONE: this RESULT; next = c-exec-015 (S1 executor CALL).

## log

2026-06-26 — work (g-9c41/S0, s-work-019): c-exec-014 S0 FOUNDATION SLICE (layered) RETURN APPLIED — S0 DELIVERED +
CLOSED (merged GasCoopGame main @824948d, -Deliver GREEN, mutation 77.6%, fresh-session G5 Sonnet could-not-refute,
verified first-hand). HANGAR PROBE returned. 5 findings decided (d-sparse-solver-defer-001 + d-overflow-guard-001).
Bet rolls to S1 (выброс-при-спауне + выдавливание), framed as c-exec-015.

## next

CALL c-exec-015 — S1 (выброс-при-спауне + выдавливание телом), build-ready at work/c-exec-015-call.md. Owner opens a
fresh GasCoopGame_dev session, opens with a PLAN (owner present, §Re-sync v8→current first), builds in small
owner-playable steps. RESULT applied home by a separate OS writer.

END_OF_FILE: live/indie-game-development/history/s-work-019.md
