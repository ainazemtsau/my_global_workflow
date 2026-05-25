---
artifact_control:
  namespace: direction_proof_project_setup
  direction_id: indie-game-development
  artifact_type: project_files_manifest
  project_name: "Indie Game Development — Proof Pilot"
  status: gate_2_2_initial
  owner: proof_carrying_workflow_os
---

# Indie Game Development — Proof Pilot Project Files Manifest

## Project

Project name: Indie Game Development — Proof Pilot

Project Instructions source:

- `directions/indie-game-development/proof/project_setup/CHATGPT_PROJECT_INSTRUCTIONS.md`

## Required Shared Proof Workflow Files

- `proof_workflow/00_PROOF_CARRYING_WORKFLOW_OS.md`
- `proof_workflow/01_SEMANTIC_KERNEL.md`
- `proof_workflow/02_RUNTIME_PROTOCOLS.md`
- `proof_workflow/03_PROOF_AND_COMMIT_POLICY.md`
- `proof_workflow/04_TRANSPORT_PROTOCOL.md`
- `proof_workflow/05_OPERATOR_CATALOG_POLICY.md`
- `proof_workflow/06_PROJECTION_POLICY.md`
- `proof_workflow/07_MIGRATION_PROTOCOL.md`
- `proof_workflow/08_CHATGPT_PROJECT_SETUP.md`
- `proof_workflow/09_STORAGE_LAYOUT_POLICY.md`
- `proof_workflow/10_CONTEXT_AUTHORITY_POLICY.md`
- `proof_workflow/invariants/CORE_INVARIANTS.md`

## Required Transport/Card Files

- `proof_workflow/transport/OPERATOR_LAUNCH_CARD.md`
- `proof_workflow/transport/RECEIPT_CARD.md`
- `proof_workflow/transport/CONTEXT_REQUEST_CARD.md`
- `proof_workflow/transport/HUMAN_DECISION_CARD.md`
- `proof_workflow/transport/COMMIT_PACKET.md`
- `proof_workflow/transport/LEGACY_IMPORT_RECEIPT_CARD.md`

## Required Pilot Direction Proof Files

- `directions/indie-game-development/proof/LEDGER.md`
- `directions/indie-game-development/proof/OBLIGATIONS.md`
- `directions/indie-game-development/proof/RECEIPTS_INDEX.md`
- `directions/indie-game-development/proof/COMMIT_SCOPES.md`
- `directions/indie-game-development/proof/DASHBOARD.md`
- `directions/indie-game-development/proof/MIGRATION_RECEIPT.md`

## Do Not Load By Default

- `workflow/runtime/**`
- `workflow/stage_registry/**`
- `workflow/stage_prompts/**`
- `workflow/transport/**`
- `directions/indie-game-development/project_files/**`
- `directions/indie-game-development/project_setup/**`
- `directions/*/project_files/**`
- `directions/*/project_setup/**`
- `migration/**`
- old docs setup files

## Refresh Rule

If any required Project File changes in GitHub, manually replace the matching uploaded ChatGPT Project File before the next material proof run.

## Restoration Steps

1. Create ChatGPT Project named "Indie Game Development — Proof Pilot".
2. Paste Project Instructions from `CHATGPT_PROJECT_INSTRUCTIONS.md`.
3. Upload all files listed in this manifest.
4. Do not upload forbidden legacy files.
5. Start a new chat with one Operator invocation over one Obligation.

END_OF_FILE: directions/indie-game-development/proof/project_setup/PROJECT_FILES_MANIFEST.md
