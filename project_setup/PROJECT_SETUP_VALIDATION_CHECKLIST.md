---
artifact_control:
  namespace: workflow_project_setup
  artifact_type: project_setup_validation_checklist
  status: u3_pack_model
  owner: workflow_os
---

# Project Setup Validation Checklist

Use this checklist after creating or refreshing a ChatGPT Direction Workflow Project.

## Required Checks

- Project Instructions source is correct.
- Default packs are uploaded:
  - `project_packs/UNIVERSAL_PROJECT_SHELL_PACK.md`
  - `project_packs/WORKFLOW_BASE_PACK.md`
  - `project_packs/TRANSPORT_CORE_PACK.md`
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
- Direction Project Instructions do not hard-code stale live state.
- Direction Project Instructions say Direction payload wins for live state.
- Root objective status is visible.
- No legacy state was imported automatically.
- Project can answer `Давай подтвердим корневую цель этого направления.` without using old vNext-R files.

## Execution Pack Enabled Check

If `project_packs/EXECUTION_HARNESS_PACK.md` is enabled:

- no CodexRun may start without an execution-ready Receipt
- no CodexRun may start without a target binding
- no CodexRun may start without a validation plan
- no done claim is valid without a validation Receipt
- product repo technical memory must remain target-repo-local

END_OF_FILE: project_setup/PROJECT_SETUP_VALIDATION_CHECKLIST.md
