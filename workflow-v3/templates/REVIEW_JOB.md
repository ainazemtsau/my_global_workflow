---
artifact_control:
  namespace: workflow_v3
  artifact_type: template
  status: candidate
  owner: workflow_governance
  authority: candidate_parallel_runtime_not_active
---

# Review Job

This file is candidate v3 design material. It is not active Workflow OS authority and does not supersede `workflow/**`.

## Purpose

Use this job to ask a bounded review question without giving the reviewer authority to mutate control state.

## Template

```yaml
review_job:
  id:
  target:
  trigger:
  question:
  input_state_refs:
  allowed_memory_refs:
  allowed_external_research:
  forbidden_actions:
  output_required:
  max_scope:
```

## Output Options

Output must be one of:

```text
no_change
patch_proposal
blocker_report
discovery_request
parent_decision_request
```

## Use Rules

- Keep the question specific.
- Restrict input state to references required for review.
- State whether external research is allowed.
- Require evidence for any proposed change.
- Return patch proposals to parent integration review.

END_OF_FILE: workflow-v3/templates/REVIEW_JOB.md
