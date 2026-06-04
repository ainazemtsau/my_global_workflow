# Procedure Registry

status: active_control_plane

## Registry

| entrypoint | procedure_ref | run_surface_type | selection_hint |
| --- | --- | --- | --- |
| `generic_answer` | `workflow_v3/procedures/GENERIC_ANSWER_PROCEDURE.md` | `generic_answer` | Lightweight non-state-sensitive answer. |
| `status_review` | `workflow_v3/procedures/STATUS_REVIEW_PROCEDURE.md` | `status_review` | Current status read without executing work. |
| `direction_project_root_bootstrap` | `workflow_v3/procedures/DIRECTION_PROJECT_ROOT_BOOTSTRAP_PROCEDURE.md` | `setup_only_root_bootstrap` | Setup-only runtime root bootstrap for a future Direction. |
| `launch_direction_definition` | `workflow_v3/procedures/DIRECTION_DEFINITION_PROCEDURE.md` | `formation_chat` | Semantic Direction Definition after setup-only root. |
| `form_direction_spine` | `workflow_v3/procedures/DIRECTION_SPINE_FORMATION_PROCEDURE.md` | `formation_chat` | Candidate Direction Spine formation. |
| `form_direction_map` | `workflow_v3/procedures/DIRECTION_MAP_FORMATION_PROCEDURE.md` | `formation_chat` | Candidate Direction Map formation. |
| `form_active_front` | `workflow_v3/procedures/ACTIVE_FRONT_FORMATION_PROCEDURE.md` | `formation_chat` | Candidate Active Front selection. |
| `form_work_graph` | `workflow_v3/procedures/WORK_GRAPH_FORMATION_PROCEDURE.md` | `formation_chat` | Candidate local Work Graph formation. |
| `form_work_contract` | `workflow_v3/procedures/WORK_CONTRACT_FORMATION_PROCEDURE.md` | `formation_chat` | Candidate bounded Work Contract formation. |
| `execute_work_contract` | `workflow_v3/procedures/WORK_CONTRACT_EXECUTION_PROCEDURE.md` | `work_contract_execution` | Execute one admitted Work Contract or transfer it to an allowed surface. |
| `parent_integration_check` | `workflow_v3/procedures/PARENT_INTEGRATION_CHECK_PROCEDURE.md` | `parent_integration` | Integrate returned child/work results into parent target. |
| `impact_propagation` | `workflow_v3/procedures/IMPACT_PROPAGATION_PROCEDURE.md` | `recovery_review` | Determine impact of invalidated assumptions or changed parent context. |
| `form_current_next_move` | `workflow_v3/procedures/CURRENT_NEXT_MOVE_FORMATION_PROCEDURE.md` | `formation_chat` | Candidate Current Next Move formation. |
| `accept_candidate_entity` | `workflow_v3/procedures/ACCEPTANCE_DECISION_FORMATION_PROCEDURE.md` | `acceptance_review` | Acceptance review for candidate entity output. |
| `promote_memory_artifact` | `workflow_v3/procedures/MEMORY_ARTIFACT_PROMOTION_PROCEDURE.md` | `formation_chat` | Candidate Memory Artifact promotion. |
| `persist_accepted_state` | `workflow_v3/procedures/STORAGE_UPDATE_PROCEDURE.md` | `storage_update_adapter` | Persist accepted state from an admitted storage package. |
| `codex_handoff` | `workflow_v3/procedures/CODEX_HANDOFF_PROCEDURE.md` | `codex_handoff` | Package bounded work for Codex. |
| `codex_result_verification` | `workflow_v3/procedures/CODEX_RESULT_VERIFICATION_PROCEDURE.md` | `codex_result_verification` | Verify returned Codex result evidence. |
| `recovery_review` | `workflow_v3/procedures/RECOVERY_REVIEW_PROCEDURE.md` | `recovery_review` | Review suspect state, evidence, or routing. |
| `author_workflow_procedure` | `workflow_v3/procedures/PROCEDURE_AUTHORING_AND_INTEGRATION_PROCEDURE.md` | `procedure_authoring` | Use when creating, revising, authoring, or integrating Workflow v3 procedure definitions; non-mutating design only. |

## Lookup rule

This file is the single registry/routing source. Do not create a separate procedure routing index.

START reads this registry first. Registry lookup does not execute the procedure.

START must select exactly one entrypoint. After selection, START reads only the selected `procedure_ref`, the matching run surface contract, and any exact required sources.

`selection_hint` must stay short. It helps select the file; it must not replace the procedure file.

If no entry matches and no bounded user request can be safely normalized into a registered entry, return `UNREGISTERED_ACTION_EXCEPTION`.

If multiple independent work items are requested, return `SPLIT_REQUIRED`.

Do not resolve by chat intuition when procedure boundaries conflict.

## Stub Authoring Rule

Every active registry entry must point to a canonical procedure file under:

```text
workflow_v3/procedures/**
```

Unauthored or unimplemented procedure logic is represented by an explicit self-contained stub procedure with `status: stub_procedure_pending_authoring`.

Stub procedures must STOP when selected for execution. A stub must include target role, workflow integration, expected output, future body scope, and stop behavior without requiring any deleted or external procedure source.

The registry hint must not carry execution logic. Detailed procedure body authoring happens in a separate bounded `author_workflow_procedure` run based on the canonical stub target spec.

END_OF_FILE: workflow_v3/control_plane/PROCEDURE_REGISTRY.md
