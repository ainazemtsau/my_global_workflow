---
artifact_control:
  namespace: workflow_project_setup
  artifact_type: universal_project_files_manifest_template
  status: u3_pack_model
  owner: workflow_os
---

# Universal Project Surface Manifest Template

Project name:

```text
<DIRECTION_DISPLAY_NAME>
```

## Project Instructions UI Source

- `directions/<direction-id>/<active-project-setup>/CHATGPT_PROJECT_INSTRUCTIONS.md`
- or universal installer instructions generated from `workflow/project_setup/UNIVERSAL_DIRECTION_PROJECT_INSTRUCTIONS.md`

Paste the UI payload from this source into the ChatGPT Project Instructions field.

The UI payload is compact bootstrap behavior text. Target 6000 characters or less between BEGIN/END UI payload markers; hard maximum 7500 characters. Do not paste repository frontmatter, source notes, or `END_OF_FILE` into the Project Instructions UI.

```yaml
project_instruction_ui_update_required: true
do_not_upload_as_project_file:
  - directions/<direction-id>/<active-project-setup>/CHATGPT_PROJECT_INSTRUCTIONS.md
```

This source is not a Project File/Source and is excluded from the default upload count.

## Default Shared Packs

- `workflow/project_packs/UNIVERSAL_PROJECT_SHELL_PACK.md`
- `workflow/project_packs/WORKFLOW_BASE_PACK.md`
- `workflow/project_packs/TRANSPORT_CORE_PACK.md`

## Direction Payload

- `directions/<direction-id>/<active-direction-state>/LEDGER.md`
- `directions/<direction-id>/<active-direction-state>/OBLIGATIONS.md`
- `directions/<direction-id>/<active-direction-state>/RECEIPTS_INDEX.md`
- `directions/<direction-id>/<active-direction-state>/COMMIT_SCOPES.md`
- `directions/<direction-id>/<active-direction-state>/DASHBOARD.md`
- `directions/<direction-id>/<active-direction-state>/MIGRATION_RECEIPT.md`

## Request-Only Capability Packs

- `workflow/project_packs/EXECUTION_HARNESS_PACK.md`
- `workflow/project_packs/PROJECT_PACKS_INDEX.md`

Load request-only capability packs only when an admitted task needs them.

## Request-Only Exact Canonical Files

If a pack summary is insufficient or exact schema/source text is material, request or load the exact canonical source file listed in the relevant pack `source_manifest`.

## Do Not Load By Default

- `workflow/**`
- `directions/<direction-id>/project_files/**`
- `directions/<direction-id>/project_setup/**` as Project Files/Sources
- `directions/*/project_files/**`
- `directions/*/project_setup/**` as Project Files/Sources
- `migration/**`
- product repo `.execution/**` unless it is in the target product repo and explicitly relevant
- old vNext-R runtime, stage, or transport files
- raw chats, archive notes, or old rebuild packs

## Refresh Rule

Project Files/Sources are runtime cache.

If the Project Instructions source changes, paste the updated UI payload into the ChatGPT Project Instructions field and do not upload the source file as a Project File/Source.

If any pack `source_manifest` file changes, regenerate or refresh that pack and replace the uploaded Project File/Source before the next material run that depends on it.

If any Direction payload file changes, replace that uploaded Direction payload Project File/Source before the next material run that depends on it.

Refresh handoffs must use separate fields:

```yaml
project_instruction_ui_update_required: []
project_sources_files_refresh_required: []
request_only_sources_refresh_required: []
do_not_upload_as_project_file: []
```

## Setup Validation

Run `workflow/project_setup/PROJECT_SETUP_VALIDATION_CHECKLIST.md` after creating or refreshing a Project.

## Project Files Count Summary

```yaml
default_upload_count: 9
default_shared_packs: 3
direction_payload_files: 6
project_instruction_sources_in_default_upload_count: 0
request_only_execution_pack: 1
```

END_OF_FILE: workflow/project_setup/UNIVERSAL_PROJECT_FILES_MANIFEST_TEMPLATE.md
