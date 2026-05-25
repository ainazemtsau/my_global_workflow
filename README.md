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

Old `workflow/**` directories may still exist in `main` until cleanup, but they are legacy-only and are not active default authority.

Do not use old workflow stage files, runtime files, transport files, or Direction `project_files/00-08` as accepted proof state.

Old Direction data may become proof workflow state only through Legacy Import Receipt + Verify + Commit.
