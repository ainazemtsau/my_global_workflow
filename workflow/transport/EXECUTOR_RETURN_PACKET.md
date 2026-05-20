# Executor Return Packet Transport Template

```yaml
artifact_control:
  artifact_name: "Executor Return Packet Transport Template"
  schema: executor_return_packet.v1
  owner_layer: transport
  status: canonical
  repo_path: "workflow/transport/EXECUTOR_RETURN_PACKET.md"
  packet_direction: executor_to_chatgpt
```

## Purpose

Defines the canonical transport template for Executor to ChatGPT evidence return after product/project execution.

The readable execution result comes first. The machine-readable packet section follows the readable result.

## Authority Boundary

Workflow transport templates own packet shape. Runtime behavior remains owned by `workflow/runtime/WF_VNEXT_R_RUNTIME_CORE.md`.

Stage identity and route validity remain owned by `workflow/stage_registry/STAGE_REGISTRY.md`. Route fields in this packet are recommendations only and must not override the registry.

## Human-Readable Execution Result

```text
Executor Return

Status:
DONE | NEEDS_INPUT | STUCK | PARTIAL | FAILED

Note:
PARTIAL and FAILED are allowed only when the active compatibility contract allows them. Otherwise map PARTIAL to NEEDS_INPUT or STUCK, and map FAILED to STUCK unless the active route defines another safe mapping.

Target:
- direction_id:
- project_id:
- project_name:
- project_root_pointer:
- expected_repo_or_workspace:
- executor_setup_status:

Summary:

Files changed:
- path:
  reason:

Validation:
- check:
  result:
  output summary:

Acceptance coverage:
- criterion:
  evidence:
  status:

Repair attempts:
- attempt:
  result:

Scope and forbidden-path confirmation:

Risks / unresolved issues:

Blockers:

Next recommended route:
```

## Canonical Packet Template

```yaml
workflow_packet: 1
type: executor_return_packet
schema: executor_return_packet.v1

status: DONE | NEEDS_INPUT | STUCK | PARTIAL | FAILED
status_compatibility_note: "PARTIAL/FAILED are allowed only when the active compatibility contract allows them; otherwise map to NEEDS_INPUT or STUCK."

target_project_ref:
  direction_id:
  project_id:
  project_name:
  project_root_pointer:
  expected_repo_or_workspace:
  executor_setup_status:

setup_status:
planning_mode: P0 | P1 | P2 | P3
task_master_graph_used: true | false
plan_preview_approved: true | false | not_required

work_completed_summary:

files_changed:
  - path:
    change_reason:
    module_or_area:

modules_touched:
  - module_or_area:

acceptance_coverage:
  - criterion:
    evidence:
    status: pass | fail | blocked | not_applicable

validation_performed:
  - level: V0_READINESS | V1_PATCH_SANITY | V2_TARGETED_BEHAVIOR | V3_INTEGRATION_BUILD | V4_RELEASE_CONFIDENCE
    command_or_check:
    result: pass | fail | skipped | blocked
    output_summary:
    skipped_checks_with_reason:
      - check:
        reason:

repair_attempts:
  - attempt_number:
    failed_check:
    suspected_root_cause:
    repair_action:
    rerun_result:

reviewer_or_subagent_evidence:
  - reviewer_or_role:
    evidence:
    result:

scope_and_forbidden_path_confirmation:
  approved_scope_only: true | false
  forbidden_paths_touched: true | false
  notes:

reuse_architecture_notes:
  existing_code_checked: true | false
  reuse_or_extension_decision:
  architecture_boundary_notes:

risks_and_unresolved_issues:
  - issue:
    severity:
    blocking: true | false

blockers:
  - blocker:
    required_resolution:

next_recommended_route:
  route:
  reason:

direction_state_boundary:
  executor_return_is_evidence: true
  chatgpt_review_approval_owns_workflow_state_update: true

no_done_without_evidence:
  required: true
  target_confirmed: true | false
  acceptance_evidenced: true | false
  validation_evidenced: true | false
  forbidden_paths_confirmed: true | false

extensions: {}
```

## DONE Rule

There is no DONE without evidence. The Executor must not claim DONE from intent, code changes alone, unavailable checks without explanation, or unreviewed assumptions.

ChatGPT review and approval own workflow state updates. The Executor return is evidence for that review, not a Direction state mutation by itself.

## Project Files / Direction State Boundary

The executor return is evidence. ChatGPT review and approval own any workflow state update, including whether Direction Project Files receive a compact outcome summary or pointers to project-local evidence.

## Validation Anchors

- `schema: executor_return_packet.v1`
- `Human-Readable Execution Result`
- `status: DONE | NEEDS_INPUT | STUCK | PARTIAL | FAILED`
- `target_project_ref`
- `validation_performed`
- `no_done_without_evidence`

END_OF_FILE: workflow/transport/EXECUTOR_RETURN_PACKET.md
