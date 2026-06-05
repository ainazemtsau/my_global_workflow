# Procedure: Impact Propagation

title: Impact Propagation
status: stub_procedure_pending_authoring
canonical_location: workflow_v3/procedures/IMPACT_PROPAGATION_PROCEDURE.md
entrypoint: impact_propagation
procedure_boundary: recovery_review

## purpose

Self-contained target spec for determining impact radius after invalidation or blocker findings. The detailed procedure body is not authored yet.

## target_role

Determine impact radius when evidence invalidates assumptions, parent claims, interfaces, or active work.

## workflow_integration

Converts invalidation/blocker findings into local repair, parent replan, Direction Map update candidate, upstream escalation, or downstream delta.

## when_to_use

- START selected `impact_propagation`.
- Evidence invalidates an assumption, parent claim, interface, or active work boundary.

## when_not_to_use

- Do not mutate graph/state silently.
- Do not cancel work without a visible packet.
- Do not invent an accepted route.

## required_inputs

- changed or invalidated node/assumption/interface;
- affected parent/child context;
- evidence and source limitations;
- return destination.

## future_body_scope

- identify changed/invalidated node or assumption;
- trace affected parents/children/interfaces;
- determine lowest layer that can absorb change;
- produce Upstream Escalation Packet using `UPSTREAM_ESCALATION_PACKET_TEMPLATE.md` if needed;
- produce Downstream Delta Packet using `DOWNSTREAM_DELTA_PACKET_TEMPLATE.md` for affected active work;
- produce Graph Delta or Derived Gate Check candidate using `GRAPH_DELTA_TEMPLATE.md` or `DERIVED_GATE_CHECK_TEMPLATE.md` when needed;
- produce repair/stop/decision next move.

## future_body_must_not

- silently mutate graph/state;
- cancel work without visible packet;
- invent accepted route.

## required_outputs_when_authored

- impact radius result or blocked result;
- repair/escalation/delta/gate candidate if needed;
- evidence and limitations;
- FINISH_PACKET;
- Result Packet;
- Next Move Packet.

## Completion Contract

```text
completion:
  result: blocked stub result explaining PROCEDURE_BODY_NOT_AUTHORED
  proof: canonical stub source exists and describes impact propagation target role
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

END_OF_FILE: workflow_v3/procedures/IMPACT_PROPAGATION_PROCEDURE.md
