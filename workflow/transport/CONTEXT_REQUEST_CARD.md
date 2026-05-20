# Context Request Transport Template

```yaml
artifact_control:
  artifact_name: "Context Request Transport Template"
  schema: transport_template.v1
  owner_layer: transport
  status: canonical
  repo_path: "workflow/transport/CONTEXT_REQUEST_CARD.md"
  runtime_schema: context_request.v1
  last_updated: "2026-05-13"
```

## Purpose

Defines the canonical transport template for requesting missing context.

Use this when required context is unavailable, stale, contradictory, or too ambiguous for safe material work.

## Transport authority boundary — AD-WF-RT-001

This template is not routing authority. Route fields are snapshots only.

The registry remains authoritative for stage IDs and normal stage-to-stage routing.

## Transport invariants

- HTML is forbidden as transport.
- Use plain Markdown with YAML-style fields.
- Unknown extension fields must be tolerated by consumers.
- Ask only for context that blocks safe progress.
- For exact repository context or exact stage prompt context, include `acquisition_audit`.
- Do not infer missing file content from memory, old chats, search snippets, or partial GitHub output.
- If safe partial progress exists, identify it explicitly.
- Context Request for exact repository context is invalid unless `acquisition_audit` documents that GitHub connector/tool acquisition was attempted, unavailable/not exposed, failed, unverified, skipped for a stated reason, or unsafe.

## Canonical packet template

```yaml
workflow_packet: 1
type: context_request
schema: context_request.v1
reason:
blocking: true | false

requested_context:
  - kind: project_file | repository_file_export | stage_prompt | codex_return | evidence | user_decision | other
    title:
    repository_path:
    file_name_suggested:
    why_needed:
    required: true | false
    freshness_required: fresh | any | latest_available

acquisition_audit:
  - repository_path:
    required_for:
    project_files:
      status:
    attachments:
      status:
    github_connector:
      available: true | false
      attempted: true | false
      method:
      result:
      source_ref:
      sha:
      line_count:
      byte_count:
      tail_or_eof_verified: true | false
      reason_if_skipped:
    codex_local_export:
      attempted: true | false
      result:
      reason:
    user_manual_export:
      requested: true | false
      reason:
    blocker:

current_state:
  direction:
  phase:
  goal:
  route_attempted:

after_provided:
  action: continue_current_stage | run_stage | regenerate_launch_card | recheck_state
  stage_id:
  expected_next_output:

instructions_for_user:
  - exact thing to paste/export/upload

extensions: {}
```

## Validation anchors

- `workflow_packet: 1`
- `schema: context_request.v1`
- `requested_context`
- `acquisition_audit`
- `blocking`
- `instructions_for_user`

## End-of-file marker

`END_OF_FILE: workflow/transport/CONTEXT_REQUEST_CARD.md`
