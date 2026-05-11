# 04 Human Decision Card Template
Status: draft Workflow version: vNext-R REBUILD Installed from roadmap step: Step 3 — Transport Templates Installed at: 2026-05-07T15:25:01.4848571+03:00 Source input: ChatGPT Step 3 result generated 2026-05-07 Authority: Trilium canonical after read-back Activation scope: rebuild root only Freshness: fresh Supersedes: Superseded by:

# 04 Human Decision Card Template

## Purpose

A Human Decision Card is emitted when the workflow needs an explicit user choice before it can safely continue.

It separates true decisions from routine missing-context questions and prevents the system from silently choosing policy, scope, priority, destructive action, or activation level.

This is a transport template only. It is not a final stage prompt.

## Transport invariants

*   HTML is forbidden as transport.
*   Use plain Markdown with YAML-style fields.
*   Unknown extension handling: consumers must tolerant-read unknown fields under `extensions`; producers must not make unknown extensions mandatory for correct execution.
*   Present decision options neutrally unless a recommendation is explicitly justified.
*   Do not default to destructive, global, irreversible, or active-workflow-changing actions.
*   Do not bundle unrelated decisions into one ambiguous choice.

## Required fields

*   `human_decision_card`
*   `card_type`
*   `workflow_version`
*   `created_at`
*   `requesting_stage`
*   `decision`
*   `options`
*   `recommendation`
*   `impact`
*   `required_response`
*   `route_after_decision`
*   `downstream_usage`
*   `extensions`

## Template

```
human_decision_card: 1
card_type: human_decision
workflow_version: vNext-R REBUILD
created_at: YYYY-MM-DDTHH:MM:SS±HH:MM
created_by: ChatGPT

requesting_stage:
  stage_id:
  stage_name:
  launch_card_ref:
  result_packet_ref:

decision:
  decision_id:
  decision_title:
  decision_question:
  why_human_decision_is_required:
  blocking: true | false
  reversibility: reversible | difficult | irreversible
  activation_impact: none | rebuild_root_only | direction_opt_in | global

options:
  - option_id: A
    label:
    description:
    benefits:
      - item:
    risks:
      - item:
    downstream_effect:
    safe_default: true | false
  - option_id: B
    label:
    description:
    benefits:
      - item:
    risks:
      - item:
    downstream_effect:
    safe_default: true | false

recommendation:
  recommended_option_id:
  rationale:
  confidence: high | medium | low
  no_recommendation_reason:

impact:
  scope_affected:
    - path_or_stage:
  writes_or_activation_blocked:
    - item:
  risk_of_no_decision:
  rollback_complexity:

required_response:
  acceptable_answers:
    - option_id:
  user_may_modify_option: true | false
  minimum_user_input_needed:

route_after_decision:
  if_option_A:
    next_route:
    next_stage_id:
    patch_required: true | false
  if_option_B:
    next_route:
    next_stage_id:
    patch_required: true | false
  if_no_decision:
    next_route: stop | context_request | partial_safe_route
    reason:

downstream_usage:
  consumed_by:
    - human user
    - ChatGPT runtime router
    - requesting stage on resume
  expected_next_artifact:
    - user decision
    - revised launch card
    - stop
  validation_notes:
    - Runtime must not infer a decision when explicit human approval is required.
    - Consumers may ignore unknown extension fields.

extensions: {}

```

## Downstream usage

The Human Decision Card is consumed by the human user, the runtime router, and the requesting stage after the user chooses an option.

## Validation anchors

*   `human_decision_card: 1`
*   `HTML is forbidden as transport.`
*   `Unknown extension handling`
*   `activation_impact`
*   `downstream_usage`