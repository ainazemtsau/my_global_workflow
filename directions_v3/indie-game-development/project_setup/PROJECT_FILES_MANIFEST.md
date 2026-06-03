# Project Files Manifest

project_name: Indie Game Development
project_type: ordinary_direction_project
direction_id_if_any: indie-game-development
repository: ainazemtsau/my_global_workflow
ref: b3f7102005c91f72ecc608cb7e8bae3de13f2f69
manifest_status: accepted_setup_only_manifest
last_refresh: pending_manual_project_setup

## Project Instructions UI source

```text
project_instruction_ui_source: directions_v3/indie-game-development/project_setup/CHATGPT_PROJECT_INSTRUCTIONS.md
payload_markers: BEGIN_CHATGPT_PROJECT_INSTRUCTIONS_UI_PAYLOAD / END_CHATGPT_PROJECT_INSTRUCTIONS_UI_PAYLOAD
payload_char_count: 3604
update_required: true
````

Instruction sources are not default Project Files/Sources.

## Default Project Files/Sources

```text
default_project_files_sources: none
```

Project Files/Sources are cache/context only and cannot override exact repository source.

## Optional Project Files/Sources after accepted root exists

```text
optional_project_files_sources:
  - path: directions_v3/indie-game-development/runtime/config/DIRECTION_PROJECT_BINDING.md
    source_ref: accepted setup-only root commit
    purpose: small binding cache only
    cache_warning: Project Files/Sources are cache/context only and cannot override exact repository runtime binding source.
```

## Request-only sources

```text
request_only_sources:
  - path: workflow_v3/control_plane/**
    source_ref: exact repository ref required by admitted task
    load_when: material admission or control-plane verification requires it
    reason: procedure authority, not default Project File cache

  - path: workflow_v3/runbooks/**
    source_ref: exact repository ref required by admitted task
    load_when: admitted runbook execution requires it
    reason: runbook authority, not default Project File cache

  - path: workflow_v3/templates/**
    source_ref: exact repository ref required by admitted task
    load_when: admitted package/template generation requires it
    reason: template authority, not default Project File cache

  - path: workflow_v3/project_setup/**
    source_ref: exact repository ref required by admitted task
    load_when: project setup, binding, or Direction Definition launch requires it
    reason: project setup authority, not default Project File cache

  - path: directions/indie-game-development/**
    source_ref: exact repository ref required by admitted legacy_evidence procedure
    load_when: only through a bounded admitted legacy_evidence procedure
    reason: old Direction files are legacy_evidence only, not accepted Workflow v3 state
```

## Do-not-upload sources

```text
do_not_upload_sources:
  - path: workflow_v3/**
    reason: workflow source docs are request-only operational sources by default, not Project File uploads

  - path: directions/**
    reason: old Direction files are not accepted Workflow v3 state and are excluded from default v3 Project Files/Sources

  - path: directions_v3/indie-game-development/project_setup/CHATGPT_PROJECT_INSTRUCTIONS.md
    reason: this is Project Instructions UI source, not a Project File upload by default
```

## Refresh requirements

```text
project_instruction_ui_update_required: true
project_sources_files_refresh_required: false
request_only_sources_refresh_required: false
do_not_upload_as_project_file: directions_v3/indie-game-development/project_setup/CHATGPT_PROJECT_INSTRUCTIONS.md
```

Repository commits do not update ChatGPT Projects by themselves.

## Validation checklist

```text
[x] Exact repository ref/path listed.
[x] Project Instructions UI source named and payload count measured.
[x] Default Project Files/Sources are cache/context only.
[x] Request-only sources have load conditions.
[x] Old Direction files are excluded from default v3 Project Files/Sources.
[x] Do-not-upload sources are listed.
[x] Refresh categories are separated.
[x] No actual Project update is implied by this manifest.
```

END_OF_FILE: directions_v3/indie-game-development/project_setup/PROJECT_FILES_MANIFEST.md
