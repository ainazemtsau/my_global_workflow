# Procedure: Direction Definition

title: Direction Definition
status: stub_procedure_pending_authoring
canonical_location: workflow_v3/procedures/DIRECTION_DEFINITION_PROCEDURE.md
entrypoint: launch_direction_definition
procedure_boundary: formation_chat

## purpose

Self-contained target spec for semantic Direction Definition after setup-only root exists. The detailed procedure body is not authored yet.

## target_role

Coordinate semantic Direction Definition after setup-only root exists by producing one bounded next-step packet at a time. The first next procedure is `form_direction_spine`; later Map and Active Front formation require explicit Next Move / Transfer Packet or separately admitted lifecycle boundaries.

## workflow_integration

Does not silently run multiple procedures. It sequences definition work through explicit NEXT_CHAT_CARD continuation artifacts / Transfer Packets.

## when_to_use

- START selected `launch_direction_definition`.
- A setup-only root exists and the next admitted work is semantic Direction Definition.

## when_not_to_use

- Do not run Spine, Map, or Active Front formation inside this procedure.
- Do not persist state or create product roadmap content.

## required_inputs

- setup-only root status;
- selected Direction context;
- accepted/admitted launch boundary;
- return destination.

## future_body_scope

- inspect setup-only root status;
- confirm Direction Definition is admitted;
- select exact next definition step;
- prepare a transfer packet for the selected single next definition step.

## future_body_must_not

- switch procedures inside RUN;
- accept Spine/Map/Front;
- persist state;
- create product roadmap.

## required_outputs_when_authored

- Direction Definition next-step packet or blocked result;
- source/read limitations;
- explicit selected next procedure;
- CLOSURE_CHECK;
- FINISH_PACKET;
- NEXT_CHAT_CARD or no_next_chat_needed.

## Completion Contract

```text
completion:
  result: blocked stub result explaining PROCEDURE_BODY_NOT_AUTHORED
  proof: canonical stub source exists and describes semantic Direction Definition target role
  blocked_if: selected for execution before detailed body is authored
```
## stop_behavior_until_authored

```text
CLOSURE_CHECK:
  status: blocked
  result: PROCEDURE_BODY_NOT_AUTHORED
  evidence: canonical stub exists and describes target role
  not_done: author detailed body in separate bounded author_workflow_procedure run
FINISH_PACKET:
  result: blocked stub result explaining PROCEDURE_BODY_NOT_AUTHORED
  evidence: canonical stub source and target role are present
  residual_risks: detailed body is not authored
NEXT_CHAT_CARD:
  title: Author this procedure body
  why: PROCEDURE_BODY_NOT_AUTHORED
  main_procedure_to_start: author_workflow_procedure
  context_to_paste: this procedure file and target role
  expected_result: authored detailed procedure body
  evidence_or_return_needed: updated procedure source with completion block
  start_instruction: START with author_workflow_procedure for this file
```

## procedure_closure_shape

- CLOSURE_CHECK
- FINISH_PACKET
- NEXT_CHAT_CARD or no_next_chat_needed

END_OF_FILE: workflow_v3/procedures/DIRECTION_DEFINITION_PROCEDURE.md
