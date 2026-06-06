# Procedure: Direction Map Formation

title: Direction Map Formation
status: stub_procedure_pending_authoring
canonical_location: workflow_v3/procedures/DIRECTION_MAP_FORMATION_PROCEDURE.md
entrypoint: form_direction_map
kind: core
procedure_boundary: formation_chat

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
- use `workflow_v3/interfaces/14_GOAL_EVIDENCE_GRAPH_INTERFACE.md`;
- produce candidates compatible with `workflow_v3/templates/GOAL_EVIDENCE_GRAPH_TEMPLATE.md`, `GOAL_EVIDENCE_NODE_TEMPLATE.md`, and `ACTIVE_UNRESOLVED_CUT_TEMPLATE.md`;
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
- candidate Active Unresolved Cut refs when available;
- risks and evidence gaps;
- acceptance question;
- CLOSURE_CHECK;
- FINISH_PACKET;
- NEXT_CHAT_CARD or no_next_chat_needed.

## Completion Contract

```text
completion:
  result: blocked stub result explaining PROCEDURE_BODY_NOT_AUTHORED
  proof: canonical stub source exists and describes candidate Direction Map target role
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

END_OF_FILE: workflow_v3/procedures/DIRECTION_MAP_FORMATION_PROCEDURE.md
