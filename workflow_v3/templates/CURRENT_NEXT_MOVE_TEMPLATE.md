# Current Next Move Template

status: template

## Current Next Move

`direction_id`:

`next_move_status`: candidate | accepted | blocked | stopped

`procedure_path`: workflow_v3/procedures/CURRENT_NEXT_MOVE_FORMATION_PROCEDURE.md

`formation_eval_ref`: workflow_v3/evals/CURRENT_NEXT_MOVE_FORMATION_EVAL.md

`source_finish_packet_ref`:

`source_next_move_packet_ref`:

`entrypoint`:

`procedure_boundary`:

`procedure_path`:

`required_source_reads`:

`source_integrity_requirement`:

`allowed_operations`:

`forbidden_operations`:

`write_admission`:

`acceptance_admission`:

`legacy_policy`:

`stop_conditions`:

`primary_next_move`:

Allowed setup-only value:

```text
launch_direction_definition
```

`reason`:

`destination_surface`:

`same_chat_allowed`:

`new_chat_needed`:

`transfer_packet_ref_or_inline`:

`blocked_if`:

`return_destination`:

`acceptance_or_launch_requirement`:

`limitations`:

## Boundary

Next Move is not accepted state by itself.

Next Move is not action admission by itself.

Route-changing or state-changing next moves require procedure registry lookup, procedure boundary contract, FINISH_PACKET, Next Move Packet, admission, and acceptance/update path when state changes.

`same_chat_allowed` means non-mutating continuation only unless direct `storage_update` admission or gated external utility write authority is explicit.

This template does not adopt a Direction, create runtime state, or launch work.

`launch_direction_definition` routes to `workflow_v3/project_setup/DIRECTION_DEFINITION_LAUNCH_PACKET_TEMPLATE.md`.

END_OF_FILE: workflow_v3/templates/CURRENT_NEXT_MOVE_TEMPLATE.md
