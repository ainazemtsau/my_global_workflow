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

## Current package boundary

No path is created now under:

```text
directions_v3/<direction-id>/runtime/**
```

This interface package is repository documentation/setup only.

## State rules

- `DIRECTION_MAP.md` is part of the future state model.
- `operations/check_jobs/` is an explicit operations surface.
- `operations/event_loop_closures/` is an explicit operations surface.
- Accepted state mutates only through acceptance/update path.
- Signals, Handler Results, Action Inbox Items, Check Jobs, Event Loop Closures, Result Packets, and Codex output do not mutate accepted state alone.

## Storage mapping

| Entity | Future storage if adopted |
| --- | --- |
| Direction Spine | `state/DIRECTION_SPINE.md` |
| Direction Map | `state/DIRECTION_MAP.md` |
| Active Front | `state/ACTIVE_FRONT.md`, `fronts/`, `indexes/FRONTS_INDEX.md` |
| Work Graph | `fronts/<front-id>/WORK_GRAPH.md` |
| Work Graph Node | `fronts/<front-id>/nodes/<node-id>/NODE.md` |
| Work Contract | `records/contracts/` and node indexes |
| Run | `records/runs/` |
| Result Packet | `records/result_packets/` |
| Evidence | `records/evidence/` |
| Acceptance Decision | `records/acceptance/` |
| Memory Candidate | `memory/candidates/` |
| Memory Artifact | `memory/artifacts/` |
| Signal | `operations/signals/` |
| Action Inbox Item | `operations/action_inbox/` |
| Check Job | `operations/check_jobs/` |
| Event Loop Closure | `operations/event_loop_closures/` |
| Recovery record | `operations/recovery/` |
| Runtime Console source | `console/` |

END_OF_FILE: workflow_v3/interfaces/09_STORAGE_STATE_INTERFACE.md
