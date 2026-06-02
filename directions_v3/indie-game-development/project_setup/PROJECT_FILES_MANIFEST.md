# Project Files Manifest — indie-game-development

project_name: Indie Game Development V3
project_type: ordinary_direction_project
direction_id: indie-game-development
repository: ainazemtsau/my_global_workflow
ref: main@32e436dcb43c0cc063ce64023e512444c926312e
manifest_status: candidate_setup_manifest
last_refresh: none

project_instruction_ui_source: directions_v3/indie-game-development/project_setup/CHATGPT_PROJECT_INSTRUCTIONS.md
project_instruction_ui_payload_markers: BEGIN_CHATGPT_PROJECT_INSTRUCTIONS_UI_PAYLOAD / END_CHATGPT_PROJECT_INSTRUCTIONS_UI_PAYLOAD
project_instruction_ui_payload_char_count: see CHATGPT_PROJECT_INSTRUCTIONS.md
runtime_binding_source: directions_v3/indie-game-development/runtime/config/DIRECTION_PROJECT_BINDING.md

## Source authority

Project Files/Sources are cache/context only.

Exact repository files at named repo/path/ref remain source authority.

If Project Files/Sources conflict with exact repository source, exact repository source wins.

## Default Project Files/Sources decision

default_project_files_sources: none

Rationale:
- The Project Instructions UI binding capsule plus exact repository reads are the default continuation mechanism.
- Project Files/Sources do not prove latest repository state.
- Project Files/Sources cannot override canonical runtime binding or runtime state files.

## Optional binding file cache

optional_project_file_cache: not_used_in_this_package

If a later explicit rollout uploads the binding file as Project File cache, it remains cache/context only and must be listed in a future manifest update.

## Runtime state file upload policy

Runtime state files are not uploaded by default unless a later explicit rollout says otherwise.

Default do not upload:
- directions_v3/indie-game-development/runtime/state/CURRENT_STATUS.md
- directions_v3/indie-game-development/runtime/state/CURRENT_NEXT_MOVE.md
- directions_v3/indie-game-development/runtime/state/DIRECTION_SPINE.md
- directions_v3/indie-game-development/runtime/state/DIRECTION_MAP.md
- directions_v3/indie-game-development/runtime/state/ACTIVE_FRONT.md
- directions_v3/indie-game-development/runtime/fronts/**
- directions_v3/indie-game-development/runtime/records/**
- directions_v3/indie-game-development/runtime/operations/**
- directions_v3/indie-game-development/runtime/memory/**

## Workflow source upload policy

workflow_v3/** source docs are not uploaded by default.

Use exact repository reads for source authority and request-only loading for bounded tasks.

## Request-only sources

request_only_sources:
- workflow_v3/interfaces/**
- workflow_v3/templates/**
- workflow_v3/adoption/**
- workflow_v3/runbooks/**
- workflow_v3/evals/**
- workflow_v3/completion/**
- workflow_v3/formation/**
- directions_v3/indie-game-development/runtime/records/**
- directions_v3/indie-game-development/runtime/fronts/**
- directions_v3/indie-game-development/runtime/operations/**

## Do-not-upload list

do_not_upload_as_project_file:
- workflow_v3/project_setup/*PROJECT_INSTRUCTIONS*.md
- workflow_v3/interfaces/**
- workflow_v3/templates/**
- workflow_v3/completion/**
- workflow_v3/adoption/**
- workflow_v3/runbooks/**
- workflow_v3/evals/**
- workflow_v3/formation/**
- directions_v3/indie-game-development/project_setup/CHATGPT_PROJECT_INSTRUCTIONS.md

## Refresh fields

project_instruction_ui_update_required: true after package acceptance/merge; manual UI update only
project_sources_files_refresh_required: false
request_only_sources_refresh_required: false
do_not_upload_as_project_file: workflow_v3/** source docs and directions_v3/indie-game-development/project_setup/CHATGPT_PROJECT_INSTRUCTIONS.md
last_refresh_ref: none
refresh_reason: setup-only root bootstrap source generation
refresh_limitations: no Project Files/Sources refresh performed by this package
