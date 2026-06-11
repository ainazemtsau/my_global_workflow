# New Device Bootstrap

Status: active

Use this file to connect a new device, local worktree, or fresh ChatGPT/Codex workspace to the Workflow OS.

## Canonical Repository

- Repository: `https://github.com/ainazemtsau/my_global_workflow`
- Branch: `main`
- Source-of-truth marker: `WORKFLOW_SOURCE_OF_TRUTH.md`
- Active workflow authority: `workflow/**`

The old vNext-R workflow is archived at:

- branch: `legacy/vnext-r-main-before-proof-os-2026-05-25`
- tag: `vnext-r-main-before-proof-os-2026-05-25`

## Required Local Setup

1. Clone the repository.
2. Use `main`.
3. Read root `AGENTS.md`.
4. Read `WORKFLOW_SOURCE_OF_TRUTH.md`.
5. Read the relevant files under `workflow/**` for the task.
6. For Direction work, use that Direction's active payload and project setup paths from its Project Files manifest.

## ChatGPT Project Restore

New ChatGPT Projects should be restored from:

- `workflow/project_setup/UNIVERSAL_DIRECTION_PROJECT_INSTALLER.md`
- `workflow/project_setup/UNIVERSAL_DIRECTION_PROJECT_INSTRUCTIONS.md`
- `workflow/project_setup/UNIVERSAL_PROJECT_FILES_MANIFEST_TEMPLATE.md`
- `workflow/project_setup/PROJECT_SETUP_VALIDATION_CHECKLIST.md`

Upload default packs:

- `workflow/project_packs/UNIVERSAL_PROJECT_SHELL_PACK.md`
- `workflow/project_packs/WORKFLOW_BASE_PACK.md`
- `workflow/project_packs/TRANSPORT_CORE_PACK.md`

Upload Direction payload:

- `directions/<direction-id>/<active-direction-state>/LEDGER.md`
- `directions/<direction-id>/<active-direction-state>/OBLIGATIONS.md`
- `directions/<direction-id>/<active-direction-state>/RECEIPTS_INDEX.md`
- `directions/<direction-id>/<active-direction-state>/COMMIT_SCOPES.md`
- `directions/<direction-id>/<active-direction-state>/DASHBOARD.md`
- `directions/<direction-id>/<active-direction-state>/MIGRATION_RECEIPT.md`

Per-Direction setup files remain under:

- the Direction's active project setup directory listed by its Project Files manifest.

Per-Direction manifests use the pack model: three shared packs plus six Direction payload files.

Project Instructions are behavior/setup instructions. Direction payload files are live state.

## Legacy Files

Old `directions/<direction-id>/project_files/00-08` files are legacy evidence, not default setup.

The active `workflow/` directory is the current Workflow OS namespace, not the old vNext-R workflow tree.

Old vNext-R workflow files are available from the legacy branch/tag, not active `main`.

Use old files only when a workflow Obligation explicitly requests legacy evidence or Legacy Import.

Do not upload old vNext-R runtime, stage, transport, old project files, or old project setup files as default Project Files.

## Codex Rules

- Keep edits inside the named allowed paths.
- Do not invent Direction proof state.
- If required files are unavailable or reads are incomplete, return the exact path and blocker.
- Repository maintenance is separate from product/project execution.
- Execution Harness Pack is request-only unless execution readiness is admitted.
- Product repo execution setup is target-repo-local, not workflow-repo-local.
- Report separated project refresh requirements when changed files affect ChatGPT Projects, including payload character counts when Project Instructions UI sources change.

END_OF_FILE: docs/NEW_DEVICE_BOOTSTRAP.md
