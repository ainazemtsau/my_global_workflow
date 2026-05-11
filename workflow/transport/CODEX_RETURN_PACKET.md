# 09 Codex Return Packet Template
Status: draft Workflow version: vNext-R REBUILD Installed from roadmap step: Step 3 — Transport Templates Installed at: 2026-05-07T15:25:01.4848571+03:00 Source input: ChatGPT Step 3 result generated 2026-05-07 Authority: GitHub repository canonical after file read-back / diff verification / commit verification Activation scope: rebuild root only Freshness: fresh Supersedes: Superseded by:

# 09 Codex Return Packet Template

## Purpose

A Codex Return Packet is the structured response Codex returns after a bounded wave of work.

It records final state, actions taken, evidence, tests, file read-back / diff verification / commit verification, blockers, rollback notes, and next route.

This Step 3 note defines only the packet shape. Detailed Codex bridge contracts are Step 4 work and are not created here.

This is a transport template only. It is not a C1/C2 final prompt.

## Transport invariants

*   HTML is forbidden as transport.
*   Use plain Markdown with YAML-style fields.
*   Unknown extension handling: consumers must tolerant-read unknown fields under `extensions`; producers must not make unknown extensions mandatory for correct execution.
*   Codex cannot claim DONE without evidence.
*   If writes occurred, Codex must include file read-back / diff verification / commit verification or equivalent verification.
*   If Codex lacks access, it must return NEEDS\_INPUT or STUCK, not DONE.

## Required fields

*   `codex_return_packet`
*   `packet_type`
*   `workflow_version`
*   `created_at`
*   `source_wave`
*   `final_state`
*   `actions_taken`
*   `changed_artifacts`
*   `evidence`
*   `validation`
*   `readback`
*   `problems_or_blockers`
*   `rollback_or_recovery`
*   `next_route`
*   `downstream_usage`
*   `extensions`

## Template

```
codex_return_packet: 1
packet_type: codex_return
workflow_version: vNext-R REBUILD
created_at: YYYY-MM-DDTHH:MM:SS±HH:MM
created_by: Codex

source_wave:
  wave_id:
  wave_title:
  wave_card_ref:
  requested_mode:
  actual_mode_used:

final_state:
  state: DONE | NEEDS_INPUT | STUCK | PARTIAL | FAILED
  status_summary:
  safe_to_continue: true | false
  done_claim_supported: true | false

actions_taken:
  summary:
  commands_run:
    - command:
      purpose:
      result:
  notes_read:
    - path:
  notes_written:
    - path:
      action:
  files_read:
    - path:
  files_changed:
    - path:
      action:

changed_artifacts:
  repository_files:
    - path:
      action:
      readback_status: pass | fail | not_applicable
  repository_files:
    - path:
      action:
      validation_status:
  generated_artifacts:
    - name:
      location:
      purpose:

evidence:
  evidence_items:
    - item:
      type: readback | test_output | diff | tree_listing | command_output | screenshot | manual_observation | other
      content_or_pointer:
  missing_evidence:
    - item:
      reason:
  evidence_limitations:
    - limitation:

validation:
  tests_run:
    - test:
      command_or_method:
      result: pass | fail | not_run
  checks_run:
    - check:
      result: pass | fail | not_applicable
  acceptance_criteria_results:
    - criterion:
      result: pass | fail | not_checked
  validation_gaps:
    - gap:

readback:
  readback_required: true | false
  readback_performed: true | false
  readback_summary:
  readback_failures:
    - path:
      issue:

problems_or_blockers:
  blockers:
    - blocker:
      needed_input:
      severity:
  nonblocking_notes:
    - note:
  unexpected_findings:
    - finding:

rollback_or_recovery:
  rollback_needed: true | false
  rollback_available: true | false
  rollback_steps:
    - step:
  recovery_close_packet_ref:
  stale_marking_recommended:
    - path:
      reason:

next_route:
  recommended_route: return_to_chatgpt_validation | request_user_input | rerun_wave | recovery_close | stop
  next_owner: ChatGPT | Codex | human
  next_instruction:

downstream_usage:
  consumed_by:
    - ChatGPT validation
    - human reviewer
    - runtime router
    - recovery flow
  expected_next_artifact:
    - validation result
    - repair instruction
    - recovery close packet
  validation_notes:
    - ChatGPT must verify final_state against evidence before accepting DONE.
    - Consumers may ignore unknown extension fields.

extensions: {}

```

## Downstream usage

The Codex Return Packet is consumed by ChatGPT validation, human review, runtime routing, and recovery flow.

## Validation anchors

*   `codex_return_packet: 1`
*   `HTML is forbidden as transport.`
*   `Unknown extension handling`
*   `Codex cannot claim DONE without evidence.`
*   `downstream_usage`