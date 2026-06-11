---
artifact_control:
  namespace: direction_proof
  direction_id: workflow-governance
  artifact_type: receipt
  receipt_id: R-WG-PROJECT-SURFACE-SEPARATION-HARDEN-001
  status: accepted
  owner: proof_carrying_workflow_os
---

# Receipt: Project Surface Separation Hardening

```yaml
receipt_id: R-WG-PROJECT-SURFACE-SEPARATION-HARDEN-001
source_obligation_id: O-WG-PROJECT-SURFACE-SEPARATION-HARDEN
commit_scope: wg_workflow_setup_policy_scope
receipt_status: accepted
accepted_at: 2026-05-26
operator_mode: repository_maintenance
product_execution_allowed: false
legacy_import_performed: false
summary: >
  Accepts that ChatGPT Project Instructions UI and Project Files/Sources are
  distinct ChatGPT surfaces. Repository instruction source files are not default
  uploads; their UI payload is pasted into Project Instructions. Handoffs,
  manifests, setup docs, generated instructions, and refresh guidance must split
  instruction UI updates from Project Files/Sources refresh.
accepted_claims:
  - project_instruction_ui_is_distinct_from_project_files_sources
  - chatgpt_project_instructions_sources_are_ui_payload_sources_not_default_uploads
  - generated_project_instructions_must_be_ui_optimized
  - refresh_handoffs_must_split_instruction_ui_updates_from_project_sources_refresh
  - project_files_manifests_must_exclude_project_instruction_sources_from_default_upload_count
evidence:
  - evidence_id: E-WG-PROJECT-SURFACE-HANDOFF-001
    kind: current_human_input
    source_ref: current Codex handoff card CCH-WG-PROJECT-SURFACE-SEPARATION-HARDEN-001
    summary: User identified conflation between Project Instructions UI and Project Files/Sources and requested repository maintenance only.
  - evidence_id: E-WG-PROJECT-SURFACE-SETUP-DOCS-001
    kind: committed_setup_source
    source_ref: workflow/project_setup/UNIVERSAL_DIRECTION_PROJECT_INSTALLER.md
    summary: Setup model now says to paste instructions into the Project Instructions UI before uploading packs and Direction payload files as Project Files/Sources.
  - evidence_id: E-WG-PROJECT-SURFACE-HANDOFF-SCHEMA-001
    kind: committed_transport_source
    source_ref: workflow/transport/CODEX_COMMIT_HANDOFF_CARD.md
    summary: Handoff schema now uses separated refresh fields for instruction UI, Project Files/Sources, request-only sources, and do-not-upload instruction sources.
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
  - workflow/project_packs/UNIVERSAL_PROJECT_SHELL_PACK.md
  - workflow/project_packs/TRANSPORT_CORE_PACK.md
  - workflow/project_packs/PROJECT_PACKS_INDEX.md
  - directions/workflow-governance/workflow/project_setup/CHATGPT_PROJECT_INSTRUCTIONS.md
  - directions/workflow-governance/workflow/project_setup/PROJECT_FILES_MANIFEST.md
  - directions/indie-game-development/workflow/project_setup/CHATGPT_PROJECT_INSTRUCTIONS.md
  - directions/indie-game-development/workflow/project_setup/PROJECT_FILES_MANIFEST.md
scope_audit:
  target_obligation: O-WG-PROJECT-SURFACE-SEPARATION-HARDEN
  in_scope_used:
    - Project Instructions UI versus Project Files/Sources taxonomy
    - repository instruction source handling
    - default setup and refresh language
    - Codex handoff refresh fields
    - setup manifests and generated instruction payloads
  necessary_dependencies:
    - active workflow setup sources in WORKFLOW_SOURCE_OF_TRUTH.md
    - current Workflow Governance proof payload
    - current direction project setup files for Workflow Governance and Indie Game Development
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
    - Treat Project Instructions UI as a separate ChatGPT surface from uploaded Project Files/Sources.
    - Treat `CHATGPT_PROJECT_INSTRUCTIONS.md` files as UI payload sources, not default uploads.
    - Keep `PROJECT_PACKS_INDEX.md` request-only unless used for exact setup inspection.
  candidate_examples:
    - Workflow Governance and Indie Game Development generated setup files were refreshed as surface examples without changing Indie proof state.
  child_handoff_needed: false
  child_handoff_reason: null
  hidden_acceptance_check: pass
  one_obligation_scope: pass
parent_chat_continuity:
  same_parent_chat_continuation: true
  continuation_reason: >
    Repository maintenance closes the same bounded setup-surface problem and returns
    separated refresh instructions to the parent chat.
  next_chat_needed: false
  next_chat_reason: null
obligation_deltas:
  - obligation_id: O-WG-PROJECT-SURFACE-SEPARATION-HARDEN
    type: workflow_setup_policy_patch
    status: satisfied
    satisfied_by_receipt: R-WG-PROJECT-SURFACE-SEPARATION-HARDEN-001
ledger_delta:
  accepted_receipts_add:
    - R-WG-PROJECT-SURFACE-SEPARATION-HARDEN-001
  accepted_claims_add:
    - project_instruction_ui_is_distinct_from_project_files_sources
    - chatgpt_project_instructions_sources_are_ui_payload_sources_not_default_uploads
    - generated_project_instructions_must_be_ui_optimized
    - refresh_handoffs_must_split_instruction_ui_updates_from_project_sources_refresh
    - project_files_manifests_must_exclude_project_instruction_sources_from_default_upload_count
forbidden_state_preserved:
  - no product execution
  - no merge to main
  - no roadmap
  - no Horizon
  - no Active Frontier
  - no legacy import
  - no Indie Game Development proof-state mutation
project_instruction_ui_update_required:
  - Paste the updated UI instruction payload from directions/workflow-governance/workflow/project_setup/CHATGPT_PROJECT_INSTRUCTIONS.md into the ChatGPT Project Instructions field.
  - Paste the updated UI instruction payload from directions/indie-game-development/workflow/project_setup/CHATGPT_PROJECT_INSTRUCTIONS.md into the ChatGPT Project Instructions field.
project_sources_files_refresh_required:
  - directions/workflow-governance/workflow/LEDGER.md
  - directions/workflow-governance/workflow/OBLIGATIONS.md
  - directions/workflow-governance/workflow/RECEIPTS_INDEX.md
  - directions/workflow-governance/workflow/DASHBOARD.md
  - workflow/project_packs/UNIVERSAL_PROJECT_SHELL_PACK.md
  - workflow/project_packs/TRANSPORT_CORE_PACK.md
request_only_sources_refresh_required:
  - workflow/project_packs/PROJECT_PACKS_INDEX.md only if already uploaded or used for setup inspection.
do_not_upload_as_project_file:
  - directions/workflow-governance/workflow/project_setup/CHATGPT_PROJECT_INSTRUCTIONS.md
  - directions/indie-game-development/workflow/project_setup/CHATGPT_PROJECT_INSTRUCTIONS.md
```

END_OF_FILE: directions/workflow-governance/workflow/receipts/R-WG-PROJECT-SURFACE-SEPARATION-HARDEN-001.md
