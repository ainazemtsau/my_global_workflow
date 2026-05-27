---
artifact_control:
  namespace: direction_proof
  direction_id: health-and-beauty
  artifact_type: receipts_index
  status: h1_blueprint_activation_obligation_admitted_downstream_not_started
  owner: proof_carrying_workflow_os
---

# Health and Beauty Receipts Index

```yaml
accepted_receipts:
  - R-HB-ROOT-OBJECTIVE-CONFIRM-2026-05-26
  - R-HB-CONSTRAINTS-DEFINE-2026-05-26
  - R-HB-ROOT-OBJECTIVE-AMEND-TO-35KG-2026-05-27
  - R-HB-SUCCESS-SEMANTICS-DEFINE-2026-05-27
  - R-HB-STRATEGIC-MAP-PROJECTION-CREATE-2026-05-27
  - R-HB-HORIZON-SELECT-2026-05-27
  - R-HB-H1-MINIMAL-DAILY-OPS-CORE-DEFINE-2026-05-27
  - R-HB-H1-PROGRAM-BLUEPRINT-DEFINE-2026-05-27
  - R-HB-H1-FIRST-PROGRAM-BLUEPRINT-CREATE-2026-05-27
  - R-HB-H1-NEXT-BOUNDED-RUN-SELECT-2026-05-27
candidate_receipts: []
rejected_receipts: []
receipt_storage_path: receipts/
rules:
  - no receipt -> no progress
  - receipt is candidate until Verify + Commit
```

Accepted receipts are listed only after Verify + Commit.

END_OF_FILE: directions/health-and-beauty/workflow/RECEIPTS_INDEX.md
