# Procedure: Work Contract Execution

title: Work Contract Execution
status: stub_procedure_pending_authoring
canonical_location: workflow_v3/procedures/WORK_CONTRACT_EXECUTION_PROCEDURE.md
entrypoint: execute_work_contract
kind: core
procedure_boundary: work_contract_execution

## purpose

Self-contained target spec for executing or coordinating one admitted Work Contract. The detailed procedure body is not authored yet.

## target_role

Execute or coordinate execution of one accepted/admitted Work Contract through an allowed surface and return candidate result/evidence.

## workflow_integration

This is the missing execution bridge between Work Contract formation and Parent Integration / Acceptance Review.

## when_to_use

- START selected `execute_work_contract`.
- One admitted Work Contract needs execution or transfer to an allowed surface.

## when_not_to_use

- Do not alter parent goal or route.
- Do not accept the result.
- Do not execute outside allowed surfaces.

## required_inputs

- admitted Work Contract;
- allowed execution surface;
- expected result and evidence requirements;
- return destination.

## future_body_scope

- verify Work Contract is admitted and bounded;
- execute same-chat work only if allowed by procedure boundary;
- or produce Transfer Packet for dependency chat, check job, Codex, human action;
- collect result/evidence;
- return FINISH_PACKET result;
- route to Parent Integration or Acceptance Review boundary through visible NEXT_CHAT_CARD continuation.

## future_body_must_not

- alter parent goal;
- change Direction Map;
- accept own result;
- execute outside allowed surfaces.

## required_outputs_when_authored

- candidate FINISH_PACKET result with evidence or blocked result;
- next move to Parent Integration or Acceptance Review boundary;
- Transfer Packet when execution must move surfaces;
- validation/source limitations;
- CLOSURE_CHECK;
- FINISH_PACKET;
- NEXT_CHAT_CARD or no_next_chat_needed.

## Completion Contract

```text
completion:
  result: blocked stub result explaining PROCEDURE_BODY_NOT_AUTHORED
  proof: canonical stub source exists and describes admitted Work Contract execution target role
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

END_OF_FILE: workflow_v3/procedures/WORK_CONTRACT_EXECUTION_PROCEDURE.md
