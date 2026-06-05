# Chat Lifecycle and Handoff Eval

status: active_repository_completion_framework

## Source files to inspect

- `workflow_v3/interfaces/06_CHAT_LIFECYCLE_AND_HANDOFF_INTERFACE.md`
- `workflow_v3/interfaces/08_PACKET_AND_TRANSFER_INTERFACE.md`
- `workflow_v3/templates/TRANSFER_PACKET_TEMPLATE.md`
- `workflow_v3/templates/NEXT_CHAT_PROMPT_TEMPLATE.md`
- `workflow_v3/templates/PARENT_RECOVERY_BLOCK_TEMPLATE.md`
- `workflow_v3/procedures/PARENT_INTEGRATION_CHECK_PROCEDURE.md`

## Evidence required

- parent target;
- RUN_EXTERNAL_HANDOFF packet if mid-RUN external evidence is required;
- expected return fields for RUN_EXTERNAL_HANDOFF if present;
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
- Transfer Packet includes required core fields and is complete enough for copy-paste use.
- Transfer Packet core fields are transfer_target, why_transfer_needed, source_context, exact_task, allowed_scope, forbidden_scope, required_sources, required_outputs, return_destination, and copy_paste_packet.
- RUN_EXTERNAL_HANDOFF is distinguished from closure Transfer Packet / Next Move Packet.
- RUN_EXTERNAL_HANDOFF includes complete copy_paste_packet, expected_return_packet, validation requirements, and same-owner resume rule.
- RUN_EXTERNAL_RETURN matches the emitted handoff before synthesis or closure relies on it.

## WARN criteria

- Optional child result is missing but parent identifies why synthesis can proceed.
- New material chat is needed but waits until current target is accepted, persisted, verified, or stopped.

## FAIL criteria

- Child chat treated as independent track.
- Child chat treated as next material chat.
- Missing child evidence synthesized.
- Parent Recovery Block missing when multiple children are launched.
- Transfer Packet requires manual user assembly.
- Transfer Packet says only "needed if using Codex", "use previous approved package", "prepare a prompt", "create Codex card", or equivalent.
- Mid-RUN external handoff is represented as Next Move Packet instead of RUN_EXTERNAL_HANDOFF.
- RUN_EXTERNAL_HANDOFF lacks copy_paste_packet or expected return fields.
- RUN_EXTERNAL_RETURN resumes a different owner procedure.
- Handoff emitted without FINISH_PACKET when lifecycle mode applies.

## Common failure modes

- Child outputs accepted without parent synthesis.
- Next material chat launched before current material target closes.
- Return destination omitted.

## Required recovery/repair action

Stop synthesis or launch, request missing child result or create Parent Recovery Block, rerun parent FINISH closure, and require explicit acceptance/update for state changes.

END_OF_FILE: workflow_v3/evals/CHAT_LIFECYCLE_HANDOFF_EVAL.md
