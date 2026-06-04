# Procedure: Direction Map Formation

title: Direction Map Formation
status: stub_procedure_pending_authoring
canonical_location: workflow_v3/procedures/DIRECTION_MAP_FORMATION_PROCEDURE.md
entrypoint: form_direction_map
run_surface_type: formation_chat

## purpose

Self-contained target spec for forming a candidate Direction Map with embedded or associated Goal Evidence Graph. The detailed procedure body is not authored yet.

## target_role

Form a candidate Direction Map with embedded/associated Goal Evidence Graph: claims, dependencies, uncertainties, obstacles, evidence gaps, candidate fronts, and active unresolved cut candidates.

## workflow_integration

Bridges Direction Spine to Active Front selection. It explains how future work is derived from root success rather than selected by preference or backlog.

## when_to_use

- START selected `form_direction_map`.
- Candidate or accepted Spine context is available for map formation.

## when_not_to_use

- Do not create a roadmap, global backlog, or local Work Graph.
- Do not select a front by preference alone.

## required_inputs

- accepted/candidate Spine context;
- source authority and evidence limitations;
- return destination;
- acceptance boundary.

## future_body_scope

- read accepted/candidate Spine context;
- create candidate Goal Evidence Graph nodes/edges;
- identify required claims and OR alternatives;
- label accepted/candidate/unresolved/hypothetical items;
- identify obstacles, dependencies, evidence gaps;
- generate candidate active unresolved cuts;
- generate candidate fronts without selecting by intuition;
- return candidate Map/Graph + risks + acceptance question.

## future_body_must_not

- become roadmap/backlog;
- open Work Graph;
- execute product work;
- accept map state.

## required_outputs_when_authored

- candidate Direction Map / Goal Evidence Graph package or blocked result;
- risks and evidence gaps;
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

END_OF_FILE: workflow_v3/procedures/DIRECTION_MAP_FORMATION_PROCEDURE.md
