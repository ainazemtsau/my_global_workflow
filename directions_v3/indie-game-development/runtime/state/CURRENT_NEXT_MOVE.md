# Current Next Move

direction_id: indie-game-development

next_move_status: accepted
formation_runbook_ref: workflow_v3/formation/CURRENT_NEXT_MOVE_FORMATION_RUNBOOK.md
formation_eval_ref: workflow_v3/evals/CURRENT_NEXT_MOVE_FORMATION_EVAL.md

source_event_loop_closure_ref: directions_v3/indie-game-development/runtime/operations/event_loop_closures/ELC-IDG-DIRECTION-SPINE-ACCEPT-2026-06-02.md
source_progression_router_result_ref: direction_definition_sequence_after_spine_acceptance

primary_next_move: form_direction_map

reason:
- Direction Spine is accepted as the first semantic v3 steering entity
- Direction Definition sequence requires Direction Map after Spine
- Direction Map must be formed before first Active Front formation
- product execution and Work Graph remain forbidden before Active Front acceptance

destination_surface: workflow_v3/formation/DIRECTION_MAP_FORMATION_RUNBOOK.md

same_chat_allowed: true
new_chat_needed: false

transition_packet_ref_or_inline:
Use the accepted Direction Spine at `directions_v3/indie-game-development/runtime/state/DIRECTION_SPINE.md` plus bounded legacy evidence refs already used in Direction Definition to form candidate Direction Map. Direction Map must remain candidate until explicit acceptance/update path. Do not create Work Graph or product execution.

blocked_if:
- Project Binding source is missing, conflicted, stale, or unreadable
- accepted Direction Spine cannot be read
- user tries to start product work before Direction Map and Active Front acceptance
- Direction Map result becomes roadmap, backlog, Work Graph, Action Inbox, or implementation plan

return_destination:
this Direction Definition chat

acceptance_or_launch_requirement:
Form candidate Direction Map; ask for explicit accept/repair/block/park decision before mutating accepted Map state.

limitations:
- Current Next Move is not product work.
- Current Next Move does not accept Direction Map, Active Front, Work Graph, Work Contract, or strategy.
- Product execution, CodexExecution, implementation, roadmap, engine/networking commitment, old-code transfer, Steam launch strategy, final gas taxonomy, and final reaction graph remain not admitted.

END_OF_FILE: directions_v3/indie-game-development/runtime/state/CURRENT_NEXT_MOVE.md
