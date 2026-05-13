# 02 Stage Result Packet Template
Status: draft Workflow version: vNext-R REBUILD Installed from roadmap step: Step 3 — Transport Templates Installed at: 2026-05-07T15:25:01.4848571+03:00 Source input: ChatGPT Step 3 result generated 2026-05-07 Authority: GitHub repository canonical after file read-back / diff verification / commit verification Activation scope: rebuild root only Freshness: fresh Supersedes: Superseded by:

# 02 Stage Result Packet Template

## Transport authority boundary — AD-WF-RT-001

This transport template is not independent routing authority.

Until transport files are converted to canonical `workflow_packet: 1` / `schema: *.v1` packet shapes, `workflow/runtime/WF_VNEXT_R_RUNTIME_CORE.md` remains the packet schema authority.

Any route fields in this file, including `allowed_next_stage_ids`, are snapshots only.

They must not override:

```text
workflow/stage_registry/STAGE_REGISTRY.md
```

If a transport packet route snapshot conflicts with the registry, return route-conflict Context Request / B1_PROBLEM / Human Decision / Stop.

## Purpose

A Stage Result Packet is the controlled output packet from a stage.

It records what the stage produced, what changed, what evidence supports the result, and what route is allowed next. It prevents silent handoff drift.

This is a transport template only. It is not a final stage prompt.

## Transport invariants

*   HTML is forbidden as transport.
*   Use plain Markdown with YAML-style fields.
*   Unknown extension handling: consumers must tolerant-read unknown fields under `extensions`; producers must not make unknown extensions mandatory for correct execution.
*   The result packet must not depend on private chain-of-thought.
*   Any write request must be expressed through an explicit Repository Patch Template.
*   A stage may stop, request context, request a human decision, emit a patch, or launch a next stage, but it must state which route it selected.

## Required fields

*   `stage_result_packet`
*   `packet_type`
*   `workflow_version`
*   `created_at`
*   `source_stage`
*   `input_launch_card_ref`
*   `status`
*   `human_summary`
*   `outputs`
*   `state_observations`
*   `decisions`
*   `evidence`
*   `write_requests`
*   `execution_log_entry`
*   `next_route`
*   `downstream_usage`
*   `extensions`

## Template

```
stage_result_packet: 1
packet_type: stage_result
workflow_version: vNext-R REBUILD
created_at: YYYY-MM-DDTHH:MM:SS±HH:MM
created_by: ChatGPT

source_stage:
  stage_id:
  stage_name:
  stage_prompt_version:
  stage_prompt_path:

input_launch_card_ref:
  launch_card_id:
  source_stage_id:
  received_at:
  required_fields_present: true | false
  missing_required_fields:
    - field:

status:
  outcome: completed | partial | blocked | stopped | failed
  confidence: high | medium | low
  blocker_summary:
  safe_to_continue: true | false

human_summary:
  concise_result:
  material_changes:
    - change:
  important_warnings:
    - warning:

outputs:
  primary_output:
    name:
    type:
    content_or_pointer:
  secondary_outputs:
    - name:
      type:
      content_or_pointer:
  rejected_outputs:
    - item:
      reason:

state_observations:
  direction_id:
  phase_id:
  goal_id:
  task_id:
  repository_state_refs:
    - path:
      observed_status:
      freshness:
  project_file_state:
    - file:
      observed_status:
      freshness:

decisions:
  decisions_made:
    - decision:
      rationale:
      reversibility: reversible | difficult | irreversible
  decisions_needed:
    - decision:
      blocking: true | false
      suggested_human_decision_card_ref:

evidence:
  sources_used:
    - source:
      type: user_input | repository | project_file | web | codex | calculation | other
      freshness: fresh | stale | unknown
  validation_performed:
    - check:
      result: pass | fail | not_applicable
  validation_gaps:
    - gap:

write_requests:
  repository_patch_required: true | false
  repository_patch_ref:
  changed_files_context_refresh_required: true | false
  changed_files_context_refresh_summary:
  no_write_reason:

execution_log_entry:
  required: true
  execution_log_entry_ref:
  inline_entry:

next_route:
  selected_route: launch_next_stage | context_request | human_decision | repository_patch | recovery_close | stop
  next_launch_card_ref:
  context_request_card_ref:
  human_decision_card_ref:
  recovery_close_packet_ref:
  stop_reason:
  allowed_next_stage_ids:
    - stage_id:
  forbidden_next_stage_ids:
    - stage_id:
      reason:

downstream_usage:
  consumed_by:
    - ChatGPT runtime router
    - next selected stage
    - GitHub repository documentation maintenance gate
    - human validation
  expected_next_artifact:
    - depends on selected_route
  validation_notes:
    - Runtime router must not infer missing next route.
    - Consumers may ignore unknown extension fields.

extensions: {}

```

## Downstream usage

The Stage Result Packet is consumed by the runtime router, documentation maintenance gate, next selected stage, and human validation flow. It is the main public handoff artifact after a stage run.

## Validation anchors

*   `stage_result_packet: 1`
*   `HTML is forbidden as transport.`
*   `Unknown extension handling`
*   `selected_route`
*   `downstream_usage`
