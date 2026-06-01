# Current Status Template

status: template

## Current Status

`direction_id`:

`status_refreshed_at_or_record_ref`:

`setup_status`: not_started | setup_only_root_created | complete | blocked

`semantic_definition_status`: pending_definition | candidate | accepted | blocked

`project_binding_status`: missing | candidate | accepted | stale | conflicted

`current_phase`: setup_only_root | direction_definition | active_front | work_graph | work_contract

`current_direction_spine_ref`:

`current_direction_map_ref`:

`current_active_front_ref`:

`current_work_graph_ref`:

`current_node_or_work_contract_ref`:

`current_blockers`:

`current_open_decisions`:

`current_evidence_status`:

`current_project_setup_status`:

`limitations`:

## Boundary

Current Status is a status view only.

It is not accepted state unless backed by the required acceptance/update path and exact accepted records.

This template does not adopt a Direction, create runtime state, update Project Instructions UI, or refresh Project Files/Sources.

Setup-only root may use `setup_status: setup_only_root_created` and `semantic_definition_status: pending_definition`.

END_OF_FILE: workflow_v3/templates/CURRENT_STATUS_TEMPLATE.md
