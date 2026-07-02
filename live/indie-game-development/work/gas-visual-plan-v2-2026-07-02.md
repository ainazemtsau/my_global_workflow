# Gas-visual PLAN v2 — the JEWEL, staged (owner-approved 2026-07-02)

Supersedes work/gas-visual-wave-plan-2026-06-29.md as the official g-7e15 track plan. Produced from a
read-only inventory of the shipped render layer (GasCoopGame main @b5675ea) + docs/ADRs, a 5-lens external
research sweep (shipped-game approach forks, per-type readability language, look-dev practice), and a
4-lens adversarial panel (perf/feasibility, owner-visible-value, repo-contracts/OS, solo-scope) that tried to
break the first draft. All panel P1/P2 fixes are folded below. Owner confirmed 2026-07-02 (single-message
batch «подтверждаю»): plan accepted; hold stays until Sc-kernel GREEN (2a); d-finer-grid-fork-001 = option 2
(3-2); W1b window = the Sc-kernel→Sc-reactions gap (4a).

## Ground truth this plan is built on (verified first-hand, not assumed)

- Render = ONE fullscreen fragment-pass raymarch over a continuous Texture3D (R=density, G=dominantTypeId,
  B=front, A=warning), behind the read-only `IGasViewSource` seam; frozen 96-byte `GpuGasParams` per type.
  This is architecturally the shipped CS2 responsive-smoke pattern (voxel sim → raymarched view) and is the
  correct base — no alternative (6-way flipbook, VFX Graph, froxel fog, Zibra/asset-store fog) renders ONE
  externally-authored density field without either requiring compute or owning its own fake sim.
- Most look levers are already implemented: baked tiling Perlin-Worley noise, quintic/smootherstep de-block
  warp, detail erosion, 0–8 self-shadow taps, HG forward-scatter "light-through" thin-lift (the W1a jelly
  fix), toon bands, curl/billow motion, IGN dither, density-shell rim + fresnel, warning-edge recolour in
  shader.
- ABSENT: depth composite (gas draws OVER walls today — every demo scene is staged open-front to hide it),
  real half-res (the `resolutionScale` knob is a declared no-op; measured GTX1060 cost elsewhere is 7–11 ms
  full-res vs ~1 ms half-res — half-res is not optional at ship quality), per-step Beer transmittance in the
  main march (linearized alpha accumulation instead), coarse empty-space skip.
- The REAL sim feed is single-species (`RealGasViewSource` hardcodes `G=0`, `TypeCount=1`) even though the
  engine already has a per-cell dominant-type STAMP since Sc-rep (merged @5442be0) — wiring a tiny read-API
  is the only blocker to multi-type render (named W1b below).
- Per-type DATA today = colour + opacity-curve + front-sharpness + warning-gate only. ALL shape/motion/
  lighting character knobs are GLOBAL render-feature uniforms — two real gases can currently differ only by
  colour, which is why "types must read as different characters" is not yet buildable.
- Only 5 of the frozen struct's reserved scalars are genuinely unconsumed (`RiseSinkBias`, `Temperature`,
  `State`, `HazardReactive`, `BehaviorModuleId`); the target per-type identity vocabulary needs ~8–10 new
  scalars → a 96→128-byte layout-ADR event is not "looming", it is **inevitable**, and must be decided before
  any per-type hero polish is signed (else the polish gets re-tuned when the layout changes — a manufactured
  regression for an owner already burned twice by "it got worse").
- Odin Inspector is installed and used; `GoodSampleAsset` (reflection-based save/A-B/promote) is the existing
  never-worse mechanism and stays as-is through Stage 1–2 (no tooling rebuild until the per-type schema
  lands, per the panel's over-engineering finding).
- The sim is deterministic integer lockstep; "connect the real sim quickly" is already solved architecturally
  (the `IGasViewSource` seam accepts any per-frame-filled Texture3D; `RealGasViewSource` already reads the
  live simulation) — no new plumbing needed to attach a real scenario to the stand.
- W1a (real gas in a lit room) is DELIVERED with owner reservations (history/2026-07-02-s-visual-011-w1a-owner-sign.md):
  LP2/LP3 confirmed live, LP1 (light-through direction read) candidate-pass only, LP4/LP5 blocked by the
  missing designed demo level — this plan's Stage 1 IS that missing level (the reshaped c-visual-004).

## Honesty line carried forward (do not silently drop)

Sub-cell **silhouette** (thin tendrils, non-cubic form finer than the ~0.5–1 m sim cell) is NOT purchasable
render-side — render buys sub-cell **richness** (noise, erosion, warp), never shape finer than the grid.
d-finer-grid-fork-001 is the named engine-side lever for silhouette; it is now ANSWERED (see Decisions below)
and must be settled in owner's mind before Stage 3 raises expectations, so a render ceiling reads as honesty,
not failure.

## The stages

Each stage = one owner-present PLAN → build → owner-eye A/B gate in motion (never a self-marked green suite)
→ RESULT home. Never-worse discipline (GoodSampleAsset baseline, A/B every change, worse = discarded) holds
throughout. Verdicts are given from ONE designated primary bookmark/preset/replay per gate; everything else
is exploratory (owner may look, never must) — this is the panel's fix for verdict-matrix fatigue.

### Stage 1 — Стенд + отсечка (CALL: work/c-visual-004-call.md)
Minimal stand (panel-trimmed: no grey/chrome spheres — a raymarched emissive volume has no surface BRDF to
calibrate; no 3-preset light rig — one lit/dark toggle is enough at this stage): one designed vertical room
in canon greybox style (floor for pooling, one motivated lamp + `GasLightBinder`, a 1 m cube + player-height
mannequin for scale), 2 fixed camera bookmarks, **one open-space no-walls bookmark** (owner correction: gas
spawns anywhere, directional jets in the open are a felt requirement — not room-only), fixed-seed restart
button on the live `VoxelSandboxDirector` (repeatable motion without a golden-replay library — the sim is
already deterministic, a scenario config is all that's needed), and the **depth composite** shader fix (march
stops at scene depth — unblocks enclosed staging and is itself a pinned visible win).
Owner sees, as two pinned before/after pairs: (1) gas no longer shines through walls in an enclosed room; (2)
the current gas in the new designed room vs the old boxy 6×4×6 box. Lineup mode and two-gas-meet replay are
explicitly NOT in Stage 1 (they would render as one indistinguishable colour — see Stage 3).

### Stage 2 — Паспорт типа + шипучий режим (schema + read-API + real half-res; short, mostly non-visual)
(a) Schema session (owner-signed): the per-type visual profile as 8 identity channels — hue, value,
saturation, edge softness, motion frequency, buoyancy silhouette (worded as a *read-through of the existing
per-type SIM weight* — never a new render-side vertical bias; `RiseSinkBias` stays reserved per ADR-0020),
interior structure, glow pattern — plus a danger scalar. This is where the 96→128-byte layout-ADR is decided
(not squeezed into the 5 leftover scalars). (b) W1b: consume the merged per-cell dominant-STAMP read-API (an
ENGINE mini-CALL, run in the `GasCoopGame_dev` worktree — see next_slices/Decisions; never touches `dev_2`).
(c) Pull real half-res + depth-aware bilateral upsample forward here (not Stage 6) so every later owner-eye
verdict is judged on the ship-quality render path, never re-litigated when perf lands.
Owner sees: a real two-colour multi-type preview (two real gases, distinct colours, meeting) — explicitly
labelled PREVIEW ("colours only; character arrives at Stage 4"); same visual quality, confirmed still-good on
the real half-res path.

### Stage 3 — Одна жемчужина (hero-polish one gas, one lever at a time)
Cheap pre-staged A/B levers: two-tone directional ambient, HZD beer-powder dark edges, per-step analytic
transmittance in the main march, HG g tuning, LUT-ramp promotion if needed — plus the two named standing
debts: toon-band count (1/2/3/4, owner-eye pick) and the opacity-ceiling number (closes
`owner-ack:esc-c-visual-003-opacity-ceiling-deferred-2026-06-30`, also the LP5 sign-off input). Then, as its
own shaped sub-leg with a real appetite and a named checkpoint date: the **natural jet fix** (curl-noise
advection + two-phase flowmap blending to kill the "plasticine capsule" read). Explicit LP1 re-test row: move/
swap the lamp → the through-light read must visibly follow (upgrades the W1a candidate-pass or the
reservation stays recorded). Explicit honest ceiling-exit written into the CALL: if the remaining gap is
sub-cell silhouette, render is DONE and the delta routes to d-finer-grid-fork-001 — a stop there is honesty,
not failure.
Owner sees: ONE gas that hits "ближе к жемчужине" in motion — natural flow, light visibly passing through,
LP1–LP5 individually re-confirmed (not an aggregate hand-wave).

### Stage 4 — Три характера + шкала опасности (CALL after Stage 3 signs)
Author 3 archetypes from the canon gas families (asphyxiant-dense = heavy, dark, pooling; flammable = warm,
nervous boil; cryogenic = pale, slow settling), each satisfying a **3-channel minimum-separation rule** (never
hue-alone — two types must differ in value AND at least one of motion/silhouette/structure; ~8% colourblind
players confuse hue-only pairs). Danger 0→1 as a per-type multiplier ladder: value/exposure up, hue shifted
toward heat, emission pulse rate up (hard-clamped **under 3 Hz** — WCAG 2.3.1 seizure guard), motion
aggression up; benign = the calm opposite (low saturation, soft edges, slow drift, steady dim glow). Add a
named **frontier-blend** lever for the point-sampled `dominantTypeId` seam (density-weighted blend or dithered
boundary) so two gases meeting does not read as a blocky Minecraft edge at the plan's biggest promised payoff.
Acceptance = a **blind** lineup test: pods shuffled to random positions each run, owner names them cold at the
start of the session (not mid-tuning-familiarity); repeated at 25%-saturation/value-only; repeated at danger
0.0/0.5/1.0 (danger must not compress the hue axis the lineup was signed on); optionally the same clip sent
to the two delegable marketing helpers as a naive-viewer cross-check.
Owner sees: three gases side by side, unmistakably different, correctly named cold — and correctly named
again at maximum danger.

### Stage 5 — Затопленная комната (perf pass, framed as a spectacle not a number)
Name the min-spec device; re-measure current render cost (the only number on record, 0.947 ms, predates every
lever added since and was measured pre-W1a); coarse-mip empty-space skip; quality tiers; and the stage's
owner-facing FACE — a room flooded with all three characters live, on the named min-spec class, ideally
captured as a clip. The half-res/upsample work itself already shipped in Stage 2; this stage is measurement +
the flood spectacle, not "same look, different number" (the panel's fix for an otherwise-invisible stage).
Feeds the marketing capture pipeline (g-2f8c/g-5b07) from here on.

### Stage 6 — Газ в мире (post-Steam-page; ONE owner-picked item, capped)
Recommended default: teammate readability (fresnel rim through gas on a character + depth-fade so the volume
never hard-clips a body) — the Helldivers-2 "opaque gas blinds your own team" failure mode is a known trap to
avoid, and it improves every future screenshot with a character in frame. Surface traces (residue/tide/frost/
soot) are named but NOT auto-included — a future costed decision, and split by source-of-truth honesty:
density-history marks (tide/frost from presence) may read view data and are cosmetic-only; reaction-class
marks (soot/burn) must wait for and consume the Sc-reactions outcome-registry events, never invented from view
data (else render history could contradict a sim-recorded outcome). Sparse VFX accents and the Feel/
MMFeedbacks juice layer (camera/post pulses on gas entry) ride here too, as optional, never load-bearing.

## Explicitly NOT in this plan (named, not silently dropped)

Flagship "странные" anomalous gases with bespoke visuals — beyond the 3 canon archetypes, a later stage once
the archetype machinery is proven. Per-cell hazard telegraph (the warning A-channel) — stays dormant; it needs
Sc-reactions' outcome-registry events, not a render-side fake. A vision-agent blind pass over captured clips
vs sim state, and the flagship 10–30s menace-clip test — both are g-7e15 TREE done_when items (#2, #3); they
run as a named node-acceptance pass after Stage 4/5, not inside any single stage. Audio-scaled danger
(Geiger-counter convention) — a real, cheap accessibility win, parked as a future capture, not scoped here.

## Mapping vs the superseded 06-29 wave plan (nothing silently dropped)

- Wave 1 foundation → delivered as W1a; its remainder (designed demo level) = Stage 1 here.
- Wave 2 alive motion (curl/billow, natural jet) → Stage 3.
- Wave 3 full per-type looks + reactions → Stages 2 (schema) + 4 (archetypes + danger).
- Wave 4 polish + perf (sparse VFX accents, weak-HW perf pass) → Stage 5 (perf) + Stage 6 (accents).
- Parallel-engine "finer sim grid" line → d-finer-grid-fork-001 (answered; see Decisions).
- Stage-plan open decisions carried forward: toon-band count → Stage 3; opacity ceiling → Stage 3; ramp
  authoring → resolved as the Stage-2 ScriptableObject schema; reserved-field assignment → Stage 2 layout-ADR.

## Calendar honesty

Track stays ON HOLD until Sc-kernel GREEN (owner default, 2026-07-02). Realistic restart ≈ mid-July. Depth
composite (Stage 1's only 07-24-critical item) is small and engine-free — it CAN run in `dev_2` during the
hold if the owner explicitly reverses «сначала разобраться с симуляцией»; absent that reversal, it waits with
the rest of Stage 1. Stages 1–4 are the realistic pre-08-31-Steam-page scope; Stages 5–6 are named post-page
unless the page capture itself needs the Stage-5 flood spectacle sooner. Owner-session budget stays engine-
weighted (~2:1) until Sc-reactions is GREEN; visual CALLs are sized to fit inside that, not around it.

## Decisions closed in this session (2026-07-02)

- **d-finer-grid-fork-001** → ANSWERED, option 2: schedule a costed READ-ONLY view-refinement engine item
  (off-checksum, detail-bubble seam, no Fact-2/ADR-0002 reopen) after Sc-damage — the keep-the-jewel path.
  Decided now, ahead of Stage 3, so the jewel bar has an honest, pre-agreed ceiling-exit.
- **d-w1b-window-001** (new) → ANSWERED: the W1b engine read-API fires as its own tiny mini-CALL in the
  `GasCoopGame_dev` worktree, in the gap after Sc-kernel merges to main and BEFORE c-exec-021 (Sc-reactions)
  fires. c-exec-021 rebases over it via its own §Re-sync sweep (already a named step). It never touches
  `dev_2` and never becomes part of a visual-track CALL (the render-only boundary stays intact — a Core/Field
  edit cannot ride inside a render-only leg).

END_OF_FILE: live/indie-game-development/work/gas-visual-plan-v2-2026-07-02.md
