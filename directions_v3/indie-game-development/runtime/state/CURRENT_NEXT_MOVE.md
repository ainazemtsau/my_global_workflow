# Current Next Move

direction_id: indie-game-development

next_move_status: accepted
formation_runbook_ref: workflow_v3/formation/CURRENT_NEXT_MOVE_FORMATION_RUNBOOK.md
formation_eval_ref: workflow_v3/evals/CURRENT_NEXT_MOVE_FORMATION_EVAL.md

source_event_loop_closure_ref: setup_only_root_bootstrap_event_loop_closure
source_progression_router_result_ref: progression_router_handler: launch_direction_definition

primary_next_move: launch_direction_definition

reason:
- setup-only runtime root exists as a technical continuation surface
- semantic Direction Definition is pending
- Direction Spine, Direction Map, and Active Front are not accepted and must be formed later

destination_surface: workflow_v3/project_setup/DIRECTION_DEFINITION_LAUNCH_PACKET_TEMPLATE.md

same_chat_allowed: false
new_chat_needed: true

transition_packet_ref_or_inline:
Use Direction Definition launch packet after this setup-only root package is accepted/merged and Project Instructions UI is manually updated from the generated per-Direction source.

blocked_if:
- Project Binding source is missing, conflicted, stale, or unreadable
- setup-only root package has not been accepted/merged
- Project Instructions UI binding capsule has not been manually updated when required
- user tries to start product work before Direction Definition

return_destination:
ordinary Direction Project parent chat / Direction Definition launch chat

acceptance_or_launch_requirement:
Launch Direction Definition only after setup-only root package acceptance/merge and binding verification.

limitations:
- Current Next Move is not product work.
- Current Next Move does not accept Spine, Map, Front, Work Graph, or strategy.
