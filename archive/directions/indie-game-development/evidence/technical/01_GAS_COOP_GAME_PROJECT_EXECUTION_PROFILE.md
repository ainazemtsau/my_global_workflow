# Gas Coop Game Project Execution Profile

```yaml
artifact_control:
  artifact_name: "Gas Coop Game Project Execution Profile"
  schema: project_execution_profile.v1
  owner_layer: direction_goal_artifact
  status: active_profile_addendum
  repo_path: "directions/indie-game-development/phases/core-coop-technical-foundation-selection/goals/codex-development-operating-model-and-architecture-protocols/01_GAS_COOP_GAME_PROJECT_EXECUTION_PROFILE.md"
  direction_id: indie_game_development
  phase_id: core-coop-technical-foundation-selection
  goal_id: H1_G2_codex_development_operating_model_and_architecture_protocols
  source_stage: F0_FAST_DIRECT
  formalized_at: "2026-05-19"
  scope: "Minimal zero-state project execution profile / addendum for future Gas Coop Game bootstrap readiness."
  implementation_allowed: false
  unity_bootstrap_allowed: false
  product_repo_creation_allowed: false
  codex_product_execution_allowed: false
  unity_mcp_status: deferred_until_H1_G3
```

## 1. Zero-state assumption

This profile assumes the Gas Coop Game product workspace does not exist yet.

```yaml
zero_state_assumption:
  product_repo: absent
  Unity_project: absent
  validators: absent
  tool_bindings: absent_or_unverified
  AGENTS_md: absent
  codex_config: absent
  Task_Master: absent
  Serena: absent
  Basic_Memory: absent
```

Consequence:

- Do not infer any project-local technical memory, validators, Unity scenes, Codex settings, Task Master graph, Serena setup, Basic Memory setup, or tool-binding state from workflow governance notes.
- Treat every future product/project execution dependency as unverified until a later basis-valid route verifies it against the actual product repository and Unity project.
- This profile is not a bootstrap operation. It is a readiness addendum for later bootstrap planning.

## 2. Future bootstrap readiness target

Future H1_G3 bootstrap readiness should establish the smallest project-local execution surface needed before production code slices.

Required future targets:

```yaml
future_bootstrap_readiness_target:
  create_new_product_repository_later: true
  create_new_Unity_project_later: true
  establish_project_local_AGENTS_md_later: true
  establish_project_scoped_codex_config_policy_later: true
  define_validation_scene_or_harness_before_production_slices: true
  verify_tool_bindings_before_Codex_product_execution: true
```

The future bootstrap route should prove:

- where the product repository lives;
- where the Unity project lives;
- which project-local files Codex must read before execution;
- which validators exist and how they are run;
- which Unity-visible or test-visible validation surfaces exist;
- which tool bindings are installed, enabled, trusted, and scoped to the project;
- which operations remain manual or user-guided.

## 3. Validation profile

No functional production-code slice may be accepted without an explicit validation surface.

```yaml
validation_profile:
  Unity_visible_or_test_visible_validation_required: true
  unit_tests_for_pure_domain_logic_where_sensible: true
  validation_scene_or_harness_requirement: true
  logs_debug_overlay_inspector_or_manual_checklist_allowed_when_automation_not_sensible: true
  no_production_code_slice_without_validation_surface: true
```

Validation surface options, in preferred order when sensible:

1. Unit tests for pure/domain logic.
2. Integration or harness tests for linked systems.
3. Unity validation scene for Unity-visible behavior.
4. Debug overlay, inspector, logs, or telemetry evidence for state that cannot yet be automated cleanly.
5. Manual checklist only when automation would be premature or misleading.

Every later Codex product slice must state:

- what behavior is being validated;
- which validator or scene/harness/checklist proves it;
- what observable result the user or reviewer can inspect;
- what stops the slice if validation cannot be produced.

## 4. Memory and tool-binding policy

ChatGPT Direction Project owns workflow orchestration, not full product technical context.

```yaml
memory_and_tool_binding_policy:
  ChatGPT_direction_project_does_not_store_full_product_technical_context: true
  product_repo_local_memory_expected_later: true
  AGENTS_md_policy_later: true
  codex_config_policy_later: true
  Task_Master_Serena_Basic_Memory_validators_must_be_verified_not_inferred: true
```

Future product-repo-local technical memory may include, if later approved:

- project-local `AGENTS.md`;
- project execution profile;
- validation profile;
- module map;
- public API/interface notes;
- ADRs or compact technical decisions;
- internal module documentation;
- project-scoped Codex config policy.

Requirements:

- Do not default-load full product technical context into the ChatGPT Direction Project.
- Store durable technical decisions in the product repository when that repository exists.
- Verify Task Master, Serena, Basic Memory, validators, MCP servers, and other tool bindings from the actual local/project setup before relying on them.
- Do not create `.codex/config.toml`, `AGENTS.md`, Task Master files, Serena config, or Basic Memory config in H1_G2.

## 5. Module and documentation requirements

Before durable technical nucleus implementation, the product repository should have a minimal module and documentation policy.

```yaml
module_and_documentation_requirements:
  Module_Map_required_before_durable_nucleus_implementation: true
  public_API_contract_required_per_module: true
  internal_module_documentation_policy_required: true
  dependency_direction_rules_required: true
  composition_root_DI_boundary_required: true
  exact_DI_package_deferred_to_later_evidence_or_decision: true
```

Minimum future module map fields:

- module name;
- responsibility;
- public API / contract;
- inputs and outputs;
- allowed dependencies;
- forbidden dependencies;
- validation surface;
- documentation owner/location;
- Codex slice boundaries.

Dependency rules to define later:

- Gameplay/domain logic should not depend directly on multiplayer transport unless explicitly approved.
- Core simulation/domain modules should be testable without Unity scene state where practical.
- Unity presentation and network transport should adapt to domain contracts rather than become hidden source-of-truth for domain logic.
- Composition root / dependency injection boundary must be defined before durable nucleus implementation.
- Exact DI package selection is deferred until sufficient project evidence or explicit decision.

Documentation policy:

- Public API contracts must be visible enough for bounded Codex work.
- Internal module notes should explain invariants, lifecycle, and validation expectations without becoming a large handbook.
- Game Documentation promotion remains blocked until a later documentation route explicitly authorizes it.

## 6. Codex slice contract

Future Codex product/project execution must use bounded slices.

Required slice contract:

```yaml
codex_slice_contract:
  target_module:
  allowed_files:
    - path:
  forbidden_files:
    - path:
  expected_output:
  validation:
  observable_result:
  rollback_or_stop_conditions:
```

Slice contract rules:

- `target_module` must name the module or bounded area under change.
- `allowed_files` must be exact enough for diff verification.
- `forbidden_files` must include generated/protected/scenes/prefabs/config/tool-binding files when not explicitly authorized.
- `expected_output` must be behavior- or artifact-specific, not broad implementation intent.
- `validation` must name tests, harnesses, scenes, logs, overlays, inspector checks, or manual checklist.
- `observable_result` must say what the user/reviewer can see after the slice.
- `rollback_or_stop_conditions` must stop Codex when validation, scope, tool binding, architecture reuse, or dependency assumptions fail.

## 7. Unity MCP policy

Unity MCP is deferred for H1_G2.

```yaml
unity_mcp_policy:
  status: deferred_until_H1_G3
  not_installed_or_configured_in_H1_G2: true
  not_required_for_profile_completion: true
  project_scoped_only_later: true
  trusted_project_only_later: true
  allowlist_driven_later: true
  initial_future_tier_0_read_only_inspection: true
  narrow_future_tier_1_validation_evidence_collection: true
  tier_3_scene_prefab_mutation_forbidden_by_default: true
  tier_4_code_generation_script_editing_forbidden_by_default: true
  code_changes_remain_in_normal_Codex_repo_diff_path: true
  local_tool_inventory_audit_required_before_enablement: true
  licensing_prereq_ambiguity_must_be_resolved_before_enablement: true
```

Future enablement constraints:

- Unity MCP must be evaluated only after a real project exists and a later route authorizes tool-binding readiness.
- Any enablement must be project-scoped and limited to trusted local project context.
- Operations must be allowlist-driven.
- Initial use, if approved later, should start at Tier 0 read-only inspection.
- Narrow Tier 1 validation evidence collection may be considered later.
- Scene/prefab mutation is forbidden by default.
- Code generation or script editing through Unity MCP is forbidden by default.
- Product code changes remain in the normal Codex repository diff path.
- Local tool inventory and licensing/prerequisite ambiguity must be resolved before enablement.

## 8. Stop rules

This profile does not authorize setup, implementation, or project mutation.

```yaml
stop_rules:
  no_Unity_bootstrap: true
  no_product_repo_creation: true
  no_product_code: true
  no_MCP_installation: true
  no_codex_config_creation: true
  no_AGENTS_creation: true
  no_Task_Master_graph: true
  no_internal_tool_setup: true
  no_scene_prefab_asset_script_mutation: true
  no_Codex_product_project_execution: true
  no_old_code_transfer: true
  no_old_code_audit_as_starting_point: true
  no_final_DI_package_selection: true
  no_full_engineering_handbook: true
  no_Game_Documentation_promotion: true
```

Stop and route back if a later step attempts to:

- create a Unity project before a bootstrap route authorizes it;
- create a product repository before a bootstrap route authorizes it;
- write product code before a validated execution envelope exists;
- install or configure Unity MCP in H1_G2;
- create Codex config, AGENTS.md, Task Master, Serena, or Basic Memory files without a later tool-binding route;
- mutate scenes, prefabs, assets, or scripts;
- use old code as the starting point;
- select a final DI package without evidence or decision;
- expand this profile into a full engineering handbook;
- promote content into Game Documentation without an explicit documentation route.

## 9. How later stages may use this profile

Later stages may use this profile as a compact addendum when planning H1_G3 project/bootstrap/tool-binding readiness.

They must still prove:

- basis-valid next route;
- concrete project/tool bindings;
- validation scene or harness plan;
- allowed and forbidden files;
- Codex product/project execution readiness;
- user approval where required.

This profile is complete only as a zero-state execution-readiness addendum. It is not product execution evidence.

## End-of-file marker

`END_OF_FILE: directions/indie-game-development/phases/core-coop-technical-foundation-selection/goals/codex-development-operating-model-and-architecture-protocols/01_GAS_COOP_GAME_PROJECT_EXECUTION_PROFILE.md`
