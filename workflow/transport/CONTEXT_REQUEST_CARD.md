# 03 Context Request Card Template
Status: draft Workflow version: vNext-R REBUILD Installed from roadmap step: Step 3 — Transport Templates Installed at: 2026-05-07T15:25:01.4848571+03:00 Source input: ChatGPT Step 3 result generated 2026-05-07 Authority: Trilium canonical after read-back Activation scope: rebuild root only Freshness: fresh Supersedes: Superseded by:

# 03 Context Request Card Template

## Purpose

A Context Request Card is emitted when a stage cannot safely proceed because required input, evidence, freshness, permission, or source material is missing.

It prevents vague clarification loops by naming exactly what is missing and what can proceed safely without it.

This is a transport template only. It is not a final stage prompt.

## Transport invariants

*   HTML is forbidden as transport.
*   Use plain Markdown with YAML-style fields.
*   Unknown extension handling: consumers must tolerant-read unknown fields under `extensions`; producers must not make unknown extensions mandatory for correct execution.
*   Ask only for context that blocks safe progress.
*   If safe partial progress exists, describe the partial route instead of stopping entirely.
*   Do not request old Workflow vNext archives unless the current step explicitly needs them.

## Required fields

*   `context_request_card`
*   `card_type`
*   `workflow_version`
*   `created_at`
*   `requesting_stage`
*   `blocking_status`
*   `missing_context`
*   `why_needed`
*   `safe_partial_route`
*   `requested_user_action`
*   `fallback_if_not_available`
*   `downstream_usage`
*   `extensions`

## Template

```
context_request_card: 1
card_type: context_request
workflow_version: vNext-R REBUILD
created_at: YYYY-MM-DDTHH:MM:SS±HH:MM
created_by: ChatGPT

requesting_stage:
  stage_id:
  stage_name:
  launch_card_ref:
  result_packet_ref:

blocking_status:
  is_blocking: true | false
  severity: low | medium | high
  can_continue_partially: true | false
  unsafe_to_continue_reason:

missing_context:
  required_items:
    - item_id:
      item_name:
      item_type: user_answer | trilium_note | project_file | source_document | codex_readback | web_verification | other
      exact_path_or_location:
      required: true | false
      freshness_required: fresh | stale_allowed | unknown_allowed
  optional_items:
    - item_id:
      item_name:
      value_if_available:

why_needed:
  dependency_explanation:
  risk_if_missing:
  decision_or_output_blocked:

safe_partial_route:
  available: true | false
  partial_output_possible:
  limits_on_partial_output:
  route_if_user_does_not_provide_context:

requested_user_action:
  exact_request:
  acceptable_response_formats:
    - format:
  do_not_provide:
    - item:
      reason:

fallback_if_not_available:
  fallback_assumption:
  fallback_risk:
  fallback_stage_or_stop_route:

downstream_usage:
  consumed_by:
    - human user
    - ChatGPT runtime router
    - requesting stage on resume
  expected_next_artifact:
    - user-provided context
    - revised launch card
    - stop
  validation_notes:
    - Requesting stage must consume only supplied context or explicitly state assumptions.
    - Consumers may ignore unknown extension fields.

extensions: {}

```

## Downstream usage

The Context Request Card is consumed by the human user, the runtime router, and the original requesting stage when work resumes.

## Validation anchors

*   `context_request_card: 1`
*   `HTML is forbidden as transport.`
*   `Unknown extension handling`
*   `safe_partial_route`
*   `downstream_usage`