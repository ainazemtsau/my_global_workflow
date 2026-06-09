# Procedure: Direction Project Root Bootstrap

title: Direction Project Root Bootstrap
status: stub_procedure_pending_authoring
canonical_location: workflow_v3/procedures/DIRECTION_PROJECT_ROOT_BOOTSTRAP_PROCEDURE.md
entrypoint: direction_project_root_bootstrap
kind: core
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
- output a candidate storage update package or Codex `CHILD_PROCEDURE_CALL` envelope only when explicitly authorized by the selected parent/core goal, with return verification required before parent closure.

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
- CLOSURE_CHECK;
- FINISH_PACKET;
- NEXT_CHAT_CARD or no_next_chat_needed.

## Completion Contract

```text
completion:
  result: blocked stub result explaining PROCEDURE_BODY_NOT_AUTHORED
  proof: canonical stub source exists and describes setup-only root bootstrap target role
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

This stub remains blocked until the detailed body is authored. Its NEXT_CHAT_CARD is post-closed continuation for a separate authoring lifecycle and must not carry unfinished child work from a current bootstrap RUN.

## procedure_closure_shape

- CLOSURE_CHECK
- FINISH_PACKET
- NEXT_CHAT_CARD or no_next_chat_needed

END_OF_FILE: workflow_v3/procedures/DIRECTION_PROJECT_ROOT_BOOTSTRAP_PROCEDURE.md
