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

## Non-creation boundary

This setup creates the Project behavior surface only.

It does not create:

- `directions_v3/<direction-id>/runtime/**`;
- accepted Direction Spine;
- accepted Direction Map;
- accepted Active Front;
- product work;
- Project Files/Sources refreshes;
- request-only source refreshes;
- legacy import or migration.

## First Project chat requirements

The first chat in the new ordinary Direction Project must:

- identify itself as an ordinary Workflow v3 Direction Project;
- ask for and normalize `direction_id` if missing;
- classify `adoption_mode`;
- emit the lifecycle signal for root bootstrap, usually `direction_runtime_missing` or `direction_adoption_needed`;
- use `workflow_v3/runbooks/DIRECTION_PROJECT_ROOT_BOOTSTRAP_RUNBOOK.md`;
- stop if a required source or decision is missing;
- require explicit user acceptance before preparing a runtime root package;
- return a bounded root bootstrap status, Event Loop Closure, and exact next move.

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
project_instruction_ui_update_required: true_for_future_manual_creation_only
project_sources_files_refresh_required: false
request_only_sources_refresh_required: false
```

## Expected refresh report

- `project_instruction_ui_update_required`: true for future ordinary Direction Project manual creation only; not performed by repository commit.
- `project_sources_files_refresh_required`: false.
- `request_only_sources_refresh_required`: false.
- `do_not_upload_as_project_file`: `workflow_v3/project_setup/*PROJECT_INSTRUCTIONS*.md`, `workflow_v3/interfaces/**`, `workflow_v3/templates/**`, `workflow_v3/completion/**`, `workflow_v3/adoption/**`, `workflow_v3/runbooks/**`, and `workflow_v3/evals/**`.

END_OF_FILE: workflow_v3/project_setup/UNIVERSAL_DIRECTION_PROJECT_INSTALLER.md
