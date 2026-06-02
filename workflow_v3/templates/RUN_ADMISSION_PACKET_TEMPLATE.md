# Run Admission Packet Template

status: template

## Run Admission Packet

`requested_action`:

`normalized_entrypoint`:

`procedure_ref`:

`source_lock_ref_or_inline`:

`resolved_commit_sha`:

`run_surface_type`:

`allowed_operations`:

`forbidden_operations`:

`required_inputs`:

`required_outputs`:

`write_admission`:

`acceptance_admission`:

`legacy_policy`:

`validation_required`:

`stop_conditions`:

`return_destination`:

## Boundary

Admission permits only the listed run surface and operations. Material admission for branch refs such as `main` should include the resolved commit SHA. Crossing run surface or write boundary requires new admission.

END_OF_FILE: workflow_v3/templates/RUN_ADMISSION_PACKET_TEMPLATE.md
