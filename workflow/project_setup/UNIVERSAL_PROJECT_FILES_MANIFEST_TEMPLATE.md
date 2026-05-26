---
artifact_control:
  namespace: workflow_project_setup
  artifact_type: universal_project_files_manifest_template
  status: project_instruction_budget_hardened
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

```yaml
project_instruction_ui_update_required: true
do_not_upload_as_project_file:
  - directions/<direction-id>/<active-project-setup>/CHATGPT_PROJECT_INSTRUCTIONS.md
project_instruction_ui_payload_budget:
  hard_max_chars: 8000
  target_max_chars: 6500
  warning_threshold_chars: 7200
  measured_scope: trimmed payload between BEGIN/END UI payload markers
```

This source is not a Project File/Source and is excluded from the default upload count.

Do not paste repository wrapper metadata, marker comments, or `END_OF_FILE` into the Project Instructions UI.

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

Before paste, extract the UI payload between markers, trim leading/trailing whitespace, count characters, and fail setup validation if the payload exceeds 8,000 characters.

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
project_instruction_ui_payload_hard_max_chars: 8000
project_instruction_ui_payload_target_max_chars: 6500
```

END_OF_FILE: workflow/project_setup/UNIVERSAL_PROJECT_FILES_MANIFEST_TEMPLATE.md
