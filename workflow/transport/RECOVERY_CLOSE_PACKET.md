# Recovery Close Transport Template

```yaml
artifact_control:
  artifact_name: "Recovery Close Transport Template"
  schema: transport_template.v1
  owner_layer: transport
  status: canonical
  repo_path: "workflow/transport/RECOVERY_CLOSE_PACKET.md"
  runtime_schema: recovery_close.v1
  last_updated: "2026-05-13"
```

## Purpose

Defines the canonical transport template for closing a failed, confused, partial, unsafe, or stale workflow route.

Recovery close records what failed, what was contained, what remains canonical, and how to safely resume or stop.

## Transport authority boundary — AD-WF-RT-001

This template is not routing authority. It must not silently relaunch or repair across a route conflict.

## Transport invariants

- HTML is forbidden as transport.
- Use plain Markdown with YAML-style fields.
- Unknown extension fields must be tolerated by consumers.
- Recovery must not silently patch forward from a confused state.
- Name the last known canonical state.
- Do not produce a next launch unless the failed state is contained and validation allows it.

## Canonical packet template

```yaml
workflow_packet: 1
type: recovery_close
schema: recovery_close.v1

recovery_source:
  source_stage_id:
  source_stage_name:
  failed_packet_ref:
  triggered_by: ChatGPT | Codex | human
  trigger_reason:

failure_summary:
  failure_type: missing_context | bad_install | wrong_path | missing_readback | uncontrolled_write | stale_context | unsafe_route | other
  concise_description:
  severity: low | medium | high | critical
  user_visible_impact:
  active_workflow_impact: none | suspected | confirmed

scope_contained:
  contained: true | false
  containment_actions:
    - action:
  paths_checked:
    - path:
  paths_confirmed_untouched:
    - path:
  remaining_uncertainty:
    - item:

canonical_state:
  last_known_good_step:
  last_known_good_validation_state:
  canonical_repository_paths:
    - path:
  canonical_project_files:
    - file:
  noncanonical_outputs:
    - item:
      reason:

stale_or_superseded_items:
  items_to_mark_stale:
    - path:
      reason:
      replacement_pointer:
  items_already_marked_stale:
    - path:
      evidence:

repair_actions:
  repair_needed: true | false
  repair_patch_ref:
  manual_repair_steps:
    - step:
  codex_repair_wave_ref:
  rerun_same_step_required: true | false

resume_or_stop_route:
  selected_route: rerun_same_step | return_to_validation | launch_next_step | stop | needs_input
  route_reason:
  next_launch_allowed: true | false
  next_launch_ref:
  stop_reason:
  needed_input:

human_manual_check:
  required: true | false
  checklist:
    - item:
  pass_condition:
  fail_condition:

extensions: {}
```

## Validation anchors

- `workflow_packet: 1`
- `schema: recovery_close.v1`
- `failure_summary`
- `canonical_state`
- `resume_or_stop_route`

## End-of-file marker

`END_OF_FILE: workflow/transport/RECOVERY_CLOSE_PACKET.md`
