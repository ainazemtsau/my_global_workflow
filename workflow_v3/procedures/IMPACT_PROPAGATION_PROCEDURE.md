# Procedure: Impact Propagation

title: Impact Propagation
status: stub_procedure_pending_authoring
canonical_location: workflow_v3/procedures/IMPACT_PROPAGATION_PROCEDURE.md
entrypoint: impact_propagation
kind: core
procedure_boundary: recovery_review

## purpose

Self-contained target spec for determining impact radius after invalidation or blocker findings. The detailed procedure body is not authored yet.

## target_role

Determine impact radius when evidence invalidates assumptions, parent claims, interfaces, or active work.

## workflow_integration

Converts invalidation/blocker findings into local repair, parent replan, Direction Map update candidate, upstream escalation, or downstream delta.

## when_to_use

- START selected `impact_propagation`.
- Evidence invalidates an assumption, parent claim, interface, or active work boundary.

## when_not_to_use

- Do not mutate graph/state silently.
- Do not cancel work without a visible packet.
- Do not invent an accepted route.

## required_inputs

- changed or invalidated node/assumption/interface;
- affected parent/child context;
- evidence and source limitations;
- return destination.

## future_body_scope

- identify changed/invalidated node or assumption;
- trace affected parents/children/interfaces;
- determine lowest layer that can absorb change;
- produce Upstream Escalation Packet using `UPSTREAM_ESCALATION_PACKET_TEMPLATE.md` if needed;
- produce Downstream Delta Packet using `DOWNSTREAM_DELTA_PACKET_TEMPLATE.md` for affected active work;
- produce Graph Delta or Derived Gate Check candidate using `GRAPH_DELTA_TEMPLATE.md` or `DERIVED_GATE_CHECK_TEMPLATE.md` when needed;
- produce repair/stop/decision next move.

## future_body_must_not

- silently mutate graph/state;
- cancel work without visible packet;
- invent accepted route.

## required_outputs_when_authored

- impact radius result or blocked result;
- repair/escalation/delta/gate candidate if needed;
- evidence and limitations;
- CLOSURE_CHECK;
- FINISH_PACKET;
- NEXT_CHAT_CARD or no_next_chat_needed.

## future_body_quality_requirements

When the detailed body is authored, it must preserve these invariants:

- impact radius names affected parent, child, interface, state, and active-work surfaces;
- the lowest layer that can absorb the change is selected before escalation;
- local repair is preferred when higher claims, parent acceptance policy, and interface dependencies are unaffected;
- upstream escalation, downstream delta, graph delta, and derived gate packets are produced only when their boundary is materially needed;
- affected work cannot continue against stale parent context without visible delta, repair, pause, replan, stop, or decision output;
- impact propagation does not silently mutate graph/state, cancel work without a visible packet, or invent an accepted route.

## Completion Contract

```text
completion:
  result: blocked stub result explaining PROCEDURE_BODY_NOT_AUTHORED
  proof: canonical stub source exists and describes impact propagation target role
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

END_OF_FILE: workflow_v3/procedures/IMPACT_PROPAGATION_PROCEDURE.md
