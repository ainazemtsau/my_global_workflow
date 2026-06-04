# Storage and State Interface

status: active_interface_layer

## Purpose

This interface defines future storage/state mapping for adopted Workflow v3 Directions.

## Future adopted Direction layout

Future adopted Directions use:

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
  console/
```

`state/GOAL_EVIDENCE_GRAPH.md` is optional. A future adopted Direction may instead embed or reference Goal Evidence Graph structure from `state/DIRECTION_MAP.md`.

## Current package boundary

No path is created now under:

```text
directions_v3/<direction-id>/runtime/**
```

This interface package is repository documentation/setup only.

## State rules

- `DIRECTION_MAP.md` is part of the future state model.
- Goal Evidence Graph may be stored as optional split state, embedded/reference state, and supporting indexes.
- `records/result_packets/` stores persisted Result Packets.
- `records/parent_integration/`, `records/graph_deltas/`, `records/upstream_escalations/`, `records/downstream_deltas/`, and `records/derived_gate_checks/` store typed records/packets when persisted.
- `operations/check_jobs/` is an explicit operations surface.
- `operations/transfer_packets/` is an explicit operations surface when a transfer packet must be retained.
- Accepted state mutates only through acceptance/update path.
- Result Packets, Next Move Packets, Transfer Packets, Check Jobs, Codex output, and Project cache do not mutate accepted state alone.

## Storage mapping

| Entity | Future storage if adopted |
| --- | --- |
| Direction Spine | `state/DIRECTION_SPINE.md` |
| Direction Map | `state/DIRECTION_MAP.md` |
| Goal Evidence Graph | `state/GOAL_EVIDENCE_GRAPH.md` or embedded/reference from `state/DIRECTION_MAP.md`; `indexes/GOAL_EVIDENCE_INDEX.md` |
| Goal Evidence Node | `state/GOAL_EVIDENCE_GRAPH.md`, graph split records, or `indexes/GOAL_EVIDENCE_INDEX.md` |
| Active Unresolved Cut | `state/DIRECTION_MAP.md`, `state/GOAL_EVIDENCE_GRAPH.md`, or front records |
| Active Front | `state/ACTIVE_FRONT.md`, `fronts/`, `indexes/FRONTS_INDEX.md` |
| Work Graph | `fronts/<front-id>/WORK_GRAPH.md` |
| Work Graph Node | `fronts/<front-id>/nodes/<node-id>/NODE.md` |
| Work Contract | `records/contracts/` and node indexes |
| Run | `records/runs/` |
| Result Packet | `records/result_packets/` |
| Evidence | `records/evidence/` |
| Acceptance Decision | `records/acceptance/` |
| Parent Integration Result | `records/parent_integration/` |
| Graph Delta | `records/graph_deltas/` |
| Upstream Escalation Packet | `records/upstream_escalations/` |
| Downstream Delta Packet | `records/downstream_deltas/` |
| Derived Gate Check | `records/derived_gate_checks/` |
| Memory Candidate | `memory/candidates/` |
| Memory Artifact | `memory/artifacts/` |
| Memory Index | `indexes/MEMORY_INDEX.md` |
| Check Job | `operations/check_jobs/` |
| Transfer Packet | `operations/transfer_packets/` |
| Recovery record | `operations/recovery/` |
| Runtime Console source | `console/` |

END_OF_FILE: workflow_v3/interfaces/09_STORAGE_STATE_INTERFACE.md
