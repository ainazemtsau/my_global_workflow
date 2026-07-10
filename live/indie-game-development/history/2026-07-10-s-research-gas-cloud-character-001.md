RESULT s-research-gas-cloud-character-001 (call: owner-plain-gas-cloud-character-2026-07-10)
direction: indie-game-development   play: research   node/task: g-7e15/c-visual-009 (informs g-9c41)

outcome: |
  The observed «rare stationary gas spots» are now separated into three evidenced mechanisms: current linear
  face-flow dilutes the finite neutral Kp12 seed to a weak near-uniform field; FBM/Worley erosion removes most
  low-density coverage; near-equilibrium Flux is sub-pixel while the surviving noise field is world-anchored.
  A durable owner-readable report compares the actual solver with five solution classes, rejects oxygen/extra
  mass/particles as fixes, and identifies a staged route: repair c-visual-009 provenance first, then authorize the
  render-vs-simulation probe; only if the owner requires compact gameplay-time locality, compare nonlinear mobility
  with explicit surplus-only packing in a separate Core PLAN. No product or live direction state was changed and
  c-visual-009 remains open.

evidence: |
  - Durable synthesis: work/gas-cloud-character-analysis-2026-07-10.md.
  - Current kernel: VoxelField.cs:1211-1245 uses mass-difference / SpreadKp flow plus separate buoyancy; the effective
    buoyancy magnitude is capped at 64. GasParentParams.cs:10-35 marks Kp as damping and DensityPacking inert.
  - Current sample: GasDemoPlumeControls.cs:865-903,1195-1203 selects OpenArena, neutral default registry, finite seed
    and disables continuous source/vent/jet; ForkedCorridorLevel.cs:79-88 is 5x16x5.
  - Mass arithmetic: 1,808,372,870 in 120 cells = 89.82% of those cells and 26.95% of the 400-cell arena; Editor.log
    records Tick 512 at 400/400 cells, 232-305 per-mille, mean 269.06.
  - Render: GasUber.shader:381-390 applies eroded = baseD - (1-noise)*FbmErode*(1-baseD); PC_Renderer.asset has
    FbmErode 1.35, WorleyMix 0.82, NoiseStrength 1, motionSpeed/curl 0. At baseD 0.23-0.30, only noise above about
    0.68-0.78 remains nonzero.
  - Late motion: Editor.log records max Flux 9,976, max MovementView 0.000591 cell and 0/400 changed R8 densities;
    GasUber.shader:218-243,328-374 samples noise at the unchanged world point while Flux offsets density endpoints.
  - Physics: NIST FDS models species advection/diffusion plus pressure/buoyancy
    (https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.1018e6.pdf); NOAA describes dense-gas gravity
    spreading plus air entrainment/dilution
    (https://response.restoration.noaa.gov/sites/default/files/ALOHA_Tech_Doc.pdf); porous-medium nonlinear
    diffusion has finite-speed compact fronts but does not prove the current lattice
    (https://ems.press/journals/aihpc/articles/4076861).
  - Reproducibility limit: the runtime probe source/JSON is absent; cited numbers survive only in Editor.log and need
    a fresh authorized capture before acceptance.
  - Provenance conflict: NOW.md:128 still records a PLAN-only pending call, while the product checkout is
    codex/c-visual-009-build at approved PLAN commit a0db28a2 with a large dirty BUILD. No product RESULT, review or
    binding fresh G5 exists; this evidence cannot close the Direction-OS call.
  - Parallel method: two independent evidence miners plus one failure-inversion architecture search were merged and
    deduped. A three-validator in-session refutation pre-pass (non-binding, not G5) preserved the core/physics
    diagnosis, exposed the missing reproducible probe, and refuted actionability inside the unauthorized dirty BUILD.

state_changes: |
  live/indie-game-development/work/:
    - add gas-cloud-character-analysis-2026-07-10.md exactly as carried by this RESULT.
  live/indie-game-development/LOG.md:
    - append the s-research-gas-cloud-character-001 log line before the END_OF_FILE trailer.
  live/indie-game-development/history/:
    - add 2026-07-10-s-research-gas-cloud-character-001.md with this full RESULT.
  live/indie-game-development/NOW.md, TREE.md, CHARTER.md and product repositories:
    - no change; c-visual-009 remains open and its stale PLAN-only provenance is not silently repaired here.

captures:
  - c-visual-009 provenance drift: NOW says PLAN-only pending; product has approved PLAN @a0db28a2 plus dirty BUILD. Route a repair; never treat the developer chat or dirty checkout as close evidence.
  - g-9c41 cloud-character seam: DensityPacking is inert and current linear diffusion has no compact-front law. If the owner selects gameplay-time locality, shape a separate baseline-compatible nonlinear-vs-packing probe no later than Sc-damage PLAN.
  - render seam: current erosion destroys weak-field coverage and visible noise stays world-anchored. A future authorized diagnostic must separate raw density, no-erosion control and current render before selecting a fix.

decisions_needed:
  - q: |
      After the source stops in a sealed room, should the special gas stay locally concentrated only over the gameplay
      horizon, remain as a permanent packed pool, or be treated as a physically mixing air/gas system?
    options:
      - gameplay-time compact front, then slow trace
      - permanent surplus-only packed pool
      - physical air/pressure/velocity mixture
    recommendation: |
      Gameplay-time compact front, then slow trace: it matches the owner's cloud requirement without silently turning
      the gas into a liquid or opening full CFD; test nonlinear mobility first and keep strict packing as the explicit
      fallback if the owner wants permanent piles.

play_check:
  - 1 Recite: done — one bounded question, return format and one-leg deep-research budget were stated.
  - 2 Investigate: done — current code, dirty BUILD, runtime log, Direction OS canon and dated primary technical sources were inspected; independent children ran in parallel and were merged/deduped.
  - 3 Confidence: done — established code/runtime facts, inference, missing reproducible probe and unproven nonlinear-law candidate are separated; three-validator pre-pass is explicitly non-binding and not G5.
  - 4 Close: done — findings return to c-visual-009 without product/live-state mutation or a false close.

log: 2026-07-10 — research (g-7e15/c-visual-009 → g-9c41 cloud character, s-research-gas-cloud-character-001): confirmed linear dilution + coverage-destroying erosion + equilibrium stillness, rejected oxygen/more-mass/particles as fixes, and recorded a staged compact-front investigation; c-visual-009 stays open and its PLAN→dirty-BUILD provenance needs repair. → history/2026-07-10-s-research-gas-cloud-character-001.md

next: |
  return-to-parent c-visual-009 — before any continuation or close, repair the PLAN-only vs dirty-BUILD provenance;
  then await the owner's cloud-equilibrium choice and issue a fresh authorized CALL rather than extending the current
  product checkout.

END_OF_FILE: live/indie-game-development/history/2026-07-10-s-research-gas-cloud-character-001.md
