# Procedure: Work Contract Execution

title: Work Contract Execution
status: stub_procedure_pending_authoring
canonical_location: workflow_v3/procedures/WORK_CONTRACT_EXECUTION_PROCEDURE.md
entrypoint: execute_work_contract
run_surface_type: work_contract_execution

## purpose

Self-contained target spec for executing or coordinating one admitted Work Contract. The detailed procedure body is not authored yet.

## target_role

Execute or coordinate execution of one accepted/admitted Work Contract through an allowed surface and return candidate result/evidence.

## workflow_integration

This is the missing execution bridge between Work Contract formation and Parent Integration / Acceptance Review.

## when_to_use

- START selected `execute_work_contract`.
- One admitted Work Contract needs execution or transfer to an allowed surface.

## when_not_to_use

- Do not alter parent goal or route.
- Do not accept the result.
- Do not execute outside allowed surfaces.

## required_inputs

- admitted Work Contract;
- allowed execution surface;
- expected result and evidence requirements;
- return destination.

## future_body_scope

- verify Work Contract is admitted and bounded;
- execute same-chat work only if allowed by run surface;
- or produce Transfer Packet for child chat, check job, Codex, human action;
- collect result/evidence;
- return Result Packet;
- route to Parent Integration or Acceptance Review.

## future_body_must_not

- alter parent goal;
- change Direction Map;
- accept own result;
- execute outside allowed surfaces.

## required_outputs_when_authored

- candidate Result Packet with evidence or blocked result;
- Transfer Packet when execution must move surfaces;
- validation/source limitations;
- FINISH_PACKET;
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

END_OF_FILE: workflow_v3/procedures/WORK_CONTRACT_EXECUTION_PROCEDURE.md
