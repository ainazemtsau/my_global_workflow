# Execution Work Package Transport Template

```yaml
artifact_control:
  artifact_name: "Execution Work Package Transport Template"
  schema: execution_work_package.v1
  owner_layer: transport
  status: canonical
  repo_path: "workflow/transport/EXECUTION_WORK_PACKAGE.md"
  packet_direction: chatgpt_to_executor
```

## Purpose

Defines the canonical transport template for ChatGPT to hand off product/project work to an Executor.

This packet is for product/project execution only. It is not a repository maintenance packet, not a workflow repository patch, not a project setup command, and not proof that execution has already occurred.

## Authority Boundary

Workflow transport templates own packet shape. Runtime behavior remains owned by `workflow/runtime/WF_VNEXT_R_RUNTIME_CORE.md`.

Stage identity and route validity remain owned by `workflow/stage_registry/STAGE_REGISTRY.md`. Any route-related field in this packet is a snapshot for review and must not override the registry.

## Canonical Packet Template

```yaml
workflow_packet: 1
type: execution_work_package
schema: execution_work_package.v1

packet_boundary:
  applies_to: product_project_execution
  repository_maintenance_packet: false
  product_execution_already_started: false

target_project_ref:
  direction_id:
  project_id:
  project_name:
  project_root_pointer:
  expected_repo_or_workspace:
  executor_setup_status:

setup_requirements:
  setup_required: true
  acceptable_setup_status:
    - complete
    - complete_with_approved_fallback
  customization_mode: core_only | tuned | deferred

work_definition:
  WHAT:
  WHY:
  DONE:
  acceptance_criteria:
    - criterion:

scope:
  scope_in:
    - item:
  scope_out:
    - item:
  forbidden_changes:
    - item:
  allowed_surfaces:
    - path_or_area:

project_local_pointers:
  agents_md: AGENTS.md
  project_profile: PROJECT_PROFILE.md
  executor_profile: EXECUTOR_PROFILE.md
  validation_profile: VALIDATION_PROFILE.md
  module_map: MODULE_MAP.md
  architecture_docs: docs/architecture
  module_docs: docs/modules
  public_interface_docs: docs/public-interfaces
  change_workspace: changes/<change-id>
  optional_codex_dir: .codex

execution_mode:
  planning_mode: P0 | P1 | P2 | P3
  task_master_graph_required: true | false
  plan_preview_required: true | false
  user_approval_required_before_autonomous_execution: true | false
  permission_mode: full_trust_target_bound

validation_expectations:
  validation_ladder_level: V0_READINESS | V1_PATCH_SANITY | V2_TARGETED_BEHAVIOR | V3_INTEGRATION_BUILD | V4_RELEASE_CONFIDENCE
  required_checks:
    - check:
  allowed_manual_evidence:
    - evidence_type:
  skipped_check_policy:

evidence_requirements:
  target_confirmation: true
  setup_status: true
  files_changed: true
  acceptance_mapping: true
  validation_output: true
  repair_attempts: true
  forbidden_path_confirmation: true
  residual_risks: true

stop_conditions:
  - wrong_target
  - setup_incomplete
  - repeated_validator_failure
  - new_dependency
  - new_module_boundary
  - forbidden_area
  - missing_validation_surface
  - out_of_scope_architecture_decision
  - public_api_scope_expansion

objective_architecture_reference:
  execution_readiness_summary:
  project_local_pointer:
  copy_full_objective_architecture_model: false

compatibility:
  current_c1_c2_may_use_or_adapt_later: true
  requires_later_approved_wave: true

non_goals:
  runtime_behavior_change: false
  stage_registration: false
  product_execution: false

extensions: {}
```

## Usage Notes

The Executor confirms `target_project_ref` before reading project-local context or changing files. A wrong target, incomplete setup, or missing validation surface blocks execution.

The Objective Architecture reference must stay compact. Do not copy the full Objective Architecture model into this packet.

## Validation Anchors

- `schema: execution_work_package.v1`
- `target_project_ref`
- `setup_required: true`
- `permission_mode: full_trust_target_bound`
- `validation_ladder_level`
- `stop_conditions`

END_OF_FILE: workflow/transport/EXECUTION_WORK_PACKAGE.md
