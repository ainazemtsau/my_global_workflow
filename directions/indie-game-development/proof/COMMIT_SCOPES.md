---
artifact_control:
  namespace: direction_proof
  direction_id: indie-game-development
  artifact_type: commit_scope_policy_storage
  status: initialized_skeleton
  owner: proof_carrying_workflow_os
---

# Indie Game Development Commit Scopes

## Policy Boundary

Commit Scope is runtime policy, not a sixth semantic primitive.

Commit Scope does not create truth.

Only committed Receipts update Ledger state.

## Initial Commit Scopes

### idg_root_scope

```yaml
commit_scope_id: idg_root_scope
controls:
  - root objective acceptance
  - human-owned direction decisions
  - hard constraints acceptance
blocked_until: []
rule: Changes require verified Receipts and Commit.
```

### idg_strategy_scope

```yaml
commit_scope_id: idg_strategy_scope
controls:
  - strategic path receipts
  - opportunity receipts
  - assumptions
  - evidence gaps
  - strategic projections
blocked_until:
  - root objective accepted
rule: Strategy cannot be committed before root objective acceptance.
```

### idg_projection_scope

```yaml
commit_scope_id: idg_projection_scope
controls:
  - dashboard projection
  - future strategic path map projection
  - future horizon projection
  - future active frontier view
blocked_until: []
rule: projection updates require committed Ledger delta
```

### idg_execution_readiness_scope

```yaml
commit_scope_id: idg_execution_readiness_scope
controls:
  - future execution readiness obligations
  - future Codex readiness receipts
blocked_until:
  - root objective accepted
  - strategy receipts accepted
  - execution-ready precondition receipts accepted
rule: Execution readiness cannot admit product/project execution by itself.
```

END_OF_FILE: directions/indie-game-development/proof/COMMIT_SCOPES.md
