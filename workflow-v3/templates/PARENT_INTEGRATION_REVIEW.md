---
artifact_control:
  namespace: workflow_v3
  artifact_type: template
  status: candidate
  owner: workflow_governance
  authority: candidate_parallel_runtime_not_active
---

# Parent Integration Review

This file is candidate v3 design material. It is not active Workflow OS authority and does not supersede `workflow/**`.

## Purpose

Use this review to accept, reject, or route child results and patch proposals.

## Template

```yaml
parent_integration_review:
  input:
  decision:
  accepted_changes:
  rejected_changes:
  events_emitted:
  memory_updates:
  next_action:
```

## Use Rules

- Review the report, evidence, and parent impact.
- Accept only changes the parent can own.
- Record rejected changes with reason.
- Promote memory only through explicit memory updates.
- Emit events for accepted reports, rejected reports, patches, and active-front changes.

END_OF_FILE: workflow-v3/templates/PARENT_INTEGRATION_REVIEW.md
