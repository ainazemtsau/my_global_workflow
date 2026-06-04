# Next Move Packet Eval

status: active_repository_completion_framework

## Purpose

Validate that closure selects exactly one primary next move with explicit boundaries.

## Evidence required

- Next Move Packet includes primary_next_move, next_move_type, return_destination, transfer_packet_if_needed, persistence_boundary, acceptance_boundary, and blocking_reason_if_any.
- `next_move_type` is one of the allowed values in `CHAT_FINISH_PROTOCOL.md`.
- Transfer Packet is complete when transfer is needed.

## PASS criteria

- Exactly one primary next move is selected.
- No hidden launch occurs.
- Persistence and acceptance boundaries are explicit.
- Blocking reason is present when the result is blocked.

## FAIL criteria

- Multiple primary next moves are selected.
- Required fields are missing.
- Transfer is needed but packet content is incomplete.
- A next move is treated as accepted state without an acceptance/update path.

## Required recovery/repair action

Block continuation, repair the Next Move Packet, and require explicit acceptance/update before state changes.

END_OF_FILE: workflow_v3/evals/NEXT_MOVE_PACKET_EVAL.md
