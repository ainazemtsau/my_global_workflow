# Workflow v3 Project Setup Index

status: active_project_setup_index

## Purpose

This directory contains repository source files for Workflow v3 ChatGPT Project setup.

Repository setup files define behavior surfaces, manifests, launch packets, and validation checklists. They do not create accepted Direction state, do not update actual ChatGPT Project surfaces, and do not create runtime roots.

## Project setup surface taxonomy

- Project Instructions UI: the external ChatGPT Project settings field where compact behavior instructions are pasted.
- Project Files/Sources: external uploaded sources used as cache/context only.
- Repository Project Instruction Source: repository source text used to produce Project Instructions UI payloads.
- Request-only sources: exact files loaded only when a bounded task needs them.
- Do-not-upload files: repository sources that must stay GitHub/repository authoritative and must not be uploaded as default Project Files/Sources.

## Project types

- Governance Maintenance Console: repository governance, setup maintenance, audits, repair design, Codex handoffs, and Codex result verification.
- Ordinary Direction Project: one ChatGPT Project for one Workflow v3 Direction after the user chooses to create it.

## Current status

- Governance Maintenance Console Project Instructions UI was already manually updated and recorded in `workflow_v3/project_setup/rollouts/GOVERNANCE_MAINTENANCE_PROJECT_ROLLOUT_RESULT.md`.
- Ordinary Direction Project setup is repository-ready, but no ordinary Direction Project has been manually created from these files.
- Ordinary Direction Project first chat is setup-only root bootstrap; semantic Direction Definition is a separate later step.
- No ordinary Direction Project binding or concrete Direction runtime root is present after this cleanup.
- No Direction adoption happens from setup docs alone.
- No `directions_v3/<direction-id>/runtime/**` root is created from setup docs alone.
- Actual Project Instructions UI updates, Project Files/Sources refreshes, and request-only source refreshes require explicit future user action or rollout evidence.

## Index

- `CHATGPT_PROJECT_CREATION_GUIDE.md` - future Project creation guide and naming rules.
- `UNIVERSAL_DIRECTION_PROJECT_INSTALLER.md` - human-facing installer for a new ordinary Workflow v3 Direction Project.
- `UNIVERSAL_DIRECTION_PROJECT_INSTRUCTIONS.md` - compact Project Instructions UI payload source for ordinary Direction Projects.
- `UNIVERSAL_DIRECTION_PROJECT_FILES_MANIFEST_TEMPLATE.md` - template for future ordinary Direction Project Files/Sources decisions.
- `DIRECTION_ROOT_BOOTSTRAP_LAUNCH_PACKET_TEMPLATE.md` - first-chat launch packet template for a newly created ordinary Direction Project.
- `DIRECTION_SETUP_ONLY_ROOT_BOOTSTRAP_PROTOCOL.md` - setup-only root/bootstrap protocol.
- `DIRECTION_DEFINITION_LAUNCH_PACKET_TEMPLATE.md` - first semantic Direction Definition launch packet after setup-only root.
- `DIRECTION_PROJECT_BINDING_AND_CONTINUATION_PROTOCOL.md` - binding and later-chat continuation protocol for ordinary Direction Projects.
- `PER_DIRECTION_PROJECT_INSTRUCTIONS_SOURCE_TEMPLATE.md` - template for future bound per-Direction Project Instructions source.
- `PER_DIRECTION_PROJECT_FILES_MANIFEST_TEMPLATE.md` - template for future bound per-Direction Project Files/Sources manifest.
- `DIRECTION_PROJECT_SETUP_VALIDATION_CHECKLIST.md` - manual validation checklist for ordinary Direction Project creation.
- `PROJECT_FILES_MANIFEST_TEMPLATE.md` - general Workflow v3 Project Files/Sources manifest template.
- `GOVERNANCE_MAINTENANCE_PROJECT_INSTRUCTIONS.md` - compact Project Instructions UI payload source for the Governance Maintenance Console.
- `GENERIC_AI_PROVIDER_SETUP.md` - setup contract for supported AI/provider adapters.
- `rollouts/` - recorded external/manual rollout evidence.

END_OF_FILE: workflow_v3/project_setup/README.md
