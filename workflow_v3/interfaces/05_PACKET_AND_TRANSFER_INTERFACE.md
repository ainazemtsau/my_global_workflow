# Packet and Transfer Interface

status: active_interface_layer

## Purpose

This file defines packets and transfer between Workflow v3 surfaces.

## Owner/surface

Owner/surface: Launch Packet, Result Packet, Transition Packet, Next Chat Prompt, Codex handoff, Codex result verification request, Check Job launch, child chat launch, next material chat launch, and human decision request boundaries.

## Persistence target

Persistence target: `workflow_v3/interfaces/05_PACKET_AND_TRANSFER_INTERFACE.md` for shared rules; future adopted Direction packet records may be stored under `directions_v3/<direction-id>/runtime/records/**` or `operations/**` after explicit adoption and acceptance.

## Packet types

Launch Packet starts bounded work.

Result Packet returns bounded work output, evidence, limitations, and exact Next Move.

Transition Packet transfers a selected next step to another surface.

Next Chat Prompt is a complete prompt for a new chat when a new chat is needed.

Codex handoff packet is a Transition Packet with repository, base ref, branch policy, allowed paths, forbidden paths, required changes, validation, stop conditions, commit/push instructions when authorized, and requested return fields.

Codex result verification request asks the current chat or a bounded review surface to verify branch, commit, changed files, allowed paths, forbidden paths, validation output, EOF markers, project refresh categories, push status, and residual risks.

## Transfer surfaces

Transfer may target:

- human decision request;
- Codex handoff;
- Codex result verification request;
- Check Job launch;
- child chat launch;
- next material chat launch;
- stop or blocked result.

## Required transfer fields

A Transition Packet must include:

- `transition_packet_type`;
- `source_authority`;
- `runtime_root`;
- `selected_next_step_target`;
- `same_chat_allowed`;
- `external_run_needed`;
- `external_run_type`;
- `returns_to_current_chat`;
- `next_material_chat_needed`;
- `context_supplied`;
- `in_scope`;
- `out_of_scope`;
- `expected_result`;
- `validation_or_evidence_required`;
- `event_loop_closure_required`;
- `return_destination`;
- `copy_paste_packet`;
- `limitations`.

## Return flags

`return_destination` names where output must come back.

`returns_to_current_chat` states whether the external run result must return to the current chat for verification, acceptance review, or Event Loop Closure.

`same_chat_allowed` states whether the selected next move can be completed in the current chat without losing source, scope, or acceptance clarity.

`new_chat_needed` states whether a new chat is required for the next step.

`next_material_chat_needed` states whether the next accepted unit of material work requires a new material chat.

## Copy-paste packet requirement

When transfer is needed, the packet must provide a complete `copy_paste_packet`.

The user must not manually build prompts from partial fragments.

The packet may be concise, but it must include enough source authority, scope, expected result, evidence, and return rules for the target surface to run safely.

## Inputs

Inputs are Event Loop Closure, Progression Router result, Work Contract, Result Packet, source context, blockers, acceptance status, and target surface constraints.

## Outputs

Outputs are complete Launch Packets, Result Packets, Transition Packets, Next Chat Prompts, Codex handoffs, Check Job launches, child chat launches, human decision requests, and stop packets.

## State mutation rights

Packets do not mutate accepted state.

Launching a packet starts or requests candidate work. Acceptance and persistence remain separate.

## Allowed producers

Allowed producers are parent chats, Progression Router, Event Loop Closure, repository-maintenance packages, Check Job designers, and Codex package creators.

## Allowed consumers

Allowed consumers are ChatGPT chats, Codex, Claude Code/future code assistants, Deep Research/research agents, GitHub access, Check Jobs, human actors, parent review, and future providers.

## Validation/evidence requirement

Validate that the packet is complete for the target surface, has exact source authority or limitations, names allowed/forbidden surfaces, states return destination, preserves candidate-state boundaries, and includes required evidence.

## Forbidden behaviors

- Sending partial prompt fragments.
- Asking the user to infer missing scope or build the packet manually.
- Omitting return destination.
- Letting Codex results bypass current-chat verification.
- Starting a next material chat before the current material target is accepted, persisted, verified, or explicitly stopped.
- Treating packet launch as acceptance.
- Launching child chats silently.

## Failure/recovery path

If a packet is incomplete, stop and repair the packet in the same closure.

If required source is missing, return a Context Request or Check Job launch.

If target surface constraints are unclear, return a human decision request.

If transfer is unsafe, return a blocked result or stop packet.

## Dependencies

- `workflow_v3/SIGNALS_HANDLERS_ACTION_INBOX.md`
- `workflow_v3/project_setup/GENERIC_AI_PROVIDER_SETUP.md`
- `workflow_v3/templates/TRANSITION_PACKET_TEMPLATE.md`
- `workflow_v3/templates/NEXT_CHAT_PROMPT_TEMPLATE.md`

END_OF_FILE: workflow_v3/interfaces/05_PACKET_AND_TRANSFER_INTERFACE.md
