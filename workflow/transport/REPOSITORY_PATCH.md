# Repository Patch Transport Template

```yaml
artifact_control:
  artifact_name: "Repository Patch Transport Template"
  schema: transport_template.v1
  owner_layer: transport
  status: canonical
  repo_path: "workflow/transport/REPOSITORY_PATCH.md"
  runtime_schema: repository_patch.v1
  last_updated: "2026-05-13"
```

## Purpose

Defines the canonical transport template for proposed GitHub repository changes.

ChatGPT creates repository patches. Codex or the user applies them. Updates are canonical only after write plus file read-back / diff verification / commit verification.

## Transport authority boundary — AD-WF-RT-001

This template is not routing authority. It must not alter stage IDs, registry transitions, or runtime routing rules.

## Transport invariants

- HTML is forbidden as transport.
- Use plain Markdown with YAML-style fields.
- Unknown extension fields must be tolerated by consumers.
- Do not physically delete files unless explicitly approved.
- Prefer scoped operations over vague append behavior.
- All content-bearing writes must include validation anchors.
- No writes outside named paths.
- Do not claim repository updates are complete without read-back / diff verification / commit verification.

## Canonical packet template

```yaml
workflow_packet: 1
type: repository_patch
schema: repository_patch.v1

patch_id:
created_by_stage:
return_state:

operations:
  - action: create_file | replace_file | replace_section | append_section | mark_stale | update_header
    file_path:
    title:
    section:
    content:
    reason:
    safety:
      destructive: false
      requires_human_approval: false

readback_required:
  - file_path:
    expected_anchor:
    expected_header:

changed_files_context_refresh:
  - source_file:
    project_file:
    reason:

extensions: {}
```

## Validation anchors

- `workflow_packet: 1`
- `schema: repository_patch.v1`
- `operations`
- `readback_required`
- `changed_files_context_refresh`

## End-of-file marker

`END_OF_FILE: workflow/transport/REPOSITORY_PATCH.md`
