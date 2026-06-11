---
artifact_control:
  namespace: direction_proof
  direction_id: workflow-governance
  artifact_type: receipt
  receipt_id: R-WG-PROJECT-INSTRUCTION-BUDGET-RESIDUAL-SWEEP-001
  status: accepted
  owner: proof_carrying_workflow_os
---

# Receipt: Project Instruction Budget Residual Sweep

```yaml
receipt_id: R-WG-PROJECT-INSTRUCTION-BUDGET-RESIDUAL-SWEEP-001
source_obligation_id: O-WG-PROJECT-INSTRUCTION-BUDGET-RESIDUAL-SWEEP
predecessor_receipt: R-WG-PROJECT-INSTRUCTION-BUDGET-HARDEN-001
status: accepted
operator: GovernancePatch / RepositoryMaintenancePlan
accepted_claims:
  - residual_project_refresh_wording_swept_from_active_codex_and_workflow_surfaces
  - codex_handoffs_require_separated_project_refresh_fields
  - instruction_source_changes_require_payload_char_counts
summary: >
  Active workflow and Codex-facing files no longer use old ambiguous
  project-refresh wording as the controlling handoff rule.
  They require separated project refresh fields and payload character counts when
  Project Instructions UI sources change.
```

## Scope

This receipt covers a narrow residual wording sweep after Project Instructions UI payload budget hardening.

It changes only the Health and Beauty Project Instructions UI payload wrapper/refresh wording under the conditional marker cleanup rule.

It does not run product execution.

It does not mutate Indie Game Development proof state.

## Changed Surfaces

- Root and Workflow Governance AGENTS wording.
- Active transport policy and core invariant wording.
- Codex/setup-facing documentation and migration checklist wording.
- Affected project packs: Governance Maintenance, Workflow Base, Transport Core, and Project Packs Index.
- Conditional Health and Beauty Project Instructions UI source marker/writing cleanup.
- Workflow Governance proof files and this receipt.

## Validation Expectations

- Active Codex-facing refresh wording uses separated project refresh requirements.
- Required separated fields remain:
  - `project_instruction_ui_update_required`
  - `project_instruction_ui_payload_char_counts`
  - `project_sources_files_refresh_required`
  - `request_only_sources_refresh_required`
  - `do_not_upload_as_project_file`
- Project Instructions source changes require measured UI payload character counts.
- Project Instruction source files remain excluded from uploaded Project Files/Sources.
- No forbidden path changes are introduced.

## Ledger Delta

```yaml
accepted_receipts_add:
  - R-WG-PROJECT-INSTRUCTION-BUDGET-RESIDUAL-SWEEP-001
accepted_claims_add:
  - residual_project_refresh_wording_swept_from_active_codex_and_workflow_surfaces
  - codex_handoffs_require_separated_project_refresh_fields
  - instruction_source_changes_require_payload_char_counts
obligation_updates:
  - obligation_id: O-WG-PROJECT-INSTRUCTION-BUDGET-RESIDUAL-SWEEP
    status: satisfied
    satisfied_by_receipt: R-WG-PROJECT-INSTRUCTION-BUDGET-RESIDUAL-SWEEP-001
    type: workflow_setup_policy_patch
    statement: >
      Sweep active workflow/Codex-facing files for residual ambiguous Project Files
      refresh wording after Project Instructions UI payload budget hardening.
```

## Project Refresh Requirements

```yaml
project_instruction_ui_update_required:
  - directions/health-and-beauty/workflow/project_setup/CHATGPT_PROJECT_INSTRUCTIONS.md
project_instruction_ui_payload_char_counts:
  - directions/health-and-beauty/workflow/project_setup/CHATGPT_PROJECT_INSTRUCTIONS.md: 6363 chars, target
project_sources_files_refresh_required:
  - AGENTS.md if uploaded
  - directions/workflow-governance/AGENTS.md if uploaded
  - directions/workflow-governance/README.md if uploaded
  - directions/workflow-governance/workflow/LEDGER.md
  - directions/workflow-governance/workflow/OBLIGATIONS.md
  - directions/workflow-governance/workflow/RECEIPTS_INDEX.md
  - directions/workflow-governance/workflow/DASHBOARD.md
  - workflow/project_packs/GOVERNANCE_MAINTENANCE_PACK.md
  - workflow/project_packs/WORKFLOW_BASE_PACK.md
  - workflow/project_packs/TRANSPORT_CORE_PACK.md
  - workflow/project_packs/PROJECT_PACKS_INDEX.md where uploaded
request_only_sources_refresh_required:
  - workflow/project_packs/PROJECT_PACKS_INDEX.md only if already uploaded or needed for setup inspection
  - workflow/project_packs/EXECUTION_HARNESS_PACK.md remains request-only and unchanged
do_not_upload_as_project_file:
  - directions/workflow-governance/workflow/project_setup/CHATGPT_PROJECT_INSTRUCTIONS.md
  - directions/indie-game-development/workflow/project_setup/CHATGPT_PROJECT_INSTRUCTIONS.md
  - directions/health-and-beauty/workflow/project_setup/CHATGPT_PROJECT_INSTRUCTIONS.md
```

END_OF_FILE: directions/workflow-governance/workflow/receipts/R-WG-PROJECT-INSTRUCTION-BUDGET-RESIDUAL-SWEEP-001.md
