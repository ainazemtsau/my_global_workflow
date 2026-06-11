---
artifact_control:
  namespace: direction_workflow_project_setup
  direction_id: health-and-beauty
  artifact_type: project_files_manifest
  project_name: "Health and Beauty — Daily Ops"
  status: daily_ops_chatgpt_project_setup_created
  owner: workflow_os
  target_binding: HB-H1-DAILY-OPS-MINIMAL-RUNTIME-SURFACE-V0
---

# Health and Beauty — Daily Ops Project Surface Manifest

Project name: Health and Beauty — Daily Ops

Project type: ordinary Direction Workflow Project / bounded Daily Ops setup surface.

Target binding: `HB-H1-DAILY-OPS-MINIMAL-RUNTIME-SURFACE-V0`

This setup surface is not Daily Ops implementation, not tracking implementation, not a template/app/integration bundle, and not execution.

## Project Instructions UI Source

- `directions/health-and-beauty/workflow/project_setup/daily_ops/CHATGPT_PROJECT_INSTRUCTIONS.md`

Paste only the UI payload between `BEGIN_CHATGPT_PROJECT_INSTRUCTIONS_UI_PAYLOAD` and `END_CHATGPT_PROJECT_INSTRUCTIONS_UI_PAYLOAD` into the ChatGPT Project Instructions field.

```yaml
project_instruction_ui_update_required: true
do_not_upload_as_project_file:
  - directions/health-and-beauty/workflow/project_setup/daily_ops/CHATGPT_PROJECT_INSTRUCTIONS.md
project_instruction_ui_payload_budget:
  hard_max_chars: 8000
  target_max_chars: 6500
  warning_threshold_chars: 7200
  measured_scope: trimmed payload between BEGIN/END UI payload markers
```

Do not paste repository wrapper metadata, marker comments, or `END_OF_FILE` into the Project Instructions UI.

## Default Shared Project Packs / Sources

* `workflow/project_packs/UNIVERSAL_PROJECT_SHELL_PACK.md`
* `workflow/project_packs/WORKFLOW_BASE_PACK.md`
* `workflow/project_packs/TRANSPORT_CORE_PACK.md`

## Direction Payload

* `directions/health-and-beauty/workflow/LEDGER.md`
* `directions/health-and-beauty/workflow/OBLIGATIONS.md`
* `directions/health-and-beauty/workflow/RECEIPTS_INDEX.md`
* `directions/health-and-beauty/workflow/COMMIT_SCOPES.md`
* `directions/health-and-beauty/workflow/DASHBOARD.md`
* `directions/health-and-beauty/workflow/MIGRATION_RECEIPT.md`

## Request-Only Exact Receipts

Load these only when exact authority is material to a run:

* `directions/health-and-beauty/workflow/receipts/R-HB-H1-NUTRITION-PLAN-CREATE-2026-05-28.md`
* `directions/health-and-beauty/workflow/receipts/R-HB-H1-TRAINING-PLAN-CREATE-2026-05-28.md`
* `directions/health-and-beauty/workflow/receipts/R-HB-H1-DAILY-OPS-IMPLEMENTATION-READINESS-DEFINE-2026-05-28.md`
* `directions/health-and-beauty/workflow/receipts/R-HB-H1-DAILY-OPS-CHATGPT-PROJECT-SETUP-2026-05-28.md`

## Request-Only Capability Packs

* `workflow/project_packs/EXECUTION_HARNESS_PACK.md`

Load request-only capability packs only when an admitted task needs them.

## Do Not Load By Default

* `directions/health-and-beauty/archive/**`
* old `proof_workflow` namespace
* old vNext-R workflow evidence from legacy branch/tag
* `directions/health-and-beauty/project_files/**`
* `directions/health-and-beauty/project_setup/**`
* `directions/*/project_files/**`
* `directions/*/project_setup/**`
* `directions/*/phases/**`
* `directions/*/execution_logs/**`
* `migration/**`
* product repo `.execution/**` unless operating inside the target product repo and explicitly admitted
* old vNext-R runtime/stage/transport files
* raw chats, archive notes, or old rebuild packs

## Refresh Rule

* If this Project Instructions source changes, paste the updated UI payload into the ChatGPT Project Instructions field.
* Before paste, extract the UI payload between markers, trim it, count characters, and fail validation if it exceeds 8,000 characters.
* Do not upload `project_setup/daily_ops/CHATGPT_PROJECT_INSTRUCTIONS.md` as a Project File/Source.
* If a Direction payload file changes, refresh that uploaded Project File/Source.
* If a project pack changes, refresh that uploaded pack.
* If any canonical source file in a pack `source_manifest` changes, regenerate and refresh that pack before relying on it.
* GitHub remains source of truth; Project Files/Sources are runtime cache.

## Restoration Steps

1. Create ChatGPT Project named "Health and Beauty — Daily Ops".
2. Paste Project Instructions UI payload from `daily_ops/CHATGPT_PROJECT_INSTRUCTIONS.md`.
3. Upload the three default shared packs as Project Files/Sources.
4. Upload the six Direction payload files as Project Files/Sources.
5. Do not upload forbidden legacy files.
6. Do not upload the Project Instructions source as a Project File/Source.
7. Run setup validation using `workflow/project_setup/PROJECT_SETUP_VALIDATION_CHECKLIST.md` if needed.
8. Start with the next valid run shown by `directions/health-and-beauty/workflow/DASHBOARD.md` / `directions/health-and-beauty/workflow/OBLIGATIONS.md`.

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

END_OF_FILE: directions/health-and-beauty/workflow/project_setup/daily_ops/PROJECT_FILES_MANIFEST.md
