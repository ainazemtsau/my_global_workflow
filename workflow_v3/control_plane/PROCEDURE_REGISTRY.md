# Procedure Registry

status: active_control_plane

## Registry

| entrypoint | procedure_ref | run_surface_type |
| --- | --- | --- |
| `generic_answer` | `workflow_v3/procedures/GENERIC_ANSWER_PROCEDURE.md` | `generic_answer` |
| `status_review` | `workflow_v3/procedures/STATUS_REVIEW_PROCEDURE.md` | `status_review` |
| `launch_direction_definition` | `workflow_v3/runbooks/DIRECTION_DEFINITION_RUNBOOK.md` | `formation_chat` |
| `form_direction_spine` | `workflow_v3/formation/DIRECTION_SPINE_FORMATION_RUNBOOK.md` | `formation_chat` |
| `form_direction_map` | `workflow_v3/formation/DIRECTION_MAP_FORMATION_RUNBOOK.md` | `formation_chat` |
| `form_active_front` | `workflow_v3/formation/ACTIVE_FRONT_FORMATION_RUNBOOK.md` | `formation_chat` |
| `form_work_graph` | `workflow_v3/formation/WORK_GRAPH_FORMATION_RUNBOOK.md` | `formation_chat` |
| `form_work_contract` | `workflow_v3/formation/WORK_CONTRACT_FORMATION_RUNBOOK.md` | `formation_chat` |
| `form_current_next_move` | `workflow_v3/formation/CURRENT_NEXT_MOVE_FORMATION_RUNBOOK.md` | `formation_chat` |
| `accept_candidate_entity` | `workflow_v3/formation/ACCEPTANCE_DECISION_FORMATION_RUNBOOK.md` | `acceptance_review` |
| `promote_memory_artifact` | `workflow_v3/formation/MEMORY_ARTIFACT_PROMOTION_RUNBOOK.md` | `formation_chat` |
| `persist_accepted_state` | `workflow_v3/control_plane/STORAGE_UPDATE_PROTOCOL.md` | `storage_update_adapter` |
| `codex_handoff` | `workflow_v3/procedures/CODEX_HANDOFF_PROCEDURE.md` | `codex_handoff` |
| `codex_result_verification` | `workflow_v3/procedures/CODEX_RESULT_VERIFICATION_PROCEDURE.md` | `codex_result_verification` |
| `recovery_review` | `workflow_v3/procedures/RECOVERY_REVIEW_PROCEDURE.md` | `recovery_review` |

## Lookup rule

If no entry matches and no bounded user request can be safely normalized into a registered entry, return `UNREGISTERED_ACTION_EXCEPTION`.

Registry lookup does not execute the procedure. It only selects exact source that must be read and verified before work.

END_OF_FILE: workflow_v3/control_plane/PROCEDURE_REGISTRY.md
