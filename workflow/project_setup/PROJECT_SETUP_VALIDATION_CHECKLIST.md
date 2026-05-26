---
artifact_control:
  namespace: workflow_project_setup
  artifact_type: project_setup_validation_checklist
  status: u3_pack_model
  owner: workflow_os
---

# Project Setup Validation Checklist

Use this checklist after creating or refreshing a ChatGPT Project.

First identify the Project type:

- ordinary Direction Workflow Project
- Workflow Governance Maintenance Project

## Ordinary Direction Workflow Project Checks

- Project Instructions source is correct.
- Project Instructions UI contains the current paste-ready UI payload.
- UI payload between BEGIN/END markers is 6000 characters or less when possible and never more than 7500 characters.
- UI payload contains direct behavior instructions, not setup documentation.
- UI payload does not contain YAML frontmatter or `END_OF_FILE`.
- Project Instructions source file is not uploaded as a Project File/Source.
- Default packs are uploaded:
  - `workflow/project_packs/UNIVERSAL_PROJECT_SHELL_PACK.md`
  - `workflow/project_packs/WORKFLOW_BASE_PACK.md`
  - `workflow/project_packs/TRANSPORT_CORE_PACK.md`
- Direction payload is uploaded:
  - `directions/<direction-id>/LEDGER.md`
  - `directions/<direction-id>/OBLIGATIONS.md`
  - `directions/<direction-id>/RECEIPTS_INDEX.md`
  - `directions/<direction-id>/COMMIT_SCOPES.md`
  - `directions/<direction-id>/DASHBOARD.md`
  - `directions/<direction-id>/MIGRATION_RECEIPT.md`
- Forbidden old files are not uploaded.
- Execution Harness Pack is absent unless deliberately enabled.
- Direction proof Ledger is loaded.
- Direction manifest uses three shared packs plus six Direction payload files.
- Direction manifest default upload count excludes Project Instructions.
- Direction Project Instructions do not hard-code stale live state.
- Direction Project Instructions say Direction payload wins for live state.
- Root objective status is visible.
- No legacy state was imported automatically.
- Project can answer `Давай подтвердим корневую цель этого направления.` without using old vNext-R files.
- Refresh handoffs use separate `project_instruction_ui_update_required`, `project_sources_files_refresh_required`, `request_only_sources_refresh_required`, and `do_not_upload_as_project_file` fields.

## Workflow Governance Maintenance Project Checks

- Project Instructions source is `directions/workflow-governance/workflow/project_setup/CHATGPT_PROJECT_INSTRUCTIONS.md`.
- Project Instructions UI contains the current paste-ready UI payload.
- UI payload between BEGIN/END markers is 6000 characters or less when possible and never more than 7500 characters.
- UI payload contains direct maintenance-console behavior instructions, not the full Governance Maintenance Pack.
- UI payload does not contain YAML frontmatter or `END_OF_FILE`.
- Project Instructions source file is not uploaded as a Project File/Source.
- Project Files manifest source is `directions/workflow-governance/workflow/project_setup/PROJECT_FILES_MANIFEST.md`.
- Default Project Files/Sources are only:
  - `WORKFLOW_SOURCE_OF_TRUTH.md`
  - `workflow/project_packs/GOVERNANCE_MAINTENANCE_PACK.md`
  - `workflow/project_packs/PROJECT_PACKS_INDEX.md`
  - `docs/CHATGPT_PROJECT_SETUP.md`
  - `workflow/policies/08_CHATGPT_PROJECT_SETUP.md`
- Stale Direction runtime Project Files were removed from the ChatGPT Project.
- `workflow/project_packs/WORKFLOW_BASE_PACK.md` is absent by default.
- `workflow/project_packs/TRANSPORT_CORE_PACK.md` is absent by default.
- `workflow/project_packs/EXECUTION_HARNESS_PACK.md` is absent by default.
- Workflow Governance Direction payload files are absent by default:
  - `directions/workflow-governance/workflow/LEDGER.md`
  - `directions/workflow-governance/workflow/OBLIGATIONS.md`
  - `directions/workflow-governance/workflow/RECEIPTS_INDEX.md`
  - `directions/workflow-governance/workflow/COMMIT_SCOPES.md`
  - `directions/workflow-governance/workflow/DASHBOARD.md`
  - `directions/workflow-governance/workflow/MIGRATION_RECEIPT.md`
- The Project does not start by reading Dashboard/Obligations next-valid-run state.
- The Project does not ask for root objective by default.
- The Project does not emit Receipt Cards by default.
- The Project handles one concrete maintenance problem, audit, research request, setup question, Codex handoff, or Codex result verification per chat.
- Repository persistence responses include a self-contained Codex handoff.
- Pasted Codex output is verified for scope, changed files, validation, forbidden-path cleanliness, separated project refresh requirements, and residual issues.

## Execution Pack Enabled Check

If `workflow/project_packs/EXECUTION_HARNESS_PACK.md` is enabled:

- no CodexRun may start without an execution-ready Receipt
- no CodexRun may start without a target binding
- no CodexRun may start without a validation plan
- no done claim is valid without a validation Receipt
- product repo technical memory must remain target-repo-local

END_OF_FILE: workflow/project_setup/PROJECT_SETUP_VALIDATION_CHECKLIST.md
