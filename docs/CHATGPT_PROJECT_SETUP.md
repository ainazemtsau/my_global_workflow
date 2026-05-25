# ChatGPT Project Setup

```yaml
artifact_control:
  artifact_name: "ChatGPT Project Setup"
  schema: proof_chatgpt_project_setup.v1
  owner_layer: setup_documentation
  status: active
  repo_path: "docs/CHATGPT_PROJECT_SETUP.md"
  authority: "Setup guide for Proof-Carrying Workflow OS ChatGPT Projects; proof_workflow/** and Direction proof ledgers remain authoritative"
  freshness: refresh_when_proof_project_setup_or_manifest_changes
```

## Purpose

Use this file to create or refresh ChatGPT Projects for the Proof-Carrying Workflow OS.

This file is setup documentation. It is not runtime state and does not create accepted Ledger state.

## Project Model

Create one ChatGPT Project per Direction.

Each Direction Project should use:

- Project Instructions source: `directions/<direction-id>/proof/project_setup/CHATGPT_PROJECT_INSTRUCTIONS.md`
- Project Files Manifest source: `directions/<direction-id>/proof/project_setup/PROJECT_FILES_MANIFEST.md`

The manifest defines the exact shared proof workflow files and Direction proof files to upload.

## Required Shared Proof Files

Load shared files from `proof_workflow/**` according to the Direction's `PROJECT_FILES_MANIFEST.md`.

Typical shared sources include:

- `proof_workflow/00_PROOF_CARRYING_WORKFLOW_OS.md`
- `proof_workflow/01_SEMANTIC_KERNEL.md`
- `proof_workflow/02_RUNTIME_PROTOCOLS.md`
- `proof_workflow/03_PROOF_AND_COMMIT_POLICY.md`
- `proof_workflow/04_TRANSPORT_PROTOCOL.md`
- `proof_workflow/08_CHATGPT_PROJECT_SETUP.md`
- `proof_workflow/09_STORAGE_LAYOUT_POLICY.md`
- `proof_workflow/10_CONTEXT_AUTHORITY_POLICY.md`
- `proof_workflow/11_HUMAN_INPUT_NORMALIZATION_POLICY.md`
- `proof_workflow/12_HUMAN_FACING_RUN_CLOSURE_POLICY.md`
- `proof_workflow/13_RECURSIVE_CHILD_HANDOFF_POLICY.md`
- `proof_workflow/invariants/CORE_INVARIANTS.md`
- required transport cards under `proof_workflow/transport/`

## Required Direction Proof Files

Load Direction proof files from `directions/<direction-id>/proof/**` according to the Direction's manifest.

Typical Direction proof sources include:

- `directions/<direction-id>/proof/LEDGER.md`
- `directions/<direction-id>/proof/OBLIGATIONS.md`
- `directions/<direction-id>/proof/RECEIPTS_INDEX.md`
- `directions/<direction-id>/proof/COMMIT_SCOPES.md`
- `directions/<direction-id>/proof/DASHBOARD.md`
- `directions/<direction-id>/proof/MIGRATION_RECEIPT.md`

Receipt files may be uploaded when the manifest requires them or when a run needs direct receipt context.

## Forbidden Default Loads

Do not load these by default for new proof workflow Projects:

- `workflow/runtime/**`
- `workflow/stage_registry/**`
- `workflow/stage_prompts/**`
- `workflow/transport/**`
- `directions/*/project_files/**`
- `directions/*/project_setup/**`
- old docs setup files
- migration/admin files unless a Legacy Import Obligation requires them

Old files may be used only as legacy evidence through Legacy Import Receipt + Verify + Commit.

The old vNext-R runtime, stage registry, stage prompt, and transport files are not present as active surfaces in `main` after M3 cleanup. Use the legacy branch/tag if historical copies are needed.

## Currently Initialized Pilot

Indie Game Development is the initialized proof pilot.

Project Instructions source:

- `directions/indie-game-development/proof/project_setup/CHATGPT_PROJECT_INSTRUCTIONS.md`

Project Files Manifest source:

- `directions/indie-game-development/proof/project_setup/PROJECT_FILES_MANIFEST.md`

## Other Directions

Other Directions require proof skeleton initialization before normal proof project setup.

If a Direction lacks `directions/<direction-id>/proof/project_setup/`, initialize its proof skeleton first. Do not fall back to old vNext-R setup as active runtime.

## Refresh Rule

A GitHub commit does not update ChatGPT Project Files.

Manually refresh uploaded Project Files when any file listed in a Project Files Manifest changes.

Old ChatGPT Projects configured from vNext-R setup are obsolete for active workflow use. Create new proof workflow Projects or replace their instructions/files from the proof manifests.

## Read Completeness Rule

If a repository read is truncated, omitted, or tail-unverified, do not treat it as source authority for material proof work.

Return a Context Request with the exact path and blocker.

END_OF_FILE: docs/CHATGPT_PROJECT_SETUP.md
