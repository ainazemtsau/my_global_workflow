# FINISH_PACKET Eval

status: active_repository_completion_framework

## Purpose

Validate that FINISH closes one selected procedure with the required packet shape and no hidden launch.

## Evidence required

- START selected exactly one procedure.
- RUN executed only the selected procedure.
- FINISH occurred only after explicit FINISH or ФИНИШ.
- FINISH_PACKET contains lifecycle_state, finished_work, finish_self_audit, result_packet, and next_move_packet.
- finish_self_audit includes no_pending_required_external_return, no_post_finish_material_start, utility_outputs_not_procedure_switches, and no_hidden_next_launch.
- Result Packet is present exactly once.
- Next Move Packet is present exactly once.
- Next Move Packet includes a required complete transfer packet when it selects an external surface.

## PASS criteria

- finish_self_audit checks are PASS or any FAIL forces blocked or repair_required result status.
- FINISH_PACKET does not mutate accepted state.
- FINISH_PACKET does not launch the selected next move invisibly.
- FINISH_PACKET does not close unresolved external handoff work.
- Utility outputs are audited as not procedure switches.
- Source/read limitations are stated.
- FINISH self-audit fails if next_move_packet lacks a required complete transfer packet.

## FAIL criteria

- FINISH_PACKET missing required fields.
- More than one selected procedure is closed.
- Result Packet or Next Move Packet is missing.
- FINISH output mutates state or launches work by implication.
- FINISH_PACKET is emitted while a required RUN_EXTERNAL_RETURN is pending.
- FINISH self-audit omits no_pending_required_external_return, no_post_finish_material_start, utility_outputs_not_procedure_switches, or no_hidden_next_launch.
- next_move_packet selects an external surface but lacks a complete Transfer Packet with copy_paste_packet.

## Required recovery/repair action

Block the closure claim, produce a corrected FINISH_PACKET, or return typed STOP if the required packets cannot be produced.

END_OF_FILE: workflow_v3/evals/FINISH_PACKET_EVAL.md
