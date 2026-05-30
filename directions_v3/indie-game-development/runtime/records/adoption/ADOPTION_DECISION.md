# Adoption Decision

status: recorded
decision_id: ADOPT-IDG-V3-CLEAN-START-2026-05-30
direction_id: indie-game-development
adoption_mode: clean_start
legacy_import: none
imported_legacy_state: none

## Decision

Create the clean-start Workflow v3 runtime root for Indie Game Development under the corrected Direction namespace.

This decision creates the runtime shell, current-state placeholders, first Active Front, indexes, operations surfaces, config, and read-only console source index.

## Not Accepted By This Decision

- product root result;
- success conditions;
- old Direction state;
- old Ledger;
- old Obligations;
- old Receipts;
- old Dashboard;
- old Migration receipt;
- old project_setup;
- old project_files;
- archive content;
- run history.

accepted_product_root_result: pending_current_human_decision
accepted_success_conditions: pending_current_human_decision

## Legacy Boundary

Old directions/indie-game-development/** files are legacy_evidence only.

No old Ledger, Obligations, Receipts, Dashboard, Migration receipt, project_setup, project_files, archive, or run history becomes accepted_v3_state.

## Project Setup Boundary

Project Instructions UI update: none
Project Files/Sources refresh: none
request-only sources refresh: none
future Project name: Workflow v3 — Indie Game Development

## Next Move

next move: define current Direction Spine from current human decision

END_OF_FILE: directions_v3/indie-game-development/runtime/records/adoption/ADOPTION_DECISION.md
