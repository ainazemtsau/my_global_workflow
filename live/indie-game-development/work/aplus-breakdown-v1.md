# A+ breakdown — v1 (dependency order + wave tree + Wave-A detail)

> **Status:** DRAFT proposal for owner card-by-card approval (G9). Produced by the A+ breakdown workflow (wf_de2cf689-047:
> 2 dependency-DAG agents + 4 wave-card agents + 2 adversarial critics) over work/aplus-wave-map-v1.md + the gas-model doc +
> the ACTUAL GasCoopGame code (HEAD main a89b36b). Every grow-vs-rewrite call is code-grounded and was verified by both critics.
> **Critic verdict: SOUND PLAN, RIGHT SHAPE, grounding holds — with ~5 hardening fixes (all "lock the keep-open seams EARLY so
> a wave doesn't weld them shut"), folded into §4 below.**

## 1. Dependency order — what to build first (both DAG agents converged)

**Start = the test SANDBOX (P0).** Nothing can precede it: every probe and every feature is verified the same way — drive the
core (spawn gas anywhere, load any level, pause, snapshot) and observe. Owner R3: «нужен достаточно быстро».

Critical path:
```
P0 SANDBOX
  → P1 active-gas CAP + wire-plane NUMBER   ┐
  → P2 cell-CEILING + round-robin + awake-set DETERMINISM
  → P3 §G(+4) PROBE-GATE  (the de-risk wall)   ← P4 HOST-MIGRATION spike runs here too
      → P5 wire RectDecomposition (sub-sector topology)
        → P6 integer geodesic FRONT (front-across-seam)
          → P7 interest-grain + sleep (graceful under PEAKS)
            → P8 visibility-as-truth (host one shared field)
              → P9 resident-gas DAMAGE law
                → P10 reactions (telegraph + queue)
                  → P11 explosion = mass-transfer + cascade
                    → P13 break-line pre-cut → P14 destructibility A → P15 B + host-migration impl
```
**Hidden deps the critics confirmed (these are the "build X before its own probe" traps):** P2 (ceiling+round-robin) must
exist before the §G#2 8-bubble probe can run; P1 (the cap NUMBER) before any many-species work; P6 (front) AFTER P5 (sub-sector
topology) — a front over a room-bounding-box cuts through an L-shaped wall; P13 (break-line pre-cut at generation) before
Case-B destructibility; P4 (host-migration spike) early enough to VETO authority assumptions the feature waves bake in.

## 2. Wave tree (5 cards — outcomes only, for approval)

**Wave A — Lab + de-risk wall.** *Outcome:* a Unity test LAB exists (owner opens ONE scene, picks a saved scenario from DATA,
presses Play, watches coarse gas on any level; Claude reads snapshots) AND a signed verdict that the A+ core has NO load-bearing
blind spot (every §G+4 probe ran RED/measured against the real kept core). *Why:* the de-risk wall before any feature — the cure
for the owner's #1 fear (a core mistake found late). *Unity-check:* owner runs a scenario, sees gas spawn/flow/pause; runs the
probe scorecard (mostly headless `dotnet test` + a couple eyeball ones), every probe GREEN. *Riskiest assumption:* the integer
core stays bit-exact across two (loopback) machines under a SPIKE — when the awake-set/ceiling/round-robin the spike rides don't
exist yet (so we build minimal versions just to prove their determinism).

**Wave B — "Where is the gas".** *Outcome:* on a real DA level of hundreds of rooms, you SEE exactly where each gas is and where
its advancing edge reached — big/L-rooms split into sub-sectors that flow correctly, an integer FRONT that rounds corners
without a kink, detail raised only near the player/event (surviving peaks). *Why:* this is the owner's actual pain ("газ слишком
крупно, не вижу ГДЕ"). *Unity-check:* load a real level, spawn one source, watch an L-room flow as several slabs + the front
creep room-to-room, no kink at seams. *Riskiest:* the front stays continuous across both the sub-sector seams AND the detailed-tier
boundary.

**Wave C — "Consequence".** *Outcome:* gas DOES things — damage only where gas really sits (§E law #1), reactions that telegraph
then fire (§E law #3, queue on overflow), explosion = mass-conserving transfer + next-tick cascade, ventilation (integer
edge-modifier, NO float solver). *Why:* transport proven ≠ a game; consequence is where depth starts. *Unity-check:* an object
breaks only under resident gas; two gases blink then react; a blast keeps total mass identical; a vent drains.

**Wave D — "Robustness".** *Outcome:* break walls (Case A opens a hole / Case B splits a room via pre-cut break-lines); kill the
host and the 4-8 session survives; a blast-door closing on a gas column conserves mass. *Why:* the co-op value-prop + the §H
open chunks. *Unity-check:* blow a hole → gas flows through; collapse → room splits; host quits → others keep playing.

**Track V — Visual GASG (∥, secondary).** *Outcome:* gases read as distinct types/meta-types, derived from sim params, reading
RN1 + the front; fog without "shelves". *Why:* the showable layer (owner: after the core). *Gate:* research can start at the
sandbox; IMPLEMENTATION waits only on the read-seams (RN1 ✓ + the front from Wave B), NOT on the core finishing.

## 3. Wave A in detail (the first wave — sandbox + probe-gate)

**GOOD NEWS (code-grounded): most of the SANDBOX is assembling pieces that already exist** — so Wave A is lighter than feared:

| Sandbox piece | grow/rewrite | grounding (HEAD a89b36b) |
|---|---|---|
| one parametric harness scene + director | GROW | `GasViewDirector.cs` is already a single-MonoBehaviour parametric harness (LevelSource enum, inspector knobs) |
| generate-any-level | GROW | `InCodeRoomLevelProducer(roomCount)` + `SnapGridFlowTopologySource(seed)` exist |
| spawn gas anywhere/any amount | GROW | `CoarseField.SetSource(sector,band,species,perTick)` exists (perTick=0 removes) |
| pause / step / tick-rate | GROW | director coroutine already gates on `_running` + tickInterval; `CoarseField.Step()` exists |
| snapshot → structured log for Claude | GROW | `GasViewDebug` already emits per-run JSON |
| MCP-drivable | GROW | `GasViewDirector` already sets `runInBackground=true` for MCP drive |
| **scenario-as-DATA + seed catalog** | **NEW** | no config-as-data today (knobs are inspector floats) — the one real new build |

*Cuts (Wave A):* the full MCP-adapted-scene-for-Claude (DESIRABLE-not-required, R3 — ship inspector-driven + Claude-reads-snapshots
if the live drive is costly); Odin live-table polish (don't gate on a paid asset); PGG-inside (later, seam reserved); pretty
rendering (Track V); a bespoke scene per probe (anti-sprawl — all probes ride the one lab via scenarios).

**The §G(+4) PROBE-GATE** — mostly reuses existing harnesses, builds a few new mechanisms only to PROVE their determinism:

| Probe | grow/new | note |
|---|---|---|
| host+2-follower bit-exact under fault | GROW | `CoarseReconstructionHarness` already runs host + 2 followers (loopback) |
| mass-conservation RED (any op changing mass = BUG) | GROW | `MassConservationTests` already asserts exact integer mass every tick |
| scale bench at hundreds of rooms | GROW | `CoarseScaleTests` already drives ~3,300 sectors |
| breach (Dijkstra-on-breach input) | GROW | `CoarseField.CommandBreach` + `CoarseBreachLayer` exist |
| render probes §G#6 slab-count / §G#7 no-shimmer | GROW | ride the existing GasDebug overlay (NOT Track V) |
| **integer geodesic FRONT (minimal, to probe)** | **NEW** | no front/Dijkstra exists |
| **cell-CEILING + round-robin + awake-set determinism** | **NEW** | no awake/sleep/budget code exists — the highest silent-desync risk |
| **resident-dose hook + confirmed-colocation guard (stubs/RED)** | **NEW** | `ReactionLayer` is a toy; build the LAW-enforceability proof, not the feature |
| **host-migration authority-handoff SPIKE** | **NEW** | one-host today, zero migration path — spike to veto bad assumptions early |

## 4. Critic hardening fixes (fold into Wave A/B — these are the "found-late core blind spots", caught now)

1. **Reserve the per-SPECIES temperature plane BEFORE fixing the wire-plane NUMBER (P1).** Today temperature is ONE shared
   `int[BandCellCount]` plane (key 6); planes 2-5 are the only free species keys. If P1 fixes the budget without reserving for
   per-species temperature, it welds shut the keep-open seam the sweep caught. → P1 consumes the per-species-temp keep-open first.
2. **Decide the coarse-layer DATA SHAPE early (transient + front + source-XY, NOT settled-only / room-totals).** Return-fidelity
   (d-returnfidelity-001, owner-signed) is buried as a late B5 sub-clause, yet the front (B2) + interest-grain (B3) build on top
   of it. → pull "data-shape = not-settled-only + source-XY filled (TopologyAnchor populated)" to the FRONT of Wave B, before the
   front is built. (Source-XY is dropped at `SetSource` + `TopologyAnchor` is empty today — fill it upstream.)
3. **Gate the interest-grain / visibility design (B3/B4) on the host-migration SPIKE verdict (A4).** If migration needs detailed
   state to be reconstructable (not host-private), that constrains the interest-grain design — so the spike's verdict must land
   before B3/B4 bake in host-private detailed state.
4. **Define the awake-set determinism CONTRACT once (Wave A), and make the Wave-B mechanism conform** — don't build a throwaway
   scaffold in A with a different determinism contract than the real B mechanism (the probe would then be meaningless).
5. **Name the two §H open chunks that were unplaced + add one probe:** (a) **GRIEFING** (a deterministic sim in players' hands =
   primitives to harm a teammate: gas a room, block ventilation, lure-and-ignite) — named-OPEN (co-op design, not built now);
   (b) **coarse economy under MANY small sources / pervasive leak** (the twin of the D.5 rarity invariant — "sleeping = zero"
   collapses if half the always-on level leaks) — named-OPEN + a Wave-A telemetry note; (c) add a **moving-geometry
   mass-conservation probe** to the A5 gate (a blast-door closing on a gas column must not create/destroy the bisected mass) —
   every other mass-conservation claim has a probe, this one didn't.

Minor honesty corrections (owner R2 demands exact grounding): "RectDecomposition is NEVER called" is overstated — it IS referenced
in `SnapGridFlowRoomReader`; the unwired part is the sub-sector SPLIT path through `FromTopology` (still GROW). And the KEEP core
is proven by t-1/t-2/t-5 (which passed the full strong gate), NOT by t-4 (which was the deviation-close, per s-review-002) — cite
the right legs.

## 5. Grow / rewrite / keep — the headline

- **KEEP untouched (the proven-expensive part — re-proving = months):** integer "water" core (`CoarseBandStep` mass-exact
  orifice/settle), host+2-follower bit-exact replication + client reconstruction (`CoarseChunkFollower` reconstructs-not-recomputes),
  the LOCKed stream, the geometry-derived-id pipeline, the frozen RN1 read-seam, ROOM capacity + back-pressure.
- **GROW (additive on the proven core):** the sandbox (assemble existing harness), RectDecomposition wiring, the scale/mass/breach
  probes, visibility-authority, return-fidelity transient (already streams).
- **REWRITE-clean / NEW (above the core — owner's "throw out, don't drag the tail"):** the geodesic front, interest-grain +
  ceiling/round-robin, resident-gas damage law, **reactions (today's `ReactionLayer` is an explicit toy → rewrite)**, host-migration,
  the sparse gas-encoding (only if a level authors >the cap), the GASG visual language.

END_OF_FILE: live/indie-game-development/work/aplus-breakdown-v1.md
