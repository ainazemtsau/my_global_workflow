# Direction Runtime Root Manifest Template

status: template

## Boundary

This is a template for a future authorized runtime root creation package. It does not create a runtime root now.

## Runtime root target

```text
directions_v3/<direction-id>/runtime/**
```

## Manifest fields

`direction_id`:

`runtime_root_path`:

`adoption_package_ref`:

`acceptance_decision_ref`:

`adoption_mode`:

`clean_start_reason`:

`legacy_evidence_allowed`:

`legacy_evidence_paths`:

`accepted_initial_direction_spine_ref`:

`accepted_initial_direction_map_ref`:

`accepted_initial_active_front_ref`:

`initial_current_status_ref`:

`initial_current_next_move_ref`:

`created_subdirectories`:

`project_setup_required`:

`project_refresh_required`:

`rollback/coexistence notes`:

`validation_evidence`:

## Required future subdirectories

```text
state/
fronts/
records/
memory/
operations/signals/
operations/action_inbox/
operations/check_jobs/
operations/event_loop_closures/
operations/recovery/
archive/
indexes/
config/
console/
```

## No-storage rules

- Project Instructions UI is external and not stored as accepted Direction runtime state.
- Project Files/Sources are external cache/context and not source authority.
- Result Packets, Evidence, and Acceptance Decisions are stored as records if persisted; they are not accepted state unless an accepted update mutates state files.
- Legacy evidence remains outside the runtime root unless a later explicit bridge/import package authorizes a copy or reference.

END_OF_FILE: workflow_v3/adoption/DIRECTION_RUNTIME_ROOT_MANIFEST_TEMPLATE.md
