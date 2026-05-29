---
artifact_control:
  namespace: workflow_v3
  artifact_type: template
  status: candidate
  owner: workflow_governance
  authority: candidate_parallel_runtime_not_active
---

# Continuation Packet

This file is candidate v3 design material. It is not active Workflow OS authority and does not supersede `workflow/**`.

## Purpose

Use this packet to restart a direction, active front, or selected node in any chat without rereading the whole project.

## Template

```yaml
continuation_packet:
  direction_id:
  current_control_state_ref:
  active_front:
  selected_node:
  allowed_memory_refs:
  latest_decisions:
  latest_events:
  current_task:
  forbidden_actions:
  expected_output:
```

## Use Rules

- Include only references the next assistant may use.
- State forbidden actions explicitly.
- Keep the current task narrow enough to finish or return a blocker report.
- Update this packet after parent integration or active-front change.
- Do not import legacy/current data through this packet without explicit import/review.

END_OF_FILE: workflow-v3/templates/CONTINUATION_PACKET.md
