---
artifact_control:
  namespace: workflow_project_setup
  artifact_type: universal_project_files_manifest_template
  status: u3_pack_model
  owner: workflow_os
---

# Universal Project Files Manifest Template

Project name:

```text
<DIRECTION_DISPLAY_NAME>
```

Project Instructions source:

- `directions/<direction-id>/proof/project_setup/CHATGPT_PROJECT_INSTRUCTIONS.md`
- or universal installer instructions generated from `project_setup/UNIVERSAL_DIRECTION_PROJECT_INSTRUCTIONS.md`

## Default Shared Packs

- `project_packs/UNIVERSAL_PROJECT_SHELL_PACK.md`
- `project_packs/WORKFLOW_BASE_PACK.md`
- `project_packs/TRANSPORT_CORE_PACK.md`

## Direction Payload

- `directions/<direction-id>/proof/LEDGER.md`
- `directions/<direction-id>/proof/OBLIGATIONS.md`
- `directions/<direction-id>/proof/RECEIPTS_INDEX.md`
- `directions/<direction-id>/proof/COMMIT_SCOPES.md`
- `directions/<direction-id>/proof/DASHBOARD.md`
- `directions/<direction-id>/proof/MIGRATION_RECEIPT.md`

## Request-Only Capability Packs

- `project_packs/EXECUTION_HARNESS_PACK.md`

Load request-only capability packs only when an admitted task needs them.

## Request-Only Exact Canonical Files

If a pack summary is insufficient or exact schema/source text is material, request or load the exact canonical source file listed in the relevant pack `source_manifest`.

## Do Not Load By Default

- `workflow/**`
- `directions/<direction-id>/project_files/**`
- `directions/<direction-id>/project_setup/**`
- `directions/*/project_files/**`
- `directions/*/project_setup/**`
- `migration/**`
- product repo `.execution/**` unless it is in the target product repo and explicitly relevant
- old vNext-R runtime, stage, or transport files
- raw chats, archive notes, or old rebuild packs

## Refresh Rule

Project Files are runtime cache.

If any pack `source_manifest` file changes, regenerate or refresh that pack and replace the uploaded Project File before the next material run that depends on it.

If any Direction payload file changes, replace that uploaded Direction payload Project File before the next material run that depends on it.

## Setup Validation

Run `project_setup/PROJECT_SETUP_VALIDATION_CHECKLIST.md` after creating or refreshing a Project.

## Project Files Count Summary

```yaml
default_upload_count: 9
default_shared_packs: 3
direction_payload_files: 6
request_only_execution_pack: 1
```

END_OF_FILE: project_setup/UNIVERSAL_PROJECT_FILES_MANIFEST_TEMPLATE.md
