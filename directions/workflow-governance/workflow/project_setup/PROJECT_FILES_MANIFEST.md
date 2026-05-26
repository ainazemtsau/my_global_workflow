---
artifact_control:
  namespace: direction_workflow_project_setup
  direction_id: workflow-governance
  artifact_type: project_files_manifest
  project_name: "Workflow Governance"
  status: governance_maintenance_console
  owner: workflow_os
---

# Workflow Governance Maintenance Console Project Files Manifest

Project name: Workflow Governance

Project Instructions source:

- `directions/workflow-governance/workflow/project_setup/CHATGPT_PROJECT_INSTRUCTIONS.md`

## Default Project Files

Upload only this minimal maintenance-console default set:

- `WORKFLOW_SOURCE_OF_TRUTH.md`
- `workflow/project_packs/GOVERNANCE_MAINTENANCE_PACK.md`
- `workflow/project_packs/PROJECT_PACKS_INDEX.md`
- `docs/CHATGPT_PROJECT_SETUP.md`
- `workflow/policies/08_CHATGPT_PROJECT_SETUP.md`

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
- `directions/workflow-governance/project_setup/**`
- `directions/*/project_files/**`
- `directions/*/project_setup/**`
- `directions/*/phases/**`
- `directions/*/execution_logs/**`
- `migration/**`
- product repo `.execution/**` unless operating inside the target product repo and explicitly requested
- old vNext-R runtime/stage/transport files
- raw chats, archive notes, or old rebuild packs

## Refresh Rule

- If a default Project File changes, refresh that uploaded Project File.
- If a request-only file was uploaded for a specific maintenance problem and later changes, refresh it before relying on the uploaded copy.
- GitHub remains source of truth; Project Files are runtime cache and may be stale.
- Remove stale Project Files from the ChatGPT Project after this patch and re-upload only the new manifest defaults.

## Restoration Steps

1. Create or open the ChatGPT Project named "Workflow Governance".
2. Paste Project Instructions from `CHATGPT_PROJECT_INSTRUCTIONS.md`.
3. Remove stale Project Files from the old Direction Workflow runtime setup.
4. Upload only the five default Project Files listed above.
5. Do not upload live Direction payload files by default.
6. Do not upload `WORKFLOW_BASE_PACK`, `TRANSPORT_CORE_PACK`, or `EXECUTION_HARNESS_PACK` by default.
7. Load request-only files only for the exact current maintenance problem.
8. Run setup validation using `workflow/project_setup/PROJECT_SETUP_VALIDATION_CHECKLIST.md` if needed.

## Project Files Count Summary

```yaml
default_upload_count: 5
default_maintenance_pack_files: 2
default_setup_context_files: 3
request_only_runtime_packs: 3
direction_payload_files_default_loaded: 0
```

END_OF_FILE: directions/workflow-governance/workflow/project_setup/PROJECT_FILES_MANIFEST.md
