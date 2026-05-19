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
- When a file defines an `END_OF_FILE` marker, append operations must insert before that marker and preserve it as the final non-whitespace content.
- A lifecycle-state-changing patch must include `lifecycle_state_reconciliation` or explicitly state why it is not required.

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

structural_integrity:
  eof_marker_policy:
    required_for_changed_files_with_eof: true
    expected_marker_count: exactly_one
    marker_must_be_last_non_whitespace: true
  append_policy:
    if_target_has_eof_marker: insert_before_eof_marker
    must_not_append_below_eof: true

lifecycle_state_reconciliation:
  required: true | false
  reason:
  expected_policy: update_runtime_state_files | stale_but_nonblocking_override_for_named_next_stage | context_request_for_state_reconciliation | not_required

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
