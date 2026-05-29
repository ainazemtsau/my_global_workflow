---
artifact_control:
  namespace: workflow_v3
  artifact_type: core_overview
  status: candidate
  owner: workflow_governance
  authority: candidate_parallel_runtime_not_active
---

# Clean Runtime Overview

This file is candidate v3 design material. It is not active Workflow OS authority and does not supersede `workflow/**`.

## Principle

Global planning is intentionally coarse; local planning is detailed only for the active front.

The runtime keeps one clear direction surface and delegates detail to active nodes. It avoids creating full-project maps that become stale before they are used.

## Architecture Elements

- Direction Control: root control surface for the project direction.
- Active Front: the current focus set selected from Direction Control.
- Local Work Maps: detailed planning for active composite nodes only.
- Memory System: scoped memory, promoted shared memory, decisions, events, and artifacts.
- Event / Review / Patch System: explicit signals, review jobs, and proposed state changes.
- Parallel Chat Runtime: child work launched only through parent contracts.
- Execution Boundary: separation between routing, implementation, validation, and evidence.
- Legacy Boundary: preserved current/old data with future explicit import/review.

## Runtime Flow

```text
Root Result
  -> Direction Control
      -> Active Front
          -> Local Work Map
              -> Child Work / Review / Execution
                  -> Result Report
                      -> Node Closeout
                          -> Memory / Events / Patches
                              -> Parent Integration
                                  -> Updated Direction Control
```

## Control Rules

- The root level names outcomes, constraints, track summaries, and queues.
- The active front names what is being worked now and what is supporting, watched, parked, or blocked.
- Local Work Maps are disposable detailed maps for active composite nodes.
- Child work returns result reports or blocker reports to the parent.
- Parent integration is the only route for child output to mutate parent control state.
- Legacy/current workflow data remains preserved in place.

END_OF_FILE: workflow-v3/core/00_CLEAN_RUNTIME_OVERVIEW.md
