# Procedure: Active Front Formation

title: Active Front Formation
status: stub_procedure_pending_authoring
canonical_location: workflow_v3/procedures/ACTIVE_FRONT_FORMATION_PROCEDURE.md
entrypoint: form_active_front
run_surface_type: formation_chat

## purpose

Self-contained target spec for selecting a candidate Active Front from Direction Map / Goal Evidence Graph context. The detailed procedure body is not authored yet.

## target_role

Select a candidate Active Front from the Direction Map / Goal Evidence Graph using active unresolved cut, evidence value, bottleneck relief, dependency unlock, reversibility, WIP/capacity, and success-dimension balance.

## workflow_integration

Produces the one current focus candidate that prevents the whole Direction from becoming active at once.

## when_to_use

- START selected `form_active_front`.
- Direction Map / Goal Evidence Graph context exists and a candidate front is needed.

## when_not_to_use

- Do not select by convenience only.
- Do not open Work Graph before front acceptance when acceptance is required.

## required_inputs

- Direction Map / Goal Evidence Graph context;
- candidate fronts or active unresolved cuts;
- WIP/capacity constraints;
- return destination.

## future_body_scope

- identify active unresolved cut;
- compare candidate fronts;
- state why this front now;
- define front exit criteria;
- define in-scope/out-of-scope;
- identify rejected/deferred alternatives;
- identify derived gates and required evidence;
- return candidate Active Front + acceptance question.

## future_body_must_not

- choose by convenience only;
- open Work Graph before accepted front if acceptance is required;
- create global backlog;
- silently launch next work.

## required_outputs_when_authored

- candidate Active Front package or blocked result;
- rejected/deferred alternatives;
- acceptance question;
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

END_OF_FILE: workflow_v3/procedures/ACTIVE_FRONT_FORMATION_PROCEDURE.md
