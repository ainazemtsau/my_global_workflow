---
artifact_control:
  namespace: direction_workflow_project_setup
  direction_id: indie-game-development
  artifact_type: project_files_manifest
  project_name: "Indie Game Development"
  status: u3_pack_model
  owner: workflow_os
---

# Indie Game Development — Workflow Project Surface Manifest

Project name: Indie Game Development

## Project Instructions UI Source

- `directions/indie-game-development/workflow/project_setup/CHATGPT_PROJECT_INSTRUCTIONS.md`

Paste the UI payload from this source into the ChatGPT Project Instructions field.

```yaml
project_instruction_ui_update_required: true
do_not_upload_as_project_file:
  - directions/indie-game-development/workflow/project_setup/CHATGPT_PROJECT_INSTRUCTIONS.md
```

This source is not a Project File/Source and is excluded from the default upload count.

## Default Shared Project Packs

- `workflow/project_packs/UNIVERSAL_PROJECT_SHELL_PACK.md`
- `workflow/project_packs/WORKFLOW_BASE_PACK.md`
- `workflow/project_packs/TRANSPORT_CORE_PACK.md`

## Direction Payload

- `directions/indie-game-development/workflow/LEDGER.md`
- `directions/indie-game-development/workflow/OBLIGATIONS.md`
- `directions/indie-game-development/workflow/RECEIPTS_INDEX.md`
- `directions/indie-game-development/workflow/COMMIT_SCOPES.md`
- `directions/indie-game-development/workflow/DASHBOARD.md`
- `directions/indie-game-development/workflow/MIGRATION_RECEIPT.md`

## Optional Receipt Records

- `directions/indie-game-development/workflow/receipts/R-IDG-ROOT-OBJECTIVE-DECISION-B-001.md`

## Request-Only Capability Packs

- `workflow/project_packs/EXECUTION_HARNESS_PACK.md`
- `workflow/project_packs/PROJECT_PACKS_INDEX.md`

Load request-only capability packs only when an admitted task needs them.

## Request-Only Exact Canonical Files

If a pack summary is insufficient or exact schema/source text is material, request or load the exact canonical source file listed in the relevant pack `source_manifest`.

## Do Not Load By Default

- `directions/indie-game-development/archive/**`
- old `proof_workflow` namespace
- old vNext-R workflow evidence from legacy branch/tag
- `directions/indie-game-development/project_files/**`
- `directions/*/project_files/**`
- `directions/indie-game-development/workflow/project_setup/**` as Project Files/Sources
- other Direction `project_setup/**` folders as Project Files/Sources
- `directions/*/phases/**`
- `directions/*/execution_logs/**`
- `migration/**`
- product repo `.execution/**` unless operating inside the target product repo and explicitly admitted
- old runtime, stage, and transport files from previous workflow systems
- raw chats, archive notes, or old rebuild packs

## Refresh Rule

- If Project Instructions source changes, paste the updated UI payload into the ChatGPT Project Instructions field.
- Do not upload `project_setup/CHATGPT_PROJECT_INSTRUCTIONS.md` as a Project File/Source.
- If a Direction payload file changes, refresh that uploaded Project File/Source.
- If a project pack changes, refresh that uploaded pack.
- If `PROJECT_PACKS_INDEX.md` changes, refresh it only if already uploaded or explicitly used for setup inspection.
- If any canonical source file in a pack `source_manifest` changes, regenerate and refresh the pack before relying on it.
- GitHub remains source of truth; Project Files/Sources are runtime cache.

## Restoration Steps

1. Create ChatGPT Project named "Indie Game Development".
2. Paste Project Instructions from `CHATGPT_PROJECT_INSTRUCTIONS.md` into the ChatGPT Project Instructions UI.
3. Upload the three default shared packs as Project Files/Sources.
4. Upload the six Direction payload files as Project Files/Sources.
5. Do not upload forbidden legacy files.
6. Confirm the uploaded file list against this manifest and run setup validation using `workflow/project_setup/PROJECT_SETUP_VALIDATION_CHECKLIST.md` if needed.
7. Start with the next valid run shown by `directions/indie-game-development/workflow/DASHBOARD.md` / `directions/indie-game-development/workflow/OBLIGATIONS.md`.

## Project Files Count Summary

```yaml
default_upload_count: 9
default_shared_packs: 3
direction_payload_files: 6
project_instruction_sources_in_default_upload_count: 0
request_only_execution_pack: 1
request_only_project_packs_index: 1
```

END_OF_FILE: directions/indie-game-development/workflow/project_setup/PROJECT_FILES_MANIFEST.md
