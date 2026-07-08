# Design Lab - Q1 Gas Spatial Form

Status: work note, not canon.
Session: `s-designlab-gas-spatial-form-001`
Call: `c-designlab-gas-spatial-form-001`
Direction: `indie-game-development`
Node: `g-d3a8`
Question: `q-first-proof-gas-spatial-form`
Play: `local/design-lab`

## Central question

In the first Bubble proof, before any Bubble exists, what is physically present
when we say "there is gas here"?

The useful answer cannot be just a noun. It must say what players can want,
read, do, risk, and change.

## Why now

This is the earliest hard blocker behind the Bubble proof. Detection/read,
transfer to Bubble, carry sizing, release, external reactions, and co-op proof
all depend on what gas occupies in space before custody begins.

Skipping this would make the next questions hide undefined mechanics behind
terms that sound solved.

## Plain-language current understanding

The first proof stays Bubble-first as one proof only: players find a dangerous
gas state, later get visible custody/value, carry it through route danger, and
failure returns gas to the world.

The spatial model for Q1 is:

> Gas before Bubble is a local region of the shared gas field, not an object,
> pickup spot, container, creature, or final VFX plate. For the first proof it
> should have a readable edge or gradient, some height/volume character, and a
> reason the room can move or deform it.

Short version:

**Use a readable field-area with layer/gradient behavior as the first paper
model.**

## Relevant map slice

Parents:
- Mechanics Workbench question map v0.1 is owner-approved, variant A.
- Bubble-first is the single current proof candidate; no two playable branches.
- Old canon is evidence/salvage only.
- Gas is a shared field/system, not creature AI.

Blockers cleared by this note:
- Q1 no longer has to choose between "object", "whole room", "source only", or
  "obvious visual blob" as the first paper model.
- Q2 can now ask what players read at the edge/gradient/height of the field-area.

Downstream still blocked:
- Q2 pre-contact read / detection.
- Q3 transfer to Bubble.
- Q4 Bubble carry / custody.
- Q5 rupture / leak / release.
- Q6 external gas / reactions.
- Q7 two-player necessity.

Adjacent questions that affect this:
- Building/tool sockets matter only as ways the room can move or reveal the
  field-area; exact tools are later.
- Source/flow matters as a modifier of the field-area, not as the whole answer.
- Quiet floor matters as low-activity/readability, not as magic sleep/wake.

Parent-canon reopen risks:
- None found. No map repair or parent reopen is needed.

## Out of scope

- No canon freeze.
- No exact transfer action.
- No exact membrane, tool, cargo, economy, full roster, title, or final VFX.
- No gas creature AI, intent, target selection, or magic sleep/wake.

## Options considered

### A. Readable local field-area with layer/gradient - recommended

Good because:
- grows from the locked shared field instead of inventing a pickup object;
- gives Q2 a concrete thing to make fair: edge, gradient, height, movement,
  residue, pressure, sound, material change, or instrument clue;
- keeps Bubble transfer open without solving it;
- makes rupture/release coherent: gas returns to the field at the failure place;
- supports co-op later because one player can read or control the field while
  another handles custody/route.

Bad because:
- it can become too abstract unless Q2 gives it perceivable, non-numeric tells;
- if the edge never moves or bites, it becomes a static hazard zone.

Verdict:
accept as the first paper spatial model, with Q2 required before any
mechanic-forge/prototype claim.

### B. Source/flow first

Good because:
- movement, vents, doors, pressure, height, and route changes become important;
- it strongly supports building-as-gas-tool later.

Bad because:
- it turns Q1 into plumbing/control too early;
- resting gas becomes unclear;
- transfer-to-Bubble starts depending on exact tools or room machinery.

Verdict:
park as a modifier inside the recommended model. A source or flow may shape the
field-area; it is not the whole first-proof spatial answer.

### C. Fully obvious visible cloud or pool

Good because:
- instantly readable;
- easy to explain in one screenshot;
- supports a simple first teaching scene.

Bad because:
- it can erase detection/read gameplay;
- it risks making gas a generic colored hazard;
- it pulls final VFX too early.

Verdict:
reject as the default first model. It may appear only as a later readability
choice for Q2, not as Q1's spatial truth.

### D. Diffuse near-invisible whole-room concentration

Good because:
- matches the idea of gas as a field;
- connects well to exposure/dose and near-field engine support.

Bad because:
- unfair without strong pre-contact read;
- tends to collapse into HUD/instrument numbers;
- gives Bubble no clear bounded scene to act around.

Verdict:
reject as the first proof's default. It may exist as an outer trace around the
recommended field-area, but cannot carry the proof alone.

### E. Discrete object/clump/pickup

Good because:
- very easy to select and collect;
- simple for inventory-like thinking.

Bad because:
- contradicts the shared-field core;
- hides the gas-world behavior the proof is supposed to show;
- makes release/reaction feel like item durability instead of a world change.

Verdict:
reject for the first proof.

## Scenes / models explored

### Scene 1 - quiet edge in a small room

Where are we?
A small room and one return corridor. Gas occupies a local field-area: denser
near one side, thinner near the doorway, with a readable edge/gradient and a
height character.

What do players want?
They want to understand where the valuable/dangerous part is before deciding
whether and how to create Bubble custody later.

What do players read?
The boundary, height, density change, and room clues: moving dust, residue,
condensation, pressure sound, door behavior, floor/ceiling layer, or a simple
diegetic spike. Exact channels are Q2.

What can players do?
They can approach, stop short, compare routes, open/close a route socket later,
warn the partner, and choose where the later Bubble action should happen. The
transfer action itself remains unresolved.

Why is the risky option tempting?
The denser/deeper part looks like better value or a cleaner capture target.

Why does fear exist?
Crossing or disturbing the edge can expose a player, alter the return route, or
move the field-area into a worse place.

What changes?
Player movement or route interaction can shift the readable edge; later rupture
would put gas back into the room as field, not delete it.

What can go wrong?
The team misreads the edge, takes the wrong route, disturbs the field before
they are ready, or makes the later Bubble action in a place that poisons the
return path.

What remains unresolved?
Exact tells, exact transfer action, Bubble size/custody, release tuning, and
reaction cases.

### Scene 2 - source/flow as pressure on the field-area

Where are we?
A crack, vent, cold spot, door gap, or vertical shaft slowly feeds or bends the
field-area.

What do players want?
They want the field-area to stay readable and useful long enough to act.

What do players read?
Direction, drift, pressure behavior, and whether opening a route makes the area
spread toward the return path.

What can players do?
They can decide whether to change the room state now or leave it alone until the
later Bubble action. Exact tools stay out of scope.

Why is the risky option tempting?
Changing the room may expose a denser or easier-to-handle part of the field.

Why does fear exist?
The same change may push gas toward the partner, route, or future custody path.

What changes?
The field-area moves, thins, thickens, or shifts height.

What can go wrong?
The proof becomes a door/vent puzzle instead of gas custody.

What remains unresolved?
Which route/building sockets belong in the first proof, if any.

Verdict:
use this only as support for the recommended model, not as the first Q1 answer.

### Scene 3 - too-obvious blob stress test

Where are we?
A room contains an obvious colored mass that every player understands from the
door.

What do players want?
They want the valuable gas because it is visibly there.

What do players read?
Mostly "avoid the colored area" or "collect the colored area".

What can players do?
They can route around it or prepare a later custody action.

Why is the risky option tempting?
It is legible and promise-rich.

Why does fear exist?
Only generic hazard fear unless Q2 adds deeper signals.

What changes?
Not much unless later systems add behavior.

What can go wrong?
Detection becomes trivial, and the gas reads like a standard hazard pickup.

What remains unresolved?
Everything interesting: field-read, source/flow, release, co-op pressure.

Verdict:
reject as Q1 default.

## Stress against mechanic lenses

1. Grows from core:
Paper pass. The recommended model derives from shared field behavior and
not-solo extraction pressure. Object/clump variants fail here.

2. Interesting decision:
Paper potential only. The model can create a tradeoff between safer outer edge
and richer/dangerous denser part, but Q2/Q5 must make the cost readable.

3. Anti-solo:
Not proven. The model gives material for later co-op roles, but Q7 must refute
sequential one-player play.

4. Pillar pull:
Paper potential. Greed can point toward denser/better gas while fear points
toward shared route exposure. This remains unverified.

5. Field-read:
Q2 is now the blocker. The model is usable only if players can read it through
perceivable channels before irreversible consequence.

6. Grey-box:
Not run. Status remains UNVERIFIED.

## Blockers found

No blocker before Q1.

New explicit blocker:
Q2 must define the first fair pre-contact read for the recommended field-area.
Without Q2, the model is only a paper skeleton.

## Side dependencies found

- Q3 transfer to Bubble must inherit "bounded part of a field-area", but not
  solve it here.
- Q5/Q6 release/reaction should inherit "gas returns as field at failure
  location".
- Q11 tools/building should inherit "room sockets can reveal or move the
  field-area", but exact sockets stay later.

## Parked topics

- Exact transfer action.
- Exact Bubble membrane/tool/cargo behavior.
- Economy/base/meta.
- Full roster, names, flagship jobs, reaction tables.
- Title and public pitch.
- Final VFX/UI.
- Exact building/tool list.
- Old canon migration.

## Visual check

No visual check is required for Q1. Q2 may need a visual plate because the next
question is explicitly about what players read.

## Lab verdict

Route: continue lab.

Q1 result:
accepted/revised/split as paper design:
- accept gas as a local shared-field area, not object/pickup/creature;
- revise first proof to use a readable edge/gradient/layer behavior;
- split exact reads to Q2, transfer to Q3, custody to Q4, release/reactions to
  Q5/Q6, anti-solo to Q7.

Canon-forge is not ready. Mechanic-forge is not ready. The next blocker is Q2:
pre-contact read / detection for this field-area.

## Next CALL

Next route:
`c-designlab-gas-precontact-read-001`.

END_OF_FILE: live/indie-game-development/work/design-labs/gas-spatial-form-001.md
