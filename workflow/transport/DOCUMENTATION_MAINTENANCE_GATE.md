# Documentation Maintenance Gate Transport Template

```yaml
artifact_control:
  artifact_name: "Documentation Maintenance Gate Transport Template"
  schema: transport_template.v1
  owner_layer: transport
  status: canonical
  repo_path: "workflow/transport/DOCUMENTATION_MAINTENANCE_GATE.md"
  runtime_schema: documentation_maintenance_gate.v1
  last_updated: "2026-05-13"
```

## Purpose

Defines the canonical transport template for deciding whether documentation maintenance is required.

Use this when workflow/model changes, durable Direction changes, Goal Review, Phase Close, context loading changes, documentation updates, or stale material discovery require maintenance review.

## Transport authority boundary — AD-WF-RT-001

This template is not routing authority and must not override runtime routing or registry transitions.

## Transport invariants

- HTML is forbidden as transport.
- Use plain Markdown with YAML-style fields.
- Unknown extension fields must be tolerated by consumers.
- Distinguish proposed documentation changes from applied documentation changes.
- Do not claim documentation was updated without read-back / diff verification / commit verification.
- Context refresh must name exact files.

## Canonical packet template

```yaml
documentation_maintenance_gate:
  required: true | false
  reason:

stable_docs_checked:
  - 01 Direction State
  - 02 Current Phase
  - 03 Focus Register
  - 04 Active Goal
  - 05 Portfolio Queue
  - 06_CONTEXT_LIBRARY_INDEX.md
  - relevant Knowledge / Canon / domain docs

updates:
  - file_path:
    action: replace_section | append_delta | mark_stale | split | merge | archive_pointer
    reason:

stale_or_superseded:
  - file_path:
    reason:
    replacement_pointer:

knowledge_updates:
  - target_file:
    summary:

canon_candidates:
  - target_file:
    summary:

context_loading_index_updates:
  - summary:

project_files_to_refresh:
  - file:
    reason:

extensions: {}
```

## Validation anchors

- `documentation_maintenance_gate`
- `stable_docs_checked`
- `updates`
- `stale_or_superseded`
- `project_files_to_refresh`

## End-of-file marker

`END_OF_FILE: workflow/transport/DOCUMENTATION_MAINTENANCE_GATE.md`
