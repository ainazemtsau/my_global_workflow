---
artifact_control:
  namespace: direction_proof
  direction_id: workflow-governance
  artifact_type: receipt
  receipt_id: R-WG-COMPACT-PROJECT-INSTRUCTIONS-UI-001
  status: accepted
  owner: proof_carrying_workflow_os
---

# Receipt: Compact Project Instructions UI Payloads

```yaml
receipt_id: R-WG-COMPACT-PROJECT-INSTRUCTIONS-UI-001
source_obligation_id: O-WG-COMPACT-PROJECT-INSTRUCTIONS-UI
commit_scope: wg_workflow_setup_policy_scope
receipt_status: accepted
accepted_at: 2026-05-26
operator_mode: repository_maintenance
product_execution_allowed: false
legacy_import_performed: false
summary: >
  Accepts that ChatGPT Project Instructions UI payloads must be compact direct
  behavior instructions. The payload between BEGIN/END UI markers targets 6000
  characters or less and must not exceed 7500 characters. Detailed workflow
  rules remain in Project Files/Sources packs and setup docs.
accepted_claims:
  - project_instructions_ui_payload_budget_required
  - project_instructions_ui_payloads_are_compact_bootstrap_text
  - detailed_workflow_rules_belong_in_packs_or_setup_docs
  - separated_project_refresh_fields_preserved
evidence:
  - evidence_id: E-WG-COMPACT-UI-HANDOFF-001
    kind: current_human_input
    source_ref: current Codex handoff card CCH-WG-COMPACT-PROJECT-INSTRUCTIONS-UI-001
    summary: User requested repository maintenance only to compact ChatGPT Project Instructions UI payloads and preserve separated refresh fields.
  - evidence_id: E-WG-COMPACT-UI-PAYLOAD-COUNTS-001
    kind: validation_evidence
    source_ref: local payload character count validation
    summary: Universal Direction, Indie Game Development, and Workflow Governance UI payloads are all below the 6000 character target.
changed_policy_surfaces:
  - workflow/policies/08_CHATGPT_PROJECT_SETUP.md
  - workflow/project_setup/UNIVERSAL_DIRECTION_PROJECT_INSTALLER.md
  - workflow/project_setup/UNIVERSAL_DIRECTION_PROJECT_INSTRUCTIONS.md
  - workflow/project_setup/UNIVERSAL_PROJECT_FILES_MANIFEST_TEMPLATE.md
  - workflow/project_setup/PROJECT_SETUP_VALIDATION_CHECKLIST.md
refreshed_runtime_caches:
  - workflow/project_packs/UNIVERSAL_PROJECT_SHELL_PACK.md
  - workflow/project_packs/PROJECT_PACKS_INDEX.md
  - directions/workflow-governance/workflow/project_setup/CHATGPT_PROJECT_INSTRUCTIONS.md
  - directions/workflow-governance/workflow/project_setup/PROJECT_FILES_MANIFEST.md
  - directions/indie-game-development/workflow/project_setup/CHATGPT_PROJECT_INSTRUCTIONS.md
  - directions/indie-game-development/workflow/project_setup/PROJECT_FILES_MANIFEST.md
ui_payload_character_counts:
  workflow/project_setup/UNIVERSAL_DIRECTION_PROJECT_INSTRUCTIONS.md: 2741
  directions/indie-game-development/workflow/project_setup/CHATGPT_PROJECT_INSTRUCTIONS.md: 2784
  directions/workflow-governance/workflow/project_setup/CHATGPT_PROJECT_INSTRUCTIONS.md: 3343
scope_audit:
  target_obligation: O-WG-COMPACT-PROJECT-INSTRUCTIONS-UI
  in_scope_used:
    - Project Instructions UI payload budget
    - compact ordinary Direction Project Instructions pattern
    - compact Workflow Governance maintenance-console Project Instructions pattern
    - setup validation and manifest language
    - allowed runtime cache summaries
  necessary_dependencies:
    - active workflow setup policy
    - current Workflow Governance proof payload
    - current Workflow Governance and Indie Game Development project setup files
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
    - TRANSPORT_CORE_PACK.md changes
    - EXECUTION_HARNESS_PACK.md changes
    - docs changes
  explicit_decisions:
    - Target UI payloads at 6000 characters or less and require a 7500 character hard maximum.
    - Keep repository frontmatter, source notes, and END_OF_FILE markers outside UI payload markers.
    - Keep Governance Maintenance Pack content in Project Files/Sources instead of pasting it into Project Instructions UI.
  candidate_examples: []
  child_handoff_needed: false
  child_handoff_reason: null
  hidden_acceptance_check: pass
  one_obligation_scope: pass
parent_chat_continuity:
  same_parent_chat_continuation: true
  continuation_reason: >
    Repository maintenance closes the same bounded Project Instructions UI
    compaction problem and returns separated refresh instructions to the parent chat.
  next_chat_needed: false
  next_chat_reason: null
obligation_deltas:
  - obligation_id: O-WG-COMPACT-PROJECT-INSTRUCTIONS-UI
    type: workflow_setup_policy_patch
    status: satisfied
    satisfied_by_receipt: R-WG-COMPACT-PROJECT-INSTRUCTIONS-UI-001
ledger_delta:
  accepted_receipts_add:
    - R-WG-COMPACT-PROJECT-INSTRUCTIONS-UI-001
  accepted_claims_add:
    - project_instructions_ui_payload_budget_required
    - project_instructions_ui_payloads_are_compact_bootstrap_text
    - detailed_workflow_rules_belong_in_packs_or_setup_docs
    - separated_project_refresh_fields_preserved
forbidden_state_preserved:
  - no product execution
  - no merge to main
  - no roadmap
  - no Horizon
  - no Active Frontier
  - no legacy import
  - no Indie Game Development proof-state mutation
project_instruction_ui_update_required:
  - Paste the compact UI payload from directions/workflow-governance/workflow/project_setup/CHATGPT_PROJECT_INSTRUCTIONS.md into the Workflow Governance Project Instructions field.
  - Paste the compact UI payload from directions/indie-game-development/workflow/project_setup/CHATGPT_PROJECT_INSTRUCTIONS.md into the Indie Game Development Project Instructions field.
project_sources_files_refresh_required:
  - Refresh changed setup/packs only where currently uploaded.
request_only_sources_refresh_required:
  - workflow/project_packs/PROJECT_PACKS_INDEX.md only if already uploaded or used for setup inspection.
do_not_upload_as_project_file:
  - directions/workflow-governance/workflow/project_setup/CHATGPT_PROJECT_INSTRUCTIONS.md
  - directions/indie-game-development/workflow/project_setup/CHATGPT_PROJECT_INSTRUCTIONS.md
```

END_OF_FILE: directions/workflow-governance/workflow/receipts/R-WG-COMPACT-PROJECT-INSTRUCTIONS-UI-001.md
