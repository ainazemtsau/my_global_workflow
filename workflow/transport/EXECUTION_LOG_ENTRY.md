# Execution Log Entry Transport Template

```yaml
artifact_control:
  artifact_name: "Execution Log Entry Transport Template"
  schema: transport_template.v1
  owner_layer: transport
  status: canonical
  repo_path: "workflow/transport/EXECUTION_LOG_ENTRY.md"
  runtime_schema: execution_log_entry.v1
  last_updated: "2026-05-13"
```

## Purpose

Defines the canonical transport template for recording observable workflow events.

Execution logs record inputs, outputs, validation, decisions, write requests, and next route without exposing private reasoning.

## Transport authority boundary — AD-WF-RT-001

This template is not routing authority. Route fields are snapshots only.

## Transport invariants

- HTML is forbidden as transport.
- Use plain Markdown with YAML-style fields.
- Unknown extension fields must be tolerated by consumers.
- Log observable facts and public rationale, not private chain-of-thought.
- Every meaningful workflow event should include an Execution Log Entry.
- If `persist: true`, the matching repository patch must include the log write.

## Canonical packet template

```yaml
execution_log_entry:
  schema: execution_log_entry.v1
  persist: true | false
  target_log_path:
  event_type: router_decision | stage_run | codex_return | problem | review | install | context_request | human_decision | recovery | other
  timestamp:
  direction:
    name:
    path:
  phase:
    name:
    path:
    status:
  goal:
    title:
    path:
    status:
  stage:
    id:
    name:
  route:
  return_state: DONE | NEEDS_INPUT | STUCK | PARTIAL | NOT_APPLICABLE
  input_sources:
    - source:
      freshness:
  outputs_created:
    -
  decisions_made:
    -
  repository_patch:
    required: true | false
    summary:
  changed_files_context_refresh:
    required: true | false
    files:
      -
  evidence_pointers:
    -
  friction:
    -
  human_burden:
    level: H0 | H1 | H2 | H3
    notes:
  ai_failure_mode:
    -
  blocker:
    -
  next_route:
  next_launch_card_created: true | false
  notes:

extensions: {}
```

## Validation anchors

- `schema: execution_log_entry.v1`
- `persist`
- `target_log_path`
- `event_type`
- `return_state`

## End-of-file marker

`END_OF_FILE: workflow/transport/EXECUTION_LOG_ENTRY.md`
