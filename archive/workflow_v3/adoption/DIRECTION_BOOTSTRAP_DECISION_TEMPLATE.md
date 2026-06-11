# Direction Bootstrap Decision Template

status: template

## Purpose

This template records the explicit decision needed before a future Direction can be adopted into Workflow v3.

## Decision fields

`decision_id`:

`direction_id`:

`decision_status`: accepted | rejected | repair_required | blocked | no_adoption

`adoption_mode`: clean_start | bridge_only | selective_import | full_migration | no_adoption

`clean_start_reason`:

`legacy_evidence_allowed`: true | false

`legacy_evidence_paths`:

`accepted_initial_direction_spine`:

`accepted_initial_direction_map`:

`accepted_initial_active_front`:

`project_setup_required`: true | false

`project_refresh_required`: true | false

`rollback/coexistence notes`:

`acceptance_decision_ref`:

`source_refs`:

`decision_maker_or_source`:

`limitations`:

## Acceptance rule

The decision must be explicit. A chat summary, Codex commit, Result Packet, old Direction file, Project File, or generated pack cannot substitute for this decision.

## Stop conditions

Stop if Direction identity, adoption mode, accepted initial state, Project setup authorization, or rollback/coexistence boundary is unclear.

END_OF_FILE: workflow_v3/adoption/DIRECTION_BOOTSTRAP_DECISION_TEMPLATE.md
