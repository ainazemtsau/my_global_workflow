# Codex Return Transport Template

```yaml
artifact_control:
  artifact_name: "Codex Return Transport Template"
  schema: transport_template.v1
  owner_layer: transport
  status: canonical
  repo_path: "workflow/transport/CODEX_RETURN_PACKET.md"
  runtime_schema: codex_return.v1
  last_updated: "2026-05-13"
```

## Purpose

Defines the canonical transport template for Codex return evidence.

Codex cannot claim DONE without evidence. If writes occurred, Codex must include file read-back / diff verification / commit verification or equivalent verification.

## Transport authority boundary — AD-WF-RT-001

This template is not routing authority. It returns evidence to the requesting ChatGPT stage/thread for validation.

## Transport invariants

- HTML is forbidden as transport.
- Use plain Markdown with YAML-style fields.
- Unknown extension fields must be tolerated by consumers.
- If Codex lacks access, it must return NEEDS_INPUT or STUCK, not DONE.
- If no files changed, say so explicitly.
- If cached Project Files changed, report manual refresh requirements.

## Canonical packet template

```yaml
workflow_packet: 1
type: codex_return
schema: codex_return.v1

final_state: DONE | NEEDS_INPUT | STUCK | PARTIAL | FAILED

repository:
  name:
  branch:
  commit_sha:

actions_taken:
  - action:

files_changed:
  - path:
    action:
    readback_status: pass | fail | not_applicable

validation:
  commands_run:
    - command:
      exit_code:
      summary:
  checks:
    - check:
      result: pass | fail | not_applicable

evidence:
  diff_verification:
    required: true | false
    result:
  read_back_anchors:
    - file_path:
      anchors_found:
        - text:
  commit_verification:
    required: true | false
    result:

project_files_cache_refresh_required: true | false
target_chatgpt_project:
manual_refresh_required: true | false
blocking_before_next_material_run: true | false
changed_cached_files:
  - repository_path:
    project_file_cache_name:
    refresh_reason:
    blocking_before_next_material_run: true | false
manual_action:

problems_or_blockers:
  - blocker:

rollback_or_recovery:
  rollback_needed: true | false
  rollback_available: true | false
  notes:

next_route:
  recommended_route: return_to_chatgpt_validation | request_user_input | rerun_wave | recovery_close | stop
  next_owner: ChatGPT | Codex | human
  next_instruction:

extensions: {}
```

## Validation anchors

- `workflow_packet: 1`
- `schema: codex_return.v1`
- `final_state`
- `evidence`
- `project_files_cache_refresh_required`

## End-of-file marker

`END_OF_FILE: workflow/transport/CODEX_RETURN_PACKET.md`
