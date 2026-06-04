# Workflow v3 Storage Layout

status: active_skeleton_namespace_corrected

## Production rules/setup namespace

`workflow_v3/**` is the Workflow v3 production rules/setup namespace.

It stores shared runtime model documentation, setup templates, future pack source notes, quality boundaries, and project setup guidance.

It does not store accepted per-Direction runtime state in this slice.

Steering entity and runtime operations are represented by canonical procedure files under:

```text
workflow_v3/procedures/
```

Those procedure files are repository rule/setup sources, not runtime state.

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
    GOAL_EVIDENCE_GRAPH.md
    ACTIVE_FRONT.md
    CURRENT_STATUS.md
    CURRENT_NEXT_MOVE.md
  fronts/
  records/
    parent_integration/
    graph_deltas/
    upstream_escalations/
    downstream_deltas/
    derived_gate_checks/
    result_packets/
    evidence/
    acceptance/
  memory/
    candidates/
    artifacts/
  operations/
    check_jobs/
    transfer_packets/
    recovery/
  archive/
  indexes/
    GOAL_EVIDENCE_INDEX.md
    MEMORY_INDEX.md
  config/
    DIRECTION_PROJECT_BINDING.md
  console/
    DIRECTION_CONSOLE.md
```

`state/GOAL_EVIDENCE_GRAPH.md` is an optional future split file. A future package may instead embed or reference Goal Evidence Graph structure from `state/DIRECTION_MAP.md`.

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
- optional Goal Evidence Graph split or Direction Map reference;
- Active Front;
- Current Status;
- Current Next Move.

## fronts

`fronts/` stores Active Front workspaces and local Work Graph material. A front may contain nodes, local context, local indexes, contracts, runs, evidence references, decisions, and closure summaries.

Front records may reference Active Unresolved Cut candidates, parent integration results, graph deltas, upstream escalation packets, downstream delta packets, and derived gate checks when a future accepted package creates those records.

## records

`records/` stores dated proof records:

- Work Contracts;
- Runs;
- Result Packets;
- Evidence;
- Acceptance Decisions;
- Parent Integration Results;
- Graph Deltas;
- Upstream Escalation Packets;
- Downstream Delta Packets;
- Derived Gate Checks.

Records are evidence and history. Accepted state changes still require explicit acceptance/update paths.

Records, evidence, packets, parent integration results, graph deltas, downstream deltas, upstream escalations, and derived gate checks do not mutate accepted state by existence.

## memory

`memory/` stores Memory Candidates, promoted Memory Artifacts, and indexes.

Raw chat notes or run output do not become Memory Artifacts without promotion.

Memory Artifact promotion must use the registered Memory Artifact Promotion procedure and explicit acceptance/update path before storage under `memory/artifacts/`.

## operations

`operations/` stores operational support surfaces that are separate from accepted state:

- `check_jobs/` for bounded verification work;
- `transfer_packets/` for copy-paste handoff packets when a transfer must be retained;
- `recovery/` for recovery records.

Direction Check Jobs belong under:

```text
directions_v3/<direction-id>/runtime/operations/check_jobs/
```

Direction Transfer Packets belong under:

```text
directions_v3/<direction-id>/runtime/operations/transfer_packets/
```

Check Jobs and Transfer Packets are operational surfaces only and do not mutate accepted state.

## archive

`archive/` stores closed, superseded, or compacted fronts, nodes, records, and supporting history while preserving evidence links.

Archive/compaction must not hide accepted decisions, evidence references, final state transitions, or unresolved blockers.

## indexes

`indexes/` stores lookup files for fronts, nodes, runs, evidence, acceptance, Goal Evidence Graph references, and memory.

Indexes support read-back and navigation. They are not an alternate acceptance path.

Future optional indexes include:

```text
indexes/GOAL_EVIDENCE_INDEX.md
indexes/MEMORY_INDEX.md
```

## config

`config/` stores adopted Direction-specific configuration such as customization profile, adapter context access, and quality gates.

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
