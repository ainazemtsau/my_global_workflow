# Procedure: Memory Artifact Promotion

title: Memory Artifact Promotion
status: stub_procedure_pending_authoring
canonical_location: workflow_v3/procedures/MEMORY_ARTIFACT_PROMOTION_PROCEDURE.md
entrypoint: promote_memory_artifact
run_surface_type: formation_chat

## purpose

Self-contained target spec for promoting a Memory Candidate to a Memory Artifact. The detailed procedure body is not authored yet.

## target_role

Promote a Memory Candidate to Memory Artifact only when reusable, source-backed, scoped, and bounded by when_to_load / when_not_to_use / refresh rules.

## workflow_integration

Keeps long-term memory useful without polluting context or replacing accepted state.

## when_to_use

- START selected `promote_memory_artifact`.
- A Memory Candidate needs promotion review.

## when_not_to_use

- Do not promote raw chat notes.
- Do not override canonical state.
- Do not create broad always-load memory.

## required_inputs

- Memory Candidate;
- source references;
- proposed scope of use;
- refresh/expiry expectations.

## future_body_scope

- review Memory Candidate;
- verify source refs;
- define scope_of_use;
- define loading and exclusion rules;
- define refresh/expiry;
- return promoted Memory Artifact candidate.

## future_body_must_not

- promote raw chat notes;
- override canonical state;
- create broad always-load memory.

## required_outputs_when_authored

- promoted Memory Artifact candidate or blocked result;
- source references and loading rules;
- refresh/expiry rule;
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

END_OF_FILE: workflow_v3/procedures/MEMORY_ARTIFACT_PROMOTION_PROCEDURE.md
