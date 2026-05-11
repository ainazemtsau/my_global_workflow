# 02 Codex Wave Card Contract
Status: test-active Workflow version: vNext-R REBUILD Installed from roadmap step: Step 4 — Codex Bridge Contracts Installed at: 2026-05-07T15:53:47.6656515+03:00 Source input: ChatGPT Step 4 output using Project Files 01/02/03 Authority: GitHub repository canonical after file read-back / diff verification / commit verification Activation scope: rebuild root only Freshness: fresh Supersedes: none Superseded by: none

# 02 Codex Wave Card Contract

## Purpose

A Codex Wave Card is the executable handoff packet from ChatGPT, a future stage prompt, or a recovery process to Codex.

It tells Codex exactly what to inspect, preview, change, test, install, or repair. It also defines allowed targets, forbidden targets, evidence requirements, validator requirements, and the required return packet.

This contract does not define the final C1 or C2 prompts. It defines the bridge those later prompts must use.

## Core rules

1.  Codex must treat the Wave Card as the immediate work authorization.
2.  Codex must not infer write permission from surrounding conversation when the Wave Card says preview or inspect only.
3.  Codex must not write outside `allowed_targets`.
4.  Codex must not touch `forbidden_targets`.
5.  Codex must return a Codex Return Packet even when blocked.
6.  Codex must not claim DONE unless the required evidence and file read-back / diff verification / commit verification requirements are satisfied.
7.  Codex must preserve unknown extension fields unless explicitly instructed to normalize or replace the packet.
8.  A Wave Card may reference Task Master, but Task Master is never canonical for workflow content unless a later validated contract explicitly changes that.

## Required Codex Wave Card template

CODEX\_WAVE\_CARD\_BEGIN

```yaml
codex_wave_card: 1

wave:
  wave_id: "{{wave_id}}"
  short_name: "{{short_name}}"
  wave_record_path: "{{repository_wave_record_path_or_none}}"
  created_at: "{{created_at}}"

origin:
  origin_type: "stage | manual | recovery | install_validation"
  stage_id: "{{stage_id_or_none}}"
  stage_name: "{{stage_name_or_none}}"
  source_packet_path: "{{repository_path_or_none}}"
  user_request_summary: "{{one_sentence_summary}}"

mode:
  codex_mode: "PREVIEW_FIRST | APPLY_AFTER_CONFIRM | INSPECT_ONLY"
  write_permission: "none | preview_only | allowed_after_human_apply"
  requires_explicit_apply_command: true
  exact_apply_command: "APPLY_INSTALL | APPLY_WAVE | APPLY_PATCH"

authority:
  canonical_repository_root: "Workflow / 20 Workflow vNext-R REBUILD"
  canonical_sources:
    - path: "{{repository_file_path}}"
      required: true
  project_files:
    - file: "01_WORKFLOW_REBUILD_CONTROL_PACK.md"
      required: true
    - file: "02_CURRENT_REBUILD_STATE.md"
      required: true
    - file: "03_CODEX_TRILIUM_INSTALLER_UNIVERSAL.md"
      required: false
  stale_or_untrusted_sources:
    - "{{source_to_ignore_unless_reintroduced}}"

task:
  task_type: "inspect | plan | patch | test | install | repair | document"
  objective: "{{specific_objective}}"
  non_goals:
    - "{{explicit_non_goal}}"
  acceptance_criteria:
    - "{{observable_acceptance_criterion}}"

allowed_targets:
  repository_paths:
    - "{{allowed_repository_path_or_none}}"
  repository_paths:
    - "{{allowed_repo_path_or_none}}"
  commands:
    - "{{allowed_command_or_category}}"

forbidden_targets:
  repository_paths:
    - "{{forbidden_repository_path_or_pattern}}"
  repository_paths:
    - "{{forbidden_repo_path_or_pattern}}"
  commands:
    - "{{forbidden_command_or_category}}"
  data:
    - "secrets"
    - "credentials"
    - "unrequested private data"

implementation_constraints:
  minimal_safe_change: true
  preserve_existing_behavior_unless_requested: true
  no_global_activation: true
  no_final_stage_prompts_unless_step_7_plus: true
  stop_on_ambiguous_write_scope: true

evidence_requirements:
  required_readback:
    - "{{path_or_artifact_to_read_back}}"
  required_commands:
    - "{{validator_or_command}}"
  required_artifacts:
    - "{{diff_summary | note_tree | test_output | log_entry}}"
  forbidden_change_check: true

task_master:
  access_granted: false
  project_identifier: "{{project_or_none}}"
  allowed_task_ids:
    - "{{task_id_or_none}}"
  allowed_actions:
    - "read | comment | status_update | create_subtask"
  must_not_mark_done_without_wave_validation: true

return_packet:
  required_contract: "Codex Return Packet Contract v1"
  required_final_states:
    - "DONE"
    - "NEEDS_INPUT"
    - "PARTIAL"
    - "STUCK"
    - "FAILED"
  must_include_next_route: true

```

CODEX\_WAVE\_CARD\_END

## Codex behavior requirements

When Codex receives a Wave Card, it must:

1.  Read all required canonical sources it can access.
2.  Report missing required sources before attempting writes.
3.  Return a preview when `codex_mode` is `PREVIEW_FIRST`.
4.  Wait for the exact apply command when `requires_explicit_apply_command` is true.
5.  Apply only the previewed changes unless the user gives a new Wave Card.
6.  Read back every created or changed GitHub repository file when the task involves GitHub repository.
7.  Run required validators when available.
8.  State explicitly when a validator cannot be run.
9.  Return a complete Codex Return Packet.
10.  Avoid creating final stage prompts before Step 7+.

## Invalid Wave Card outcomes

Codex must return `NEEDS_INPUT` or `STUCK`, not DONE, when:

*   required canonical sources are inaccessible;
*   write scope is ambiguous;
*   allowed targets and requested work conflict;
*   forbidden paths would need to be touched;
*   validators required for DONE cannot run and no waiver is present;
*   file read-back / diff verification / commit verification is required but cannot be performed;
*   the Wave Card asks Codex to overwrite active Workflow vNext without explicit global activation approval.

## Acceptance anchors

This note is acceptable only if these anchors remain visible on file read-back / diff verification / commit verification:

*   `CODEX_WAVE_CARD_BEGIN`
*   `requires_explicit_apply_command: true`
*   `allowed_targets`
*   `forbidden_targets`
*   `must_not_mark_done_without_wave_validation: true`
*   `CODEX_WAVE_CARD_END`