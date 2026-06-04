# Procedure: Storage Update

title: Storage Update
status: stub_procedure_pending_authoring
canonical_location: workflow_v3/procedures/STORAGE_UPDATE_PROCEDURE.md
entrypoint: persist_accepted_state
run_surface_type: storage_update_adapter

## purpose

Self-contained target spec for persisting accepted state or accepted records from an admitted storage update package. The detailed procedure body is not authored yet.

## target_role

Persist accepted state or accepted records only from an admitted storage update package.

## workflow_integration

This is the only procedure surface that can mutate allowed repository/runtime state after explicit acceptance/update authorization.

## when_to_use

- START selected `persist_accepted_state`.
- A complete admitted storage update package lists exact allowed files and validation.

## when_not_to_use

- Do not decide acceptance.
- Do not broaden write scope.
- Do not create Direction state without adoption.

## required_inputs

- accepted update package;
- exact allowed files and forbidden paths;
- validation commands;
- project refresh reporting requirements.

## future_body_scope

- verify accepted update package;
- verify allowed/forbidden paths;
- write only listed files;
- preserve EOF markers;
- return changed files and validation;
- report project refresh requirements.

## future_body_must_not

- decide acceptance;
- broaden write scope;
- create Direction state without adoption.

## required_outputs_when_authored

- changed files and validation output or blocked result;
- project refresh requirements;
- source/read limitations;
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

END_OF_FILE: workflow_v3/procedures/STORAGE_UPDATE_PROCEDURE.md
