---
artifact_control:
  namespace: direction_proof
  direction_id: workflow-governance
  artifact_type: ledger
  status: root_objective_accepted
  owner: proof_carrying_workflow_os
---

# Workflow Governance Proof Ledger

```yaml
direction_id: workflow-governance
proof_state: root_objective_accepted
accepted_receipts:
  - R-WG-ROOT-OBJECTIVE-ATOMIC-RUN-001
accepted_claims:
  - workflow_governance_root_objective_accepted
  - atomic_run_hardening_is_primary_governance_goal
  - operator_independence_and_scope_triage_required
  - workflow_core_patch_requires_separate_admitted_obligation
  - codex_repository_maintenance_required_for_persistence
root_objective: >
  Maintain and harden the Workflow OS so every Direction chat follows proof-carrying,
  one-obligation-at-a-time execution: broad user input is preserved and normalized,
  but the operator remains scope-disciplined, evidence-driven, resistant to premature
  phase jumps, and unable to convert candidate context into accepted state without
  Receipt, Verify, and Commit.
open_obligations: directions/workflow-governance/workflow/OBLIGATIONS.md
commit_scopes: directions/workflow-governance/workflow/COMMIT_SCOPES.md
projections_state: none_available_until_receipts_committed
legacy_import_state: not_performed
legacy_state_authority: false
next_valid_run:
  - O-WG-ATOMIC-RUN-HARDEN
```

This Ledger records the accepted Workflow Governance root objective only.

Old `project_files/00-08` are not accepted proof state.

Any future import requires Legacy Import Receipt + Verify + Commit.

Only verified Receipts committed to this Ledger create accepted state for this Direction.

END_OF_FILE: directions/workflow-governance/workflow/LEDGER.md
