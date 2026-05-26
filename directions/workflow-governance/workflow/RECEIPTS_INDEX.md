---
artifact_control:
  namespace: direction_proof
  direction_id: workflow-governance
  artifact_type: receipts_index
  status: root_objective_accepted
  owner: proof_carrying_workflow_os
---

# Workflow Governance Receipts Index

```yaml
accepted_receipts:
  - R-WG-ROOT-OBJECTIVE-ATOMIC-RUN-001
candidate_receipts: []
rejected_receipts: []
receipt_storage_path: receipts/
rules:
  - no receipt -> no progress
  - receipt is candidate until Verify + Commit
```

Accepted receipt storage:

- `receipts/R-WG-ROOT-OBJECTIVE-ATOMIC-RUN-001.md`

END_OF_FILE: directions/workflow-governance/workflow/RECEIPTS_INDEX.md
