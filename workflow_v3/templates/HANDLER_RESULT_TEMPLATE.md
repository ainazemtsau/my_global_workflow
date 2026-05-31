# Handler Result Template

status: template

## Handler Result

`handler_name`:

`matched_signal_id`:

`matched_reason`:

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
- `human_decision_request`;
- `no_action_with_reason`.

## Boundary

Handler output is candidate only.

No handler may silently launch work.

END_OF_FILE: workflow_v3/templates/HANDLER_RESULT_TEMPLATE.md
