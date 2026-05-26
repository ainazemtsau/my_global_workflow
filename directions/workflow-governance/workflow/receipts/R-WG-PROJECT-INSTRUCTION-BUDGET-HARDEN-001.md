---
artifact_control:
  namespace: direction_proof
  direction_id: workflow-governance
  artifact_type: receipt
  receipt_id: R-WG-PROJECT-INSTRUCTION-BUDGET-HARDEN-001
  status: accepted
  owner: proof_carrying_workflow_os
---

# Receipt: Project Instructions UI Payload Budget Hardening

```yaml
receipt_id: R-WG-PROJECT-INSTRUCTION-BUDGET-HARDEN-001
source_obligation_id: O-WG-PROJECT-INSTRUCTION-BUDGET-HARDEN
commit_scope: wg_workflow_setup_policy_scope
receipt_status: accepted
accepted_at: 2026-05-26
operator_mode: repository_maintenance
product_execution_allowed: false
legacy_import_performed: false
summary: >
  Accepts that ChatGPT Project Instructions UI payloads must be compact,
  behavior-oriented, paste-ready, and below the ChatGPT Web UI practical limit.
  Workflow details belong in canonical files and uploaded packs/files, not in
  oversized UI instructions.
accepted_claims:
  - project_instructions_ui_payload_hard_max_8000_chars
  - project_instructions_ui_payload_target_max_6500_chars
  - generated_project_instructions_must_be_compact_behavioral_payloads
  - workflow_details_belong_in_canonical_files_and_packs_not_oversized_ui_instructions
  - instruction_payload_length_validation_required
payload_budget:
  hard_max_chars: 8000
  target_max_chars: 6500
  warning_threshold_chars: 7200
  measured_scope: trimmed content between BEGIN_CHATGPT_PROJECT_INSTRUCTIONS_UI_PAYLOAD and END_CHATGPT_PROJECT_INSTRUCTIONS_UI_PAYLOAD
payload_counts:
  - path: workflow/project_setup/UNIVERSAL_DIRECTION_PROJECT_INSTRUCTIONS.md
    chars: 3222
    status: target
  - path: directions/workflow-governance/workflow/project_setup/CHATGPT_PROJECT_INSTRUCTIONS.md
    chars: 3363
    status: target
  - path: directions/indie-game-development/workflow/project_setup/CHATGPT_PROJECT_INSTRUCTIONS.md
    chars: 3588
    status: target
evidence:
  - evidence_id: E-WG-INSTRUCTION-BUDGET-HANDOFF-001
    kind: current_human_input
    source_ref: current Codex handoff card CCH-WG-PROJECT-INSTRUCTION-BUDGET-HARDEN-001
    summary: User reported that generated Project Instructions UI payloads exceeded the ChatGPT Web UI field limit.
  - evidence_id: E-WG-INSTRUCTION-BUDGET-COUNTS-001
    kind: repository_readback
    source_ref: generated UI payload marker extraction
    summary: Universal ordinary, Workflow Governance, and Indie Game Development UI payloads are all at or below the 6,500-character target.
changed_policy_surfaces:
  - docs/CHATGPT_PROJECT_SETUP.md
  - workflow/policies/08_CHATGPT_PROJECT_SETUP.md
  - workflow/policies/12_HUMAN_FACING_RUN_CLOSURE_POLICY.md
  - workflow/project_setup/UNIVERSAL_DIRECTION_PROJECT_INSTALLER.md
  - workflow/project_setup/UNIVERSAL_DIRECTION_PROJECT_INSTRUCTIONS.md
  - workflow/project_setup/UNIVERSAL_PROJECT_FILES_MANIFEST_TEMPLATE.md
  - workflow/project_setup/PROJECT_SETUP_VALIDATION_CHECKLIST.md
  - workflow/transport/CODEX_COMMIT_HANDOFF_CARD.md
refreshed_runtime_caches:
  - workflow/project_packs/GOVERNANCE_MAINTENANCE_PACK.md
  - workflow/project_packs/UNIVERSAL_PROJECT_SHELL_PACK.md
  - workflow/project_packs/TRANSPORT_CORE_PACK.md
  - workflow/project_packs/PROJECT_PACKS_INDEX.md
  - directions/workflow-governance/workflow/project_setup/CHATGPT_PROJECT_INSTRUCTIONS.md
  - directions/workflow-governance/workflow/project_setup/PROJECT_FILES_MANIFEST.md
  - directions/indie-game-development/workflow/project_setup/CHATGPT_PROJECT_INSTRUCTIONS.md
  - directions/indie-game-development/workflow/project_setup/PROJECT_FILES_MANIFEST.md
scope_audit:
  target_obligation: O-WG-PROJECT-INSTRUCTION-BUDGET-HARDEN
  in_scope_used:
    - Project Instructions UI hard max, target, and warning threshold
    - compact ordinary Direction payload
    - compact Workflow Governance Maintenance Console payload
    - payload extraction and character-count validation
    - Codex handoff return fields for payload counts
  necessary_dependencies:
    - R-WG-PROJECT-SURFACE-SEPARATION-HARDEN-001
    - active project setup sources
    - generated Governance and Indie Project Instructions sources
  parked_residual_context: []
  proposed_residual_obligations: []
  blocked_or_forbidden:
    - product execution
    - merge to main
    - Indie Game Development proof-state mutation
    - workflow/core changes
    - workflow/invariants changes
    - workflow/execution changes
    - WORKFLOW_BASE_PACK.md changes
    - EXECUTION_HARNESS_PACK.md changes
  explicit_decisions:
    - Hard max for generated Project Instructions UI payloads is 8,000 characters.
    - Target max for generated Project Instructions UI payloads is 6,500 characters.
    - Warning threshold is 7,200 characters.
    - UI payloads must be compact behavior instructions and must rely on canonical files/packs for detail.
  child_handoff_needed: false
  child_handoff_reason: null
  hidden_acceptance_check: pass
  one_obligation_scope: pass
obligation_deltas:
  - obligation_id: O-WG-PROJECT-INSTRUCTION-BUDGET-HARDEN
    type: workflow_setup_policy_patch
    status: satisfied
    satisfied_by_receipt: R-WG-PROJECT-INSTRUCTION-BUDGET-HARDEN-001
ledger_delta:
  accepted_receipts_add:
    - R-WG-PROJECT-INSTRUCTION-BUDGET-HARDEN-001
  accepted_claims_add:
    - project_instructions_ui_payload_hard_max_8000_chars
    - project_instructions_ui_payload_target_max_6500_chars
    - generated_project_instructions_must_be_compact_behavioral_payloads
    - workflow_details_belong_in_canonical_files_and_packs_not_oversized_ui_instructions
    - instruction_payload_length_validation_required
forbidden_state_preserved:
  - no product execution
  - no merge to main
  - no roadmap
  - no Horizon
  - no Active Frontier
  - no legacy import
  - no Indie Game Development proof-state mutation
project_instruction_ui_update_required:
  - Paste only the updated UI payload between markers from directions/workflow-governance/workflow/project_setup/CHATGPT_PROJECT_INSTRUCTIONS.md into the ChatGPT Project Instructions field.
  - Paste only the updated UI payload between markers from directions/indie-game-development/workflow/project_setup/CHATGPT_PROJECT_INSTRUCTIONS.md into the ChatGPT Project Instructions field.
project_sources_files_refresh_required:
  - Refresh changed loaded setup sources/packs if uploaded.
  - Refresh changed shared packs where uploaded: GOVERNANCE_MAINTENANCE_PACK.md, UNIVERSAL_PROJECT_SHELL_PACK.md, TRANSPORT_CORE_PACK.md, PROJECT_PACKS_INDEX.md as applicable.
request_only_sources_refresh_required:
  - PROJECT_PACKS_INDEX.md only if already uploaded or needed for setup inspection in ordinary Direction Projects.
  - EXECUTION_HARNESS_PACK.md remains request-only and unchanged.
do_not_upload_as_project_file:
  - directions/workflow-governance/workflow/project_setup/CHATGPT_PROJECT_INSTRUCTIONS.md
  - directions/indie-game-development/workflow/project_setup/CHATGPT_PROJECT_INSTRUCTIONS.md
```

END_OF_FILE: directions/workflow-governance/workflow/receipts/R-WG-PROJECT-INSTRUCTION-BUDGET-HARDEN-001.md
