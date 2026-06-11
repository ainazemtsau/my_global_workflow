---
artifact_control:
  namespace: direction_proof_project_setup
  direction_id: solo-max-productive
  artifact_type: project_files_manifest
  project_name: "Solo Max Productive — Proof"
  status: project_instruction_budget_active_direction_sweep
  owner: proof_carrying_workflow_os
---

# Solo Max Productive — Proof Project Surface Manifest

Project name: Solo Max Productive — Proof

## Project Instructions UI Source

- `directions/solo-max-productive/setup/CHATGPT_PROJECT_INSTRUCTIONS.md`

Paste the UI payload from this source into the ChatGPT Project Instructions field.

```yaml
project_instruction_ui_update_required: true
do_not_upload_as_project_file:
  - directions/solo-max-productive/setup/CHATGPT_PROJECT_INSTRUCTIONS.md
project_instruction_ui_payload_budget:
  hard_max_chars: 8000
  target_max_chars: 6500
  warning_threshold_chars: 7200
  measured_scope: trimmed payload between BEGIN/END UI payload markers
```

This source is not a Project File/Source and is excluded from the default upload count.

Do not paste repository wrapper metadata, marker comments, or `END_OF_FILE` into the Project Instructions UI.

## Default Shared Project Packs / Sources

- `workflow/project_packs/UNIVERSAL_PROJECT_SHELL_PACK.md`
- `workflow/project_packs/WORKFLOW_BASE_PACK.md`
- `workflow/project_packs/TRANSPORT_CORE_PACK.md`

## Direction Payload

- `directions/solo-max-productive/workflow/LEDGER.md`
- `directions/solo-max-productive/workflow/OBLIGATIONS.md`
- `directions/solo-max-productive/workflow/RECEIPTS_INDEX.md`
- `directions/solo-max-productive/workflow/COMMIT_SCOPES.md`
- `directions/solo-max-productive/workflow/DASHBOARD.md`
- `directions/solo-max-productive/workflow/MIGRATION_RECEIPT.md`

## Request-Only Capability Packs

- `workflow/project_packs/EXECUTION_HARNESS_PACK.md`

Load request-only capability packs only when an admitted task needs them.

## Request-Only Exact Canonical Files

If a pack summary is insufficient or exact schema/source text is material, request or load the exact canonical source file listed in the relevant pack `source_manifest`.

## Do Not Load By Default

- `directions/solo-max-productive/archive/**`
- `directions/solo-max-productive/setup/**`
- old `proof_workflow` namespace
- old vNext-R workflow evidence from legacy branch/tag
- `directions/solo-max-productive/project_files/**`
- `directions/solo-max-productive/project_setup/**`
- `directions/*/project_files/**`
- `directions/*/project_setup/**`
- `directions/*/phases/**`
- `directions/*/execution_logs/**`
- `migration/**`
- product repo `.execution/**` unless operating inside the target product repo and explicitly admitted
- old vNext-R runtime/stage/transport files
- raw chats, archive notes, or old rebuild packs

## Refresh Rule

- If Project Instructions source changes, paste the updated UI payload into the ChatGPT Project Instructions field.
- Before paste, extract the UI payload between markers, trim it, count characters, and fail validation if it exceeds 8,000 characters.
- Do not upload `setup/CHATGPT_PROJECT_INSTRUCTIONS.md` as a Project File/Source.
- If a Direction payload file changes, refresh that uploaded Project File/Source.
- If a project pack changes, refresh that uploaded pack.
- If any canonical source file in a pack `source_manifest` changes, regenerate and refresh the pack before relying on it.
- GitHub remains source of truth; Project Files/Sources are runtime cache.

## Restoration Steps

1. Create ChatGPT Project named "Solo Max Productive — Proof".
2. Paste Project Instructions UI payload from `CHATGPT_PROJECT_INSTRUCTIONS.md`.
3. Upload the three default shared packs as Project Files/Sources.
4. Upload the six Direction payload files as Project Files/Sources.
5. Do not upload forbidden legacy files.
6. Run setup validation using `workflow/project_setup/PROJECT_SETUP_VALIDATION_CHECKLIST.md` if needed.
7. Start with the next valid run shown by `DASHBOARD.md` / `OBLIGATIONS.md`.

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

END_OF_FILE: directions/solo-max-productive/setup/PROJECT_FILES_MANIFEST.md
