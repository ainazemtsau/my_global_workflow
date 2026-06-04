# Procedure: Direction Spine Formation

title: Direction Spine Formation
status: stub_procedure_pending_authoring
canonical_location: workflow_v3/procedures/DIRECTION_SPINE_FORMATION_PROCEDURE.md
entrypoint: form_direction_spine
run_surface_type: formation_chat

## purpose

Self-contained target spec for forming a candidate Direction Spine. The detailed procedure body is not authored yet.

## target_role

Form a candidate Direction Spine: root outcome, success dimensions, constraints, non-goals, failure modes, proof indicators, and open uncertainties.

## workflow_integration

Produces candidate Spine for acceptance review. It is the top success axis for Direction Map / Goal Evidence Graph formation.

## when_to_use

- START selected `form_direction_spine`.
- Direction Definition needs a candidate Spine.

## when_not_to_use

- Do not accept its own output.
- Do not create roadmap, backlog, map, or front state.

## required_inputs

- source authority and human input;
- setup-only root or Direction Definition context;
- return destination;
- acceptance boundary.

## future_body_scope

- classify source authority and human input;
- derive candidate root outcome;
- define success dimensions / tracks;
- define constraints and non-goals;
- identify failure modes and proof indicators;
- cut roadmap/backlog/work-graph content;
- return candidate Spine + acceptance question.

## future_body_must_not

- accept its own output;
- create roadmap/backlog;
- create Direction Map or Active Front;
- mutate repository state.

## required_outputs_when_authored

- candidate Direction Spine package or blocked result;
- acceptance question;
- evidence and source limitations;
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

END_OF_FILE: workflow_v3/procedures/DIRECTION_SPINE_FORMATION_PROCEDURE.md
