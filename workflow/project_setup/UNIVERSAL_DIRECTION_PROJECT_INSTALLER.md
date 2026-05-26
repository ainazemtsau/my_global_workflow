---
artifact_control:
  namespace: workflow_project_setup
  artifact_type: universal_direction_project_installer
  status: project_instruction_budget_hardened
  owner: workflow_os
---

# Universal Direction Project Installer

## Purpose

This file defines one universal setup protocol for all Direction ChatGPT Workflow Projects.

The pack-based Project Files model is active for Direction Workflow Projects.

It is the repository source for the project installation process. It does not create accepted Ledger state.

## Setup Model

Layer 0 - Project Instructions UI:

- behavior instructions pasted into the ChatGPT Project Instructions field
- generated from repository instruction sources such as `CHATGPT_PROJECT_INSTRUCTIONS.md`
- not uploaded as a Project File/Source
- not live Direction state

Layer A - Universal Project Shell:

- shared ChatGPT Project behavior
- context authority
- human input normalization
- human-facing run closure
- recursive child handoff
- legacy boundary

Layer B - Shared Workflow Runtime Packs / Project Files/Sources:

- semantic kernel and workflow runtime cache
- normal transport/card cache
- Project Files upload convenience

Layer C - Direction Payload / Project Files/Sources:

- the Direction proof files that carry accepted state and projections
- the only live Direction state source for Project startup

Layer D - Optional Request-Only Sources:

- request-only packs loaded only when an admitted task needs the capability

Product Repo Execution Setup is separate. Product/project technical memory belongs in the target product repository, not this workflow repository.

## Required Default Setup

Step 1: paste or update Project Instructions in the ChatGPT Project Instructions UI using the generated instruction source.

Paste only the compact UI payload between the `BEGIN_CHATGPT_PROJECT_INSTRUCTIONS_UI_PAYLOAD` and `END_CHATGPT_PROJECT_INSTRUCTIONS_UI_PAYLOAD` markers.

Before paste, count the trimmed payload characters: target at or below 6,500, warn above 7,200, fail above 8,000.

Do not paste repository wrapper metadata, artifact frontmatter, marker comments, or `END_OF_FILE`.

Do not upload `project_setup/CHATGPT_PROJECT_INSTRUCTIONS.md` as a Project File/Source.

Step 2: upload the following default Project Files/Sources.

## Default Shared Packs

Upload these shared packs for all new Direction Workflow Projects:

- `workflow/project_packs/UNIVERSAL_PROJECT_SHELL_PACK.md`
- `workflow/project_packs/WORKFLOW_BASE_PACK.md`
- `workflow/project_packs/TRANSPORT_CORE_PACK.md`

Upload these Direction payload files:

- `directions/<direction-id>/LEDGER.md`
- `directions/<direction-id>/OBLIGATIONS.md`
- `directions/<direction-id>/RECEIPTS_INDEX.md`
- `directions/<direction-id>/COMMIT_SCOPES.md`
- `directions/<direction-id>/DASHBOARD.md`
- `directions/<direction-id>/MIGRATION_RECEIPT.md`

## Request-Only Capability Packs

Load this only when execution readiness, product repo setup, CodexRun, validation, human-guided execution, or complex technical mission work is admitted:

- `workflow/project_packs/EXECUTION_HARNESS_PACK.md`

Load this only when exact pack/setup inspection requires the index:

- `workflow/project_packs/PROJECT_PACKS_INDEX.md`

Future optional capability packs may be added later:

- `workflow/project_packs/MIGRATION_LEGACY_IMPORT_PACK.md`
- `workflow/project_packs/GOVERNANCE_MAINTENANCE_PACK.md`

These future packs are not created by this installer unless those files exist in the repository.

## Forbidden Default Loads

Do not upload these by default:

- `workflow/**`
- `directions/<direction-id>/project_files/**`
- `directions/<direction-id>/project_setup/**` as Project Files/Sources, including `CHATGPT_PROJECT_INSTRUCTIONS.md`
- `directions/*/project_files/**`
- `directions/*/project_setup/**` as Project Files/Sources
- `migration/**`
- old vNext-R runtime, stage, or transport files
- product repo `.execution/**` files in this workflow repository

Old files may be loaded only as legacy evidence for an admitted Legacy Import Obligation.

## Restoration Steps

1. Create a ChatGPT Project with the Direction project name.
2. Paste Project Instructions from the universal template or the Direction-specific source generated from it into the ChatGPT Project Instructions UI.
3. Upload the default shared packs as Project Files/Sources.
4. Upload the Direction payload files as Project Files/Sources.
5. Do not upload forbidden legacy files.
6. Run the setup validation prompt/checklist.
7. Start with the next valid run shown by `DASHBOARD.md` / `OBLIGATIONS.md`.

Project Instructions are behavior/setup instructions in the Project Instructions UI. They must not store live Direction state and must not be uploaded as Project Files/Sources.

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

ChatGPT Project surfaces are runtime cache. GitHub remains source of truth.

If Project Instructions source changes, paste the updated UI payload into the ChatGPT Project Instructions field. Do not treat that action as a Project Files/Sources refresh.

If Project Instructions source changes, extract the payload between markers and report its character count before paste.

If any pack `source_manifest` file changes, regenerate or refresh that pack and replace the uploaded Project File/Source before the next material run that depends on it.

If Direction payload files change, refresh the uploaded Direction payload file before the next material run.

Refresh handoffs must separate `project_instruction_ui_update_required`, `project_sources_files_refresh_required`, `request_only_sources_refresh_required`, and `do_not_upload_as_project_file`.

## Validation Checklist

Before using a new Direction Workflow Project for material work, confirm:

- required shared packs are uploaded
- Direction payload files are uploaded
- Project Instructions are pasted into the Project Instructions UI
- Project Instructions UI payload is at or below 8,000 characters and target at or below 6,500
- Project Instructions UI payload omits repository wrapper metadata and `END_OF_FILE`
- Project Instructions source files are not uploaded as Project Files/Sources
- Project Instructions do not hard-code stale live state
- Direction manifests use three shared packs plus six Direction payload files
- Direction manifests exclude Project Instructions from the default upload count
- forbidden old files are not uploaded
- old vNext-R files are not default-loaded
- Context Authority is present
- Human Input Normalization is present
- Human-Facing Run Closure is present
- Direction Ledger starts clean unless accepted Receipts exist
- Execution Harness Pack is absent unless intentionally enabled
- Project starts from the next valid run shown by `DASHBOARD.md` / `OBLIGATIONS.md`

END_OF_FILE: workflow/project_setup/UNIVERSAL_DIRECTION_PROJECT_INSTALLER.md
