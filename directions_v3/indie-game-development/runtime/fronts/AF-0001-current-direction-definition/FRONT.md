# AF-0001 Current Direction Definition

status: active
front_id: AF-0001-current-direction-definition
direction_id: indie-game-development
front_type: direction_spine_definition
adoption_mode: clean_start
legacy_import: none

## Target

Define the current Direction Spine for Indie Game Development from a current human decision.

## Expected Result

A later explicit acceptance/update path records:

- accepted_product_root_result;
- accepted_success_conditions;
- initial spine points or tracks if supplied;
- next Active Front after the Direction Spine is accepted.

Current values remain pending:

- accepted_product_root_result: pending_current_human_decision
- accepted_success_conditions: pending_current_human_decision

## Allowed Context

Current human input is the required authority for accepted Workflow v3 Direction state.

Old directions/indie-game-development/** files may be inspected only as legacy_evidence if a later bounded request authorizes that inspection.

## Forbidden Outcomes

- importing legacy state;
- treating old Ledger, Obligations, Receipts, Dashboard, Migration receipt, project_setup, project_files, archive, or run history as accepted_v3_state;
- updating Project Instructions UI;
- refreshing Project Files/Sources;
- starting product execution.

## Work Graph

See `WORK_GRAPH.md`.

END_OF_FILE: directions_v3/indie-game-development/runtime/fronts/AF-0001-current-direction-definition/FRONT.md
