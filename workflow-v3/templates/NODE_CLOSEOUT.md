---
artifact_control:
  namespace: workflow_v3
  artifact_type: template
  status: candidate
  owner: workflow_governance
  authority: candidate_parallel_runtime_not_active
---

# Node Closeout

This file is candidate v3 design material. It is not active Workflow OS authority and does not supersede `workflow/**`.

## Purpose

Use this closeout when a parent accepts a node result or blocker report and updates the next continuation surface.

## Template

```yaml
node_closeout:
  input:
  completion_check:
  memory_promotions:
  event_entries:
  parent_patch_proposals:
  review_queue_updates:
  next_continuation_packet:
```

## Use Rules

- Check whether the node contract was satisfied.
- Promote only accepted reusable output.
- Record event entries for lifecycle and integration changes.
- Create parent patch proposals for any larger control change.
- Update the next continuation packet.

END_OF_FILE: workflow-v3/templates/NODE_CLOSEOUT.md
