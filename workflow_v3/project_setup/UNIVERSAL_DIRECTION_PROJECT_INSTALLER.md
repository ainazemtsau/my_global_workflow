# Universal Direction Project Installer

status: installer_ready_repository_source

## Purpose

This installer is the human-facing procedure for creating a new ordinary Workflow v3 Direction ChatGPT Project from repository sources.

It is not for the Workflow v3 Governance Maintenance Console.

## Target project type

ordinary Direction Project

## Preconditions

- The repository `main` SHA/ref used for setup is known and recorded.
- The user has chosen to create an ordinary Direction Project.
- No specific Direction adoption happens in the Governance Maintenance Console.
- The future Project starts from repository source authority, not from stale Project Files/Sources, old Direction files, or chat memory.

## Manual install steps

1. Create a new ChatGPT Project for one ordinary Workflow v3 Direction.
2. Open `workflow_v3/project_setup/UNIVERSAL_DIRECTION_PROJECT_INSTRUCTIONS.md` at the chosen repository ref.
3. Copy only the trimmed payload between `BEGIN_CHATGPT_PROJECT_INSTRUCTIONS_UI_PAYLOAD` and `END_CHATGPT_PROJECT_INSTRUCTIONS_UI_PAYLOAD`.
4. Paste that payload into the ChatGPT Project Instructions UI.
5. Record the measured Project Instructions UI payload character count.
6. Do not upload `workflow_v3/**` source docs as default Project Files/Sources unless a later explicit rollout says otherwise.
7. Use exact GitHub/repository source reads when material setup, adoption, bootstrap, or runtime state decisions depend on repository state.
8. Start the first Project chat with `workflow_v3/project_setup/DIRECTION_ROOT_BOOTSTRAP_LAUNCH_PACKET_TEMPLATE.md`.
9. The first chat performs setup-only root bootstrap. It does not require root outcome or accept semantic Direction content.
10. After an accepted setup-only runtime root package exists, require Project Binding installation and per-Direction Project setup source generation before treating later chats as stable.
11. Launch semantic Direction Definition from `workflow_v3/project_setup/DIRECTION_DEFINITION_LAUNCH_PACKET_TEMPLATE.md` when `CURRENT_NEXT_MOVE = launch_direction_definition`.

## Non-creation boundary

This setup creates the Project behavior surface only.

It does not create:

- `directions_v3/<direction-id>/runtime/**`;
- accepted Direction Spine;
- accepted Direction Map;
- accepted Active Front;
- Direction Definition;
- product work;
- Project Files/Sources refreshes;
- request-only source refreshes;
- legacy import or migration.

## First Project chat requirements

The first chat in the new ordinary Direction Project must:

- identify itself as an ordinary Workflow v3 Direction Project;
- ask for and normalize `direction_id` if missing;
- classify setup mode and legacy policy;
- emit the lifecycle fact for root bootstrap, usually `direction_runtime_missing` or `direction_adoption_needed`;
- use `workflow_v3/procedures/DIRECTION_PROJECT_ROOT_BOOTSTRAP_PROCEDURE.md`;
- not require initial root outcome;
- classify any user-provided outcome, tracks, or product ideas as `candidate_context_for_direction_definition` only;
- stop if a required source or decision is missing;
- require explicit user acceptance before preparing a runtime root package;
- if a setup-only runtime root package is prepared, require placeholder pending Definition statuses, `runtime/config/DIRECTION_PROJECT_BINDING.md`, and per-Direction Project setup sources in the package;
- return setup-only root status, FINISH_PACKET, Result Packet, Next Move Packet, binding installation next move, and exact next move `launch_direction_definition`.

## Post-bootstrap Project Binding requirement

After an accepted setup-only runtime root package creates `directions_v3/<direction-id>/runtime/**`, the package must also:

- create canonical runtime binding from `workflow_v3/templates/DIRECTION_PROJECT_BINDING_TEMPLATE.md`;
- write `state/DIRECTION_SPINE.md` and `state/DIRECTION_MAP.md` as `pending_definition`;
- write `state/ACTIVE_FRONT.md` as `none_selected` or `pending_definition`;
- write `state/CURRENT_STATUS.md` as `setup_only_root_created` with `semantic_definition_status: pending_definition`;
- write `state/CURRENT_NEXT_MOVE.md` with `primary_next_move: launch_direction_definition`;
- generate `directions_v3/<direction-id>/project_setup/CHATGPT_PROJECT_INSTRUCTIONS.md` from `workflow_v3/project_setup/PER_DIRECTION_PROJECT_INSTRUCTIONS_SOURCE_TEMPLATE.md`;
- generate `directions_v3/<direction-id>/project_setup/PROJECT_FILES_MANIFEST.md` from `workflow_v3/project_setup/PER_DIRECTION_PROJECT_FILES_MANIFEST_TEMPLATE.md`;
- report manual Project Instructions UI update requirements separately from Project Files/Sources refreshes;
- keep Project Files/Sources refresh default false unless an optional binding cache is explicitly used.

Next chats are not considered stable until the binding capsule has been applied to the Project Instructions UI or the user provides a binding repair/bootstrap packet naming exact repo/path/ref.

## Manual evidence fields

Record these fields after manual Project creation:

```text
project_name:
repository:
payload_source_path:
payload_source_ref:
measured_chars:
project_files_sources_decision:
request_only_sources_decision:
user_confirmation:
first_chat_launch_packet_path:
first_chat_started:
first_chat_result_summary:
candidate_context_for_direction_definition:
post_bootstrap_binding_plan:
per_direction_project_setup_sources:
direction_definition_launch_packet_path:
manual_project_instruction_ui_update_required:
project_instruction_ui_update_required: true_for_future_manual_creation_only
project_sources_files_refresh_required: false
request_only_sources_refresh_required: false
```

## Expected refresh report

- `project_instruction_ui_update_required`: true for future ordinary Direction Project manual creation only; not performed by repository commit.
- `project_sources_files_refresh_required`: false.
- `request_only_sources_refresh_required`: false.
- `do_not_upload_as_project_file`: `workflow_v3/project_setup/*PROJECT_INSTRUCTIONS*.md`, `workflow_v3/interfaces/**`, `workflow_v3/templates/**`, `workflow_v3/completion/**`, `workflow_v3/adoption/**`, `workflow_v3/procedures/**`, and `workflow_v3/evals/**`.

END_OF_FILE: workflow_v3/project_setup/UNIVERSAL_DIRECTION_PROJECT_INSTALLER.md
