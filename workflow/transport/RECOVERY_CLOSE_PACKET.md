# 10 Recovery Close Packet Template
Status: draft Workflow version: vNext-R REBUILD Installed from roadmap step: Step 3 — Transport Templates Installed at: 2026-05-07T15:25:01.4848571+03:00 Source input: ChatGPT Step 3 result generated 2026-05-07 Authority: GitHub repository canonical after file read-back / diff verification / commit verification Activation scope: rebuild root only Freshness: fresh Supersedes: Superseded by:

# 10 Recovery Close Packet Template

## Purpose

A Recovery Close Packet closes a failed, confused, partial, unsafe, or stale workflow route.

It records what failed, what was contained, what was marked stale, what remains canonical, and how to safely resume or stop.

This is a transport template only. It is not the final R0 Recovery Close stage prompt.

## Transport invariants

*   HTML is forbidden as transport.
*   Use plain Markdown with YAML-style fields.
*   Unknown extension handling: consumers must tolerant-read unknown fields under `extensions`; producers must not make unknown extensions mandatory for correct execution.
*   Recovery must not silently patch forward from a confused install.
*   Mark bad notes stale or move under controlled failed-install/draft-amendment paths when instructed.
*   Do not produce a next roadmap launch unless the failed state is contained and validation allows it.

## Required fields

*   `recovery_close_packet`
*   `packet_type`
*   `workflow_version`
*   `created_at`
*   `recovery_source`
*   `failure_summary`
*   `scope_contained`
*   `canonical_state`
*   `stale_or_superseded_items`
*   `repair_actions`
*   `resume_or_stop_route`
*   `human_manual_check`
*   `downstream_usage`
*   `extensions`

## Template

```
recovery_close_packet: 1
packet_type: recovery_close
workflow_version: vNext-R REBUILD
created_at: YYYY-MM-DDTHH:MM:SS±HH:MM
created_by: ChatGPT

recovery_source:
  source_stage_id:
  source_stage_name:
  failed_packet_ref:
  failed_install_result_ref:
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
  failed_install_archive_path:

repair_actions:
  repair_needed: true | false
  repair_patch_ref:
  manual_repair_steps:
    - step:
  codex_repair_wave_card_ref:
  rerun_same_step_required: true | false

resume_or_stop_route:
  selected_route: rerun_same_step | return_to_validation | launch_next_step | stop | needs_input
  route_reason:
  next_launch_card_allowed: true | false
  next_launch_card_ref:
  stop_reason:
  needed_input:

human_manual_check:
  required: true | false
  checklist:
    - item:
  pass_condition:
  fail_condition:

downstream_usage:
  consumed_by:
    - ChatGPT recovery flow
    - human reviewer
    - Codex repair wave
    - runtime router
  expected_next_artifact:
    - repair patch
    - same-step relaunch
    - validation result
    - stop
  validation_notes:
    - Recovery close must name the last canonical state.
    - Consumers may ignore unknown extension fields.

extensions: {}

```

## Downstream usage

The Recovery Close Packet is consumed by ChatGPT recovery flow, human review, Codex repair waves, and the runtime router.

## Validation anchors

*   `recovery_close_packet: 1`
*   `HTML is forbidden as transport.`
*   `Unknown extension handling`
*   `last_known_good_step`
*   `downstream_usage`