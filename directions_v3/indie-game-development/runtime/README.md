# Indie Game Development Workflow v3 Runtime

status: active_runtime_root_created
direction_id: indie-game-development
adoption_mode: clean_start
legacy_import: none
imported_legacy_state: none
accepted_product_root_result: pending_current_human_decision
accepted_success_conditions: pending_current_human_decision

## Purpose

This is the clean-start Workflow v3 runtime root for the Indie Game Development Direction.

It creates only the current runtime storage shell and the first Active Front needed to define the current Direction Spine from a current human decision.

## Authority Boundary

Shared Workflow v3 rules and setup sources remain under `workflow_v3/**`.

This runtime root stores only per-Direction runtime state for `indie-game-development`.

Old directions/indie-game-development/** files are legacy_evidence only. They may inform a later current human decision, but they are not imported and do not become accepted_v3_state.

No old Ledger, Obligations, Receipts, Dashboard, Migration receipt, project_setup, project_files, archive, or run history becomes accepted_v3_state.

## Current State

- adoption_mode: clean_start
- legacy_import: none
- imported_legacy_state: none
- accepted_product_root_result: pending_current_human_decision
- accepted_success_conditions: pending_current_human_decision
- active_front: AF-0001-current-direction-definition
- Runtime Console: read-only
- next move: define current Direction Spine from current human decision

## Project Setup Boundary

- Project Instructions UI update: none
- Project Files/Sources refresh: none
- request-only sources refresh: none
- future Project name: Workflow v3 — Indie Game Development
- do_not_upload_as_project_file: all files in this runtime root until a separate Project setup rollout package authorizes upload or refresh

## Runtime Layout

```text
state/
fronts/
records/
memory/
operations/
indexes/
config/
console/
```

END_OF_FILE: directions_v3/indie-game-development/runtime/README.md
