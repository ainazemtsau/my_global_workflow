---
artifact_control:
  namespace: direction_proof
  direction_id: workflow-governance
  artifact_type: receipts_index
  status: project_instruction_budget_hardened
  owner: proof_carrying_workflow_os
---

# Workflow Governance Receipts Index

```yaml
accepted_receipts:
  - R-WG-ROOT-OBJECTIVE-ATOMIC-RUN-001
  - R-WG-ATOMIC-RUN-HARDEN-001
  - R-WG-PROJECT-SURFACE-SEPARATION-HARDEN-001
  - R-WG-PROJECT-INSTRUCTION-BUDGET-HARDEN-001
candidate_receipts: []
rejected_receipts: []
receipt_storage_path: receipts/
rules:
  - no receipt -> no progress
  - receipt is candidate until Verify + Commit
```

Accepted receipt storage:

- `receipts/R-WG-ROOT-OBJECTIVE-ATOMIC-RUN-001.md`
- `receipts/R-WG-ATOMIC-RUN-HARDEN-001.md`
- `receipts/R-WG-PROJECT-SURFACE-SEPARATION-HARDEN-001.md`
- `receipts/R-WG-PROJECT-INSTRUCTION-BUDGET-HARDEN-001.md`

END_OF_FILE: directions/workflow-governance/workflow/RECEIPTS_INDEX.md
