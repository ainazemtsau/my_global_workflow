# CALL c-exec-019 — Sc-types: META-TYPE / TYPE PARAM STRUCTURE (multi-gas foundation, ENGINE-ONLY)

Direction: indie-game-development / g-9c41 / Sc-types — the FIRST slice of the CHARACTER ROAD (d-character-road-001, owner
«можем оформлять» 2026-06-29). Builds on the clean post-S2 base (GasCoopGame `main` @adb9255). Executor: a FRESH
GasCoopGame_dev session (branch `dev` → `main` when green, owner-gated). Opens with a PLAN (owner present).
State source = NOW.md (active_tasks Sc-types). Canon = knowledge/g9c41-gas-engine-SPEC.md (R15 §5:134, Факт-4, §9 шов 5/§9.5,
the §1 ADR poprawка: lock = ADR-0002). Shape basis = work/character-road-shape-2026-06-29.md.

## Why this slice (and the lock id)

The plan audit found the "jewel" (characterful gas) is built nowhere; the owner chose the CHARACTER ROAD over far-tier
plumbing. This is its FIRST slice: the multi-gas TYPE substrate everything else (weight, reactions, damage) keys off. Lock =
**ADR-0002** (input-lockstep); determinism preserved, not reopened.

## goal (outcome, not method)

The engine carries MORE THAN ONE gas type, and types behave VISIBLY DIFFERENTLY, driven by a 3-LAYER DATA-DRIVEN param
structure (R15). Owner SEES two TEST gases behave differently in the engine debug view (e.g. one billows fast, one creeps
slow). The day-one determinism + moddability sockets are laid so weight/reactions/damage and later real/DLC types plug in
without a schema migration or a desync. **ENGINE-ONLY — no visual-track hookup this slice** (the look connects later; the
visual track runs independently on dev2).

## context (read first — applied, not just cited)

1. **§Re-sync the GasCoopGame repo contract FIRST.**
2. **d-character-road-001 (NOW.md decision_inbox) — the decided design** (R15 3-layer params, day-one TypeId socket,
   moddability seam, dense-vs-sparse-at-PLAN, port-old-far-tier-math). + the shape doc work/character-road-shape-2026-06-29.md.
3. **Canon:** R15 (§5:134 — shared PARENT params + per-meta-type group + own visual + per-type config; visual is procedural
   FROM params); Факт-4 (sparse-dominant model + chemistry as DATA day-one); §9 шов 5/§9.5 («Чексумм покрывает СМЫСЛ» —
   includes `TypeId` слота); the lock = ADR-0002.
4. **CODE STATUS (verify first-hand):** VoxelField mass/flux/carry are already `[species][cell]`; VoxelFaceFlow loops
   per-species; `SeedMass(cell,species,mass)` is species-aware — but `speciesCount=1` is pinned, there is NO per-type PARAM
   table (the flow law has one Kp for all), the forced-flow bias is per-FACE not per-type, and the MeaningChecksum has no
   per-cell dominant-TypeId. So this is an EXTENSION of the existing shape, not a rewrite.
5. **The OLD far-tier already has proven 4-species + weight + heat integer math** — PORT/reuse that proven law where
   relevant rather than re-R&D it (and note it must be ported before S4 ever deletes the far tier).

## the 3-layer param structure (R15)

- **Shared PARENT params** (common to ALL gases, defined ONCE, never copied): density / per-cell packing, ratio-to-air
  (weight class), spread speed, … (the PLAN enumerates the day-one set).
- **per-META-TYPE group params** + (later) its own visual — a meta-type overrides/extends the parent.
- **per-type / per-instance** = pure config + env tuning (intensity/danger at spawn).
A gas type = a DATA asset / registry entry. **NOTHING about a type is hardcoded in C#** (no enum/switch on types — that
welds moddability shut + forces a rewrite).

## boundaries (out of scope / STOP-escalate if tempted)

- **NO visual-track hookup** (engine-only; the look connects in a later step; do NOT touch the dev2 visual track).
- **NO weight/buoyancy, NO reactions, NO damage, NO temperature** — those are Sc-weight / Sc-reactions / Sc-damage. Types
  differ THIS slice only via params that EXIST (spread speed, density/packing). (The PLAN may decide a minimal weight is in
  scope — owner present — but default is OUT.)
- **NO lore-canon types** — ship 2-3 TEST/placeholder meta-types spanning the behaviour range; real types are config later.
- **NO real mod-loader** (asset bundles / mod API / workshop) — reserve the SEAM only.
- **NO hardcoded C# type enum/switch.** Lock = ADR-0002 (input-lockstep) — NOT reopened; no stored velocity / float on the
  authoritative path / re-flux-as-gate = STOP-escalate. Laws in headless Core/**.

## done_when (verifiable)

1. **PLAN (owner present):** §Re-sync FIRST; ingest d-character-road-001 + R15 + canon §3/§4/§9.5/Факт-4; DECIDE the
   representation (dense `[species][cell]` vs Факт-4 sparse-dominant — dense ok at few test types, RECORD the decision +
   when it must revisit); classify ведро; pick the 2-3 TEST meta-types + the day-one parent-param set.
2. **≥2 TEST meta-types behave DIFFERENTLY** via per-type params (spread speed / density) — independent-author RED tests:
   the two types DIVERGE in behaviour on a seeded run; AND a single-type run reproduces today's S0/S1 goldens byte-identical
   (no regression).
3. **3-layer param structure is DATA-DRIVEN** — a type = a data asset / registry entry; an independent RED test proves NO
   type is hardcoded (adding a test type touches DATA only, no C# change). Shared PARENT params defined once (no copy).
4. **Day-one DETERMINISM socket:** per-cell dominant-TypeId folded into the MeaningChecksum (RED: two peers with different
   per-cell type assignment DIVERGE the checksum; a silently-absent TypeId field stays green = FAIL).
5. **MODDABILITY seam reserved:** the type set = an ORDERED, CONTENT-HASHED, session-FIXED registry; its content-hash exists
   + is reserved as the lockstep session-start handshake hook (RED: a different registry → a different hash). Built-in TEST
   set only; external mod-loading DEFERRED.
6. **DETERMINISM by construction:** integer-only authoritative path; the per-type code inside BOTH zero-float + int-overflow
   scan roots (CLOSE the scan-root parity gap surfaced by S2b — add the new authoritative subtree to both scans + a
   self-test); loopback determinism hash green over a multi-type seeded run (planted-float / order-dependence RED controls).
7. **check.ps1 -Deliver GREEN** (build + headless + zero-float + int-overflow scans + mutation ≥70 on new Core + spec-silence
   + deliverable-coverage). G0-frozen (openspec + frozen spec + ledger + mutation-<id>.json ≥70; RESULT.md = DELIVERED).
8. **ZERO-LEGACY**; tests rewritten not dragged.
9. **OWNER-EYE (confidence, NOT a gate):** owner sees 2 test gases behave differently in the debug view; owner-run, no
   self-marking.

## discipline / gates (carried)

RED-first by an INDEPENDENT test-author (builder cannot edit the red tests) · Core/** placement · -Deliver GREEN ·
mutation ≥ floor (70%) · a FRESH-SESSION G5 (different model family) refuting the per-type determinism / data-driven-no-
hardcode / TypeId-checksum / registry-hash seams + the single-type-no-regression claim — COULD-NOT-REFUTE is the bar ·
STOP-discipline (a hardcoded type path, a visual hookup creeping in, weight/reactions creeping in, float on the
authoritative path, reopening ADR-0002 = mandatory STOP + escalate) · build in small steps.

## return

A RESULT routed HOME (the OS owns the next CALL): outcome + evidence (commits, -Deliver transcript, mutation json, G5
verdict, the multi-type loopback hash + RED-control trips, the representation decision, the registry/handshake seam) +
findings for the planner. dev→main merge + push is OWNER-GATED. On GREEN → the road rolls to Sc-weight (per-type buoyancy).

## budget

One slice. If the PLAN finds the param structure + ≥2 differentiated types + the two sockets is too big for one leg, STOP
and return "split needed" (e.g. the data-driven param table + 2 types + TypeId socket land first; the moddability
registry-hash seam second) — do not silently build a blob. Keep the TEST-types scope tight (2-3, behaviour-spanning).

END_OF_FILE: live/indie-game-development/work/c-exec-019-call.md
