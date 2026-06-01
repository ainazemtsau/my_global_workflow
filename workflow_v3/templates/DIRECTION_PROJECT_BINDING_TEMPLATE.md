# Direction Project Binding Template

status: template

## Boundary

This template is for a future accepted runtime root package. It does not create a runtime root, adopt a Direction, update Project Instructions UI, refresh Project Files/Sources, or accept product state.

Future concrete target path:

```text
directions_v3/<direction-id>/runtime/config/DIRECTION_PROJECT_BINDING.md
```

## Binding fields

`direction_id`:

`binding_status`: candidate | accepted | superseded

`project_type`: ordinary_direction_project

`semantic_definition_status`: pending_definition | candidate | accepted | blocked

`runtime_root`: directions_v3/<direction-id>/runtime/

`current_status_path`: directions_v3/<direction-id>/runtime/state/CURRENT_STATUS.md

`current_next_move_path`: directions_v3/<direction-id>/runtime/state/CURRENT_NEXT_MOVE.md

`direction_spine_path`: directions_v3/<direction-id>/runtime/state/DIRECTION_SPINE.md

`direction_map_path`: directions_v3/<direction-id>/runtime/state/DIRECTION_MAP.md

`active_front_path`: directions_v3/<direction-id>/runtime/state/ACTIVE_FRONT.md

`project_setup_source_path`: directions_v3/<direction-id>/project_setup/CHATGPT_PROJECT_INSTRUCTIONS.md

`project_files_manifest_path`: directions_v3/<direction-id>/project_setup/PROJECT_FILES_MANIFEST.md

`project_instruction_payload_source_ref`:

`accepted_root_package_ref`:

`acceptance_decision_ref`:

`source_authority`: Exact repository files at named repo/path/ref win over Project Files/Sources, uploaded files, generated packs, summaries, chat memory, Project title, and optional binding cache.

`project_title_hint`:

`project_title_is_not_authority`: true

## Binding capsule payload

Generate this compact payload from the accepted binding source and include it in the per-Direction Project Instructions UI payload:

```text
Project Binding Capsule:
direction_id:
runtime_root:
current_status_path:
current_next_move_path:
project_binding_source_path:
project_setup_source_path:
project_files_manifest_path:
source_authority: exact repo/path/ref wins; Project title, previous chat memory, Project Files/Sources, and optional binding cache are not binding authority.
```

## Optional Project File cache policy

`optional_project_file_cache_policy`:

- The binding file may be uploaded as a small Project File/Sources cache only after the concrete runtime root exists.
- If uploaded, it remains cache/context only.
- It cannot override the exact repository runtime binding source.
- It must be listed in the concrete per-Direction Project Files manifest.

## Update policy

`update_policy`:

- Update the canonical runtime binding through an explicit accepted package.
- Regenerate the Project Instructions UI binding capsule from the canonical binding.
- Report Project Instructions UI update requirements separately from Project Files/Sources refreshes.
- Supersede old binding records instead of silently overwriting accepted source history.

## Conflict policy

`conflict_policy`:

- If capsule, runtime binding, optional Project File cache, Project title, or user input conflict, stop.
- Verify exact repository binding source.
- Ask for binding repair if exact source cannot resolve the conflict.
- Do not infer from title, memory, or whole-repository search.

## Limitations

`limitations`:

- This binding is a Project-to-Direction locator and continuation configuration.
- It does not create accepted Direction state.
- It does not authorize product execution.
- It does not replace Direction Map, Active Front, Work Graph, Work Contract, Current Status, or Current Next Move.
- It may exist while semantic Direction definition is pending.

## Boundary

Binding is not accepted product state, not Direction Map, not Work Graph, not Project title, not previous chat memory.

END_OF_FILE: workflow_v3/templates/DIRECTION_PROJECT_BINDING_TEMPLATE.md
