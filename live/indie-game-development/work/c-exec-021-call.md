# CALL c-exec-021 — Sc-reactions: INTEGER CHEMISTRY BETWEEN WEIGHT-CLASS TYPES (telegraph + bang = shared event, ENGINE-ONLY)

Direction: indie-game-development / g-9c41 / Sc-reactions — the THIRD slice of the CHARACTER ROAD (d-character-road-001,
owner «можем оформлять» 2026-06-29). Builds on the post-Sc-weight base (GasCoopGame `main` at-or-after @61b7923 — the
c-exec-020 Sc-weight merge; §Re-sync confirms HEAD first — small repo-hygiene-only commits atop it are expected).
Executor: a FRESH GasCoopGame_dev session (branch `dev` → `main` when green, owner-gated). Opens with a PLAN (owner
present). State source = NOW.md (active_tasks Sc-reactions). Canon = knowledge/g9c41-gas-engine-SPEC.md (Факт-4 «целочисленная
химия = ДАННЫЕ, не код-ветвление»; §3 «доминирующий тип + количество + временный mix-overlay при реакции» + «Триггер
реакции/детонации читает refinement-инвариантные ГРУБЫЕ тоталы … цепь — следующим тиком»; Ведро-2 «триггер реакции + масса»;
§6 п.5 «согласованность ≠ взаимозависимость»; §9.5/шов 5 + шов 9 «порог взрыва»; §1 ADR poprawка: lock = ADR-0002). Shape
basis = work/character-road-shape-2026-06-29.md (Sc-reactions slice). Folds decision d-coop-interdependence-repin-001 (the
dropped forced-coop affordance — RATIFIED at the PLAN, see done_when #1).
HARDENED 2026-06-30 (wf_86b1f6d0-bda: 12 adversarial lenses → 40 findings → refute-verify + direction adjudication →
must/should-fixes folded. Key catches: the old ReactionLayer is a Wave-2 LOCKED openspec contract not free dead code;
ADR-0020 is already taken on dev2 (→ ADR-0021); the co-op axis was framed as consistency not interdependence; the telegraph
fold needs a distinctness RED; the handshake hash needs a convergence + reactant-set-canonical RED; EmitImpulse is not
atomic/canonical; the shove must stay inside the c-020 settle envelope; the split must fracture along machinery; telegraph
STORED-vs-DERIVED is the PLAN's call. Refuted: a shared buoyancy/_bias register STOP (buoyancy is DERIVED, touches neither
_bias nor EmitImpulse); the next=Sc-damage pointer as a method-leak.)

## ⚠ HELD + RE-SCOPED 2026-06-30 (s-reshape-sparse-dominant-001) — read BEFORE the body below

This CALL was framed + hardened on the PRIOR plan (DENSE `[species][cell]` rep, pairwise, no
dynamic-typing/waves). The owner then LOCKED **sparse-dominant** representation + env-derived dynamic
typing + condition-waves (s-design-gas-core-001), and the road gained a new slice **Sc-rep**
(re-represent dense→sparse-dominant) that runs BEFORE reactions. This CALL is **HELD, NOT trashed**: its
hardening is REUSED as PRINCIPLE. It does NOT fire until the road REACHES reactions (after Sc-rep merges).
Its FULL re-hardening (a fresh workflow) happens THEN — the code-grounding shifts under sparse-dominant.
The body below is the prior-plan text kept for reuse; where it conflicts with this banner, THIS banner wins.

**Re-scope direction (apply at the future reactions shape):**
1. **Base** = post-**Sc-rep** (sparse-dominant), not post-Sc-weight dense.
2. **Reaction schema → AXES** (fuel↔oxidizer, cold↔heat, caustic↔inert, …), NOT type-pairs — a new gas of
   any tier adds ZERO new rules (O(axes)). The no-pair-dispatch crux below still binds.
3. **Partial combine** = reactions fire ONLY at the OVERLAP FRONT (≥2 reactant types co-resident); a per-tick
   cap marches the front inward — instant whole-cloud combine is structurally impossible.
4. **Outcomes = pluggable EVENT KINDS** via an outcome-registry (sorted ids + ContentHash riding the session
   handshake) + registered-handler dispatch, built on the **near VoxelField** — NOT on the old `GridEvent`
   bus and NOT by widening `GridEvent`/replacing the `GridEventKind` if-chain (that IS the Wave-2-LOCKED
   contract the boundaries below forbid touching). The design doc's «replace the GridEventKind if-Kind chain»
   note lands on the near VoxelField under this re-scope, NOT the locked bus. If the owner ever wants the
   locked GridEvent path changed, that is a SURFACED owner-gated live-spec amendment, never a quiet bullet.
5. **Condition-WAVES (fork)**: a reaction MAY emit a PROPAGATING coarse event carrying a condition-tag + a
   per-type response table (gas1,2→gas4; gas3→annihilate; gas5→ignite; gas6→ignore). ⚠ The wave PROPAGATION
   channel is DISTINCT from single-cell outcome dispatch (item 4) and from EmitImpulse — it is a marching
   coarse promo-event other cells READ and respond to. The reactions shape MUST decide which machinery carries
   it and verify FIRST-HAND whether a propagating promo-event substrate exists or must be built (SPEC:
   promo-event machinery is a precondition for any ведро-2 mechanic) AND that it does not re-collide with the
   Wave-2-LOCKED GridEvent contract. So the local-only-vs-wave fork is NOT a free data flag — the wave branch
   carries a possible new-machinery cost.
6. **Dynamic-typing socket**: reactions read the per-cell dominant STAMP (laid by Sc-rep); the typing MECHANISM
   (exposure accumulator/flip) is its own concern — if «accumulate» wins (design fork-1), it adds a NEW per-cell
   replicated field = a NEW cell-keyed SKIP-ZERO MeaningChecksum member (its own bit, NOT the stamp's), a §9.5
   schema decision to take deliberately at the typing slice.
7. **§Re-sync dense→sparse touchpoints (builder MUST re-verify at the tip — do NOT inherit silently):**
   (a) the no-regression golden is now the post-Sc-rep SPARSE golden (the dense path is removed by Sc-rep
   ZERO-LEGACY), not the Sc-weight dense golden; (b) mass-bookkeeping + per-tick checksum — the dense per-plane
   `MaxCellMass` cap / «moves mass between species planes» / «sum across all species planes» reasoning is
   dense-framed; re-express against the sparse cell store (dominant amount + K-bounded overlay), conservation
   oracle = per-cell TOTAL (not per-plane), and a reaction product exceeding K overlay slots is the SAME overflow
   surface Sc-rep decides (LOUD THROW / declared policy); (c) handshake-hash — DROP the «per dense index»
   phrasing (the handshake folds REGISTRY/rule-set identity, not the field — the fold mechanism survives, but the
   dense-layout wording must not be inferred from it).
8. **Forks** (flip-vs-accumulate, consume-vs-residue, wave gameplay-vs-cosmetic, regime-vs-identity, target
   weak-hardware) resolve at THIS CALL's future shape, owner present.
9. **ADR**: the prior «ADR-0021» assumption is STALE — Sc-rep takes ADR-0021 ahead of this CALL; c-021 takes the
   next free engine number at its time (≈ADR-0022, verify mechanically: `git ls-tree -r --name-only dev2 --
   docs/adr` + main docs/adr; record chosen + siblings).
10. **All existing hardening below is PRESERVED as PRINCIPLE** (no-pair-dispatch crux, handshake-hash
    order-independence, per-tick checksum SKIP-ZERO cell-keyed, mass integer-exact/no-silent-wrap/atomic,
    ZERO-LEGACY ReactionLayer-LOCKED, co-op interdependence, the gate battery) — re-grounded onto sparse-dominant
    at the future re-hardening, NOT carried forward with dense assumptions.

**⚠ BANNER CORRECTIONS (2026-07-02, s-repair-review-reconcile-001 — the review found the banner itself drifted;
these win over the items above where they conflict):**

11. **ADR (corrects item 9):** the product repo adopted TRACK-NAMESPACED ADRs (ADR-P-0001, owner-approved 2026-06-30;
    flat numbers frozen; Sc-rep took **ADR-E-0001**). «ADR-0021 / ≈ADR-0022» will never exist. Standing rule: OS-side
    docs do NOT pre-assign concrete ADR numbers — the executor binds the next free **ADR-E-*** number at the tip per
    ADR-P-0001 and records it in the RESULT.
12. **Base (corrects items 1/2 + the «THIRD slice» header):** Sc-rep is BUILT (dev checkpoint adc3b9d, pending fresh
    G5 / owner-eye / owner-gated merge), and the 2026-07-02 REAL hangar measurement (dev @8db3ee1,
    docs/measurements/sc-rep-hangar-real-measurement-2026-07-02.md) showed tick cost ∝ REGISTERED roster × domain
    cells (dense expand/rebuild kernel; roster-64 hangar = 587 ms/tick) → slice **Sc-kernel** (active-front tick
    iteration; d-sparse-tick-kernel-001, pending owner sign; draft work/c-exec-023-draft-call.md) is recommended
    BEFORE this CALL. If approved, this CALL's base = post-Sc-kernel.
13. **NEW NAMED FORK for this CALL's shape — co-residency/overflow under mixing:** K=3 overlay (max 4 co-resident
    types per cell) with >K = LOUD THROW is wired into the NORMAL tick path — under lockstep that is a deterministic
    ALL-PEER session halt reachable by ordinary gameplay mixing (5 types meeting at a junction), in a game whose core
    fantasy is mixing. Item 7(b)'s «the SAME overflow surface Sc-rep decides» is a CIRCULAR pointer (Sc-rep's CALL
    deferred the policy back to reactions design) — the buck stops at THIS shape. The shape MUST decide, owner present:
    (a) the representation-level policy for NON-reacting >4-type mixes (canonical merge-to-nearest-axis / raised K /
    owner-signed declared sink), and (b) an adversarial RED: a 5-type junction scenario proving the throw is
    unreachable in the intended level + chemistry design. Until then, any level/chemistry permitting 5+ types in one
    zone is ship-blocking.
14. **Stale body specifics confirmed at review (do NOT inherit):** the checksum-bit math «1<<6 / current max TypeId
    1<<5» predates Sc-rep's stamp+overlay checksum members (bits shifted — verify MeaningMembers at the tip); the
    engineering contract is **v9** (body says v8); body line-refs are pre-Sc-rep. The re-hardening's FIRST step = a
    recorded line-by-line drift-sweep of every number/ref in the body against the then-tip — or better, REWRITE the
    body at the shape instead of stacking a third banner generation.

## Why this slice (and the lock id)

Sc-types laid the multi-gas substrate (dense `[species][cell]` planes, a canonical content-hashed registry, per-cell type
identity in the checksum); Sc-weight wired the FIRST per-type vertical FEEL. Sc-reactions is the FIRST slice where ≥2 gas
types INTERACT: when reactant types co-reside, the gas TELEGRAPHS then BANGS — a deterministic integer chemistry that both
peers compute identically and whose consequence reaches a SECOND occupant (the forced-coop affordance,
d-coop-interdependence-repin-001). This is the FIRST slice whose behaviour DIVERGES on a PAIR (or set) of type identities —
so it is the textbook hardcode-dispatch / N²-table trap, and the §3 «trigger reads coarse totals, chain next tick»
determinism crux. Lock = **ADR-0002** (input-lockstep; §1 drift-guard: any stray «ADR-0010-as-lock» is a citation error —
ADR-0010 = the unrelated test-sandbox). Determinism preserved, not reopened.

## goal (outcome, not method)

Near-tier gas acquires INTEGER CHEMISTRY: when ≥2 reactant gas types co-reside in a cell at/above a DATA-defined threshold,
the cell TELEGRAPHS (a visible WARNING phase), then BANGS — the reactant masses transform (integer, DATA-defined) into a
product (a product gas type AND/OR a coarse pressure event that shoves the surrounding gas), as a SHARED consequence both
lockstep peers compute identically and which reaches beyond the reactant cell (what a second occupant would feel). A reaction
is pure DATA: **a new gas type adds ZERO new code branches** (no per-type-pair `if`/`switch`, no N² code table) — reactions
are DATA rules applied by a GENERIC engine. The owner SEES, in the engine debug view, two reactant test gases meet, telegraph
(warn), then react (a visible bang / product appears), deterministically. **ENGINE-ONLY — no visual-track hookup** (the look
connects later; the g-7e15 visual track runs independently on dev2).

**approach token = `data-driven-reaction-rules-telegraph-then-bang`** — the ONE substrate this leg exists to prove: an
integer, content-hashed, GENERICALLY-applied reaction rule-set (NOT a per-type-pair code path), with a telegraph→bang that
chains one step per tick. A delivered artifact whose recorded `approach:` differs (esp. an enum/switch/dict/2D-array/if-chain
dispatch on type-pairs, or a same-tick unbounded cascade) is a self-authored substitution needing owner-ack — otherwise
STOP-escalate.

## the model (frame the OUTCOME; the PLAN owns the realization)

The reaction resolves as a deterministic GATHER-THEN-APPLY pass: read tick-start per-cell masses, compute ALL reactions,
apply atomically — so the outcome is order-independent within a tick (never a mid-tick mutated value, never a sub-cell fine
detail). **WHETHER this is a separate operator run alongside `VoxelFaceFlow.Step` OR folded INTO the existing flow tick** (as
Sc-weight folded per-type buoyancy into `VoxelFaceFlow.Step`'s per-species loop, c-020) **is the PLAN's call.** IF the PLAN
makes reaction a separable phase, the flow↔reaction order within a tick is determinism-relevant and MUST be fixed and
identical on both peers (record it). Four OUTCOME properties the PLAN must honour:

1. **DATA-DRIVEN rule-set, applied generically (the heart — see «the N² / no-pair-dispatch crux»).** A reaction is a DATA
   rule whose load-bearing fields are (illustratively, for the explicit-rule schema) its reactant type-SET + threshold +
   telegraph delay + product/effect + consumption/production stoichiometry. The engine applies rules by a GENERIC canonical
   lookup; authoring a new reaction OR a new gas type touches DATA only. **Whether the schema is explicit reactant-set rules
   OR per-type reagent-class axes combined by a fixed function is the PLAN's call** — both are «data, not branches»; what the
   CALL mandates is the data-driven + zero-type-pair-control-flow PROPERTY, not the exact schema or its field list.
2. **TELEGRAPH then BANG (chains one step per tick — the §3 determinism crux).** Detection reads the AUTHORITATIVE tick-start
   per-cell mass (gather-then-apply — never a mid-tick mutated value, never a sub-cell fine detail). A detected reaction
   TELEGRAPHS (a visible WARNING phase), and only resolves (BANGS) after the DATA-defined delay. A CHAIN reaction therefore
   advances ONE step per tick — there is NEVER an unbounded same-tick cascade (canon §3 «цепь — следующим тиком»: a same-tick
   cascade is order-dependent → desync, and a gameplay-pop). **Whether the telegraph is STORED per-cell state (a countdown)
   OR DERIVED each tick** (e.g. the warning IS the rising co-resident mass, the bang = crossing a higher threshold, no stored
   timer) **is the PLAN's call — it states which** (this is the main appetite-relief lever; see «the per-tick MeaningChecksum
   decision»). The telegraph is also the player-feel: the gas WARNS before it bangs.
3. **The BANG is a shared, in-checksum COARSE EVENT (ведро-2 — the co-op affordance).** The bang's hard consequences (mass
   transform + any outward pressure shove) are computed from the AUTHORITATIVE shared field on EVERY peer and ride the
   checksum — zero new network traffic (canon Факт-3 «жёсткие общие последствия ПРОМОУТЯТСЯ в грубые СОБЫТИЯ»). One natural
   realization computes a pressure shove and reuses the S1 impulse machinery (`VoxelField.EmitImpulse`/`VoxelImpulse`,
   VoxelField.cs:181-207) — but the PLAN owns whether the bang shoves, produces a product type, or both. ⚠ IF the shove rides
   `EmitImpulse`, two real constraints (see §the per-tick MeaningChecksum decision): (a) `EmitImpulse` is NOT part of the
   atomic `Step` — it mutates `_impulses` immediately (VoxelField.cs:206) and THROWS on a sealed/void/out-of-range face
   (VoxelField.cs:194-197), so a per-cell shove loop must emit in a CANONICAL field-derived order, computed from the tick-start
   field, validated-all-before-any-mutation (preserving the «thrown reaction tick leaves the field byte-unchanged» atomicity);
   and (b) the drained S1 bias is COMBINED into `desiredMove` alongside the gradient AND the c-020 buoyancy term in the same
   per-species loop (VoxelFaceFlow.cs:184-207), so an over-strength shove on Z-faces stacks past the c-020 settle envelope
   (which was derived for the buoyancy term alone) — the PLAN MUST bound the emitted Strength/Ttl so the COMBINED desiredMove
   (gradient + buoyancy + shove) still reaches rest (reuse the c-020 over-strength settle RED: a planted over-strength shove
   that sloshes forever while loopback-green MUST be RED).

Do NOT prescribe the exact integer rule form — that is the PLAN's call — but it MUST be: integer-only, deterministic
(canonical cell order, gather-then-apply for BOTH detection AND resolution/apply), conservative-or-DATA-declared (see «mass
bookkeeping»), chains one-tick-per-step, and data-driven (zero type-pair control flow).

## the N² / no-pair-dispatch crux (the central obligation — read this twice)

Sc-reactions is the FIRST slice whose behaviour diverges on a PAIR/SET of type identities. The temptation is a hardcoded
dispatch: an `if`/`&&`/`==`-chain over a type-pair (`if (a==FIRE && b==FUEL)` / `if(a==X){if(b==Y)…}`), a `switch ((a,b))`, a
`Dictionary<(int,int),Rule>` of DELEGATES, OR a **const 2D array indexed by (typeIdA, typeIdB)** (the N²-code table — the EXACT
shape canon Факт-4 forbids: «как ДАННЫЕ, не как код-ветвление … новый тип = 0 новых веток»). The existing
`tools/type-hardcode-scan.ps1` (contract v8) catches only `enum`/`switch` TOKENS and ONLY in `Core/Field/Types` (its
`$DefaultRoots`, line 44) — it will NOT see reaction code that lands elsewhere (`Core/Field/Voxel` or a new
`Core/Field/Reactions`), and an `if`-chain, a `Dictionary<(int,int),…>`, or a `[,]` indexed by TypeId is NOT an enum/switch
token, so it escapes the scan ENTIRELY (its self-test even WHITELISTS a plain `if`, line 141). The PLAN picks ONE (a silent
reliance on the old scan = STOP):
- **(a) PREFERRED — pure data-rule application, no type-pair dispatch:** the reaction rule-SET is DATA (its hash rides the
  session-start handshake — see «the handshake hash»); the engine applies it by a GENERIC canonical lookup (e.g. a data-built
  rule index keyed by a canonically-ordered reactant key), with ZERO type-identity control flow AND no rule-logic keyed by a
  hardcoded TypeId pair. Adding a reaction or a type is DATA only — no code change. THEN correct the type-hardcode scan's
  scope + «strongest guarantee» header to honestly cover the reaction path's ACTUAL location (mirroring the c-020 honesty note
  that records the Voxel buoyancy path as data-arithmetic covered by the zero-float/int-overflow scans + data-driven RED
  tests). **Option (a) is PREFERRED precisely because it sidesteps the token-scan limitation below entirely.**
- **(b) broaden the scan by SYMBOL:** extend type-hardcode-scan to catch reaction-dispatch — a `switch` over a type-pair, a
  `Dictionary<(int,int|ValueTuple),…>` of delegates keyed by a TypeId pair, a `[,]`/jagged array indexed by TypeId, AND an
  `if`/`&&`/`==`-chain comparing a TypeId pair — each with a planted-violation self-test (mirroring the existing
  `mustFlag`/`mustPass` cases, lines 131-149). ⚠ Two false-positive sources, not one: (i) a naive DIRECTORY-append of
  `Core/Field/Voxel` false-positives the geometry `switch (face)` in VoxelFaces.cs:23,40 and the `[Flags] enum MeaningMembers`
  (MeaningMembers.cs:18); (ii) because the scan is a pure regex TOKEN matcher with NO semantic model, it CANNOT tell a
  `(int,int)`/ValueTuple key that is a TypeId pair from one that is a `(cell,face)` pair — the codebase already uses
  `HashSet<(int,int)>` for `(cell,face)` (VoxelField.cs:190). So a shape-only `(int,int)`-dict / `[,]`-array rule either
  false-positives legitimate tuples or misses the real dispatch. An option-(b) scan must therefore rest on a NAMING/whitelist
  convention (e.g. the reaction rule-index lives in a single NAMED symbol the scan asserts is data-built; all other
  `(int,int)` tuples go in the self-test's `mustPass`), and the per-pattern planted-violation self-test is where that
  disambiguation is PROVEN, not assumed. Do NOT mandate the detection mechanism — the PLAN owns it.
The PRIMARY mechanical falsifier (the GATE, not a reviewer note) is the NEW-TYPE-IS-DATA RED in done_when #2: an independent
test ADDS a NEW reaction rule + a NEW reactant type as DATA ONLY and asserts the reaction fires (you'd have to edit CODE to
add a row to a code-keyed table — so this catches a hardcode the token scan cannot). The scan is the bounded SECONDARY
tripwire.

## the handshake hash (the lockstep session-start determinism gate — DO NOT skip)

The reaction rule-set is determinism-LOAD-BEARING session content, exactly like the per-type weight override Sc-weight added.
Today the lockstep session-start handshake compares `GasTypeRegistry.ContentHash` (GasTypeRegistry.cs:64), which folds the
parent params + count + per-index `(TypeId, MetaTypeId, EffectiveKp, EffectiveWeight)` (GasTypeRegistry.cs:163-178; NB the
public `ContentHash()` SUMMARY docstrings at cs:61-64/155-156 are STALE — they still omit `EffectiveWeight`; fold by the
ACTUAL method body, and refresh those docstrings when you add the reaction fold) — there is NO reaction data. So two
registries IDENTICAL in types but differing in their REACTION RULES yield an IDENTICAL handshake hash AND an IDENTICAL
`MeaningMembers.TypeId` fold (VoxelField.cs:379-389) — a matching handshake while reaction physics diverges → a silent
cross-peer / cross-mod desync under a GREEN checksum (canon Факт-1 / §9.5 «чексумм ЗЕЛЁНЫЙ, физика мусор»; Факт-5 no-late-join
early-rejection defeated). **OBLIGATION (a determinism PROPERTY, not a placement):** the reaction rule-set's hash MUST ride
the SAME content-hash both peers compare at the session-start handshake — **WHERE it lives (absorbed into the registry's
`ComputeContentHash`, or a sibling `ReactionRuleSet` object whose own hash is combined into the handshake hash) is the PLAN's
call.** It MUST be combined CANONICALLY / order-independently, MATCHING ITS SCHEMA:
- for explicit reactant-set RULES: fold a stable-key-sorted rule LIST, **each rule's reactant SET itself canonicalized** (its
  reactant TypeIds sorted) so a rule authored `[A,B]` folds IDENTICALLY to `[B,A]` — TWO levels (canonical reactant key per
  rule, then a stable cross-rule sort); a single rule-sort is NOT enough (a rule's identity is a set, not a scalar). Fold the
  rule COUNT before the loop (the `ordered.Length` length-guard precedent, GasTypeRegistry.cs:169) so a prefix/short set
  cannot collide. Fold EVERY load-bearing field (reactant-set, threshold, telegraph delay, product TypeId, stoichiometry) —
  the «fold every per-index field» discipline (GasTypeRegistry.cs:170-176).
- for per-type reagent-class AXES: fold the resolved axes per dense index INSIDE the existing canonical-TypeId loop, exactly
  as `EffectiveWeight` is folded (GasTypeRegistry.cs:175) — order-independent for free via the existing TypeId sort.
RED controls (BOTH halves — a divergence-only test is satisfied by a non-canonical fold whenever both test registries happen
to author in the same order): (1) DIVERGENCE — two registries differing in ANY load-bearing field, **most importantly WHICH
type-set reacts** (`{A,B}` vs `{A,C}`), and also product/threshold/delay/stoichiometry, MUST DIVERGE the handshake hash; (2)
CONVERGENCE — two registries built from the SAME reaction content authored in a DIFFERENT order (rules permuted; AND, IF the
schema carries multi-reactant tuples, the reactant order within a rule permuted) MUST yield the IDENTICAL hash (a fold that
DIVERGES on a pure re-ordering is non-canonical = FAIL; mirrors the committed `…SameContent_DifferentInsertionOrder_SameHash`
tests). A rule's product/reactant TypeId MUST reference a REGISTERED type — an unknown TypeId is a LOUD build error, NEVER a
silent skip (mirror the «unknown MetaTypeId» loud-throw, GasTypeRegistry.cs:135-137).

## the per-tick MeaningChecksum decision (trip-wire — the PLAN decides, but states which)

ORTHOGONAL to the handshake hash (that is the registry-identity handshake; this is the per-tick field-state digest). Mirror
the c-020 DERIVED-vs-STORED shape:
- **TELEGRAPH state — DERIVED (recommended where possible, the appetite-relief path):** if the telegraph is a pure per-tick
  function of co-residence + a deterministic phase (e.g. the warning IS the rising co-resident mass, recomputed each tick,
  never stored as field state), it adds NO new per-tick member — the mass it reads already folds under `Mass`. The PLAN
  RECORDS this.
- **TELEGRAPH state — STORED → a NEW member.** If a pending-reaction countdown is stored per-tick field state the next tick
  reads, it MUST become a NEW `MeaningMembers` member at the next free bit **`1 << 6`** (current max `TypeId = 1 << 5`,
  MeaningMembers.cs:36), folded ADDITIVELY via the **SKIP-ZERO precedent** (a cell with no pending reaction folds NOTHING — a
  no-reaction scene stays BYTE-IDENTICAL to the Sc-weight goldens, like `Bias`/`ImpulseQueue` fold nothing when empty,
  VoxelField.cs:334-371). **Fold each pending reaction KEYED BY ITS CELL's canonical X,Y,Z coordinate** (mirror the Bias fold,
  VoxelField.cs:341-345) — NOT merely a countdown value or a queue sorted on countdown alone: two fields IDENTICAL in mass but
  with telegraphs on DIFFERENT cells (or different countdowns on the same cells) MUST DIVERGE the checksum (the §9.5/шов-5
  trip-wire — a non-cell-keyed fold is a UNIFORM bug both peers build identically, loopback-green, yet two distinct layouts
  alias). TWO RED controls: (i) ISOLATION — `All & ~<member>` fails parity when the member is non-trivial (proves it is
  folded); (ii) DISTINCTNESS — two distinct telegraph layouts (different cells / values, same mass) MUST DIVERGE (proves the
  fold is cell-keyed / collision-free). Do NOT reuse `ImpulseQueue` (1<<4) or `Bias` (1<<3) for telegraph state — a distinct
  concept gets a distinct bit.
- **Mass transform** folds under the existing `Mass` (1<<0); **a shove via `EmitImpulse`** rides the existing `ImpulseQueue`
  (1<<4), emitted deterministically from the shared field, in canonical field-derived order, validate-all-atomic (see §the
  model property 3).
Regenerating/rebaselining the Sc-types/Sc-weight goldens to absorb a reaction change = STOP-escalate.

## mass bookkeeping (integer-exact, no silent wrap)

A reaction TRANSFORMS mass (chemistry — unlike flow, a reaction may legitimately change a cell's total mass by its DATA-defined
stoichiometry, and MOVES mass BETWEEN species planes). It MUST be: integer-only (no float — zero-float scan); each reactant
consumption + product production validated and on out-of-range **THROW loudly, ATOMIC** (field byte-unchanged, mirroring the
real precedent `VoxelFaceFlow.cs:252-253` / `SeedMass` cs:121-122 — both THROW, neither saturates), NEVER a silent
two's-complement wrap (canon «Детерминизм — как гарантируется»: «wrap бит-идентичен на всех пирах → чексумм ЗЕЛЁНЫЙ, физика
мусор»). ⚠ `VoxelField.MaxCellMass` (cs:19) is a PER-PLANE per-`(species,cell)` cap (checked per plane in `SeedMass`,
cs:118-122) — so even a reaction the PLAN declares mass-CONSERVATIVE can push a single PRODUCT plane over `MaxCellMass` while
the cell total is conserved; such an out-of-range product MUST THROW, never saturate-and-drop (how the PLAN keeps a product
under the per-plane cap — re-balance, reject the reaction, or a DATA-declared cap policy — is the PLAN's call). The PLAN
DECIDES + RECORDS whether a reaction CONSERVES total mass or is a DATA-declared net source/sink — but a NET MASS LOSS that is
not an explicit DATA-declared sink is a leak = STOP (GAP-2 void/sink is reserved, not active — canon §4; do NOT route reaction
loss through it silently). No `int*int` on the authoritative path without a long guard (int-overflow scan).

## the mix-overlay / «blended cell» resolution (sparse-dominant — the cell IS the blended cell) — RE-SCOPED 2026-06-30

Under the LOCKED sparse-dominant representation (Sc-rep), a cell natively carries {dominant type + amount + a small bounded
mix-overlay}, so a «blended/mixed cell» IS the native representation — the reaction reads the dominant + the co-resident
overlay slots directly, and canon §3 / Факт-4's «mix-overlay» is the cell's own overlay (no separate structure). **STOP =
reverting to dense `[species][cell]` planes** (the prior plan's rep — removed by Sc-rep ZERO-LEGACY). The old dense-rep claims
that stood here («dense `[species][cell]` is the canon-sanctioned shape»; «§3 разреженная доминантная … НЕ плотные страницы is
SUPERSEDED by the delegation»; «STOP = inventing a PARALLEL species-mix REPRESENTATION beside the dense planes») are DELETED —
they pointed the wrong way once representation resolved to sparse-dominant (SPEC Факт-4, s-reshape-sparse-dominant-001; the
SPEC.md Факт-4 honesty-note citation the old STOP rested on is itself now superseded). The PLAN re-grounds the mass/overflow
handling onto the sparse cell store (per the §Re-sync touchpoints in the RE-SCOPE banner): conservation oracle = per-cell total,
a product exceeding K overlay slots = the Sc-rep overflow surface (LOUD THROW / declared policy), NOT a dense per-plane cap.

## ZERO-LEGACY: the old ReactionLayer is a LOCKED contract (do NOT revive, do NOT free-delete)

The OLD `Core/Field/Layers/ReactionLayer.cs` (+ `TemperatureLayer.cs`, the v1 `Layers/` ILayer demo) is a publish-only
producer in the dead `Layers/` ILayer demo tier — uncomposed in production (nothing wires `ReactionLayer` in a real
composition root). BUT it is NOT free-to-delete dead code: `GridEventKind.Reaction (=3)`, the publish-only `ReactionLayer`,
and `ReactionHeat (=32)` are a **Wave-2 LOCKED openspec contract** — `openspec/specs/sim-core/spec.md:153-172` carries an
ACTIVE SHALL («`GridEventKind.Reaction` (=3) SHALL be published by a publish-only `ReactionLayer` … `TemperatureLayer` SHALL
gain ONE additive P2 branch heating by a frozen `ReactionHeat=32`») AND declares the cross-layer event contract LOCKED /
immutable for Wave 2 (verdict=HOLD fired). `check.ps1`'s spec-silence audit only checks the NEW change's frozen-spec section,
NOT source-vs-existing-spec — so a delete would leave EVERY mechanical gate GREEN while silently violating a locked SHALL.
**DEFAULT disposition = an explicit recorded CUT + a pin** (out of appetite; matches the c-020 frozen-tier discipline «do NOT
touch … retire later»; the orphaned producer is left intact). DELETE is available ONLY after the builder verifies FIRST-HAND
at the tip that NO live `openspec/specs/**/spec.md` SHALL references `ReactionLayer` / `GridEventKind.Reaction` / `ReactionHeat`
(it currently DOES) AND an owner-gated live-spec amendment lands first. **Do NOT revive or extend `ReactionLayer` /
`GridEventKind.Reaction` / the old `GridEvent` bus** — build reactions on the near `VoxelField`; the bang's pressure shove (if
any) reuses the S1 `EmitImpulse` path, NOT the old GridEvent bus. (Terminology: this is the dead `Layers/` ILayer demo tier —
distinct from the far-tier room-graph ROLLUP in `Core/Field/Coarse`, which is canon's chosen far model, DEFERRED not retired.)

## co-op interdependence (d-coop-interdependence-repin-001 — RATIFIED at the PLAN, framed HERE)

The signed forced-coop rule (shared gas must force teamwork) lost its engine node (audit THEME-3); its recommended home is
THIS PLAN + Sc-damage. d-coop-interdependence-repin-001 is still an OPEN decision in NOW.md (options + recommendation, not
ratified) — so the PLAN, owner present, RATIFIES the fold-into-this-PLAN home (vs the separate-node / defer options) BEFORE the
co-op axis is treated as binding (done_when #1). Canon §6 п.5 is explicit: the engine is co-op-NEUTRAL, and
«согласованность ≠ взаимозависимость» — byte-identical-on-both-endpoints is CONSISTENCY (already guaranteed by the determinism
gates), NOT interdependence; the feel/design half is the canon track g-d3a8, not the engine. So the engine axis this slice can
prove is the PRECONDITION for interdependence: **the bang's consequence reaches a cell the reactants did NOT occupy** (a
non-local shared consequence — canon's «ОБЩЕЕ-последствие-которое-чувствует-второй-игрок»). Add this as a
**REQUIRED-to-CHECK owner-eye axis (confidence, not a delivery gate — like the rest of #10)**. HONESTY: engine-only / loopback,
no real 2nd player — this proves only the engine precondition (a non-local shared consequence); the full 2-player feel lands
when networked gas does (~S4) + the gameplay payoff at Sc-damage.

## boundaries (out of scope / STOP-escalate if tempted)

- **NO type-pair hardcode dispatch** — an `if`/`&&`/`==`-chain over a type-pair, an enum/switch over a pair, a dict-of-delegates
  keyed by a TypeId pair, a const 2D array indexed by `(typeId,typeId)` — reactions are DATA rules applied generically; a new
  type = 0 new code branches = STOP.
- **NO same-tick unbounded cascade** — a chain advances ONE step per tick (telegraph→bang); a same-tick recursive cascade is
  order-dependent = desync = STOP (canon §3 «цепь — следующим тиком»).
- **NO temperature / heat mechanic, NO damage** — temperature appears nowhere this slice. ⚠ The natural trap: an EXOTHERMIC
  reaction that writes a temperature/heat field — that is Sc-damage's thin sink-layer (d-tempfeedback-001) = STOP. A reaction
  product is a gas TYPE and/or a pressure EVENT, never a heat field.
- **NO visual-track hookup** (engine-only); do NOT touch the dev2 visual track or its reserved fields.
- **Do NOT revive/extend the old `ReactionLayer` / `GridEventKind.Reaction` / the dead `Layers/` ILayer demo tier; do NOT
  delete the Wave-2-LOCKED cross-layer event contract** (`GridEventKind.Reaction=3`, `ReactionLayer`, `ReactionHeat=32`, per
  openspec/specs/sim-core/spec.md:153-172) without an owner-gated live-spec amendment = STOP (see ZERO-LEGACY).
- **Do NOT touch / refactor / re-data-drive / move / scan the FROZEN far-tier** `CoarseSpecies` / `CoarseBandStep`
  (Core/Field/Coarse) — it retires at S4; the type-hardcode scan must still NOT scan it.
- **NO stored velocity / advection / true inertia / coasting** (TIER-3 / cracks the lock — d-gas-richness-tiers-001) — the
  bang shove is a bounded BIAS impulse (S1 register, inside the c-020 settle envelope), not a velocity field.
- **NO silent mass leak** — a net-mass-reducing reaction must be a DATA-declared sink, not a quiet drop (no silent GAP-2).
- **NO float on the authoritative path / re-flux-as-gate**; integer-only; laws in headless Core/**. Lock = ADR-0002, NOT
  reopened. The new engine ADR number is taken from the lowest number FREE across BOTH `main` docs/adr AND the `dev2` visual
  track — NB **dev2 already holds `ADR-0020-gas-visual-w1a`, and engine ADRs run to 0019 (Sc-weight), so the next free engine
  number is ADR-0021** (verify mechanically: `git ls-tree -r --name-only dev2 -- docs/adr`; OR, if a same-number double-book
  is unavoidable mid-track, copy ADR-0019's collision-header convention verbatim — state the cross-track double-book +
  «renumber at the dev/dev2→main merge»). Record the chosen number + the sibling numbers checked in the RESULT.
- **Forward-discipline (note, do NOT scope in now):** when the detail bubble lands later, the reaction trigger reads the
  COARSE authoritative total, never the bubble (canon §3 несущие — «подход игрока сам детонирует облако» is the desync). This
  slice has no bubble; just do not architect the trigger to depend on sub-cell fine detail.

## ведро classification (PLAN reconfirms — already decided)

- **Ведро-2** (coarse-promotable, IN-checksum, shared by all peers): the reaction trigger + the bang's mass-transform + any
  pressure event are authoritative laws on the shared 50cm grid — they ride the mass + the (derived-or-stored) telegraph state
  + the rule-set every peer agrees on, and are the co-op affordance.
- **Ведро-1** (off-checksum local detail): ABSENT this slice. **Ведро-3** (sub-room AND shared): ABSENT.
The PLAN reconfirms this disposition; it does not re-derive it.

## done_when (verifiable)

1. **PLAN (owner present):** §Re-sync FIRST; ingest canon Факт-4 (data-not-branches) + §3 (telegraph/chain/coarse-event,
   mix-overlay) + §6 п.5 (consistency≠interdependence) + §9.5/шов 5 + d-character-road-001 + d-coop-interdependence-repin-001;
   **RATIFY (owner present) d-coop-interdependence-repin-001's fold-into-this-PLAN home** (vs the separate-node / defer options)
   before treating the co-op axis as binding; DECIDE and RECORD: (i) the reaction rule SCHEMA (explicit reactant-set rules vs
   per-type reagent-class axes) + (if reaction is a separable phase) the fixed flow↔reaction tick ORDER; (ii) the telegraph
   delay + telegraph STORED-vs-DERIVED + whether the bang shoves / produces a product / both; (iii) the per-tick
   MeaningChecksum decision (DERIVED → no member + recorded rationale, or STORED → a NEW `1<<6` SKIP-ZERO cell-keyed telegraph
   member) + how the reaction rule-set rides the session handshake hash (registry-absorbed vs sibling-combined); (iv) the
   no-pair-dispatch fix (option a pure data-rules + scan-honesty, or option b broaden-the-scan-by-symbol); (v) the mass policy
   (conserve vs DATA-declared sink/source) + the «blended cell = dense co-residence, no parallel overlay» record; (vi) the
   disposition of the orphaned `Layers/` demo (DEFAULT recorded-cut+pin; delete only after a live-spec check + owner-gated
   amendment); (vii) the new ADR number (lowest free across main + dev2; ADR-0021 likely). Reconfirm ведро (ведро-2 only);
   name the 2-3 reactant TEST types + ≥1 product (reuse/extend the Sc-types test set; weight-class-spanning).
2. **≥2 reactant types REACT, data-driven** — independent-author RED: over a seeded run, two reactant types co-resident above
   threshold telegraph then BANG (the product appears / the shove fires); a single-reactant or below-threshold run does NOT
   react. **NEW-TYPE-IS-DATA (the primary no-pair-dispatch falsifier):** an independently-authored RED registers a NEW
   reaction rule + a NEW reactant type as DATA ONLY (no code edit) and asserts the reaction fires. **NO REGRESSION:** a
   no-reaction run reproduces the committed pre-slice gas golden BYTE-IDENTICALLY (this golden already CONTAINS Sc-weight
   buoyancy creep — verify FIRST-HAND at the tip WHICH committed golden covers the gas path); the loopback two-endpoint
   `MeaningChecksum` harness is the determinism tripwire, NOT the golden, and being relational (A==B) it will NOT catch a
   uniform fold (see #5/#6).
3. **NO-PAIR-DISPATCH (the N² obligation):** reaction logic has ZERO type-identity control flow keyed by a type-pair — no
   `if`/`&&`/`==`-chain over a pair, no enum/switch over a pair, no `Dictionary<(int,int),…>` of delegates, no `[,]`/jagged
   array indexed by a TypeId pair; the mechanical falsifier (option a: pure data-rule application + the type-hardcode scan's
   scope/header corrected to honestly cover the reaction path's location; OR option b: the scan broadened BY SYMBOL/naming with
   a planted-violation self-test for EACH dispatch pattern incl. the if-chain — NOT a blind directory-append, and resting on a
   naming/whitelist convention because a token scan cannot semantically distinguish a TypeId-pair tuple from a `(cell,face)`
   tuple) covers the reaction code's ACTUAL location. The FROZEN far-tier `CoarseSpecies` stays unscanned + untouched.
4. **TELEGRAPH→BANG, chain one-tick-per-step — TWO named falsifiers:** (i) a TICK-COUNT oracle — a chain of depth N (N cells
   that would each trigger the next) resolves over EXACTLY N ticks, so a depth-2 chain that fully resolves in 1 tick MUST FAIL
   (this is the relational-invisible falsifier the loopback hash cannot provide — a canonically-ordered same-tick cascade is
   loopback-green AND permutation-stable); (ii) an ORDER-PERMUTATION control over BOTH detection AND resolution/apply —
   detection + the multi-cell reaction-apply (reactant consumption + product production) compute entirely from tick-start
   masses, so permuting the order in which simultaneously-banging cells are resolved yields a BYTE-IDENTICAL field; a planted
   read-/apply-against-mutated-mass realization MUST FAIL.
5. **HANDSHAKE-HASH socket (conditional on #1):** the reaction rule-set's hash rides the session handshake hash canonically —
   (a) DIVERGENCE RED: two registries differing in ANY load-bearing field, most importantly WHICH type-set reacts (`{A,B}` vs
   `{A,C}`), also product/threshold/delay/stoichiometry, DIVERGE the hash; (b) CONVERGENCE RED: the SAME reaction content in a
   DIFFERENT authoring order (rules permuted; reactant order within a rule permuted, schema-permitting) yields the IDENTICAL
   hash (a fold that diverges on pure re-ordering = FAIL); an unknown reactant/product TypeId is a LOUD build error; the rule
   count is folded (length guard).
6. **PER-TICK CHECKSUM socket (conditional on #1):** telegraph DERIVED → no member (recorded); STORED → a NEW `1<<6`
   `MeaningMembers` member, ADDITIVELY (SKIP-ZERO) folded KEYED BY canonical cell coordinate, with TWO RED controls —
   ISOLATION (`All & ~<member>`) AND DISTINCTNESS (two telegraph layouts identical in mass but on different cells / values
   DIVERGE). The mass transform folds under `Mass`; a shove via `EmitImpulse` rides `ImpulseQueue`, emitted deterministically
   from the tick-start shared field in canonical field-derived order, validated-all-before-mutation (atomic), and bounded so
   the COMBINED desiredMove (gradient+buoyancy+shove) still settles (the c-020 over-strength settle RED applies). The S1
   `_bias`/`ImpulseQueue` is NOT repurposed for telegraph state.
7. **MASS bookkeeping:** integer-exact; reactant consumption + product production THROW loudly on out-of-range / per-plane
   `MaxCellMass` overflow (no silent wrap, no saturate-and-drop), atomic (a thrown reaction tick leaves the field
   byte-unchanged); the mass policy (conserve / DATA-declared sink) RECORDED; the conservation RED control checks the
   CELL-TOTAL mass summed ACROSS ALL species planes — conserved EXACTLY for a declared-conservative reaction, or changed by
   EXACTLY the data-declared net amount for a declared sink/source — NOT a per-species exactness (a reaction legitimately moves
   mass between planes; this DIFFERS from the c-020 per-species buoyancy oracle); a planted leak/duplication MUST FAIL it.
8. **DETERMINISM + scan coverage:** integer-only authoritative path; the new reaction code covered by BOTH the zero-float +
   int-overflow scans (roots = {Voxel, Structure, Determinism, Types}, zero-float-scan.ps1:36 / int-overflow-scan.ps1:47): if
   the reaction code lands under an already-scanned root, VERIFY both cover the new files; ONLY IF it introduces a NEW
   authoritative directory (e.g. `Core/Field/Reactions`), add it to BOTH root lists (keep them identical) + a planted-violation
   RED self-test there. (The TYPE-HARDCODE scan is a SEPARATE obligation under #3.) Loopback determinism hash green over a
   multi-type reacting seeded run (planted-float / order-dependence RED controls).
9. **check.ps1 -Deliver GREEN** (build + headless + zero-float + int-overflow + type-hardcode scans + mutation ≥70 on new
   Core + spec-silence + deliverable-coverage). G0-frozen (openspec + frozen spec + ledger + mutation-<id>.json ≥70;
   RESULT.md = DELIVERED).
10. **ZERO-LEGACY**; tests rewritten not dragged; the orphaned `Layers/` disposition honoured AND a live-spec check confirms
    no deletion contradicts a current `openspec/specs/**/spec.md` SHALL (the Wave-2-LOCKED `GridEventKind.Reaction` /
    `ReactionLayer` / `ReactionHeat` contract is NOT deleted without an owner-gated amendment); the old `ReactionLayer` /
    `GridEventKind.Reaction` NOT revived.
11. **OWNER-EYE (confidence, NOT a gate):** owner sees two reactant test gases meet, TELEGRAPH (warn), then BANG (a visible
    product / shove) deterministically in the debug view; AND the REQUIRED-to-CHECK co-op axis — the bang's consequence reaches
    a cell the reactants did not occupy (a non-local shared consequence; a bang whose effect never leaves the trigger cell
    FAILS the axis). Owner-run, no self-marking.

## discipline / gates (carried)

RED-first by an INDEPENDENT test-author (builder cannot edit the red tests) · Core/** placement · -Deliver GREEN · mutation
≥ floor (70%) · a FRESH-SESSION G5 (different model family) refuting the data-driven-no-pair-dispatch /
reaction-rules-ride-the-handshake-hash-ORDER-INDEPENDENTLY / telegraph-member-additive-SKIP-ZERO-and-cell-keyed-DISTINCT /
chain-one-tick-TICK-COUNT-and-apply-permutation / mass-cell-total-conserved-no-wrap / dense-co-residence-no-parallel-overlay /
no-regression-byte-identical-incl-buoyancy / shove-inside-the-settle-envelope / orphaned-ReactionLayer-LOCKED-not-deleted /
co-op-consequence-is-NON-LOCAL seams — COULD-NOT-REFUTE is the bar · STOP-discipline (a type-pair hardcode dispatch incl. an
if-chain, a same-tick cascade, reviving or free-deleting the LOCKED ReactionLayer, a temperature/damage/exothermic-heat
mechanic, touching the frozen far-tier, a silent mass leak, an over-strength shove past the settle envelope, float on the
authoritative path, reopening ADR-0002 = mandatory STOP + escalate) · build in small steps.

## return

A RESULT routed HOME (the OS owns the next CALL): outcome + evidence (commits, -Deliver transcript, mutation json, G5
verdict, the multi-type reacting loopback hash + RED-control trips, the rule-schema + telegraph DERIVED-vs-STORED + handshake-
hash-fold + no-pair-dispatch-fix + mass-policy + mix-overlay-record + Layers-disposition decisions, the chosen ADR number +
sibling numbers checked, the co-op-axis non-local-consequence evidence) + findings for the planner. dev→main merge + push is
OWNER-GATED. On GREEN → the road rolls to Sc-damage (the first real gameplay payoff + the co-op interdependence gameplay
moment).

## budget

One slice. ⚠ The two heaviest NEW obligations are EITHER c-020-sized: (i) a 2-phase STORED telegraph state machine that becomes
a new per-tick `1<<6` checksum member with a chain-one-tick oracle, and (ii) folding a whole new rule-set into the handshake
hash. **SPLIT TRIP (mechanical, not a vibe):** if shipping leg 1 would require BOTH a new STORED `1<<6` telegraph member AND
the rule-set handshake-hash fold AND a multi-tick chain oracle in one build, STOP and split along the MACHINERY seam — leg 1 =
the data-driven RULE-SET + handshake-hash fold + an INSTANTANEOUS (same-detect-tick) bang doing a mass-transform ONLY (proves
the no-pair-dispatch + handshake gates, telegraph DERIVED / no new member); leg 2 = the 2-phase TELEGRAPH (the new STORED
`1<<6` member + the chain-one-tick oracle) + any pressure shove. Do NOT bundle the new per-tick checksum member with the
registry-fold gate; do NOT silently build a blob. For the FIRST leg the bang realizes ONE visible effect (a product type OR a
pressure shove, the PLAN's choice — both is the richer-product deferral). Keep the TEST-types scope tight (2-3 reactant test
types + ≥1 product).

END_OF_FILE: live/indie-game-development/work/c-exec-021-call.md
