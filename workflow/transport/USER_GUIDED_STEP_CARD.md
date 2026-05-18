# User Guided Step Card Transport Template

```yaml
artifact_control:
  artifact_name: "User Guided Step Card Transport Template"
  schema: transport_template.v1
  owner_layer: transport
  status: canonical
  repo_path: "workflow/transport/USER_GUIDED_STEP_CARD.md"
  runtime_schema: user_guided_step_card.v1
  last_updated: "2026-05-18"
```

## Purpose

Defines the canonical step-level transport template for `U1_USER_GUIDED_EXECUTION`.

A User Guided Step Card tells the human operator exactly what to do next in an external UI/program/site/setup surface, what they should see, and what evidence or confirmation to return.

This card is not a stage ID, not routing authority, and not a repository patch.

## Transport authority boundary — AD-WF-RT-001

This template is not routing authority. It must not alter stage IDs, registry transitions, or runtime routing rules.

Stage identity and transitions are owned by:

```text
workflow/stage_registry/STAGE_REGISTRY.md
```

Runtime behavior is owned by:

```text
workflow/runtime/WF_VNEXT_R_RUNTIME_CORE.md
```

## Transport invariants

- HTML is forbidden as transport.
- Use plain Markdown with YAML-style fields.
- Unknown extension fields must be tolerated by consumers.
- One card should normally contain one next action.
- Do not include secrets.
- Do not claim the external action was completed unless user/tool evidence confirms it.
- Destructive, irreversible, security, privacy, payment, permission, or account changes require explicit confirmation.

## Canonical packet template

```yaml
workflow_packet: 1
type: user_guided_step_card
schema: user_guided_step_card.v1

stage:
  id: U1_USER_GUIDED_EXECUTION
  name: User Guided Execution

task:
  objective:
  smallest_safe_slice:
  surface_type: external_app | website | chatgpt_ui | local_program | game_engine_editor | design_tool | admin_console | setup_wizard | os_ui | unknown
  tool_or_app_name:
  version_or_context:
  operator_skill_assumption: novice | intermediate | expert | unknown
  tool_binding_status: verified | not_verified | unavailable | unknown

current_state:
  known_screen_or_state:
  evidence_available:
    - user_text | screenshot | copied_error | none
  uncertainty:
    -

step:
  step_id:
  instruction:
  expected_visible_state:
  user_reply_required: OK | screenshot | copied_error_text | selected_option | observed_state | other
  screenshot_required: true | false
  screenshot_reason:
  if_mismatch:
  safe_stop_or_rollback:
  irreversible_or_sensitive_action: true | false
  confirmation_required_before_sensitive_action: true | false

validation:
  completion_signal:
  evidence_required:
  do_not_claim_done_without:

next_step_policy:
  proceed_after_ok: true | false
  proceed_after_screenshot_review: true | false
  route_if_error:
  route_if_decision_needed:
  route_if_research_needed:
  route_if_execution_replanned:

extensions: {}
```

## Validation anchors

- `workflow_packet: 1`
- `schema: user_guided_step_card.v1`
- `stage.id: U1_USER_GUIDED_EXECUTION`
- `step.instruction`
- `step.expected_visible_state`
- `step.user_reply_required`

## End-of-file marker

`END_OF_FILE: workflow/transport/USER_GUIDED_STEP_CARD.md`
