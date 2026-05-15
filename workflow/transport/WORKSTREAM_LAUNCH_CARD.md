# Workstream Launch Card Transport Template

```yaml
artifact_control:
  artifact_name: "Workstream Launch Card Transport Template"
  schema: transport_template.v1
  owner_layer: transport
  status: canonical
  repo_path: "workflow/transport/WORKSTREAM_LAUNCH_CARD.md"
  runtime_schema: workstream_launch_card.v1
  last_updated: "2026-05-15"
```

## Purpose

Defines the canonical transport template for launching one bounded branch/workstream under a parent Goal.

A Workstream Launch Card targets an existing registered stage. It is not a new stage ID and not routing authority.

## Authority boundary

Stage identity and allowed transitions are owned by:

```text
workflow/stage_registry/STAGE_REGISTRY.md
```

Runtime behavior and branch state policy are owned by:

```text
workflow/runtime/WF_VNEXT_R_RUNTIME_CORE.md
```

## Canonical packet template

```yaml
workflow_packet: 1
type: workstream_launch
schema: workstream_launch_card.v1

topology:
  topology_id:
  selected_topology:
  parent_goal_id:
  parent_goal_title:

branch:
  branch_id:
  branch_name:
  branch_objective:
  expected_output:
  required_for_synthesis: true | false

stage:
  id:
  name:
  source_path:
  reason:

prompt_delivery:
  mode: prompt_text_embedded | prompt_attachment_provided | manual_prompt_required | codex_verified_local_bundle
  stage_prompt_source_path:
  stage_prompt_version:
  stage_prompt_status:
  prompt_text_included: true | false
  prompt_text: null
  execute_allowed: true | false

dependency_policy:
  mode: parallel_safe | gated_after | blocked_until | optional_parallel | synthesis_only
  depends_on:
    - branch_id:
  reason:
  uncertainty: none | low | medium | high

artifact_policy:
  heavy_artifact_expected: true | false
  artifact_type: research_report | audit_report | decision_input | implementation_brief | codex_graph | other
  return_full_artifact_to_parent: false
  parent_must_read_full_artifact: false
  artifact_persistence:
    mode: ephemeral_chat | attached_file | repository_path_after_approval | codex_verified_export | not_persisted_summary_only
    pointer:
    parent_accessible_now: true | false

required_context:
  - item:

forbidden_actions:
  - action:

state_policy:
  may_mutate_parent_goal: false
  may_mutate_direction_state: false
  may_mutate_phase_state: false
  may_emit_repository_patch: false
  may_claim_parent_goal_accepted: false
  must_return_to_parent: true

return_contract:
  output_type: workstream_result_card.v1
  paste_back_to_parent_chat: true
  compact_card_required: true
  full_artifact_return_default: false

stop_conditions:
  - condition:

validation_anchors:
  - "schema: workstream_launch_card.v1"
  - "branch_id:"
  - "stage:"
  - "dependency_policy:"
  - "artifact_policy:"
  - "return_contract:"
```

## End-of-file marker

`END_OF_FILE: workflow/transport/WORKSTREAM_LAUNCH_CARD.md`
