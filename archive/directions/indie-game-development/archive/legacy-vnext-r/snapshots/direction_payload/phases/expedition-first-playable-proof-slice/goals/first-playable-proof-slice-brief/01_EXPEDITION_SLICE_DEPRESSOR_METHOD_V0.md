# Expedition Slice Depressor Method v0

```yaml
artifact_control:
  artifact_name: "Expedition Slice Depressor Method v0"
  schema: evaluation_method.v0
  owner_layer: workflow_runtime
  status: active_goal_working_context
  reuse_status: reusable_candidate
  repo_path: "directions/indie-game-development/phases/expedition-first-playable-proof-slice/goals/first-playable-proof-slice-brief/01_EXPEDITION_SLICE_DEPRESSOR_METHOD_V0.md"
  created_by_stage: D1_DEEP_RESEARCH
  created_at: "2026-05-13"
  direction_id: indie_game_development
  phase_id: expedition-first-playable-proof-slice
  goal_id: first-playable-proof-slice-brief
  canonical_status: not_canon
  game_documentation_status: not_game_documentation
  knowledge_patterns_status: not_promoted
```

## Purpose

This method exists to depress optimistic slice design before F0 writes the actual `First Playable Proof Slice Brief`.

Its job is to distinguish:

- real Expedition game quality;
- from formal checklist coverage;
- from a technically interesting gas/grid/topology/destructibility toy;
- from a loose sandbox or generic extraction situation.

The central question is:

> Can a low-fidelity paper-run of the candidate slice produce observable Expedition behavior and the promised co-op judgment experience at acceptable proof cost, without silently deciding deferred exact mechanics?

This method is not a new proof boundary. The accepted proof handoff and accepted minimum proof core remain the boundary.

## Reuse status

Status: `Goal Working Context / reusable-candidate`.

This method may be reused by later Expedition slice/feature checks, but it is not canon.

It must not be copied into `knowledge/patterns/**` until later R1 validation proves that it helped reject a weak option, improve a strong option, or prevent a misleading implementation path.

## Intended use

Use this method before F0 writes the `First Playable Proof Slice Brief`.

F0 must use it to pressure-test the candidate slice, not merely reference it.

The method should be used when the next artifact needs to answer:

- what player experience the slice promises;
- whether the slice creates a connected Expedition judgment loop;
- whether gas/grid/topology/destructibility are game-relevant;
- whether co-op is necessary rather than decorative;
- whether retreat/abandon is a real decision;
- whether the result creates a reason for the next descent;
- whether the slice is cheap enough to prove before implementation.

## Not for / misuse boundaries

Do not use this method to:

- write the actual playable slice inside D1;
- implement a prototype;
- create code tasks;
- create a Task Master graph;
- route directly into Codex product/project execution;
- decide exact cargo mechanics;
- decide exact carrying model;
- decide exact death / downing / group failure model;
- decide exact lift failure or contamination model;
- decide exact procedural generation model;
- decide exact tool list or tool stats;
- decide exact gas recipes, taxonomy, or reaction tables;
- promote Game Documentation;
- promote knowledge/patterns;
- reopen Expedition versus Containment.

If the method seems to require exact mechanics decisions to produce a verdict, that is a warning signal. Route to a decision stage or revise the candidate slice instead of silently solving deferred mechanics.

## Player-experience target

The candidate slice must not promise:

> Players manipulate gas in a cool system.

It must promise something closer to:

> A small co-op team commits to a risky descent for dangerous value in a readable hostile environment, where route pressure, temporary safety, shared consequences, and retreat/abandon judgment make leaving with less a potentially smart decision.

Target experience components:

- Expedition legibility: players understand the run as risk, stake, retreat, partial success, loss, and possible abandoned value.
- Discovery: players read an unknown route / gas / topology situation.
- Pressure and challenge: the situation pushes them toward a costly choice.
- Fellowship / shared dependence: players need shared state, communication, and role dependence.
- Meaningful retreat judgment: push / reroute / secure / retreat / abandon must be a real decision.
- Next-descent pull: the result must create a concrete reason to go down again.

## Evaluation principles

1. Observable behavior beats author intent.

If the author says the slice creates tension, but the paper-run produces no hesitation, negotiation, risk talk, or retreat discussion, treat the claim as weak or failed.

2. Connected loop beats isolated cool moment.

A single impressive gas, destruction, route, or vessel moment does not pass unless it connects to the accepted Expedition loop.

3. Shared-state need beats formal co-op.

Co-op is valid only when removing a player, role, shared resource, or shared consequence meaningfully changes the available decisions.

4. Retreat / abandon must be painful enough to matter.

Retreat is not proof if it is just a menu option or obvious optimal escape.

5. Gas is pressure, not proof.

Gas is valid only when it affects route choice, temporary safety, dangerous vessel-value, co-op consequence, push/reroute/secure/retreat/abandon judgment, or consequence-ledger reason for the next descent.

6. Deferred mechanics must stay visible.

The method may use abstract placeholders, but it must not pretend exact cargo, carrying, death, lift, tool, procgen, inventory, economy, or gas taxonomy decisions have been made.

7. Cheapest honest proof wins.

Prefer the smallest paper-run or low-fidelity representation that can honestly test the judgment loop.

## Paper-run protocol

Run the candidate slice at low fidelity before any implementation plan.

Minimum materials:

- a simple route / room / path sketch;
- markers for gas or pressure zones;
- one dangerous vessel-value marker;
- simple tool / intervention tokens;
- a lift / exit boundary marker;
- a consequence ledger note area;
- a run log.

Minimum roles:

- Facilitator: runs the slice and exposes only what players would plausibly read.
- Player team: 2–4 people, or simulated roles if real players are unavailable.
- Depressor / skeptic: asks failure questions and watches for false positives.
- Ledger keeper: records decisions, consequences, and next-descent reason.

Minimum three runs:

1. Baseline run.
   - Does the candidate produce Expedition legibility without extra author rescue?
2. Route / return pressure run.
   - Does gas/topology change route, safety, return path, or decision timing?
3. Vessel-value destabilization run.
   - Does dangerous value create stake, carrying pressure, leakage, damage, loss, or reason to abandon?

After each run, record:

- when the team first discussed risk;
- when the team first discussed retreat;
- what made co-op necessary;
- what decision felt most painful;
- what consequence was locked into the ledger;
- why the team would or would not descend again;
- what hidden rule the facilitator had to invent to keep the run alive.

A paper-run is weak or failed if it only works through continuous facilitator rescue, hidden exact mechanics, or author explanation that players would not have.

## Mechanics-to-experience translation

Use a compact MDA-style translation:

`mechanic / affordance -> expected dynamic -> required player experience`

Required mapping rows:

| Slice element | Expected dynamic | Required experience |
| --- | --- | --- |
| Lift / descent boundary | Commitment, entry/exit threshold, result lock-in | Expedition tension |
| Unknown route + topology | Reading, uncertainty, route comparison | Discovery and spatial judgment |
| Gas pressure | Rerouting, temporary safety, retreat timing, shared risk | Challenge under readable consequence |
| Dangerous vessel-value | Reward-threat coupling, carrying/stabilizing pressure | Stake, loss, temptation |
| Tool / intervention | Costly temporary safety or access | Agency under constraint |
| Co-op shared state | Communication, role dependence, shared consequence | Fellowship / team judgment |
| Push / reroute / secure / retreat / abandon point | Irreversible or costly choice | Real judgment |
| Consequence ledger | State persists after run | Next-descent pull |

If a candidate slice cannot fill this mapping without vague phrases like "players will care" or "gas makes it interesting," treat it as weak.

## Follow-the-fun hypothesis check

Do not ask only:

> Was it fun?

Ask which promised Expedition experience appeared.

Minimum hypotheses:

- Players start speaking as an expedition team before the first intervention.
- The first tense discussion happens before result lock-in.
- Removing one player, role, or shared resource meaningfully changes options.
- Gas/topology changes at least one real route, safety, retreat, vessel, or ledger decision.
- The dangerous vessel-value makes success feel risky rather than just rewarding.
- Retreat or abandon becomes a reasonable and emotionally costly option.
- The ledger creates a concrete, state-based reason for a next descent.

Mark "false-positive fun" when the strongest enjoyment comes only from:

- watching gas move;
- breaking things;
- experimenting with a route toy;
- optimizing a generic loot extraction;
- enjoying a sandbox with no Expedition judgment.

False-positive fun does not kill the whole Direction, but it should revise or kill the candidate slice.

## Red-team / depressor questions

Use these before accepting a candidate slice.

1. If gas is replaced by a generic timer, does the slice stay almost the same?
2. If dangerous vessel-value is replaced by ordinary loot, does the tension stay almost the same?
3. If co-op is replaced by parallel solo tasks, does anything essential disappear?
4. If retreat is always obviously right or obviously wrong, is there any real judgment?
5. If the consequence ledger leaves no concrete reason for next descent, what did the run prove?
6. If the strongest memory is "cool system" rather than "hard expedition decision," did it pass the right test?
7. If the paper-run needs exact cargo, carrying, death, lift, procgen, tool, or gas rules to be judged, is the slice too expensive or too undefined?
8. If the slice works only because the facilitator explains stakes verbally, are the stakes actually in the play?
9. If one player can solve the situation while others assist decoratively, is co-op proof fake?
10. If no one would want another descent after the ledger result, where is the replay pull?

Any "yes, almost the same" answer to questions 1-4 is a major warning.

## Pass / Weak / Fail matrix

Evaluate seven axes.

| Axis | Pass | Weak | Fail |
| --- | --- | --- | --- |
| Player promise / Expedition legibility | Players can describe the situation as a risky expedition with stake, retreat, partial success/loss, and possible abandoned value. | Expedition framing exists but depends on author explanation. | It reads as gas sim, sandbox, generic extraction, or Containment/crisis ops. |
| Connected judgment loop | Accepted minimum loop appears as one connected sequence. | Required beats exist but feel separate. | The slice is a set of disconnected mechanics or moments. |
| Decision tension | Push/reroute/secure/retreat/abandon is meaningfully debated. | Decision exists but is obvious or low-cost. | No real judgment point appears. |
| Co-op necessity | Shared state makes communication, role dependence, or rescue/retreat coordination necessary. | Co-op helps but mostly decorates. | Players can run parallel solo tasks without loss. |
| Gas/grid/topology/destructibility relevance | Systems affect route, safety, vessel risk, shared coordination, retreat, or ledger. | Systems affect play only in one local moment. | Systems are spectacle, toy, or replaceable by generic obstacle/timer. |
| Consequence ledger / replay pull | Result creates concrete reason for next descent. | Ledger exists but next descent reason is generic. | No stateful aftermath or next-descent pull. |
| Paper-run viability | Low-fi run works without hidden exact mechanics or constant author rescue. | Run works but needs some unsupported assumptions. | Run cannot be evaluated without solving deferred mechanics or building prototype. |

Hard-fail axes:

- Player promise / Expedition legibility.
- Connected judgment loop.
- Decision tension.
- Co-op necessity.
- Gas-only rejection.

A hard fail blocks `go`.

## Go / Revise / Kill rules

### Go

Use `go` only if:

- no hard-fail axis fails;
- most axes are `pass`;
- any `weak` axis has a clear, small revision path;
- gas-only rejection does not trigger;
- paper-run produces observable risk talk, route/safety judgment, co-op dependence, and next-descent reason;
- cost-to-proof remains small enough for F0 to write a bounded brief.

`go` means F0 may write the slice brief.

It does not mean implementation should start.

### Revise

Use `revise` if:

- Expedition identity is visible but fragile;
- 1–3 axes are weak;
- no hard-fail axis fails;
- the main weakness can be fixed without exact mechanics decisions;
- the candidate still looks like the right thing to test.

`revise` means F0 should not write the final slice brief yet. Adjust the candidate slice shape and run the method again.

### Kill

Use `kill` if:

- any hard-fail axis fails;
- gas-only rejection triggers;
- the slice collapses into gas simulation, loose sandbox, generic extraction, or Containment/crisis ops;
- co-op is decorative;
- retreat/abandon is not a meaningful choice;
- no ledger-based next-descent reason appears;
- paper-run requires hidden exact mechanics or prototype-level fidelity to be judged;
- cost-to-proof is too high for the current Phase.

`kill` means do not send this candidate into F0 as the first playable proof slice.

## Gas / grid / topology / destructibility sanity checks

Apply four tests to each system element.

### 1. Removal test

Remove the element.

Ask:

- Does the team's judgment change?
- Does route, safety, vessel handling, retreat, or ledger change?
- Does co-op dependence change?

If not, the element is probably decoration.

### 2. Swap test

Replace the element with a generic timer, obstacle, lock, or damage zone.

Ask:

- Does the play stay almost the same?
- Does the Expedition promise stay equally intact?

If yes, the element is not yet Expedition-specific.

### 3. Connection test

The element must affect at least two of:

- route choice;
- temporary safety or access;
- dangerous vessel-value risk;
- shared coordination;
- retreat timing;
- consequence ledger;
- next-descent reason.

One isolated effect is weak.

### 4. Spectacle trap test

Ask whether the element's main appeal is:

- visual;
- technical;
- sandbox curiosity;
- destructibility spectacle;
- simulation elegance.

If spectacle is stronger than judgment, mark weak or fail.

Destructibility passes only if it changes access, safety, return path, vessel risk, or cost of decision. "It is cool that things break" is not enough.

## Cost-to-proof check

Before F0 proceeds, ask:

> What is the cheapest honest form that can prove this slice's Expedition judgment loop?

Acceptable proof cost:

- paper-run;
- simple route diagram;
- abstract tokens;
- one dangerous value placeholder;
- simple consequence ledger;
- minimal player-role assumptions;
- explicit unresolved mechanics list.

Warning signs:

- needs full gas taxonomy;
- needs exact reaction tables;
- needs exact tool catalog;
- needs detailed carrying/inventory model;
- needs death/downing/group-failure rules;
- needs procedural generation logic;
- needs full digital readability;
- needs economy/progression/base design;
- needs implementation before identity can be judged.

If proof cost is high, revise or kill. Do not smuggle implementation planning into the slice brief.

## Required F0 output contract

F0 must include evidence that it used this method.

The `First Playable Proof Slice Brief` must include:

1. One-sentence player promise.
2. Candidate slice loop.
3. Mapping from candidate slice to accepted minimum Expedition loop.
4. MDA-style mechanics-to-experience table.
5. Paper-run summary or paper-run-ready protocol if no live paper-run was possible.
6. Follow-the-fun hypothesis check.
7. Red-team / depressor answers.
8. Pass / Weak / Fail matrix.
9. Go / Revise / Kill verdict.
10. Gas-only rejection check.
11. Gas/grid/topology/destructibility relevance statement.
12. Cost-to-proof check.
13. Visible deferred mechanics list.
14. Explicit statement that no exact deferred mechanics were silently decided.

If F0 cannot provide these sections, it must not claim the playable slice brief is ready for R1.

## Promotion rule for later reuse

This method may be promoted later only if all are true:

- it is used in at least two slice/feature contexts;
- R1 or later review confirms it materially improved judgment quality;
- it helped reject a weak option, improve a strong option, or prevent implementation of a misleading candidate;
- it did not create checklist bloat;
- it remained compatible with the accepted Expedition proof core;
- the user explicitly approves promotion.

Possible future target only after validation:

`directions/indie-game-development/knowledge/patterns/playable-slice-depressor-method.md`

Do not create that file now.

## Source basis

This method is supported by compact external practice references, used only as evaluation discipline:

- Game Design Workshop / playcentric design and core mechanic prototyping.
- MDA: Mechanics, Dynamics, Aesthetics.
- Low-fidelity prototyping practice.
- Premortem / red-team critique.
- RITE-style rapid iterative evaluation.
- Pretotyping / “right it before build it right.”

These sources do not override the accepted Expedition proof handoff or accepted minimum proof core.
