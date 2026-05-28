---
artifact_control:
  namespace: direction_proof
  direction_id: health-and-beauty
  artifact_type: skeleton_migration_receipt
  status: m4_initialized_skeleton
  owner: proof_carrying_workflow_os
---

# Health and Beauty Migration Receipt

This file is a skeleton migration receipt, not a legacy import receipt.

```yaml
migration_gate: M4 skeleton only
legacy_import_performed: false
imported_claims: []
accepted_legacy_claims: []
rejected_legacy_claims: []
contamination_check:
  old_direction_map_as_truth: false
  old_active_goal_as_obligation: false
  old_current_phase_as_ledger_state: false
  old_portfolio_queue_as_backlog: false
future_legacy_import_requires:
  - admitted LegacyImport obligation
  - Legacy Import Receipt
  - Verify
  - Commit
```

No old state is imported by this skeleton.

END_OF_FILE: directions/health-and-beauty/workflow/MIGRATION_RECEIPT.md
