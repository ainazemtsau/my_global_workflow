# ChatGPT Project Setup

```yaml
artifact_control:
  artifact_name: "ChatGPT Project Setup"
  schema: workflow_chatgpt_project_setup.v2
  owner_layer: setup_documentation
  status: active
  repo_path: "docs/CHATGPT_PROJECT_SETUP.md"
  authority: "Setup guide for Workflow OS ChatGPT Projects; root workflow files and directories and Direction proof ledgers remain authoritative"
  freshness: refresh_when_workflow_project_setup_pack_or_manifest_changes
```

## Purpose

Use this file to create or refresh ChatGPT Projects for the Workflow OS.

This file is setup documentation. It is not runtime state and does not create accepted Ledger state.

## Project Model

Create one ChatGPT Project per Direction.

New Workflow Projects should use:

- Universal installer: `project_setup/UNIVERSAL_DIRECTION_PROJECT_INSTALLER.md`
- Universal instructions template: `project_setup/UNIVERSAL_DIRECTION_PROJECT_INSTRUCTIONS.md`
- Universal manifest template: `project_setup/UNIVERSAL_PROJECT_FILES_MANIFEST_TEMPLATE.md`
- Setup validation checklist: `project_setup/PROJECT_SETUP_VALIDATION_CHECKLIST.md`

Per-Direction manifests remain under:

- `directions/<direction-id>/project_setup/CHATGPT_PROJECT_INSTRUCTIONS.md`
- `directions/<direction-id>/project_setup/PROJECT_FILES_MANIFEST.md`

Per-Direction manifests now use the pack model.

## Default Shared Packs

New Workflow Projects should upload these shared packs:

- `project_packs/UNIVERSAL_PROJECT_SHELL_PACK.md`
- `project_packs/WORKFLOW_BASE_PACK.md`
- `project_packs/TRANSPORT_CORE_PACK.md`

The packs are runtime cache / upload convenience files. They are not semantic authority. Canonical source files listed in each pack remain authority.

## Required Direction Payload

Upload Direction proof files from `directions/<direction-id>/**`:

- `directions/<direction-id>/LEDGER.md`
- `directions/<direction-id>/OBLIGATIONS.md`
- `directions/<direction-id>/RECEIPTS_INDEX.md`
- `directions/<direction-id>/COMMIT_SCOPES.md`
- `directions/<direction-id>/DASHBOARD.md`
- `directions/<direction-id>/MIGRATION_RECEIPT.md`

Receipt files may be uploaded when the manifest requires them or when a run needs direct receipt context.

## Request-Only Capability Packs

Load `project_packs/EXECUTION_HARNESS_PACK.md` only when execution readiness, product repo setup, CodexRun, validation, human-guided execution, or complex technical mission work is admitted.

The Execution Harness Pack is not a default load for all Projects.

## Forbidden Default Loads

Do not load these by default for new workflow Projects:

- `workflow/**`
- `workflow/runtime/**`
- `workflow/stage_registry/**`
- `workflow/stage_prompts/**`
- `workflow/transport/**`
- `directions/*/project_files/**`
- `directions/*/project_setup/**`
- old docs setup files
- migration/admin files unless a Legacy Import Obligation requires them
- product repo `.execution/**` files inside this workflow repository

Old files may be used only as legacy evidence through Legacy Import Receipt + Verify + Commit.

The old vNext-R `workflow/` tree is not present in active `main`. Use the legacy branch/tag if historical copies are needed.

## Active Manifest Model

The older per-Direction 31-file manifests are superseded.

New Project creation should use pack-based manifests.

Default upload is three shared packs plus six Direction payload files.

Project Instructions are behavior/setup instructions. Direction payload files are live state.

Do not fall back to old vNext-R setup as active runtime.

## Refresh Rule

A GitHub commit does not update ChatGPT Project Files.

If a pack source file changes, regenerate or refresh the pack and replace the uploaded Project File before the next material run that depends on it.

If a Direction payload file changes, refresh that uploaded Project File before the next material run that depends on it.

Old ChatGPT Projects configured from vNext-R setup are obsolete for active workflow use. Create new workflow Projects or replace their instructions/files from the workflow setup sources.

## Read Completeness Rule

If a repository read is truncated, omitted, or tail-unverified, do not treat it as source authority for material workflow work.

Return a Context Request with the exact path and blocker.

END_OF_FILE: docs/CHATGPT_PROJECT_SETUP.md
