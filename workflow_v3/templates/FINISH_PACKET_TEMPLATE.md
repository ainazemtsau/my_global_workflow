# FINISH_PACKET Template

status: template

## FINISH_PACKET

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

`continuation` must contain either `NEXT_CHAT_CARD` or `no_next_chat_needed` with reason.

## Required Audit Fields

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
  child_procedure_calls_returned_to_same_main_procedure:
  required_child_work_opened_when_detected:
  no_open_child_procedure_calls:
  all_required_child_returns_received:
  all_required_child_returns_verified:
  closure_check_compared_actual_result_to_completion:
  no_handoff_card_or_package_used_as_completion:
  required_validation_present_when_work_required_validation:
  closure_check_gaps_empty_or_blocked_completion_explicit:
  next_chat_card_not_used_for_unfinished_child_work:
  no_unadmitted_state_mutation:
  no_hidden_launch_or_acceptance:
  next_chat_card_or_no_next_chat_needed_present:
```

## Boundary

FINISH_PACKET closes the selected chat procedure after explicit FINISH and passed audit. It is not acceptance, persistence, launch authority, permission to switch procedures, or completion by package/card/handoff alone. It must fail when required child/adaptor repair was detected but no child call was opened, child calls are open, returns are missing or unverified, validation/evidence is absent, completion gaps are non-empty without explicit blocked completion, or `NEXT_CHAT_CARD` carries unfinished current-goal child work.

## Quality Checks

- FINISH_PACKET follows passed CLOSURE_CHECK or explicit blocked completion from the selected procedure.
- FINISH audit compares START, RUN, child returns, declared stage sequence, validation/evidence, and selected procedure completion.
- FINISH_PACKET includes human-readable result, evidence, validation, project refresh requirements when relevant, residual risks, and continuation.
- Continuation is exactly post-closed NEXT_CHAT_CARD for a new independent lifecycle or `no_next_chat_needed` with reason.
- FINISH_PACKET must not be first reveal of work, close with non-empty gaps unless blocked completion is explicit, or silently launch next work.

END_OF_FILE: workflow_v3/templates/FINISH_PACKET_TEMPLATE.md
