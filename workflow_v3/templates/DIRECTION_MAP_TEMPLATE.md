# Direction Map Template

status: template

## Direction Map

`direction_id`:

`map_status`: pending_definition | candidate | accepted | superseded

`formation_runbook_ref`: workflow_v3/formation/DIRECTION_MAP_FORMATION_RUNBOOK.md

`formation_eval_ref`: workflow_v3/evals/DIRECTION_MAP_FORMATION_EVAL.md

`source_spine_ref`:

`map_claim_discipline`:

`tracks`:

`map_areas`:

| map_area_id | label | tracks | status | source_or_evidence | notes |
| --- | --- | --- | --- | --- | --- |
|  |  |  | candidate |  |  |

`strategic_dependencies`:

`strategic_uncertainties`:

`candidate_active_fronts`:

`accepted_or_closed_fronts`:

`blocked_areas`:

`evidence_links`:

`accepted_labels`:

`candidate_labels`:

`unresolved_labels`:

`hypothetical_labels`:

`update_candidates`:

`acceptance_decision_ref`:

`limitations`:

## Boundary

Direction Map is not a roadmap, backlog, unreviewed task list, or local Work Graph.

Map claims must be sourced and labeled as accepted, candidate, unresolved, or hypothetical.

This template does not adopt a Direction, create runtime state, or authorize `directions_v3/<direction-id>/runtime/**`.

Direction Map changes only through an explicit acceptance/update path.

`pending_definition` is valid for setup-only root placeholders only. It is not accepted semantic content.

END_OF_FILE: workflow_v3/templates/DIRECTION_MAP_TEMPLATE.md
