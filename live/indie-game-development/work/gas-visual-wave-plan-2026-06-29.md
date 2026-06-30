# Gas-visual WAVE PLAN — toward the JEWEL on the REAL sim (owner re-plan 2026-06-29)

Owner-co-created in s-visual-010 after the framed S2 (two-type + scatter-glow tuned in the EMPTY
analytic gas-lab) degraded to jelly / two bobbing blobs / visible grid — WORSE than the prior
single-column S1. This plan REPLACES the "S2 as the next sub-leg" SEQUENCING in
docs/gas-visual-stage-plan.md; the look levers in that doc (§S1, §S6+ P1/P2) remain the menu we draw from.

## Root cause of the failure (verified in code, not guessed)
1. The look was judged in an EMPTY black void (the gas-lab) — heavy gas had no floor to settle on,
   "light through volume" had no visible light source, no scale → gas reads as floating blobs.
2. The render method has a low ceiling today (coarse cheap noise; Worley off for FPS → visible grid).
3. Blind live knob-turning chasing "jewel" on top of (1)+(2) → chased one artifact into another
   (jelly → grain → blobs), each worse.
The TASK (two characterful gases + light-through) was fine; the SETUP and PROCESS were wrong.

## What changed (the fix)
- JUDGE ON THE REAL SIMULATION, in a real lit room — not a fake gas in a void. Verified feasible &
  safe first-hand: RealGasViewSource (Adapters/GasView) already reads VoxelField.ConcentrationAt
  render-only; the read-only guarantee is STRUCTURAL (it holds no writable sim handle) → the visual
  cannot change the sim. GasVoxelSandboxScene + the c-visual-001 S5 swap already render real gas in
  motion. The analytic gas-lab is DEMOTED to a helper (isolate a look lever in clean conditions; it
  transfers to the real sim with ZERO shader change via the shared IGasViewSource seam). The real sim
  is COARSE (~0.5-1m cells) → real-gas SHAPE is capped by sim resolution; finer-grid-near-player is an
  ENGINE job (g-9c41), not a visual bug.
- NEVER-WORSE discipline (the process fix): a saved best baseline (one-click), every change shown A/B
  vs it, becomes the new baseline only if the owner sees it better; worse = discarded. ONE inspector,
  all knobs labelled, nothing hidden. ONE visible win at a time, the expectation stated in plain words
  BEFORE the step. Uncertainty comes HOME, never knob-chased.

## The destination — "maximum gas" (the ~10 levers; ~3 used today, ceiling far per the stage-plan doc)
Real gas in a real lit space + light through the volume; rich detailed substance (baked 3D noise +
detail erosion); smooth non-cubic shape (smootherstep warp + finer sim near player = ENGINE); alive
motion (curl billow + natural flowing jets, not stretching capsules); EACH type its own full look AND
behaviour (colour / edge / noise / motion / glow / buoyancy as DATA); bold readable edge + warning
telegraph; stylized lighting; optional sparse VFX accents; runs on weak HW (perf pass).

## The road — waves (each = visible wins, never going backwards)
- WAVE 1 — out of the hole + honest foundation (THIS = c-visual-003): real room (floor / walls / scale /
  visible lamp / fixed camera) on the REAL sim; light THROUGH the gas (scatter-glow = the "jelly" fix);
  base-render cleanup (smootherstep warp + baked 3D noise to kill cubic/lines/grid); then the first TWO
  gases reading as different character (heavy sinks / light rises). May split at PLAN into visible
  sub-steps (1a one good gas in the lit room -> 1b second type), each owner-eye-signed. Result: a
  clearly-good, real, readable gas in a real room — the floor we never drop below.
- WAVE 2 — alive motion: real curl/billow + a natural flowing jet (not a capsule) + per-type motion signatures.
- WAVE 3 — full per-type looks + reactions: each type its complete visual profile (DATA); emissive reactive
  cores; warning telegraphs.
- WAVE 4 — polish + perf: anti-banding/dither, sparse VFX accents, the weak-HW perf pass (§S4), finest detail.
- PARALLEL ENGINE (not visual): finer sim grid near the player -> real-gas SHAPE less blocky (g-9c41 roadmap).

## Boundaries (hold every wave)
RENDER-ONLY (R13): zero Core/** edit, sim untouched & its tests unchanged, upload-only, no readback.
96B GpuGasParams layout FROZEN — a new per-type field = a reserved-field assignment or a layout-ADR event,
never silent. "Done" = the owner's EYE on the real gas in motion, never a self-marked green suite.

END_OF_FILE: live/indie-game-development/work/gas-visual-wave-plan-2026-06-29.md
