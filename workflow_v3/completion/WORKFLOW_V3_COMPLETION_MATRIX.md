# Workflow v3 Completion Matrix

status: active_repository_completion_framework

## Purpose

This matrix summarizes active Workflow v3 repository-side completion coverage after procedure-first closure simplification.

| Surface | Definition sources | Templates | Evals | Status | Notes |
| --- | --- | --- | --- | --- | --- |
| namespace/source authority | `WORKFLOW_SOURCE_OF_TRUTH.md`; `workflow_v3/README.md`; `workflow_v3/ACTIVATION_STATUS.md` | explicit no-template rule | `workflow_v3/evals/NO_HIDDEN_STATE_OR_ROUTE_EVAL.md`; source/context gate | complete | Future packages must name exact ref/path and avoid stale Project cache. |
| Procedure lifecycle | `workflow_v3/control_plane/CHAT_LIFECYCLE_PROTOCOL.md`; `workflow_v3/control_plane/CHAT_FINISH_PROTOCOL.md`; `workflow_v3/procedures/PROCEDURE_DEFINITION_CANON.md` | `workflow_v3/templates/FINISH_PACKET_TEMPLATE.md`; `workflow_v3/templates/RESULT_PACKET_TEMPLATE.md`; `workflow_v3/templates/NEXT_MOVE_PACKET_TEMPLATE.md` | `workflow_v3/evals/FINISH_PACKET_EVAL.md`; `workflow_v3/evals/NEXT_MOVE_PACKET_EVAL.md`; `workflow_v3/evals/PROCEDURE_EXECUTION_EVAL.md` | complete | START selects one procedure, RUN executes only that procedure, FINISH closes with packet trio. |
| Procedure registry | `workflow_v3/control_plane/PROCEDURE_REGISTRY.md`; `workflow_v3/control_plane/RUN_SURFACE_CONTRACTS.md` | procedure stubs under `workflow_v3/procedures/**` | `workflow_v3/evals/ACTION_ADMISSION_EVAL.md`; `workflow_v3/evals/PROCEDURE_DEFINITION_EVAL.md` | complete | Active registry refs point to canonical procedure files. |
| Direction structure | `workflow_v3/interfaces/01_DIRECTION_STRUCTURE_INTERFACE.md`; `workflow_v3/RUNTIME_MODEL.md` | `workflow_v3/templates/DIRECTION_SPINE_TEMPLATE.md`; `workflow_v3/templates/DIRECTION_MAP_TEMPLATE.md`; `workflow_v3/templates/ACTIVE_FRONT_TEMPLATE.md` | `workflow_v3/evals/DIRECTION_RUNTIME_BOOTSTRAP_EVAL.md`; direction lifecycle gate | complete | No real Direction is adopted until a later accepted package. |
| Direction Map | `workflow_v3/interfaces/02_DIRECTION_MAP_INTERFACE.md`; `workflow_v3/RUNTIME_MODEL.md` | `workflow_v3/templates/DIRECTION_MAP_TEMPLATE.md` | `workflow_v3/evals/DIRECTION_MAP_FRONT_GRAPH_EVAL.md` | complete | Future operators must keep map distinct from roadmap, backlog, Work Graph, and unreviewed task lists. |
| Active Front selection | `workflow_v3/interfaces/04_ACTIVE_FRONT_SELECTION_INTERFACE.md` | `workflow_v3/templates/ACTIVE_FRONT_TEMPLATE.md`; `workflow_v3/templates/FRONT_TEMPLATE.md` | `workflow_v3/evals/DIRECTION_MAP_FRONT_GRAPH_EVAL.md` | complete | Future selection must include map areas, evidence, rejected alternatives, exit criteria, and acceptance question. |
| Work Graph/node | `workflow_v3/interfaces/05_WORK_GRAPH_AND_NODE_INTERFACE.md` | `workflow_v3/templates/WORK_GRAPH_TEMPLATE.md`; `workflow_v3/templates/WORK_GRAPH_NODE_TEMPLATE.md`; `workflow_v3/templates/NODE_CLOSURE_SUMMARY_TEMPLATE.md`; `workflow_v3/templates/FRONT_CLOSURE_SUMMARY_TEMPLATE.md` | `workflow_v3/evals/DIRECTION_MAP_FRONT_GRAPH_EVAL.md` | complete | Future graphs must stay local to one Active Front. |
| Work Contract/Run/Result/Evidence/Acceptance | `workflow_v3/interfaces/05_WORK_GRAPH_AND_NODE_INTERFACE.md`; `workflow_v3/interfaces/08_PACKET_AND_TRANSFER_INTERFACE.md`; `workflow_v3/interfaces/10_ADAPTER_CODEX_PROVIDER_INTERFACE.md`; `workflow_v3/interfaces/12_QUALITY_RECOVERY_INTERFACE.md` | `workflow_v3/templates/WORK_CONTRACT_TEMPLATE.md`; `workflow_v3/templates/RUN_RECORD_TEMPLATE.md`; `workflow_v3/templates/RESULT_PACKET_TEMPLATE.md`; `workflow_v3/templates/EVIDENCE_RECORD_TEMPLATE.md`; `workflow_v3/templates/ACCEPTANCE_DECISION_TEMPLATE.md` | `workflow_v3/evals/CODEX_HANDOFF_RESULT_EVAL.md`; evidence gate; acceptance gate | complete | Future adapters may return evidence only; acceptance remains separate. |
| Transfer/Next Chat/Child Chat/Parent Recovery | `workflow_v3/interfaces/06_CHAT_LIFECYCLE_AND_HANDOFF_INTERFACE.md`; `workflow_v3/interfaces/08_PACKET_AND_TRANSFER_INTERFACE.md` | `workflow_v3/templates/TRANSFER_PACKET_TEMPLATE.md`; `workflow_v3/templates/NEXT_CHAT_PROMPT_TEMPLATE.md`; `workflow_v3/templates/PARENT_RECOVERY_BLOCK_TEMPLATE.md` | `workflow_v3/evals/CHAT_LIFECYCLE_HANDOFF_EVAL.md`; `workflow_v3/evals/NEXT_MOVE_PACKET_EVAL.md` | complete | Child outputs must return to parent; parent remains synthesis authority. |
| Memory | `workflow_v3/RUNTIME_MODEL.md`; `workflow_v3/interfaces/09_STORAGE_STATE_INTERFACE.md` | `workflow_v3/templates/MEMORY_CANDIDATE_TEMPLATE.md`; `workflow_v3/templates/MEMORY_ARTIFACT_TEMPLATE.md` | `workflow_v3/evals/NO_HIDDEN_STATE_OR_ROUTE_EVAL.md` | complete | Promotion must not replace canonical state or exact source reads. |
| Codex/adapters/providers | `workflow_v3/interfaces/10_ADAPTER_CODEX_PROVIDER_INTERFACE.md`; `workflow_v3/project_setup/GENERIC_AI_PROVIDER_SETUP.md` | `workflow_v3/templates/WORK_CONTRACT_TEMPLATE.md`; `workflow_v3/templates/RUN_RECORD_TEMPLATE.md`; `workflow_v3/templates/RESULT_PACKET_TEMPLATE.md`; `workflow_v3/templates/TRANSFER_PACKET_TEMPLATE.md` | `workflow_v3/evals/CODEX_HANDOFF_RESULT_EVAL.md` | complete | Future handoffs must return branch, commit/diff, validation, changed files, EOF, and refresh fields. |
| Storage and state | `workflow_v3/STORAGE_LAYOUT.md`; `workflow_v3/interfaces/09_STORAGE_STATE_INTERFACE.md` | `workflow_v3/templates/CURRENT_STATUS_TEMPLATE.md`; `workflow_v3/templates/CURRENT_NEXT_MOVE_TEMPLATE.md`; `workflow_v3/templates/DIRECTION_PROJECT_BINDING_TEMPLATE.md`; `workflow_v3/templates/DIRECTION_CONSOLE_TEMPLATE.md` | `workflow_v3/evals/STORAGE_UPDATE_PACKAGE_EVAL.md` | complete | No accepted per-Direction state is created in this slice. |
| Project setup | `workflow_v3/PROJECT_SETUP_MODEL.md`; `workflow_v3/project_setup/**` | Project setup manifests and instruction sources | `workflow_v3/evals/PROJECT_SETUP_ROLLOUT_EVAL.md`; `workflow_v3/evals/DIRECTION_PROJECT_SETUP_EVAL.md`; `workflow_v3/evals/DIRECTION_PROJECT_CONTINUATION_EVAL.md` | complete | Repository commits do not update actual Project UI or files. |
| Legacy evidence | `workflow_v3/LEGACY_EVIDENCE_POLICY.md`; `workflow_v3/adoption/LEGACY_EVIDENCE_REVIEW_TEMPLATE.md` | legacy review template | `workflow_v3/evals/LEGACY_EVIDENCE_BOUNDARY_EVAL.md` | complete | Old Direction state remains evidence only unless explicitly imported. |

## Entity coverage summary

| Entity | Coverage surface |
| --- | --- |
| Direction | Direction structure |
| Direction Runtime Root | Storage and state |
| Direction Spine | Direction structure |
| Direction Map | Direction Map |
| Candidate Active Front | Active Front selection |
| Active Front | Active Front selection |
| Work Graph | Work Graph/node |
| Work Graph Node | Work Graph/node |
| Work Contract | Work Contract/Run/Result/Evidence/Acceptance |
| Run | Work Contract/Run/Result/Evidence/Acceptance |
| FINISH_PACKET | Procedure lifecycle |
| Result Packet | Procedure lifecycle |
| Next Move Packet | Procedure lifecycle |
| Transfer Packet | Transfer/Next Chat/Child Chat/Parent Recovery |
| Check Job | Transfer/Next Chat/Child Chat/Parent Recovery |
| Acceptance Decision | Work Contract/Run/Result/Evidence/Acceptance |
| Memory Candidate | Memory |
| Memory Artifact | Memory |
| Runtime Console | Storage and state; Codex/adapters/providers |
| Adapter | Codex/adapters/providers |
| Codex Handoff | Codex/adapters/providers |
| Codex Result Verification | Codex/adapters/providers |

END_OF_FILE: workflow_v3/completion/WORKFLOW_V3_COMPLETION_MATRIX.md
