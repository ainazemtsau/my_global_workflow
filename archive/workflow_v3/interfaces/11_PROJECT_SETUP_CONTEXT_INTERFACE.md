# Project Setup and Context Interface

status: active_interface_layer

## Purpose

This interface defines ChatGPT Project setup/context boundaries for Workflow v3.

## Surfaces

| Surface | Role | Boundary |
| --- | --- | --- |
| Project Instructions UI | Compact behavior bootstrap. | Not accepted state, not long docs, not auto-updated by commit. |
| Project Files/Sources | Cache/context files available to a Project. | Not canonical authority or acceptance proof. |
| Repository Project Instruction Source | Repo file used to prepare UI payload. | Commit does not apply it to the UI. |
| Request-only Sources | Loaded only for admitted tasks that need them. | Not default Project Files/Sources. |
| `do_not_upload_as_project_file` | Sources excluded from Project Files/Sources until explicit rollout. | Must be reported separately. |

## Hard boundaries

- GitHub commit does not update Project UI.
- GitHub commit does not update Project Files/Sources.
- Project Files/Sources are cache/context only.
- Exact repository path/ref wins over Project cache.
- Payload character count is required when Project Instructions sources change.
- Refresh categories must be reported separately:
  - `project_instruction_ui_update_required`;
  - `project_sources_files_refresh_required`;
  - `request_only_sources_refresh_required`;
  - `do_not_upload_as_project_file`.

## Current interface package refresh state

For this package:

- `project_instruction_ui_update_required`: false.
- `project_sources_files_refresh_required`: false for current Projects.
- `request_only_sources_refresh_required`: false.
- `do_not_upload_as_project_file`: `workflow_v3/interfaces/**` until a later explicit Workflow v3 Project setup rollout/adoption package says otherwise.

END_OF_FILE: workflow_v3/interfaces/11_PROJECT_SETUP_CONTEXT_INTERFACE.md
