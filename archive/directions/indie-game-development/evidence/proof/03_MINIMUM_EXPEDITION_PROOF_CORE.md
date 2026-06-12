# Minimum Expedition Proof Core

## Proof question

Can the first proof show Expedition as an escalating co-op judgment loop—prepare risk, descend through a lift, read gas/topology/dangerous value, alter route or safety, recover or stabilize a dangerous vessel, face readable consequences, and choose push, reroute, secure, retreat, or abandon—rather than as an isolated gas simulation or loose prototype?

## Smallest testable Expedition loop

The first proof must show this minimum loop at contour level:

```text
prepare risk / tools
→ descend through lift
→ read unknown route + gas + dangerous value
→ spend tool / change route / create temporary safety
→ recover or stabilize dangerous vessel-value
→ readable gas/topology/vessel consequence happens
→ team chooses push / reroute / secure / retreat / abandon
→ result is locked into consequence ledger
→ there is a reason for next descent
```

This loop is the minimum Expedition judgment loop.

If this loop is not visible, the proof does not prove Expedition.

Required system interactions:

- Gas must affect route, retreat, temporary safety, dangerous vessel handling, or co-op consequence.
- Topology must make gas and route pressure readable at room / route / return-path scale.
- Dangerous vessel-value must connect reward and threat.
- Tools must act as risky capital roles, not as a finalized tool roster.
- Lift / extraction must act as the physical boundary between entry, retreat, result locking, and between-run consequence.
- Between-run state must stay a consequence ledger, not an economy, shop, upgrade tree, or progression system.

This artifact does not define a prototype scene, implementation plan, task list, or technical build order.

## Observable proof signals

The first proof needs six observable signals:

1. **Expedition legibility** — players understand the situation as an expedition with risk, stake, retreat, partial success, loss, and possible abandoned value.
2. **Gas/topology route pressure** — gas and spatial structure change route choice, safety windows, return path, or the decision to continue or leave.
3. **Dangerous vessel-value stake** — value is not generic loot; it is dangerous because it can be damaged, leak gas, lose value, create carrying pressure, or become worth abandoning.
4. **Co-op shared-state consequence** — co-op matters because players share one gas, route, cargo, tool, rescue, and retreat state rather than doing parallel solo tasks.
5. **Real judgment point** — the run creates a meaningful push / reroute / secure / retreat / abandon decision before the result is locked.
6. **Next-descent reason** — after the result, there is a concrete reason for another descent, such as extracted value, lost tools, damaged vessel/access, gained route knowledge, opened access, or unresolved risk.

## Gas-only rejection

A proof is invalid if it can pass only by showing gas movement, gas reactions, gas visuals, or Gas/Grid technical competence.

Gas is valid proof pressure only when it connects to Expedition meaning:

- route choice;
- retreat pressure;
- dangerous vessel-value;
- co-op consequence;
- push / reroute / secure / retreat / abandon judgment;
- consequence-ledger reason for the next descent.

A technically impressive gas simulation is supporting evidence, not proof.

If gas does not produce Expedition judgment, the proof collapses into a gas tech demo.

## Non-goals and deferred decisions

This artifact and the first proof boundary do not decide:

- playable proof design;
- prototype scene specification;
- implementation plan;
- code tasks;
- Codex execution;
- exact cargo mechanics;
- exact carrying model;
- exact death / downing / group failure model;
- exact lift failure or contamination model;
- exact procedural generation model;
- exact tool list or tool stats;
- exact gas recipes, gas taxonomy, or reaction tables;
- exact inventory system;
- exact economy;
- exact progression;
- exact reward curve;
- exact base / hub form;
- Expedition versus Containment reopening;
- Game Documentation promotion.

Deferred decisions remain visible but unresolved:

- found vessel vs player-filled vessel;
- shared vs personal cargo ownership;
- hand-carrying vs backpack vs shared carrying vs tool-assisted carrying;
- death / downing / group failure;
- lift failure / contamination;
- between-run base / hub / economy form;
- depth unlock model;
- 4-player proof focus vs future 4-8 pressure test;
- exact gas taxonomy and reactions;
- exact tool catalog;
- exact procedural model;
- exact one-use consequence tracking.

These questions must not be silently solved inside F0.

## Validation method

Validate the first proof at proof-boundary level, not as a production metrics plan.

Method:

1. Review later proof evidence against the six observable proof signals.
2. Mark each signal as `pass`, `weak`, or `fail`.
3. Check whether the smallest Expedition loop appears as one connected judgment loop.
4. Check whether gas is tied to Expedition meaning rather than isolated simulation quality.
5. Assign one outcome: `go`, `revise`, or `kill`.

Outcome criteria:

### Go

Use `go` if:

- Expedition is legible as Expedition;
- gas, topology, dangerous value, co-op consequence, retreat/extraction judgment, and consequence ledger reinforce each other;
- there is a real push / reroute / secure / retreat / abandon decision;
- gas-only rejection does not trigger.

### Revise

Use `revise` if:

- Expedition is partly visible but weak;
- systems work separately but not as one judgment loop;
- dangerous vessel-value does not create enough stake;
- co-op consequence is decorative or unclear;
- retreat / abandon exists formally but does not feel like a meaningful decision.

### Kill

Use `kill` if:

- the proof collapses into gas simulation;
- the proof becomes a loose sandbox;
- the proof becomes generic cargo extraction;
- the framing becomes Containment / crisis ops;
- systems stay disconnected and do not produce Expedition judgment;
- the selected Expedition bet would require major identity change to work.

## Stop rules

Stop before execution or route to the appropriate review / decision stage if any of these happen:

- Work shifts into playable proof design.
- Work shifts into prototype scene specification.
- Work shifts into implementation planning or code tasks.
- The proof can pass as gas simulation alone.
- The artifact requires choosing exact cargo, carrying, death, lift, procgen, tool, inventory, economy, or progression mechanics.
- Codex/project execution is requested before active project root, AGENTS.md, project/tool bindings, validators, and required runtime surfaces are verified.
- Gas/Grid technical work tries to replace missing Grid-owned room identity, room bounds, connection identity, door state, anchors, apertures, capacities, or deterministic topology ordering with hidden fallbacks.
- The work requires changing Game Documentation before artifact acceptance / R1 review.
- The work reopens Expedition vs Containment.
- The work touches sibling Directions, project/code files, tooling/binding files, or common workflow canon.

## Acceptance checklist / matrix

| Acceptance item | Artifact evidence | Read-back check |
| --- | --- | --- |
| One-sentence proof question | `## Proof question` | Confirm the section contains exactly one question sentence. |
| Smallest testable Expedition loop | `## Smallest testable Expedition loop` | Confirm the loop is boundary-level, not prototype design. |
| 4-6 observable proof signals | `## Observable proof signals` | Confirm there are exactly six signals. |
| Explicit gas-only proof rejection | `## Gas-only rejection` | Confirm gas simulation alone is rejected. |
| Explicit non-goals and deferred decisions | `## Non-goals and deferred decisions` | Confirm unresolved mechanics are not silently decided. |
| Validation method with go/revise/kill | `## Validation method` | Confirm all three outcomes are present. |
| Codex/project-binding stop rule | `## Stop rules` | Confirm Codex/project execution is blocked until bindings are verified. |
