# CALL c-visual-003 — WAVE 1: real gas in a real lit room (foundation) — RENDER-ONLY

- direction: indie-game-development
- node: g-7e15 (VISUAL track)
- play: work (executor leg — GasCoopGame render/adapter layer; dev2->main when green)
- runs_in: a FRESH GasCoopGame_dev_2 session (the BUILD session; NOT the OS-worktree session)
- supersedes: the c-visual-002 "S2 two-type + scatter-glow tuned in the empty analytic lab" framing (it
  degraded the look; re-planned to waves on the REAL sim — work/gas-visual-wave-plan-2026-06-29.md)
- opens_with: a PLAN (owner present). §Re-sync the GasCoopGame contract FIRST. Base at-or-after main @7d08882
  (clean — the degraded S2 work was uncommitted on dev2 and is being rolled back). The PLAN MAY SPLIT wave 1
  into visible sub-steps (each comes HOME with an owner-eye sign).

## goal (outcome, not method)
In a proper, presentable ROOM (not a void), OUR gas — driven by the REAL simulation — reads at a glance as a
real, especially-cool gas DOING ITS THING, with light visibly passing THROUGH the volume, and with two
genuinely DIFFERENT-character gases (heavy sinks dark&dense / light rises wispy&pale) readable in the same
room. The owner signs «ближе к жемчужине», judged IN MOTION on the real sim.

## what wave 1 builds (the foundation; draw look levers from docs/gas-visual-stage-plan.md §S1/§S6+)
1. REAL ROOM: a clean scene with a floor (heavy gas settles/creeps on it), walls + a known-size object for
   scale, a VISIBLE light source (lamp/window) positioned so its light goes THROUGH the gas, a fixed good
   camera. Driven by the REAL sim (RealGasViewSource + VoxelSandboxDirector; reuse the GasVoxelSandboxScene
   plumbing, dress it into a presentable room). NOT the analytic lab (that is now a helper only).
2. LIGHT THROUGH THE VOLUME: the lamp's light passes through the gas — thin parts glow/translucent, dense
   parts stay dark and opaque (the owner-agreed (г)+(в): real backlight + see-through, NOT self-glow alone —
   self-glow alone was the "jelly"). Scatter-glow remap of the self-shadow (§S6+ P1) is the "jelly" fix.
3. BASE-RENDER CLEANUP: smootherstep (quintic) coord-warp before the trilinear tap + a baked tiling 3D noise
   texture (inverted-Worley + Perlin) -> kill the "cubic / vertical-lines / grid" artifact (§S6+ P1, the
   biggest SHAPE jump). Detail-volume erosion if cheap.
4. TWO TYPES (first character): hook the visual to the now-existing multi-type engine substrate (c-exec-019):
   RealGasViewSource reads per-type (G channel = real dominantTypeId, not 0) and the scene spawns TWO gases;
   give each a different character via a reserved per-type field (RiseSinkBias buoyancy: heavy sinks / light
   rises) — reserved-field path, no 96B layout edit. (May be sub-step 1b, after 1a one-gas-in-the-room.)

## the process this leg MUST run by (the owner's required fix — build these, not just the look)
- NEVER-WORSE: keep the current best look saved as a one-click preset ("good baseline"). Show every change A/B
  vs the baseline. It becomes the new baseline ONLY if the owner sees it clearly better; if worse, DISCARD
  (baseline unchanged). The owner is never shown a regression as "progress."
- ONE THING AT A TIME: before each sub-step, state in plain words what the owner will see and why it's better.
- ONE CONTROL PANEL: every knob in ONE inspector, labelled in human words, nothing hidden — the owner can nudge
  and see live. A NAMED deliverable, not "buried in code."
- UNCERTAINTY COMES HOME: a confusing visual or a planning ambiguity -> STOP and bring it home, never blind
  knob-thrashing.

## reading set (self-contained, GasCoopGame)
- docs/gas-visual-stage-plan.md §S1, §S6+ (P1 levers: bake-noise, smootherstep, detail erosion, scatter-glow,
  analytical transmittance) — the look menu.
- REUSE, do NOT rebuild: RealGasViewSource + VoxelSandboxDirector + GasVoxelSandboxScene (the real-sim path),
  GasUber.shader (body), the GasParams buffer + GridView seam (ADR-0012..0016), GasParamsLayout reserved fields,
  GasConceptPresets (live switcher).
- The canon VISUAL-STYLE minimal-gas-stage note (OS history/s-canon-visual-style-minimal-gas-stage-001.md) — the
  room/stage must match the minimal world style; ask the owner to relay it if unavailable in the build repo.

## boundaries (STOP-and-escalate if hit — never a silent substitute)
- RENDER-ONLY (R13): ZERO Core/** edit; the sim is untouched; its tests stay green & UNCHANGED; UPLOAD-ONLY, no
  readback. The visual READS the sim; it never writes it.
- 96B GpuGasParams layout FROZEN — a new per-type field = a reserved-field assignment or a layout-ADR event,
  decided in the PLAN, never silent.
- SCOPE = wave 1 only (real room + light-through + base-render cleanup + first two-type). Alive motion (curl /
  natural jet), full per-type profiles, reactions, accents, the weak-HW perf pass = LATER waves. Past that -> STOP.
- A blocked/infeasible named approach, or a reduced-fidelity crutch, = mandatory STOP + escalate.

## done_when
- Opened with the PLAN, owner-signed; §Re-sync done first; the baseline saved before tuning.
- A presentable lit ROOM exists, reproducible, driven by the REAL sim.
- Light visibly passes THROUGH the gas (thin glows, dense stays dark).
- The "cubic/lines/grid" artifact is gone (smootherstep + baked noise).
- Two visibly-DIFFERENT-character gases (heavy sinks / light rises) read in the same room on the real sim.
- HEADLESS «точно»: tools/check.ps1 -Deliver GREEN; git diff Core/** EMPTY; sim tests UNCHANGED; C#<->HLSL stride
  gate green; no readback. RED-first only where there is genuine new mechanical surface (reserved-field decode,
  baked-asset format guard); else say so honestly.
- OWNER-EYE — the BINDING gate: owner runs the room, sees the gas (not jelly/cubic/blobs) + light-through + two
  different characters, judged IN MOTION, signs «ближе к жемчужине». No self-marking.
- RESULT comes HOME to OS (state_changes applied by a separate writer). dev2->main owner-gated.

## return
A RESULT routed home: outcome + evidence (render-only invariants + the owner-eye sign + the saved never-worse
baseline) + the next look slice (wave 2 = alive motion).

## budget & rigor
Secondary visual-track cadence in owner-gated engine build-gaps; no fixed hour quota. Fresh GasCoopGame_dev_2
session. Same contour as the engine legs (CALL -> PLAN -> build -> gates -> RESULT home). Binding gate = the
owner's EYE + the render-only regression invariants (no heavy multi-agent refutation — render-only). May SPLIT
at the PLAN.

END_OF_FILE: live/indie-game-development/work/c-visual-003-call.md
