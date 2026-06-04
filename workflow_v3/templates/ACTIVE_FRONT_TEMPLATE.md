# Active Front Template

status: template

## Active Front

`front_id`:

`front_status`: none_selected | pending_definition | candidate | accepted | closed | superseded

`procedure_ref`: workflow_v3/procedures/ACTIVE_FRONT_FORMATION_PROCEDURE.md

`formation_eval_ref`: workflow_v3/evals/ACTIVE_FRONT_FORMATION_EVAL.md

`source_direction_map_ref`:

`source_goal_evidence_graph_ref`:

`active_unresolved_cut_ref`:

`source_map_areas`:

`source_graph_node_refs`:

`touched_tracks`:

`success_dimensions_touched`:

`bottleneck_or_uncertainty`:

`why_now`:

`selection_reason`: root_criticality | bottleneck_relief | uncertainty_reduction | dependency_unlock | evidence_value | reversibility | WIP_capacity | success_dimension_balance | explicit_user_priority

`selection_evidence`:

`rejected_or_deferred_alternatives`:

`front_exit_criteria`:

`exit_criteria_graph_or_map_claim_refs`:

`in_scope`:

`out_of_scope`:

`first_work_graph_seed`:

`blockers`:

`acceptance_question`:

`acceptance_decision_ref`:

`closure_policy`:

## Boundary

Active Front is not global Direction state, a roadmap, or all active work.

The front remains candidate until accepted through an explicit acceptance/update path.

`none_selected` or `pending_definition` is valid for setup-only root placeholders only. It is not accepted semantic content.

This template does not adopt a Direction, create runtime state, or authorize `directions_v3/<direction-id>/runtime/**`.

END_OF_FILE: workflow_v3/templates/ACTIVE_FRONT_TEMPLATE.md
