# Parent/Child Chat Runbook

status: active_repository_completion_framework

## Trigger condition

Use when the current parent target needs a bounded child chat, multiple child chats, child result synthesis, or parent recovery.

Trigger signals include `child_result_returned`, `child_missing_result`, `parent_child_coordination_issue`, `material_run_closed`, or `blocked_lifecycle_transition`.

## Input sources

- parent chat target;
- parent source authority and accepted records;
- child launch packet;
- child result packets;
- `workflow_v3/interfaces/06_CHAT_LIFECYCLE_AND_HANDOFF_INTERFACE.md`.

## Source authority classification

Parent-supplied exact sources and accepted records are authority. Child output is candidate support for parent synthesis. Project cache and child chat memory are not accepted state.

## Required templates

- `workflow_v3/templates/TRANSFER_PACKET_TEMPLATE.md`
- `workflow_v3/templates/NEXT_CHAT_PROMPT_TEMPLATE.md`
- `workflow_v3/templates/PARENT_RECOVERY_BLOCK_TEMPLATE.md`
- `workflow_v3/templates/RESULT_PACKET_TEMPLATE.md`
- `workflow_v3/templates/EVENT_LOOP_CLOSURE_TEMPLATE.md`

## Operating path

1. Confirm the child chat serves the current parent target.
2. State the required child result and return destination.
3. Include source authority, in scope, out of scope, expected result, and closure signal in the child prompt.
4. Require the child to return to parent.
5. Keep child chat distinct from next material chat.
6. Keep parent as synthesis authority.
7. When multiple children are launched, create Parent Recovery Block.
8. Block synthesis when required child result is missing.
9. Parent synthesizes child outputs and runs Event Loop Closure.

## Expected output

Child launch packet, child result packet, parent synthesis, Parent Recovery Block when needed, and exact Next Move.

## Closure signal

`child_result_returned`, `child_missing_result`, `material_run_closed`, or `blocked_lifecycle_transition`.

## Return destination

Child returns to parent chat. Parent returns to acceptance/update path or current Direction chat.

## Acceptance/update requirement

Child result and parent synthesis are candidate until explicit acceptance/update path.

## Failure/stop condition

Stop if a child becomes next material chat, an independent execution track, a state acceptor, a Codex committer, or a source of product route authority.

END_OF_FILE: workflow_v3/runbooks/PARENT_CHILD_CHAT_RUNBOOK.md
