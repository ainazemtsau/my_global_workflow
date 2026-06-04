# Chat Lifecycle and Handoff Eval

status: active_repository_completion_framework

## Source files to inspect

- `workflow_v3/interfaces/06_CHAT_LIFECYCLE_AND_HANDOFF_INTERFACE.md`
- `workflow_v3/interfaces/08_PACKET_AND_TRANSFER_INTERFACE.md`
- `workflow_v3/templates/TRANSITION_PACKET_TEMPLATE.md`
- `workflow_v3/templates/NEXT_CHAT_PROMPT_TEMPLATE.md`
- `workflow_v3/templates/PARENT_RECOVERY_BLOCK_TEMPLATE.md`
- `workflow_v3/runbooks/PARENT_CHILD_CHAT_RUNBOOK.md`

## Evidence required

- parent target;
- child launch packet if any;
- child result or missing-result evidence;
- FINISH_PACKET when lifecycle mode applies;
- return destination;
- Parent Recovery Block when multiple children are launched;
- FINISH_PACKET, Result Packet, and Next Move Packet.

## Lifecycle precheck

For material or state-sensitive chats, run CHAT_LIFECYCLE_PROTOCOL_EVAL before handoff-specific checks.

## PASS criteria

- Child chat serves current parent target and returns to parent.
- Child chat is not next material chat and not independent execution track.
- Parent remains synthesis authority.
- Missing required child result blocks synthesis.
- Transfer Packet or Next Chat Prompt is complete enough for copy-paste use.

## WARN criteria

- Optional child result is missing but parent identifies why synthesis can proceed.
- New material chat is needed but waits until current target is accepted, persisted, verified, or stopped.

## FAIL criteria

- Child chat treated as independent track.
- Child chat treated as next material chat.
- Missing child evidence synthesized.
- Parent Recovery Block missing when multiple children are launched.
- Transition Packet requires manual user assembly.
- Handoff emitted without FINISH_PACKET when lifecycle mode applies.

## Common failure modes

- Child outputs accepted without parent synthesis.
- Next material chat launched before current material target closes.
- Return destination omitted.

## Required recovery/repair action

Stop synthesis or launch, request missing child result or create Parent Recovery Block, rerun parent FINISH closure, and require explicit acceptance/update for state changes.

END_OF_FILE: workflow_v3/evals/CHAT_LIFECYCLE_HANDOFF_EVAL.md
