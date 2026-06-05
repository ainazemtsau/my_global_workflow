# Procedure: Parent Integration Check

title: Parent Integration Check
status: stub_procedure_pending_authoring
canonical_location: workflow_v3/procedures/PARENT_INTEGRATION_CHECK_PROCEDURE.md
entrypoint: parent_integration_check
procedure_boundary: parent_integration

## purpose

Self-contained target spec for integrating child/work results into the parent target. The detailed procedure body is not authored yet.

## target_role

Integrate child/work results into parent Work Graph node, Active Front, or Goal Evidence Graph node.

## workflow_integration

Implements fan-in. Child/work results are candidate evidence. Parent Integration decides continue, repair, local replan, close parent, escalate, or produce graph delta.

## when_to_use

- START selected `parent_integration_check`.
- One or more child/work Result Packets returned to a parent target.

## when_not_to_use

- Do not synthesize missing evidence.
- Do not accept parent state.
- Do not silently open a new front.

## required_inputs

- parent Work Graph node, Active Front, or Goal Evidence Graph target;
- required child/work results;
- parent acceptance criteria;
- return destination.

## future_body_scope

- verify required child results received;
- compare evidence against parent acceptance policy;
- identify missing/conflicting evidence;
- update candidate statuses;
- produce Parent Integration Result using `PARENT_INTEGRATION_RESULT_TEMPLATE.md`;
- produce Graph Delta, Upstream Escalation Packet, or Downstream Delta Packet candidates using `GRAPH_DELTA_TEMPLATE.md`, `UPSTREAM_ESCALATION_PACKET_TEMPLATE.md`, or `DOWNSTREAM_DELTA_PACKET_TEMPLATE.md` when needed;
- produce Derived Gate Check candidate using `DERIVED_GATE_CHECK_TEMPLATE.md` when a boundary gate is required;
- select next move packet.

## future_body_must_not

- synthesize missing evidence;
- let child accept parent state;
- mutate accepted state;
- silently open new front.

## required_outputs_when_authored

- Parent Integration Result or blocked result;
- missing/conflicting evidence list;
- candidate graph/escalation/delta/gate packet refs if needed;
- FINISH_PACKET;
- Result Packet;
- Next Move Packet.

## Completion Contract

```text
completion:
  result: blocked stub result explaining PROCEDURE_BODY_NOT_AUTHORED
  proof: canonical stub source exists and describes parent integration target role
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

END_OF_FILE: workflow_v3/procedures/PARENT_INTEGRATION_CHECK_PROCEDURE.md
