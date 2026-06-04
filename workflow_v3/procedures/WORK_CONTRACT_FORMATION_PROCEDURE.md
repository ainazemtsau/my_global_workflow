# Procedure: Work Contract Formation

title: Work Contract Formation

status: stub_procedure_pending_migration

canonical_location: workflow_v3/procedures/WORK_CONTRACT_FORMATION_PROCEDURE.md

## migration_source

old_source_path: workflow_v3/formation/WORK_CONTRACT_FORMATION_RUNBOOK.md

old_file_retained_as_migration_source: true

## purpose

Represent the registered Work Contract formation entrypoint without executing the old source body in the active procedure model.

## trigger_when_to_use

- Use when START selects `form_work_contract`.

## when_not_to_use

- Do not use to form a Work Contract until the body is migrated.
- Do not use to migrate this procedure body in the same run.

## required_inputs

- entrypoint: `form_work_contract`
- run_surface_type: `formation_chat`
- Work Graph node or bounded slice context.

## source_requirements

- Read this stub procedure.
- Treat `old_source_path` as retained migration source only.
- Do not execute or import detailed old source logic.

## context_classification

- this stub: canonical source
- old_source_path: migration source
- user input: current human input until accepted through the admitted procedure

## stage_cards

```text
stage_id: migration_guard
purpose: prevent execution of unmigrated formation logic
activation conditions: always
inputs: selected entrypoint and old_source_path
required intermediate output: MIGRATION_REQUIRED result
gate: STOP
checkpoint rule: no checkpoint
expansion rule: no expansion
stop behavior: return blocked Result Packet and Next Move Packet
```

## output_contract

```text
result_packet:
  status: blocked
  result: MIGRATION_REQUIRED / PROCEDURE_BODY_NOT_MIGRATED
  evidence: old_source_path retained for future migration
  changed_files: none
  validation: not run
  source_read_limitations: detailed body not migrated
  not_done: migrate procedure body
  project_refresh_requirements: none
  residual_risks: entrypoint cannot execute until migrated
  exact_next_move: migrate this procedure in a separate bounded author_workflow_procedure run
next_move_packet:
  primary_next_move: migrate this procedure in a separate bounded author_workflow_procedure run
  next_move_type: same_chat_continuation
  return_destination: current chat
  transfer_packet_if_needed: not needed
  persistence_boundary: no persistence
  acceptance_boundary: no acceptance
  blocking_reason_if_any: PROCEDURE_BODY_NOT_MIGRATED
```

## stop_conditions

- Stop whenever this stub is selected for execution.

## procedure_closure

Return FINISH_REQUEST if lifecycle FINISH is active, then close with FINISH_PACKET, Result Packet, and Next Move Packet. The Result Packet status must be blocked and name `MIGRATION_REQUIRED / PROCEDURE_BODY_NOT_MIGRATED`.

END_OF_FILE: workflow_v3/procedures/WORK_CONTRACT_FORMATION_PROCEDURE.md
