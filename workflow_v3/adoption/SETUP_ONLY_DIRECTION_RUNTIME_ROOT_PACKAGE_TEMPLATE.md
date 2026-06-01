# Setup-Only Direction Runtime Root Package Template

status: template_only

## Future concrete target

```text
directions_v3/<direction-id>/runtime/**
```

## Package purpose

Create a setup-only technical runtime root and binding for one future Direction.

This package is not semantic Direction content. It does not accept Direction Spine, Direction Map, Active Front, Work Graph, or product work.

## Required inputs

```text
direction_id:
setup_mode: setup_only_root_bootstrap
legacy_policy: no_import | read_only_legacy_evidence
project_binding_required: true
per_direction_project_setup_sources_required: true
candidate_context_for_direction_definition:
```

## Explicitly not required

- root outcome;
- accepted Direction Spine;
- accepted Direction Map;
- accepted Active Front;
- Work Graph.

## Required future files

```text
state/DIRECTION_SPINE.md                status: pending_definition
state/DIRECTION_MAP.md                  status: pending_definition
state/ACTIVE_FRONT.md                   status: none_selected or pending_definition
state/CURRENT_STATUS.md                 setup_status: setup_only_root_created
state/CURRENT_NEXT_MOVE.md              primary_next_move: launch_direction_definition
config/DIRECTION_PROJECT_BINDING.md
console/DIRECTION_CONSOLE.md            if used
directions_v3/<direction-id>/project_setup/CHATGPT_PROJECT_INSTRUCTIONS.md
directions_v3/<direction-id>/project_setup/PROJECT_FILES_MANIFEST.md
```

## Validation requirements

- no accepted semantic Direction content appears in placeholder files;
- candidate context is labeled as candidate context only;
- Project Binding resolves exact status and next-move paths;
- per-Direction Project setup sources are generated;
- manual Project Instructions UI update requirement is reported separately;
- no Project Files/Sources refresh is implied by default.

## Refresh requirements

```text
project_instruction_ui_update_required: true after concrete per-Direction source generation; manual only
project_sources_files_refresh_required: false by default
request_only_sources_refresh_required: false
do_not_upload_as_project_file: workflow_v3/** source docs and concrete Project Instructions source unless a later rollout says otherwise
```

## Stop conditions

Stop if the package requires root outcome, accepts Spine/Map/Front, starts product work, imports legacy state, lacks binding/setup sources, or implies actual Project UI update by repository commit.

END_OF_FILE: workflow_v3/adoption/SETUP_ONLY_DIRECTION_RUNTIME_ROOT_PACKAGE_TEMPLATE.md
