# My Global Workflow

Status: active

This repository is the canonical AI workflow source for the Workflow OS.

GitHub canonical activation is recorded in `WORKFLOW_SOURCE_OF_TRUTH.md`.

## Active Workflow

- Shared workflow kernel and runtime policies live under `workflow/`.
- Universal ChatGPT Project setup lives under `workflow/project_setup/`.
- Project pack runtime-cache files live under `workflow/project_packs/`.
- Direction accepted workflow state lives under each Direction's active payload directory as listed by its Project Files manifest.
- New ChatGPT Projects should be created or restored from the universal installer and the pack-based manifest in each Direction's active project setup directory.
- Workflow Governance is self-hosted and uses active payload files under `directions/workflow-governance/workflow/`.

## Workflow v3 Namespace Separation

- Current and rollback Workflow OS namespace: `workflow/**`.
- Workflow v3 clean-start skeleton namespace: `workflow_v3/**`.
- Old Direction namespace for Workflow v3: `directions/**` as `legacy_evidence` only, unless an explicit bridge/import/adoption policy says otherwise.
- Future Workflow v3 Direction namespace: `directions_v3/**`.

Workflow v3 does not decommission the old/current Workflow OS. The `workflow/**` namespace remains available as current Workflow OS and rollback context unless a later explicit package changes that boundary.

## Project Setup

Use:

- `workflow/project_setup/UNIVERSAL_DIRECTION_PROJECT_INSTALLER.md`
- `workflow/project_setup/UNIVERSAL_DIRECTION_PROJECT_INSTRUCTIONS.md`
- `workflow/project_setup/UNIVERSAL_PROJECT_FILES_MANIFEST_TEMPLATE.md`
- `workflow/project_setup/PROJECT_SETUP_VALIDATION_CHECKLIST.md`

Default shared Project Files are:

- `workflow/project_packs/UNIVERSAL_PROJECT_SHELL_PACK.md`
- `workflow/project_packs/WORKFLOW_BASE_PACK.md`
- `workflow/project_packs/TRANSPORT_CORE_PACK.md`

The Execution Harness Pack is request-only.

Direction payload files are live state. Project Instructions are behavior/setup instructions.

## Legacy Boundary

The old vNext-R workflow is preserved at:

- branch: `legacy/vnext-r-main-before-proof-os-2026-05-25`
- tag: `vnext-r-main-before-proof-os-2026-05-25`

Old vNext-R runtime, stage registry, stage prompt, and transport directories were removed from active `main` after archival. Use the legacy branch/tag if those historical files are needed.

The active `workflow/` directory is the current Workflow OS namespace. It is not the old vNext-R workflow tree.

Do not use old workflow stage files, runtime files, transport files, or Direction `project_files/00-08` as accepted state. Historical workflow files are available only from the legacy branch/tag.

Old Direction data may become workflow state only through Legacy Import Receipt + Verify + Commit.

END_OF_FILE: README.md
