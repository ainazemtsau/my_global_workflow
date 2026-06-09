# Procedure: Active Front Formation

title: Active Front Formation
status: stub_procedure_pending_authoring
canonical_location: workflow_v3/procedures/ACTIVE_FRONT_FORMATION_PROCEDURE.md
entrypoint: form_active_front
kind: core
procedure_boundary: formation_chat

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
- use `workflow_v3/templates/ACTIVE_UNRESOLVED_CUT_TEMPLATE.md` and `workflow_v3/interfaces/14_GOAL_EVIDENCE_GRAPH_INTERFACE.md` when graph context exists;
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
- graph/cut/map trace for selected exit criteria;
- rejected/deferred alternatives;
- acceptance question;
- CLOSURE_CHECK;
- FINISH_PACKET;
- NEXT_CHAT_CARD or no_next_chat_needed.

## future_body_quality_requirements

When the detailed body is authored, it must preserve these invariants:

- candidate front selection traces to Direction Map areas and, when available, Goal Evidence Graph nodes or Active Unresolved Cut;
- touched tracks, success dimensions, evidence value, risk, dependency unlock, reversibility, WIP/capacity, and bottleneck relief are considered;
- rejected or deferred alternatives are named with reasons;
- front exit criteria tie back to graph nodes, cut items, or map claims when those structures exist;
- candidate Active Front remains candidate-only until an explicit acceptance/update path admits mutation;
- preference-only selection, whole-Direction activation, global backlog, hidden acceptance, and Work Graph launch before required acceptance are excluded.

## Completion Contract

```text
completion:
  result: blocked stub result explaining PROCEDURE_BODY_NOT_AUTHORED
  proof: canonical stub source exists and describes candidate Active Front target role
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

END_OF_FILE: workflow_v3/procedures/ACTIVE_FRONT_FORMATION_PROCEDURE.md
