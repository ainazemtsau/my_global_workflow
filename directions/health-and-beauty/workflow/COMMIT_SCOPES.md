---
artifact_control:
  namespace: direction_proof
  direction_id: health-and-beauty
  artifact_type: commit_scopes
  status: m4_initialized_skeleton
  owner: proof_carrying_workflow_os
---

# Health and Beauty Commit Scopes

Commit scopes are runtime policy, not semantic primitives.

```yaml
commit_scopes:
  - scope_id: hb_root_scope
    controls:
      - root objective acceptance
      - human-owned direction decisions
      - hard constraints acceptance

  - scope_id: hb_strategy_scope
    controls:
      - strategic path receipts
      - opportunity receipts
      - assumptions
      - evidence gaps
      - strategic projections
    blocked_until:
      - root objective accepted

  - scope_id: hb_projection_scope
    controls:
      - dashboard projection
      - future strategic path map projection
      - future horizon projection
      - future active frontier view
    rule: projection updates require committed Ledger delta

  - scope_id: hb_execution_readiness_scope
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

END_OF_FILE: directions/health-and-beauty/workflow/COMMIT_SCOPES.md
