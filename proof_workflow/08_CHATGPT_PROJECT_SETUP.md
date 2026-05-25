---
artifact_control:
  namespace: proof_workflow
  artifact_type: chatgpt_project_setup_principles
  status: gate_1_initial
  owner: proof_carrying_workflow_os
---

# ChatGPT Project Setup Principles

## Scope

This file defines future setup principles only.

It does not edit actual ChatGPT Project Instructions, old project setup files, old workflow files, or Direction project files.

The exact project setup switch is deferred to a later migration gate.

## Future Default Load Set

New proof workflow ChatGPT Projects should load the shared kernel and protocol docs under `proof_workflow/`.

Candidate shared load set:

- `proof_workflow/00_PROOF_CARRYING_WORKFLOW_OS.md`
- `proof_workflow/01_SEMANTIC_KERNEL.md`
- `proof_workflow/02_RUNTIME_PROTOCOLS.md`
- `proof_workflow/03_PROOF_AND_COMMIT_POLICY.md`
- `proof_workflow/04_TRANSPORT_PROTOCOL.md`
- `proof_workflow/05_OPERATOR_CATALOG_POLICY.md`
- `proof_workflow/06_PROJECTION_POLICY.md`
- `proof_workflow/07_MIGRATION_PROTOCOL.md`
- `proof_workflow/09_STORAGE_LAYOUT_POLICY.md`
- `proof_workflow/10_CONTEXT_AUTHORITY_POLICY.md`
- `proof_workflow/11_HUMAN_INPUT_NORMALIZATION_POLICY.md`
- `proof_workflow/12_HUMAN_FACING_RUN_CLOSURE_POLICY.md`
- `proof_workflow/13_RECURSIVE_CHILD_HANDOFF_POLICY.md`
- `proof_workflow/invariants/CORE_INVARIANTS.md`

Transport card docs may be loaded when a chat needs handoff, receipt, context request, human decision, legacy import, or commit serialization.

Candidate transport load set:

- `proof_workflow/transport/CODEX_COMMIT_HANDOFF_CARD.md`
- `proof_workflow/transport/CHILD_OBLIGATION_REQUEST_CARD.md`
- `proof_workflow/transport/CHILD_RESULT_RETURN_CARD.md`
- `proof_workflow/transport/PARENT_RECOVERY_BLOCK.md`

## Context Authority Setup Rule

Project Files may provide context, but only committed Ledger and Receipts provide accepted proof state.

Loaded domain files must be treated as candidate_context unless the Ledger says otherwise.

## Human Input Setup Rule

Proof Projects should not require users to answer in YAML.

Terse or spoken answers must be normalized when intent is clear.

## Run Closure Setup Rule

Proof Projects must not make the user build Codex tasks manually from Receipts.

Material runs must end with a human-readable terminal outcome and any needed copy-paste handoff.

Proof Projects must expect Codex Commit Handoff Cards to be fully self-contained.

Users should not manually construct repository maintenance wrappers from Receipts.

If a Codex handoff is not self-contained, the correct response is to ask the Operator chat to regenerate the handoff, not to patch it manually.

## Stored Project Setup Files

Proof ChatGPT Project Instructions must be stored in repository files.

Project Instructions provided only in chat are not restorable and are invalid for durable pilot setup.

Pilot Project setup files may live under:

- `directions/<direction-id>/proof/project_setup/`

For Indie Game Development Proof Pilot:

- `directions/indie-game-development/proof/project_setup/CHATGPT_PROJECT_INSTRUCTIONS.md`
- `directions/indie-game-development/proof/project_setup/PROJECT_FILES_MANIFEST.md`

Stored proof Project setup files are adapter/storage surfaces. They do not create accepted Ledger state.

## Legacy Non-Authority

Old workflow runtime files, old stage prompts, old project files, and old project setup files must not be default authority for the new proof workflow.

They may be loaded later only as explicitly identified legacy evidence for a migration Obligation.

## Direction Proof Files

Direction proof files will be loaded only after a Direction is migrated or initialized under a future `directions/<direction-id>/proof/` namespace.

Future direction load candidates:

- `directions/<direction-id>/proof/LEDGER.md`
- `directions/<direction-id>/proof/OBLIGATIONS.md`
- `directions/<direction-id>/proof/RECEIPTS_INDEX.md`
- `directions/<direction-id>/proof/COMMIT_SCOPES.md`
- `directions/<direction-id>/proof/DASHBOARD.md`

Direction-specific load sets become active only when their proof files exist and are selected by a stored Project Files manifest.

## Chat Rule

One ChatGPT chat should handle one Operator invocation over one Obligation.

If the work is compound, the chat must decompose or return `split_required` instead of pretending completion.

END_OF_FILE: proof_workflow/08_CHATGPT_PROJECT_SETUP.md
