---
artifact_control:
  namespace: proof_workflow_project_setup
  artifact_type: project_setup_validation_checklist
  status: u2_initial
  owner: proof_carrying_workflow_os
---

# Project Setup Validation Checklist

Use this checklist after creating or refreshing a ChatGPT Direction Proof Project.

## Required Checks

- Project Instructions source is correct.
- Default packs are uploaded:
  - `proof_workflow/project_packs/UNIVERSAL_PROJECT_SHELL_PACK.md`
  - `proof_workflow/project_packs/PROOF_BASE_PACK.md`
  - `proof_workflow/project_packs/TRANSPORT_CORE_PACK.md`
- Direction payload is uploaded:
  - `directions/<direction-id>/proof/LEDGER.md`
  - `directions/<direction-id>/proof/OBLIGATIONS.md`
  - `directions/<direction-id>/proof/RECEIPTS_INDEX.md`
  - `directions/<direction-id>/proof/COMMIT_SCOPES.md`
  - `directions/<direction-id>/proof/DASHBOARD.md`
  - `directions/<direction-id>/proof/MIGRATION_RECEIPT.md`
- Forbidden old files are not uploaded.
- Execution Harness Pack is absent unless deliberately enabled.
- Direction proof Ledger is loaded.
- Root objective status is visible.
- No legacy state was imported automatically.
- Project can answer `Давай подтвердим корневую цель этого направления.` without using old vNext-R files.

## Execution Pack Enabled Check

If `proof_workflow/project_packs/EXECUTION_HARNESS_PACK.md` is enabled:

- no CodexRun may start without an execution-ready Receipt
- no CodexRun may start without a target binding
- no CodexRun may start without a validation plan
- no done claim is valid without a validation Receipt
- product repo technical memory must remain target-repo-local

END_OF_FILE: proof_workflow/project_setup/PROJECT_SETUP_VALIDATION_CHECKLIST.md
