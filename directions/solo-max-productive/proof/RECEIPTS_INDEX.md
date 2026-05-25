---
artifact_control:
  namespace: direction_proof
  direction_id: solo-max-productive
  artifact_type: receipts_index
  status: m4_initialized_skeleton
  owner: proof_carrying_workflow_os
---

# Solo Max Productive Receipts Index

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

END_OF_FILE: directions/solo-max-productive/proof/RECEIPTS_INDEX.md
