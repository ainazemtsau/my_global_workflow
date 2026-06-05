# Chat Finish Protocol

status: active_control_plane

## Purpose

FINISH performs final audit and closure for the selected Workflow v3 main procedure.

FINISH is not first reveal of work, acceptance by itself, persistence by itself, utility launch authority, or permission to start a new material lifecycle in the same chat.

## Load Rule

Read this file only after CHECK has passed or the selected procedure has an explicit blocked completion condition.

FINISH may begin only after the user sends standalone `FINISH` or `ФИНИШ`.

## FINISH Audit

FINISH must audit:

```text
finish_audit:
  start_selected_exactly_one_main_procedure:
  selected_procedure_source_was_read:
  selected_completion_contract_was_shown:
  run_executed_only_selected_main_procedure:
  material_stages_emitted_stage_result:
  user_confirmation_observed_between_material_stages:
  utility_calls_returned_to_same_main_procedure:
  utility_returns_verified_before_reliance:
  closure_check_compared_actual_result_to_completion:
  no_unadmitted_state_mutation:
  no_hidden_launch_or_acceptance:
  no_unresolved_required_utility_return:
  next_chat_card_or_no_next_chat_needed_present:
```

Each value is `PASS`, `FAIL`, or `not_applicable`.

If any required audit item fails, FINISH must not close. Return to RUN repair or blocked escalation.

## FINISH Output

FINISH output should be human-readable first and include exact evidence where needed.

Required shape:

```text
FINISH_PACKET:
  selected_entrypoint:
  selected_procedure_path:
  completion_contract:
  closure_check:
  finish_audit:
  result:
  evidence:
  validation:
  project_refresh_requirements:
  residual_risks:
  continuation:
```

`continuation` must be exactly one of:

```text
NEXT_CHAT_CARD:
  title:
  why:
  main_procedure_to_start:
  context_to_paste:
  expected_result:
  evidence_or_return_needed:
  start_instruction:
```

or:

```text
no_next_chat_needed:
  reason:
```

## Failure Behavior

FINISH failure must return one of:

- `RUN_REPAIR_REQUIRED` when the selected procedure can repair the gap in the same lifecycle;
- `BLOCKED_ESCALATION` when source, authority, validation, utility return, or completion proof is missing;
- `CONTEXT_REQUEST` when exact user input or source excerpts are required.

FINISH failure must not emit a closed-chat result.

## Closed Boundary

After FINISH passes, the chat enters CLOSED. Same-chat follow-up may clarify the closed result or point to the emitted card, but it must not start new material work.

END_OF_FILE: workflow_v3/control_plane/CHAT_FINISH_PROTOCOL.md