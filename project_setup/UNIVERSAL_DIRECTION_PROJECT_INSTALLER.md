---
artifact_control:
  namespace: workflow_project_setup
  artifact_type: universal_direction_project_installer
  status: canonical_setup_guide
  owner: workflow_os
---

# Universal Direction Project Installer

## Purpose

This file defines one universal setup protocol for all Direction ChatGPT Workflow Projects.

The pack-based Project Files model is active for Direction Workflow Projects.

It is the repository source for the project installation process. It does not create accepted Ledger state.

## Setup Model

Layer A - Universal Project Shell:

- shared ChatGPT Project behavior
- context authority
- human input normalization
- human-facing run closure
- recursive child handoff
- legacy boundary

Layer B - Shared Workflow Runtime Packs:

- semantic kernel and workflow runtime cache
- normal transport/card cache
- Project Files upload convenience

Layer C - Direction Payload:

- the Direction proof files that carry accepted state and projections
- the only live Direction state source for Project startup

Layer D - Optional Capability Packs:

- request-only packs loaded only when an admitted task needs the capability

Product Repo Execution Setup is separate. Product/project technical memory belongs in the target product repository, not this workflow repository.

## Required Default Project Files

Upload these shared packs for all new Direction Workflow Projects:

- `project_packs/UNIVERSAL_PROJECT_SHELL_PACK.md`
- `project_packs/WORKFLOW_BASE_PACK.md`
- `project_packs/TRANSPORT_CORE_PACK.md`

Upload these Direction payload files:

- `directions/<direction-id>/LEDGER.md`
- `directions/<direction-id>/OBLIGATIONS.md`
- `directions/<direction-id>/RECEIPTS_INDEX.md`
- `directions/<direction-id>/COMMIT_SCOPES.md`
- `directions/<direction-id>/DASHBOARD.md`
- `directions/<direction-id>/MIGRATION_RECEIPT.md`

## Request-Only Capability Packs

Load this only when execution readiness, product repo setup, CodexRun, validation, human-guided execution, or complex technical mission work is admitted:

- `project_packs/EXECUTION_HARNESS_PACK.md`

Future optional capability packs may be added later:

- `project_packs/MIGRATION_LEGACY_IMPORT_PACK.md`
- `project_packs/GOVERNANCE_MAINTENANCE_PACK.md`

These future packs are not created by this installer unless those files exist in the repository.

## Forbidden Default Loads

Do not upload these by default:

- `workflow/**`
- `directions/<direction-id>/project_files/**`
- `directions/<direction-id>/project_setup/**`
- `directions/*/project_files/**`
- `directions/*/project_setup/**`
- `migration/**`
- old vNext-R runtime, stage, or transport files
- product repo `.execution/**` files in this workflow repository

Old files may be loaded only as legacy evidence for an admitted Legacy Import Obligation.

## Restoration Steps

1. Create a ChatGPT Project with the Direction project name.
2. Paste Project Instructions from the universal template or the Direction-specific source generated from it.
3. Upload the default shared packs.
4. Upload the Direction payload files.
5. Do not upload forbidden legacy files.
6. Run the setup validation prompt/checklist.
7. Start with the next valid run shown by `DASHBOARD.md` / `OBLIGATIONS.md`.

Project Instructions are behavior/setup instructions. They must not store live Direction state.

Live state must be read from Direction payload files. If Project Instructions and Direction payload conflict, Direction payload wins for live state.

## Existing Direction No-Data-Loss Rule

Old Direction data remains legacy evidence only.

Import requires:

```text
Legacy Import Receipt -> Verify -> Commit
```

Old chats are not source of truth. Old Direction Map, Active Goal, Current Phase, Portfolio Queue, project files, project setup files, phases, and execution logs do not become accepted state without a verified committed Receipt.

## Execution Harness Enablement

The Execution Harness Pack is request-only.

Request-load it only when execution readiness, product repo setup, CodexRun, validation, human-guided execution, or complex technical mission work is admitted.

No execution-ready Receipt means no CodexRun.

No validation Receipt means no done.

Complex technical mission direct CodexRun is denied.

## Product Repo Execution Boundary

Product/project technical memory belongs in the target product repository, not this workflow repository.

Target product repositories should maintain:

```text
AGENTS.md
.execution/project_profile.md
.execution/validation_profile.md
.execution/module_map.md
.execution/technical_ledger.md
.execution/known_risks.md
.execution/receipts/
.execution/plans/
```

Do not create product repo `.execution/**` setup inside this workflow repository.

## Refresh Rule

Project Files are runtime cache. GitHub remains source of truth.

If any pack `source_manifest` file changes, regenerate or refresh that pack and replace the uploaded Project File before the next material run that depends on it.

If Direction payload files change, refresh the uploaded Direction payload file before the next material run.

## Validation Checklist

Before using a new Direction Workflow Project for material work, confirm:

- required shared packs are uploaded
- Direction payload files are uploaded
- Project Instructions do not hard-code stale live state
- Direction manifests use three shared packs plus six Direction payload files
- forbidden old files are not uploaded
- old vNext-R files are not default-loaded
- Context Authority is present
- Human Input Normalization is present
- Human-Facing Run Closure is present
- Direction Ledger starts clean unless accepted Receipts exist
- Execution Harness Pack is absent unless intentionally enabled
- Project starts from the next valid run shown by `DASHBOARD.md` / `OBLIGATIONS.md`

END_OF_FILE: project_setup/UNIVERSAL_DIRECTION_PROJECT_INSTALLER.md
