# Storage Update Package Template

status: template

## Storage Update Package

`storage_update_id`:

`source_acceptance_decision_ref`:

`candidate_result_ref`:

`allowed_files`:

`forbidden_paths`:

`exact_required_changes`:

`expected_diff_or_file_states`:

`validation_commands_or_checks`:

`source_integrity_requirements`:

`stop_conditions`:

`commit_policy`:

`push_policy`:

`return_fields`:

## Boundary

Human acceptance input is not storage authorization. Storage update requires adapter admission and exact package fields.

## Quality Checks

- Package includes source acceptance decision or admitted source authority, candidate result, allowed files, forbidden paths, exact changes, expected diff or file states, validation, source integrity requirements, stop conditions, commit policy, push policy, and return fields.
- Adapter touches only listed files and returns validation output.
- Project Instructions payload count and refresh categories are returned when those sources change.
- Package omission, unlisted path mutation, or treating human acceptance input as storage execution authority fails admission.

END_OF_FILE: workflow_v3/templates/STORAGE_UPDATE_PACKAGE_TEMPLATE.md
