# FINISH_PACKET Eval

status: active_eval

## Required Checks

- FINISH follows passed `CLOSURE_CHECK` or explicit blocked completion from the selected procedure.
- FINISH audit compares START, RUN, child returns, declared stage sequence, validation evidence, and selected procedure completion.
- FINISH audit includes `start_goal_was_explicit`, `start_goal_satisfied_or_explicitly_blocked`, `declared_stage_sequence_not_compressed`, `required_child_work_opened_when_detected`, `no_open_child_procedure_calls`, `all_required_child_returns_received`, `all_required_child_returns_verified`, `no_handoff_card_or_package_used_as_completion`, `required_validation_present_when_work_required_validation`, `closure_check_gaps_empty_or_blocked_completion_explicit`, and `next_chat_card_not_used_for_unfinished_child_work`.
- FINISH does not close if CHECK failed.
- FINISH failure returns to RUN repair or blocked escalation.
- FINISH_PACKET includes human-readable result, evidence, validation, refresh requirements when relevant, and residual risks.
- FINISH_PACKET includes post-closed `NEXT_CHAT_CARD` when a new independent lifecycle is needed.
- FINISH_PACKET includes `no_next_chat_needed` with reason when continuation is not needed.

## Failure Checks

- FINISH is first reveal of work.
- FINISH closes with unverified child evidence.
- FINISH closes with open child call.
- FINISH closes when required child return is missing.
- FINISH closes when required child/adaptor repair was identified but not opened, returned, and verified.
- FINISH closes when required validation/evidence is absent.
- FINISH closes despite completion gaps.
- FINISH passes when actual result is only a patch plan, package, handoff, or card for required current-goal repair.
- FINISH closes with non-empty gaps unless blocked completion is explicit and result is marked blocked.
- FINISH closes when actual_result is only a child call, handoff, card, package, copy-paste packet, Codex package, check packet, storage packet, child-chat card, or `NEXT_CHAT_CARD`.
- FINISH uses `NEXT_CHAT_CARD` for unfinished child work.
- FINISH omits continuation card or no-continuation reason.
- FINISH silently launches next work.

END_OF_FILE: workflow_v3/evals/FINISH_PACKET_EVAL.md
