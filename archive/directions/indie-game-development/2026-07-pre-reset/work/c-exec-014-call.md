# c-exec-014 — S0 FOUNDATION SLICE (LAYERED) — executor CALL

```
id:          c-exec-014
direction:   indie-game-development / g-9c41
play:        executor (engineering, GasCoopGame) — S0 foundation slice, LAYERED
supersedes:  c-exec-013 (the gas-centric "one 50cm grid" S0)
status:      build-ready (authored 2026-06-26 from R1-layered-reshape, owner «да»)
repo:        GasCoopGame — C:\projects\Unity\GasCoopGame_dev, branch dev → main when green
session:     a FRESH GasCoopGame_dev session (Unity-MCP + v8 contract). NOT the old c-exec-013 builder chat (its premise is superseded).
```

**READING-SET (read FIRST, in order):**
1. `knowledge/g9c41-gas-engine-SPEC.md` — the canon (RE-SHAPED 2026-06-26: layered coordinating grid; Факт 2 + §9 швы 9/5/2 + §7).
2. `work/gas-engine-layered-reshape-R1-2026-06-26.md` — the R# (this CALL's source; §3 = the contract deltas; §5 = the refutation log).
3. `work/gas-engine-build-roadmap-2026-06-26.md` — the small-steps order + owner-playable scenes + benchmark.
4. `work/c-exec-013-call.md` — PRIOR CALL, kept as HISTORY for the carried-over (model-agnostic) hardening — see §3.

**OPEN WITH A PLAN (owner present).** Leg ritual (unchanged): §Re-sync repo contract v8 FIRST → PLAN (classify each mechanic ведро-1/2/3, default Вариант A) → RED-first **INDEPENDENT test-author** (builder cannot edit the RED tests) → integer zero-legacy build → -Deliver gate → fresh-session G5 refutation → owner-eye «точно/весело». Approach token += `+layered: structure-25 reads markers+geometry → integer per-Z-band projection → gas-50`.

---

## §1 SCOPE

**S0-LAYERED** = a sandbox where the owner SEES a DA level become the **LAYERED grid** (gas 50cm authoritative + structure 25cm), watches gas FILL A ROOM by integer face-flow through **real door apertures** (not whole-wall), and signs «точно + весело». Built in **small owner-PLAYABLE steps** (roadmap §steps 1–4).

**IN:** structure-layer reader (DA geometry + module markers → gas-grid 50 + structure-grid 25 + region_id + door apertures); door = validated aperture → per-Z-band conductivity projection; gas face-flow consuming that projection; per-face/breach data-path (stub + a one-breach proof); determinism + lockstep loopback; the sandbox; a clickable benchmark harness (incl. the hangar probe).

**OUT (later slices / RESERVED, do NOT build):** breach BEHAVIOR beyond the one-breach data-proof (S5); reactions/chemistry/cascade (S6); placement MECHANIC (resolution reserved only); **big-hall optimization** (`mid-2.5D` far-LOD + sub-partition — RESERVED, OFF, owner-sign-gated); pretty/stylized render (Track V, g-7e15 — sandbox uses crude slabs/gizmos); monotone-B BEHAVIOR (predicate + the oracle RED only); sphere-cap BEHAVIOR beyond reserving the radius+cell-size as a locked config.

---

## §2 done_when

`[HEADLESS-RED]` = authored by the INDEPENDENT test-author from the SPEC BEFORE build; the builder cannot edit. `[BUILD-SCAN]` = a real gate (check.ps1). `[OWNER-RUN]` = binding, no self-marking. «точно» is DISCHARGED by the green `[HEADLESS-RED]`+`[BUILD-SCAN]` suite; «весело» is the ONLY owner-run axis.

**(1) STRUCTURE-LAYER READER → LAYERED GRID `[HEADLESS-RED]`**
- **PLACEMENT (hard):** the reader + voxelizer + the doorway→open-sub-faces integer function live in `Assets/GasCoopGame/Core/**` (engine-free, integer-only; a `using UnityEngine` / `using DungeonArchitect` there FAILS the dependency-boundary gate by construction). A reader in `Adapters/**` = a STOP-v8 substitution.
- DA levels enter as engine-free integer boundary data (`RoomSpec`/`LinkSpec`), never the DA internal model. The reader reads the **BUILT geometry + module MARKERS**, not the generator.
- **Two grids:** gas-grid **50cm** (authoritative sim) + structure-grid **25cm** (topology). `resolution_tag` default `(geometry_res=25, gas_res=50)`; INVERTED invariant `gas_res = integer multiple of geometry_res` (`TopologyConformance` REJECTS non-integer ratios). *S0 may START at `(50,50)` 1:1 for the determinism ramp, then config-switch to `(25,50)` — NO rebuild; BOTH must be green.*
- **Marker contract (the c-exec-012 anti-cheat reframed):** GEOMETRIC markers (wall/floor/opening/breach-face) — authored on reusable modules (owner OR builder-via-MCP), **VALIDATED against the built mesh**; SEMANTIC markers (material / breach-threshold / direction-mask / region_id) — **owner/fixture authored ONLY**; the builder READS them and may NEVER author/edit a semantic marker to satisfy a test.
- **RED:** (a) re-voxelization byte-identical (same DA-derived `RoomSpec` → byte-identical layered grid on re-run); (b) fixture correctness (in-code `RoomSpec`/`LinkSpec` → the expected grid: cells, `region_id`, per-face open/closed); (c) `resolution_tag` invariant (reject 75-vs-50, accept (25,50)/(50,50)/(25,100)).

**(2) DOOR APERTURE + STRUCTURE→GAS PROJECTION `[HEADLESS-RED]`**
- A door = a structure-layer **declared aperture** = a rectangle of open 25cm sub-faces (BOTH width AND height), declared on the module, **validated vs geometry**: the validator MUST independently re-derive the 25cm sub-face occupancy FROM the built mesh and assert `declared == derived` (a validator that trusts the marker without re-deriving = STOP-v8). This is the old generator-blind mesh-read, now at 25cm and as a VALIDATOR, not a source.
- Structure stores a **per-gas-face 25cm sub-face occupancy BITMAP**. Gas reads the PROJECTION: `conductivity = count(open 25cm sub-faces WITHIN its Z-cell's face)` — computed AFTER the gas grid's Z-cell decomposition, so a low aperture opens the LOW Z-cell face (conductivity>0) and NOT the high one (conductivity=0), SEPARATELY. `conductivity` is a COUNT (0..N), NEVER a divided ratio (no float, no `/4` integer-division — it strangles the slit, violates R6).
- This SUPERSEDES the product-repo S1 rule "lateral = full shared boundary": gas opens only the declared aperture's sub-faces. The "газ открыл всю стену" bug is structurally precluded.
- **RED:** (a) low-slit vs high-transom NEGATIVE CONTROL — two fixtures with IDENTICAL whole-face open-sub-face count MUST produce DIFFERENT gas behavior (low drains the low cell, high does not); the naive scalar-0..4 projection MUST fail this, the per-Z-band one passes; (b) conductivity-is-count (a planted `/4` MUST fail an oracle).

**(3) FACE-FLOW `[HEADLESS-RED]`**
- Gas fills a room by integer face-flow (gather-then-apply + carry) that **CONSUMES the per-Z-band conductivity count as DATA** (the named near supersede of the area-blind `t=mEq/kP`).
- **RED:** (a) MONOTONIC (per-tick transfer non-decreasing in open-face count); (b) **SLIT-SEEPS** (flow strictly >0 at conductivity=1); (c) WALL-ZERO (closed face = 0); (d) MASS-CONSERVATION (integer, clamped [0,cap], loud assert never silent wrap); (e) EMERGENT-HEIGHT (a low doorway drains only the low Z-cells, now at 25cm per-Z-band granularity).

**(4) PER-FACE / BREACH DATA-PATH `[HEADLESS-RED]`**
- Per-face record carries, as integer fields present day-one with inert defaults: open/closed; conductivity (= the projected per-Z-band count); direction-mask (bidirectional stub); breach/explosion threshold (disabled stub). Part of the checksummed face record; the sub-face occupancy bitmap stays OUT of checksum in S0 (count-only) — **trip-wire (invariant):** the FIRST slice where any effect depends on WHICH sub-faces are open MUST first fold the bitmap into the meaning-checksum (canonical sub-face order) — decide this schema NOW, not as a live-node migration.
- **One-breach PROOF (S0 scope, NOT S5):** flip ONE previously-closed GEOMETRIC sub-face (a validated geometric flip, NOT a semantic-threshold write) → re-project → conductivity 0→1 → gas flow through that face changes. `breach_threshold` stays an inert owner-authored stub (the breach proof is NEVER where a builder writes a semantic value). On a NEAR non-collapsed face only (re-flux/collapse interaction = S4/S5, out of scope).

**(5) DETERMINISM-BY-CONSTRUCTION `[HEADLESS-RED]` + `[BUILD-SCAN]`**
- Integer-only authoritative path. **zero-float scan** as a real `check.ps1` gate over `Core/**` — now spanning BOTH grids + the structure→gas projection (a structure-layer sub-face decision in `Adapters/**` or via float marker geometry = STOP-v8). A planted-float RED control MUST trip the scan.
- **loopback** (2 processes, ONE machine) byte-identical hash; real 2 physical machines NEVER a gate. Integer mass clamp [0,cap] = loud assert, never silent wrap.

**(6) SANDBOX `[exists: scene artifact, owner-PLAYABLE]`**
- A test scene with: load an owner-generated DA level → SEE the layered grid + room labels (`region_id`) + door APERTURES highlighted (no gas yet) `[roadmap step 1 — this is where the owner verifies "doors/types read right" by eye, the ORIGINAL question]`; spawn-at-cell → WATCH gas fill + flow to the next room via the aperture, emergent low-creep `[step 2]`; door-toggle; orbit camera. Render = the existing **crude slabs/gizmos** (pretty render = Track V, NOT here).

**(7) BENCHMARK HARNESS `[exists: clickable Unity scene]`**
- A scene with a button: run a scenario → measure **active cells + frame-time** and show the numbers. Two scenarios: a TYPICAL one (several sources, medium rooms) and the **HANGAR PROBE** (one player in a large open volume, full-3D, Burst/Jobs) — the #1 unmeasured number.
- ⚠ **Machine caveat (encode in the readout):** gas-sim is CPU, not GPU; the owner's RTX-4090 / top-AMD rig makes numbers OPTIMISTIC. Report cells+ms and compare to the **weak-target budget** (~200k active-cell comfort ceiling on a weak core), NOT "smooth on my rig".

**(8) ZERO-LEGACY `[BUILD-SCAN]`** — the dead DA→grid path removed (see §3 keep/delete set); no unused/legacy code in the tree.

**(9) OWNER-EYE `[OWNER-RUN, binding, no self-marking]`** — ALL `[HEADLESS-RED]`+`[BUILD-SCAN]` GREEN (authored by the independent test-author, builder can't edit) BEFORE the gate is offered. «точно» = the green suite. «весело» = the owner opens the sandbox, sees level→grid→gas-filling, signs (early). An owner sign-off NEVER substitutes for a missing/red test.

---

## §3 PRESERVED from c-exec-013 (carried over UNCHANGED — read `work/c-exec-013-call.md` for the verbatim text)

- §0 PRE-FLIGHT (§Re-sync v8 first; canon single-source; OPEN-WITH-A-PLAN; the RED-first independent-test-author → -Deliver → fresh-session G5 → owner-eye ritual).
- The 4 GAP sockets (cap / void-sink / `resolution_tag` / `tick_divisor`) + `{energy_sum, capacity_sum}` temp-pair + the per-edge flux-register as day-one STUBBED DATA.
- KEEP-set (proven healthy): `TopologyDocument` / `TopologyConformance` / `TopologyStableIds`; `RoomSpec`/`LinkSpec` (engine-free integer DTOs); RN1 read-model (`IGasReadModel`/`CoarseGasReadModel`/`ExposureQuery`, frozen, NOT mutated — the visual track targets a NEW near-50 read-model built alongside).
- DELETE-set: `SnapGridFlowRoomReader.cs` + `VScale=2` crutch + `SnapGridFlowTopologySource.cs` (DA-model read) + scene reconcile. ChunkEncoder `(byte)c` overflow = OUT of S0 (S2 net), named deferral.
- The 2-band coarse tier = keep-as-far-tier until S4; S0 builds the NEW 50cm near-grid + face-flow as a net-new `Core/Field/Voxel/` subtree, COEXISTENCE not replacement.

---

## §4 STOP-discipline v8 (anti-substitution — reshaped per R# §3)

A blocked/infeasible NAMED approach or a crutch = mandatory STOP + escalate, NEVER a silent substitute/descope. **Forbidden as a substitution:** VScale-style scaling crutch; per-LEVEL marker editing to pass a test; **trusting a geometric marker WITHOUT re-deriving its sub-face occupancy from the built mesh**; a builder authoring/editing a SEMANTIC marker (no oracle) to satisfy a test; the voxelizer/projection in `Adapters/**` (outside the gated zero-float Core). **The builder may author EXACTLY what an oracle can refute, nothing more.** Anti-fabricated-approval: «весело» is the only non-unit-testable axis = OWNER-RUN; a leg may not close on an unconfirmed owner-run step.

---

## §5 HAND-OFF

- **BUILD runs in `GasCoopGame_dev`** (MCP + dev branch + v8 contract), a FRESH session — NOT the OS worktree (PLAN-only here) and NOT the old c-exec-013 chat.
- **RED tests authored there by the INDEPENDENT test-author** BEFORE build (builder can't edit): the (1)–(5) clauses above, incl. the low-slit-vs-high-transom negative control, the geometric-marker-⟂-mesh validation (with independent sub-face re-derivation), the conductivity-is-count oracle, and the breach geometric-flip projection RED.
- **RESULT applied home by a separate OS writer** (this CALL is PLAN/author-only). On GREEN → S0 done + open S1 (выброс-при-спауне + выдавливание). On STOP (a named approach proves infeasible) → escalate to the direction, never substitute.

END_OF_FILE: live/indie-game-development/work/c-exec-014-call.md
