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

`setup_mode`: setup_only_root_bootstrap | semantic_adoption

`clean_start_reason`:

`legacy_evidence_allowed`:

`legacy_evidence_paths`:

`accepted_initial_direction_spine_ref`:

`accepted_initial_direction_map_ref`:

`accepted_initial_active_front_ref`:

`direction_spine_status`: pending_definition | candidate | accepted | superseded

`direction_map_status`: pending_definition | candidate | accepted | superseded

`active_front_status`: none_selected | pending_definition | candidate | accepted | closed | superseded

`initial_current_status_ref`:

`initial_current_next_move_ref`:

`project_binding_ref`: config/DIRECTION_PROJECT_BINDING.md

`per_direction_project_instructions_source_ref`: directions_v3/<direction-id>/project_setup/CHATGPT_PROJECT_INSTRUCTIONS.md

`per_direction_project_files_manifest_ref`: directions_v3/<direction-id>/project_setup/PROJECT_FILES_MANIFEST.md

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

## Required future config files

```text
config/DIRECTION_PROJECT_BINDING.md
```

## Setup-only root state allowance

For setup-only root creation, semantic state files may exist as placeholders only:

```text
state/DIRECTION_SPINE.md      status: pending_definition
state/DIRECTION_MAP.md        status: pending_definition
state/ACTIVE_FRONT.md         status: none_selected or pending_definition
state/CURRENT_STATUS.md       setup_status: setup_only_root_created; semantic_definition_status: pending_definition
state/CURRENT_NEXT_MOVE.md    primary_next_move: launch_direction_definition
```

This allowance does not accept semantic Direction content.

## Optional related project setup source paths

```text
directions_v3/<direction-id>/project_setup/CHATGPT_PROJECT_INSTRUCTIONS.md
directions_v3/<direction-id>/project_setup/PROJECT_FILES_MANIFEST.md
```

## No-storage rules

- Project Instructions UI is external and not stored as accepted Direction runtime state.
- Project Files/Sources are external cache/context and not source authority.
- Result Packets, Evidence, and Acceptance Decisions are stored as records if persisted; they are not accepted state unless an accepted update mutates state files.
- Legacy evidence remains outside the runtime root unless a later explicit bridge/import package authorizes a copy or reference.
- Pending setup-only state is not accepted semantic Direction state.

END_OF_FILE: workflow_v3/adoption/DIRECTION_RUNTIME_ROOT_MANIFEST_TEMPLATE.md
