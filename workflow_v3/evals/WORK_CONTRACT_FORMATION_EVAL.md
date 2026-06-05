# Work Contract Formation Eval

status: active_eval

## Purpose

Validate Work Contract formation quality.

## PASS checks

- Uses the registered canonical `workflow_v3/procedures/WORK_CONTRACT_FORMATION_PROCEDURE.md` source; if the procedure is still a stub, it stops with `PROCEDURE_BODY_NOT_AUTHORED`.
- Forms one bounded run target.
- Includes target, parent_graph_node_ref, parent_front_ref, parent_work_graph_node_ref, relation_to_parent, source_authority, in_scope, out_of_scope, allowed_surfaces, forbidden_surfaces, expected_result, evidence_required, validation_required, return_destination, and stop_conditions.
- Returns `split_required` when the target combines independent jobs.
- Does not grant route, acceptance, product-meaning, or scope-expansion authority.
- Returns Launch Packet or exact next move.

## WARN checks

- Validation is limited but the limitation is explicit.
- Human action is needed before launch.

## FAIL checks

- Contract combines multiple independent jobs.
- Allowed/forbidden surfaces are missing.
- Parent graph/front/node refs or relation_to_parent are missing.
- Evidence or validation requirement is missing.
- Adapter output is treated as accepted.

END_OF_FILE: workflow_v3/evals/WORK_CONTRACT_FORMATION_EVAL.md
