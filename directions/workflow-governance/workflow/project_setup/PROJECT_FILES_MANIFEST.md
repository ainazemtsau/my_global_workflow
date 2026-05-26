---
artifact_control:
  namespace: direction_workflow_project_setup
  direction_id: workflow-governance
  artifact_type: project_files_manifest
  project_name: "Workflow Governance"
  status: governance_maintenance_console_budget_hardened
  owner: workflow_os
---

# Workflow Governance Maintenance Console Project Surface Manifest

Project name: Workflow Governance

## Project Instructions UI Source

- `directions/workflow-governance/workflow/project_setup/CHATGPT_PROJECT_INSTRUCTIONS.md`

Paste the UI payload from this source into the ChatGPT Project Instructions field.

```yaml
project_instruction_ui_update_required: true
do_not_upload_as_project_file:
  - directions/workflow-governance/workflow/project_setup/CHATGPT_PROJECT_INSTRUCTIONS.md
project_instruction_ui_payload_budget:
  hard_max_chars: 8000
  target_max_chars: 6500
  warning_threshold_chars: 7200
  measured_scope: trimmed payload between BEGIN/END UI payload markers
```

This source is not a Project File/Source and is excluded from the default upload count.

Do not paste repository wrapper metadata, marker comments, or `END_OF_FILE` into the Project Instructions UI.

## Default Project Files/Sources

Upload only this minimal maintenance-console default set:

- `WORKFLOW_SOURCE_OF_TRUTH.md`
- `workflow/project_packs/GOVERNANCE_MAINTENANCE_PACK.md`
- `workflow/project_packs/PROJECT_PACKS_INDEX.md`
- `docs/CHATGPT_PROJECT_SETUP.md`
- `workflow/policies/08_CHATGPT_PROJECT_SETUP.md`

`PROJECT_PACKS_INDEX.md` is default only for this maintenance console because setup and pack inspection are part of its job. It remains request-only for ordinary Direction Workflow Projects.

## Request-Only Runtime Packs

Load these only when the current maintenance problem specifically requires their contents:

- `workflow/project_packs/WORKFLOW_BASE_PACK.md`
- `workflow/project_packs/TRANSPORT_CORE_PACK.md`
- `workflow/project_packs/EXECUTION_HARNESS_PACK.md`

Do not default-load `WORKFLOW_BASE_PACK` or `TRANSPORT_CORE_PACK` into the maintenance console.

Do not default-load `EXECUTION_HARNESS_PACK` into the maintenance console.

## Request-Only Canonical Areas

Load exact files from these areas only when needed for the current maintenance problem:

- `workflow/project_setup/*`
- `workflow/core/*`
- `workflow/policies/*`
- `workflow/transport/*`
- `workflow/execution/*`

## Request-Only Workflow Governance Direction Payload

Load live Direction payload files only when the current maintenance problem specifically concerns that live state:

- `directions/workflow-governance/workflow/LEDGER.md`
- `directions/workflow-governance/workflow/OBLIGATIONS.md`
- `directions/workflow-governance/workflow/RECEIPTS_INDEX.md`
- `directions/workflow-governance/workflow/COMMIT_SCOPES.md`
- `directions/workflow-governance/workflow/DASHBOARD.md`
- `directions/workflow-governance/workflow/MIGRATION_RECEIPT.md`

Do not default-load live Direction payload files.

Do not start with Dashboard/Obligations next valid run.

## Request-Only Exact Files

Load exact files needed for the current maintenance problem.

If a pack summary is insufficient or exact schema/source text is material, request or load the exact canonical source file listed in the relevant pack `source_manifest`.

## Do Not Load By Default

- live Direction payload files
- Dashboard/Obligations next-valid-run state
- ordinary Direction runtime packs
- old `proof_workflow` namespace
- old vNext-R workflow evidence from legacy branch/tag
- `directions/workflow-governance/project_files/**`
- `directions/workflow-governance/project_setup/**` as Project Files/Sources
- `directions/*/project_files/**`
- `directions/*/project_setup/**` as Project Files/Sources
- `directions/*/phases/**`
- `directions/*/execution_logs/**`
- `migration/**`
- product repo `.execution/**` unless operating inside the target product repo and explicitly requested
- old vNext-R runtime/stage/transport files
- raw chats, archive notes, or old rebuild packs

## Refresh Rule

- If Project Instructions source changes, paste the updated UI payload into the ChatGPT Project Instructions field.
- Before paste, extract the payload between markers, trim it, count characters, and fail validation if it exceeds 8,000 characters.
- Do not upload `project_setup/CHATGPT_PROJECT_INSTRUCTIONS.md` as a Project File/Source.
- If a default Project File/Source changes, refresh that uploaded Project File/Source.
- If a request-only file was uploaded for a specific maintenance problem and later changes, refresh it before relying on the uploaded copy.
- GitHub remains source of truth; Project Files/Sources are runtime cache and may be stale.
- Remove stale Project Files/Sources from the ChatGPT Project after this patch and re-upload only the new manifest defaults.

## Restoration Steps

1. Create or open the ChatGPT Project named "Workflow Governance".
2. Paste Project Instructions from `CHATGPT_PROJECT_INSTRUCTIONS.md` into the ChatGPT Project Instructions UI.
3. Remove stale Project Files/Sources from the old Direction Workflow runtime setup.
4. Upload only the five default Project Files/Sources listed above.
5. Do not upload live Direction payload files by default.
6. Do not upload `WORKFLOW_BASE_PACK`, `TRANSPORT_CORE_PACK`, or `EXECUTION_HARNESS_PACK` by default.
7. Load request-only files only for the exact current maintenance problem.
8. Run setup validation using `workflow/project_setup/PROJECT_SETUP_VALIDATION_CHECKLIST.md` if needed.

## Project Files Count Summary

```yaml
default_upload_count: 5
default_maintenance_pack_files: 2
default_setup_context_files: 3
project_instruction_sources_in_default_upload_count: 0
request_only_runtime_packs: 3
direction_payload_files_default_loaded: 0
project_instruction_ui_payload_hard_max_chars: 8000
project_instruction_ui_payload_target_max_chars: 6500
```

END_OF_FILE: directions/workflow-governance/workflow/project_setup/PROJECT_FILES_MANIFEST.md
