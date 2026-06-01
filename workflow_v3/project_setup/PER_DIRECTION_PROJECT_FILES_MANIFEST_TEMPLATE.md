# Per-Direction Project Files Manifest Template

status: template_only

## Boundary

This template is for a future concrete ordinary Direction Project Files/Sources manifest.

Future concrete target path:

```text
directions_v3/<direction-id>/project_setup/PROJECT_FILES_MANIFEST.md
```

This template does not create a concrete Direction file, refresh Project Files/Sources, update Project Instructions UI, or create runtime state.

## Source authority

Project Files/Sources are cache/context only.

Exact repository files at named repo/path/ref remain source authority.

If Project Files/Sources conflict with exact repository source, the exact repository source wins.

## Manifest fields

```text
project_name:
project_type: ordinary_direction_project
direction_id:
repository:
ref:
manifest_status:
last_refresh:
project_instruction_ui_source: directions_v3/<direction-id>/project_setup/CHATGPT_PROJECT_INSTRUCTIONS.md
project_instruction_ui_payload_markers: BEGIN_CHATGPT_PROJECT_INSTRUCTIONS_UI_PAYLOAD / END_CHATGPT_PROJECT_INSTRUCTIONS_UI_PAYLOAD
project_instruction_ui_payload_char_count:
runtime_binding_source: directions_v3/<direction-id>/runtime/config/DIRECTION_PROJECT_BINDING.md
```

## Default Project Files/Sources decision

Default:

```text
default_project_files_sources: none
```

Rationale:

- The Project Instructions UI binding capsule plus exact repository reads are the default continuation mechanism.
- Project Files/Sources do not prove latest repository state.
- Project Files/Sources cannot override canonical runtime binding or runtime state files.

## Optional binding file cache

Optional after concrete runtime root creation:

```text
optional_project_file_cache:
  - path: directions_v3/<direction-id>/runtime/config/DIRECTION_PROJECT_BINDING.md
    source_ref:
    purpose: Small binding locator cache for the Project.
    cache_warning: Cache/context only; exact repository runtime binding source wins.
```

If used, the optional binding cache may require `project_sources_files_refresh_required: true` for that future Project action only.

## Runtime state file upload policy

Runtime state files are not uploaded by default unless a later explicit rollout says otherwise.

Default do not upload:

```text
directions_v3/<direction-id>/runtime/state/CURRENT_STATUS.md
directions_v3/<direction-id>/runtime/state/CURRENT_NEXT_MOVE.md
directions_v3/<direction-id>/runtime/state/DIRECTION_SPINE.md
directions_v3/<direction-id>/runtime/state/DIRECTION_MAP.md
directions_v3/<direction-id>/runtime/state/ACTIVE_FRONT.md
directions_v3/<direction-id>/runtime/fronts/**
directions_v3/<direction-id>/runtime/records/**
directions_v3/<direction-id>/runtime/operations/**
directions_v3/<direction-id>/runtime/memory/**
```

## Workflow source upload policy

`workflow_v3/**` source docs are not uploaded by default.

Use exact repository reads for source authority and request-only loading for bounded tasks.

## Request-only sources

```text
request_only_sources:
  - workflow_v3/interfaces/**
  - workflow_v3/templates/**
  - workflow_v3/adoption/**
  - workflow_v3/runbooks/**
  - workflow_v3/evals/**
  - workflow_v3/completion/**
  - workflow_v3/formation/**
  - directions_v3/<direction-id>/runtime/records/**
  - directions_v3/<direction-id>/runtime/fronts/**
  - directions_v3/<direction-id>/runtime/operations/**
```

## Do-not-upload list

```text
workflow_v3/project_setup/*PROJECT_INSTRUCTIONS*.md
workflow_v3/interfaces/**
workflow_v3/templates/**
workflow_v3/completion/**
workflow_v3/adoption/**
workflow_v3/runbooks/**
workflow_v3/evals/**
workflow_v3/formation/**
directions_v3/<direction-id>/project_setup/CHATGPT_PROJECT_INSTRUCTIONS.md
```

## Refresh fields

```text
project_instruction_ui_update_required:
project_sources_files_refresh_required:
request_only_sources_refresh_required:
do_not_upload_as_project_file:
last_refresh_ref:
refresh_reason:
refresh_limitations:
```

END_OF_FILE: workflow_v3/project_setup/PER_DIRECTION_PROJECT_FILES_MANIFEST_TEMPLATE.md
