Both anchors confirmed: `:74` (trigger reads coarse, "approach detonates the cloud = gameplay-pop + desync"), `:79` (Ведро-3 = the persistent split changing exit-door, the deep-interaction case), `:134` (hangar = single unmeasured number, no cap, ADR-0010 lock on coarsening). The synthesis is grounded. Here is the decision document.

---

# DECISION: Gas Architecture — Current Grid vs Owner's Cloud Model

## 1. Verdict headline

**HYBRID — keep the built+hardened integer grid as the authoritative spine; fold in the cloud model's ONE real win (a fixed-radius sphere as the near-detail cap) as a non-authoritative window. The single decisive reason: every kill attempt that touched authority landed — the cloud far-tier cannot own the checksum without rebuilding the exact integer grid it claims to replace (`:74`, `:93`, `:46`), while its only genuine breakthrough (capping the unmeasured hangar number `:134`) is adoptable WITHOUT the Lagrangian paradigm.**

The owner is right about the problem (the hangar gap is real and unsolved) and right about the lever (cap the fine zone by a sphere). He is wrong that this requires clouds-as-authority. Take the lever; leave the paradigm.

---

## 2. Comparison matrix

| Boundary case / requirement | CURRENT (grid + room-rollup) | CLOUD (Lagrangian far + sphere near) | Winner |
|---|---|---|---|
| 8 spread (1/room) | ~20k fine cells, sparsity pays | ~7.2k near cells + far cloud sim | CLOUD (marginal) |
| 8 clustered | Region-shared, ~2.5k, clustering COLLAPSES cost (`:33`) | Overlapping spheres: unspecified merge → reinvents shared region or desyncs | **CURRENT** |
| 8 fast-scatter | Correct but spikes (8 simultaneous `expand`) | Flat ~7.2k, no wake spike — smoother | CLOUD |
| Running THROUGH gas | Dose = coarse event, approach can't detonate (`:74`) | Coord-intersection trigger = approach detonates cloud + per-peer desync | **CURRENT** |
| Caps TOTAL near cells? | **NO** — geometry-bound, unmeasured (`:134`) | **YES** — O(players × sphere), hard cap | **CLOUD** |
| Overlapping spheres | No spheres; overlap = free (region-shared) | No owner rule for shared cell → double-count / desync | **CURRENT** |
| Worst spread (2 halls + 6 rooms) | ~175k–512k cells, no in-lock fix (`:134`) | ~7–40k cells, hall size drops out | **CLOUD (decisive)** |
| Partial-fill blob POSITION (far) | Position-less bucket — sum has no coordinate (`:68`) | Clouds keep coordinates natively | **CLOUD** |
| Return-to-room (blob in corner) | Exact only for held rooms (fine-shadow); else regenerated (`:68`) | Position survives by default, no eviction cliff | CLOUD (position) / CURRENT (mass) |
| Cloud SPLIT across rooms (door) | Trivial — `region_id` labels + flux carry (`:67`,`:93`) | Forced integer cloud-split at every door = owner's flagged weak spot, on hot path | **CURRENT (decisive)** |
| Turbulence / split-off wisp | Ведро-1 free (off-checksum) / Ведро-3 paid, already ratified (`:77`,`:79`) | Split/merge on authoritative path = desync surface | **CURRENT** |
| LOOT finite source (far) | Smears to room-average (position-less) | Blob keeps leak in the corner | **CLOUD (narrow)** |
| Two-gas 5%+5%+wind react (near) | Default-A over-reacts on room totals; spatial gating needs Ведро-3 | Coord-overlap spatially-gates for free | **CLOUD (its strongest point)** |
| Same reaction FAR from player | Over-triggers (position-less) OR expensive Ведро-3 | Spatially-gated, BUT global cloud sim NOT sphere-capped | CLOUD (fidelity) / CURRENT (cost honesty) |
| EXPLOSIONS | Refinement-invariant coarse trigger, hardened, documents WHY (`:74`) | Geometry trigger = worst place for non-determinism | **CURRENT (decisive)** |
| Energy / WIND flows | Integer face-bias, mass-conserving, gated (`:62`,`:93`) | Lagrangian advection = the deepest determinism hole + turbulence | **CURRENT** |
| MASS conservation (integer, exact) | Closed-by-construction, motion triggers NO conversion (`:68`,`:93`) | Moving boundary 8×/tick, no flux-register on sphere skin, overlap double-claim | **CURRENT (decisive)** |
| Determinism / cross-CPU checksum | Integer path + zero-float scan + clamp, specified & hardened (`:46`) | Constructible only by re-deriving all of it on a harder topology | **CURRENT** |
| Big-hall worst case (the gap) | OPEN, unmeasured, no cap (`:134`) | Solved by construction (sphere cap) | **CLOUD (the one it's built for)** |
| RENDER far body | Bounded by sim window — uploads 256k-cell buffer | Cheap blob/metaball far render, position-preserved | CLOUD |
| No-pop at near/far boundary | Proven-by-construction at STATIC wall (`:68`) | NEW moving in-view sphere seam, no construction guarantee | **CURRENT (decisive)** |
| Deep level-spanning interaction (the CENTER `:83`) | Coarse EVENT, zero traffic, BUILT (`:34`,`:83`) | Dropped where no player present; or rebuild grid | **CURRENT (decisive)** |
| Migration cost | Incremental — finish the build; reshape DOUBLES DOWN on grid (reshape `:50,:79`) | Lagrangian = near-restart of the most-hardened layer | **CURRENT (decisive)** |

**Tally:** CLOUD wins decisively on exactly TWO axes — the hangar cap (`:134`) and far-tier position. CURRENT wins decisively on the four that "we cannot mess this up" cares about most: mass conservation, determinism, deep level-spanning interaction, and no-pop/migration.

---

## 3. Where the CLOUD idea genuinely wins — and how to fold it in WITHOUT Lagrangian

Two real insights. Both are adoptable into the grid as a hybrid; neither requires clouds-as-authority.

**WIN 1 — The fixed-radius sphere caps the architecture's single unmeasured number.**
This is the owner's genuinely important contribution. The canon admits the hangar is "единственное неизмеренное число всей архитектуры," has NO fixed cap, and its only lock-safe fallbacks are all-peers-all-bubbles or smaller levels (`:134`). A player in a hall fines a ~256k-cell window; a 4m-radius sphere @50cm is **~2,145 cells** (8m → ~17k). That is a **15×–120× cut** on the worst number in the system, and it caps near-cost at **O(players × sphere) ≈ 8 × 2k ≈ 16k** regardless of hall size or the 2-hall spread that pushes CURRENT to ~512k.

**Minimal fold-in (the hybrid — survives all three kills):** make the existing non-authoritative detail bubble (`:33`) a **fixed-radius sphere instead of a room-sized window**. The bubble is *already* off-checksum, read-only, discarded-on-leave, and never writes back (`:33`,`:70`). Capping its RADIUS changes nothing about authority, mass, or determinism — it only bounds how many cells the local view refines. The mass-boundary kill confirmed this is the version that survives: *"a fixed-radius sphere is a legitimate cap for the local non-authoritative detail bubble — it does not touch the authoritative coarse field, so it needs no ADR-0010 un-lock."* This is the steelman of the owner's pitch, and it is a near-free change to the built grid.
- *Cost it pays:* in a hall, far-field gas beyond the sphere is shown at coarse resolution (the player loses the 50cm floor-sheet silhouette across a 40m hall). That is the honest trade — but CURRENT *cannot afford to show that anyway* on the weak peer, so the sphere loses fidelity CURRENT couldn't pay for in the first place.

**WIN 2 — Coordinate-carrying far gas preserves sub-room position (the corner-pool / finite-leak case).**
CURRENT's far rollup is position-less by construction: `collapse(region)` is a scalar SUM (`:68`), so a 5% corner-pool and a 5% even haze are byte-identical when far, and a finite loot-leak smears to room-average. The cloud's coordinates fix this for the two narrow cases that matter (return-to-room blob; finite leak staying in the corner).

**Minimal fold-in (OPTIONAL, do NOT pursue first):** give the far rollup an OPTIONAL small set of integer "centroid hint" coordinates per gas-type per room — a position annotation on the coarse mass, NOT a replicated authoritative entity. Mass stays the scalar sum (authority unchanged); the hint only biases `expand()`'s largest-remainder seeding so a returned/observed room re-grows the blob near where it actually was. This captures most of WIN 2 without entities, without split/merge, without putting coordinates in the reaction trigger. The render-maturity cluster reached the same conclusion: *"could be captured incrementally by giving CURRENT's far rollup optional coordinates, without throwing away the hardened grid."* This is a later, gated nice-to-have — not load-bearing.

**WIN 3 (real but already owned) — cheap, legible FAR rendering.** Blob/metaball far-render is cheaper and more legible than uploading a 256k-cell buffer. This lives entirely in the render layer, which is already specified as a read-only voxelizer over the grid (`:67`) with an off-checksum 25cm visual bubble (`:152`). The renderer can draw the far field as impostor blobs fed by the rollup (+ WIN-2 hints) with zero change to the authoritative sim. Free to adopt; pure presentation.

---

## 4. Where the CLOUD idea loses — the hardest problems, with kill verdicts

**A. Deep level-spanning interaction — the CENTER — is silently dropped (KILLED as far-tier).** The canon names this the architecture's CENTER, in BUILD not research (`:83`). If only per-player spheres carry authoritative cells, then gas with no player nearby has no authoritative fine state — and Ведро-3's defining case (the persistent split that decides *which exit door* the cascade takes, `:79`) lives exactly there. CURRENT can promote that room to full detail for ALL peers; the sphere-capped cloud model *structurally cannot*, because its CPU thesis is "no cells where there is no player." Worse, the 5%+5%+wind-far case gives the **physically wrong** answer (two non-overlapping blobs → no reaction; coarse totals → reaction fires `:74`), with the outcome decided by blob-radius — a rendering artifact deciding gameplay. The global cloud sim that would fix this is **not sphere-capped** — it scales with total cloud count across the level, so the owner's headline benefit does not even cover the CENTER workload.

**B. Moving-boundary mass conservation — double-claim race (KILLED, not airtight).** CURRENT's no-mass-loss proof is *per static edge* (flux-register on every edge, `:93`) over a static partition (`region_id` per tick, `:67`). The sphere skin is a moving implicit surface with no edges to attach a carry to. Two overlapping spheres unfolding the same cloud either double-count (7 mass in → 14 out — a legal in-range integer the clamp can't catch, **checksum GREEN, physics garbage**, the exact `:46` failure class) or lose the split remainder (no flux-register to carry it). "Conversion through the grid" doesn't save it — two spheres writing the same grid cells same-tick is precisely the forbidden multi-owner / same-tick cross-layer write the canon flags as the desync origin (`:97`). Survives ONLY by demoting the sphere to a read-only window (= WIN 1), at which point the mass was never in the sphere to double-claim.

**C. Determinism — split/merge topology race (SURVIVES-WITH-COST, high).** An all-integer cloud model *can* be byte-deterministic, but only by re-deriving the grid's machinery on a harder topology: clouds need minted IDs in canonical order, all-pairs interactions processed in a stable sort with largest-remainder mass-splits, and split-predicates that read ONLY checksummed state (never the off-checksum sphere). The cloud model also forfeits the grid's free parallelism dividend ("pure function of previous tick, no atomics," `:134`) — birth/death object dependencies need a serialization point the grid never needed. And it re-opens the reaction-on-shape invariant (`:74`) the grid deliberately closed: the coordinate-intersection trigger IS player-approach-detonates-the-cloud, re-armed.

**D. Migration — the worst possible trade shape.** The grid is BUILD-phase, adversarially hardened (`:83`), and the reshape this very week DOUBLES DOWN on a single 50cm grid (reshape `:50,:56,:79`). The cloud model's render advantages live in the *least-built* layer; its costs (determinism, integer mass, no-pop) land on the *most-hardened* layer. You would throw away your strongest banked work to win in your weakest-built one — and you'd still need an ADR-0010 un-lock (`:12`,`:134`) larger than the coarsening fallback the canon already refused to grant silently.

---

## 5. Kill-attempt results

| Kill attempt | Verdict | One line |
|---|---|---|
| **Determinism** (byte-identical cross-CPU for moving clouds) | **SURVIVES-WITH-COST (high)** | Integer clouds *can* be deterministic, but only by re-deriving canonical-order IDs, largest-remainder splits, and the flux-register on a harder topology — forfeiting the grid's free-parallelism dividend and re-opening the reaction-on-shape bug (`:74`). |
| **Moving-boundary mass conservation** | **KILLED (not airtight)** | Overlapping moving spheres double-claim a cloud → 7 in / 14 out, GREEN checksum + garbage physics (`:46`); no flux-register on the sphere skin (`:93`); survives only by demoting the sphere to a read-only window. |
| **Deep-interaction** (preserve the CENTER `:83`) | **KILLED as far-tier authority** | Clouds-as-authority drop level-spanning interaction where no player is present and give physically-wrong far reactions; cloud-overlap-reaction that is deterministic and fair IS the fine grid wearing a coordinate hat. Sphere survives as near-cap; clouds survive ONLY as off-checksum visual LOD. |

**Net:** of three kills, two LANDED and the third survives only at a cost that refunds the CPU savings. The common thread of every landed kill: the moment clouds touch AUTHORITY (checksum, mass, triggers), they fail or rebuild the grid. The moment they stay OUT of authority (a capped read-only window + visual LOD), they're a clean win.

---

## 6. Recommendation

**Adopt the HYBRID. Keep the current integer grid + room-rollup as the sole authoritative spine, unchanged. Fold in exactly one thing now, and one thing later.**

**DO NOW (load-bearing, near-free, survives all kills):**
- **Cap the non-authoritative detail bubble to a fixed-radius sphere** (`:33` bubble → fixed radius instead of room-sized). This directly closes the canon's single unmeasured gap — the hangar worst case (`:134`) — taking the near worst case from ~256k toward ~2–17k cells/player and the 2-hall spread from ~512k to ~tens-of-k. It touches NO authority: the bubble is already off-checksum, read-only, discarded-on-leave (`:33`,`:70`). **Lock the sphere radius + cell-size with the same ADR discipline Fact-2 has (`:134`)** — otherwise 25cm-inside-sphere or a large radius silently re-opens the blowup (8 × 137k @25cm/8m = ~1.1M). The cap is real ONLY under a lock.

**DO LATER (optional, gated, pure upside, not load-bearing):**
- **Optional integer position-hints on the far rollup** to bias `expand()` seeding, so returned/observed rooms re-grow blobs where they actually were (captures the corner-pool / finite-leak position win without entities, split/merge, or coordinates-in-triggers).
- **Far-field blob/impostor rendering** fed by the rollup + hints — cheaper and more legible than uploading dense buffers; lives entirely in the read-only render layer (`:67`,`:152`).

**DO NOT:**
- Do not make clouds authoritative. Do not put cloud coordinates in the checksum. Do not trigger reactions/explosions off coordinate-intersection (`:74`). Do not replace the room-rollup far-tier with Lagrangian blobs. Each of these either dropped the CENTER (`:83`), broke mass conservation (`:46`,`:93`), or re-armed the approach-detonates-the-cloud desync (`:74`) — and all of them throw away the BUILD-phase-hardened grid (`:83`) the reshape is currently doubling down on (reshape `:50,:79`).

**What still needs a decision or a focused prototype:**
1. **(Decision) Sphere radius + inside-cell-size, and lock them via a short ADR** — this is the one real new parameter; it must be locked like Fact-2 or the cap is illusory. Recommend starting at 4m @50cm (~2k cells).
2. **(Prototype, FIRST — it's the canon's own open item) Measure the hangar number with the sphere cap in place** (`:134` says measure it first, before any net/sleep/GPU code, on ALL cores). This single measurement validates the entire WIN-1 fold-in and is already the architecture's #1 unmeasured number — the sphere just turns "measure an unbounded window" into "confirm the capped window fits."
3. **(Deferred) The far-tier position-hint and blob-render folds** can wait until a mechanic actually needs far-room sub-position; do not gate the core on them.

**Position, no hedge:** the owner found a real hole and a real lever. The lever is "cap the fine zone by a fixed sphere" — adopt it, as a window, today. The paradigm he wrapped it in (clouds own the world) fails the three things this game cannot mess up. Keep the grid; cap the bubble; lock the radius; measure the hall.

---

Reference files: `C:\my_global_workflow_worktrees\indie-game-development\live\indie-game-development\knowledge\g9c41-gas-engine-SPEC.md` (canon — authority/trigger `:32-34,:74`; ведро/Variant `:76-81`; mass seam `:66-68,:93-94`; determinism/clamp `:46`; checksum-by-meaning `:95,:97`; hangar gap + ADR-0010 lock `:132-134`; CENTER `:83`; visual bubble `:152`) and `C:\my_global_workflow_worktrees\indie-game-development\live\indie-game-development\work\gas-engine-layered-reshape-2026-06-26.md` (orthogonal reshape; keeps gas as one 50cm grid — `:50,:56,:79,:83`).