# Handler Result Template

status: template

## Handler Result

`handler_name`:

`matched_signal_id`:

`matched_reason`:

`handler_result_type`:

`output_type`:

`candidate_output`:

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
- `next_chat_prompt`;
- `transition_packet`;
- `stop_condition`.

## Boundary

Handler output is candidate only.

No handler may silently launch work.

END_OF_FILE: workflow_v3/templates/HANDLER_RESULT_TEMPLATE.md
