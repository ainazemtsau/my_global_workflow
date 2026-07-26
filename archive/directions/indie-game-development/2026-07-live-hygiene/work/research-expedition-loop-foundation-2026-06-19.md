# Research — expedition-loop gameplay foundation

direction: indie-game-development
node: g-d3a8
question: q-expedition-loop-foundation
call: c-gameplay-foundation-research-001
parent: s-canon-011
date: 2026-06-19

## Outcome

The gameplay foundation should not start from biome taxonomy. It should start from
repeatable expedition problems: what the team does, what pressure makes the action
interesting, what forces co-op, and what kind of room must exist because of that
pressure.

Four viable architectures survive at this altitude. They are not final loops; they
are gameplay-problem spines that can be tested, compared, and used to frame the next
canon question.

Recommended next forge: `q-coop-shape`.

`q-base-biome-room-families` should remain deferred. It becomes useful after the
project knows which room jobs must exist: split operation, shared extraction,
route-making, quench/containment, rescue, or some chosen combination. Without that,
biomes risk becoming art taxonomy with props instead of gameplay grammar.

## Source Anchors

- North Star: the player experience is "Мы рискнули — и вытащили это вместе";
  each run pulls between taking the payoff out and pushing deeper; the loop must not
  become "соло-с-друзьями".
  Source: `C:\projects\gas_coop_game_canon\questions\q-north-star.md:26`,
  `:32`, `:41`.
- Gas role: gas is a structured field, not generic fog; effects are non-local, and
  greed raises danger in a shared field. Gas provides a co-op seam, but `q-coop-shape`
  must still choose the actual non-solo mechanism.
  Source: `C:\projects\gas_coop_game_canon\questions\q-gas-role.md:54`,
  `:57`, `:60`, `:90`.
- City/base: descent is continuous through the shaft; depth is gated by the
  environment, not locks; return goes back through the dangerous depth.
  Source: `C:\projects\gas_coop_game_canon\questions\q-the-city.md:101`,
  `:102`, `:108`.
- Base economy: raw gas is not the product; value is a controlled regime plus a
  stabilized output. The reusable factory unit is the regime cell.
  Source: `C:\projects\gas_coop_game_canon\questions\q-base-logistics-labs-factories.md:32`,
  `:35`, `:66`.
- Room affordances: valves, manifolds, bypasses, quench controls, scrubbers,
  cassettes, pressure/temperature readings, and logs are useful only when they
  create decision, risk, tool use, or co-op reading; chores-for-chores are out.
  Source: `C:\projects\gas_coop_game_canon\questions\q-regime-cell-affordances.md:20`,
  `:21`, `:29`.
- g-9c41 reality: the current engineering spine supports a coarse gas world on a
  real generated level, one controlled breach/topology change, coarse replication,
  and a player-legible render terminus. Fine local front reconstruction, temperature
  feedback, full gas-type seam, full destruction, population, save/load, and late
  join are later or out.
  Source: `C:\my_global_workflow_worktrees\indie-game-development\live\indie-game-development\NOW.md:77`,
  `:84`, `:85`, `:97`, `:107`, `:141`, `:152`, `:365`.

## Viable Architectures

### 1. Elevator-Spine Depth Push

Repeated player action:

The team descends through the shaft spine, reads current gas/temperature/route
conditions, chooses whether to push deeper or turn back, takes a valuable objective,
and returns through the same increasingly hostile vertical route.

Why it is interesting:

It is the cleanest match to the North Star's greed/fear pull. The decision is not
"clear every room"; it is "we can still leave, but the next layer may pay better."
Return matters because the path home is part of the risk, not a menu exit.

Co-op pressure:

Depth alone does not force co-op. This architecture needs a hard shared extraction
rule, split route responsibilities, rescue/failure coupling, or shaft/commit logic
that makes the objective team-shaped. Otherwise it collapses into parallel solo
scavenging.

Gas/base fit:

Strong. The city already defines the lift shaft as physical spine and depth as an
environmental gate. Gas pockets, heat profile, and return-through-danger all follow
from frozen canon.

g-9c41 / production fit:

Good at foundation altitude. It can ride coarse whole-level gas, generated topology,
and legible room filling. It must not require fine 25cm return fidelity or a large
gas roster yet.

Decisive unknown:

What exactly makes the payoff "together": shared carry, shared extraction boundary,
simultaneous roles, rescue dependency, or a combined rule?

Room/biome implication:

Rooms are not "residential biome #4"; they are staging pockets, shaft access,
route-risk rooms, bypasses, cold buffers, measurement horizons, and return
chokepoints.

### 2. Regime-Cell Heist

Repeated player action:

The team enters a small set of reusable production rooms and turns dangerous room
conditions into a temporary controlled process: isolate, feed, set conditions, read
instruments, hold, quench, clean/certify, and extract the stabilized output.

Why it is interesting:

It makes gas danger, prize, and engine the same thing. The reward comes from
operating near the edge of a regime, not from finding a chest. A small room kit can
generate many situations if pressure, heat, gas state, and route consequences vary.

Co-op pressure:

Natural but not automatic. One player can be at the active cell, another at the
control/read/quench side, another watching the route or stabilizing the carry-out.
It fails if this becomes synchronized button chores; every action must change risk,
route, output, or rescue state.

Gas/base fit:

Very strong. It is directly downstream of the frozen "base as vertical factory of
regimes" canon and explains why production/logistics rooms exist.

g-9c41 / production fit:

Medium-good. Coarse gas, temperature as a replicated plane, and room capacity can
support a first pass. Exact gas-family reactions, product economy, temperature-to-gas
feedback, and detailed props remain later.

Decisive unknown:

What is the smallest placeholder regime grammar that creates decisions without
freezing exact gas families or product economy?

Room/biome implication:

Room families follow from procedure jobs: feed rooms, control galleries, quench
rooms, scrubber corridors, sample/cassette staging, failed cells, and bypassed old
cells.

### 3. Breach/Vent Route-Making

Repeated player action:

The team reshapes the room graph and gas routes: open or close bypasses, trigger or
exploit one controlled breach, vent/trap gas, redirect flow, and make a route safe
enough to reach or extract the objective.

Why it is interesting:

The environment becomes both obstacle and tool. A room is valuable when it changes
the gas field somewhere else. The player is not solving a static puzzle; each action
changes the route the team must still survive.

Co-op pressure:

Strong if non-locality is made explicit. One player operates or reads a remote node;
another stands in the room where pressure/gas/temperature changes; another protects
the return or handles rescue. It fails if it is only solo vent puzzles with voice chat.

Gas/base fit:

Strong. Frozen canon already says effects are non-local and logistics creates
"action here / consequence there" structure. The base canon also supports old
bypasses, cold spine, valves, manifolds, scrubbers, and lift logistics.

g-9c41 / production fit:

Best immediate fit. Current engineering has a generated topology seam, one real
controlled breach, gas flow across topology change, and a player-legible coarse
render goal. It must not depend on many breaches, full destruction, population, or
late-join/network product polish.

Decisive unknown:

Is route-making the primary loop, or is it a supporting layer inside depth-push /
regime-cell heists?

Room/biome implication:

Room families become flow-control problems: bypass corridors, valve galleries,
pressure-buffer rooms, breach-adjacent spaces, scrubber/quench access, and rescue
pockets.

### 4. Containment/Quench Relay

Repeated player action:

The team moves an unstable sample/cassette/output through rooms to a quench,
clean/certify, or extraction point while its risk state and the surrounding gas field
change.

Why it is interesting:

It gives "вытащили вместе" a concrete object without freezing the whole economy. The
payload can be prize and hazard at once: carrying it may leak, heat, attract a regime
flip, block tools, slow movement, or force the team through a safer-but-longer route.

Co-op pressure:

Potentially the hardest anti-solo rule: shared carry, escort, remote stabilization,
route control, and rescue can all attach to one object. It fails if it is just package
delivery with scary lighting.

Gas/base fit:

Good. Canon says canisters/cassettes are last-meter logistics, not the whole bulk gas
economy, and quench/clean/certify is mandatory for a product. This keeps raw-gas
mining rejected while preserving a tangible carried prize.

g-9c41 / production fit:

Medium. The field/room risk can be represented at coarse level, but the exact object
rules, inventory/carry UI, product identity, and balance are not available yet and
should not be promised.

Decisive unknown:

Can the carried thing itself produce meaningful shared air/route decisions, or does
it become a thin fetch quest?

Room/biome implication:

Room families become relay problems: cassette staging, cold buffers, quench rooms,
contaminated corridors, elevator loading, emergency scrubber shortcuts, and failed
certification rooms.

## Merge / Dedupe Notes

- "Threshold manipulation / activation geography" is real, but it is better treated
  as a pressure layer inside the four survivors, not as a fifth architecture. It says
  how gas becomes valuable/dangerous; it does not by itself say what the team does
  together.
- "Non-local systems intervention" is also real, but it is a co-op seam shared by
  Regime-Cell Heist and Breach/Vent Route-Making. It should be carried into
  `q-coop-shape` as a mechanism candidate, not frozen as a complete loop.
- "Coarse-field breach slice" is an engineering-compatible proof slice, not the full
  product loop. It most strongly supports Breach/Vent Route-Making and can feed the
  next design choice after t-4 returns.

## Parked / Rejected Directions

- Biome-first taxonomy: parked. The owner already stopped it because room families
  are premature without gameplay-problem grammar.
- Pure gas-sim sandbox / tech demo: rejected. The charter says the core game is not a
  gas simulation tech demo.
- Parallel-solo scavenging: rejected. It directly violates the North Star unless a
  shared extraction, shared air, split operation, or rescue/failure mechanism binds
  players.
- Raw gas mining / selling gas bottles: rejected. Frozen canon says raw gas is not
  the product; value comes from controlled regimes and stabilized outputs.
- Monster/chase horror core: rejected. Horror is seasoning, and gas has no agency,
  targeting, or chase intent.
- Exact gas roster / reaction menu / product economy first: parked. These depend on
  later `q-gas-families` and `q-controlled-products-economy`; this session must not
  freeze them.
- Chores-for-chores station operation: rejected. Interactives must create decision,
  risk, tool use, or co-op read.
- Arbitrary locks/keyhunts/quotas: rejected. Depth is gated by environment and
  preparation, not "collect X to open door."
- Content-volume solution: parked. The solo scope favors a small reusable vocabulary
  of room problems over a large list of bespoke biomes.

## Decisive Unknowns

1. Hard co-op enforcement: which pressure actually prevents solo-with-friends?
   Candidates: shared extraction/carry, non-local split operation, rescue/failure
   coupling, route/return dependency, or a hybrid.
2. Primary expedition spine: is the run primarily a depth-push, a regime-cell heist,
   a route-making operation, a containment relay, or a macro/micro combination?
3. Prize identity at high altitude: what can be named now without freezing exact
   products? Likely "stabilized output / cassette / sample / certified regime data",
   not raw gas.
4. Minimum room-problem kit: what small set of reusable room jobs proves the loop
   before any biome roster exists?
5. g-9c41 timing: how much should design wait for the t-4 player-legible artifact?
   It can inform which survivor is most readable, but the canon can already rule out
   weak directions.
6. Gas-family dependency: can `q-coop-shape` work with placeholder gas regimes, or
   does it need one tiny provisional set from `q-gas-families`?

## Recommendation

Forge `q-coop-shape` next.

Reason:

`q-gas-role` already gives the co-op seam: shared field, non-local effects, greed
raising danger for everyone. It explicitly does not choose the actual mechanism that
makes the loop non-solo. `q-base-logistics-labs-factories` gives room bones, but it
also says the co-op seam is not exhausted there. Therefore the next load-bearing
canon decision is not gas families and not biomes; it is the co-op shape that decides
which hard pressure(s) the expedition loop must obey.

Recommended framing for that forge:

Which co-op spine makes the expedition structurally not solo-with-friends while
preserving "рискнули — и вытащили это вместе"?

Options to consider in that forge:

- Shared extraction spine: the payoff is team-gated by carry/extraction/commit rules.
- Non-local operation spine: meaningful actions happen here while consequences land
  there, forcing split roles and communication.
- Rescue/failure spine: gas states create recoverable teammate crises that are costly
  but not arbitrary.
- Hybrid spine: macro Elevator-Spine Depth Push, with Breach/Vent Route-Making and
  Regime-Cell/Containment problems as repeatable room jobs.

The likely strongest starting hypothesis is the hybrid spine, because it preserves
the macro greed/fear promise while letting rooms be generated from a small set of
systemic co-op problems. But that is still a hypothesis for `q-coop-shape`, not a
frozen answer here.

## Why q-base-biome-room-families Stays Deferred

`q-base-biome-room-families` asks for biome lists, compartment families, props,
hazards, loot, traversal affordances, and states. Those are downstream nouns. The
missing upstream verbs are still open: split, carry, quench, vent, read, rescue,
route, extract, decide to go deeper or return.

Resume biome grammar only after:

1. `q-coop-shape` freezes the hard co-op spine or at least the co-op pressure menu.
2. Either `q-gas-families` or a narrower placeholder gas-regime decision gives enough
   gas problem vocabulary for room jobs.
3. `q-regime-cell-affordances` can define the reusable interactive props without
   becoming chores.

Until then, biome work should only collect examples as raw material, not freeze
canon.

## Confidence And Limits

Established from sources:

- The North Star requires co-op-first, shared risk/reward, and "вытащили вместе".
- Gas is a structured field with non-local effects and shared-air risk.
- The base is a vertical factory of regimes, not a raw-gas mine.
- The current engineering substrate supports coarse generated topology, one breach,
  and player-legible gas at coarse level; it does not yet support final gas families,
  fine local fronts, temperature feedback, full destruction, or proven co-op feel.
- Biome/room-family freeze was intentionally stopped as premature.

Inference:

- The four architectures above are viable problem spines, not canon decisions.
- The hybrid spine is probably the best next hypothesis, because it unifies macro
  expedition pressure with reusable room jobs.
- `q-coop-shape` should precede `q-gas-families` unless the owner wants a tiny
  provisional gas-regime set first for design thinking.

What would change the answer:

- The owner rejects regime-cell operation as too factory-procedural or too chore-like.
- The t-4 render terminus reveals that route-making / breach flow is dramatically
  more legible than regime operation, or the opposite.
- `q-who-we-are` chooses a player identity that strongly implies a different mission
  contract.
- Early co-op playtest evidence shows that the chosen pressure does not create
  communication, dependency, or shared tactical planning.

## Sources Read

- `C:\my_global_workflow_worktrees\indie-game-development\os\KERNEL.md`
- `C:\my_global_workflow_worktrees\indie-game-development\os\plays\research.md`
- `C:\my_global_workflow_worktrees\indie-game-development\live\indie-game-development\NOW.md`
- `C:\my_global_workflow_worktrees\indie-game-development\live\indie-game-development\TREE.md`
- `C:\my_global_workflow_worktrees\indie-game-development\live\indie-game-development\CHARTER.md`
- `C:\my_global_workflow_worktrees\indie-game-development\live\indie-game-development\history\s-canon-011.md`
- `C:\my_global_workflow_worktrees\indie-game-development\live\indie-game-development\work\canon-track-design-2026-06-15.md`
- `C:\projects\gas_coop_game_canon\questions\q-north-star.md`
- `C:\projects\gas_coop_game_canon\questions\q-coop-shape.md`
- `C:\projects\gas_coop_game_canon\questions\q-gas-role.md`
- `C:\projects\gas_coop_game_canon\questions\q-the-city.md`
- `C:\projects\gas_coop_game_canon\questions\q-base-logistics-labs-factories.md`
- `C:\projects\gas_coop_game_canon\questions\q-base-biome-room-families.md`
- `C:\projects\gas_coop_game_canon\questions\q-regime-cell-affordances.md`
- `C:\projects\gas_coop_game_canon\questions\q-controlled-products-economy.md`
- `C:\projects\gas_coop_game_canon\questions\q-visual-style.md`
- `C:\projects\gas_coop_game_canon\questions\q-who-we-are.md`
- `C:\projects\gas_coop_game_canon\maps\World.md`

END_OF_FILE: live/indie-game-development/work/research-expedition-loop-foundation-2026-06-19.md
