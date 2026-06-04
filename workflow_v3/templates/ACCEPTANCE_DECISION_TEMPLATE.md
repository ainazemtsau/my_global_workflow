# Acceptance Decision Template

status: template

## Acceptance Decision

`acceptance_decision_id`:

`procedure_ref`: workflow_v3/procedures/ACCEPTANCE_DECISION_FORMATION_PROCEDURE.md

`formation_eval_ref`: workflow_v3/evals/ACCEPTANCE_DECISION_FORMATION_EVAL.md

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

`finish_packet_ref`:

`limitations`:

## Boundary

Adapters cannot accept their own output.

Acceptance Decision must be explicit, sourced, and separate from Result Packet, Evidence, Run, FINISH_PACKET, Next Move Packet, Transfer Packet, or chat intuition.

Acceptance formation must separate result quality from state mutation authorization.

Only accepted decisions and authorized update paths may mutate accepted state.

Acceptance Decision may authorize that storage update is needed.

It does not itself admit the producing chat to write.

Storage mutation requires Storage Update Package / `storage_update_adapter` admission.

Human acceptance input is not storage authorization unless an admitted storage update package exists.

END_OF_FILE: workflow_v3/templates/ACCEPTANCE_DECISION_TEMPLATE.md
