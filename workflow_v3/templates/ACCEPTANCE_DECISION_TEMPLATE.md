# Acceptance Decision Template

status: template

## Acceptance Decision

`acceptance_decision_id`:

`decision_status`: accepted | rejected | repair_required | blocked | parked

`candidate_result_ref`:

`evidence_refs`:

`reviewer_or_decision_source`:

`accepted_changes`:

`rejected_changes`:

`repair_required`:

`state_mutation_authorized`:

`storage_update_needed`:

`codex_or_human_action_needed`:

`event_loop_closure_ref`:

`limitations`:

## Boundary

Adapters cannot accept their own output.

Acceptance Decision must be explicit, sourced, and separate from Result Packet, Evidence, Run, Signal, Handler, Action Inbox, or chat intuition.

Only accepted decisions and authorized update paths may mutate accepted state.

END_OF_FILE: workflow_v3/templates/ACCEPTANCE_DECISION_TEMPLATE.md
