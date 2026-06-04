# Storage Update Protocol

status: active_control_plane

## Purpose

Storage update is a separate adapter surface. It is the only control-plane surface that may write accepted repository/runtime state after admission.

Acceptance Decision may authorize that storage update is needed. It does not grant the producing candidate or acceptance chat permission to write.

Canonical persistence requires storage_update_adapter admission.

GitHub write tools are default-denied by workflow policy.

No write without exact allowed files, forbidden paths, expected diff, validation, and return fields.

## Storage Update Package required fields

```text
storage_update_id:
source_acceptance_decision_ref:
candidate_result_ref:
allowed_files:
forbidden_paths:
exact_required_changes:
expected_diff_or_file_states:
validation_commands_or_checks:
source_integrity_requirements:
stop_conditions:
commit_policy:
push_policy:
return_fields:
```

## Adapter boundary

The adapter may apply only listed changes to listed files, run listed checks, and return evidence. It must not decide acceptance, broaden scope, touch unlisted paths, continue to the next semantic step, or use chat memory/cache as accepted state.

If storage update touches `Project Instructions` source, payload character count must be recalculated and refresh classifications must be returned.

END_OF_FILE: workflow_v3/control_plane/STORAGE_UPDATE_PROTOCOL.md
