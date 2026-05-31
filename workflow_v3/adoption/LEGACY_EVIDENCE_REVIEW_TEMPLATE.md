# Legacy Evidence Review Template

status: template

## Boundary

Old `directions/**` files are `legacy_evidence` only. This review may inform a current decision, but it must not import, migrate, accept, or rewrite old state by implication.

## Review fields

`review_id`:

`direction_id`:

`adoption_mode`:

`clean_start_reason`:

`legacy_evidence_allowed`: true | false

`legacy_evidence_paths`:

`source_ref_and_read_completeness`:

`evidence_summary`:

`candidate_relevance_to_initial_direction_spine`:

`candidate_relevance_to_initial_direction_map`:

`candidate_relevance_to_initial_active_front`:

`explicitly_not_imported`:

`conflicts_or_gaps`:

`project_setup_required`: true | false

`project_refresh_required`: true | false

`rollback/coexistence notes`:

`acceptance_decision_ref`:

`limitations`:

## Allowed use

Legacy evidence may be cited as context for a current acceptance decision only when the citation is explicit, sourced, and labeled as `legacy_evidence`.

## Forbidden use

Do not treat old Ledger, Obligations, Receipts, Dashboard, Commit Scopes, Project setup files, old Direction Map, old project files, or old migration receipts as accepted Workflow v3 state.

## Stop conditions

Stop if review pressure becomes implicit migration, old-state import, invented Direction proof state, or Project setup action without authorization.

END_OF_FILE: workflow_v3/adoption/LEGACY_EVIDENCE_REVIEW_TEMPLATE.md
