# New Device Bootstrap

Status: active

Use this file to connect a new device, local worktree, or fresh ChatGPT/Codex workspace to the Proof-Carrying Workflow OS.

## Canonical Repository

- Repository: `https://github.com/ainazemtsau/my_global_workflow`
- Branch: `main`
- Source-of-truth marker: `WORKFLOW_SOURCE_OF_TRUTH.md`
- Active workflow authority: `proof_workflow/**`

The old vNext-R workflow is archived at:

- branch: `legacy/vnext-r-main-before-proof-os-2026-05-25`
- tag: `vnext-r-main-before-proof-os-2026-05-25`

## Required Local Setup

1. Clone the repository.
2. Use `main`.
3. Read root `AGENTS.md`.
4. Read `WORKFLOW_SOURCE_OF_TRUTH.md`.
5. Read relevant `proof_workflow/**` files for the task.
6. For Direction work, use `directions/<direction-id>/proof/**` after that Direction has a proof skeleton.

## ChatGPT Project Restore

New ChatGPT Projects should be restored from:

- `proof_workflow/project_setup/UNIVERSAL_DIRECTION_PROJECT_INSTALLER.md`
- `proof_workflow/project_setup/UNIVERSAL_DIRECTION_PROJECT_INSTRUCTIONS.md`
- `proof_workflow/project_setup/UNIVERSAL_PROJECT_FILES_MANIFEST_TEMPLATE.md`
- `proof_workflow/project_setup/PROJECT_SETUP_VALIDATION_CHECKLIST.md`

Upload default packs:

- `proof_workflow/project_packs/UNIVERSAL_PROJECT_SHELL_PACK.md`
- `proof_workflow/project_packs/PROOF_BASE_PACK.md`
- `proof_workflow/project_packs/TRANSPORT_CORE_PACK.md`

Upload Direction payload:

- `directions/<direction-id>/proof/LEDGER.md`
- `directions/<direction-id>/proof/OBLIGATIONS.md`
- `directions/<direction-id>/proof/RECEIPTS_INDEX.md`
- `directions/<direction-id>/proof/COMMIT_SCOPES.md`
- `directions/<direction-id>/proof/DASHBOARD.md`
- `directions/<direction-id>/proof/MIGRATION_RECEIPT.md`

Per-Direction setup files remain under:

- `directions/<direction-id>/proof/project_setup/CHATGPT_PROJECT_INSTRUCTIONS.md`
- `directions/<direction-id>/proof/project_setup/PROJECT_FILES_MANIFEST.md`

Per-Direction manifests use the pack model: three shared packs plus six Direction payload files.

Project Instructions are behavior/setup instructions. Direction payload files are live state.

## Legacy Files

Old `directions/<direction-id>/project_files/00-08` files are legacy evidence, not default setup.

The old vNext-R `workflow/` tree is not present in active `main`.

Old vNext-R workflow files are available from the legacy branch/tag, not active `main`.

Use old files only when a proof workflow Obligation explicitly requests legacy evidence or Legacy Import.

Do not upload old vNext-R runtime, stage, transport, old project files, or old project setup files as default Project Files.

## Codex Rules

- Keep edits inside the named allowed paths.
- Do not invent Direction proof state.
- If required files are unavailable or reads are incomplete, return the exact path and blocker.
- Repository maintenance is separate from product/project execution.
- Execution Harness Pack is request-only unless execution readiness is admitted.
- Product repo execution setup is target-repo-local, not workflow-repo-local.
- Report Project Files refresh requirements when changed files are loaded in ChatGPT Projects.

END_OF_FILE: docs/NEW_DEVICE_BOOTSTRAP.md
