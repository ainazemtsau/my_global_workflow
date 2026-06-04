# Packet and Transfer Interface

status: active_interface_layer

## Purpose

This interface defines packet transfer surfaces for Workflow v3.

## Packet surfaces

| Surface | Purpose | Required fields |
| --- | --- | --- |
| Launch Packet | Starts bounded work on a material surface. | target, source authority, context, scope, expected result, evidence, return destination, blockers. |
| FINISH_PACKET | Closes a selected procedure after explicit FINISH. | lifecycle_state, finished_work, finish_self_audit, result_packet, next_move_packet. |
| Result Packet | Returns candidate result and evidence. | status, result, evidence, changed files, validation, source/read limitations, not done, project refresh requirements, residual risks, exact next move. |
| Next Move Packet | Selects exactly one primary next move. | primary_next_move, next_move_type, return_destination, transfer_packet_if_needed, persistence_boundary, acceptance_boundary, blocking_reason_if_any. |
| Transfer Packet | Transfers selected next step to another surface. | transfer type, selected target, same-chat/external run flags, return destination, closure fact, copy-paste packet. |
| Next Chat Prompt | Starts next material chat after current target closes. | chat role, parent context if any, target, scope, expected result, FINISH closure required, required return fields. |
| Codex handoff | Bounded repository implementation. | repo, base ref, branch, allowed/forbidden paths, required reads/changes, validation, commit/push instruction, return fields. |
| Codex result verification request | Verifies Codex output. | branch, commit/diff, changed files, validation results, allowed/forbidden path checks, residual risks. |
| child chat launch | Launches child support for current parent target. | parent target, required child result, sources, return destination, closure fact, required return fields. |
| check job launch | Launches bounded verification. | source question, relation, sources, expected finding, return destination, closure fact. |
| human decision request | Requests human judgment/permission/acceptance. | decision question, evidence summary, options, consequences, return destination. |

## Required transfer concepts

- `return_destination` states where the result must come back.
- `returns_to_current_chat` states whether the external surface returns to the current chat for verification or closure.
- `closure_fact` states the fact emitted when the transfer returns/closes.
- `copy_paste_packet` must be complete enough that the user does not build prompts manually.

## Hard rules

- User must not build prompts manually.
- A packet that says only "create a prompt/package" is incomplete.
- Child chat launch is not next material chat launch.
- Codex result returns for verification/closure before acceptance.
- Transfer output remains candidate until accepted or explicitly launched.

END_OF_FILE: workflow_v3/interfaces/08_PACKET_AND_TRANSFER_INTERFACE.md
