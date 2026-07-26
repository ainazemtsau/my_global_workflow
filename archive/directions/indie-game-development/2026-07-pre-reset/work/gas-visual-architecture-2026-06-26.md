# Gas-Visual (GASG) — the procedural visualization ARCHITECTURE (structure-first) — 2026-06-26

VISUAL track **g-7e15**, session **s-visual-002**. The owner steered STRUCTURE-FIRST: build the procedural,
parameter-driven visualization ENGINE (params → picture; new gas type = DATA not code; many types; performant)
BEFORE the visual-design grammar. Crude visuals are fine for v1; the SYSTEM must really work and be extensible.

Source: deep-research workflow `wf_579651ba-7f9` (13 agents — 5 architecture dimensions each adversarially
verified, a draft synthesis, a solo-dev over-engineering critic, a final incorporating the critique). Builds ON
(does NOT relitigate) `work/gas-visual-research-2026-06-21.md` (the layered read-only architecture + the two
render paths: URP raymarch for the body, VFX-Graph particles for accents).

Owner decisions ratified this session (the scope these answers honor):
1. STRUCTURE-FIRST — research the architecture (param→picture, extensibility, perf); defer palettes/legend/which-gases.
2. TEST FIXTURES = 3 PARAMETER-SPACE EXTREMES ("heavy+cold+settles" / "fire-state light+hot+emissive" /
   "reactive+telegraphs"), NOT a lore roster, NO "neutral" gas.
3. RESERVE a seam for "special" gases with their OWN behavior/animation (fog-creeps-and-grows-hands); build look-only v1.

> ENGINE-GROUNDING CORRECTION: some research agents described Layer 0 with a borrowed "verdict E / float clouds-far"
> framing. That is NOT our engine. Our authoritative gas engine (g-9c41) is the **integer, deterministic,
> host-authoritative LAYERED coordinating grid** (gas at 50cm; per `knowledge/g9c41-gas-engine-SPEC.md`). The
> visual conclusions are unaffected: the visual only needs a **read-only per-cell/per-region snapshot + discrete
> warning events** from a host-authoritative sim, which the integer grid provides exactly. Everywhere below,
> "Layer 0" = our integer layered grid.

---

## 1. THE STRUCTURE — four layers + one reserved hook

The visual is a **read-only view** over the authoritative grid (the sim simulates; the visual only reads and draws —
a read-only dashboard over a database). The decoupling is literal: a one-way seam so we develop on FAKE data now and
swap to the real engine later with ZERO change to the drawing layers.

| Layer | Role | Reads | Writes |
|---|---|---|---|
| **0 — Engine** (out of scope for the visual) | The authoritative integer layered grid (g-9c41), host-authoritative + deterministic. The single truth of where gas is, how much, which type, the front, and danger events. | nothing from the visual | publishes, once per sim tick, (a) a per-cell coarse snapshot of the camera-relevant region, (b) discrete WarningEvents {kind, pos, severity, ttl}. Writes only *downward* across the seam. |
| **1 — Seam** (FAKE now / real later) | The decoupling boundary. A thin producer `IGasViewSource` that fills the GPU buffers. v1 ships `FakeGasViewSource` (scripted blobs/the 3 extremes); later `RealGasViewSource` bridges the engine snapshot with ZERO change to Layers 2–3. Guarded by a **stride-conformance test** (C#/HLSL agree on the struct layout byte-for-byte — the classic silent-corruption bug). | engine snapshot + events (real impl); nothing (fake impl) | TWO GPU buffers: **GridView** (per-cell {density, dominantTypeId, frontStrength, warningFlag} ≈ RGBA32, addressed as a scrolling/clipmap 3D texture so camera motion re-centers by writing only the new slab, never re-uploading the whole volume) + **GasParams** (one small element per type). Upload-only, no read-back → cannot stall or desync the sim. |
| **2 — BODY channel** (steady-state) | The at-a-glance body: where / how-much / which-type / front. ONE shared, type-agnostic URP raymarch fullscreen pass (RenderGraph / URP 17 Full Screen Pass) that marches GridView and styles each sample by `GasParams[dominantTypeId]`. Body MASS at half/quarter res + depth-aware bilateral upsample; the FRONT is reconstructed at FULL res against the depth buffer so it stays sharp (the readability cue is not degraded by the cheap low-res body). Camera-inside-gas clamps to a "submerged" ceiling instead of washing the screen opaque. | GridView + GasParams (read-only on GPU); camera depth | only the camera color. The OPTIONAL accent VFX path (feature-flagged) reads the SAME buffers, emits particles only. |
| **3 — WARNING channel** (event-driven) | The OFF-by-default danger telegraph, decoupled from the body. A client-local `TelegraphDirector` + `WarningRegistry` of ScriptableObjects. Fires ON only when Layer 0 raises a replicated event (sim-side hysteresis). DEFAULT primitive = URP **Decal Projectors** (floor markers, no compute needed); OPTIONAL = pooled VFX bursts. This is the AUTHORITATIVE channel for the player's danger read. | replicated WarningEvents (one-way); a WarningKindSO by stable id | only its own pooled cosmetic objects + the camera image. Never the grid/sim. |
| **Special-gas SEAM** (reserved hook) | The extension point for gases needing their OWN behavior/animation. v1 ships ONLY the cheapest reservation: a nullable `behaviorModule` field on the type definition (null for all v1 types) + ONE null-guarded call-site + a TODO. NO frozen interface in v1 — its real shape is designed by the post-v1 floor-fog spike that first exercises it. | v1: nothing. Later: a read-only snapshot view (no writable grid handle → contamination impossible by construction). | v1: nothing. Later: only its own client-local cosmetic buffers. |

---

## 2. THE DATA MODEL — the parameter contract IS the structure

A new ordinary gas type = ONE `GasTypeDefinition` ScriptableObject asset. Its fields (the parameter contract every
gas exposes, packed into the `GasParams` GPU buffer):

| Field | Purpose | How it drives the visual |
|---|---|---|
| `typeId` (registry-assigned, stable) | the shared id between the sim grid and the visual buffers | indexes `GasParams[]` in the shader; the join key for the whole system |
| `bodyTint` (color) | "which gas" = the dominant saturated color in a desaturated world | multiplied into the accumulated raymarch color; the primary at-a-glance type cue. **Registry hue-allocation discipline**: deconflicts authored tints, reserves the danger hue out of the palette, warns if > ~3–4 saturated families co-locate |
| `emission` | hot/fire-state light vs cold inert | self-illumination in the body shader (fire fixture = high, heavy-cold = zero) |
| `densityToOpacity` (curve) | concentration → "how much" | shapes per-sample alpha; reads GridView.density; clamped by the submerged ceiling when the camera is inside |
| `motionCharacter` / `riseSinkBias` | heavy-settles vs light-rises | a vertical bias on the shader's internal noise (NOT a sim force; a lerp weight, never an if-branch). ⚠ shader-internal motion is decoupled from real density — verify by eye at build-step 2 |
| `frontSharpness` | how crisp the edge reads | sharpens the FULL-RES front composite (against depth, not the upsampled body) using GridView.frontStrength |
| `temperature` / `state` (enum) | secondary appearance modifier | tints scatter/absorption in the body |
| `hazardReactive` (flag) + event→warning map (rows of stable ids) | marks reactive gases; maps sim EventId → WarningKindSO id | does NOT light the body idly; on a sim event the TelegraphDirector fires the mapped warning. Event spark = signal, not idle noise |
| `accentVfxParams` | per-type flavor for the ONE optional shared accent graph | exposed VFX properties when the accent flag is ON; carries NO readability-critical signal (so it can be absent on no-compute hardware) |
| `behaviorModule` (nullable) | the reserved special-gas hook | null → pure read-only look (every v1 gas); its shape is the post-v1 spike's job |

**The data/code line (R15, held ruthlessly):** anything expressible as a WEIGHTED BLEND of the fixed body operators
(rise/settle, emissive, scatter, front, opacity) is DATA = a GasTypeDefinition asset (a "specific gas"); anything
needing a NEW operator or NEW motion is CODE behind the special-gas seam (a new "meta-archetype" / behavior module).
The shared raymarch archetype IS the "meta-gas"; each ScriptableObject IS a specific gas as pure config. Hold this
line or "new type = data" erodes into "new type = another branch". (The 3-tier meta-taxonomy stays a one-line
guardrail, not a formal model — it changes zero v1 code.)

---

## 3. THE OWNER'S SHADER QUESTION — answered

**ONE shared "uber" gas body shader, configured entirely by DATA** (per-type params delivered through a
`typeId`-indexed StructuredBuffer). **NOT a shader per type. NOT MaterialPropertyBlock.** A second shader / VFX graph
is reached ONLY at the explicit special-gas seam (a gas needing a structurally different render topology, e.g.
ghostly-hand tendrils, or a behavior module).

Why:
- The body is a fullscreen raymarch BLIT, so N types = **zero** new shader variants and the per-sample cost is the
  same whether there is 1 type or 30 (a single `params[typeId]` lookup, no branches).
- A shader-per-type would multiply variants, break batching for the optional mesh/accent path, and force a code
  edit per type — the opposite of "new type = data".
- INVARIANT: the body shader is **branch-free per sample** — every type param is a multiply/lerp weight, never
  `if(typeId==X)`. (Avoids GPU divergence AND keeps the solo-dev maintenance line clear.)
- (Do NOT use MaterialPropertyBlock for per-type params — it breaks the SRP Batcher / instancing on exactly the
  min-spec integrated GPUs we target. Route per-type params through the StructuredBuffer that already crosses the seam.)

**How a new ordinary gas is added (all DATA):** (1) Create → Gas → GasTypeDefinition, name it. (2) Set the Inspector
fields (tint, emission, motion, front, temperature, hazard flag, accent params; for a reactive type add one
event→warning row). (3) Leave `behaviorModule` null. (4) **Add the asset to the serialized `GasVisualRegistry` list**
(this is the honest SECOND step — an editor validation fires if an authored asset is NOT registered, so the
silent-no-show-in-a-built-player bug is caught, not shipped). (5) Press Play — the existing uber shader renders it by
index. Zero shader edits, zero new material, zero recompile.

---

## 4. THE TWO CHANNELS — body vs warning

- **BODY** (steady, always-on, Layer 2): renders type (hue), concentration (opacity), and the front (sharpness) for
  ALL types in one type-agnostic pass. Overlapping types composite by **dominant-gas-per-cell** only for v1 (the
  most-hazardous-or-densest type owns the cell color; the tie-break is a pure function of replicated sim state +
  hysteresis so it can't desync or flicker). Known v1 limit (accepted): dominant-per-cell loses "which gas is in
  front" when two bodies physically interpenetrate along the ray; fallback if eye-test fails = depth-weighted
  dominant, NOT true N-way mixing (the min-spec killer, rejected). Cap on-screen hues ~3–4 via the registry.
- **WARNING** (event-driven, OFF by default, Layer 3): turns ON only on a replicated sim event (hysteresis: arm on
  crossing UP through a high threshold, disarm below a lower one). DEFAULT primitive = floor decals (no compute).
  **Pass-order (a real design point, not just "measure it"):** floor decals render in the opaque/decal queue and the
  fog blit runs AFTER and reads depth, so decals stay visible THROUGH the gas body they warn about. Telegraph grammar
  = a learnable three-phase lead-in → fire → recovery in a RESERVED danger hue (excluded from the gas palette), so
  "about-to-blow" reads the same across kinds. Pooled with a severity-priority cap.
- **event → visual map (data-driven):** a `WarningRegistry` of `WarningKindSO` assets (id, decal material+size+anim,
  optional VFX, overlay, severity, leadTime, ttl, audio). The director looks up the SO by a STABLE id and drives the
  pooled primitives generically — a new warning STYLE re-using an existing primitive = one SO asset = data. A brand-new
  telegraph PRIMITIVE (new shape/motion) is code, same status as the special-gas seam.
- **Acknowledged coupling (not 100% decoupled):** the body shader carries a per-cell `warningFlag` ambient pulse that
  can DISAGREE with the Layer-3 telegraph (different thresholds). The **Layer-3 telegraph is authoritative** for the
  player's danger read; the body pulse is cosmetic ambience — documented so the player learns one danger language.

---

## 5. THE SPECIAL-GAS SEAM — reserved cheaply, look-only v1

- **v1 builds ONLY:** the nullable `behaviorModule` field + one null-guarded call-site + a TODO naming the post-v1
  spike. behaviorModule is null for all three test fixtures. NO concrete behavior, NO formal interface, NO read-model
  type, NO per-type bespoke shader.
- **Why not a full interface now:** the project's own lesson ("prove on one card before encoding"; an unexercised
  interface usually has the wrong shape) argues AGAINST freezing a 3-method interface v1 never exercises. The first
  concrete special behavior (the creeping floor-fog / ghostly-hands one-gas spike) is POST-v1 and is what DESIGNS the
  interface — and may reveal the seam must be WIDENED if a creep needs to read AHEAD of the coarse sim front (flagged
  now so it isn't a surprise).
- **Network/determinism guarantee (cheap + structural):** the entire visual stack is on the cosmetic side of the
  read-only seam. The engine is host-authoritative, so there is no cross-client determinism to defend — clients are
  pure replicas. Data crosses the engine→visual line exactly once, one-way, by buffer upload; nothing is serialized,
  checksummed, or read back by the sim. A future behavior module **cannot desync co-op because it is never handed a
  writable sim handle** (enforced by NOT handing out the handle, not by discipline). Per-client cosmetic divergence is
  harmless; the danger model reads ONLY the engine grid.

---

## 6. PERFORMANCE — many types cheap, and what must be MEASURED

**Many types approach:** a SINGLE shared raymarch pass over ONE packed GridView field, styled by a per-sample
`params[typeId]` lookup. Body cost is O(screen-pixels × steps), **independent of how many types exist**. Overlap =
dominant-gas-per-cell (constant per-step ALU regardless of global type count). HONEST QUALIFIER: the owner's real
scenario is many types *simultaneously on screen*, whose cost is dominated by OVERLAP resolution + HUE count (~3–4)
+ (if the optional flag is on) live particle count — NOT raw type count. The body's type-count-independence is real
but answers a slightly different question; the on-screen-many cost is unfounded until profiled.

**Min-spec levers:** body MASS at half/quarter res + bilateral upsample, FRONT reconstructed at full res; tune
raymarch step count (~25–40) + RT scale as a quality tier set by the step-0 measurement; the DEFAULT path (body +
decals) needs NO compute — the optional VFX accent/burst layer is ONE feature flag gated on
`SystemInfo.supportsComputeShaders` (force Vulkan/DX11, never GLES; VFX fails silently without compute); bound the
uploaded GridView to the camera region via a clipmap (write only the new slab); single-buffer for fake steps,
add double-buffer + in-shader lerp only at the real-engine swap and only if tick-stepping is visible.

**Perf unknowns — DEFERRED to a later optimization pass (owner steer 2026-06-26; NOT a front gate — owner has no min-spec HW). Carried so they aren't lost; a free rough reading on the home machine is a non-gating smell test:**
1. Does the min-spec integrated GPU support compute shaders at all? (gates ONLY the optional VFX layer; default
   body+decals does not need it; fails silently → check on real hardware in step 0).
2. Real grid→GPU upload time + steady-state VRAM at the LARGEST active region on an iGPU sharing system RAM,
   including clipmap re-upload churn (THE primary unvalidated perf variable; measure before freezing grid resolution).
3. Actual fragment cost of the half/quarter-res raymarch at 25–40 steps at target screen res after the rest of the
   game's draw (30–40 steps fullscreen on an iGPU at 1080p may already be over budget → sets RT scale + step count).
4. Does the full-res-front + half-res-body recombination read crisp at the front, or show seam artifacts?
5. Warning granularity: per-region (in GridView) vs per-type-global (in GasParams) — a schema fork resolved before
   freezing the buffer layout (step 1).
6. How many simultaneous decals + (optional) VFX bursts the iGPU sustains alongside the body pass (sets the caps).

---

## 7. THE DE-RISKED BUILD SEQUENCE — each step owner-visible on FAKE data

Runs as executor legs in **GasCoopGame_dev** (Unity). FAKE data throughout until the last step, so it never waits on
the engine.

**PERF POLICY (owner steer 2026-06-26, d-visual-buildstep0-001 = adjust):** min-spec perf is NOT a front gate and is
NOT measured first. The owner has no min-spec machine, and a perf number does not change the architecture (it only
sets tuning knobs or, worst case, forces a cheaper BODY-rendering technique later — which the read-only seam makes a
cheap swap). FIRST GOAL = a WORKING visual on the owner's HOME machine (steps 1→4 below); real optimization +
min-spec derivation is a LATER pass once the visual/game exists and the target audience HW is known. Cheap safeguards
kept from day one: (a) two body knobs — render-resolution scale + raymarch step count — so we never hard-code the
most expensive version; (b) a free, NON-GATING rough frame-cost reading on the home machine along the way (a smell
test, not a min-spec verdict); (c) the body stays behind the seam so it is swappable later. NAMED DEFERRED RISK: if
the raymarch body is fundamentally too heavy for the eventual min-spec, the body technique may have to be swapped
later — bounded, because the decoupling preserves the data model / authoring / warning / the 3 gases across a
body-renderer swap.

| Step | Goal | De-risks | Owner sees | Fake data |
|---|---|---|---|---|
| **0. PERF — DEFERRED (a policy, not a leg; owner steer)** | NO min-spec spike first. Build the working version on home (steps 1→4); keep the 2 body knobs (resolution scale + step count) + take a free non-gating rough frame-cost reading on the home machine; real optimization + min-spec derivation is a LATER pass once the visual exists | avoids chasing an un-measurable target now (owner has no min-spec HW) without painting into a corner; the decoupling makes a later body swap cheap | nothing new to "see" — the first thing he SEES is step 1 | n/a |
| **1. The seam + buffer contract** | define GasParams (aligned, blittable) + GridView (clipmap 3D texture); build `IGasViewSource` + `FakeGasViewSource`; wire the body to index GasParams[dominantTypeId]; resolve the warning-granularity fork; add the stride-conformance test | locks the parameter contract (the structure) + the stride discipline as a CHECKED gate; proves the engine-swap seam on fake data | a fake gas blob whose color/opacity is driven by a real buffer lookup (change a number → the body changes) + a green stride test | yes |
| **2. Data-driven type authoring** | GasTypeDefinition SO + the serialized GasVisualRegistry (stable typeIds, hue deconflict) + the forgot-to-register editor warning; author the 3 parameter-space extremes as DATA | proves "new type = author one asset + register it" across three different looks with ZERO shader edits; validates the branch-free invariant + the register guard | three visibly distinct gases from three Inspector assets, no code touched; a deliberate forget-to-register test producing a visible warning | yes |
| **3. Many-types overlap + EYE-judged readability bar** | dominant-gas-per-cell compositing (hysteresis tie-break) + the OPTIONAL VFX accent layer; stress with many overlapping fakes incl. camera-inside-the-cloud; a screenshot harness with the 3 extremes co-located, judged by the OWNER'S EYE as the readability pass/fail | validates the one genuinely-new design piece (the dominance rule) + the interpenetration / camera-inside cases against an explicit eye bar; confirms many types stay cheap and body-only is readable | several overlapping gases readable at a glance (~3–4 hues), front crisp, danger legible even when submerged + an explicit owner thumbs-up/down | yes |
| **4. The WARNING channel** | TelegraphDirector + WarningRegistry/WarningKindSO + the default decal primitive (proven to render THROUGH the fog via the pass order) + the optional pooled-VFX burst + local fullscreen overlay; fire from fake/replicated events; acceptance: add a SECOND warning kind as a config asset | proves the two channels are separate, the event-spark-not-idle-spark discipline, the decal-through-fog pass order, "new warning kind = data" | a reactive gas that stays calm until an event fires, then telegraphs (decal ramp → burst → fade) VISIBLE through the body; a second warning kind added with no code | yes |
| **5. Reserve the special-gas hook (bare, look-only)** | add ONLY the nullable behaviorModule field + the null-guarded call-site + a TODO; null for all fixtures; NO interface, NO behavior | establishes the extension point at the cheapest cost without freezing an unexercised interface | the system runs identically with the hook present-but-empty + a note that the floor-creep/ghostly-hands gas is the post-v1 spike that designs the interface | yes |
| **6. Real-engine swap (FAKE → real)** | `RealGasViewSource` bridges the Layer-0 snapshot into the SAME buffers + event stream with ZERO change to Layers 2–3; assert byte-identical struct/stride (conformance gate re-run on real data); add double-buffer+lerp only if tick-stepping is now visible | proves the decoupling seam end-to-end as a CHECKED equality; re-measures upload/VRAM on real data; decides double-buffer on observed evidence | the real authoritative gas (not fake blobs) rendered by the UNCHANGED visual stack, in networked co-op, no desync, green fake-vs-real equality | no |

---

## 8. HONEST UNKNOWNS + OVER-ENGINEERING GUARDRAILS

Beyond the perf unknowns in §6: readability of dominant-gas-per-cell under interpenetration + when submerged (eye-judged,
step 3; fallback = depth-weighted dominant, not N-way); hue-allocation under load (can ~3–4 hues + a reserved danger
hue deconflict enough co-located types, or does the palette saturate?); whether the reserved hook is expressive enough
for the flagship floor-creep gas or must be widened to read ahead of the coarse front (post-v1 spike); whether
double-buffer+lerp across the 10–20 Hz tick reads as flow or stepping (step 6).

Guardrails (keep it solo-dev-sized — DO NOT build):
- Exactly ONE body shader; the optional VFX accent + warning-VFX burst are a SINGLE feature flag. Resist per-type variant sprawl.
- Exactly ONE GasTypeDefinition class + ONE registry + ONE TelegraphDirector + ONE WarningKindSO class + TWO GPU buffers. No third buffer, no node-graph mini-engine, no ECS, no Addressables at this asset count.
- DEFER secondaryTypeId+blend (single-dominant-per-cell only); DEFER double-buffering (until the real-engine swap, if stepping is visible).
- RESERVE the special-gas seam with ONLY a nullable hook + a TODO (no formal interface / read-model / safe-motion taxonomy in v1).
- Do NOT pre-build a shader-stipple accent fallback; ship body+decals (no-compute default), treat ALL VFX accents as one optional flag; build a fallback only if a real min-spec machine proves compute absent AND the owner wants accents there.
- Do NOT build true N-way multi-field gas mixing (dominant-per-cell only; depth-ordering loss accepted).
- Crude visuals are FINE for v1; invest only in the shared body + front readability; do not polish individual gas looks before the SYSTEM is proven on fake data.
- Honest: "new type = data" is author + register (two steps), guarded by the editor validation — not a silent one-step.
- No visual (accent, warning, future behavior) may originate a gameplay value or precede the authoritative front; the Layer-3 telegraph (not the body pulse) is authoritative for danger.

---

## 9. Method + provenance

- Workflow `wf_579651ba-7f9`: 5 finder dimensions (data-driven authoring; many-types-perf; two-channels; special-gas
  seam; reference architectures), each adversarially verified by an independent skeptic; a draft synthesis; a solo-dev
  over-engineering critic; a final incorporating the critique. Verified 5/5 dimensions.
- Builds on `work/gas-visual-research-2026-06-21.md` (deep-research `wf_e5924329`): the layered read-only architecture,
  the two render paths (raymarch body + VFX accents), the INSIDE "Low Complexity High Fidelity" distinctiveness lever,
  and the half/quarter-res + bilateral-upsample min-spec lever — all carried forward, not relitigated.
- Confidence: the read-only layered structure + one-uber-shader-by-data + two-channel + reserved-hook are
  high-confidence and solo-dev-sized. The load-bearing UNVERIFIED item is min-spec PERF (the raymarch frame budget +
  the upload cost + whether the iGPU supports the optional compute path) — which the owner has chosen to DEFER
  (d-visual-buildstep0-001 = adjust): he has no min-spec machine, and a perf number does not change the architecture
  (only tuning knobs or, worst case, a later body-renderer swap the read-only seam makes cheap). So we build the
  working version on home FIRST and treat perf as a later optimization pass, keeping two cheap body knobs + a free
  non-gating home frame-cost reading from day one as smell tests.

END_OF_FILE: live/indie-game-development/work/gas-visual-architecture-2026-06-26.md
