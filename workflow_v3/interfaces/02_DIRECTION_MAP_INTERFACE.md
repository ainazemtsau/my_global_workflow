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
- dependencies;
- strategic uncertainties;
- candidate fronts;
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

## Claim discipline

Every map claim must be backed by accepted records/evidence or marked `candidate`, `unresolved`, or `hypothetical`.

A map claim without status and source is not accepted Direction state.

## Active Front selection

Active Front selection must reference Direction Map areas.

A proposed Active Front must identify:

- source map area or areas;
- touched tracks;
- bottleneck or uncertainty;
- why this focus matters now;
- evidence or decision source;
- rejected/deferred alternatives;
- exit criteria.

## Update path

Direction Map updates only through acceptance/update path.

Result Packets, Next Move Packets, Check Jobs, child chats, and Codex results may propose map updates, but they cannot accept them.

## Future storage target

After a Direction adoption package creates runtime state, the future storage target is:

```text
directions_v3/<direction-id>/runtime/state/DIRECTION_MAP.md
```

This interface package creates no `directions_v3/<direction-id>/runtime/**` path.

END_OF_FILE: workflow_v3/interfaces/02_DIRECTION_MAP_INTERFACE.md
