# My Global Workflow

Status: active

This repository is the canonical AI workflow source for the Proof-Carrying Workflow OS.

GitHub canonical activation is recorded in `WORKFLOW_SOURCE_OF_TRUTH.md`.

## Active Workflow

- Shared workflow kernel and runtime policies live under `proof_workflow/`.
- Direction proof state lives under `directions/<direction-id>/proof/`.
- New ChatGPT Projects should be created or restored from proof project setup manifests under `directions/<direction-id>/proof/project_setup/`.

## Legacy Boundary

The old vNext-R workflow is preserved at:

- branch: `legacy/vnext-r-main-before-proof-os-2026-05-25`
- tag: `vnext-r-main-before-proof-os-2026-05-25`

Old vNext-R runtime, stage registry, stage prompt, and transport directories were removed from active `main` after archival. Use the legacy branch/tag if those historical files are needed.

Any remaining old `workflow/**` directories in `main` are legacy/future-inspection surfaces, not active default authority.

Do not use old workflow stage files, runtime files, transport files, or Direction `project_files/00-08` as accepted proof state.

Old Direction data may become proof workflow state only through Legacy Import Receipt + Verify + Commit.
