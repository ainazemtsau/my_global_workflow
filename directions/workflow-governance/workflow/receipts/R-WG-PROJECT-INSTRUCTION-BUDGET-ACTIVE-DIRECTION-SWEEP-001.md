---
artifact_control:
  namespace: direction_proof
  direction_id: workflow-governance
  artifact_type: receipt
  receipt_id: R-WG-PROJECT-INSTRUCTION-BUDGET-ACTIVE-DIRECTION-SWEEP-001
  status: accepted
  owner: proof_carrying_workflow_os
---

# Receipt: Active Direction Project Instructions Sweep

```yaml
receipt_id: R-WG-PROJECT-INSTRUCTION-BUDGET-ACTIVE-DIRECTION-SWEEP-001
source_obligation_id: O-WG-PROJECT-INSTRUCTION-BUDGET-ACTIVE-DIRECTION-SWEEP
predecessor_receipts:
  - R-WG-PROJECT-INSTRUCTION-BUDGET-HARDEN-001
  - R-WG-PROJECT-INSTRUCTION-BUDGET-RESIDUAL-SWEEP-001
status: accepted
operator: GovernancePatch / RepositoryMaintenancePlan
accepted_claims:
  - active_direction_project_instruction_sources_swept_for_payload_budget
  - solo_max_productive_project_instruction_source_budget_hardened
  - active_direction_manifests_exclude_instruction_sources_from_default_upload
summary: >
  Active Direction Project Instructions sources were scanned for Project Instructions
  UI payload budget compliance. Solo Max Productive was moved from the old setup model
  to the marked UI payload model, and its manifest now separates Project Instructions
  UI source from uploaded Project Files/Sources.
```

## Active Directions Scanned

- workflow-governance
- indie-game-development
- health-and-beauty
- solo-max-productive

## Active Generated Project Instructions Sources

```yaml
workflow-governance:
  path: directions/workflow-governance/workflow/project_setup/CHATGPT_PROJECT_INSTRUCTIONS.md
  classification: workflow_governance_special_payload
  payload_chars: 3401
  status: target
indie-game-development:
  path: directions/indie-game-development/workflow/project_setup/CHATGPT_PROJECT_INSTRUCTIONS.md
  classification: ordinary_direction_payload
  payload_chars: 3625
  status: target
health-and-beauty:
  path: directions/health-and-beauty/workflow/project_setup/CHATGPT_PROJECT_INSTRUCTIONS.md
  classification: ordinary_direction_payload
  payload_chars: 6363
  status: target
solo-max-productive:
  path: directions/solo-max-productive/setup/CHATGPT_PROJECT_INSTRUCTIONS.md
  classification: ordinary_direction_payload
  payload_chars: 3626
  status: target
```

## Scope

This receipt covers active Direction setup source compliance only.

It does not run product execution.

It does not mutate ordinary Direction proof-state files.

It leaves legacy/archive setup and old project files untouched.

## Validation Expectations

- Every active generated Project Instructions source has UI payload markers and budget metadata.
- Every active generated UI payload is below the 8,000-character hard max and at or below the 6,500-character target.
- Active Project Files manifests separate Project Instructions UI source from uploaded Project Files/Sources.
- Active Project Files manifests exclude `CHATGPT_PROJECT_INSTRUCTIONS.md` from default upload counts.
- No active generated setup source retains the exact old ambiguous refresh phrase.

## Ledger Delta

```yaml
accepted_receipts_add:
  - R-WG-PROJECT-INSTRUCTION-BUDGET-ACTIVE-DIRECTION-SWEEP-001
accepted_claims_add:
  - active_direction_project_instruction_sources_swept_for_payload_budget
  - solo_max_productive_project_instruction_source_budget_hardened
  - active_direction_manifests_exclude_instruction_sources_from_default_upload
obligation_updates:
  - obligation_id: O-WG-PROJECT-INSTRUCTION-BUDGET-ACTIVE-DIRECTION-SWEEP
    status: satisfied
    satisfied_by_receipt: R-WG-PROJECT-INSTRUCTION-BUDGET-ACTIVE-DIRECTION-SWEEP-001
    type: workflow_setup_policy_patch
    statement: >
      Sweep active Direction Project Instructions sources and manifests for
      Project Instructions UI payload budget compliance after the initial budget
      hardening and residual refresh wording sweep.
```

## Project Refresh Requirements

```yaml
project_instruction_ui_update_required:
  - directions/solo-max-productive/setup/CHATGPT_PROJECT_INSTRUCTIONS.md
project_instruction_ui_payload_char_counts:
  - directions/solo-max-productive/setup/CHATGPT_PROJECT_INSTRUCTIONS.md: 3626 chars, target
project_sources_files_refresh_required:
  - directions/solo-max-productive/setup/PROJECT_FILES_MANIFEST.md if uploaded
  - directions/health-and-beauty/workflow/project_setup/PROJECT_FILES_MANIFEST.md if uploaded
  - directions/workflow-governance/workflow/LEDGER.md
  - directions/workflow-governance/workflow/OBLIGATIONS.md
  - directions/workflow-governance/workflow/RECEIPTS_INDEX.md
  - directions/workflow-governance/workflow/DASHBOARD.md
request_only_sources_refresh_required:
  - workflow/project_packs/PROJECT_PACKS_INDEX.md only if already uploaded or needed for setup inspection
  - workflow/project_packs/EXECUTION_HARNESS_PACK.md remains request-only and unchanged
do_not_upload_as_project_file:
  - directions/solo-max-productive/setup/CHATGPT_PROJECT_INSTRUCTIONS.md
```

END_OF_FILE: directions/workflow-governance/workflow/receipts/R-WG-PROJECT-INSTRUCTION-BUDGET-ACTIVE-DIRECTION-SWEEP-001.md
