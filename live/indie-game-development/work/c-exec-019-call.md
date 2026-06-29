# CALL c-exec-019 — Sc-types: META-TYPE / TYPE PARAM STRUCTURE (multi-gas foundation, ENGINE-ONLY)

Direction: indie-game-development / g-9c41 / Sc-types — the FIRST slice of the CHARACTER ROAD (d-character-road-001, owner
«можем оформлять» 2026-06-29). Builds on the clean post-S2 base (GasCoopGame `main` at-or-after @adb9255 — the S2b
load-bearing-loopback merge; §Re-sync confirms HEAD first — small repo-hygiene-only commits atop it are expected, e.g.
@2117341). Executor: a FRESH GasCoopGame_dev session (branch `dev` → `main` when green, owner-gated). Opens with a PLAN
(owner present). State source = NOW.md (active_tasks Sc-types). Canon = knowledge/g9c41-gas-engine-SPEC.md
(R15 §5:134, Факт-4, §4 шов 5/§9.5, §1 ADR poprawка: lock = ADR-0002). Shape basis = work/character-road-shape-2026-06-29.md.
HARDENED 2026-06-29 (wf_672e0128-009, 5 must-fix + 10 should-fix folded).

## Why this slice (and the lock id)

The plan audit found the "jewel" (characterful gas) is built nowhere; the owner chose the CHARACTER ROAD over far-tier
plumbing. This is its FIRST slice: the multi-gas TYPE substrate everything else (weight, reactions, damage) keys off.
Lock = **ADR-0002** (input-lockstep; drift-guard per SPEC §1 / d-adr-lockstep-citation-001: read any stray «ADR-0010-as-lock»
in the SPEC or prior CALLs as a citation error — the lock is ADR-0002, the repo's ADR-0010 is the unrelated test-sandbox;
this mis-citation recurred in c-016/c-017, c-018 carried this guard). Determinism preserved, not reopened.

## goal (outcome, not method)

The engine carries MORE THAN ONE gas type, and types behave VISIBLY DIFFERENTLY, driven by a 3-LAYER DATA-DRIVEN param
structure (R15). Owner SEES two TEST gases behave differently in the engine debug view (a settle-rate spread within the
stable range — e.g. one billows fast, one creeps slow). The day-one determinism + moddability sockets are laid so
weight/reactions/damage and later real/DLC types plug in without a schema migration or a desync. Both day-one sockets
(TypeId-in-checksum, registry-hash) are safe to lay NOW because types are not networked-live until ~S4 (loopback only this
slice) — no live networked nodes to migrate (d-character-road-001); deferring them forces a painful networked-schema
migration later. **ENGINE-ONLY — no visual-track hookup this slice** (the look connects later; the visual track runs
independently on dev2).

## context (read first — applied, not just cited)

1. **§Re-sync the GasCoopGame repo contract FIRST** (confirm HEAD; the base is at-or-after @adb9255).
2. **d-character-road-001 (NOW.md decision_inbox) — the decided design** (R15 3-layer params, day-one TypeId socket,
   moddability seam, dense-vs-sparse-at-PLAN, port-old-far-tier-math) + the shape doc work/character-road-shape-2026-06-29.md.
   **CROSS-TRACK single-source SEAM (decided, d-character-road-001):** the engine's gas-type DEFINITION is the ONE source
   for a type — shape the type record so the g-7e15 visual's look-params can attach to the SAME definition LATER, NOT a
   second parallel one (R15: the visual is procedural FROM params — one source, not two). ENGINE-ONLY this slice: RESERVE
   the shape only — add/wire NO look-param, do NOT touch the dev2 visual track.
3. **Canon:** R15 (§5:134 — shared PARENT params + per-meta-type group + own visual + per-type config; visual procedural FROM
   params); Факт-4 (sparse-dominant model; types AND the chemistry/reaction collision-table are both «ДАННЫЕ с первого дня»
   — but THIS slice lays only the per-TYPE param + per-cell TypeId data shape; the reaction/collision-TABLE data shape is
   OUT, deferred to Sc-reactions; cite Факт-4 for the type half only, do NOT claim chemistry-day-one coverage in the RESULT);
   §4 шов 5 / §9.5 («Чексумм покрывает СМЫСЛ» — separates «масса по типу/слою» from the «`TypeId` слота» member); lock = ADR-0002.
4. **CODE STATUS (verify first-hand):** VoxelField mass/flux/carry are `[species][cell]`; VoxelFaceFlow loops per-species;
   `SeedMass(cell,species,mass)` is species-aware — but `speciesCount=1` is pinned, there is NO per-type PARAM table (one Kp
   for all), the bias is per-FACE not per-type, and the MeaningChecksum folds ONLY per-species mass + a per-face species
   index (VoxelField.cs ~281-282) with NO per-cell TypeId field (grep TypeId in Core = zero). EXTENSION, not a rewrite.
5. **FROZEN far-tier (do NOT touch):** the OLD far-tier `CoarseSpecies` (Core/Field/Coarse) is a hardcoded-in-C# species
   table (ADR-0005: `Count=4`, `Weights={64,32,16,8}`, MolecularWeight + buoyancy shift). It is OUT of scope here — its
   proven weight/heat integer math is a future Sc-weight PORT; do NOT refactor it, re-data-drive it, or trip any no-hardcode
   scan on it.

## the 3-layer param structure (R15)

- **Shared PARENT params** (common to ALL gases, defined ONCE, never copied): density/packing, ratio-to-air (weight class)
  [inert DATA/checksum slot only this slice — NO Z-bias/buoyancy reads it; that wiring is Sc-weight], spread speed, … (the
  PLAN enumerates the day-one set).
- **per-META-TYPE group params** + (later) its own visual — a meta-type overrides/extends the parent.
- **per-type** = pure config (exercised by done_when #2/#3). The **per-INSTANCE env-tuning** sub-layer (spawn-time
  intensity/danger) is STRUCTURE-RESERVED THIS SLICE: leave a place for it in the data shape, but its behaviour wiring is a
  later slice — and "danger" tuning has no substrate until Sc-damage, so do NOT wire it here.
A gas type = a DATA asset / registry entry. **NOTHING about a NEAR-tier type is hardcoded in C# on the new per-type/registry
path** (no enum/switch over TypeId — welds moddability shut + forces a rewrite).

## boundaries (out of scope / STOP-escalate if tempted)

- **NO visual-track hookup** (engine-only; the look connects later; do NOT touch the dev2 visual track).
- **Spread speed (per-type Kp) is the ONLY live behaviour-divergence lever this slice.** density/packing + ratio-to-air
  (weight class) are RESERVED, inert DATA slots (folded in the checksum like the existing CapSocket cap stub — drives NO
  near behaviour). Making density/packing OR weight-class behavioural near = buoyancy = **Sc-weight = OUT** (STOP-escalate).
  Porting the far-tier MolecularWeight/buoyancy law (CoarseSpecies) into the near path this slice = Sc-weight creeping in = STOP.
- **A per-type spread param that settles SLOWER-to-converge than baseline is fine; but any per-type realization that violates
  the flow law's monotone-settle floor (Kp ≥ 2*degree, VoxelFaceFlow.cs — a type that NEVER reaches покоя / reintroduces the
  period-2 sloshing the owner-eye already caught) is FORBIDDEN = STOP-escalate.** The fastest stable type cannot exceed the
  baseline stable settle rate. Do NOT prescribe HOW per-type spread is realized — that is the PLAN's call.
- **NO reactions** (incl. the reaction/collision-TABLE data shape — deferred to Sc-reactions, not laid here), **NO weight/
  buoyancy, NO damage, NO temperature** (Sc-weight / Sc-reactions / Sc-damage).
- **NO lore-canon types** — ship 2-3 TEST/placeholder meta-types spanning the behaviour (settle-rate) range; real types are
  config later.
- **NO real mod-loader** (asset bundles / mod API / workshop) — reserve the SEAM only.
- **Per-INSTANCE env tuning = STRUCTURE-RESERVED, not built** (keys off damage, Sc-damage; reserve a data-shape slot only).
- **Any TypeId→index assignment or per-type fold order NOT canonically fixed by the ordered registry** (insertion/dict/glob-
  dependent) = STOP (latent speciesCount>1 desync; moot at the pinned 1). **NO hardcoded C# type enum/switch** on the new path.
- Lock = ADR-0002 — NOT reopened; no stored velocity / float on the authoritative path / re-flux-as-gate = STOP-escalate.
  Laws in headless Core/**.

## ведро classification (PLAN reconfirms — already decided)

- **Ведро-2** (coarse-promotable, IN-checksum, shared by all peers): the TEST type SET + the per-cell dominant-TypeId are in
  the meaning-checksum and shared by every peer (canon §9.5 — `TypeId` слота IS a member) — the substrate all later
  character mechanics ride.
- **Ведро-1** (off-checksum local detail): ABSENT this slice. **Ведро-3** (sub-room AND shared): ABSENT.
The PLAN reconfirms this disposition; it does not re-derive it.

## done_when (verifiable)

1. **PLAN (owner present):** §Re-sync FIRST; ingest d-character-road-001 + R15 + canon §3/§4/§9.5/Факт-4; DECIDE the
   representation (dense `[species][cell]` vs Факт-4 sparse-dominant) AND record a CONCRETE revisit-trigger as a NUMERIC
   threshold (a type-count or active-cell count above which dense MUST be re-litigated — a bare "dense is fine" with no
   named number = NOT done; HOW it's later enforced is the PLAN's call, no code-stub required); reconfirm ведро (per the
   section above — ведро-2 only, no ведро-1/3); pick 2-3 TEST meta-types + the day-one parent-param set.
2. **≥2 TEST meta-types behave DIFFERENTLY** via per-type SPREAD SPEED (per-type Kp) — independent-author RED tests: the two
   types DIVERGE in behaviour on a seeded run. **NO REGRESSION:** a single-type (speciesCount=1) run shows no regression vs
   today's committed gas golden oracle — verify FIRST-HAND at the tip WHICH committed golden vector covers the gas-only path
   and prove it reproduces byte-identically (the F11 loopback / VoxelField.MeaningChecksum two-endpoint harness is the
   determinism-by-construction tripwire, NOT the committed-golden oracle; and because the loopback goldens are RELATIONAL
   (A==B) they will NOT catch a uniform fold — see #4). Elevate existing artifacts; do NOT rebuild them; do NOT assume a
   test literally named "S0/S1 golden" exists.
3. **3-layer param structure is DATA-DRIVEN** (NOT a C# enum/switch over types). TWO independently-authored controls:
   (a) a POSITIVE RED test registers a NEW data-only type + asserts it behaves (the data path is LIVE + the only path the
   registry exposes); AND (b) a build-SCAN over the NEW near type/registry subtree that FAILS on a switch/enum over TypeId,
   with a planted-violation self-test (the mechanical falsifier for "no hardcode" — precedent: tools/zero-float-scan.ps1
   `$Forbidden` token-scan + `-SelfTest`, wired into check.ps1; folds into the both-scan-roots work in #6; the PLAN picks the
   exact form). The scan covers ONLY the new near per-type path and explicitly does NOT scan the FROZEN far-tier
   `CoarseSpecies` (do NOT refactor or re-data-drive it). "adding a test type touches DATA only" is a reviewer observation,
   NOT the gate — the gate is (a)+(b). Shared PARENT params defined once (no copy). Single-source SEAM reserved: an
   independent check confirms a later look-param field CAN be added to the EXISTING type definition/registry record WITHOUT
   spawning a parallel definition (RED: a type record shaped so look-params cannot attach FAILS); reserve only, no look-param
   built/wired.
4. **Day-one DETERMINISM socket (conditional on the #1 rep decision):** the per-cell dominant-TypeId is a checksum member
   DISTINCT from today's fold (canon §9.5 separates «масса по типу/слою» from «`TypeId` слота»; the checksum today folds only
   per-species mass + a per-face species index). Under the **sparse-dominant** rep: the STORED per-cell dominant TypeId is
   folded into the MeaningChecksum (canon §4 шов 5); RED control: two peers whose cells carry IDENTICAL per-species mass but
   DIFFERENT per-cell dominant-TypeId MUST DIVERGE the checksum (isolate the new member via a MeaningMembers mask — the
   S2bMembershipTests `All & ~TypeId` pattern — so the control cannot pass on the pre-existing mass fold; a silently-absent
   TypeId field that leaves it green = FAIL). Under the **dense `[species][cell]`** rep: type identity is ALREADY positional
   in the per-species mass planes, so NO redundant `argmax(mass)` dominant-id field is added — the PLAN instead RECORDS canon
   §4 шов 5 verbatim as the schema rule («the FIRST slice where any effect reads a single per-cell dominant id MUST fold that
   id THEN, as a schema decision taken now, NEVER a live-node checksum migration»). The TypeId member MUST be ADDITIVELY
   folded (precedent: Bias/ImpulseQueue fold nothing when trivial — a quiet scene stays byte-identical to prior slices), so
   a single default-type run is byte-identical to its pre-slice self. Regenerating/rebaselining the S0/S1 single-type goldens
   to absorb a TypeId change = STOP-escalate. STOP if tempted to fold a redundant argmax(mass) field under dense, or to leave
   the trip-wire unrecorded.
5. **MODDABILITY seam reserved:** the type set = an ORDERED, CONTENT-HASHED, session-FIXED registry; its content-hash exists
   + is reserved as the lockstep session-start handshake hook (Факт-5 no-late-join makes a Start handshake natural).
   **DETERMINISM INVARIANT:** the ordered registry CANONICALLY assigns TypeId→plane/array index, identical on every peer;
   every per-type/per-species checksum fold + iteration runs in canonical TypeId order (NEVER registry-insertion / dict-
   enumeration / file-glob order) — the dense mass fold folds `_mass[s][c]` by POSITION and does NOT fold the index `s` as a
   value, so a differing index assignment or iteration order desyncs under a green-looking fold (canon Факт-1 «закреплённый
   порядок обхода»). RED: (a) a different registry CONTENT → a DIFFERENT hash; (b) two peers building the registry from the
   SAME content in DIFFERENT insertion/glob order MUST converge to the SAME TypeId→index AND the SAME hash, STABLE across
   runs/processes (a non-canonical order, or a trivial object-identity/insertion-order hash passing (a) but failing (b),
   RED-FAILS). Built-in TEST set only; external mod-loading DEFERRED.
6. **DETERMINISM by construction + scan coverage:** integer-only authoritative path; the new per-type code covered by BOTH
   the zero-float + int-overflow scans. NOTE (corrected): both scans ALREADY carry IDENTICAL `$DefaultRoots`
   ({Voxel, Structure, Determinism}, both with `-SelfTest`) — there is no current root-list mismatch. The obligation is
   forward-discipline: IF the per-type/registry code adds a NEW authoritative directory, add it to BOTH root lists (keep them
   identical) + a planted-violation RED self-test for that dir (a float AND an unguarded int*int there must be flagged by
   BOTH scans; the same plant must go UNSCANNED before the root is added); IF it lands under an already-scanned root (e.g.
   Core/Field/Voxel), VERIFY both scans cover the new files — either branch DEMONSTRATED, not asserted. Loopback determinism
   hash green over a multi-type seeded run (planted-float / order-dependence RED controls). Extend the settle/quiescence
   oracle to the MULTI-TYPE path: every test type's field reaches a fixed point (dirty-chunk count drains to 0) within
   bounded ticks; a planted sub-floor / non-settling per-type config MUST FAIL (a perpetually-sloshing-but-byte-identical
   multi-type run that keeps the loopback hash GREEN must be RED here).
7. **check.ps1 -Deliver GREEN** (build + headless + zero-float + int-overflow scans + mutation ≥70 on new Core + spec-silence
   + deliverable-coverage). G0-frozen (openspec + frozen spec + ledger + mutation-<id>.json ≥70; RESULT.md = DELIVERED).
8. **ZERO-LEGACY**; tests rewritten not dragged.
9. **OWNER-EYE (confidence, NOT a gate):** owner sees 2 test gases behave differently in the debug view; owner-run, no
   self-marking.

## discipline / gates (carried)

RED-first by an INDEPENDENT test-author (builder cannot edit the red tests) · Core/** placement · -Deliver GREEN ·
mutation ≥ floor (70%) · a FRESH-SESSION G5 (different model family) refuting the per-type determinism / data-driven-no-
hardcode / TypeId-checksum-distinct-and-additive / registry-canonical-order / single-type-no-regression / multi-type-settle
seams — COULD-NOT-REFUTE is the bar · STOP-discipline (a hardcoded type path, a visual hookup creeping in,
weight/reactions creeping in, a sub-floor Kp, non-canonical registry order, float on the authoritative path, touching the
frozen far-tier CoarseSpecies, reopening ADR-0002 = mandatory STOP + escalate) · build in small steps.

## return

A RESULT routed HOME (the OS owns the next CALL): outcome + evidence (commits, -Deliver transcript, mutation json, G5
verdict, the multi-type loopback hash + RED-control trips, the rep decision + its numeric revisit-trigger, the registry/
handshake seam) + findings for the planner. dev→main merge + push is OWNER-GATED. On GREEN → the road rolls to Sc-weight
(per-type buoyancy — PORT the proven CoarseSpecies weight/heat integer law).

## budget

One slice. If the PLAN finds the param structure + ≥2 differentiated types + the two sockets is too big for one leg, STOP
and return "split needed" (e.g. the data-driven param table + 2 types differing by spread + the TypeId-checksum socket land
first; the moddability registry-hash + canonical-order seam second) — do not silently build a blob. Keep the TEST-types
scope tight (2-3, behaviour/settle-rate-spanning).

END_OF_FILE: live/indie-game-development/work/c-exec-019-call.md
