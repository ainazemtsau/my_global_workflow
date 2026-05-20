# Workstream Result Card Transport Template

```yaml
artifact_control:
  artifact_name: "Workstream Result Card Transport Template"
  schema: transport_template.v1
  owner_layer: transport
  status: canonical
  repo_path: "workflow/transport/WORKSTREAM_RESULT_CARD.md"
  runtime_schema: workstream_result_card.v1
  last_updated: "2026-05-15"
```

## Purpose

Defines the canonical transport template for returning one bounded branch/workstream result to a parent synthesis chat.

The Workstream Result Card is compact by default. It must not paste full heavy artifacts into the parent by default.

## Authority boundary

Runtime behavior, state mutation policy, and parent synthesis rules are owned by:

```text
workflow/runtime/WF_VNEXT_R_RUNTIME_CORE.md
```

Packet shape is defined here.

## Canonical packet template

```yaml
workflow_packet: 1
type: workstream_result
schema: workstream_result_card.v1

identity:
  topology_id:
  parent_goal_id:
  parent_goal_title:
  branch_id:
  branch_name:
  branch_stage:
  return_state: DONE | PARTIAL | NEEDS_INPUT | STUCK

compact_summary:
  - point:

parent_relevant_findings:
  - finding:
    implication_for_parent_goal:
    confidence: low | medium | high

artifact:
  produced: true | false
  title:
  type: research_report | audit_report | decision_input | implementation_brief | executor_work_package | executor_execution_plan | other
  persistence_mode: ephemeral_chat | attached_file | repository_path_after_approval | codex_verified_export | not_persisted_summary_only
  pointer:
  parent_accessible_now: true | false
  parent_must_read_full_artifact: false
  recommended_sections_to_read:
    - section:
      why:

decisions_made:
  - decision:

decisions_not_made:
  - open_decision:
    reason:
    recommended_route: S3_DECIDE | D1_DEEP_RESEARCH | A1_AUDIT | E1_EXECUTION_BRIEF | B1_PROBLEM | Context Request | Human Decision | Stop

blockers:
  - blocker:

synthesis_readiness:
  sufficient_for_parent_synthesis: true | false
  missing_inputs:
    - item:
  confidence: low | medium | high

recommended_parent_next_action:
  action:
  reason:

state_policy_confirmation:
  parent_goal_mutated: false
  direction_state_mutated: false
  phase_state_mutated: false
  repository_patch_emitted: false
  parent_goal_acceptance_claimed: false

validation_anchors:
  - "schema: workstream_result_card.v1"
  - "branch_id:"
  - "compact_summary:"
  - "synthesis_readiness:"
  - "state_policy_confirmation:"
```

## End-of-file marker

`END_OF_FILE: workflow/transport/WORKSTREAM_RESULT_CARD.md`
