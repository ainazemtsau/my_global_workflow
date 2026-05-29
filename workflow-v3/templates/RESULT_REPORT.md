---
artifact_control:
  namespace: workflow_v3
  artifact_type: template
  status: candidate
  owner: workflow_governance
  authority: candidate_parallel_runtime_not_active
---

# Result Report

This file is candidate v3 design material. It is not active Workflow OS authority and does not supersede `workflow/**`.

## Purpose

Use this report when a node returns completed work, partial work, or a blocker to its parent.

## Template

```yaml
result_report:
  node_id:
  status:
  produced_outputs:
  evidence:
  decisions:
  assumptions_changed:
  shared_memory_candidates:
  events_emitted:
  parent_impact:
  recommended_next_action:
```

## Use Rules

- Attach evidence for every done claim.
- Separate decisions made from decisions requested.
- Mark assumptions that changed during work.
- List shared memory candidates without promoting them.
- State the recommended next parent action.

END_OF_FILE: workflow-v3/templates/RESULT_REPORT.md
