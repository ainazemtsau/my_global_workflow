# Workflow v3 Activation Status

status: active_skeleton_namespace_corrected

## Status matrix

| Surface | Status |
| --- | --- |
| workflow_v3_production_namespace_skeleton | active |
| workflow_v3_interface_layer | active_repository_documentation_setup_only |
| workflow_v3_repository_completion_framework | active_repository_documentation_setup_only |
| workflow_v3_steering_procedure_stub_layer | ready_repository_source_only |
| setup_only_root_direction_definition_split | ready_repository_source_only |
| ordinary_direction_project_installer | ready_repository_source_only |
| direction_project_binding_protocol | ready_repository_source_only |
| direction_adoption | none |
| concrete_direction_runtime_roots | none |
| ordinary_direction_project_bindings | none |
| governance_maintenance_project_ui_update | deferred_until_final_repository_cleanup |
| ordinary_direction_project_ui_update | none |
| legacy_state_import | none |
| project_files_sources_refresh | none |
| request_only_sources_refresh | none_performed |
| project_instruction_ui_update_required | true |
| project_sources_files_refresh_required | false |
| request_only_sources_refresh_required | false_or_on_demand_only |
| generated_project_pack_upload | none |
| old_workflow_os_decommission | none |

## What is activated at this slice

Activated means only this:

- the repository now has the initial `workflow_v3/**` documentation/setup skeleton;
- the repository now has an interface layer refinement under `workflow_v3/interfaces/**`;
- the repository now has completion, adoption-template, procedure, and owner-quality readiness files under `workflow_v3/**`;
- the repository now has canonical procedure stubs under `workflow_v3/procedures/**` for steering-entity candidate formation;
- the repository now separates ordinary Direction setup-only root bootstrap from semantic Direction Definition;
- the repository now has universal ordinary Direction Project installer, setup manifest, launch packet, procedure, and owner-quality sources for future manual Project creation;
- the repository now has repository-only Direction Project binding and continuation protocol sources for future post-bootstrap setup;
- the skeleton defines Workflow v3 production namespace boundaries for later packages;
- the skeleton may be cited as the starting source for future Workflow v3 setup work.

Activation at this slice does not mean a live runtime exists. It does not create accepted Direction state, accepted v3 state, migration authority, actual Project UI update authority, Project Files/Sources refresh authority, request-only source refresh authority, legacy import authority, or decommission authority.

## Governance Project UI status

- The Governance Maintenance Project Instructions source has changed.
- The actual Governance Maintenance Project Instructions UI is not updated to the current source yet.
- Manual UI update is intentionally deferred until final repository cleanup is complete.
- The canonical copy source is `workflow_v3/project_setup/GOVERNANCE_MAINTENANCE_PROJECT_INSTRUCTIONS.md`.
- The human copies only the trimmed payload between `BEGIN_CHATGPT_PROJECT_INSTRUCTIONS_UI_PAYLOAD` and `END_CHATGPT_PROJECT_INSTRUCTIONS_UI_PAYLOAD`.
- Repository commits do not perform external ChatGPT Project UI updates.
- No Project Files/Sources were refreshed.
- No request-only sources were refreshed.
- No Direction adoption or runtime root was created.

## Current Project refresh status

- `project_instruction_ui_update_required`: true, deferred until final repository cleanup is complete.
- `project_sources_files_refresh_required`: false.
- `request_only_sources_refresh_required`: false by default; request-only sources are loaded on demand by admitted future tasks.
- `do_not_upload_as_project_file`: Project Instructions sources remain UI payload sources, not Project Files/Sources uploads by default.

## What remains not activated

Not activated in this slice:

- any Direction adoption;
- any `directions_v3/<direction-id>/runtime/**` state root;
- any old Direction state import;
- any bridge from old Direction files into accepted v3 state;
- any ordinary Direction Project Instructions UI update;
- current Governance Maintenance Console Project Instructions UI update after final repository cleanup;
- any ordinary Direction Project binding installed in a concrete runtime root;
- any semantic Direction Definition accepted for a concrete Direction;
- any ordinary Direction Project manual creation;
- any current Project Files/Sources refresh;
- any request-only source refresh;
- any generated Project Pack;
- any generated Project Pack upload;
- any old Workflow OS archive, deletion, rename, move, replacement, or decommission.

## Allowed future packages

Allowed future packages must be separate, explicit, bounded, and validated. Examples:

- production runtime rule refinement under `workflow_v3/**`;
- procedure body authoring under `workflow_v3/procedures/**`;
- future setup-only root package for one Direction, followed by separate Direction Definition;
- future Project setup package with measured payload character counts;
- future manual ordinary Direction Project creation from `workflow_v3/project_setup/UNIVERSAL_DIRECTION_PROJECT_INSTALLER.md`;
- future project pack generation package;
- one per-Direction adoption package after an explicit adoption decision;
- clean-start Direction runtime state package under `directions_v3/<direction-id>/runtime/**`;
- bridge or selective import package only after explicit policy and evidence;
- rollback/coexistence verification package.

## Forbidden next actions

Forbidden as an implicit follow-up to this slice:

- adopting a Direction automatically;
- importing old Direction state automatically;
- treating old Ledger, Obligations, Receipts, or project files as accepted_v3_state;
- updating additional actual ChatGPT Projects from these files;
- creating an ordinary Direction Project automatically from these files;
- refreshing current Project Files/Sources from these files;
- uploading these files as current Project Files/Sources without a later explicit rollout/adoption package;
- deleting, renaming, moving, replacing, or decommissioning old Workflow OS files;
- using candidate docs as accepted Direction state.

END_OF_FILE: workflow_v3/ACTIVATION_STATUS.md
