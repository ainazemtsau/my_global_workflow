---
artifact_control:
  namespace: workflow
  artifact_type: project_setup_protocol
  status: gate_2_initial
  owner: workflow_os
---

# Project Setup Protocol

## Purpose

Project setup/adaptation is a receipt-backed execution prerequisite.

It establishes whether a target product/project repository can safely receive execution work and how validation should be run.

This protocol works for any stack. Unity, Web, and Python are examples only, not hardcoded assumptions.

## Project Modes

Existing projects use `adapt_existing_project`.

New projects use `create_new_project` only when the target Obligation explicitly authorizes new project creation.

Project-specific technical memory lives in the target product/project repository, not in the workflow governance repository.

## Setup Flow

Project Setup Protocol:

1. Identify project type, stack, runtime, package/tool managers, and repository boundaries.
2. Bind the target project/repository and allowed worktree.
3. Create or update `AGENTS.md`.
4. Create or update `.execution/project_profile.md`.
5. Create or update `.execution/validation_profile.md`.
6. Create or update `.execution/module_map.md`.
7. Create or update `.execution/technical_ledger.md`.
8. Create `.execution/receipts/` when absent.
9. Run setup validation, or return a setup_gap Receipt.

## Setup Receipt

The setup Operator must return a Project Setup Receipt that records:

- target project identity
- project type/profile
- setup mode
- technical memory status
- validation profile status
- module map status
- setup checks run
- setup gaps
- next allowed execution mode

## Setup Gap

If setup cannot be completed safely, the Operator returns `setup_gap`.

`setup_gap` must state what is missing, why execution would be unsafe, and which Human Action Card or residual Obligation can resolve the gap.

No CodexRun may proceed until setup status is known.

END_OF_FILE: execution/01_PROJECT_SETUP_PROTOCOL.md
