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

New ChatGPT Projects should be restored from proof project setup files.

When available, use:

- `directions/<direction-id>/proof/project_setup/CHATGPT_PROJECT_INSTRUCTIONS.md`
- `directions/<direction-id>/proof/project_setup/PROJECT_FILES_MANIFEST.md`

Upload Project Files exactly as listed in the manifest.

If a Direction lacks `directions/<direction-id>/proof/project_setup/`, initialize the proof skeleton first. Do not fall back to old vNext-R setup as active runtime.

## Legacy Files

Old `directions/<direction-id>/project_files/00-08` files are legacy evidence, not default setup.

Old workflow runtime, stage registry, stage prompts, and old transport files are legacy-only and are not default setup.

After M3 cleanup, old vNext-R runtime, stage registry, stage prompt, and transport files are available from the legacy branch/tag, not active `main`.

Use old files only when a proof workflow Obligation explicitly requests legacy evidence or Legacy Import.

## Codex Rules

- Keep edits inside the named allowed paths.
- Do not invent Direction proof state.
- If required files are unavailable or reads are incomplete, return the exact path and blocker.
- Repository maintenance is separate from product/project execution.
- Report Project Files refresh requirements when changed files are loaded in ChatGPT Projects.
