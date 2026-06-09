# Procedure: Work Graph Formation

title: Work Graph Formation
status: stub_procedure_pending_authoring
canonical_location: workflow_v3/procedures/WORK_GRAPH_FORMATION_PROCEDURE.md
entrypoint: form_work_graph
kind: core
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
- CLOSURE_CHECK;
- FINISH_PACKET;
- NEXT_CHAT_CARD or no_next_chat_needed.

## Completion Contract

```text
completion:
  result: blocked stub result explaining PROCEDURE_BODY_NOT_AUTHORED
  proof: canonical stub source exists and describes local Work Graph formation target role
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

END_OF_FILE: workflow_v3/procedures/WORK_GRAPH_FORMATION_PROCEDURE.md
