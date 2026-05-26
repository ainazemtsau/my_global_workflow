---
artifact_control:
  namespace: workflow
  artifact_type: chatgpt_project_setup_principles
  status: u3_pack_model
  owner: workflow_os
---

# ChatGPT Project Setup Principles

## Scope

This file defines active setup principles for ChatGPT Direction Workflow Projects.

Project setup files are storage/adapter surfaces. They do not create accepted Ledger state.

Use `project_setup/UNIVERSAL_DIRECTION_PROJECT_INSTALLER.md` for new Projects.

## Universal Setup Model

New Direction Workflow Projects use one setup model:

- Universal Project Shell
- Shared Workflow Runtime Packs
- Direction Payload
- Optional Capability Packs
- Product Repo Execution Setup, handled separately in the target product repository

## Default Upload Surface

Use packs as the default shared upload surface:

- `project_packs/UNIVERSAL_PROJECT_SHELL_PACK.md`
- `project_packs/WORKFLOW_BASE_PACK.md`
- `project_packs/TRANSPORT_CORE_PACK.md`

Upload Direction payload files individually:

- `directions/<direction-id>/proof/LEDGER.md`
- `directions/<direction-id>/proof/OBLIGATIONS.md`
- `directions/<direction-id>/proof/RECEIPTS_INDEX.md`
- `directions/<direction-id>/proof/COMMIT_SCOPES.md`
- `directions/<direction-id>/proof/DASHBOARD.md`
- `directions/<direction-id>/proof/MIGRATION_RECEIPT.md`

## Active Manifest Model

Direction-specific manifests use the pack model.

The older 31-file Project Files model is superseded.

Default upload is three shared packs plus six Direction payload files.

Project Instructions are behavior/setup instructions. They must not store live state. Direction payload files win for live state.

## Request-Only Execution Harness

`project_packs/EXECUTION_HARNESS_PACK.md` is request-only.

Do not default-load the Execution Harness Pack unless execution readiness, product repo setup, CodexRun, validation, human-guided execution, or complex technical mission work is admitted.

Execution is not a semantic primitive.

Codex is not the execution system.

CodexRun is a gated Operator family inside execution.

## Stored Project Setup Files

Universal project setup sources live under:

- `project_setup/UNIVERSAL_DIRECTION_PROJECT_INSTALLER.md`
- `project_setup/UNIVERSAL_DIRECTION_PROJECT_INSTRUCTIONS.md`
- `project_setup/UNIVERSAL_PROJECT_FILES_MANIFEST_TEMPLATE.md`
- `project_setup/PROJECT_SETUP_VALIDATION_CHECKLIST.md`

Per-Direction generated setup files live under:

- `directions/<direction-id>/proof/project_setup/`

## Context Authority Setup Rule

Project Files may provide context, but only committed Ledger and Receipts provide accepted state.

Loaded domain files must be treated as candidate_context unless the Ledger says otherwise.

## Human Input Setup Rule

Workflow Projects should not require users to answer in YAML.

Terse or spoken answers must be normalized when intent is clear.

## Run Closure Setup Rule

Workflow Projects must not make the user build Codex tasks manually from Receipts.

Material runs must end with a human-readable terminal outcome and any needed copy-paste handoff.

Workflow Projects must expect Codex Commit Handoff Cards to be fully self-contained.

If a Codex handoff is not self-contained, the correct response is to ask the Operator chat to regenerate the handoff.

## Legacy Non-Authority

Old workflow runtime files, old stage prompts, old transport files, old Direction project files, and old project setup files must not be default authority for the workflow.

They may be loaded only as explicitly identified legacy evidence for a Legacy Import Obligation.

## Chat Rule

One ChatGPT chat should handle one Operator invocation over one Obligation.

If the work is compound, the chat must decompose or return `split_required` instead of pretending completion.

END_OF_FILE: 08_CHATGPT_PROJECT_SETUP.md
