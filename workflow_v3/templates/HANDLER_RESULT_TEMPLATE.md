# Handler Result Template

status: template

## Handler Result

`handler_name`:

`handler_class`:

`matched_signal_id`:

`matched_reason`:

`lifecycle_transition_candidate_if_any`:

`handler_result_type`:

`output_type`:

`candidate_packet_type_if_any`:

`candidate_output`:

`return_destination`:

`closure_signal_if_launched_or_returned`:

`must_not_do_checked`:

`persistence_needed`:

`limitations`:

## Allowed output types

- `inline`;
- `action_inbox_candidate`;
- `check_job`;
- `blocked_result`;
- `repair_next_move`;
- `candidate_launch_packet`;
- `candidate_result_packet`;
- `primary_next_move`;
- `secondary_candidate`;
- `next_chat_prompt`;
- `transition_packet`;
- `stop_condition`;
- `human_decision_request`;
- `no_action_with_reason`.

## Allowed handler_result_type values

- `primary_next_move`;
- `secondary_candidate`;
- `candidate_packet`;
- `lifecycle_transition_candidate`;
- `next_chat_prompt`;
- `transition_packet`;
- `stop_condition`.

## Boundary

Handler output is candidate only.

No handler may silently launch work.

END_OF_FILE: workflow_v3/templates/HANDLER_RESULT_TEMPLATE.md
