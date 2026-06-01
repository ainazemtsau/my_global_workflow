# Workflow v3 Storage Layout

status: active_skeleton_namespace_corrected

## Production rules/setup namespace

`workflow_v3/**` is the Workflow v3 production rules/setup namespace.

It stores shared runtime model documentation, setup templates, future pack source notes, quality boundaries, and project setup guidance.

It does not store accepted per-Direction runtime state in this slice.

Formation protocols and steering entity runbooks live under:

```text
workflow_v3/formation/
```

They are repository rule/setup sources, not runtime state.

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
    DIRECTION_PROJECT_BINDING.md
  console/
    DIRECTION_CONSOLE.md
```

Setup-only root packages may create this future runtime root with semantic placeholders only:

```text
state/DIRECTION_SPINE.md      pending_definition
state/DIRECTION_MAP.md        pending_definition
state/ACTIVE_FRONT.md         none_selected or pending_definition
state/CURRENT_STATUS.md       setup_only_root_created
state/CURRENT_NEXT_MOVE.md    launch_direction_definition
```

These placeholders are not accepted semantic Direction content.

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

Memory Artifact promotion must use the formation and acceptance path before storage under `memory/artifacts/`.

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

The future canonical Project Binding for an adopted ordinary Direction Project belongs at:

```text
directions_v3/<direction-id>/runtime/config/DIRECTION_PROJECT_BINDING.md
```

This binding resolves the ordinary ChatGPT Project to one Direction runtime root. It is future adopted runtime config, not created now.

## console

`console/` stores read-only Runtime Console source indexes.

Console sources support status/navigation views only. They do not execute work or mutate accepted state.

A future read-only Direction Console may be stored at:

```text
directions_v3/<direction-id>/runtime/console/DIRECTION_CONSOLE.md
```

This is a future adopted runtime surface, not created now.

## Non-creation statement

This correction package creates no per-Direction runtime state. Old Direction files under `directions/**` remain legacy evidence unless a later package explicitly adopts, bridges, or imports them.

END_OF_FILE: workflow_v3/STORAGE_LAYOUT.md
