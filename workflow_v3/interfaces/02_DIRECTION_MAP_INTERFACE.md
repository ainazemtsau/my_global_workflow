# Direction Map Interface

status: active_interface_layer

## Purpose

Direction Map is the global structural map between Direction Spine and Active Front.

It prevents the Direction Spine, Active Front, Work Graph, unreviewed task lists, and chat intuition from redefining one another.

## Definition

Direction Map describes the current accepted/candidate/unresolved structural landscape of one Direction after adoption.

It may include:

- tracks;
- map areas;
- embedded or associated Goal Evidence Graph;
- required claims;
- alternatives;
- obstacles;
- evidence gaps;
- dependencies;
- strategic uncertainties;
- candidate fronts;
- candidate Active Unresolved Cuts;
- closed fronts;
- blocked areas;
- evidence links;
- accepted labels;
- candidate labels;
- unresolved labels;
- hypothetical labels.

## Not this

Direction Map is not:

- a roadmap;
- a backlog;
- a Work Graph;
- an unreviewed task list;
- a list of tasks;
- a chat-authored plan without source labels;
- a storage replacement for accepted records/evidence.

Goal Evidence Graph may explain the evidence/control structure associated with Direction Map claims. It remains a steering/control projection, not a semantic primitive or accepted state by existence.

## Claim discipline

Every map claim must be backed by accepted records/evidence or marked `candidate`, `unresolved`, or `hypothetical`.

A map claim without status and source is not accepted Direction state.

## Active Front selection

Active Front selection must reference Direction Map areas.

When a Goal Evidence Graph exists, Active Front selection should also reference the Active Unresolved Cut and the relevant graph nodes or map claims.

A proposed Active Front must identify:

- source map area or areas;
- source Goal Evidence Graph node or Active Unresolved Cut when available;
- touched tracks;
- bottleneck or uncertainty;
- why this focus matters now;
- evidence or decision source;
- rejected/deferred alternatives;
- exit criteria.

## Update path

Direction Map updates only through acceptance/update path.

STAGE_RESULTs, FINISH_PACKETs, NEXT_CHAT_CARDs, Check Jobs, child chats, and Codex results may propose map updates, but they cannot accept them.

## Quality Checks

- Map areas, tracks, dependencies, strategic uncertainties, obstacles, evidence gaps, alternatives, candidate fronts, and candidate cuts are visible when material.
- Each claim carries source/status discipline: accepted, candidate, unresolved, or hypothetical.
- Goal Evidence Graph references trace root outcome, required claims, evidence, blockers, alternatives, and gaps without becoming a roadmap or backlog.
- Active Front candidates trace to map areas and, when available, graph nodes or Active Unresolved Cut.

## Future storage target

After a Direction adoption package creates runtime state, the future storage target is:

```text
directions_v3/<direction-id>/runtime/state/DIRECTION_MAP.md
```

This interface package creates no `directions_v3/<direction-id>/runtime/**` path.

END_OF_FILE: workflow_v3/interfaces/02_DIRECTION_MAP_INTERFACE.md
