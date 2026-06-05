# Procedure: Acceptance Decision Formation

title: Acceptance Decision Formation
status: stub_procedure_pending_authoring
canonical_location: workflow_v3/procedures/ACCEPTANCE_DECISION_FORMATION_PROCEDURE.md
entrypoint: accept_candidate_entity
run_surface_type: acceptance_review

## purpose

Self-contained target spec for reviewing candidate result/evidence and forming an acceptance decision candidate. The detailed procedure body is not authored yet.

## target_role

Review candidate result/evidence and form an explicit accept, reject, repair, block, or park decision candidate.

## workflow_integration

Separates candidate output from accepted state. Acceptance can authorize update need; direct ChatGPT storage mutation requires storage_update_adapter, and external utility write requires Utility Use Gate, write gate, exact paths, validation, and verified return.

## when_to_use

- START selected `accept_candidate_entity`.
- Candidate result/evidence needs explicit review.

## when_not_to_use

- Do not let an adapter accept its own output.
- Do not infer acceptance from silence.
- Do not mutate storage directly.

## required_inputs

- candidate result/evidence;
- reviewer authority;
- affected state boundary;
- return destination.

## future_body_scope

- read candidate result/evidence;
- check validation and source limitations;
- classify decision options;
- ask or record explicit human/parent decision;
- produce Acceptance Decision candidate/package.

## future_body_must_not

- let adapter accept own output;
- infer acceptance from silence;
- mutate storage directly.

## required_outputs_when_authored

- Acceptance Decision candidate or blocked result;
- storage update need if applicable;
- evidence/source limitations;
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

END_OF_FILE: workflow_v3/procedures/ACCEPTANCE_DECISION_FORMATION_PROCEDURE.md
