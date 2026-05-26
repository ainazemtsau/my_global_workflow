---
artifact_control:
  namespace: direction_proof
  direction_id: health-and-beauty
  artifact_type: receipts_index
  status: root_objective_accepted
  owner: proof_carrying_workflow_os
---

# Health and Beauty Receipts Index

```yaml
accepted_receipts:
  - R-HB-ROOT-OBJECTIVE-CONFIRM-2026-05-26
candidate_receipts: []
rejected_receipts: []
receipt_storage_path: receipts/
rules:
  - no receipt -> no progress
  - receipt is candidate until Verify + Commit
```

Accepted receipts are listed only after Verify + Commit.

END_OF_FILE: directions/health-and-beauty/workflow/RECEIPTS_INDEX.md
