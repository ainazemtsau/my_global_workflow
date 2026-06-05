# Procedure: Work Graph Formation

title: Work Graph Formation
status: stub_procedure_pending_authoring
canonical_location: workflow_v3/procedures/WORK_GRAPH_FORMATION_PROCEDURE.md
entrypoint: form_work_graph
procedure_boundary: formation_chat

## purpose

Self-contained target spec for forming a local Work Graph under one Active Front. The detailed procedure body is not authored yet.

## target_role

Form a local Work Graph under one Active Front. Nodes must derive only from the front exit criteria and evidence needs.

## workflow_integration

Converts an accepted/candidate Active Front into bounded local nodes that can become Work Contracts.

## when_to_use

- START selected `form_work_graph`.
- An Active Front and exit criteria need local Work Graph decomposition.

## when_not_to_use

- Do not create a global roadmap.
- Do not execute nodes or product work.

## required_inputs

- Active Front and exit criteria;
- source/evidence requirements;
- acceptance or launch boundary;
- return destination.

## future_body_scope

- read Active Front and exit criteria;
- derive minimum necessary nodes;
- preserve graph/front/map trace;
- define node relation to parent graph node, map claim, or front closure;
- define dependencies;
- define proof path and closure condition;
- identify non-nodes / cut items;
- return candidate Work Graph + acceptance/launch question.

## future_body_must_not

- create global roadmap;
- duplicate Direction Map;
- include unrelated product work;
- execute nodes.

## required_outputs_when_authored

- candidate Work Graph package or blocked result;
- node relation-to-parent summary;
- node dependency/evidence summary;
- acceptance or launch question;
- FINISH_PACKET;
- Result Packet;
- Next Move Packet.

## Completion Contract

```text
completion:
  result: blocked stub result explaining PROCEDURE_BODY_NOT_AUTHORED
  proof: canonical stub source exists and describes local Work Graph formation target role
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

END_OF_FILE: workflow_v3/procedures/WORK_GRAPH_FORMATION_PROCEDURE.md
