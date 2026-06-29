# CALL c-visual-002 — gas-lab (unclipped, in-motion) + cloud look + early two-type-character probe

- direction: indie-game-development
- node: g-7e15 (VISUAL track)
- play: work (executor leg — GasCoopGame render/adapter layer; dev2→main when green)
- runs_in: a FRESH GasCoopGame_dev_2 session (the BUILD session; NOT the OS-worktree session)
- opens_with: a PLAN (owner present). §Re-sync the GasCoopGame repo contract FIRST, then PLAN — exactly like an engine leg. The PLAN is a PROPER plan (full discipline). HONEST SIZE: this is NOT a tiny step — a lab scene + characteristic motion + an unclipped volume + the resting look + an early per-type probe. The PLAN MAY SPLIT it (e.g. lab+unclipped+motion first → then the two-type probe); a split is fine as long as each part comes HOME with an owner-eye sign.

## provenance — this CALL was VALIDATED, not adopted

The earlier draft borrowed the dev plan (docs/gas-visual-stage-plan.md §S6+). An adversarial check against the REAL dev2
code (wf, ground-truth + skeptical critique + refute referee) KEPT the plan's spine (gas-lab → look levers → per-type
character) — it does NOT need a re-spine — but found two real holes + one thing to reconsider, all folded below. Where
this CALL differs from the stage-plan doc, THIS CALL WINS; the PLAN annotates the doc with these corrections.

VERIFIED root cause of «блекло» (in code, not a guess): NOT a weak shader (GasUber.shader is already feature-rich —
FBM + inverted-Worley + self-shadow + gradient-normal key light + fresnel + toon-band + per-type colour ramp + curl
motion, ~40 knobs). The dullness is (a) the COARSE sim grid (OpenArena 5x16x5 / rooms 3x3x4 cells, cellSize 1.0)
trilinearly upsampled, and (b) the HARD AXIS-ALIGNED BOX AABB that clips the cloud into a rectangle
(GasVisualRenderFeature sets `_GasVolMin/Max` from `WorldBounds`; GasUber.shader hard-discards rays outside the box).

## goal (outcome, not method)

In a dedicated, convenient test scene where the gas is NEVER clipped into a rectangle, OUR gas — shown DOING ITS THING
(spawn / jet / creep) — reads at a glance as a real, especially-cool gas, AND two genuinely DIFFERENT-character gases
can be seen in the same volume at once. The owner signs «ближе к жемчужине».

## the 3 validated changes (vs the borrowed plan) — these are the point of this leg

1. **UNCLIPPED test scene (owner-requested).** Build a SEPARATE, convenient gas-lab scene (open space, no level walls,
   clean fixed camera + light, easy to re-open/iterate). The gas must NOT show a rectangular cut: the volume bounds are
   generous and the cloud density fades to zero WELL INSIDE them (soft falloff), so the box edge is never visible —
   verify from MULTIPLE camera angles. (The box-AABB clip is a code-confirmed root cause of the distorted perception.)
2. **Gas IN MOTION, not a frozen puff.** The lab drives the GridView with a scripted CHARACTERISTIC-MOTION loop over
   time — a spawn bloom + a directional jet + a slow creep — because OUR gas's identity is motion-borne. Do NOT tune the
   look on a motionless sphere (a still-ball look transfers poorly the moment real jets arrive). The existing render-only
   curl is cosmetic billow, not this.
3. **Front-load an early TWO-TYPE-CHARACTER probe (the owner's headline, pulled forward).** Today every shape/motion/
   light lever is GLOBAL — only colour is per-type — so two gases cannot differ in CHARACTER on one screen (the "4
   concepts" are mutually-exclusive whole-screen presets). This is a BOUNDED fix, not a rewrite: the GasParams buffer is
   already per-type-indexed (colour already varies per `dominantTypeId`), and the frozen 96B layout already has RESERVED
   per-type fields (RiseSinkBias / Temperature / State / HazardReactive / BehaviorModuleId). Drive ONE shape-or-motion
   lever per-type from a reserved field so TWO visibly-different-character gases (e.g. heavy-sinking vs buoyant-wispy)
   render in the SAME volume at once. This validates "types differ by CHARACTER" EARLY instead of at the finale. Make the
   reserved-field-vs-layout-ADR micro-decision now (cheap — reserved fields exist); keep FULL per-type profiles for later.

## reconsider (flagged, not yet decided) — the "jewel" levers

The borrowed plan picked the SAFE levers (bake-noise, smootherstep, scatter-glow = "tasteful default smoke" — the
plateau) and SKIPPED the DIFFERENTIATING ones (light scattering THROUGH the volume / glow-through, emissive cores for
reactive types, anisotropic stretch ALONG a jet/velocity, jet-head/trail shaping) as "photoreal-overkill under
stylization" — but that skip-list was written when TOON was assumed; the owner REVOKED that ("toon not required, gas is
the JEWEL, unique"). So in the PLAN, pick levers by DIFFERENTIATION (does it widen the gap between two archetypes /
make the gas look UNIQUE), not just niceness; treat bake-noise/smootherstep/detail-volume as supporting polish. (The
deep strategic pass on "the single biggest jewel lever" failed mid-analysis; its lead was "light-through-the-volume,
not more form/noise" — surface this in the PLAN as an owner decision, do not silently skip it again.)

## reading set (self-contained)

- GasCoopGame `docs/gas-visual-stage-plan.md` — §Aesthetic target, §S1, §S6+ (the levers + diagnosis). Annotate it in the
  PLAN with the 2 corrections (free-puff→in-motion; per-type character forward, not finale).
- REUSE, do NOT rebuild: `GasUber.shader` (body), `RealGasViewSource`, the `GasParams` StructuredBuffer + GridView seam
  (ADR-0012/0013/0014/0015), `GasConceptPresets` (the live look-switcher). Note `GasParamsLayout.hlsl` reserved fields.
- `AGENTS.md` / current build + gate conventions (the §Re-sync target).

## open with this PLAN (owner present — a proper, full plan)

1. **§Re-sync** the GasCoopGame repo contract BEFORE touching anything.
2. **Ingest** the reading set; annotate the stage-plan doc with the 2 validated corrections; state REUSE vs ADD.
3. **Decide the HOW, put each to the owner with a recommendation:** (a) the unclipped lab scene — bounds + soft-falloff
   approach that guarantees no visible rectangular cut; (b) the characteristic-motion loop — how spawn/jet/creep drive
   the GridView over time (real sim source vs a scripted fake motion source); (c) the two-type probe — WHICH one lever
   goes per-type and WHICH reserved field carries it (RiseSinkBias/Temperature/State…), and the reserved-field-vs-ADR
   call; (d) which DIFFERENTIATING look levers to try first. Surface every genuine fork as an owner decision.
4. **Name the gates** (done_when) + the render-only invariants. If a needed change would touch `Core/**` or the sim →
   STOP and escalate.
5. **Owner signs the PLAN** (incl. any SPLIT) before build.

## boundaries (STOP-and-escalate if hit — never a silent substitute)

- **RENDER-ONLY (R13):** ZERO `Core/**` edit; the sim is untouched; the 977 sim tests stay green & UNCHANGED; no
  `VoxelField` handle; UPLOAD-ONLY (no readback into the sim). A motion loop in the LAB drives the GridView for display
  only — it is NOT a new sim and never feeds back.
- **96B `GpuGasParams` layout FROZEN** — a new per-type field = a reserved-field assignment or a layout-ADR event,
  decided in the PLAN, never silent.
- **SCOPE:** this leg = the unclipped lab + characteristic motion + the resting look + the ONE two-type probe. Full
  per-type profiles for ALL archetypes, the full jet-shape system, behaviour, particle accents, and the weak-HW perf
  pass are LATER legs. If the build reaches past the probe → STOP.
- **PERF is UNVERIFIED, not "a free bolt-on":** `resolutionScale` is currently identity and weak-HW cost is UNMEASURED.
  Do not let "optimize later" be treated as settled. Name a min-spec GPU and take a free non-gating home frame-cost
  reading once the lab exists; a real perf pass is a later leg.
- A blocked/infeasible named approach, or a reduced-fidelity crutch, = mandatory STOP + escalate.

## done_when

- Opened with the PLAN above, owner-signed; §Re-sync done first.
- The UNCLIPPED lab scene exists and is reproducible; the gas shows NO rectangular cut from multiple camera angles.
- The gas runs its CHARACTERISTIC-MOTION loop (spawn + jet + creep) in the lab.
- The TWO-TYPE probe renders two visibly-DIFFERENT-character gases in the same volume at once (one per-type shape/motion
  lever driven from a reserved field).
- **HEADLESS — the «точно» half:** `tools/check.ps1 -Deliver` GREEN; render-only invariants hold — `git diff Core/**`
  EMPTY; the 977 sim tests UNCHANGED; the C#↔HLSL stride gate green; no readback. RED-first only where there is genuine
  mechanically-testable NEW surface (e.g. a reserved-field decode, a baked-asset format guard); if none, say so honestly.
- **OWNER-EYE — the BINDING gate (not unit-testable):** owner opens the lab, sees the gas DOING ITS THING (not blocky,
  not jelly, not a rectangle) and two types reading as DIFFERENT CHARACTERS, and signs «ближе к жемчужине». Owner-run,
  judged IN MOTION, no self-marking.
- The RESULT comes HOME to OS (state_changes applied by a separate writer); NO off-contour merge. dev2→main owner-gated.

## return

A RESULT routed home: outcome + evidence (the render-only invariants + the owner-eye sign + the two-type probe result)
+ the next look slice.

## budget & rigor

~40-60 min/day owner-gated build-gaps; a fresh GasCoopGame_dev_2 session. SAME contour as the engine legs
(CALL → proper PLAN → build → gates → RESULT home). Right-sized rigor: the binding gate is the owner's EYE + the
render-only regression invariants; no heavy independent-RED-test-author + multi-agent refutation round (nothing
correctness-critical to refute — render-only). This right-sizes the GATE; it does not skip the contour, the §Re-sync,
or the PLAN. May SPLIT at the PLAN (each split still comes home with an owner-eye sign).

END_OF_FILE: live/indie-game-development/work/c-visual-002-call.md
