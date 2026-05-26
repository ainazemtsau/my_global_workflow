---
artifact_control:
  namespace: direction_proof
  direction_id: health-and-beauty
  artifact_type: receipts_index
  status: m4_initialized_skeleton
  owner: proof_carrying_workflow_os
---

# Health and Beauty Receipts Index

```yaml
accepted_receipts: []
candidate_receipts: []
rejected_receipts: []
receipt_storage_path: receipts/
rules:
  - no receipt -> no progress
  - receipt is candidate until Verify + Commit
```

No receipts are invented by this skeleton.

END_OF_FILE: directions/health-and-beauty/workflow/RECEIPTS_INDEX.md
