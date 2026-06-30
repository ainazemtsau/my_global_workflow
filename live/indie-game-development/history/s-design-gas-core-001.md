# RESULT — s-design-gas-core-001 (design: gas reaction/typing core; LOCK sparse-dominant; route to re-shape)

play: research/design (owner-driven exploration) · bet: g-9c41 (CHARACTER ROAD) · date: 2026-06-30

## outcome

Owner-driven design pass on the gas REACTION + TYPING core. One architecture decision LOCKED (gas representation =
sparse-dominant), one NEW core requirement recorded (env-derived dynamic typing, from lore), the extensible core
mechanism captured, and the road ROUTED to a re-shape. No bet/TREE change applied here (that is the next session's
job). The parallel-session Sc-reactions CALL (c-exec-021) is HELD, not trashed.

## evidence

Grounded in real GasCoopGame code (main @61b7923) + the SPEC + frozen canon + a verification workflow
(wf_21bd0e17-210). The load-bearing claim was re-verified FIRST-HAND: identity is POSITIONAL — `VoxelField._mass =
int[][]` `[species][cell]`, `SpeciesCount` ctor-fixed, a cell has NO stored mutable "type"; the checksum's TypeId
member folds the REGISTRY mapping, not a per-cell id. So env-derived dynamic typing is a real gap on dense, cleanly
closed by sparse-dominant (a per-cell dominant-type stamp). Full design → work/gas-reaction-typing-design-2026-06-30.md.

## decisions (resolved this session)

- **d-gas-representation-001 = SPARSE-DOMINANT** (owner «фиксируем sparse-dominant»). Resolves the SPEC's deferred
  representation decision (Fact 4 / §6 revisit-trigger). Rationale: serves a ~128 roster (~free), the per-cell
  type-stamp for dynamic typing, and condition-waves — all at once. Honest cost: a real re-representation of the gas
  field (Sc-types shipped dense); cheapest now, before reactions pile on. To be ratified into the SPEC at the re-shape
  (G9).

## captures (for the re-shape / reactions shape — NOT acted on here)

- Unified core mechanism: reactions/typing/waves = one deterministic integer f(cell contents + committed-revision
  environment + accumulated history) at the overlap/coarse front → move mass between types OR emit a coarse
  {kind,payload} event other systems read.
- Reactions = a DATA table keyed by AXES (not type-pairs) → new gas = 0 new rules. Outcomes = a pluggable
  event-kind registry (kills today's if-Kind hardcode + thin GridEvent payload). Partial-combine = overlap front,
  rate-limited, mass-exact by construction. Blast wave = reuse the shipped S1 forced-flow impulse. Annihilate =
  declared sink (conservation gate must distinguish from a leak).
- Condition-WAVES (owner extension): a reaction may emit a PROPAGATING coarse event carrying a condition-tag; each
  gas type has DATA rows for how it responds (become X / annihilate / ignite / ignore). Configurable local vs wave.
- NEW core requirement: env-derived dynamic typing (lore q-gas-role «зеркало среды»). REGIME (continuous, derived
  read, no mass move) vs IDENTITY (discrete flip = mass move via a per-cell exposure accumulator + committed-revision
  env read). Temperature-keyed typing/reactions wait on the deferred temp→gas feedback (socket now, dormant).
- Roster fixed at level-load (determinism handshake); ~128 = config ceiling, sparse makes roster size ~free; real
  limit = co-resident-active types + active cells.
- Performance: lockstep → weakest peer's CPU/cache is the wall; new features add bounded constants, not new scaling;
  the one unmeasured = the hangar → bake its FIRST measurement into the sparse-dominant slice.
- Big-space seam already reserved (S4 / representation_tag / collapse-expand / §9.10) → keep open, do not build.
- Open forks for the reactions shape: flip-vs-accumulate (owner leans accumulate), consume-vs-residue, blast
  gameplay-vs-cosmetic, regime-vs-identity, target weakest-hardware.

## decisions_needed

The 5 open forks above are decided at the reactions slice's shape (owner present), not now. No batched decision
request this session — the owner is mid-design and steering live.

## state_changes

Applied to live/** (commit local): NOW.updated→s-design-gas-core-001; current_truth gains the design-lock + HOLD
note; task Sc-reactions status_note + open_calls c-exec-021 note marked HELD (re-scope, do not fire as-is);
NOW.next repointed from `CALL c-exec-021` (fire reactions) to `CALL c-reshape-sparse-dominant` (shape session);
history_pointers + LOG appended; work/gas-reaction-typing-design-2026-06-30.md written; this history file saved.
c-exec-021 / work/c-exec-021-call.md PRESERVED (held, not deleted).

## play_check

- Owner exploration that produced keepable decisions → closed as a design/research session with captures + the one
  resolved decision (KERNEL read-only exception → research session).
- No TREE/CHARTER edit (G9 untouched); no bet re-shape (that is the routed shape session).
- Concurrency surfaced + handled: a parallel writer (s-work-034) advanced the prior plan; reconciled by HOLDING
  c-exec-021 and re-pointing next per the owner's live decision (authority order: live owner instruction > prior
  session), preserving the concurrent work.

## log

2026-06-30 — design (g-9c41 reaction/typing core, s-design-gas-core-001): LOCKED sparse-dominant representation;
captured the unified reaction/typing/wave core + the new env-derived dynamic-typing requirement + performance verdict
+ big-space seam; HELD the concurrently-framed c-exec-021; next = re-shape.

## next

CALL c-reshape-sparse-dominant (shape session, owner present): resolve the SPEC representation decision =
sparse-dominant + record dynamic typing + keep the big-space seam reserved; insert a sparse-dominant representation
slice into the road before reactions (G6, risk task = the first hangar measurement); re-scope c-exec-021 onto it +
fold the new design (reusing its hardening). Open forks resolved at the reactions slice's shape.

END_OF_FILE: live/indie-game-development/history/s-design-gas-core-001.md
