# 05 Repository Patch Template
Status: draft Workflow version: vNext-R REBUILD Installed from roadmap step: Step 3 — Transport Templates Installed at: 2026-05-07T15:25:01.4848571+03:00 Source input: ChatGPT Step 3 result generated 2026-05-07 Authority: GitHub repository canonical after file read-back / diff verification / commit verification Activation scope: rebuild root only Freshness: fresh Supersedes: Superseded by:

# 05 Repository Patch Template

## Purpose

A Repository Patch Template describes exact file changes for Codex or a human to apply in the GitHub repository.

It prevents vague write instructions by naming exact paths, actions, content, validation anchors, forbidden paths, and file read-back / diff verification / commit verification expectations.

This is a transport template only. It is not a Codex bridge contract and not a final stage prompt.

## Transport invariants

*   HTML is forbidden as transport.
*   Use plain Markdown with YAML-style fields.
*   Unknown extension handling: consumers must tolerant-read unknown fields under `extensions`; producers must not make unknown extensions mandatory for correct execution.
*   Do not physically delete files unless explicit human approval is included.
*   Prefer `create`, `replace_file`, `replace_section`, `update_header`, or `mark_stale` over vague append behavior.
*   All content-bearing writes must include validation anchors.
*   No writes outside named paths.

## Allowed actions

*   `create`
*   `replace_file`
*   `replace_section`
*   `append_section`
*   `update_header`
*   `mark_stale`

## Required fields

*   `repository_patch_template`
*   `patch_type`
*   `workflow_version`
*   `created_at`
*   `source_stage`
*   `install_target`
*   `dependencies`
*   `files_to_create_or_update`
*   `files_to_mark_stale`
*   `do_not_touch`
*   `readback_requirements`
*   `rollback_note`
*   `downstream_usage`
*   `extensions`

## Template

```
repository_patch_template: 1
patch_type: repository_patch
workflow_version: vNext-R REBUILD
created_at: YYYY-MM-DDTHH:MM:SS±HH:MM
created_by: ChatGPT

source_stage:
  stage_id:
  stage_name:
  result_packet_ref:
  execution_log_entry_ref:

install_target:
  repository_root: "Workflow / 20 Workflow vNext-R REBUILD"
  activation_mode: draft | test-active | active-candidate
  global_activation: false
  codex_mode: PREVIEW_FIRST | APPLY_AFTER_HUMAN_APPROVAL

dependencies:
  required_notes:
    - path:
      required: true
      expected_status:
  required_prior_steps:
    - step_id:
      required: true
  dependency_failure_route: context_request | human_decision | recovery_close | stop

files_to_create_or_update:
  - path:
    title:
    action: create | replace_file | replace_section | append_section | update_header | mark_stale
    status: draft | test-active | active-candidate | active | superseded
    section_anchor:
    content: |
      [full note or section content]
    validation_anchors:
      - text:

files_to_mark_stale:
  - path:
    reason:
    replacement_pointer:
    header_updates:
      Status: superseded
      Freshness: stale
      Superseded by:

do_not_touch:
  - path:
    reason:

readback_requirements:
  expected_tree_root:
  expected_notes:
    - path:
  expected_headers:
    - field:
  expected_content_anchors:
    - path:
      anchors:
        - text:
  forbidden_changes:
    - path_or_pattern:
      reason:

rollback_note:
  rollback_possible: true | false
  rollback_method:
  stale_marking_if_failed:
  human_recovery_required_if:

downstream_usage:
  consumed_by:
    - Codex GitHub diff/commit/PR workflower
    - human manual installer
    - ChatGPT install validator
  expected_next_artifact:
    - Codex preview result
    - Codex install result
    - manual file read-back / diff verification / commit verification packet
  validation_notes:
    - Installer must not infer unspecified note structure.
    - Consumers may ignore unknown extension fields.

extensions: {}

```

## Downstream usage

The Repository Patch Template is consumed by Codex, a human manual installer, and ChatGPT install validation. It is the only acceptable transport form for structured GitHub repository file writes.

## Validation anchors

*   `repository_patch_template: 1`
*   `HTML is forbidden as transport.`
*   `Unknown extension handling`
*   `Allowed actions`
*   `readback_requirements`
*   `downstream_usage`