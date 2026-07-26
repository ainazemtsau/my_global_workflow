RESULT s-research-gas-visual-tech-001 (owner plain message: gas visual technology options)
direction: indie-game-development   play: research   node/task: g-7e15/gas-visual-tech-research

outcome: |
  First bounded technology landscape for "more impressive gas visuals over the locked integer grid" is complete. The
  recommended direction is NOT an architecture reset and NOT a marketplace fluid sim: keep the data-driven URP raymarch
  body as the readable mass layer, then make it impressive through additive layers that read the same grid/event data:
  front/tendril accents, lighting/compositing, event-driven warning bursts, and one later flagship/special-gas module.

  Practical shortlist:
  1. KEEP / harden: one shared URP fullscreen raymarch body from GridView + GasParams. This remains the spine because it
     maps directly to where/how-much/type/front and preserves the read-only seam.
  2. ADD NEXT FOR WOW: VFX Graph or particle-system accents spawned/sampled from front cells and forced-flow vectors:
     tendrils, sparks, wisps, suction/jet streaks. These should never be the readability-critical body; they are flavor.
  3. ADD EVENT DRAMA: URP decals/projectors + pooled bursts + light/color-post pulses for reactions and danger. This
     gives "something is happening" without idle noisy sparkles.
  4. IMPROVE BODY SHADER BEFORE REPLACING IT: density-gradient edge, blue-noise/jittered raymarch, low-res body with
     depth-aware upsample, emission/scattering controls, camera-inside-gas clamp, and flow-biased procedural motion.
  5. RESERVE HERO GAS TECH: for anomalous gases only, use a special look module (procedural SDF/floor creep/hands or
     baked VDB/flipbook-like effect triggered by sim events). This is not the default gas system.
  6. AVOID AS CORE: Zibra/Obi/live fluid solvers, HDRP pipeline switch, shader-per-gas, and VDB playback as the live gas
     body. They can be cosmetic/rare-effect tools later, but they do not naturally accept our authoritative grid as truth.

  Recommendation for the next discussion/research: investigate "front/accent layer" first, because the current complaint
  is not that gas is unreadable in principle; it is that the result does not yet impress. A front/accent probe is the
  cheapest way to add motion personality while preserving c-visual-001's structure-first seam.

evidence: |
  Local state read first-hand:
  - live/indie-game-development/NOW.md g-7e15 parallel track and queued c-visual-001.
  - live/indie-game-development/work/gas-visual-research-2026-06-21.md.
  - live/indie-game-development/work/gas-visual-architecture-2026-06-26.md.
  - live/indie-game-development/work/c-visual-001-call.md.

  External/current sources checked:
  - Unity URP Full Screen Pass Renderer Feature: https://docs.unity3d.com/6000.1/Documentation/Manual/urp/renderer-features/renderer-feature-full-screen-pass.html
  - Unity VFX Graph Sample Graphics Buffer: https://docs.unity3d.com/Packages/com.unity.visualeffectgraph%4012.1/manual/Operator-SampleBuffer.html
  - Unity URP Decal Renderer Feature / Decal Projector: https://docs.unity3d.com/Packages/com.unity.render-pipelines.universal%4014.0/manual/renderer-feature-decal.html and https://docs.unity3d.com/6000.0/Documentation/Manual/urp/renderer-feature-decal-projector-reference.html
  - Unity HDRP Local Volumetric Fog: https://docs.unity3d.com/Packages/com.unity.render-pipelines.high-definition%4017.0/manual/local-volumetric-fog-volume-reference.html
  - Unity Particle System Force Field: https://docs.unity3d.com/6000.4/Documentation/Manual/class-ParticleSystemForceField.html
  - Zibra Liquid glossary / Zibra smoke-fire case material: https://www.zibra.ai/blog-posts/zibra-liquid-glossary and https://www.zibra.ai/case-studies/enhancing-game-visuals-with-zibra-liquid-and-zibra-smoke-fire-a-creators-journey
  - Obi Solver / Obi Emitters: https://obi.virtualmethodstudio.com/manual/6.3/obisolver.html and https://obi.virtualmethodstudio.com/manual/6.3/emitters.html
  - Joint Bilateral Upsampling, spatiotemporal blue noise, GPU Gems volumetric light scattering: https://www.microsoft.com/en-us/research/publication/joint-bilateral-upsampling/ , https://developer.nvidia.com/blog/rendering-in-real-time-with-spatiotemporal-blue-noise-textures-part-1/ , https://developer.nvidia.com/gpugems/gpugems3/part-ii-light-and-shadows/chapter-13-volumetric-light-scattering-post-process
  - NanoVDB / ZibraVDB fit check: https://developer.nvidia.com/nanovdb and https://www.zibra.ai/zibra-vdb-compression

state_changes: |
  LOG.md: + the s-research-gas-visual-tech-001 line.
  history/: + s-research-gas-visual-tech-001.md (this full RESULT).
  NOW.md: no change; c-visual-001 remains queued and build-ready.

captures:
  - Potential next research: "front/accent layer over GridView" — compare VFX Graph GraphicsBuffer, classic ParticleSystem+ForceField, and custom instanced quads/tubes; output should be a single probe design.
  - Potential next research: "body shader upgrade pack" — what concrete shader features make the current raymarch look expensive without changing data contract.
  - Potential later probe: one flagship anomalous gas visual module, deliberately outside the shared-body rule but read-only and cosmetic.
  - Avoid buying/building full live fluid solvers as core gas truth; evaluate them only as cosmetic overlays or rare hero effects if a specific gas demands it.

decisions_needed:
  - q: Which visual research branch should be opened next?
    options: [front/accent layer, body shader upgrade, hero/special gas module]
    recommendation: front/accent layer, because it is the shortest path from "works but not impressive" to motion/personality while keeping the existing c-visual-001 seam intact.

play_check:
  - 1 Recite: done — owner approved option 1 ("как получить впечатляющий газ поверх integer grid без смены авторитетной физики?") with "ок"; return format = practical technology shortlist + recommendation.
  - 2 Investigate: done — read current visual-track state and local architecture/CALL docs; checked Unity/Zibra/Obi/VDB/rendering sources.
  - 3 Confidence: done — established facts separated from inference below.
  - 4 Close: done — findings returned as a bounded research RESULT; no NOW change proposed.

confidence: |
  Established: URP fullscreen passes, VFX Graph GraphicsBuffer sampling, URP decals, and Unity particle force fields are real compatible primitives for read-only visual layers; HDRP has stronger built-in volumetric fog than URP but implies a pipeline shift; Zibra/Obi are independent simulation systems built around their own emitters/solvers/manipulators, not a natural live rendering backend for our authoritative grid.
  Inference: the fastest path to "impressive" is a hybrid visual stack (body + front accents + event drama), not a new physics model. This could change if the current Cloudy Code implementation already has strong front accents and still fails; I did not inspect screenshots/video, so the exact failure mode is not diagnosed.

log: research (g-7e15, s-research-gas-visual-tech-001): gas visual tech landscape completed; rec = keep URP raymarch body as readable mass, add front/accent + event-drama layers for "wow"; avoid live fluid solvers/HDRP switch as core.

next: |
  awaiting_decision: choose the next visual research branch — recommended = front/accent layer over GridView (VFX Graph vs ParticleSystem/ForceField vs custom instanced geometry), because it best targets the owner's "works but not impressive" complaint without changing the locked read-only visual architecture.

END_OF_FILE: live/indie-game-development/history/s-research-gas-visual-tech-001.md
