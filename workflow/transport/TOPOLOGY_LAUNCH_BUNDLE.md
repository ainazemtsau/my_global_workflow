# Topology Launch Bundle Transport Template

```yaml
artifact_control:
  artifact_name: "Topology Launch Bundle Transport Template"
  schema: transport_template.v1
  owner_layer: transport
  status: canonical
  repo_path: "workflow/transport/TOPOLOGY_LAUNCH_BUNDLE.md"
  runtime_schema: topology_launch_bundle.v1
  last_updated: "2026-05-15"
```

## Purpose

Defines the canonical transport template for launching multiple bounded workstream branches under one parent Goal.

A Topology Launch Bundle is one terminal launch artifact. It is not a stage prompt and not routing authority.

## Authority boundary

Route fields are snapshots only. Every branch launch card must target a registry-valid stage from:

```text
workflow/stage_registry/STAGE_REGISTRY.md
```

If a branch route conflicts with the registry, return route-conflict Context Request / B1_PROBLEM / Human Decision / Stop.

Runtime behavior, branchability gates, approval/formalization rules, and parent synthesis rules are owned by:

```text
workflow/runtime/WF_VNEXT_R_RUNTIME_CORE.md
```

## Canonical packet template

```yaml
workflow_packet: 1
type: topology_launch_bundle
schema: topology_launch_bundle.v1

topology:
  topology_id:
  parent_goal_id:
  parent_goal_title:
  selected_topology: single_direct | gated_sequential | parallel_workstreams | parallel_then_gated_synthesis | decision_map | executor_work_package | human_decision_blocked
  reason_monolithic_execution_rejected:
  parent_stage: E1_EXECUTION_BRIEF

source_state:
  direction_id:
  direction_name:
  phase_id:
  phase_name:
  source_goal_contract:
  source_stage_result:
  approval_state:
    material_change_approved: true | false
    approval_source:

branches:
  - branch_id:
    branch_name:
    required_for_synthesis: true | false
    branch_launch_card:
      workflow_packet: 1
      type: workstream_launch
      schema: workstream_launch_card.v1
      stage:
        id:
        name:
        source_path:
      branch_objective:
      expected_output:
      dependency_policy:
        mode: parallel_safe | gated_after | blocked_until | optional_parallel | synthesis_only
        depends_on:
          - branch_id:
        reason:
        uncertainty: none | low | medium | high
      artifact_policy:
        heavy_artifact_expected: true | false
        artifact_type:
        return_full_artifact_to_parent: false
        parent_must_read_full_artifact: false
        artifact_persistence:
          mode: ephemeral_chat | attached_file | repository_path_after_approval | codex_verified_export | not_persisted_summary_only
          pointer:
          parent_accessible_now: true | false
      state_policy:
        may_mutate_parent_goal: false
        may_mutate_direction_state: false
        may_emit_repository_patch: false
        must_return_to_parent: true
      return_contract:
        output_type: workstream_result_card.v1
        paste_back_to_parent_chat: true
      forbidden_actions:
        - action:
      stop_conditions:
        - condition:

synthesis_plan:
  required_branch_results:
    - branch_id:
  optional_branch_results:
    - branch_id:
  can_synthesize_if_partial: true | false
  partial_synthesis_conditions:
  conflict_policy:
  next_route_after_required_results:
  parent_synthesis_stage_hint: F0_FAST_DIRECT | E1_EXECUTION_BRIEF | S3_DECIDE | B1_PROBLEM | D1_DEEP_RESEARCH | A1_AUDIT | R1_GOAL_REVIEW_DISTILL

parent_return_instructions:
  expected_result_cards:
    - workstream_result_card.v1
  parent_reads_full_artifacts_by_default: false
  targeted_full_artifact_read_allowed_when:
    - branch marks synthesis insufficient
    - material conflict exists
    - confidence is low
    - R1 or user challenges evidence
    - required evidence is missing from the compact card

validation_anchors:
  - "schema: topology_launch_bundle.v1"
  - "selected_topology:"
  - "branches:"
  - "synthesis_plan:"
  - "state_policy:"
```

## End-of-file marker

`END_OF_FILE: workflow/transport/TOPOLOGY_LAUNCH_BUNDLE.md`
