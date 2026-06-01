# Universal Direction Project Files Manifest Template

status: template_only

## Purpose

This template records future ordinary Workflow v3 Direction Project Files/Sources decisions.

It is a template only. It does not refresh Project Files/Sources, update Project Instructions UI, adopt a Direction, or create runtime state.

## Source authority

Project Files/Sources are cache/context only.

Exact GitHub/repository files at a named repo/path/ref remain source authority.

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
project_instruction_ui_source:
project_instruction_ui_payload_markers:
project_instruction_ui_payload_char_count:
```

## Default upload recommendation for v3

- Do not upload `workflow_v3/**` source docs by default unless a later explicit rollout says otherwise.
- Do not use old `workflow/**` as v3 authority.
- Do not use old `directions/**` as accepted v3 state.
- Do not upload old Direction files as default Project Files/Sources.
- Use exact GitHub/repository source reads when material state, setup, or adoption decisions depend on exact source.

## Default Project Files/Sources

```text
default_project_files_sources:
  - path:
    source_ref:
    purpose:
    cache_warning: Project Files/Sources are cache/context only.
```

For a newly created ordinary Direction Project before runtime root creation, the default recommendation is no default uploaded `workflow_v3/**` source docs.

Future Direction runtime payload files may be considered only after explicit runtime root creation under `directions_v3/<direction-id>/runtime/**`.

## Request-only sources

```text
request_only_sources:
  - workflow_v3/interfaces/**
  - workflow_v3/templates/**
  - workflow_v3/adoption/**
  - workflow_v3/runbooks/**
  - workflow_v3/evals/**
  - workflow_v3/completion/**
```

Load request-only sources only when a bounded task needs the exact source.

## Do-not-upload list

```text
workflow_v3/project_setup/*PROJECT_INSTRUCTIONS*.md
workflow_v3/interfaces/**
workflow_v3/templates/**
workflow_v3/completion/**
workflow_v3/adoption/**
workflow_v3/runbooks/**
workflow_v3/evals/**
```

## Future Direction runtime payload

Future Direction runtime payload becomes eligible for Project Files/Sources consideration only after an explicit accepted package creates:

```text
directions_v3/<direction-id>/runtime/**
```

Before that root exists, do not invent or upload concrete Direction runtime state.

## Refresh requirements

```text
project_instruction_ui_update_required:
project_sources_files_refresh_required:
request_only_sources_refresh_required:
do_not_upload_as_project_file:
```

END_OF_FILE: workflow_v3/project_setup/UNIVERSAL_DIRECTION_PROJECT_FILES_MANIFEST_TEMPLATE.md
