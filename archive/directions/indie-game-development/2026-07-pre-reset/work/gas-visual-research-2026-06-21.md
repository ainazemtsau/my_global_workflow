# Gas-Visual (GASG) — approach research (2026-06-21)

First step of the VISUAL track (node g-7e15), the owner asked for: *"how do we even DO the gas
visuals — there are many options — figure out the approach and write the structure."* This is the
research + the recommended structure, NOT a build. Source: deep-research `wf_e5924329` (95 agents, 3
search angles, 15 sources, 60 claims → 25 adversarially verified, 24 confirmed / 1 killed).

Owner framing folded in (this conversation):
- Visual is DECOUPLED from the engine: develop on FAKE/simulated data now, connect to the real sim later.
- It is a real parallel track, SECONDARY to the engine, started now (schedule risk if left to the end).
- FIŠKA «Живое Стекло» is CUT (already removed from canon — b274967 / s-repair-008); not a gas-visual concern.

---

## 1. The architecture verdict (high confidence)

There is **no single technique** — the right answer is a **layered architecture**, and the spine of it
is exactly the owner's "visual separated from implementation":

- **Layer 0 — authoritative sim grid (the ENGINE).** A coarse cell-centered density(+velocity) grid is
  the single source of truth (our existing integer "water" core / RN1). The classic Stam *Stable Fluids
  for Games* model is unconditionally stable and was real-time on 2003 hardware → trivially cheap on a
  2026 min-spec GPU; per-cell density + the emergent front ARE the WHERE / HOW-MUCH / boundary data the
  visual reads. *(verified 3-0; one sub-claim 2-1 — escaped by scoping to a COARSE grid.)*
- **Layer 1 — read-only client VIEW.** Each tick, upload the grid to the GPU (GraphicsBuffer or 3D
  texture) and render it. The visual **never simulates** — it only reads. (Enterprise analogy: a
  read-only reporting view / read-replica over a DB.) This is exactly the R13/R14 seam: a **fake data
  provider now**, swapped for the **real Wave-B front later with zero change to the visualizer**.
- **Layer 2 — distinctiveness ("soul").** Gas = the dominant saturated colour and the dominant light
  source in an otherwise desaturated world. INSIDE's GDC post-mortem *"Low Complexity, High Fidelity"*
  proves a deliberately minimal, LOCAL volumetric look — not a heavy full-scene system — carries a
  game's entire signature. Cheap-richness = one coherent stylized look. *(verified 3-0.)* Matches our
  existing art direction (gas-as-light).

---

## 2. The two viable render paths (both READ our grid) — high confidence

| Path | What it is | Best for | Watch-outs |
|---|---|---|---|
| **A. VFX Graph particles fed from our grid** | Unity's GPU particle system reads an external `GraphicsBuffer` via the *Sample Graphics Buffer* operator; a programmer (not artist) encodes per-gas-type look in **Custom HLSL**. Official since 2021.2, persists through VFX Graph 17.x / Unity 6; URP-supported. | Type-specific **accents**, reactive/flagship gases, front "sparkle". | Use `GraphicsBuffer` (legacy `ComputeBuffer` unsupported); needs compute/SSBO support (desktop only — fine for our min-spec); GPU-sync timing. *(3-0)* |
| **B. Custom URP raymarch pass over our grid** | A `ScriptableRendererFeature` + render pass raymarches a volume, sampling density from an uploaded 3D-texture / structured buffer of the grid. Proven in multiple open repos (vertexfragment, hylu.dev — the latter feeds a voxel grid into the raymarch loop explicitly). | The continuous **BODY** of the gas (concentration falloff, soft fronts). | **Min-spec perf is the unproven axis** — hylu.dev *abandoned* voxel raymarch for cost. Mitigate with half/quarter-res + depth-aware upsample. *(3-0; 1 sub-claim 2-1.)* |

They can **coexist over one buffer**: body via raymarch + accents via VFX particles.

**Min-spec lever (high confidence, 3-0):** render the volumetric pass at half/third/quarter resolution,
then recombine with a **depth-aware bilateral upsample** (preserves hard edges). Standard across shipping
volumetrics; grounded in Joint Bilateral Upsampling (Kopf et al. 2007).

---

## 3. What does NOT fit (saves money/time) — high confidence (3-0)

Off-the-shelf is **mostly architecturally mismatched** to "read-only view driven by OUR authoritative grid":
- **Zibra Effects / Liquids** — a *self-contained* internal simulator, steered only by force fields;
  **cannot** be driven by an external authoritative grid. (Only the separate ZibraVDB plays back pre-baked OpenVDB.)
- **URP-Fog-Volumes (free, MIT)** — density is animated 3D-texture **noise**; only a static `Texture3D` input,
  no live/compute/structured-buffer hook → needs custom modification; tested only on Unity 2022.3.
- **rajabala Volumetric-Particles**, **Valerio Marty's raymarcher** — self-generate density / single light,
  **no external-density path** without custom work.

**Conclusion:** this is written by hand (custom-but-feasible plumbing), not bought. The buyable pieces are
small helpers, not the core.

> Currency caveat: several cited samples predate URP 17 / Unity 6 **RenderGraph** (now default). The raymarch
> APPROACH is confirmed still valid under Unity 6 (CristianQiu repo); only the render-pass plumbing must be
> ported. Treat copied sample code as needing a RenderGraph port for our Unity 6.3 LTS target.

---

## 4. Multi-type readability (encoding scheme — to be designed)

Encode, per gas, so it reads at a glance:
- **TYPE** via hue / emission / motion signature (heavy = settling, low, cold hue; light = rising; fire = hot
  emissive; poison = sickly desaturating; flagship = a distinct silhouette/motion).
- **CONCENTRATION** via density / opacity.
- **FRONT / boundary** via a sharper edge term read from the grid's advection gradient.

⚠ **Open design unknown:** making MANY types readable *simultaneously* without colour/motion collisions is
NOT a solved/sourced problem — the research found single-field examples (INSIDE, fog-of-war), not a shipped
multi-type "gas legend". This is our design work, gated by the grey-box / owner-eye, not by a citation.

---

## 5. Proposed structure — the prototype sequence (the "структура")

Build in this order; each step de-risks the next. **Prove the data path and readability before any art.**

- **P1 (FIRST — de-risks the biggest unknown):** the grid→GPU **"pipe"** + a trivial single-gas render that
  just shows **WHERE + HOW-MUCH**. Reads the EXISTING RN1 (can start NOW). No art. → CALL `c-visual-001`.
- **P2:** add the **front/edge** read — prove a glanceable boundary. (Deepens when Wave B ships the real front;
  until then, a FAKE front provider feeds it.)
- **P3:** add a **SECOND gas type** — prove multi-type readability via the §4 encoding scheme.
- **P4:** **min-spec pass** — half/quarter-res + bilateral upsample; **measure on a real min-spec-class GPU**
  (the unproven perf axis). Gate P2/P3 expansion on P1+P4 evidence.
- **P5:** **distinctiveness pass** — desaturated world + gas-as-light (the INSIDE lever).

**Risky unknowns (gating):** (a) min-spec perf of a grid-fed raymarch is UNPROVEN — measure early; (b) Unity 6
RenderGraph port of any sample; (c) GPU sync (compute finishes before the visual samples); (d) per-tick grid→GPU
upload bandwidth, esp. when the sim is networked/authoritative at a lower tick rate than render.

**Decision gates:** choose raymarch-vs-VFX-vs-both only AFTER P1 proves the upload path and P4 gives a perf
number. Commit to art direction (P5) only after multi-type readability (P3) holds — never pin the "spectacular"
look to a stub sim.

---

## 6. Open questions carried (for the shape / later steps)
1. Measured frame cost on the actual min-spec target for a grid-fed raymarch vs a GraphicsBuffer-fed VFX field — which wins, or coexist?
2. Per-tick upload + GPU-sync strategy (double-buffer / AsyncGPUReadback timing) to feed the authoritative grid every frame without stalls.
3. The concrete multi-type visual-encoding legend (§4) — no shipped reference solved it; our design.
4. For reactive/flagship gas: does pure read-only hold, or does it need a little client-side derived animation (Custom HLSL secondary motion) kept deterministic/networked-consistent?

---

## 7. Sources (verified)
- Stam, *Stable Fluids for Games* (CMU/Clemson/NVIDIA GPU Gems 3 ch.30) — the coarse grid model.
- Unity 6 VFX Graph e-book + docs *Sample Graphics Buffer* operator; keijiro `VfxGraphGraphicsBufferTest`; drumath2237 — external-buffer → VFX.
- vertexfragment URP volumetric fog; hylu.dev volumetric fog-of-war (voxel grid → raymarch); Valerio Marty raymarched volumetrics; sinnwrig `URP-Fog-Volumes`; CristianQiu `Unity-URP-Volumetric-Light` (Unity 6 RenderGraph).
- INSIDE — GDC 2016 *"Low Complexity, High Fidelity"* (Gjoel/Svendsen) + Playdead lighting blog.
- Mismatch checks: zibra.ai (Effects/Liquids); rajabala Volumetric-Particles.
- Joint Bilateral Upsampling (Kopf et al., ACM TOG 2007) — the min-spec upsample.

Full raw findings (claims + votes + evidence) in the deep-research output for `wf_e5924329`.

END_OF_FILE: live/indie-game-development/work/gas-visual-research-2026-06-21.md
