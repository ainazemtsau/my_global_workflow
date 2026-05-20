# Executor Setup Request Transport Template

```yaml
artifact_control:
  artifact_name: "Executor Setup Request Transport Template"
  schema: executor_setup_request.v1
  owner_layer: transport
  status: canonical
  repo_path: "workflow/transport/EXECUTOR_SETUP_REQUEST.md"
  packet_direction: chatgpt_to_executor_setup
```

## Purpose

Defines the canonical transport template for ChatGPT/E1 to request Executor Project Setup through `X0_EXECUTOR_PROJECT_SETUP`.

This packet is for product/project setup only. It is not repository maintenance, not normal execution, and not a registered stage identity.

## Authority Boundary

Workflow transport templates own packet shape. Runtime behavior remains owned by `workflow/runtime/WF_VNEXT_R_RUNTIME_CORE.md`.

Stage identity and route validity remain owned by `workflow/stage_registry/STAGE_REGISTRY.md`. Project Setup Wizard is a capability/action executed through `X0_EXECUTOR_PROJECT_SETUP`.

## Canonical Packet Template

```yaml
workflow_packet: 1
type: executor_setup_request
schema: executor_setup_request.v1

packet_boundary:
  setup_request: true
  execution_work_package: false
  repository_maintenance_packet: false

target_project_ref:
  direction_id:
  project_id:
  project_name:
  project_root_pointer:
  expected_repo_or_workspace:

setup_objective:
  reason:
  minimum_complete_setup_outcome:
  requested_executor_adapter:

project_identity:
  project_type:
  project_state: new | existing | unknown
  project_owner_direction:
  known_stack:
  known_constraints:

core_bootstrap_required:
  agents_md: true
  project_profile: true
  executor_profile: true
  validation_profile: true
  module_map: true
  doctor: true

codex_adapter_baseline:
  task_master_required: true
  subagents_required: true
  reviewer_roles_required: true
  doctor_required: true

stack_specific_tuning:
  mode: skip | evaluate | research_more
  candidates:
    - item:
      reason:
  decision_policy: enable_now | park | reject | research_more

validation_expectations:
  setup_doctor_required: true
  evidence_required:
    - target_confirmation
    - generated_or_verified_files
    - tool_verification
    - doctor_result
    - setup_status
    - customization_mode

forbidden_actions:
  - blind_optional_tool_install
  - full_product_context_mirroring_to_direction_project_files
  - product_execution_beyond_setup
  - repository_maintenance_without_separate_approval

expected_return:
  stage_id: X0_EXECUTOR_PROJECT_SETUP
  schema: executor_setup_result.v1
  template: workflow/transport/EXECUTOR_SETUP_RESULT.md

route_authority:
  selected_next_stage_must_be_registry_valid: true
  setup_stage: X0_EXECUTOR_PROJECT_SETUP
  executor_run_stage: X1_EXECUTOR_RUN

extensions: {}
```

## Usage Notes

Core-only setup is valid complete setup. Stack-specific tuning is optional and decision-gated unless it is needed to make validation or evidence possible.

No blind Unity, MCP, or optional tool install is allowed. Wrong target blocks setup mutation.

Setup action does not require prior completed Executor Project Setup. Product execution beyond setup requires a separate normal execution route.

## Validation Anchors

- `schema: executor_setup_request.v1`
- `target_project_ref`
- `setup_objective`
- `core_bootstrap_required`
- `expected_return.schema: executor_setup_result.v1`
- `route_authority.setup_stage: X0_EXECUTOR_PROJECT_SETUP`

END_OF_FILE: workflow/transport/EXECUTOR_SETUP_REQUEST.md
