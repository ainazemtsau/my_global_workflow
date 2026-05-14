# 01 Wave Record Template
artifact_control:
  artifact_name: "01 Wave Record Template"
  schema: codex_workflow_contract.v1
  owner_layer: codex_runtime_contract
  status: canonical
  repo_path: "workflow/codex/WAVE_RECORD_TEMPLATE.md"
  authority: "GitHub repository canonical after file read-back / diff verification / commit verification"
  activation_scope: workflow_runtime_reference
  freshness: refresh_when_codex_runtime_contract_changes
  last_updated: "2026-05-13"

# 01 Wave Record Template

## Purpose

A Wave Record is the persistent ledger entry for one Codex work wave.

It must be readable as normal GitHub repository markdown and also structured enough for Codex to parse without relying on HTML, screenshots, or implicit conversation memory.

A Wave Record is not a stage prompt. It does not itself authorize work. It records the lifecycle of a Codex wave, links the originating handoff packet, captures evidence, and preserves validation status.

## Contract rules

1.  One Wave Record exists for one `wave_id`.
2.  The Wave Record must remain GitHub repository-readable as a human audit note.
3.  The Wave Record must remain Codex-readable through stable headings, explicit field names, and a YAML data block.
4.  The associated Codex Wave Card is the executable handoff packet.
5.  The associated Codex Return Packet is the required result/evidence packet.
6.  A Wave Record may be created before Codex runs, but it must not be marked `validated` until ChatGPT or a named human validator records PASS or PASS\_WITH\_NONBLOCKING\_NOTES.
7.  Unknown extension fields are tolerated. Codex must preserve unknown fields unless the Wave Card explicitly authorizes a rewrite.
8.  HTML is not valid transport for a Wave Record.
9.  Final C1/C2 stage prompts are not defined here.

## Status vocabulary

Allowed `wave_status` values:

```text
draft
planned
previewed
applied
returned
validation_pending
validated
failed
repaired
superseded

```

Status meanings:

*   `draft`: record exists but is not ready for Codex.
*   `planned`: record has enough fields to generate or attach a Codex Wave Card.
*   `previewed`: Codex has returned a preview but has not applied writes.
*   `applied`: Codex reports writes were applied, but validation is not complete.
*   `returned`: Codex returned a packet and evidence.
*   `validation_pending`: awaiting ChatGPT or human validation.
*   `validated`: validation recorded PASS or PASS\_WITH\_NONBLOCKING\_NOTES.
*   `failed`: validation failed or Codex returned failed/stuck output.
*   `repaired`: a recovery action repaired a failed wave.
*   `superseded`: later record replaces this wave.

## Required template

WAVE\_RECORD\_TEMPLATE\_BEGIN

# Wave Record: {{wave\_id}} — {{short\_name}}

```yaml
wave_record:
  schema_version: 1
  workflow_version: "vNext-R REBUILD"
  wave_id: "{{wave_id}}"
  short_name: "{{short_name}}"
  wave_status: "draft"
  created_at: "{{created_at}}"
  updated_at: "{{updated_at}}"

origin:
  originating_stage_id: "{{stage_id_or_manual}}"
  originating_stage_name: "{{stage_name_or_manual}}"
  stage_result_packet_path: "{{repository_path_or_none}}"
  launch_card_path: "{{repository_path_or_none}}"
  human_request_summary: "{{one_sentence_summary}}"

authority:
  canonical_root: "Workflow / 20 Workflow vNext-R REBUILD"
  canonical_sources:
    - "{{repository_file_path}}"
  project_files_used:
    - "01_WORKFLOW_REBUILD_CONTROL_PACK.md"
    - "02_CURRENT_REBUILD_STATE.md"
    - "03_CODEX_TRILIUM_INSTALLER_UNIVERSAL.md"
  noncanonical_sources:
    - "{{optional_reference_or_none}}"

scope:
  work_type: "inspect | plan | patch | test | install | repair | document"
  target_system: "GitHub repository | repository | local_files | mixed"
  target_paths:
    - "{{allowed_target_path}}"
  forbidden_paths:
    - "{{forbidden_path_or_pattern}}"
  activation_scope: "rebuild root only | direction opt-in | global"
  global_activation_allowed: false

codex_handoff:
  codex_wave_card_path: "{{repository_path_or_inline_packet_id}}"
  codex_mode: "PREVIEW_FIRST | APPLY_AFTER_CONFIRM | INSPECT_ONLY"
  expected_return_packet: "Codex Return Packet Contract v1"
  requires_read_back: true

task_master:
  access_granted: false
  allowed_task_ids:
    - "{{task_id_or_none}}"
  allowed_actions:
    - "read | comment | status_update | create_subtask"
  canonical_for_workflow_content: false

acceptance:
  required_evidence:
    - "{{evidence_item}}"
  required_validators:
    - "{{validator_name}}"
  required_readback:
    - "{{path_or_artifact}}"
  done_blockers:
    - "{{condition_that_blocks_DONE}}"

execution_summary:
  plan_summary: "{{short_summary_or_pending}}"
  files_or_notes_changed:
    - "{{path_or_none_yet}}"
  commands_run:
    - "{{command_or_none_yet}}"
  evidence_paths:
    - "{{evidence_path_or_none_yet}}"

validation:
  codex_final_state: "not_returned | DONE | NEEDS_INPUT | PARTIAL | STUCK | FAILED"
  chatgpt_validation_state: "not_checked | PASS | PASS_WITH_NONBLOCKING_NOTES | FAIL | NEEDS_INPUT"
  validator_name: "{{validator_or_none}}"
  validation_date: "{{date_or_pending}}"
  validation_notes: "{{notes_or_pending}}"

next_route:
  route_type: "return_to_chatgpt_validation | human_decision | recovery | next_stage"
  instruction: "{{exact_next_instruction}}"

```

## Human-readable summary

*   Wave ID: `{{wave_id}}`
*   Current status: `{{wave_status}}`
*   Target system: `{{target_system}}`
*   Allowed targets: `{{target_paths}}`
*   Forbidden targets: `{{forbidden_paths}}`
*   Codex mode: `{{codex_mode}}`
*   Read-back required: `{{requires_read_back}}`
*   Validation state: `{{chatgpt_validation_state}}`

## Evidence ledger

| Evidence item | Required | Returned | Pass/fail | Notes |
| --- | ---: | ---: | ---: | --- |
| Source digest | yes | pending | pending | Must identify canonical source notes or files. |
| Target diff or note write list | yes | pending | pending | Must name exact changed files/notes. |
| Validator output | yes | pending | pending | Must include command/result or explicit not-run reason. |
| Read-back evidence | yes | pending | pending | Required for GitHub repository files and install operations. |
| Forbidden path check | yes | pending | pending | Must confirm protected paths were not changed. |

## Change log

| Date/time | Actor | Change |
| --- | --- | --- |
| `{{created_at}}` | `{{actor}}` | Created Wave Record. |

WAVE\_RECORD\_TEMPLATE\_END

## Codex Wave/Return schema compatibility note

Wave Records may continue to use human-readable names such as `Codex Wave Card` and `Codex Return Packet`.

Canonical transport schema IDs are:

```text
codex_wave.v1
codex_return.v1
```

Compatibility aliases:

```text
codex_wave_card: 1 -> codex_wave.v1
codex_return_packet / codex_return_packet.v1 -> codex_return.v1
CODEX_WAVE_CARD_BEGIN/END -> extensions.legacy_wrapper
CODEX_RETURN_PACKET_BEGIN/END -> extensions.legacy_wrapper
```

Wave Records should point to the canonical transport templates:

```text
workflow/transport/CODEX_WAVE_CARD.md
workflow/transport/CODEX_RETURN_PACKET.md
```

Legacy aliases may be preserved in historical Wave Records, but new Wave Records should reference canonical schema IDs where practical.

## Acceptance anchors

This note is acceptable only if these anchors remain visible on file read-back / diff verification / commit verification:

*   `WAVE_RECORD_TEMPLATE_BEGIN`
*   `wave_status`
*   `requires_read_back: true`
*   `chatgpt_validation_state`
*   `WAVE_RECORD_TEMPLATE_END`
