---
artifact_control:
  namespace: workflow_v3
  artifact_type: template
  status: candidate
  owner: workflow_governance
  authority: candidate_parallel_runtime_not_active
---

# Child Chat Packet

This file is candidate v3 design material. It is not active Workflow OS authority and does not supersede `workflow/**`.

## Purpose

Use this packet to launch bounded parallel work that returns to a parent node for integration.

## Template

```yaml
child_chat_packet:
  parent_node:
  child_node:
  purpose:
  input_context:
  allowed_memory:
  forbidden_memory:
  allowed_actions:
  forbidden_actions:
  expected_outputs:
  result_report_required:
  events_to_emit:
  return_to:
```

## Use Rules

- Give the child only the context needed for its task.
- Require a result report or blocker report.
- Name events the child should emit or request.
- Keep parent integration as the only control-state mutation path.
- Do not let child work inspect arbitrary internals of sibling nodes.

END_OF_FILE: workflow-v3/templates/CHILD_CHAT_PACKET.md
