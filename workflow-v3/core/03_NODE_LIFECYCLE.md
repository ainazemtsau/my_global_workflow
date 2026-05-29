---
artifact_control:
  namespace: workflow_v3
  artifact_type: core_spec
  status: candidate
  owner: workflow_governance
  authority: candidate_parallel_runtime_not_active
---

# Node Lifecycle

This file is candidate v3 design material. It is not active Workflow OS authority and does not supersede `workflow/**`.

## Node Model

- Composite node: a unit that needs a Local Work Map before child work is selected.
- Executable node: a bounded unit that can be executed, reviewed, researched, or written from a clear contract.

## Statuses

```text
proposed, ready, active, delegated, done, blocked, parked, dropped, superseded
```

## Node Contract

```yaml
node_contract:
  node_id:
  parent_node:
  node_type:
  purpose:
  inputs:
  allowed_memory_refs:
  forbidden_actions:
  expected_outputs:
  validation_or_review_required:
  integration_owner:
```

## Execution Contract

```yaml
execution_contract:
  target:
  readiness_check:
  allowed_actions:
  forbidden_actions:
  validation_plan:
  evidence_required:
  result_report_required: true
```

## Result Report Requirement

Every executed, reviewed, researched, or delegated node returns a result report or blocker report to its parent.

A result report records:

- Produced outputs.
- Evidence.
- Decisions made or requested.
- Assumptions changed.
- Shared memory candidates.
- Events emitted.
- Parent impact.
- Recommended next action.

## Node Closeout Requirement

A node is not complete until its parent accepts its result report or blocker report.

Closeout must decide:

- Whether outputs are accepted.
- Whether memory is promoted.
- Whether events are recorded.
- Whether patches are proposed to parent state.
- Whether blocked, parked, dropped, or superseded status is appropriate.
- Which continuation packet becomes current.

END_OF_FILE: workflow-v3/core/03_NODE_LIFECYCLE.md
