# Procedure Registry

status: active_control_plane

## Registry

| entrypoint | procedure_ref | run_surface_type | procedure_class | embedded_use_policy | selection_hint |
| --- | --- | --- | --- | --- | --- |
| `generic_answer` | `workflow_v3/procedures/GENERIC_ANSWER_PROCEDURE.md` | `generic_answer` | `readonly_console` | `no_material_utility_by_default` | Lightweight non-state-sensitive answer. |
| `status_review` | `workflow_v3/procedures/STATUS_REVIEW_PROCEDURE.md` | `status_review` | `readonly_console` | `no_material_utility_by_default` | Current status read without executing work. |
| `direction_project_root_bootstrap` | `workflow_v3/procedures/DIRECTION_PROJECT_ROOT_BOOTSTRAP_PROCEDURE.md` | `setup_only_root_bootstrap` | `core_material` | `may_use_global_utility_layer` | Setup-only runtime root bootstrap for a future Direction. |
| `launch_direction_definition` | `workflow_v3/procedures/DIRECTION_DEFINITION_PROCEDURE.md` | `formation_chat` | `core_material` | `may_use_global_utility_layer` | Semantic Direction Definition after setup-only root. |
| `form_direction_spine` | `workflow_v3/procedures/DIRECTION_SPINE_FORMATION_PROCEDURE.md` | `formation_chat` | `core_material` | `may_use_global_utility_layer` | Candidate Direction Spine formation. |
| `form_direction_map` | `workflow_v3/procedures/DIRECTION_MAP_FORMATION_PROCEDURE.md` | `formation_chat` | `core_material` | `may_use_global_utility_layer` | Candidate Direction Map formation. |
| `form_active_front` | `workflow_v3/procedures/ACTIVE_FRONT_FORMATION_PROCEDURE.md` | `formation_chat` | `core_material` | `may_use_global_utility_layer` | Candidate Active Front selection. |
| `form_work_graph` | `workflow_v3/procedures/WORK_GRAPH_FORMATION_PROCEDURE.md` | `formation_chat` | `core_material` | `may_use_global_utility_layer` | Candidate local Work Graph formation. |
| `form_work_contract` | `workflow_v3/procedures/WORK_CONTRACT_FORMATION_PROCEDURE.md` | `formation_chat` | `core_material` | `may_use_global_utility_layer` | Candidate bounded Work Contract formation. |
| `execute_work_contract` | `workflow_v3/procedures/WORK_CONTRACT_EXECUTION_PROCEDURE.md` | `work_contract_execution` | `core_material` | `may_use_global_utility_layer` | Execute one admitted Work Contract or transfer it to an allowed surface. |
| `parent_integration_check` | `workflow_v3/procedures/PARENT_INTEGRATION_CHECK_PROCEDURE.md` | `parent_integration` | `core_material` | `may_use_global_utility_layer` | Integrate returned child/work results into parent target. |
| `impact_propagation` | `workflow_v3/procedures/IMPACT_PROPAGATION_PROCEDURE.md` | `recovery_review` | `core_material` | `may_use_global_utility_layer` | Determine impact of invalidated assumptions or changed parent context. |
| `form_current_next_move` | `workflow_v3/procedures/CURRENT_NEXT_MOVE_FORMATION_PROCEDURE.md` | `formation_chat` | `core_material` | `may_use_global_utility_layer` | Candidate Current Next Move formation. |
| `accept_candidate_entity` | `workflow_v3/procedures/ACCEPTANCE_DECISION_FORMATION_PROCEDURE.md` | `acceptance_review` | `core_material` | `may_use_global_utility_layer` | Acceptance review for candidate entity output. |
| `promote_memory_artifact` | `workflow_v3/procedures/MEMORY_ARTIFACT_PROMOTION_PROCEDURE.md` | `formation_chat` | `core_material` | `may_use_global_utility_layer` | Candidate Memory Artifact promotion. |
| `persist_accepted_state` | `workflow_v3/procedures/STORAGE_UPDATE_PROCEDURE.md` | `storage_update_adapter` | `storage_adapter` | `callable_persistence_utility_with_write_gate` | Persist accepted state from an admitted storage package. |
| `codex_handoff` | `workflow_v3/procedures/CODEX_HANDOFF_PROCEDURE.md` | `codex_handoff` | `utility_adapter` | `callable_utility` | Package bounded work for Codex. |
| `codex_result_verification` | `workflow_v3/procedures/CODEX_RESULT_VERIFICATION_PROCEDURE.md` | `codex_result_verification` | `verification_adapter` | `callable_verification_utility` | Verify returned Codex result evidence. |
| `recovery_review` | `workflow_v3/procedures/RECOVERY_REVIEW_PROCEDURE.md` | `recovery_review` | `core_material` | `may_use_global_utility_layer` | Review suspect state, evidence, or routing. |
| `author_workflow_procedure` | `workflow_v3/procedures/PROCEDURE_AUTHORING_AND_INTEGRATION_PROCEDURE.md` | `procedure_authoring` | `core_material` | `may_use_global_utility_layer` | Author or integrate Workflow v3 procedures. |

## Lookup rule

This file is the single registry/routing source. Do not create a separate procedure routing index.

START reads this registry first. Registry lookup does not execute the procedure.

START must select exactly one owner entrypoint. After selection, START reads only the selected `procedure_ref`, the matching run surface contract, and any exact required sources.

`selection_hint` must stay short. It helps select the file; it must not replace the procedure file.

If no entry matches and no bounded user request can be safely normalized into a registered entry, return `UNREGISTERED_ACTION_EXCEPTION`.

If multiple independent work items are requested, return `SPLIT_REQUIRED`.

Do not resolve by chat intuition when procedure boundaries conflict.

## Procedure Class Rule

START selects exactly one owner procedure through this registry.

`procedure_class` classifies the selected entrypoint. It does not authorize another selected procedure during RUN.

`utility_adapter`, `verification_adapter`, and `storage_adapter` entries may be selected standalone only when the user's primary work item is that adapter work.

When a core/material owner procedure uses an adapter during RUN, the adapter is a callable utility resource, utility/adapter packet, or verification schema. It is not a new selected procedure.

Core/material owner procedures may use the global utility layer through the Utility Use Gate. Registry metadata is owner selection source and boundary classification, not a call graph or utility whitelist.

`procedure_class` values, `embedded_use_policy` values, and embedded utility semantics are defined in:

```text
workflow_v3/control_plane/UTILITY_ADAPTER_PROTOCOL.md
```

Registry class metadata is for START selection and boundary checks only. It must not become a second router or a procedure call graph.

Embedded utility/adapter use during RUN does not select a new owner procedure.

## Stub Authoring Rule

Every active registry entry must point to a canonical procedure file under:

```text
workflow_v3/procedures/**
```

Unauthored or unimplemented procedure logic is represented by an explicit self-contained stub procedure with `status: stub_procedure_pending_authoring`.

Stub procedures must STOP when selected for execution. A stub must include target role, workflow integration, expected output, future body scope, and stop behavior without requiring any deleted or external procedure source.

The registry hint must not carry execution logic. Detailed procedure body authoring happens in a separate bounded `author_workflow_procedure` run based on the canonical stub target spec.

END_OF_FILE: workflow_v3/control_plane/PROCEDURE_REGISTRY.md
