---
artifact_control:
  namespace: workflow_v3
  artifact_type: template
  status: candidate
  owner: workflow_governance
  authority: candidate_parallel_runtime_not_active
---

# Patch Proposal

This file is candidate v3 design material. It is not active Workflow OS authority and does not supersede `workflow/**`.

## Purpose

Use this proposal to describe a possible change to a parent-controlled surface.

## Template

```yaml
patch_proposal:
  id:
  target_surface:
  change_kind:
  reason:
  evidence:
  affected_nodes:
  risk:
  confidence:
  rollback_or_reopen_condition:
```

## Use Rules

- Name the exact target surface.
- Distinguish reason from evidence.
- List affected nodes and integration risk.
- Include confidence and a reopen condition.
- Wait for parent integration review before applying.

END_OF_FILE: workflow-v3/templates/PATCH_PROPOSAL.md
