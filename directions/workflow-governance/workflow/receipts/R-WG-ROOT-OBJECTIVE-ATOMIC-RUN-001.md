---
artifact_control:
  namespace: direction_proof
  direction_id: workflow-governance
  artifact_type: receipt
  receipt_id: R-WG-ROOT-OBJECTIVE-ATOMIC-RUN-001
  status: accepted
  owner: proof_carrying_workflow_os
---

# Receipt: Workflow Governance Root Objective For Atomic Run Hardening

```yaml
receipt_id: R-WG-ROOT-OBJECTIVE-ATOMIC-RUN-001
source_obligation_id: O-WG-ROOT-OBJECTIVE-CONFIRM
commit_scope: wg_root_scope
receipt_status: accepted
accepted_at: 2026-05-26
operator_mode: repository_maintenance
product_execution_allowed: false
legacy_import_performed: false
summary: >
  Accepts the Workflow Governance root objective: maintain and harden Workflow OS
  so Direction chats operate one admitted Obligation at a time. Broad user input is
  preserved and normalized, but cannot cause phase drift, hidden acceptance,
  premature roadmap, strategy, or execution work, or multi-obligation scope creep.
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
minimal_success_semantics:
  - Direction chats operate one admitted Obligation at a time.
  - Broad user input is preserved and normalized without becoming accepted state.
  - Candidate context cannot create phase drift, hidden acceptance, premature roadmap,
    strategy, execution, or multi-obligation scope creep.
  - Workflow core hardening is admitted only through a separate material Obligation.
constraints_satisfied_by_root_receipt:
  - repository maintenance only
  - no product execution
  - no workflow-core policy patch in this commit
  - no roadmap, Horizon, Active Frontier, or legacy import introduced
  - Codex-backed repository maintenance required for persistence
obligation_deltas:
  - obligation_id: O-WG-ROOT-OBJECTIVE-CONFIRM
    status: satisfied
    satisfied_by_receipt: R-WG-ROOT-OBJECTIVE-ATOMIC-RUN-001
  - obligation_id: O-WG-SUCCESS-SEMANTICS-DEFINE
    status: satisfied_by_root_receipt
    satisfied_by_receipt: R-WG-ROOT-OBJECTIVE-ATOMIC-RUN-001
  - obligation_id: O-WG-CONSTRAINTS-DEFINE
    status: satisfied_by_root_receipt
    satisfied_by_receipt: R-WG-ROOT-OBJECTIVE-ATOMIC-RUN-001
  - obligation_id: O-WG-ATOMIC-RUN-HARDEN
    status: open
    type: workflow_policy_patch
    required_operator: GovernancePatch / RepositoryMaintenancePlan
    statement: >
      Harden Workflow OS with explicit Atomic Run / Single Responsibility,
      Operator Independence, Scope Triage, and child-handoff gating rules.
next_valid_run:
  - O-WG-ATOMIC-RUN-HARDEN
project_files_refresh_required:
  - Upload updated directions/workflow-governance/workflow/LEDGER.md,
    OBLIGATIONS.md, RECEIPTS_INDEX.md, and DASHBOARD.md to the Workflow
    Governance ChatGPT Project Files.
  - No shared project pack refresh is required because workflow/** and
    workflow/project_packs/** are unchanged.
```

END_OF_FILE: directions/workflow-governance/workflow/receipts/R-WG-ROOT-OBJECTIVE-ATOMIC-RUN-001.md
