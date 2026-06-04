# FINISH_PACKET Eval

status: active_repository_completion_framework

## Purpose

Validate that FINISH closes one selected procedure with the required packet shape and no hidden launch.

## Evidence required

- START selected exactly one procedure.
- RUN executed only the selected procedure.
- FINISH occurred only after explicit FINISH or ФИНИШ.
- FINISH_PACKET contains lifecycle_state, finished_work, finish_self_audit, result_packet, and next_move_packet.
- Result Packet is present exactly once.
- Next Move Packet is present exactly once.

## PASS criteria

- finish_self_audit checks are PASS or any FAIL forces blocked or repair_required result status.
- FINISH_PACKET does not mutate accepted state.
- FINISH_PACKET does not launch the selected next move invisibly.
- Source/read limitations are stated.

## FAIL criteria

- FINISH_PACKET missing required fields.
- More than one selected procedure is closed.
- Result Packet or Next Move Packet is missing.
- FINISH output mutates state or launches work by implication.

## Required recovery/repair action

Block the closure claim, produce a corrected FINISH_PACKET, or return typed STOP if the required packets cannot be produced.

END_OF_FILE: workflow_v3/evals/FINISH_PACKET_EVAL.md
