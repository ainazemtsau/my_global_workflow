# Packet and Transfer Interface

status: active_interface_layer

## Purpose

This interface defines packet transfer surfaces for Workflow v3.

## Packet surfaces

| Surface | Purpose | Required transfer fields |
| --- | --- | --- |
| Launch Packet | Starts bounded work on a material surface. | target, source authority, context, scope, expected result, evidence, return destination, blockers. |
| Result Packet | Returns candidate result and evidence. | result, evidence, source/read limitations, not done, assumptions, risks, return destination, candidate-state notice. |
| Transition Packet | Transfers selected next step to another surface. | packet type, selected target, same-chat/external run flags, return destination, closure signal, copy-paste packet. |
| Next Chat Prompt | Starts next material chat after current target closes. | chat role, parent context if any, target, scope, expected result, closure signal required, required return fields. |
| Codex handoff | Bounded repository implementation. | repo, base ref, branch, allowed/forbidden paths, required reads/changes, validation, commit/push instruction, return fields. |
| Codex result verification request | Verifies Codex output. | branch, commit/diff, changed files, validation results, allowed/forbidden path checks, residual risks. |
| child chat launch | Launches child support for current parent target. | parent target, required child result, sources, return destination, closure signal, required return fields. |
| check job launch | Launches bounded verification. | source question, relation, sources, expected finding, return destination, closure signal. |
| human decision request | Requests human judgment/permission/acceptance. | decision question, evidence summary, options, consequences, return destination. |

## Required transfer concepts

- `return_destination` states where the result must come back.
- `returns_to_current_chat` states whether the external surface returns to the current chat for verification or closure.
- `closure_signal` states the fact emitted when the transfer returns/closes.
- `copy_paste_packet` must be complete enough that the user does not build prompts manually.

## Hard rules

- User must not build prompts manually.
- A packet that says only "create a prompt/package" is incomplete.
- Child chat launch is not next material chat launch.
- Codex result returns for verification/closure before acceptance.
- Transfer output remains candidate until accepted or explicitly launched.

END_OF_FILE: workflow_v3/interfaces/08_PACKET_AND_TRANSFER_INTERFACE.md
