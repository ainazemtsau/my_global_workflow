# Procedure: Direction Spine Formation

title: Direction Spine Formation
status: stub_procedure_pending_authoring
canonical_location: workflow_v3/procedures/DIRECTION_SPINE_FORMATION_PROCEDURE.md
entrypoint: form_direction_spine
kind: core
procedure_boundary: formation_chat

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
- invoke research/check child/adaptor calls when required evidence is missing and the child-call gate passes;
- checkpoint with the user before any persistence route;
- use Codex/storage child-call or storage packages only for approved persistence routing;
- verify returned child/adaptor evidence before FINISH is requested when relied on;
- cut roadmap/backlog/work-graph content;
- return candidate Spine + acceptance question.

## future_body_must_not

- accept its own output;
- mutate repository state or persist hidden state;
- switch to another core procedure;
- create roadmap, backlog, Direction Map, Active Front, or front state.

## required_outputs_when_authored

- candidate Direction Spine package or blocked result;
- acceptance question;
- evidence and source limitations;
- CLOSURE_CHECK;
- FINISH_PACKET;
- NEXT_CHAT_CARD or no_next_chat_needed.

## future_body_quality_requirements

When the detailed body is authored, it must preserve these invariants:

- root outcome, success dimensions/tracks, constraints, non-goals, proof indicators, failure modes, uncertainties, and risks are explicit;
- alternatives and tradeoffs are visible before a candidate Spine is returned;
- source authority and evidence limitations are labeled;
- candidate Spine output remains candidate-only until an explicit acceptance/update path admits it;
- roadmap, backlog, Direction Map, Active Front, Work Graph, product execution, and hidden persistence are excluded;
- closure returns candidate Spine package, acceptance question, limitations, CLOSURE_CHECK, FINISH_PACKET, and continuation/no-continuation.

## Completion Contract

```text
completion:
  result: blocked stub result explaining PROCEDURE_BODY_NOT_AUTHORED
  proof: canonical stub source exists and describes candidate Direction Spine target role
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

END_OF_FILE: workflow_v3/procedures/DIRECTION_SPINE_FORMATION_PROCEDURE.md
