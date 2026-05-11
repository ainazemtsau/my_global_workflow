# 01 Stage Launch Card Template
Status: draft Workflow version: vNext-R REBUILD Installed from roadmap step: Step 3 — Transport Templates Installed at: 2026-05-07T15:25:01.4848571+03:00 Source input: ChatGPT Step 3 result generated 2026-05-07 Authority: GitHub repository canonical after file read-back / diff verification / commit verification Activation scope: rebuild root only Freshness: fresh Supersedes: Superseded by:

# 01 Stage Launch Card Template

## Purpose

A Stage Launch Card is the controlled input packet for starting a workflow stage or route.

It exists so a downstream stage can run from a clean public contract instead of relying on private reasoning, hidden context, or informal chat history.

This is a transport template only. It is not a final stage prompt.

## Transport invariants

*   HTML is forbidden as transport.
*   Use plain Markdown with YAML-style fields.
*   Required fields must remain readable as plain text.
*   Unknown extension handling: consumers must tolerant-read unknown fields under `extensions`; producers must not make unknown extensions mandatory for correct execution.
*   Do not embed private chain-of-thought, invisible scratchpad content, or unvalidated prior outputs.
*   GitHub repository paths must be exact when referenced.
*   Dates should use ISO-8601 when available.

## Required fields

*   `stage_launch_card`
*   `card_type`
*   `workflow_version`
*   `created_at`
*   `created_by`
*   `source`
*   `target`
*   `route`
*   `state`
*   `context`
*   `user_request`
*   `mission`
*   `inputs`
*   `constraints`
*   `freshness_and_boundaries`
*   `expected_output`
*   `downstream_usage`
*   `extensions`

## Template

```
stage_launch_card: 1
card_type: stage_launch
workflow_version: vNext-R REBUILD
created_at: YYYY-MM-DDTHH:MM:SS±HH:MM
created_by: ChatGPT

source:
  stage_id:
  stage_name:
  source_result_packet_ref:
  source_execution_log_ref:
  source_repository_file_refs:
    - path:
      required: true
      freshness: fresh | stale | unknown

target:
  stage_id:
  stage_name:
  stage_prompt_path:
  required_mode: draft | test-active | active-candidate | active

route:
  route_reason:
  allowed_next_stage_ids:
    - stage_id:
  disallowed_stage_ids:
    - stage_id:
      reason:
  stop_conditions:
    - condition:

state:
  rebuild_root: "Workflow / 20 Workflow vNext-R REBUILD"
  direction_id:
  phase_id:
  goal_id:
  task_id:
  current_workflow_state:
  last_validated_step:
  activation_scope: rebuild root only | direction opt-in | global

context:
  repository_files:
    - path:
      role:
      required: true | false
      freshness: fresh | stale | unknown
  project_files:
    - file:
      role:
      required: true | false
      freshness: fresh | stale | unknown
  prior_packets:
    - packet_id:
      packet_type:
      required: true | false
  excluded_context:
    - item:
      reason:

user_request:
  raw_request:
  interpreted_request:
  ambiguity_notes:
    - note:

mission:
  objective:
  non_objectives:
    - item:
  success_definition:
  smallest_safe_route:

inputs:
  artifacts:
    - name:
      type:
      location_or_path:
      required: true | false
  facts:
    - fact:
      source:
      freshness: fresh | stale | unknown
  assumptions:
    - assumption:
      risk:
      validation_needed: true | false

constraints:
  hard_constraints:
    - constraint:
  soft_preferences:
    - preference:
  safety_boundaries:
    - boundary:
  output_constraints:
    - constraint:

freshness_and_boundaries:
  web_required: true | false
  repository_read_required: true | false
  codex_required: true | false
  human_decision_required_before_write: true | false
  stale_context_policy:
  missing_context_policy:

expected_output:
  primary_packet_type: stage_result_packet
  must_include:
    - item:
  may_return:
    - context_request_card
    - human_decision_card
    - repository_patch_template
    - recovery_close_packet
  forbidden_outputs:
    - item:

downstream_usage:
  consumed_by:
    - target stage prompt
    - ChatGPT runtime router
  expected_next_artifact:
    - Stage Result Packet
  validation_notes:
    - Target stage must verify required fields before proceeding.
    - Target stage may ignore unknown extension fields.

extensions: {}

```

## Downstream usage

The Stage Launch Card is consumed by the target stage prompt and by the ChatGPT runtime router. It must be sufficient for the target stage to start without reading private internals from previous stages.

## Validation anchors

*   `stage_launch_card: 1`
*   `HTML is forbidden as transport.`
*   `Unknown extension handling`
*   `downstream_usage`