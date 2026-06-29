# CALL c-visual-002 — gas-lab + cloud-at-rest (look-development step 0+1)

direction: indie-game-development
node: g-7e15 (VISUAL track)
play: work (executor leg — GasCoopGame render/adapter layer; dev2→main when green)
opens_with: a PLAN (owner present); §Re-sync the GasCoopGame repo contract FIRST.
runs_in: a fresh GasCoopGame_dev_2 session (the BUILD session; this is NOT the OS-worktree session).

## goal (outcome, not method)

In a dedicated open-space "gas lab", a single gas cloud AT REST reads at a glance as a real, beautiful gas — not
blocky voxels, not "jelly" — the honest foundation the owner signs as «ближе к жемчужине». Small confident step:
the lab + the resting-cloud look only.

## context (read first; self-contained pointers)

- Forward spec / techniques: `GasCoopGame docs/gas-visual-stage-plan.md` (§Aesthetic target, S1 smoke-bomb, S6+ P1 levers).
- Delivered base to REUSE (do NOT rebuild): the `GasUber` raymarch body + `RealGasViewSource` + the `GasParams` seam
  (ADR-0012/0013/0014/0015); the `GasConceptPresets` live look-switcher.
- Felt TARGET (owner): gas = the game's JEWEL; each type its own CHARACTER (a later step); low-poly = the WORLD, not a
  cap on the gas; commercial-clean (no NVIDIA Flow).
- Root-cause the lab fixes (gas-visual-stage-plan §S6+): the coarse BOX + grid drives the cubic/lines/jelly read; open
  space + the P1 form/light levers fix it. (The box scene "lies" — that is why the lab comes first.)

## scope — step 0+1 ONLY (keep it small)

- **0) GAS-LAB scene** — gas as a FREE cloud/puff in OPEN space (NO level walls, no VoxelSandbox box), a clean fixed
  camera + light rig, a resting puff. (Buttons for spawn/jet/wind arrive with THEIR steps, not now.)
- **1) CLOUD-AT-REST look** — apply the P1 form/light levers so the resting cloud reads as real gas: smootherstep
  coord-warp + a baked/inverted-Worley detail-volume (kill the cubic creases/lines) + cheap stylized lighting (two-tone
  ambient + scatter-GLOW; drop the opaque "jelly" feel). Default gas character only.

## boundaries (STOP-and-ask if any is hit — never a silent substitute)

- **RENDER-ONLY (R13):** ZERO `Core/**` edit; the sim is untouched; the 977 sim tests stay green & unchanged; no
  `VoxelField` handle, UPLOAD-ONLY (no readback into the sim).
- **96B `GpuGasParams` layout FROZEN** — a new per-type field = a reserved-field or a layout-ADR, never silent.
- **LOOK-FIRST:** no min-spec perf pass (S4 deferred); 2 body knobs + a free NON-gating home frame-cost reading only.
- **SMALL STEP:** NO spawn / jet / types / behavior this leg (those are steps 2-5). If the build reaches for them →
  STOP, it is a later step.

## done_when

- Opens with a PLAN (owner present); §Re-sync the GasCoopGame contract first.
- The gas-lab scene exists (open-space resting cloud, clean camera/light), reproducible.
- **HEADLESS (the «точно» half — automatable):** `tools/check.ps1 -Deliver` GREEN; render-only regression invariants
  hold — `git diff Core/**` empty, 977 sim tests unchanged, the C#↔HLSL stride gate green, no readback. RED-first ONLY
  where there is genuinely mechanically-testable NEW surface; if there is none, say so honestly ("no new headless law —
  owner-eye binds") rather than manufacturing a test.
- **OWNER-EYE (the BINDING gate — not unit-testable):** owner opens the lab, sees ONE resting cloud that reads as real
  gas (not blocky, not jelly), and signs «ближе к жемчужине». Owner-run, no self-marking.
- The RESULT comes HOME to OS (state_changes applied by a separate writer); NO off-contour merge.

## return

A RESULT routed home — outcome + evidence (the render-only invariants + the owner-eye sign) + the next look slice
(step 2 = spawn / выброс).

## budget / rigor (right-sized — this is the one legit sim-vs-look difference)

~40-60 min/day owner-gated build-gaps; a fresh GasCoopGame_dev_2 session. The SAME contour as the engine legs, but the
rigor is right-sized to a render-only look step: the binding gate is the owner's EYE plus the render-only regression
invariants. NO heavy adversarial test-authoring / multi-agent refutation hardening here — there is nothing
correctness-critical to refute (the sim can't break, render-only). That heavy round exists for the SIMULATION because a
determinism bug is catastrophic and objectively testable; "looks like a jewel" is neither.

END_OF_FILE: live/indie-game-development/work/c-visual-002-call.md
