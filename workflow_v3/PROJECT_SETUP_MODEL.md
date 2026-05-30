# Workflow v3 Project Setup Model

status: active_skeleton_namespace_corrected

## Purpose

This file defines the future ChatGPT Project setup model for Workflow v3. It does not update actual ChatGPT Projects in this slice.

## Project Instructions UI role

Project Instructions UI is a compact behavior bootstrap. It should state:

- source authority rules;
- context classification;
- Launch Packet and Result Packet requirements;
- exact Next Move requirement;
- no hidden accepted state;
- no migration/import by default;
- Runtime Console read-only boundary.

Project Instructions UI is not long documentation, not accepted Direction state, and not default Project Files/Sources.

## Project Files/Sources role

Project Files/Sources are cache/context only. They may help orientation and repeated context access, but they do not prove latest repository state, acceptance, successful implementation, runtime activation, or Direction adoption.

If Project Files/Sources conflict with exact repository files at a known ref/path, the exact repository read wins.

## Request-only sources

Request-only sources are loaded only when a Launch Packet, Check Job, Codex package, review, or human decision needs them.

Examples include exact node workspaces, Work Contract records, Run records, Result Packets, Evidence records, Acceptance Decisions, Memory Artifacts beyond indexes, raw run logs, archives, old Direction files used as legacy_evidence, and candidate docs used for maintenance review.

## Future Project types

Future Workflow v3 Project types:

- Workflow v3 Direction Project - one ordinary Project for one adopted Direction.
- Workflow v3 Governance - Maintenance Console - a repository governance/setup maintenance Project.

Ordinary Direction Projects must not become governance consoles. The Governance Maintenance Console must not run Direction runtime by default.

## Refresh categories

Project setup reporting uses these categories:

- `project_instruction_ui_update_required`;
- `project_sources_files_refresh_required`;
- `request_only_sources_refresh_required`;
- `do_not_upload_as_project_file`.

## Current slice refresh status

This slice does not update actual ChatGPT Projects.

For this slice:

- `project_instruction_ui_update_required`: no actual ChatGPT Project UI update;
- `project_sources_files_refresh_required`: no current Project Files/Sources refresh;
- `request_only_sources_refresh_required`: no request-only source refresh;
- `do_not_upload_as_project_file`: all `workflow_v3/**` files until a later explicit Project setup rollout/adoption package says otherwise.

END_OF_FILE: workflow_v3/PROJECT_SETUP_MODEL.md
