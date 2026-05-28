---
artifact_control:
  namespace: direction_proof
  direction_id: workflow-governance
  artifact_type: commit_scopes
  status: active_payload_layout_aligned
  owner: proof_carrying_workflow_os
---

# Workflow Governance Commit Scopes

Commit scopes are runtime policy, not semantic primitives.

```yaml
commit_scopes:
  - scope_id: wg_root_scope
    controls:
      - root objective acceptance
      - human-owned direction decisions
      - hard constraints acceptance

  - scope_id: wg_workflow_policy_scope
    controls:
      - Workflow OS runtime protocol maintenance
      - Workflow OS policy maintenance
      - core invariant maintenance
      - transport card schema maintenance
      - project setup instruction refresh
      - project pack refresh
      - Workflow Governance proof-state maintenance for policy receipts
    blocked_actions:
      - product execution
      - roadmap creation
      - Horizon selection
      - Active Frontier selection
      - legacy import
      - unrelated Direction proof-state mutation

  - scope_id: wg_strategy_scope
    controls:
      - strategic path receipts
      - opportunity receipts
      - assumptions
      - evidence gaps
      - strategic projections
    blocked_until:
      - root objective accepted

  - scope_id: wg_projection_scope
    controls:
      - dashboard projection
      - future strategic path map projection
      - future horizon projection
      - future active frontier view
    rule: projection updates require committed Ledger delta

  - scope_id: wg_execution_readiness_scope
    controls:
      - future execution readiness obligations
      - future Codex readiness receipts
    blocked_until:
      - root objective accepted
      - strategy receipts accepted
      - execution-ready precondition receipts accepted
```

Commit Scope is not a sixth semantic primitive.

Commit Scope does not create truth.

Only committed Receipts update Ledger state.

END_OF_FILE: directions/workflow-governance/workflow/COMMIT_SCOPES.md
