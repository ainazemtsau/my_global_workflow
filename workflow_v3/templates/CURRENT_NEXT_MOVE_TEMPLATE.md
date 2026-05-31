# Current Next Move Template

status: template

## Current Next Move

`direction_id`:

`next_move_status`: candidate | accepted | blocked | stopped

`source_event_loop_closure_ref`:

`source_progression_router_result_ref`:

`primary_next_move`:

`reason`:

`destination_surface`:

`same_chat_allowed`:

`new_chat_needed`:

`transition_packet_ref_or_inline`:

`blocked_if`:

`return_destination`:

`acceptance_or_launch_requirement`:

`limitations`:

## Boundary

Next Move is not accepted state by itself.

Route-changing or state-changing next moves require visible Event Loop Closure, Progression Router output, and acceptance/update path when state changes.

This template does not adopt a Direction, create runtime state, or launch work.

END_OF_FILE: workflow_v3/templates/CURRENT_NEXT_MOVE_TEMPLATE.md
