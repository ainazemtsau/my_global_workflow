# Workflow v3 Project Files Manifest Template

status: active_skeleton_namespace_corrected

## Purpose

This is a template for future Project Files/Sources manifests. It is template only in this slice and does not update any actual ChatGPT Project.

## Manifest metadata

```text
project_name:
project_type:
direction_id_if_any:
repository:
ref:
manifest_status:
last_refresh:
```

## Project Instructions UI source

Name the source file for the Project Instructions UI payload.

```text
project_instruction_ui_source:
payload_markers:
payload_char_count:
update_required:
```

Instruction sources are not default Project Files/Sources unless a later explicit setup package says otherwise.

## Default Project Files/Sources

List cache/context files uploaded by default for the future Project.

```text
default_project_files_sources:
  - path:
    source_ref:
    purpose:
    cache_warning: Project Files/Sources are cache/context only.
```

For ordinary v3 Direction Projects, default sources may include future shared packs and selected current-state Direction runtime files after adoption.

Exclude old Direction files from default v3 Project Files/Sources.

## Request-only sources

List sources loaded only when the admitted task depends on them.

```text
request_only_sources:
  - path:
    source_ref:
    load_when:
    reason:
```

Examples: exact node files, contracts, run records, result packets, evidence, acceptance decisions, archives, raw logs, candidate docs for maintenance review, and old Direction files used as legacy_evidence.

## Do-not-upload sources

List files that must not be uploaded as Project Files/Sources for this manifest.

```text
do_not_upload_sources:
  - path:
    reason:
```

By default in this repository completion framework, all `workflow_v3/**` files are do-not-upload sources until a later explicit Project setup rollout/adoption package says otherwise.

At minimum, list these as do-not-upload:

```text
workflow_v3/control_plane/**
workflow_v3/interfaces/**
workflow_v3/templates/**
workflow_v3/completion/**
workflow_v3/adoption/**
workflow_v3/procedures/**
workflow_v3/QUALITY_AND_RECOVERY.md
workflow_v3/project_setup/*PROJECT_INSTRUCTIONS*.md
```

## Refresh requirements

Report refresh requirements separately.

```text
project_instruction_ui_update_required:
project_sources_files_refresh_required:
request_only_sources_refresh_required:
do_not_upload_as_project_file:
```

Repository commits do not update ChatGPT Projects by themselves.

## Validation checklist

```text
[ ] Exact repository ref/path listed.
[ ] Project Instructions UI source named and payload count measured.
[ ] Default Project Files/Sources are cache/context only.
[ ] Request-only sources have load conditions.
[ ] Old Direction files are excluded from default v3 Project Files/Sources.
[ ] Do-not-upload sources are listed.
[ ] Refresh categories are separated.
[ ] Owner quality/check source docs are used instead of Project Files/Sources as authority.
[ ] No actual Project update is implied by this manifest.
```

END_OF_FILE: workflow_v3/project_setup/PROJECT_FILES_MANIFEST_TEMPLATE.md
