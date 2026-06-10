# Procedure: Parent Integration Check

title: Parent Integration Check
status: stub_procedure_pending_authoring
canonical_location: workflow_v3/procedures/PARENT_INTEGRATION_CHECK_PROCEDURE.md
entrypoint: parent_integration_check
kind: core
procedure_boundary: parent_integration

## purpose

Self-contained target spec for integrating dependency/work results into the parent target. The detailed procedure body is not authored yet.

## target_role

Integrate dependency/work results into parent Work Graph node, Active Front, or Goal Evidence Graph node.

## workflow_integration

Implements fan-in. Dependency/work results are candidate evidence. Parent Integration decides continue, repair, local replan, close parent, escalate, or produce graph delta.

## when_to_use

- START selected `parent_integration_check`.
- One or more dependency/work FINISH_PACKET results returned to a parent target.

## when_not_to_use

- Do not synthesize missing evidence.
- Do not accept parent state.
- Do not silently open a new front.

## required_inputs

- parent Work Graph node, Active Front, or Goal Evidence Graph target;
- required dependency/work results;
- parent acceptance criteria;
- return destination.

## future_body_scope

- verify required dependency results received;
- compare evidence against parent acceptance policy;
- identify missing/conflicting evidence;
- update candidate statuses;
- produce Parent Integration Result using `PARENT_INTEGRATION_RESULT_TEMPLATE.md`;
- produce Graph Delta, Upstream Escalation Packet, or Downstream Delta Packet candidates using `GRAPH_DELTA_TEMPLATE.md`, `UPSTREAM_ESCALATION_PACKET_TEMPLATE.md`, or `DOWNSTREAM_DELTA_PACKET_TEMPLATE.md` when needed;
- produce Derived Gate Check candidate using `DERIVED_GATE_CHECK_TEMPLATE.md` when a boundary gate is required;
- select NEXT_CHAT_CARD or no_next_chat_needed continuation.

## future_body_must_not

- synthesize missing evidence;
- let dependency surface accept parent state;
- mutate accepted state;
- silently open new front.

## required_outputs_when_authored

- Parent Integration Result or blocked result;
- missing/conflicting evidence list;
- candidate graph/escalation/delta/gate packet refs if needed;
- CLOSURE_CHECK;
- FINISH_PACKET;
- NEXT_CHAT_CARD or no_next_chat_needed.

## future_body_quality_requirements

When the detailed body is authored, it must preserve these invariants:

- every required dependency/work result is accounted for as present, missing, conflicting, blocked, explicitly deferred, or no longer required by accepted parent change;
- returned evidence is compared against parent acceptance criteria before closure, repair, replan, close, escalate, delta, continue, or stop is selected;
- missing and conflicting evidence remain visible and block closure unless parent policy explicitly allows partial closure;
- candidate Graph Delta, Upstream Escalation Packet, Downstream Delta Packet, Derived Gate Check, and NEXT_CHAT_CARD outputs are visible when needed;
- dependency outputs remain candidate evidence and cannot accept parent state;
- parent integration does not synthesize missing evidence, mutate accepted state, or silently open a new front.

## Completion Contract

```text
completion:
  result: blocked stub result explaining PROCEDURE_BODY_NOT_AUTHORED
  proof: canonical stub source exists and describes parent integration target role
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

END_OF_FILE: workflow_v3/procedures/PARENT_INTEGRATION_CHECK_PROCEDURE.md
