# 07 Documentation Maintenance Gate Template
Status: draft Workflow version: vNext-R REBUILD Installed from roadmap step: Step 3 — Transport Templates Installed at: 2026-05-07T15:25:01.4848571+03:00 Source input: ChatGPT Step 3 result generated 2026-05-07 Authority: Trilium canonical after read-back Activation scope: rebuild root only Freshness: fresh Supersedes: Superseded by:

# 07 Documentation Maintenance Gate Template

## Purpose

A Documentation Maintenance Gate determines whether a stage result requires Trilium documentation updates, Project File refresh, stale marking, or no write action.

It prevents documentation drift by making maintenance a formal gate instead of an afterthought.

This is a transport template only. It is not a final stage prompt.

## Transport invariants

*   HTML is forbidden as transport.
*   Use plain Markdown with YAML-style fields.
*   Unknown extension handling: consumers must tolerant-read unknown fields under `extensions`; producers must not make unknown extensions mandatory for correct execution.
*   The gate must distinguish proposed documentation changes from applied documentation changes.
*   Do not overwrite active Workflow vNext.
*   Project File refresh must be explicit and must name exact file content or exact update block.

## Required fields

*   `documentation_maintenance_gate`
*   `gate_type`
*   `workflow_version`
*   `created_at`
*   `source_stage`
*   `change_summary`
*   `documentation_impact`
*   `trilium_patch`
*   `project_files_refresh`
*   `staleness_review`
*   `decision`
*   `downstream_usage`
*   `extensions`

## Template

```
documentation_maintenance_gate: 1
gate_type: documentation_maintenance
workflow_version: vNext-R REBUILD
created_at: YYYY-MM-DDTHH:MM:SS±HH:MM
created_by: ChatGPT

source_stage:
  stage_id:
  stage_name:
  result_packet_ref:
  execution_log_entry_ref:

change_summary:
  material_change_made: true | false
  summary:
  affected_concepts:
    - concept:
  affected_paths:
    - path:

documentation_impact:
  trilium_update_needed: true | false
  project_file_update_needed: true | false
  stale_marking_needed: true | false
  install_log_needed: true | false
  no_update_reason:

trilium_patch:
  required: true | false
  patch_ref:
  inline_patch:
  patch_scope:
    - path:
  human_approval_required_before_apply: true | false

project_files_refresh:
  required: true | false
  files:
    - file:
      action: replace_file | replace_section | no_action
      reason:
      content_update_summary:
      exact_update_block_ref:

staleness_review:
  notes_to_mark_stale:
    - path:
      reason:
      replacement_pointer:
  notes_confirmed_fresh:
    - path:
      reason:
  unknown_freshness:
    - path:
      required_followup:

decision:
  selected_gate_outcome: no_docs_change | emit_patch | request_human_decision | request_context | recovery_close | stop
  rationale:
  safe_to_continue_after_gate: true | false
  next_route:

downstream_usage:
  consumed_by:
    - ChatGPT runtime router
    - Codex installer
    - human manual checker
    - future review/distill stages
  expected_next_artifact:
    - Trilium Patch Template
    - Human Decision Card
    - Context Request Card
    - Stage Result Packet continuation
  validation_notes:
    - Gate must not claim documentation was updated unless read-back or explicit installation evidence exists.
    - Consumers may ignore unknown extension fields.

extensions: {}

```

## Downstream usage

The Documentation Maintenance Gate is consumed by the runtime router, Codex installer, human manual checker, and review/distill stages.

## Validation anchors

*   `documentation_maintenance_gate: 1`
*   `HTML is forbidden as transport.`
*   `Unknown extension handling`
*   `project_files_refresh`
*   `downstream_usage`