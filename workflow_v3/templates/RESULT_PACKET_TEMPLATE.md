# Result Packet Template

status: template

## Result Packet

`result_packet_id`:

`source_run_or_child_ref`:

`work_contract_ref`:

`result_summary`:

`material_output`:

`evidence_refs`:

`validation_results`:

`limitations`:

`out_of_scope_not_done`:

`candidate_state_changes`:

`parent_integration_result_ref_if_any`:

`graph_delta_ref_if_any`:

`upstream_escalation_ref_if_any`:

`downstream_delta_ref_if_any`:

`derived_gate_check_ref_if_any`:

`acceptance_question`:

`recommended_next_move`:

`closure_fact`:

## Boundary

Result Packet is candidate until accepted.

It does not mutate accepted state, accept evidence, or route product meaning by itself.

State changes require Acceptance Decision and the explicit acceptance/update path.

END_OF_FILE: workflow_v3/templates/RESULT_PACKET_TEMPLATE.md
