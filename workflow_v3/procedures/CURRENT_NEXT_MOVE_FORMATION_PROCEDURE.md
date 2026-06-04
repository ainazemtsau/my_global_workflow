# Procedure: Current Next Move Formation

title: Current Next Move Formation
status: stub_procedure_pending_authoring
canonical_location: workflow_v3/procedures/CURRENT_NEXT_MOVE_FORMATION_PROCEDURE.md
entrypoint: form_current_next_move
run_surface_type: formation_chat

## purpose

Self-contained target spec for forming a candidate Current Next Move / Next Move Packet. The detailed procedure body is not authored yet.

## target_role

Form a candidate Current Next Move / Next Move Packet from closure state, result, accepted boundaries, and selected procedure context.

## workflow_integration

Makes the next step explicit without using removed lifecycle/router concepts.

## when_to_use

- START selected `form_current_next_move`.
- A closed result needs exactly one primary next move.

## when_not_to_use

- Do not execute the next move.
- Do not launch multiple steps or bypass acceptance/update path.

## required_inputs

- FINISH_PACKET or closure state;
- Result Packet;
- accepted boundaries;
- selected procedure context.

## future_body_scope

- inspect Result Packet and FINISH_PACKET;
- select one primary next move;
- classify next_move_type;
- include Transfer Packet if needed;
- preserve acceptance/persistence boundary;
- avoid hidden launches.

## future_body_must_not

- execute next move;
- launch multiple steps;
- bypass acceptance/update path.

## required_outputs_when_authored

- candidate Next Move Packet or blocked result;
- transfer packet if needed;
- persistence and acceptance boundary;
- FINISH_PACKET;
- Result Packet.

## stop_behavior_until_authored

```text
result_packet.status: blocked
result_packet.result: PROCEDURE_BODY_NOT_AUTHORED
result_packet.evidence: canonical stub exists and describes target role
result_packet.not_done: author detailed body in separate bounded author_workflow_procedure run
next_move_packet.primary_next_move: author this procedure body in separate bounded author_workflow_procedure run
next_move_packet.next_move_type: next_material_chat | same_chat_continuation
next_move_packet.blocking_reason_if_any: PROCEDURE_BODY_NOT_AUTHORED
```

## finish_closure_shape

- FINISH_PACKET
- Result Packet
- Next Move Packet

END_OF_FILE: workflow_v3/procedures/CURRENT_NEXT_MOVE_FORMATION_PROCEDURE.md
