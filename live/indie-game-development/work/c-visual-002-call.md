# CALL c-visual-002 — gas-lab + cloud-at-rest (look-development, step 0+1)

- direction: indie-game-development
- node: g-7e15 (VISUAL track)
- play: work (executor leg — GasCoopGame render/adapter layer; dev2→main when green)
- runs_in: a FRESH GasCoopGame_dev_2 session (the BUILD session; NOT the OS-worktree session)
- opens_with: a PLAN (owner present). §Re-sync the GasCoopGame repo contract FIRST, then PLAN — exactly like an engine leg. This PLAN is a PROPER plan; only the SCOPE it plans is small (step 0+1).

## goal (outcome, not method)

In a dedicated open-space "gas lab", a single gas cloud AT REST reads at a glance as a real, beautiful gas — not blocky
voxels, not "jelly" — the honest foundation the owner signs «ближе к жемчужине». Small scope: the lab + the resting
cloud's look only.

## why this step, and why the lab first

The owner felt the gas «блекло / топчемся». Diagnosis (GasCoopGame `docs/gas-visual-stage-plan.md §S6+`): only ~3 of
~10 look levers are built AND the level BOX + coarse grid drive the "cubic / vertical-lines / jelly" read — the box
scene "lies". So the lab (gas as a free cloud in OPEN space) comes first, so the look can be judged and developed
honestly; then the form/light levers make the resting cloud read as real gas. Spawn / jet / types / behaviour are later
steps (2-5) — NOT here. This is the felt TARGET: gas = the game's JEWEL; each type its own character (a later step);
low-poly = the WORLD, not a cap on the gas; commercial-clean (no NVIDIA Flow).

## reading set (self-contained — read these first)

- `GasCoopGame docs/gas-visual-stage-plan.md` — §Aesthetic target, §S1 (smoke-bomb base), §S6+ (the P1 levers + the
  root-cause diagnosis + the agreed gas-lab path).
- The delivered base to REUSE, do NOT rebuild: the `GasUber` URP raymarch body shader, `RealGasViewSource`, the
  `GasParams` GraphicsBuffer + GridView seam (ADR-0012/0013/0014/0015), and the `GasConceptPresets` live look-switcher.
- The repo contract: `AGENTS.md` / the current build conventions (the §Re-sync target).

## open with this PLAN (owner present — a proper plan, same discipline as the engine legs)

1. **§Re-sync** the GasCoopGame repo contract (AGENTS.md / current build + gate conventions) BEFORE touching anything.
2. **Ingest** the reading set; state explicitly what you REUSE (body/seam/switcher) vs what you ADD (the lab scene +
   the resting-look levers). Nothing in `Core/**` is touched.
3. **Decide the HOW and put it to the owner** (with a recommendation each):
   (a) the gas-lab scene shape — open-space puff, a fixed camera + light rig, and how the resting cloud is fed (a simple
       resting source; real or fake data both fine here — the look is what matters);
   (b) which P1 levers you apply for the resting look and in what order — smootherstep coord-warp; baked 3D
       inverted-Worley detail-volume vs the inline proxy; the stylized scatter-GLOW + two-tone ambient light; plus the
       2 reserved body knobs (resolution scale + step count). Surface any genuine FORK (e.g. bake-a-noise-texture-now
       vs inline) as an owner decision.
4. **Name the gates** you will hit (the done_when below) and the render-only invariants you will keep. If any needed
   change would touch `Core/**` or the sim → STOP and escalate (then it isn't render-only and isn't this leg).
5. **Owner signs the PLAN** before any build.

## scope — step 0+1 ONLY

- **0) GAS-LAB scene** — gas as a FREE cloud/puff in OPEN space (NO level walls, no VoxelSandbox box); a clean fixed
  camera + light rig; a resting puff; reproducible (a scene you can re-open and re-run).
- **1) CLOUD-AT-REST look** — apply the P1 form/light levers so the resting cloud reads as real gas: smootherstep
  coord-warp + a baked/inverted-Worley detail-volume (kill the cubic creases / lines) + cheap stylized lighting
  (two-tone ambient + scatter-GLOW; drop the opaque "jelly" feel). Default gas character only.

## boundaries (STOP-and-escalate if hit — never a silent substitute)

- **RENDER-ONLY (R13):** ZERO `Core/**` edit; the sim is untouched; the 977 sim tests stay green & UNCHANGED; no
  `VoxelField` handle; UPLOAD-ONLY (no readback into the sim).
- **96B `GpuGasParams` layout FROZEN** — a new per-type field = a reserved-field or a layout-ADR event, never silent.
- **LOOK-FIRST:** no min-spec perf pass (S4 deferred); only the 2 body knobs + a free NON-gating home frame-cost reading.
- **SMALL STEP:** NO spawn / jet / types / behaviour this leg (those are steps 2-5). If the build reaches for them →
  STOP; it is a later step. (The owner will hold this line too.)
- A blocked/infeasible named approach, or a reduced-fidelity crutch, = mandatory STOP + escalate (repo STOP-discipline).

## done_when

- Opened with the PLAN above, owner-signed; §Re-sync done first.
- The gas-lab scene EXISTS (open-space resting cloud, clean camera/light), reproducible.
- **HEADLESS — the «точно» half (objective, automatable):** `tools/check.ps1 -Deliver` GREEN; the render-only
  regression invariants hold — `git diff Core/**` EMPTY; the 977 sim tests UNCHANGED; the C#↔HLSL stride-conformance
  gate green; no readback. RED-first ONLY where there is genuinely mechanically-testable NEW surface (e.g. a baked-noise
  asset's load/format contract is worth a guard); if there is none, SAY SO honestly ("no new headless-testable law —
  owner-eye binds"), do not manufacture a test.
- **OWNER-EYE — the BINDING gate (not unit-testable):** the owner opens the lab, sees ONE resting cloud that reads as
  real gas (not blocky, not jelly), and signs «ближе к жемчужине». Owner-run, no self-marking, judged IN MOTION (a
  still can lie).
- The RESULT comes HOME to OS (state_changes applied by a separate writer); NO off-contour merge. dev2→main is
  owner-gated when green.

## return

A RESULT routed home: `outcome` + `evidence` (the render-only invariants + the owner-eye sign) + the next look slice
(step 2 = spawn / выброс).

## budget & rigor (the ONE legit sim-vs-look difference — stated, not hidden)

~40-60 min/day owner-gated build-gaps; a fresh GasCoopGame_dev_2 session. SAME contour as the engine legs
(CALL → proper PLAN → build → gates → RESULT home). The rigor is right-sized to a render-only look step: the binding
gate is the owner's EYE plus the render-only regression invariants. NO heavy independent-RED-test-author +
multi-agent adversarial-refutation round — there is nothing correctness-critical to refute (the sim cannot break;
render-only). That heavy round exists for the SIMULATION because a determinism bug is catastrophic AND objectively
testable; "looks like a jewel" is neither. This right-sizes the GATE — it does not skip the contour, the §Re-sync, or
the PLAN.

END_OF_FILE: live/indie-game-development/work/c-visual-002-call.md
