---
artifact_control:
  namespace: direction_proof
  direction_id: workflow-governance
  artifact_type: ledger
  status: project_instruction_budget_residual_sweep
  owner: proof_carrying_workflow_os
---

# Workflow Governance Proof Ledger

```yaml
direction_id: workflow-governance
proof_state: project_instruction_budget_residual_sweep
accepted_receipts:
  - R-WG-ROOT-OBJECTIVE-ATOMIC-RUN-001
  - R-WG-ATOMIC-RUN-HARDEN-001
  - R-WG-PROJECT-SURFACE-SEPARATION-HARDEN-001
  - R-WG-PROJECT-INSTRUCTION-BUDGET-HARDEN-001
  - R-WG-PROJECT-INSTRUCTION-BUDGET-RESIDUAL-SWEEP-001
accepted_claims:
  - workflow_governance_root_objective_accepted
  - atomic_run_hardening_is_primary_governance_goal
  - operator_independence_and_scope_triage_required
  - workflow_core_patch_requires_separate_admitted_obligation
  - codex_repository_maintenance_required_for_persistence
  - atomic_run_single_responsibility_hardened
  - operator_independence_hardened
  - scope_triage_before_material_work_required
  - parent_chat_problem_closure_required
  - child_handoff_gated_by_current_obligation_need
  - receipt_scope_audit_required
  - same_parent_chat_default_for_codex_results
  - project_instruction_ui_is_distinct_from_project_files_sources
  - chatgpt_project_instructions_sources_are_ui_payload_sources_not_default_uploads
  - generated_project_instructions_must_be_ui_optimized
  - refresh_handoffs_must_split_instruction_ui_updates_from_project_sources_refresh
  - project_files_manifests_must_exclude_project_instruction_sources_from_default_upload_count
  - project_instructions_ui_payload_hard_max_8000_chars
  - project_instructions_ui_payload_target_max_6500_chars
  - generated_project_instructions_must_be_compact_behavioral_payloads
  - workflow_details_belong_in_canonical_files_and_packs_not_oversized_ui_instructions
  - instruction_payload_length_validation_required
  - residual_project_refresh_wording_swept_from_active_codex_and_workflow_surfaces
  - codex_handoffs_require_separated_project_refresh_fields
  - instruction_source_changes_require_payload_char_counts
root_objective: >
  Maintain and harden the Workflow OS so every Direction chat follows proof-carrying,
  one-obligation-at-a-time execution: broad user input is preserved and normalized,
  but the operator remains scope-disciplined, evidence-driven, resistant to premature
  phase jumps, and unable to convert candidate context into accepted state without
  Receipt, Verify, and Commit.
open_obligations: directions/workflow-governance/workflow/OBLIGATIONS.md
commit_scopes: directions/workflow-governance/workflow/COMMIT_SCOPES.md
projections_state: dashboard_updated_from_accepted_receipts
legacy_import_state: not_performed
legacy_state_authority: false
next_valid_run: []
```

This Ledger records the accepted Workflow Governance root objective, Atomic Run hardening, Project Surface Separation hardening, Project Instructions UI payload budget hardening, and residual project refresh wording sweep.

Old `project_files/00-08` are not accepted proof state.

Any future import requires Legacy Import Receipt + Verify + Commit.

Only verified Receipts committed to this Ledger create accepted state for this Direction.

END_OF_FILE: directions/workflow-governance/workflow/LEDGER.md
