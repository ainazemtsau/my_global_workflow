# Gas reaction + typing CORE — design pass (2026-06-30, owner-driven)

Status: a design/decision exploration with the owner on the gas reaction/typing core. It LOCKS one architecture
decision, adds one new core requirement (from lore), and ROUTES to a re-shape (it does NOT itself re-shape the bet).
Grounded in real GasCoopGame code (main @61b7923), the SPEC (knowledge/g9c41-gas-engine-SPEC.md), and frozen canon,
plus a verification workflow (wf_21bd0e17-210) whose key claim was re-checked first-hand in code.

This file is the SELF-CONTAINED input for the re-shape session. Read it + NOW.md + the existing (now HELD)
work/c-exec-021-call.md.

## LOCKED decision (owner «фиксируем sparse-dominant»)

**Gas representation = SPARSE-DOMINANT**, not the current dense `int[species][cell]` planes. A cell stores
`{dominant type + amount + a small mix-overlay}`. This RESOLVES the representation decision the SPEC deferred
(Fact 4 / §6 revisit-trigger). Verified in code: today identity is POSITIONAL — `_mass = int[][]` `[species][cell]`,
`SpeciesCount` is ctor-fixed, a cell has NO stored "which type am I" field; the per-cell TypeId in the checksum folds
the REGISTRY mapping, not a mutable per-cell id (VoxelField.cs ~30-130).

Why this is the keystone (it serves THREE owner requirements at once):
1. a large roster (~128 types) becomes nearly free — you pay for active cells + co-resident types, not a full plane
   per possible type;
2. it gives the per-cell **dominant-type stamp** that today does not exist — that stamp is what makes runtime
   re-typing (flip the stamp) and condition-waves (pass through, change the stamp) natural and cheap;
3. reactions ride it organically (dominant + overlay = the "mix-overlay" the SPEC's Fact 4 already names).
Honest cost: it is a real re-representation of how the field stores gas (Sc-types shipped dense). Cheapest to do NOW,
before reactions/typing pile onto dense.

## The ONE unified mechanism (the core to build well)

Reactions AND env-typing AND condition-waves are the SAME pattern: a deterministic integer
`f(local cell contents + committed-revision environment + accumulated history)` evaluated AT THE OVERLAP/COARSE FRONT
in canonical order, that EITHER moves mass between types (combine / transform / re-type) OR emits a coarse
`{kind, payload}` EVENT other systems read. Chemistry/axes/outcomes are DATA folded into the registry ContentHash so
divergent tables desync at the START handshake, never silently mid-run.

- **Reactions = a DATA table keyed by AXES** (fuel↔oxidizer, cold↔heat, caustic↔inert, …), NOT by type-pairs → a new
  gas of any tier adds ZERO new rules (O(axes)). A rule = (predicate over reactants' axis coords + optional env band)
  → (outcome kind, integer consume ratio rA:rB, optional product type C, per-tick rate cap). Axes/menu are CONFIG
  (come from canon q-gas-families; the engine invents no numbers).
- **Conditions = a per-cell integer ENVIRONMENT VECTOR** assembled from already-authoritative layers (temperature
  {energy_sum,capacity_sum}, local density, reserved channels: radiation/neighbours/catalysts). Read at
  COMMITTED-REVISION (1-tick lag, SPEC seam 7) — never same-tick (same-tick cross-layer = desync). This is exactly
  why temperature→gas feedback is deferred (d-tempfeedback-001) and is the true unblock dependency for any
  temperature-CONDITIONED reaction/typing.
- **Outcomes = pluggable EVENT KINDS** (transform / explosion / ignite / freeze): a session-fixed outcome-registry
  (mirror GasTypeRegistry: sorted ids + ContentHash) + registered-handler dispatch REPLACES today's hardcoded
  if-Kind chain (GridEventKind is a hand-numbered enum read by if/else today — the hardcode the owner wants gone).
  New outcome = one data row + one handler, zero core-switch edits. The GridEvent payload (one int today) widens to a
  fixed Arg0..Arg3 block whose meaning the kind owns (keep existing kinds byte-identical so goldens never rebaseline).
- **Partial combine (owner's "two huge clouds")** = front-local, rate-limited, mass-exact BY CONSTRUCTION: reaction
  fires ONLY where both reactant types are non-zero (the overlap front); pure interiors have a zero factor. The
  per-tick cap marches the front inward over ticks — "instant whole-cloud combine" is structurally impossible.
- **Mass:** "transform" conserves (by ratio); "annihilate" REMOVES mass = a DECLARED sink. Legal, but it must be an
  explicit declared outcome the conservation gate distinguishes from an accidental leak.
- **Blast wave = REUSE the shipped S1 forced-flow impulse** (VoxelImpulse + EmitImpulse + the decaying per-face bias
  register) — an explosion emits an impulse and inherits conservation / back-pressure / determinism for free. No new
  shock field, no new checksum member.

## Owner extension — CONDITION-WAVES (propagating transformation)

A reaction MAY emit a PROPAGATING coarse event that carries a condition-TAG (owner's "условие A"); each gas type has
DATA rows describing how IT responds to that tag (gas1,2 → gas4; gas3 → annihilate; gas5 → ignite; gas6 → ignore).
So "a wave along which gas changes, each type differently" = a propagating coarse promo-event + a per-type response
table — the SAME mechanism, just an event that propagates. Configurable per reaction: local-only vs wave (a data flag
on the outcome). Cost = a marching front with a per-tick cap (spread over ticks, not one frame); determinism = it is a
coarse event computed from coarse state on every peer (the existing promo-event machinery; must NOT read a private
near bubble).

## NEW core requirement — env-derived DYNAMIC TYPING (from lore, q-gas-role «зеркало среды»)

Not previously in the engine plan. Lore (frozen): gas is one substance, MANY faces; a face = a CONTINUOUS function of
CURRENT local conditions; the generic PARENT is never shown as itself. At SPAWN a gas reads its environment and
BECOMES a type; at RUNTIME, if its environment changes (cold-room gas drifts into heat), it ACCUMULATES and can FLIP
type. This is a REAL gap on dense (no per-cell stamp to flip) — and the keystone reason sparse-dominant is right.

Implementation under sparse-dominant (the SAME core mechanism): split along canon's seam —
- **REGIME** (continuous "angrier in heat" WITHOUT becoming a new gas) = a DERIVED read off the env vector; changes
  only how the field is POSTED (intensity + effect-category), moves no mass, folds nothing new.
- **IDENTITY** (the discrete jump A→C) = the only thing that moves mass: a per-cell **exposure ACCUMULATOR**
  integrates env-vs-threshold each tick (heat ++, cold --, clamped, hysteresis); crossing a DATA threshold flips the
  dominant type (+ emits a typed event). The generic parent = a plane/flag that transforms on first env-eval.
Dependency: temperature-keyed typing needs the deferred temp→gas feedback (committed-revision read) — SOCKET it now,
temperature rows DORMANT until that slice; density/neighbour conditions can drive it sooner.

## Roster ceiling

The hard constraint is NOT "how many types" — it is that the ROSTER (which types CAN appear) is fixed at level/session
load (it seeds the lockstep registry ContentHash handshake). "Load all we have each level" as a roster = fine.
~128 is a reasonable CONFIG ceiling, NOT hardcoded. Under sparse-dominant, roster size is ~free; the real limit is
co-resident-ACTIVE types in one area (a handful) + active-cell count. Recommendation: roster size = config; do not
weld 128 in.

## Performance

Governing law: lockstep → the WEAKEST peer's CPU (really memory/cache bandwidth) is the wall, NOT the network. Cost ∝
ACTIVE cells (sparse-awake already computes only the front; slept gas is ~free). The new features (sparse-dominant,
reactions, waves, typing) add BOUNDED constants to already-active cells — NOT a new scaling axis. sparse-dominant
implementation must be CACHE-friendly (dominant + small fixed overlay inline per cell, not a per-cell hashmap).
The ONE genuinely unmeasured number = the "hangar" (a player in a big open ACTIVE volume, memory/cache-bound).
RECOMMENDATION: bake a FIRST hangar worst-case measurement into the sparse-dominant slice's done_when (the SPEC says
measure it first; sparse-dominant changes the memory profile, so it is the moment). Open: pick the target
weakest-hardware as an explicit assumption (sets the active-gas budget).

## Big-space seam (owner ask: "leave room for huge-space optimization")

ALREADY reserved in the architecture — NOT building it now, just keep the door open: S4 coarse room-rollup +
`representation_tag {fine-3D | coarse | bucket}` + collapse/expand conversion (SPEC Fact 2/§4 seams 2,4 / §9.10
address reserve / far-only mid-2.5D reserve, §7). The sparse-dominant slice MUST preserve the per-region structure +
collapse/expand seam so S4 plugs in later WITHOUT core edits (a done_when line). S4 itself stays deferred.

## CONCURRENCY note (important)

While this design ran, a PARALLEL session (s-work-034) framed + hardened the Sc-reactions executor CALL c-exec-021
(work/c-exec-021-call.md) on the PRIOR plan (dense rep, pairwise, no dynamic-typing/waves). It is **HELD, not
trashed**: much of its hardening survives and is REUSED (telegraph+bang = coarse event, no-hardcode-dispatch,
the machinery, ADR-0021, the Wave-2-LOCKED ReactionLayer/GridEventKind contract). It must be RE-SCOPED onto
sparse-dominant + fold this design BEFORE it fires. Do NOT fire c-exec-021 as-is. (Two writer-sessions on one
direction again — flagged to the owner to serialize.)

## Open forks (decide at the reactions slice's shape, owner present)

1. Re-typing: hard FLIP vs gradual ACCUMULATE (owner LEANS accumulate-with-hysteresis — canon-faithful, no border
   chatter, but it is the one genuinely new replicated per-cell field). NOT yet confirmed.
2. Combine: consume reactants fully (one cloud eats the other) vs leave a co-resident RESIDUE of both.
3. Blast wave: gameplay-load-bearing (pushes gas/bodies, chains detonations → in the sim, S1-impulse) vs cosmetic
   (a visual whoosh → could live in the visual track).
4. Regime vs identity: model the continuous "angrier in heat" channel now, or only the discrete A→C jump first
   (cheaper; regime as a later derived read).
5. Target weakest-hardware assumption (sets the active-gas budget for the hangar measure).

## RE-SHAPE MANDATE (what the next session does — shape play, owner present, G6/G9)

1. Update the SPEC (knowledge/g9c41-gas-engine-SPEC.md, G9 owner sign): resolve the deferred representation decision =
   sparse-dominant; record the env-derived dynamic-typing requirement; note the big-space seam stays reserved and the
   sparse-dominant slice keeps it open.
2. Insert a SPARSE-DOMINANT REPRESENTATION step into the character road AFTER Sc-weight, BEFORE Sc-reactions; shape it
   (G6: appetite, cut list, lens sweep, risk task = the hangar measurement). done_when incl.: gas field
   re-represented sparse-dominant (dominant + amount + small overlay), per-cell dominant-id present (enables typing),
   roster-size config, byte-identical single-type no-regression, determinism preserved, big-space collapse/expand
   seam preserved, FIRST hangar measurement, the usual gate battery (-Deliver, mutation ≥70, independent REDs,
   fresh-session G5, ZERO-LEGACY, owner-eye).
3. Re-scope c-exec-021 (Sc-reactions) onto sparse-dominant + fold this design (condition-waves, per-type response,
   dynamic-typing socket), reusing its hardening; the open forks resolved at its shape.

END_OF_FILE: live/indie-game-development/work/gas-reaction-typing-design-2026-06-30.md
