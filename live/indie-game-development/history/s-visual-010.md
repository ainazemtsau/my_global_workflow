# s-visual-010 — VISUAL track g-7e15 re-plan: from "S2 in the empty lab" to WAVES on the REAL sim

RESULT (re-plan / re-shape of the look-development approach; owner-co-created; RENDER-ONLY track, parallel to g-9c41, G1 intact).

## outcome
The framed c-visual-002 S2 (two differently-charactered gases + scatter-glow tuned in the EMPTY analytic gas-lab)
hit a wall in the GasCoopGame_dev_2 build: the look degraded to "jelly / two bobbing blobs / visible grid" —
WORSE than the prior single-column S1. Stopped, diagnosed the ROOT CAUSE (with the builder, verified in code),
and RE-PLANNED the whole look-development approach with the owner.

## root cause (verified, not guessed)
(1) the look was judged in an EMPTY black void (no floor for heavy gas to settle on, no visible light for
"light-through-volume", no scale -> floating blobs); (2) the render method has a low ceiling today (cheap inline
noise, Worley off -> visible grid); (3) blind live knob-turning chased one artifact into another. The TASK was
fine; the SETUP + PROCESS were wrong.

## the re-plan (owner-approved in-session)
- JUDGE ON THE REAL SIMULATION in a real lit room, not a fake gas in a void. Verified feasible & safe first-hand:
  RealGasViewSource (Adapters/GasView/) already reads VoxelField.ConcentrationAt render-only; the read-only
  guarantee is STRUCTURAL (holds no writable sim handle) -> the visual cannot change the sim. GasVoxelSandboxScene
  + the c-visual-001 S5 real-data swap (d90695c) already render real gas in motion. The analytic gas-lab is
  DEMOTED to a helper (isolate a look lever in clean conditions; transfers to real via the shared IGasViewSource
  seam, zero shader change). The real sim is COARSE (~0.5-1m cells) -> real-gas SHAPE is capped by sim resolution;
  finer-grid-near-player is an ENGINE job (g-9c41), not a visual bug.
- NEVER-WORSE process discipline (the owner's required fix): a saved one-click best baseline, A/B every change,
  new baseline only if the owner sees it better, one-inspector control panel, one visible win at a time with the
  expectation stated up front, uncertainty comes HOME not knob-chased.
- FULL ROAD recorded as a WAVE plan (the owner wanted the comprehensive plan made official): wave 1 foundation
  (real room + light-through + base-render cleanup + first two-type) -> wave 2 alive motion -> wave 3 full per-type
  looks + reactions -> wave 4 polish + perf, parallel an engine finer-grid track. ~3 of ~10 look levers used;
  ceiling far (per docs/gas-visual-stage-plan.md). Plan = work/gas-visual-wave-plan-2026-06-29.md.

## rollback
The degraded S2 work was UNCOMMITTED on dev2 only (dev2 == main @7d08882; main = the good S1). Builder ordered to
discard the uncommitted changes back to the clean baseline (also restores an accidentally-deleted FishNet .meta).
Nothing bad merged; main untouched.

## state_changes
- NOW.md parallel_tracks g-7e15 note: replaced the "next = old S2, no CALL open" text with the re-plan summary +
  pointers to work/gas-visual-wave-plan-2026-06-29.md and the wave-1 CALL work/c-visual-003-call.md; the old
  "S2 two-type+scatter as framed" marked SUPERSEDED. No bet / TREE / active-task change (parallel track, G1 intact).
- LOG.md: appended the s-visual-010 line.
- work/gas-visual-wave-plan-2026-06-29.md: NEW (the official wave plan).
- work/c-visual-003-call.md: NEW (the wave-1 CALL, ready for a fresh GasCoopGame_dev_2 session).

## evidence
First-hand code reads on GasCoopGame main @7d08882 / @f7efbea: RealGasViewSource.cs (reads VoxelField.ConcentrationAt
via VoxelSandboxDirector, holds no VoxelField handle), IGasViewSource.cs (structural read-only / upload-only seam),
GasVoxelSandboxScene.unity + d90695c (S5 real-data swap delivered), dev2 git status (the S2 changes uncommitted,
dev2 == main). docs/gas-visual-stage-plan.md (~3/10 levers, ceiling far). A verification workflow (wf_75fef20b-9cf)
was run but failed on a tool-format error; the facts were re-verified first-hand by direct code read.

## next
Wave 1 = work/c-visual-003-call.md — opens in a fresh GasCoopGame_dev_2 session with a PLAN (owner present), after
the dev2 rollback to the clean baseline. Comes HOME with an owner-eye sign.

END_OF_FILE: live/indie-game-development/history/s-visual-010.md
