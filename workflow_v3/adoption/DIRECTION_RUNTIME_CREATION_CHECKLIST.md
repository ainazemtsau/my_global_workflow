# Direction Runtime Creation Checklist

status: template

## Boundary

Use this checklist only inside a later package that explicitly authorizes runtime root creation. This file does not create runtime state.

## Preconditions

- `direction_id` is explicit.
- `adoption_mode` is explicit.
- `clean_start_reason` is recorded.
- `legacy_evidence_allowed` is explicit.
- `legacy_evidence_paths` are listed or explicitly empty.
- `accepted_initial_direction_spine` is accepted or the package is blocked.
- `accepted_initial_direction_map` is accepted or the package is blocked.
- `accepted_initial_active_front` is accepted or the package is blocked.
- `project_setup_required` is separated from repository creation.
- `project_refresh_required` is separated from repository creation.
- `rollback/coexistence notes` are present.
- `acceptance_decision_ref` authorizes creation.

## Creation checklist

- [ ] Confirm exact repository base ref.
- [ ] Confirm no existing runtime root at `directions_v3/<direction-id>/runtime/**` unless the package is an authorized repair.
- [ ] Create only the authorized runtime root and subdirectories.
- [ ] Populate state files only from accepted initial decisions.
- [ ] Do not copy old `directions/**` files into accepted state.
- [ ] Record legacy evidence references only as evidence references when authorized.
- [ ] Use Workflow v3 templates for initial state and records.
- [ ] Report Project setup impact without performing actual Project UI or Project Files/Sources updates unless separately authorized.
- [ ] Validate allowed/forbidden paths.
- [ ] Validate EOF markers for Markdown.

## Stop conditions

Stop if runtime creation would require implicit migration, missing acceptance, forbidden old-state import, unauthorized Project setup action, or any path outside the authorized runtime root.

END_OF_FILE: workflow_v3/adoption/DIRECTION_RUNTIME_CREATION_CHECKLIST.md
