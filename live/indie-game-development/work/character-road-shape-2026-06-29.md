# Character road — shape (2026-06-29, s-work-030)

Owner approved «можем оформлять» (d-character-road-001). This shapes the CHARACTER ROAD — the ordered near-term slice
spine that builds the visible "jewel" (gas with character), chosen OVER the far-tier S3/S4 plumbing (deferred to "when
levels get big"). Rolling-wave: only the FIRST slice is detailed here; the rest are named + dependency-tagged and shaped
when their turn comes. Basis: the plan audit (work/gas-engine-plan-audit-2026-06-29.md) + the decided seams in
d-character-road-001 (R15 layered params, day-one TypeId socket, moddability seam, dense-vs-sparse, port-old-far-tier-math).

## The ordered road (near-term spine, replaces the "S6+ ellipsis" + reprioritizes ahead of far-tier)

1. **Sc-types — META-TYPE / TYPE PARAM STRUCTURE (ACTIVE, first).** The substrate everything else keys off.
2. **Sc-weight — WEIGHT / BUOYANCY.** Per-type vertical drift (heavy sinks / light rises, tunable). Keys off Sc-types.
3. **Sc-reactions — REACTIONS.** Integer chemistry: ≥2 types react → telegraph + bang = coarse event; mix-overlay cell.
   Keys off Sc-types (needs ≥2 types).
4. **Sc-damage — DAMAGE / TEMPERATURE.** Dose-from-coarse (gas hurts; type-specific); temperature as a sink-layer.
   Keys off Sc-types + Sc-weight; the first real gameplay payoff. The co-op-interdependence affordance
   (d-coop-interdependence-repin-001) is folded into this + Sc-reactions PLANs (where a shared gas consequence the 2nd
   player feels lives).

DEFERRED (not deleted) — the far-tier S3 (height-routing layers) / S4 (coarse rollup + no-pop) / S5 (breach): scale-plumbing
for big/~150-room levels, NOT urgent at the current small scale. Re-prioritize when levels grow. (S5 breach carries the
sub-face-bitmap checksum trip-wire when it lands — canon §4 шов 5.)

## SLICE 1 detailed — Sc-types (META-TYPE / TYPE PARAM STRUCTURE)

GOAL (outcome): the engine carries MORE THAN ONE gas type, and types behave DIFFERENTLY, driven by a 3-LAYER DATA-DRIVEN
param structure — so the owner SEES two test gases behave visibly differently (in the engine's debug view), and the
foundation for weight/reactions/damage is laid. ENGINE-ONLY (no visual-track hookup this slice).

What it builds:
- **3-layer param structure (R15):** shared PARENT params common to ALL gases (density / packing, ratio-to-air = weight
  class, spread speed, …) defined ONCE → per-META-TYPE group params → per-type/per-instance tuning (env intensity/danger at
  spawn). A type = pure DATA/config; NOTHING about a type hardcoded in C#.
- **The engine actually carries ≥2 meta-types** (flip speciesCount>1; the [species][cell] shape is already there) that
  differ via the params that EXIST today — primarily SPREAD SPEED (per-type Kp) + density/packing — so the difference is
  real + visible (one gas billows fast, one creeps slow). (WEIGHT difference = Sc-weight; REACTIONS = Sc-reactions —
  out of this slice; do NOT build them here.)
- **TEST types, not lore:** ship 2-3 PLACEHOLDER meta-types chosen to SPAN the behaviour range (e.g. a light-fast vs a
  heavy-slow), explicitly marked TEST/placeholder. Purpose = exercise different behaviour; real lore types replace the
  config later with ZERO structure change.
- **Day-one DETERMINISM socket:** per-cell dominant-TypeId folded into the MeaningChecksum (canon §9.5 wanted it day-one;
  was skipped) — so reaching more types later is NOT a painful networked-schema migration. Safe to add now (loopback only;
  network ~S4).
- **MODDABILITY seam (reserve, don't build the mechanism):** the type set = an ORDERED, CONTENT-HASHED, session-FIXED
  REGISTRY; its content-hash reserved as a hook for the future lockstep session-start handshake (Факт-5 no-late-join makes
  this natural). Ship a fixed built-in TEST set; later DLC/mod types = more registry entries. DEFER actual external
  mod-loading (asset bundles / mod API / workshop).

Boundaries / STOP:
- NO visual-track hookup (engine-only; the look connects in a later step; visual track continues on dev2 independently).
- NO weight/buoyancy, NO reactions, NO damage, NO temperature (those are Sc-weight/Sc-reactions/Sc-damage).
- NO lore-canon types (test placeholders only). NO real mod-loader (seam only).
- NO hardcoded-in-C# type enum/switch (would weld moddability shut). Lock = ADR-0002; determinism preserved.

done_when (verifiable, set at framing):
- PLAN (owner present): §Re-sync; ingest d-character-road-001 + R15 + canon §3/§4/§9.5/Факт-4; DECIDE the representation
  (dense [species][cell] vs Факт-4 sparse-dominant — dense ok at few test types, but record the decision); classify ведро.
- Engine carries ≥2 test meta-types behaving differently (per-type spread/density) — RED tests proving they DIVERGE in
  behaviour AND that a single-type run reproduces today's S0/S1 goldens byte-identical.
- The 3-layer param table is data-driven (a type = a data asset/registry entry; an independent RED test proves NO type is
  hardcoded — adding a test type touches only data).
- Per-cell dominant-TypeId in the MeaningChecksum (RED: two peers with different type assignment diverge); the registry
  content-hash exists + is reserved for the handshake (RED: a different registry → different hash).
- check.ps1 -Deliver GREEN + mutation ≥70 on new Core + spec-silence + deliverable-coverage; loopback determinism hash
  green (the new per-type code inside BOTH zero-float/int-overflow scan roots — close the scan-root parity gap here);
  ZERO-LEGACY; fresh-session G5; owner-eye (sees 2 test gases behave differently in the debug view — confidence, not a gate).
- ведро: substrate → ведро-2 (the type set + per-cell TypeId are in-checksum, shared); no ведро-1/3.

ведро / cut list (G6):
- CUT this slice: visual hookup; weight/reactions/damage/temperature; lore types; the real mod-loader; far-tier.
- The riskiest assumption tested first: that ≥2 types behave differently AND stay deterministic in loopback (the per-type
  param path must not introduce float / order-dependence).

## NEXT
Frame Sc-types as the executor CALL c-exec-019 (PLAN-first, owner present) → adversarially harden (like c-016/c-018) →
owner opens it in a fresh GasCoopGame_dev session. Then the road rolls to Sc-weight.

END_OF_FILE: live/indie-game-development/work/character-road-shape-2026-06-29.md
