# Procedure: Direction Project Root Bootstrap

title: Direction Project Root Bootstrap
status: stub_procedure_pending_authoring
canonical_location: workflow_v3/procedures/DIRECTION_PROJECT_ROOT_BOOTSTRAP_PROCEDURE.md
entrypoint: direction_project_root_bootstrap
procedure_boundary: setup_only_root_bootstrap

## purpose

Self-contained target spec for the setup-only Direction Project root bootstrap procedure. The detailed procedure body is not authored yet.

## target_role

Create only the technical skeleton/package for a future Direction runtime root. It must not define semantic Direction content.

## workflow_integration

Runs before Direction Definition. Produces setup-only candidate package and next move to launch Direction Definition.

## when_to_use

- START selected `direction_project_root_bootstrap`.
- A future Direction root needs technical setup only.

## when_not_to_use

- Do not define Direction semantics.
- Do not create accepted runtime state.
- Do not execute storage mutation without storage update admission.

## required_inputs

- requested direction id/name;
- setup mode and mutation boundary;
- repository/base ref if a repository package is requested;
- return destination.

## future_body_scope

- validate requested direction id/name;
- prepare setup-only runtime root package;
- prepare placeholder state files with `pending_definition` / `none_selected` values;
- prepare Project Binding / setup source plan if applicable;
- output storage update or Codex handoff package only if explicitly authorized.

## future_body_must_not

- accept root outcome;
- create Direction Spine;
- create Direction Map;
- select Active Front;
- create Work Graph or Work Contract;
- import legacy state.

## required_outputs_when_authored

- setup-only candidate package or blocked result;
- source/read limitations;
- validation needs;
- FINISH_PACKET;
- Result Packet;
- Next Move Packet.

## Completion Contract

```text
completion:
  result: blocked stub result explaining PROCEDURE_BODY_NOT_AUTHORED
  proof: canonical stub source exists and describes setup-only root bootstrap target role
  blocked_if: selected for execution before detailed body is authored
```
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

END_OF_FILE: workflow_v3/procedures/DIRECTION_PROJECT_ROOT_BOOTSTRAP_PROCEDURE.md
