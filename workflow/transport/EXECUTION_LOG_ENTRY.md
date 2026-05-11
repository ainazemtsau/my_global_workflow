# 06 Execution Log Entry Template
Status: draft Workflow version: vNext-R REBUILD Installed from roadmap step: Step 3 — Transport Templates Installed at: 2026-05-07T15:25:01.4848571+03:00 Source input: ChatGPT Step 3 result generated 2026-05-07 Authority: GitHub repository canonical after file read-back / diff verification / commit verification Activation scope: rebuild root only Freshness: fresh Supersedes: Superseded by:

# 06 Execution Log Entry Template

## Purpose

An Execution Log Entry records what happened during a workflow stage or controlled runtime operation.

It makes stage execution auditable without exposing private reasoning. It records inputs, outputs, validation, decisions, write requests, and next route.

This is a transport template only. It is not an install log and not a final stage prompt.

## Transport invariants

*   HTML is forbidden as transport.
*   Use plain Markdown with YAML-style fields.
*   Unknown extension handling: consumers must tolerant-read unknown fields under `extensions`; producers must not make unknown extensions mandatory for correct execution.
*   Log observable facts and public rationale, not private chain-of-thought.
*   Every stage result should either include or point to an Execution Log Entry.
*   Execution logs must name the associated launch card and result packet.

## Required fields

*   `execution_log_entry`
*   `entry_type`
*   `workflow_version`
*   `created_at`
*   `stage`
*   `input_refs`
*   `operation_summary`
*   `outputs`
*   `validation`
*   `decisions`
*   `write_activity`
*   `next_route`
*   `downstream_usage`
*   `extensions`

## Template

```
execution_log_entry: 1
entry_type: execution_log
workflow_version: vNext-R REBUILD
created_at: YYYY-MM-DDTHH:MM:SS±HH:MM
created_by: ChatGPT

stage:
  stage_id:
  stage_name:
  stage_prompt_version:
  stage_prompt_path:

input_refs:
  launch_card_ref:
  prior_result_packet_refs:
    - ref:
  repository_context_refs:
    - path:
      freshness:
  project_file_refs:
    - file:
      freshness:

operation_summary:
  user_visible_summary:
  objective:
  non_objectives:
    - item:
  route_taken:
  route_reason:

outputs:
  result_packet_ref:
  produced_artifacts:
    - name:
      type:
      pointer_or_inline_summary:
  rejected_or_deferred_items:
    - item:
      reason:

validation:
  checks_performed:
    - check:
      result: pass | fail | not_applicable
  evidence_refs:
    - ref:
  known_gaps:
    - gap:
  confidence: high | medium | low

decisions:
  decisions_made:
    - decision:
      public_rationale:
  decisions_deferred:
    - decision:
      reason:
      human_decision_card_ref:

write_activity:
  repository_patch_emitted: true | false
  repository_patch_ref:
  changed_files_context_refresh_required: true | false
  docs_maintenance_gate_ref:
  writes_applied_this_stage: none | proposed_only | applied_by_codex | applied_manually

next_route:
  selected_route:
  next_stage_id:
  next_launch_card_ref:
  stop_reason:
  recovery_close_packet_ref:

downstream_usage:
  consumed_by:
    - human audit
    - ChatGPT runtime router
    - GitHub repository documentation maintenance
    - future review/distill stages
  expected_next_artifact:
    - Stage Result Packet
    - Next Launch Card
    - Documentation Maintenance Gate
  validation_notes:
    - Log must be sufficient for audit without private reasoning.
    - Consumers may ignore unknown extension fields.

extensions: {}

```

## Downstream usage

The Execution Log Entry is consumed by human audit, the runtime router, documentation maintenance, and review/distill stages.

## Validation anchors

*   `execution_log_entry: 1`
*   `HTML is forbidden as transport.`
*   `Unknown extension handling`
*   `writes_applied_this_stage`
*   `downstream_usage`