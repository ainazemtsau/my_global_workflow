# Next Move Packet Eval

status: active_repository_completion_framework

## Purpose

Validate that closure selects exactly one primary next move with explicit boundaries.

## Evidence required

- Next Move Packet includes primary_next_move, next_move_type, return_destination, transfer_packet_if_needed, persistence_boundary, acceptance_boundary, and blocking_reason_if_any.
- `next_move_type` is one of the allowed values in `CHAT_FINISH_PROTOCOL.md`.
- Transfer Packet is complete when transfer is needed and includes transfer_target, why_transfer_needed, source_context, exact_task, allowed_scope, forbidden_scope, required_sources, required_outputs, return_destination, and copy_paste_packet.
- External transfer next_move_type has a complete Transfer Packet with copy_paste_packet.
- Evidence shows this is closure routing after the selected procedure completes or stops, not a mid-RUN RUN_EXTERNAL_HANDOFF.

## PASS criteria

- Exactly one primary next move is selected.
- No hidden launch occurs.
- Persistence and acceptance boundaries are explicit.
- Blocking reason is present when the result is blocked.
- When an external surface is selected, packet content is complete enough to copy/paste.
- RUN_EXTERNAL_HANDOFF is used instead when the selected owner RUN must wait for external evidence before FINISH_REQUEST.

## FAIL criteria

- Multiple primary next moves are selected.
- Required fields are missing.
- Transfer is needed but packet content lacks required core Transfer Packet fields.
- External transfer next_move_type has placeholder or vague `transfer_packet_if_needed`.
- User must assemble the Codex/check/child/next-chat prompt manually.
- Next Move Packet is used for a mid-RUN external handoff.
- `human_decision` is used to avoid a known required Transfer Packet.
- `transfer_packet_if_needed` says only "needed if using Codex", "use previous approved package", "prepare a prompt", "create Codex card", or equivalent.
- A next move is treated as accepted state without an acceptance/update path.

## Required recovery/repair action

Block continuation, repair the Next Move Packet, and require explicit acceptance/update before state changes.

END_OF_FILE: workflow_v3/evals/NEXT_MOVE_PACKET_EVAL.md
