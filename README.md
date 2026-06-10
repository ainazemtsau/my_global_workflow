# My Global Workflow

## ACTIVE SYSTEM: Direction OS (`os/` + `live/`)

The active workflow system is **Direction OS**:

- Rules: `os/KERNEL.md` (start here), plays in `os/plays/`, schemas in `os/schema/`, platform adapters in `os/adapters/`.
- How to start: `os/BOOTSTRAP.md`.
- Live direction state: `live/<direction-id>/`.
- Rationale: `os/docs/` (requirements, research basis, design).

Everything below this section — `workflow/**`, `workflow_v3/**`, `directions/**`, `directions_v3/**`, `WORKFLOW_SOURCE_OF_TRUTH.md` — is **frozen legacy**, kept as archive and evidence only. No session should treat it as rules. Content (plans, knowledge) may be imported into `live/**` deliberately; mechanics may not.

---

# Legacy (frozen 2026-06-10)

Status: archived

This repository was previously the canonical AI workflow source for the Workflow OS.

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
- Workflow v3 canonical control-plane, setup, procedure, template, completion, adoption, and owner-quality source namespace: `workflow_v3/**`.
- Workflow v3 clean-start Direction namespace: `directions_v3/**`.
- Old Direction namespace for Workflow v3: `directions/**` as `legacy_evidence` only, unless an explicit bridge/import/adoption policy says otherwise.

Workflow v3 does not decommission the old/current Workflow OS. The `workflow/**` namespace remains available as current Workflow OS and rollback context unless a later explicit package changes that boundary.

Workflow v3 repository-side sources now live under `workflow_v3/**`, including `workflow_v3/control_plane/**`, `workflow_v3/project_setup/**`, `workflow_v3/procedures/**`, `workflow_v3/templates/**`, `workflow_v3/completion/**`, `workflow_v3/adoption/**`, and owner-quality docs. These are repository documentation/setup sources only and do not adopt Directions or update ChatGPT Projects.

No `indie-game-development` Direction exists after this cleanup in either the clean-start Workflow v3 namespace or the old Direction namespace.

Old `directions/**` material is not accepted Workflow v3 state.

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
