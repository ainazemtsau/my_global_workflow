# Workflow v3 ChatGPT Project Creation Guide

status: active_skeleton_namespace_corrected

## Purpose

This guide describes future ChatGPT Project creation for Workflow v3. It does not create or update any ChatGPT Project by this repository commit.

## Future Project creation

Future Project creation requires a separate rollout/adoption package that states:

- Project type;
- source authority;
- Project Instructions UI payload source;
- Project Files/Sources manifest;
- request-only sources;
- do-not-upload sources;
- refresh requirements;
- validation evidence.

Use `workflow_v3/runbooks/PROJECT_SETUP_ROLLOUT_RUNBOOK.md` and `workflow_v3/evals/PROJECT_SETUP_ROLLOUT_EVAL.md` for future rollout preparation and verification.

Repository commits alone do not update ChatGPT Project UI or files.

## Refresh reporting

Every future Project setup package must report these fields separately:

- `project_instruction_ui_update_required`;
- `project_sources_files_refresh_required`;
- `request_only_sources_refresh_required`;
- `do_not_upload_as_project_file`.

## Recommended names

Recommended user-facing ChatGPT Project names:

- `Workflow v3 — <Direction Name>`
- `Workflow v3 — Sandbox`
- `Workflow v3 — Rollout Test`
- `Workflow v3 Governance — Maintenance Console`

Do not use user-facing Project names containing "Pilot".

## Ordinary Direction Project

An ordinary Workflow v3 Direction Project is for one adopted Direction only. It uses compact universal Direction Project Instructions plus selected cache/context files after a later adoption package.

It does not import old Direction files by default and does not treat Project Files/Sources as truth.

## Governance Maintenance Console

The Governance Maintenance Console is for repository governance, setup maintenance, audits, repair design, Codex handoffs, and Codex result verification.

It does not run Direction runtime by default and does not mutate Direction accepted state.

## Current slice boundary

No Projects are created or updated by this repository commit.

No current Project Files/Sources refresh is required by this slice.

END_OF_FILE: workflow_v3/project_setup/CHATGPT_PROJECT_CREATION_GUIDE.md
