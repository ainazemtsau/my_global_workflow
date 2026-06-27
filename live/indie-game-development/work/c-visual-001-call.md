# c-visual-001 — build-step 1 executor CALL (gas-visual, structure-first)

Authored + adversarially hardened 2026-06-26 (s-visual-004) — workflow `wf_5dd9d57a-142` (4 review lenses:
Unity-6.3 feasibility / scope-boundary / done_when-verifiability / read-only-discipline → synthesis). Re-specs the
stale pre-structure-first `c-visual-001` placeholder (was "grid→GPU pipe over RN1"). Build-step 1 of
`work/gas-visual-architecture-2026-06-26.md` §7.

---

CALL c-visual-001  (re-specs the stale pre-structure-first c-visual-001 placeholder)
to: executor   direction: indie-game-development   node: g-7e15 (VISUAL parallel track)
repo: ainazemtsau/GasCoopGame   kind: engineering   surface: cli (GasCoopGame_dev)

goal: |
  A WORKING gas-visual on the developer's HOME machine: a FAKE gas volume renders in the game view showing WHERE the
  gas is and HOW MUCH (concentration -> opacity, type -> color, plus a visible edge), driven entirely by a read-only
  per-cell data source through a one-way SEAM — proving the data-driven visual pipeline end-to-end on FAKE data, with
  the engine-swap seam and its byte-layout discipline locked as a CHECKED gate that freezes the FINAL buffer layout
  (the one later steps fill unchanged). Build-step 1 of work/gas-visual-architecture-2026-06-26.md (§7 step 1). Crude
  visuals are fine; the SYSTEM is the point.

context: |
  Input evidence (NOT a binding spec — the doc owns the data model; the CALL does not re-specify it):
  work/gas-visual-architecture-2026-06-26.md (§1 layers, §2 GasParams field contract, §3 one-uber-shader-by-data,
  §4 channels, §5 read-only/no-writable-handle guarantee, §7 step 1) + work/gas-visual-research-2026-06-21.md
  (URP raymarch body; half/quarter-res + bilateral-upsample is a LATER min-spec lever). Rules R13/R14 (sim CORE pure
  C#, zero Unity refs; Unity = render/input/transport adapters only). Unity 6.3 LTS / URP 17 (RenderGraph default).
  RN1 (the real engine read-model) EXISTS (S0 @824948d) but is UNUSED this leg — fake source only; the real swap is
  step 6.
  Perf is DE-GATED this leg (owner steer d-visual-buildstep0-001; owner has no min-spec machine): a perf number does
  not change the architecture, only later tuning knobs or, worst case, a body-renderer swap the read-only seam makes
  cheap.

boundaries: |
  - FAKE data only: a FakeGasViewSource fills the source. ONE settable fake blob (a type + a density it can vary) is
    the COMPLETE slice; authoring the 3 parameter-extreme fixtures as assets is STEP 2, not required here.
  - The seam references NO engine / RN1 / snapshot types and is handed NO writable sim or grid handle — the read-only
    guarantee is STRUCTURAL (there is no handle to write through; §5), not a matter of builder restraint. The visual
    writes nothing to any sim/grid (R13).
  - The seam is UPLOAD-ONLY: data crosses the engine->visual line one-way by GPU upload; the visual never reads back
    from GPU into the sim (no AsyncGPUReadback into sim state). This is the property that makes it provably unable to
    stall or desync co-op (§5) — keep it, the HOW is the PLAN's.
  - The shared visual-buffer struct definitions live on the RENDER/ADAPTER side (a render-side shared assembly), NEVER
    in the engine-free Core — a headless stride TEST does not require the types to sit in Core, and putting them there
    would contaminate the R13 boundary.
  - FIXED bounded region this leg: the per-cell view covers a flat, bounded volume; full re-upload per change is fine.
    Camera-region SCROLLING / clipmap re-centering (write-only-the-new-slab) is DEFERRED to the perf pass — keep the
    addressing scheme such that it CAN later become scrolling behind the seam without touching the body/shader, but do
    NOT build the slab/toroidal upload here.
  - FRONT this leg = a flat density-gradient edge at body resolution. The depth-composited FULL-RES front (camera-depth
    sampling, ConfigureInput(Depth) / intermediate-texture wiring) is DEFERRED to step 3's readability bar — do not
    pull camera depth into this leg.
  - Type params crossing the seam must be GPU-friendly: any curve-typed param (e.g. densityToOpacity) is BAKED to a
    value / small LUT on the GPU side — no managed AnimationCurve crosses the seam. (Flag, not a design: the PLAN owns
    the bake.)
  - INVARIANT (build constraint, evidenced by a shader-source review note in the RESULT, NOT a unit gate this leg):
    the body shader is branch-free per sample — every type param is a multiply/lerp weight, never if(typeId==X). Its
    binding stress test is the many-types/overlap leg (step 3).
  - NO aesthetics polish; NO warning CHANNEL (step 4 — but see done_when (1) re reserving its field); NO special-gas
    behavior (step 5 reserves only the bare hook); NO real-engine swap (step 6); NO double-buffering; NO required VFX
    accent layer; NO secondary-type blend / N-way mixing (single-dominant-per-cell only); NO half-res + bilateral-
    upsample pipeline (the resolution knob is a PARAMETER that exists, not a license to build the upsample chain).
  - A NEW render scene/feature (fork-by-copy); do NOT co-edit the engine's gas scenes / Core.

done_when: |
  Opens with a PLAN (owner present). Items (1)-(5) are HEADLESS / mechanically checkable (the binding non-owner
  evidence); item (6) is the ONLY owner-run gate. No item in (1)-(5) may be marked done by eye.
  (1) SEAM + FROZEN LAYOUT: a one-way producer interface (IGasViewSource) fills TWO GPU resources — a per-cell
      GridView volume + a per-type GasParams buffer (a GraphicsBuffer, NOT legacy ComputeBuffer; a blittable struct,
      no bool/managed fields, explicit 16-byte / float4 alignment), carrying the agreed §2 GasParams fields. A
      FakeGasViewSource fills both. This leg DECIDES the warning-granularity fork (§6 unknown #5: warningFlag per-cell
      in GridView vs per-type-global in GasParams) and freezes the layout reflecting that decision — so the stride the
      gate certifies is the FINAL one that steps 4/6 fill UNCHANGED, not a layout a later step must re-cut. State which
      field set each resource locks. (PLAN chooses Texture3D-vs-StructuredBuffer for GridView; the stride gate below is
      meaningful for the GasParams STRUCT specifically — a Texture3D GridView has a texel-FORMAT contract, gated
      accordingly.)
  (2) BODY: a single shared URP 17 RenderGraph fullscreen raymarch pass marches GridView and styles each sample by
      GasParams[dominantTypeId]; the fake blob renders WHERE + HOW-MUCH + a visible edge.
  (3) STRIDE-CONFORMANCE GATE (binding, headless, two passing greens):
      (3a) a single DECLARED expected-stride constant (bytes per GasParams element; per GridView cell/texel) is
           asserted GREEN to match BOTH the C# blittable struct size AND the documented HLSL buffer layout — the test
           fails if EITHER side diverges from the constant (not a C#-against-C# self-check).
      (3b) a negative-control test that injects a WRONG stride and asserts the gate REJECTS it — this test itself goes
           GREEN in the RESULT, proving the gate has teeth (a passing artifact, not an unobservable "would red-fail").
  (4) DATA PATH (headless): a test changes a GasParams field and asserts the GPU buffer the body samples changes
      accordingly — the data->picture path is exercised mechanically (the "visibly changes" observation lives in (6)).
  (5) the 2 body knobs (render-resolution scale + raymarch step count) exist as parameters; a rough HOME-machine
      frame-cost reading is captured (frame timer / GPU timestamp on the home machine, NOT the editor Stats overlay)
      and RECORDED AS A NUMBER IN THE RESULT (non-gating).
  (6) OWNER-EYE (binding, non-unit-testable; the SOLE owner-run axis): owner presses Play and confirms in plain words
      that he SEES the fake gas — its color tells the type, denser = more opaque, it has a visible EDGE / boundary (not
      a uniform fog filling the whole screen), AND when a number in FakeGasViewSource is changed the body visibly
      changes. Item (2) BUILDS the front/body; the owner-eye gate is what BINDS its readability. Owner-run, no
      self-marking.

return: |
  RESULT: commits/PR + the render scene/feature + the green stride gate (3a) AND the green negative-control (3b) + the
  green data-path test (4) + the recorded home frame-cost NUMBER + the owner-eye confirmation; the seam (the two
  resources, with the warning-granularity decision and the frozen field set/stride named) documented as the stable
  interface a later RealGasViewSource fills UNCHANGED, referencing no engine types and holding no writable handle.

budget: one build leg (a few GasCoopGame_dev sessions at the owner's cadence).

---

## Hardening provenance (wf_5dd9d57a-142)

Folded must/should-fixes (the draft was tightened on all four lenses):
- Clipmap/scroll-without-re-upload DOWNGRADED → fixed bounded region + full re-upload this leg; scrolling deferred to the perf pass (kept swap-able behind the seam). [biggest stall risk, flagged by all 4 lenses]
- Depth-composited full-res front SCOPED OUT → flat density-gradient edge at body resolution this leg; depth wiring deferred to step 3.
- Warning-granularity fork RE-ADDED → this leg DECIDES warningFlag placement and freezes the FINAL layout/stride so steps 4/6 fill it unchanged.
- Stride gate rewritten → a single declared expected-stride constant asserted against BOTH the C# struct size AND the documented HLSL layout (kills the C#-vs-C# self-mark loophole) + a PASSING negative control (inject wrong stride, assert rejection, test goes green).
- "data-drives-picture" SPLIT → headless data-path test (4) + the eye judgment moved into the owner-eye gate (6); items 1–5 may not be marked by eye.
- Added the UPLOAD-ONLY / no-readback boundary + the NO-WRITABLE-HANDLE + references-no-engine-types boundary (read-only guarantee made STRUCTURAL per doc §5).
- GraphicsBuffer (not ComputeBuffer); 16-byte/float4-aligned blittable struct (no bool/managed); curve params baked to value/LUT (no managed AnimationCurve crosses the seam); struct defs on a render/adapter-side assembly, never Core.
- "branch-free per sample" demoted from a gate to a boundary INVARIANT (evidenced by a shader-source note; binding stress = step 3).
- Frame-cost reading = a NUMBER in the RESULT via a home-machine frame timer/GPU timestamp (not the editor Stats overlay).

## Residual risks (carried, accepted)
- The warning-granularity decision is required + must be NAMED in the RESULT, but the QUALITY of that decision is not itself gated here — a hasty choice could leave the frozen stride sub-optimal for step 4.
- "Addressing can later become scrolling without touching the body/shader" is asserted but NOT tested this leg (scrolling deferred); a later perf-pass swap could surface a seam coupling the fixed-region v1 did not exercise. Accepted (consistent with the doc deferring clipmap churn).
- The stride gate asserts C# against a DOCUMENTED HLSL layout constant, not a live HLSL-compiled reflection; if the HLSL source later drifts from its documented layout the gate would not auto-catch it. True C#↔compiled-HLSL reflection left to the PLAN if cheap.
- Owner-eye is the sole binding readability axis; a subtly-wrong front/opacity could pass a loose plain-words confirmation. Inherent to a non-designer owner-eye gate; accepted by project policy.
- The home frame-cost number is NON-gating; a comfortable home number says nothing about min-spec — the RESULT must label it a smell test, not a verdict.

## Left to the builder PLAN (CALL hygiene — not over-specified)
- Texture3D vs StructuredBuffer for the GridView volume.
- The actual warning-granularity decision (per-cell vs per-type-global) + which field set each resource locks.
- The raymarch step scheme, sample accumulation, and how the flat density-gradient front is reconstructed at body resolution.
- How curve params are baked (single value vs small LUT) + GasParams field packing within the 16-byte alignment.
- The mechanism of the stride-conformance test + how the negative control injects a wrong stride.
- How the fixed-region addressing is structured so it can later become scrolling/clipmap behind the seam.
- Which render-side shared assembly hosts the struct defs; the IGasViewSource / FakeGasViewSource shape.
- How the home frame-cost reading is captured (frame timer vs GPU timestamp).

END_OF_FILE: live/indie-game-development/work/c-visual-001-call.md
