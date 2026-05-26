---
artifact_control:
  namespace: direction_proof
  direction_id: indie-game-development
  artifact_type: receipts_index
  status: initialized_skeleton
  owner: proof_carrying_workflow_os
---

# Indie Game Development Receipts Index

## Receipt State

```yaml
accepted_receipts: []
candidate_receipts: []
rejected_receipts: []
receipt_storage_path: receipts/
```

## Accepted Receipts

None.

## Rules

No receipt -> no progress.

Receipt is candidate until Verify + Commit.

Accepted Receipts are Ledger authority only after Commit.

No legacy import Receipts exist yet.

No accepted strategic Receipts exist yet.

END_OF_FILE: directions/indie-game-development/workflow/RECEIPTS_INDEX.md
