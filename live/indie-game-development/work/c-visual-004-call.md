# CALL c-visual-004 — Stage 1: Стенд + отсечка по глубине — RENDER-ONLY

> 🔥 **FIRE-READY 2026-07-06** (s-work-054; owner: «визуал — параллельный трек, хочу запускать»). Base + scope
> refreshed for launch. **Base = GasCoopGame main @26dd062** (contract v18; includes Sc-rep/Sc-kernel/W1b +
> c-029/c-030/c-031 §Re-sync + c-visual-005). **dev_2 RESET:** reset `GasCoopGame_dev_2` to `origin/main` @26dd062
> FIRST (it already carries c-visual-005's merged work; do NOT build on the old contaminated tip @3858752 or the
> stale @40b94cc/@bc25a33).
>
> ⚠ **RE-SCOPE — c-visual-005 already landed a CHUNK of Stage 1 (do NOT rebuild it):** the DEPTH COMPOSITE (#1 —
> gas no longer draws through walls: `GASUBER_DEPTH_CLAMP` + `GasVisualRenderFeature` depth input/read wiring +
> `GasShaderMath.SceneDeviceDepth` + `GasShaderDepthMathTests`) AND the camera/replay plumbing (Open-Arena-Jet
> replay, LP1-Proof camera, `ApplyNow()`/`RefreshNow()`, serialized `GasRoomScene.unity` camera state) are DONE +
> merged on @26dd062. So the PLAN's step 1 is: OWNER-EYE what is already on @26dd062, then build ONLY the REMAINDER
> of Stage 1 — #2 THE STAND (designed greybox room ~8-10 m + motivated lamp/`GasLightBinder` + scale cube +
> mannequin capsule + ONE lit/dark toggle + finalize the 2 fixed camera bookmarks), #3 the OPEN-SPACE no-walls
> bookmark with directional-jet framing, #4 the fixed-seed restart + ONE serialized single-vent emitter config.
> Do NOT redo #1 (depth) or the camera path.
>
> ⚠ **v17/v18 (contract now v18):** the visual wiring-smoke must stay EXISTENCE-ONLY (`File.Exists`, NO source-text
> scan / `Does.Contain` / marker-grep — c-visual-005 retired the scanners; do NOT reintroduce any); any render/
> behavior claim is owner-eye + a real Unity/live-MCP run, NEVER a source scan (v17); the RESULT (per-leg
> `docs/results/c-visual-004.md`, RESULT-per-leg is live since c-030) may cite only review/ADR paths that EXIST at
> HEAD (v18). Stage 2+ stays HELD (W1b landed, but opening Stage 2+ needs a fresh owner check — not an auto cascade).
> Runs in a FRESH GasCoopGame_dev_2 session (never dev — engine cubes live there); dev_2→main merge owner-gated.
> Re-verify the CALL's assumptions (RealGasViewSource / VoxelSandboxDirector / GasRoomScene / GasUber.shader /
> GasParams layout) still hold on @26dd062 before building.
> [Superseded: the 2026-07-03 OPENED banner (base @bc25a33, dev_2 behind @40b94cc) is stale — base is now @26dd062.]

- direction: indie-game-development
- node: g-7e15 (VISUAL track)
- play: work (executor leg — GasCoopGame render/adapter layer; dev_2 → main when green)
- runs_in: a FRESH GasCoopGame_dev_2 session (the BUILD session; NOT the OS-worktree session)
- supersedes: the queued "designed gas demo scene" placeholder (c-visual-003's `next`) — this CALL IS that
  leg, reshaped as Stage 1 of work/gas-visual-plan-v2-2026-07-02.md
- opens_with: a PLAN (owner present). §Re-sync the GasCoopGame contract FIRST (dev_2 is behind main — merge
  main into dev_2 before anything else). Base = GasCoopGame main tip, currently @bc25a33 (post Sc-rep + Sc-kernel
  + W1a merges + the 2026-07-03 contract-v11 §Re-sync; re-check at open for any later merge).

## goal (outcome, not method)
Give the owner ONE place to honestly judge gas, ever after: a designed room + an open-space pad where the
CURRENT gas is staged fairly (motivated light, real scale, no walls hiding artifacts), where the gas no longer
draws through walls, and where any future look change replays on the identical canned motion for a fair A/B.

## what Stage 1 builds
1. **DEPTH COMPOSITE** (the pinned, time-critical fix): wire `ConfigureInput(ScriptableRenderPassInput.Depth)`
   + sample `resourceData.cameraDepthTexture` in the fullscreen gas pass; the march stops at scene depth
   (reversed-Z-consistent, same `_GasInvViewProj` already in use). Known limits to record, not hide:
   transparent props still don't write depth (gas still overdraws glass); a single motivated lamp per preset
   (a second simultaneous lamp ≈ +30–40% cost from a second shadow march — not in scope here).
2. **THE STAND**: one designed vertical room (~8–10 m) in canon greybox style (off-white/grey concrete,
   sparse props per StyleBible) with a floor for pooling, one motivated lamp + `GasLightBinder`, a 1 m cube +
   a player-height mannequin capsule for scale. ONE lit/dark toggle (not 3 presets — panel-trimmed; add more
   only if Stage 3's LP1 re-test needs it). 2 fixed camera bookmarks (near + room-wide) using the existing
   deterministic-framing camera path — a small serialized-pose script since Unity has no built-in bookmarks.
3. **ONE OPEN-SPACE BOOKMARK**: a no-walls pad (or the room's roof opened) with a directional-jet framing —
   gas spawns anywhere and directional jets in the open are a standing owner correction; every future stage-2+
   verdict must exist in both the room AND the open context, not room-only.
4. **REPEATABLE MOTION, no golden-replay library**: a fixed-seed restart button + ONE serialized emitter
   config (single-vent) on the existing `VoxelSandboxDirector` demo-control surface (reuses `SpawnAt`/
   `ValveOn`/jet fields — no new director capability). A second config (room-flood, same nozzle at higher
   rate) if cheap. Do NOT build a scenario-asset format or a canned-clip library — the sim is already
   deterministic; a restart + fixed config is sufficient and does not rot when Sc-reactions/Sc-typing later
   change sim behavior (a golden-clip library would).
5. **CAPTURE**: reuse the existing per-bookmark screenshot path; no new clip pipeline this leg.

## explicitly OUT of Stage 1 (moved to later stages, not silently dropped)
- LINEUP mode (3+ pods side by side) and the "two-gas-meet" replay: the real sim feed is single-species
  (`RealGasViewSource` hardcodes `G=0`/`TypeCount=1`) until Stage 2's W1b read-API lands — building lineup
  tooling now would render N identical-coloured clouds. Moves to Stage 4.
- Odin panel consolidation / per-profile save-load: duplicates the Stage 2 ScriptableObject schema work one
  stage later — do not build twice. Keep Odin v1 + the existing `GoodSampleAsset` A/B mechanism.
- 3-preset lighting rig, grey/chrome calibration spheres, Macbeth chart: a raymarched emissive volume has no
  surface BRDF for these film look-dev props to calibrate — they would pay no rent here.

## the process this leg MUST run by (unchanged owner-required discipline)
- NEVER-WORSE: `GoodSampleAsset` baseline kept; every change shown A/B vs it; worse = discarded, baseline
  unchanged.
- ONE THING AT A TIME: state in plain words what the owner will see and why it's better, before each sub-step.
- VERDICTS FROM THE PRIMARY BOOKMARK ONLY: one designated bookmark/preset/replay decides the gate; the other
  bookmark, the open-space pad, and free orbit are exploratory — notes, not verdicts.
- UNCERTAINTY COMES HOME: a confusing visual or a planning ambiguity → STOP and bring it home, never blind
  knob-thrashing.

## reading set (self-contained, GasCoopGame)
- live/indie-game-development/work/gas-visual-plan-v2-2026-07-02.md (the full staged plan this CALL belongs to).
- docs/gas-visual-stage-plan.md §S1/§S6+ (the look-lever menu; most already implemented — do not re-build).
- REUSE, do NOT rebuild: `RealGasViewSource` + `VoxelSandboxDirector` + `GasRoomSceneSetup`/`GasRoomScene`
  (the W1a room — restyle/extend rather than start over), `GasUber.shader`, `GasParams` buffer + `GridView`
  seam, `GasParamsLayout` reserved fields (do NOT consume any this leg — that is Stage 2), `GoodSampleAsset`.
- The canon minimal-gas-stage style note (OS history/s-canon-visual-style-minimal-gas-stage-001.md;
  StyleBible.md in the canon repo) — the room must match it.

## boundaries (STOP-and-escalate if hit — never a silent substitute)
- RENDER-ONLY (R13): ZERO `Core/**` edit; the sim is untouched; its tests stay green & UNCHANGED; UPLOAD-ONLY,
  no readback. The visual READS the sim; it never writes it.
- 96-byte `GpuGasParams` layout FROZEN THIS LEG — Stage 1 consumes NO reserved field; the layout-ADR is
  Stage 2's job, decided BEFORE any per-type polish, never silent.
- SCOPE = depth composite + the stand + the open-space bookmark + fixed-seed repeatable motion + capture.
  Lineup, multi-type, per-type schema, natural-jet fix, danger ladder, perf beyond depth-composite = LATER
  stages. Past that → STOP.
- A blocked/infeasible named approach, or a reduced-fidelity crutch, = mandatory STOP + escalate.

## done_when
- Opened with the PLAN, owner-signed; §Re-sync done first; the baseline saved before tuning.
- Depth composite: gas visibly stops drawing through a wall in an enclosed framing (before/after A/B, owner-eye).
- A presentable designed lit room exists, reproducible, driven by the REAL sim, restyled to canon greybox.
- The current gas in the new room reads visibly better than in the old boxy 6×4×6 box (before/after A/B).
- One open-space no-walls bookmark exists and is exercised with a directional-jet scenario.
- Fixed-seed restart reproduces identical motion across runs (verify: two consecutive restarts, same scenario,
  visually and via checksum where cheap).
- HEADLESS «точно»: tools/check.ps1 -Deliver GREEN; git diff Core/** EMPTY; sim tests UNCHANGED; C#↔HLSL stride
  gate green; no readback scan clean. RED-first only where there is genuine new mechanical surface (depth-
  composite reconstruction math, fixed-seed scenario config parsing); else say so honestly.
- OWNER-EYE — the BINDING gate: owner runs the stand, sees the two pinned before/afters, judged IN MOTION,
  signs off. No self-marking.
- RESULT comes HOME to OS (state_changes applied by a separate writer). dev_2 → main owner-gated.

## return
A RESULT routed home: outcome + evidence (the two before/after pairs + owner-eye sign + the updated
`GoodSampleAsset` baseline) + the next look slice (Stage 2 = schema + W1b consumption + real half-res).

## budget & rigor
Secondary visual-track cadence, owner-session-budget-constrained (~1 visual : ~2 engine while Sc-reactions is
in flight — see plan v2 §Calendar honesty). Fresh GasCoopGame_dev_2 session. Same contour as engine legs (CALL
→ PLAN → build → gates → RESULT home). Binding gate = the owner's EYE + the render-only regression invariants
(render-only — no heavy multi-agent refutation needed). May split at the PLAN if the depth-composite fix and
the stand turn out to have different natural checkpoints.

END_OF_FILE: live/indie-game-development/work/c-visual-004-call.md
