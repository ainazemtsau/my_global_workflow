# Procedure: Work Contract Formation

title: Work Contract Formation
status: stub_procedure_pending_authoring
canonical_location: workflow_v3/procedures/WORK_CONTRACT_FORMATION_PROCEDURE.md
entrypoint: form_work_contract
procedure_boundary: formation_chat

## purpose

Self-contained target spec for forming one bounded Work Contract. The detailed procedure body is not authored yet.

## target_role

Form one bounded Work Contract for one Work Graph node or node slice.

## workflow_integration

Produces the executable contract that a chat, child chat, Codex, human action, check job, or other adapter can run.

## when_to_use

- START selected `form_work_contract`.
- One Work Graph node or node slice needs an executable contract.

## when_not_to_use

- Do not execute the contract.
- Do not broaden scope or grant acceptance authority.

## required_inputs

- selected Work Graph node or node slice;
- parent front/node relation;
- allowed and forbidden execution surfaces;
- return destination.

## future_body_scope

- select one node/slice;
- define target and relation to parent graph/front/node;
- preserve parent graph/front/node trace;
- define source reads;
- define in-scope/out-of-scope;
- define allowed/forbidden surfaces;
- define expected result and evidence requirement;
- define validation/return destination;
- return split_required if multiple independent jobs are present.

## future_body_must_not

- execute the contract;
- broaden scope;
- grant acceptance authority;
- become roadmap.

## required_outputs_when_authored

- candidate Work Contract or split/block result;
- parent graph/front/node trace;
- evidence and validation requirements;
- launch/acceptance question;
- FINISH_PACKET;
- Result Packet;
- Next Move Packet.

## Completion Contract

```text
completion:
  result: blocked stub result explaining PROCEDURE_BODY_NOT_AUTHORED
  proof: canonical stub source exists and describes bounded Work Contract formation target role
  blocked_if: selected for execution before detailed body is authored
```
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

END_OF_FILE: workflow_v3/procedures/WORK_CONTRACT_FORMATION_PROCEDURE.md
