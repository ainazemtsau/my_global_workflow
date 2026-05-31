# Workflow v3 Storage Layout

status: active_skeleton_namespace_corrected

## Production rules/setup namespace

`workflow_v3/**` is the Workflow v3 production rules/setup namespace.

It stores shared runtime model documentation, setup templates, future pack source notes, quality boundaries, and project setup guidance.

It does not store accepted per-Direction runtime state in this slice.

## Future per-Direction runtime state root

The future per-Direction runtime state root is:

```text
directions_v3/<direction-id>/runtime/
```

That path may be created only after a separate per-Direction adoption package with explicit acceptance, scope, validation, and rollback/coexistence evidence.

No `directions_v3/<direction-id>/runtime/**` root is created in this correction package.

## Future per-Direction layout

Future adopted Directions may use this layout:

```text
directions_v3/<direction-id>/runtime/
  state/
    DIRECTION_SPINE.md
    DIRECTION_MAP.md
    ACTIVE_FRONT.md
    CURRENT_STATUS.md
    CURRENT_NEXT_MOVE.md
  fronts/
  records/
  memory/
  operations/
    signals/
    action_inbox/
    check_jobs/
    event_loop_closures/
    recovery/
  archive/
  indexes/
  config/
  console/
```

## state

`state/` stores small current-state files needed to resume the adopted Direction:

- Direction Spine;
- Direction Map;
- Active Front;
- Current Status;
- Current Next Move.

## fronts

`fronts/` stores Active Front workspaces and local Work Graph material. A front may contain nodes, local context, local indexes, contracts, runs, evidence references, decisions, and closure summaries.

## records

`records/` stores dated proof records:

- Work Contracts;
- Runs;
- Result Packets;
- Evidence;
- Acceptance Decisions.

Records are evidence and history. Accepted state changes still require explicit acceptance/update paths.

## memory

`memory/` stores Memory Candidates, promoted Memory Artifacts, and indexes.

Raw chat notes or run output do not become Memory Artifacts without promotion.

## operations

`operations/` stores operational support surfaces such as Signals, Action Inbox/Q, closed actions, Check Jobs, Event Loop Closure records, and recovery records.

Persisted signal history for an adopted Direction belongs under:

```text
directions_v3/<direction-id>/runtime/operations/signals/
```

Direction Action Inbox/Q belongs under:

```text
directions_v3/<direction-id>/runtime/operations/action_inbox/
```

Direction Check Jobs belong under:

```text
directions_v3/<direction-id>/runtime/operations/check_jobs/
```

Direction Event Loop Closures belong under:

```text
directions_v3/<direction-id>/runtime/operations/event_loop_closures/
```

Action Inbox stores candidate actions, not raw signals.

Signals, Action Inbox items, Check Jobs, and Event Loop Closures are operational surfaces only and do not mutate accepted state.

## archive

`archive/` stores closed, superseded, or compacted fronts, nodes, records, and supporting history while preserving evidence links.

Archive/compaction must not hide accepted decisions, evidence references, final state transitions, or unresolved blockers.

## indexes

`indexes/` stores lookup files for fronts, nodes, runs, evidence, acceptance, and memory.

Indexes support read-back and navigation. They are not an alternate acceptance path.

## config

`config/` stores adopted Direction-specific configuration such as customization profile, handlers, adapter context access, and quality gates.

The Direction handler registry belongs at:

```text
directions_v3/<direction-id>/runtime/config/HANDLERS.md
```

Direction-specific config must preserve the core Workflow v3 acceptance and adapter boundaries.

## console

`console/` stores read-only Runtime Console source indexes.

Console sources support status/navigation views only. They do not execute work or mutate accepted state.

## Non-creation statement

This correction package creates no per-Direction runtime state. Old Direction files under `directions/**` remain legacy evidence unless a later package explicitly adopts, bridges, or imports them.

END_OF_FILE: workflow_v3/STORAGE_LAYOUT.md
