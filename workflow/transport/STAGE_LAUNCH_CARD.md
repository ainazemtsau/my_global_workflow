# Stage Launch Transport Template

```yaml
artifact_control:
  artifact_name: "Stage Launch Transport Template"
  schema: transport_template.v1
  owner_layer: transport
  status: canonical
  repo_path: "workflow/transport/STAGE_LAUNCH_CARD.md"
  runtime_schema: stage_launch.v1
  last_updated: "2026-05-13"
```

## Purpose

Defines the canonical transport template for launching a workflow stage.

This file is a transport template. It is not a stage prompt and not routing authority.

## Transport authority boundary — AD-WF-RT-001

This transport template is not independent routing authority.

Route fields are snapshots only. They must not override:

```text
workflow/stage_registry/STAGE_REGISTRY.md
```

If a route snapshot conflicts with the registry, return route-conflict Context Request / B1_PROBLEM / Human Decision / Stop.

Packet fields in this template must remain compatible with `workflow/runtime/WF_VNEXT_R_RUNTIME_CORE.md` until a later runtime-core reference cleanup changes packet-authority references.

## Transport invariants

- HTML is forbidden as transport.
- Use plain Markdown with YAML-style fields.
- Required fields must remain readable as plain text.
- Unknown extension fields must be tolerated by consumers.
- Do not embed private chain-of-thought or invisible scratchpad content.
- GitHub repository paths must be exact when referenced.
- Dates should use ISO-8601 when available.

## Canonical packet template

```yaml
workflow_packet: 1
type: stage_launch
schema: stage_launch.v1
action: run_stage
mode: execute
target_runtime: chatgpt_direction_project | chatgpt_current_chat | codex

stage:
  id:
  name:
  source_path:
  version:
  status:

prompt_delivery:
  mode: prompt_text_embedded | prompt_attachment_provided | manual_prompt_required | codex_verified_local_bundle
  stage_prompt_source_path:
  stage_prompt_version:
  stage_prompt_status:
  prompt_text_included: true | false
  prompt_text: null
  source_commit:
  line_count:
  byte_count:
  tail_anchor_or_eof_verified: true | false
  execute_allowed: true | false

direction:
  name:
  repository_path:
  project_name:

phase:
  name:
  path:
  status:
  critical_constraint:

goal:
  title:
  path:
  status:

source_state:
  from_stage:
  previous_return_state:
  pending_repository_patch: true | false
  changed_files_context_refresh_required: true | false

formalization_control:
  first_response_mode: compact_direct_result | reviewable_brief | decision_memo_work_product_preview | context_request_or_human_decision | formalization
  formalization_policy: proposal_first | direct_formalization_allowed
  approval_state:
    material_change_approved: true | false
    repository_patch_approved: true | false
    approval_source: none | launch_card | user_message | prior_stage_packet
  formalization_trigger: APPROVE AND FORMALIZE

input_artifacts:
  previous_stage_result_summary:
  goal_contract:
  execution_brief:
  decision_record:
  codex_return:
  other:

required_context:
  project_files:
    - 00_DIRECTION_START_HERE.md
    - 01_DIRECTION_STATE.md
    - 02_CURRENT_PHASE.md
    - 03_FOCUS_REGISTER.md
    - 04_ACTIVE_GOAL.md
    - 05_PORTFOLIO_QUEUE.md
    - 06_CONTEXT_LIBRARY_INDEX.md
    - 07_PHASE_MEMORY_INDEX.md
    - 08_DIRECTION_MAP.md
  shared_runtime_files:
    - WORKFLOW_SOURCE_OF_TRUTH.md
    - workflow/runtime/WF_VNEXT_R_RUNTIME_CORE.md
    - workflow/runtime/GITHUB_LONG_FILE_READ_GUARD.md
    - workflow/runtime/WORKFLOW_RUNTIME_CACHE_MANIFEST.md
    - workflow/stage_registry/STAGE_REGISTRY.md
  additional_repository_file_exports:
    - path:
      reason:
      required: true | false

missing_context_policy: ask_only_if_blocking

expected_first_response_outputs:
  - Direct Result / Reviewable Brief / Decision Memo / Work Product Preview
  - planned_patch_summary, if a repository change may be needed
  - planned_formalization_summary
  - approval request, Context Request, Human Decision, or Stop

expected_after_approval_outputs:
  - Human-readable result
  - Stage Result Packet
  - Repository Patch or none
  - Execution Log Entry
  - Changed Files / Context Refresh List
  - Next Launch Card / Context Request / Human Decision Card / Stop

expected_outputs:
  compatibility: fallback_only_do_not_override_formalization_control
  outputs:
    - Human-readable result
    - Stage Result Packet
    - Repository Patch or none
    - Execution Log Entry
    - Changed Files / Context Refresh List
    - Next Launch Card / Context Request / Human Decision Card / Stop

instructions:
  do_not_echo_prompt: true
  do_not_run_unrelated_stage: true
  do_not_reconstruct_missing_prompt: true
  route_authority: workflow/stage_registry/STAGE_REGISTRY.md

extensions: {}
```

## Validation anchors

- `workflow_packet: 1`
- `schema: stage_launch.v1`
- `route_authority: workflow/stage_registry/STAGE_REGISTRY.md`
- `target_runtime`
- `formalization_control`

## End-of-file marker

`END_OF_FILE: workflow/transport/STAGE_LAUNCH_CARD.md`
