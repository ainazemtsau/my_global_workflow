# Procedure: Direction Definition

title: Direction Definition
status: stub_procedure_pending_authoring
canonical_location: workflow_v3/procedures/DIRECTION_DEFINITION_PROCEDURE.md
entrypoint: launch_direction_definition
run_surface_type: formation_chat

## purpose

Self-contained target spec for semantic Direction Definition after setup-only root exists. The detailed procedure body is not authored yet.

## target_role

Coordinate semantic Direction Definition after setup-only root exists by producing bounded next-step packets for Spine, Map, and first Active Front formation.

## workflow_integration

Does not silently run multiple procedures. It sequences definition work through explicit Next Move Packets / Transfer Packets.

## when_to_use

- START selected `launch_direction_definition`.
- A setup-only root exists and the next admitted work is semantic Direction Definition.

## when_not_to_use

- Do not run Spine, Map, or Active Front formation inside this procedure.
- Do not persist state or create product roadmap content.

## required_inputs

- setup-only root status;
- selected Direction context;
- accepted/admitted launch boundary;
- return destination.

## future_body_scope

- inspect setup-only root status;
- confirm Direction Definition is admitted;
- select exact next definition step;
- prepare transfer packet to form Direction Spine, then Map, then Active Front as separate procedures.

## future_body_must_not

- switch procedures inside RUN;
- accept Spine/Map/Front;
- persist state;
- create product roadmap.

## required_outputs_when_authored

- Direction Definition next-step packet or blocked result;
- source/read limitations;
- explicit selected next procedure;
- FINISH_PACKET;
- Result Packet;
- Next Move Packet.

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

END_OF_FILE: workflow_v3/procedures/DIRECTION_DEFINITION_PROCEDURE.md
