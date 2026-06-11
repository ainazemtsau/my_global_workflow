# ChatGPT Project Setup

```yaml
artifact_control:
  artifact_name: "ChatGPT Project Setup"
  schema: workflow_chatgpt_project_setup.v2
  owner_layer: setup_documentation
  status: active
  repo_path: "docs/CHATGPT_PROJECT_SETUP.md"
  authority: "Setup guide for Workflow OS ChatGPT Projects; workflow/** and Direction proof ledgers remain authoritative"
  freshness: refresh_when_workflow_project_setup_pack_or_manifest_changes
```

## Purpose

Use this file to create or refresh ChatGPT Projects for the Workflow OS.

This file is setup documentation. It is not runtime state and does not create accepted Ledger state.

This file documents current/rollback Workflow OS Project setup. It is not Workflow v3 governance authority.

Workflow v3 Governance Maintenance Project behavior is governed by:

- `workflow_v3/project_setup/GOVERNANCE_MAINTENANCE_PROJECT_INSTRUCTIONS.md`

Exact repository files under `workflow_v3/**` win for Workflow v3 governance maintenance.

## Project Model

There are two supported ChatGPT Project types:

- Direction Workflow Project
- current/rollback Workflow OS Governance Maintenance Project

ChatGPT Project setup has separate surfaces:

- Project Instructions UI: the ChatGPT Project settings field where behavior instructions are pasted.
- Project Files/Sources: uploaded reference materials used as runtime context.
- Repository Project Instruction Source: a repository file or template that produces the text for the Project Instructions UI.
- Request-only sources: files or packs loaded only when an admitted task requires them.

Repository files named `CHATGPT_PROJECT_INSTRUCTIONS.md` are sources for the Project Instructions UI. Paste only the compact UI payload between markers into the Project Instructions field. Do not upload them as default Project Files/Sources.

## Project Instructions UI Payload Budget

The ChatGPT Project Instructions UI has a practical payload limit.

Generated Project Instructions UI payloads must be compact behavioral control text:

- hard max: 8,000 characters
- target max: 6,500 characters
- warning threshold: 7,200 characters

Count only the trimmed content between `BEGIN_CHATGPT_PROJECT_INSTRUCTIONS_UI_PAYLOAD` and `END_CHATGPT_PROJECT_INSTRUCTIONS_UI_PAYLOAD`.

Validation fails if any generated payload exceeds 8,000 characters.

Do not use the Project Instructions UI as workflow documentation, schema storage, or a Project File substitute. Put detailed workflow rules in canonical files and uploaded packs/files, and tell the model to inspect exact files when needed.

## Project Types

### Direction Workflow Project

A Direction Workflow Project runs the Workflow OS for one Direction.

Create one ChatGPT Project per ordinary Direction.

Direction Workflow Projects use the universal runtime setup and the Direction payload for that Direction.

They are allowed to use Dashboard/Obligations next-valid-run behavior according to their Project Instructions and manifest.

### Current/Rollback Workflow OS Governance Maintenance Project

The current/rollback Workflow OS Governance Maintenance Project services the Workflow OS repository.

It is a maintenance, audit, debug, research, setup, Codex handoff, and Codex result verification console.

It uses a different default upload set from ordinary Direction Workflow Projects.

This default upload set is current/rollback Workflow OS cache. Do not use it as Workflow v3 Governance Maintenance authority.

It must not start from Dashboard/Obligations next valid run.

It must not ask for root objective unless the user's specific issue is about root objective state.

It must not default-load Direction payload files.

Its Project Instructions source is:

- `directions/workflow-governance/workflow/project_setup/CHATGPT_PROJECT_INSTRUCTIONS.md`

Its Project Files/Sources manifest source is:

- `directions/workflow-governance/workflow/project_setup/PROJECT_FILES_MANIFEST.md`

Its default Project Files/Sources are:

- `WORKFLOW_SOURCE_OF_TRUTH.md`
- `workflow/project_packs/GOVERNANCE_MAINTENANCE_PACK.md`
- `workflow/project_packs/PROJECT_PACKS_INDEX.md`
- `docs/CHATGPT_PROJECT_SETUP.md`
- `workflow/policies/08_CHATGPT_PROJECT_SETUP.md`

`PROJECT_PACKS_INDEX.md` is default only for the current/rollback Workflow OS Governance Maintenance Project because that project is explicitly a setup and pack inspection console. It remains request-only for ordinary Direction Workflow Projects.

Workflow runtime packs and Workflow Governance Direction payload files are request-only in the maintenance project.

Workflow v3 Governance Maintenance uses repository authority under `workflow_v3/**`, with `workflow_v3/project_setup/GOVERNANCE_MAINTENANCE_PROJECT_INSTRUCTIONS.md` as the Project Instructions UI source.

## Direction Workflow Project Setup

New ordinary Direction Workflow Projects should use:

- Universal installer: `workflow/project_setup/UNIVERSAL_DIRECTION_PROJECT_INSTALLER.md`
- Universal instructions template: `workflow/project_setup/UNIVERSAL_DIRECTION_PROJECT_INSTRUCTIONS.md`
- Universal manifest template: `workflow/project_setup/UNIVERSAL_PROJECT_FILES_MANIFEST_TEMPLATE.md`
- Setup validation checklist: `workflow/project_setup/PROJECT_SETUP_VALIDATION_CHECKLIST.md`

Per-Direction manifests for ordinary Direction Workflow Projects remain under:

- `directions/<direction-id>/<active-project-setup>/CHATGPT_PROJECT_INSTRUCTIONS.md`
- `directions/<direction-id>/<active-project-setup>/PROJECT_FILES_MANIFEST.md`

Per-Direction Project Files manifests use the pack model and list only uploaded Project Files/Sources plus request-only sources.

## Direction Default Shared Packs

After the Project Instructions UI is updated, ordinary Direction Workflow Projects should upload these shared packs as Project Files/Sources:

- `workflow/project_packs/UNIVERSAL_PROJECT_SHELL_PACK.md`
- `workflow/project_packs/WORKFLOW_BASE_PACK.md`
- `workflow/project_packs/TRANSPORT_CORE_PACK.md`

The packs are runtime cache / upload convenience files. They are not semantic authority. Canonical source files listed in each pack remain authority.

## Direction Required Payload

For ordinary Direction Workflow Projects, upload Direction proof files from the Direction's active payload directory as Project Files/Sources. For the inspected Directions, `direction.meta.yml` and the Project Files manifest resolve `<active-direction-state>` to `workflow`:

- `directions/<direction-id>/<active-direction-state>/LEDGER.md`
- `directions/<direction-id>/<active-direction-state>/OBLIGATIONS.md`
- `directions/<direction-id>/<active-direction-state>/RECEIPTS_INDEX.md`
- `directions/<direction-id>/<active-direction-state>/COMMIT_SCOPES.md`
- `directions/<direction-id>/<active-direction-state>/DASHBOARD.md`
- `directions/<direction-id>/<active-direction-state>/MIGRATION_RECEIPT.md`

Receipt files may be uploaded when the manifest requires them or when a run needs direct receipt context.

## Request-Only Sources

Load `workflow/project_packs/EXECUTION_HARNESS_PACK.md` only when execution readiness, product repo setup, CodexRun, validation, human-guided execution, or complex technical mission work is admitted.

The Execution Harness Pack is not a default load for all Projects.

For ordinary Direction Workflow Projects, load `workflow/project_packs/PROJECT_PACKS_INDEX.md` only when a setup inspection task explicitly needs the index or it is already uploaded and must be refreshed.

## Forbidden Default Loads

Do not load these by default for new workflow Projects:

- old vNext-R workflow evidence from legacy branch/tag
- `directions/*/project_files/**`
- `directions/*/*/project_setup/**` as Project Files/Sources, including `CHATGPT_PROJECT_INSTRUCTIONS.md`
- old docs setup files
- migration/admin files unless a Legacy Import Obligation requires them
- product repo `.execution/**` files inside this workflow repository

Old files may be used only as legacy evidence through Legacy Import Receipt + Verify + Commit.

The active `workflow/` directory is the current Workflow OS namespace. Use the legacy branch/tag if old vNext-R historical copies are needed.

## Active Manifest Model

The older per-Direction 31-file manifests are superseded.

Ordinary Direction Workflow Project creation should use pack-based manifests.

Ordinary Direction default upload is three shared packs plus six Direction payload files.

The current/rollback Workflow OS Governance Maintenance Project default upload is the five-file maintenance-console set listed in Project Types.

Project Instructions are pasted into the Project Instructions UI. They are not uploaded Project Files/Sources and do not count toward the default upload count.

Direction payload files are live state.

Do not fall back to old vNext-R setup as active runtime.

## Refresh Rule

A GitHub commit does not update ChatGPT Project surfaces.

When Project Instructions source text changes, paste the updated UI payload into the ChatGPT Project Instructions field. Do not classify that update as an uploaded Project Files/Sources refresh.

When Project Instructions source text changes, report the measured UI payload character count for each changed instruction source.

If a pack source file changes, regenerate or refresh the pack and replace the uploaded Project File/Source before the next material run that depends on it.

If a Direction payload file changes, refresh that uploaded Project File/Source before the next material run that depends on it.

Refresh handoffs must separate:

- `project_instruction_ui_update_required`
- `project_sources_files_refresh_required`
- `request_only_sources_refresh_required`
- `do_not_upload_as_project_file`

Old ChatGPT Projects configured from vNext-R setup are obsolete for active workflow use. Create new workflow Projects or replace their Project Instructions UI content and Project Files/Sources from the workflow setup sources.

## Read Completeness Rule

If a repository read is truncated, omitted, or tail-unverified, do not treat it as source authority for material workflow work.

Return a Context Request with the exact path and blocker.

END_OF_FILE: docs/CHATGPT_PROJECT_SETUP.md
