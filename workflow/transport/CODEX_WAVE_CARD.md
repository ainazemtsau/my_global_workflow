# 08 Codex Wave Card Template
Status: draft Workflow version: vNext-R REBUILD Installed from roadmap step: Step 3 — Transport Templates Installed at: 2026-05-07T15:25:01.4848571+03:00 Source input: ChatGPT Step 3 result generated 2026-05-07 Authority: GitHub repository canonical after file read-back / diff verification / commit verification Activation scope: rebuild root only Freshness: fresh Supersedes: Superseded by:

# 08 Codex Wave Card Template

## Purpose

A Codex Wave Card is a generic transport packet for giving Codex a bounded unit of implementation, inspection, repair, validation, or installation work.

This Step 3 note defines only the packet shape. Detailed Codex bridge contracts are Step 4 work and are not created here.

This is a transport template only. It is not a C1/C2 final prompt and not an AGENTS.md contract.

## Transport invariants

*   HTML is forbidden as transport.
*   Use plain Markdown with YAML-style fields.
*   Unknown extension handling: consumers must tolerant-read unknown fields under `extensions`; producers must not make unknown extensions mandatory for correct execution.
*   Codex scope must be bounded by exact repository paths, GitHub repository paths, or named artifacts.
*   Codex must be told whether it is in preview, apply, inspect, repair, or validation mode.
*   Codex must return evidence through a Codex Return Packet.

## Required fields

*   `codex_wave_card`
*   `card_type`
*   `workflow_version`
*   `created_at`
*   `issuing_stage`
*   `wave_identity`
*   `mode`
*   `scope`
*   `task`
*   `constraints`
*   `allowed_actions`
*   `forbidden_actions`
*   `evidence_required`
*   `return_packet_requirement`
*   `downstream_usage`
*   `extensions`

## Template

```
codex_wave_card: 1
card_type: codex_wave
workflow_version: vNext-R REBUILD
created_at: YYYY-MM-DDTHH:MM:SS±HH:MM
created_by: ChatGPT

issuing_stage:
  stage_id:
  stage_name:
  result_packet_ref:
  execution_log_entry_ref:

wave_identity:
  wave_id:
  wave_title:
  wave_type: inspect | plan | implement | repair | validate | install_preview | install_apply
  priority: low | normal | high
  parent_wave_id:

mode:
  codex_mode: PREVIEW_ONLY | APPLY_AFTER_APPROVAL | APPLY_NOW_IF_SAFE | READ_ONLY
  human_approval_required_before_write: true | false
  stop_on_uncertainty: true | false

scope:
  repositories:
    - repo:
      branch:
      allowed_paths:
        - path:
      forbidden_paths:
        - path:
  repository_paths:
    - path:
      allowed_action:
  external_artifacts:
    - name:
      location:
      allowed_action:
  out_of_scope:
    - item:
      reason:

task:
  objective:
  acceptance_criteria:
    - criterion:
  non_objectives:
    - item:
  assumptions_allowed:
    - assumption:
  assumptions_forbidden:
    - assumption:

constraints:
  safety_constraints:
    - constraint:
  style_or_format_constraints:
    - constraint:
  dependency_constraints:
    - constraint:
  time_or_complexity_constraints:
    - constraint:

allowed_actions:
  - action:
forbidden_actions:
  - action:
    reason:

evidence_required:
  readback_required: true | false
  tests_required:
    - test:
  files_or_notes_to_report:
    - path:
  command_outputs_required:
    - command:
  validation_anchors:
    - text:

return_packet_requirement:
  required_packet_type: codex_return_packet
  must_include:
    - final_state
    - files_changed_or_notes_changed
    - evidence
    - problems_or_blockers
    - rollback_or_recovery_notes
  cannot_claim_done_without:
    - evidence
    - file read-back / diff verification / commit verification or equivalent verification when writes occur

downstream_usage:
  consumed_by:
    - Codex
    - ChatGPT validation
    - human reviewer
  expected_next_artifact:
    - Codex Return Packet
  validation_notes:
    - This card does not authorize work outside named scope.
    - Consumers may ignore unknown extension fields.

extensions: {}

```

## Downstream usage

The Codex Wave Card is consumed by Codex, ChatGPT validation, and human review. It is used to dispatch a bounded Codex work wave and require a structured return packet.

## Validation anchors

*   `codex_wave_card: 1`
*   `HTML is forbidden as transport.`
*   `Unknown extension handling`
*   `This Step 3 note defines only the packet shape.`
*   `downstream_usage`