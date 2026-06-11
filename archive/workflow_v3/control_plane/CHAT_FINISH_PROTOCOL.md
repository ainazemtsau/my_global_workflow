# Chat Finish Protocol

status: active_control_plane

## Purpose

FINISH performs final audit and closure for the selected Workflow v3 main procedure.

FINISH is not first reveal of work, acceptance by itself, persistence by itself, dependency-call launch authority, or permission to start a new material lifecycle in the same chat.

## Load Rule

Read this file only after CHECK has passed or the selected procedure has an explicit blocked completion condition.

FINISH may begin only after the user sends standalone `FINISH` or `ФИНИШ`.

## FINISH Audit

FINISH must audit:

```text
finish_audit:
  start_goal_was_explicit:
  start_goal_satisfied_or_explicitly_blocked:
  start_selected_exactly_one_main_procedure:
  selected_procedure_source_was_read:
  selected_completion_contract_was_shown:
  run_executed_only_selected_main_procedure:
  declared_stage_sequence_not_compressed:
  material_stages_emitted_stage_result:
  user_confirmation_observed_between_material_stages:
  dependency_calls_returned_to_same_main_procedure:
  required_dependency_work_opened_when_detected:
  no_open_dependencies:
  all_required_dependency_returns_received:
  all_required_dependency_returns_verified:
  closure_check_compared_actual_result_to_completion:
  no_handoff_card_or_package_used_as_completion:
  required_validation_present_when_work_required_validation:
  closure_check_gaps_empty_or_blocked_completion_explicit:
  next_chat_card_not_used_for_unfinished_dependency_work:
  no_unadmitted_state_mutation:
  no_hidden_launch_or_acceptance:
  next_chat_card_or_no_next_chat_needed_present:
```

Each value is `PASS`, `FAIL`, or `not_applicable`.

If any required audit item is `FAIL`, FINISH must not close. Return to RUN repair or blocked escalation.

Additional hard gates:

- If `CLOSURE_CHECK.gaps` is non-empty and the selected completion contract does not explicitly allow blocked completion, FINISH must fail.
- If blocked completion is allowed, the result must be marked blocked, not completed.
- If `actual_result` is only a dependency call, handoff, card, package, copy-paste packet, Codex package, check packet, storage packet, dependency packet, or `NEXT_CHAT_CARD`, FINISH must fail.
- If `open_dependencies != empty`, any required dependency return is missing (`missing_dependency_return`), or any required dependency return is unverified (`unverified_dependency_return`), FINISH must fail.
- If `required_dependency_work_detected = true` and `dependency_call_opened = false`, FINISH must fail.
- If `repair_needed = true` and the selected parent cannot mutate directly, then a patch plan, draft packet, deferred launch instruction, or handoff text cannot satisfy RUN completion; the required path is `DEPENDENCY_CALL` -> `RUN_WAITING_FOR_DEPENDENCY_RETURN` -> verified `DEPENDENCY_RETURN`.
- If required validation or evidence is absent, FINISH must fail.

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

NEXT_CHAT_CARD is post-closed continuation only. It is not a dependency call, not a support dependency launch, and not evidence that the current START goal has completed. It may appear only inside FINISH_PACKET after FINISH audit passes, or as a clearly named post-closed continuation. It is for a new independent lifecycle after the current START goal is completed or explicitly blocked. It must not represent unfinished dependency work, replace `DEPENDENCY_CALL`, or make the user assemble a missing dependency call from scattered earlier text.

Old dependency packet and waiting-state labels are unsupported; the hard gates above use dependency-neutral fields.

## Failure Behavior

FINISH failure must return one of:

- `RUN_REPAIR_REQUIRED` when the selected procedure can repair the gap in the same lifecycle;
- `BLOCKED_ESCALATION` when source, authority, validation, dependency return, or completion proof is missing;
- `CONTEXT_REQUEST` when exact user input or source excerpts are required.

FINISH failure must not emit a closed-chat result.

## Closed Boundary

After FINISH passes, the chat enters CLOSED. Same-chat follow-up may clarify the closed result or point to the emitted card, but it must not start new material work.

## Quality Check Ownership

This protocol owns FINISH audit quality checks. Ordinary FINISH applies these checks from this protocol and does not require an external check file.

- FINISH follows passed CLOSURE_CHECK or an explicit blocked completion condition from the selected procedure.
- FINISH audits START, RUN, dependency returns, declared stage progression, validation/evidence, and selected procedure completion before closure.
- FINISH_PACKET includes human-readable result, evidence, validation, project refresh requirements when relevant, residual risks, and exactly one continuation state.
- FINISH fails when it would be first reveal of work, close with completion gaps, rely on open/missing/unverified dependency returns, omit required validation/evidence, treat package/card/handoff/dependency-call output as completion, or use NEXT_CHAT_CARD for unfinished current-goal dependency work.
- FINISH failure returns to RUN repair, blocked escalation, or Context Request; it must not emit a closed-chat result.

END_OF_FILE: workflow_v3/control_plane/CHAT_FINISH_PROTOCOL.md
