---
artifact_control:
  namespace: workflow_project_setup
  artifact_type: project_setup_validation_checklist
  status: project_instruction_budget_hardened
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
- UI payload was extracted between `BEGIN_CHATGPT_PROJECT_INSTRUCTIONS_UI_PAYLOAD` and `END_CHATGPT_PROJECT_INSTRUCTIONS_UI_PAYLOAD`.
- Extracted UI payload was trimmed and character-counted.
- UI payload is at or below the 8,000-character hard max.
- UI payload is reported as warning if above 7,200 characters.
- UI payload target is at or below 6,500 characters.
- UI payload is compact behavior instructions, not repository documentation or schema/card storage.
- UI payload does not include artifact metadata, marker comments, or `END_OF_FILE`.
- Project Instructions source file is not uploaded as a Project File/Source.
- Default packs are uploaded:
  - `workflow/project_packs/UNIVERSAL_PROJECT_SHELL_PACK.md`
  - `workflow/project_packs/WORKFLOW_BASE_PACK.md`
  - `workflow/project_packs/TRANSPORT_CORE_PACK.md`
- Direction payload is uploaded:
  - `directions/<direction-id>/<active-direction-state>/LEDGER.md`
  - `directions/<direction-id>/<active-direction-state>/OBLIGATIONS.md`
  - `directions/<direction-id>/<active-direction-state>/RECEIPTS_INDEX.md`
  - `directions/<direction-id>/<active-direction-state>/COMMIT_SCOPES.md`
  - `directions/<direction-id>/<active-direction-state>/DASHBOARD.md`
  - `directions/<direction-id>/<active-direction-state>/MIGRATION_RECEIPT.md`
- Forbidden old files are not uploaded.
- Execution Harness Pack is absent unless deliberately enabled.
- Direction proof Ledger is loaded.
- Direction manifest uses three shared packs plus six Direction payload files.
- Direction manifest default upload count excludes Project Instructions.
- Direction Project Instructions do not hard-code stale live state.
- Direction Project Instructions say Direction payload wins for live state.
- Project handles no-next-valid-run state by returning a human admission decision or `NEXT_CHAT_NEEDED` recovery prompt without treating candidate routes as accepted or executable.
- Root objective status is visible.
- No legacy state was imported automatically.
- Project can answer `Давай подтвердим корневую цель этого направления.` without using old vNext-R files.
- Refresh handoffs use separate `project_instruction_ui_update_required`, `project_sources_files_refresh_required`, `request_only_sources_refresh_required`, and `do_not_upload_as_project_file` fields.
- Codex handoffs declare `branch_policy`; missing or unclear policy means `review_branch_required`, and `direct_to_main_allowed` is limited to eligible simple single-Direction proof-state commits.

## Workflow Governance Maintenance Project Checks

- Project Instructions source is `directions/workflow-governance/workflow/project_setup/CHATGPT_PROJECT_INSTRUCTIONS.md`.
- Project Instructions UI contains the current paste-ready UI payload.
- UI payload was extracted between `BEGIN_CHATGPT_PROJECT_INSTRUCTIONS_UI_PAYLOAD` and `END_CHATGPT_PROJECT_INSTRUCTIONS_UI_PAYLOAD`.
- Extracted UI payload was trimmed and character-counted.
- UI payload is at or below the 8,000-character hard max, with target at or below 6,500 characters.
- UI payload is compact maintenance-console behavior instructions, not repository documentation or schema/card storage.
- UI payload does not include artifact metadata, marker comments, or `END_OF_FILE`.
- Project Instructions source file is not uploaded as a Project File/Source.
- Project Files manifest source is `directions/workflow-governance/workflow/project_setup/PROJECT_FILES_MANIFEST.md`.
- Default Project Files/Sources are only:
  - `WORKFLOW_SOURCE_OF_TRUTH.md`
  - `workflow/project_packs/GOVERNANCE_MAINTENANCE_PACK.md`
  - `workflow/project_packs/PROJECT_PACKS_INDEX.md`
  - `docs/CHATGPT_PROJECT_SETUP.md`
  - `workflow/policies/08_CHATGPT_PROJECT_SETUP.md`
- Stale Direction runtime Project Files/Sources were removed from the ChatGPT Project.
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
- Codex handoffs declare `branch_policy`, preserve `review_branch_required` for workflow/setup/risky changes, and do not classify Project Instructions sources as Project Files/Sources refresh.
- Pasted Codex output is verified for scope, changed files, validation, forbidden-path cleanliness, separated project refresh requirements, and residual issues.

## Execution Pack Enabled Check

If `workflow/project_packs/EXECUTION_HARNESS_PACK.md` is enabled:

- no CodexRun may start without an execution-ready Receipt
- no CodexRun may start without a target binding
- no CodexRun may start without a validation plan
- no done claim is valid without a validation Receipt
- product repo technical memory must remain target-repo-local

END_OF_FILE: workflow/project_setup/PROJECT_SETUP_VALIDATION_CHECKLIST.md
