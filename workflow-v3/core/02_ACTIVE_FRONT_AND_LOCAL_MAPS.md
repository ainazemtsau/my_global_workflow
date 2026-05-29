---
artifact_control:
  namespace: workflow_v3
  artifact_type: core_spec
  status: candidate
  owner: workflow_governance
  authority: candidate_parallel_runtime_not_active
---

# Active Front And Local Maps

This file is candidate v3 design material. It is not active Workflow OS authority and does not supersede `workflow/**`.

## Active Front Semantics

The Active Front is the bounded set of work the parent is currently prepared to advance and integrate.

- Primary: the main composite or executable node being advanced.
- Support: work that directly enables the primary node.
- Watch: known conditions to monitor without immediate action.
- Parked: valid work intentionally deferred.
- Blocked: work waiting on input, evidence, permission, dependency, or decision.

The root level should not attempt to contain a detailed graph of the whole project.

## When To Build A Local Work Map

Build a Local Work Map when:

- The selected node is composite.
- The parent can define a clear node contract.
- The parent can integrate the expected child results.
- The next execution or review step needs more detail than Direction Control should carry.

Do not build Local Work Maps for parked, blocked, or merely speculative work.

## Local Work Map Shape

```yaml
local_work_map:
  parent_node:
  map_scope:
  ready:
  locked:
  blocked:
  selected_next:
  child_nodes:
  validation_refs:
  expected_result_reports:
```

## Local State Rules

- Ready: work has enough contract and input to start.
- Locked: work must wait for predecessor output or parent decision.
- Blocked: work cannot proceed without missing input or condition change.
- Selected next: the next node the parent intends to advance.

Local maps only exist for active composite nodes. They are revised or closed during parent integration.

## Boundary Rules

- A Local Work Map is not a replacement for Direction Control.
- Child nodes do not change parent state directly.
- Results return through result reports or blocker reports.
- Old data may inform a map only after explicit import/review.

END_OF_FILE: workflow-v3/core/02_ACTIVE_FRONT_AND_LOCAL_MAPS.md
