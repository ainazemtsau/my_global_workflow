# Workflow v3 Repository Completion Matrix

status: active_repository_completion_framework

## Purpose

This matrix shows that the repository-side Workflow v3 framework has canonical definitions, storage/no-storage rules, templates/no-template rules, lifecycle handling, packet boundaries, acceptance/update rules, validation/eval gates, runbooks, Project setup impact classification, and completion coverage.

Completion here means repository documentation/setup readiness only. It does not create accepted per-Direction runtime state.

## Surface matrix

| Surface | Canonical file(s) | Required templates | Runbook/protocol file | Validation/eval gate | Completion status | Unresolved risk |
| --- | --- | --- | --- | --- | --- | --- |
| namespace/source authority | `WORKFLOW_SOURCE_OF_TRUTH.md`; `README.md`; `workflow_v3/README.md`; `directions_v3/README.md`; `workflow_v3/ACTIVATION_STATUS.md` | explicit no-template rule | `workflow_v3/runbooks/PROJECT_SETUP_ROLLOUT_RUNBOOK.md` | `workflow_v3/evals/NO_HIDDEN_STATE_OR_ROUTE_EVAL.md`; source/context gate | complete | Future packages must name exact ref/path and avoid stale Project cache. |
| Direction structure | `workflow_v3/interfaces/01_DIRECTION_STRUCTURE_INTERFACE.md`; `workflow_v3/RUNTIME_MODEL.md` | `workflow_v3/templates/DIRECTION_SPINE_TEMPLATE.md`; `workflow_v3/templates/DIRECTION_MAP_TEMPLATE.md`; `workflow_v3/templates/ACTIVE_FRONT_TEMPLATE.md` | `workflow_v3/runbooks/DIRECTION_BOOTSTRAP_RUNBOOK.md`; `workflow_v3/runbooks/DIRECTION_SPINE_CHAT_RUNBOOK.md` | `workflow_v3/evals/DIRECTION_RUNTIME_BOOTSTRAP_EVAL.md`; direction lifecycle gate | complete | No real Direction is adopted until a later accepted package. |
| Direction Map | `workflow_v3/interfaces/02_DIRECTION_MAP_INTERFACE.md`; `workflow_v3/RUNTIME_MODEL.md` | `workflow_v3/templates/DIRECTION_MAP_TEMPLATE.md` | `workflow_v3/runbooks/DIRECTION_MAP_CHAT_RUNBOOK.md` | `workflow_v3/evals/DIRECTION_MAP_FRONT_GRAPH_EVAL.md` | complete | Future operators must keep map distinct from roadmap, backlog, Work Graph, and Action Inbox. |
| lifecycle signals/handlers | `workflow_v3/interfaces/03_DIRECTION_LIFECYCLE_SIGNAL_INTERFACE.md`; `workflow_v3/SIGNALS_HANDLERS_ACTION_INBOX.md` | `workflow_v3/templates/SIGNAL_RECORD_TEMPLATE.md`; `workflow_v3/templates/HANDLER_RESULT_TEMPLATE.md` | `workflow_v3/runbooks/EVENT_LOOP_CLOSURE_RUNBOOK.md`; `workflow_v3/runbooks/RUNTIME_CONSOLE_RUNBOOK.md` | `workflow_v3/evals/SIGNAL_HANDLER_LIFECYCLE_EVAL.md` | complete | Handler outputs remain candidate; future persistence needs accepted update path. |
| Active Front selection | `workflow_v3/interfaces/04_ACTIVE_FRONT_SELECTION_INTERFACE.md` | `workflow_v3/templates/ACTIVE_FRONT_TEMPLATE.md`; `workflow_v3/templates/FRONT_TEMPLATE.md` | `workflow_v3/runbooks/ACTIVE_FRONT_SELECTION_RUNBOOK.md` | `workflow_v3/evals/DIRECTION_MAP_FRONT_GRAPH_EVAL.md` | complete | Future selection must include map areas, evidence, rejected alternatives, exit criteria, and acceptance question. |
| Work Graph/node | `workflow_v3/interfaces/05_WORK_GRAPH_AND_NODE_INTERFACE.md` | `workflow_v3/templates/WORK_GRAPH_TEMPLATE.md`; `workflow_v3/templates/WORK_GRAPH_NODE_TEMPLATE.md`; `workflow_v3/templates/NODE_CLOSURE_SUMMARY_TEMPLATE.md`; `workflow_v3/templates/FRONT_CLOSURE_SUMMARY_TEMPLATE.md` | `workflow_v3/runbooks/WORK_GRAPH_OPENING_RUNBOOK.md` | `workflow_v3/evals/DIRECTION_MAP_FRONT_GRAPH_EVAL.md` | complete | Future graphs must stay local to one Active Front. |
| Work Contract/Run/Result/Evidence/Acceptance | `workflow_v3/interfaces/05_WORK_GRAPH_AND_NODE_INTERFACE.md`; `workflow_v3/interfaces/08_PACKET_AND_TRANSFER_INTERFACE.md`; `workflow_v3/interfaces/10_ADAPTER_CODEX_PROVIDER_INTERFACE.md`; `workflow_v3/interfaces/12_QUALITY_RECOVERY_INTERFACE.md` | `workflow_v3/templates/WORK_CONTRACT_TEMPLATE.md`; `workflow_v3/templates/RUN_RECORD_TEMPLATE.md`; `workflow_v3/templates/RESULT_PACKET_TEMPLATE.md`; `workflow_v3/templates/EVIDENCE_RECORD_TEMPLATE.md`; `workflow_v3/templates/ACCEPTANCE_DECISION_TEMPLATE.md` | `workflow_v3/runbooks/WORK_CONTRACT_RUNBOOK.md`; `workflow_v3/runbooks/CODEX_HANDOFF_VERIFICATION_RUNBOOK.md` | `workflow_v3/evals/CODEX_HANDOFF_RESULT_EVAL.md`; evidence gate; acceptance gate | complete | Future adapters may return evidence only; acceptance remains separate. |
| Memory | `workflow_v3/RUNTIME_MODEL.md`; `workflow_v3/interfaces/09_STORAGE_STATE_INTERFACE.md` | `workflow_v3/templates/MEMORY_CANDIDATE_TEMPLATE.md`; `workflow_v3/templates/MEMORY_ARTIFACT_TEMPLATE.md` | `workflow_v3/runbooks/EVENT_LOOP_CLOSURE_RUNBOOK.md` | `workflow_v3/evals/NO_HIDDEN_STATE_OR_ROUTE_EVAL.md` | complete | Promotion must not replace canonical state or exact source reads. |
| Action Inbox/Check Jobs/Event Loop Closure/Progression Router | `workflow_v3/interfaces/07_EVENT_LOOP_AND_ROUTING_INTERFACE.md`; `workflow_v3/SIGNALS_HANDLERS_ACTION_INBOX.md` | `workflow_v3/templates/ACTION_INBOX_ITEM_TEMPLATE.md`; `workflow_v3/templates/CHECK_JOB_TEMPLATE.md`; `workflow_v3/templates/EVENT_LOOP_CLOSURE_TEMPLATE.md`; `workflow_v3/templates/PROGRESSION_ROUTER_RESULT_TEMPLATE.md`; `workflow_v3/templates/CURRENT_NEXT_MOVE_TEMPLATE.md` | `workflow_v3/runbooks/EVENT_LOOP_CLOSURE_RUNBOOK.md`; `workflow_v3/runbooks/RUNTIME_CONSOLE_RUNBOOK.md` | `workflow_v3/evals/SIGNAL_HANDLER_LIFECYCLE_EVAL.md`; `workflow_v3/evals/NO_HIDDEN_STATE_OR_ROUTE_EVAL.md` | complete | Router selects one primary next move; it cannot execute or accept it. |
| Transition/Next Chat/Child Chat/Parent Recovery | `workflow_v3/interfaces/06_CHAT_LIFECYCLE_AND_HANDOFF_INTERFACE.md`; `workflow_v3/interfaces/08_PACKET_AND_TRANSFER_INTERFACE.md` | `workflow_v3/templates/TRANSITION_PACKET_TEMPLATE.md`; `workflow_v3/templates/NEXT_CHAT_PROMPT_TEMPLATE.md`; `workflow_v3/templates/PARENT_RECOVERY_BLOCK_TEMPLATE.md` | `workflow_v3/runbooks/PARENT_CHILD_CHAT_RUNBOOK.md`; `workflow_v3/runbooks/EVENT_LOOP_CLOSURE_RUNBOOK.md` | `workflow_v3/evals/CHAT_LIFECYCLE_HANDOFF_EVAL.md` | complete | Child outputs must return to parent; parent remains synthesis authority. |
| Codex/adapters/providers | `workflow_v3/interfaces/10_ADAPTER_CODEX_PROVIDER_INTERFACE.md`; `workflow_v3/project_setup/GENERIC_AI_PROVIDER_SETUP.md` | `workflow_v3/templates/WORK_CONTRACT_TEMPLATE.md`; `workflow_v3/templates/RUN_RECORD_TEMPLATE.md`; `workflow_v3/templates/RESULT_PACKET_TEMPLATE.md`; `workflow_v3/templates/TRANSITION_PACKET_TEMPLATE.md` | `workflow_v3/runbooks/CODEX_HANDOFF_VERIFICATION_RUNBOOK.md`; `workflow_v3/runbooks/WORK_CONTRACT_RUNBOOK.md` | `workflow_v3/evals/CODEX_HANDOFF_RESULT_EVAL.md` | complete | Future handoffs must return branch, commit/diff, validation, changed files, EOF, and refresh fields. |
| storage layout | `workflow_v3/STORAGE_LAYOUT.md`; `workflow_v3/interfaces/09_STORAGE_STATE_INTERFACE.md` | runtime state templates in `workflow_v3/templates/**` | `workflow_v3/runbooks/DIRECTION_BOOTSTRAP_RUNBOOK.md` | `workflow_v3/evals/DIRECTION_RUNTIME_BOOTSTRAP_EVAL.md` | complete | Future runtime roots require explicit adoption and must not be created by shared docs. |
| clean-start adoption | `workflow_v3/LEGACY_EVIDENCE_POLICY.md`; `workflow_v3/adoption/README.md`; adoption templates under `workflow_v3/adoption/**` | `workflow_v3/adoption/CLEAN_START_DIRECTION_ADOPTION_PACKAGE_TEMPLATE.md`; `workflow_v3/adoption/DIRECTION_RUNTIME_ROOT_MANIFEST_TEMPLATE.md`; `workflow_v3/adoption/DIRECTION_BOOTSTRAP_DECISION_TEMPLATE.md`; `workflow_v3/adoption/ADOPTION_RESULT_PACKET_TEMPLATE.md` | `workflow_v3/runbooks/DIRECTION_BOOTSTRAP_RUNBOOK.md` | `workflow_v3/evals/DIRECTION_RUNTIME_BOOTSTRAP_EVAL.md`; `workflow_v3/evals/LEGACY_EVIDENCE_BOUNDARY_EVAL.md` | complete | Later adoption can decide clean-start state only; import/bridge requires explicit package. |
| Project setup sources | `workflow_v3/PROJECT_SETUP_MODEL.md`; `workflow_v3/project_setup/CHATGPT_PROJECT_CREATION_GUIDE.md`; Project Instructions source files | `workflow_v3/project_setup/PROJECT_FILES_MANIFEST_TEMPLATE.md` | `workflow_v3/runbooks/PROJECT_SETUP_ROLLOUT_RUNBOOK.md` | `workflow_v3/evals/PROJECT_SETUP_ROLLOUT_EVAL.md` | complete | Repository commit is not an actual Project UI update. |
| Project Files/Sources manifest | `workflow_v3/project_setup/PROJECT_FILES_MANIFEST_TEMPLATE.md`; `workflow_v3/interfaces/11_PROJECT_SETUP_CONTEXT_INTERFACE.md` | manifest template only | `workflow_v3/runbooks/PROJECT_SETUP_ROLLOUT_RUNBOOK.md` | `workflow_v3/evals/PROJECT_SETUP_ROLLOUT_EVAL.md` | complete | Project Files/Sources remain cache/context and require separate refresh authorization. |
| project packs source model | `workflow_v3/project_packs/README.md` | explicit no-template rule for generated packs in this package | `workflow_v3/runbooks/PROJECT_SETUP_ROLLOUT_RUNBOOK.md` | `workflow_v3/evals/PROJECT_SETUP_ROLLOUT_EVAL.md` | complete | No generated upload packs are created or uploaded. |
| quality/evals/recovery | `workflow_v3/QUALITY_AND_RECOVERY.md`; `workflow_v3/interfaces/12_QUALITY_RECOVERY_INTERFACE.md`; `workflow_v3/evals/**` | explicit no-template rule for evals; records use relevant templates | `workflow_v3/runbooks/EVENT_LOOP_CLOSURE_RUNBOOK.md`; targeted runbooks in `workflow_v3/runbooks/**` | all files under `workflow_v3/evals/**` | complete | Future packages must run applicable gates before done claims. |
| rollout boundaries | `workflow_v3/ACTIVATION_STATUS.md`; `workflow_v3/PROJECT_SETUP_MODEL.md`; `workflow_v3/interfaces/13_PARALLEL_WORKSTREAM_BRANCH_POLICY.md` | explicit no-template rule | `workflow_v3/runbooks/PROJECT_SETUP_ROLLOUT_RUNBOOK.md`; `workflow_v3/runbooks/CODEX_HANDOFF_VERIFICATION_RUNBOOK.md` | `workflow_v3/evals/PROJECT_SETUP_ROLLOUT_EVAL.md`; rollback/coexistence gate | complete | Actual rollout remains a later bounded package. |
| legacy evidence boundary | `workflow_v3/LEGACY_EVIDENCE_POLICY.md`; `workflow_v3/interfaces/12_QUALITY_RECOVERY_INTERFACE.md`; `WORKFLOW_SOURCE_OF_TRUTH.md` | `workflow_v3/adoption/LEGACY_EVIDENCE_REVIEW_TEMPLATE.md` | `workflow_v3/runbooks/DIRECTION_BOOTSTRAP_RUNBOOK.md` | `workflow_v3/evals/LEGACY_EVIDENCE_BOUNDARY_EVAL.md` | complete | Old Direction files remain `legacy_evidence`, not accepted v3 state. |

## Entity coverage crosswalk

Each registry entity is covered by the matrix surfaces above.

| Registry entity | Matrix surface |
| --- | --- |
| Direction | Direction structure; clean-start adoption |
| Direction Runtime Root | storage layout; clean-start adoption |
| Direction Spine | Direction structure |
| Direction Map | Direction Map |
| Track | Direction Map |
| Map Area | Direction Map; Active Front selection |
| Strategic Dependency | Direction Map |
| Strategic Uncertainty | Direction Map |
| Candidate Active Front | Active Front selection |
| Active Front | Active Front selection |
| Front Exit Criteria | Active Front selection; Work Graph/node |
| Work Graph | Work Graph/node |
| Work Graph Node | Work Graph/node |
| Node Closure | Work Graph/node |
| Work Contract | Work Contract/Run/Result/Evidence/Acceptance |
| Run | Work Contract/Run/Result/Evidence/Acceptance |
| Result Packet | Work Contract/Run/Result/Evidence/Acceptance |
| Evidence | Work Contract/Run/Result/Evidence/Acceptance |
| Acceptance Decision | Work Contract/Run/Result/Evidence/Acceptance |
| Accepted State | storage layout; Work Contract/Run/Result/Evidence/Acceptance |
| Memory Candidate | Memory |
| Memory Artifact | Memory |
| Signal | lifecycle signals/handlers; Action Inbox/Check Jobs/Event Loop Closure/Progression Router |
| Lifecycle Signal | lifecycle signals/handlers |
| Handler | lifecycle signals/handlers |
| Action Inbox Item | Action Inbox/Check Jobs/Event Loop Closure/Progression Router |
| Check Job | Action Inbox/Check Jobs/Event Loop Closure/Progression Router |
| Event Loop Closure | Action Inbox/Check Jobs/Event Loop Closure/Progression Router |
| Progression Router Result | Action Inbox/Check Jobs/Event Loop Closure/Progression Router |
| Next Move | Action Inbox/Check Jobs/Event Loop Closure/Progression Router |
| Transition Packet | Transition/Next Chat/Child Chat/Parent Recovery |
| Next Chat Prompt | Transition/Next Chat/Child Chat/Parent Recovery |
| Child Chat | Transition/Next Chat/Child Chat/Parent Recovery |
| Parent Chat | Transition/Next Chat/Child Chat/Parent Recovery |
| Runtime Console | Action Inbox/Check Jobs/Event Loop Closure/Progression Router; Codex/adapters/providers |
| Adapter | Codex/adapters/providers |
| Codex Handoff | Codex/adapters/providers |
| Codex Result Verification | Codex/adapters/providers |
| Project Instructions UI | Project setup sources |
| Project Files/Sources | Project Files/Sources manifest |
| Request-only Sources | Project Files/Sources manifest |
| legacy_evidence | legacy evidence boundary |

END_OF_FILE: workflow_v3/completion/WORKFLOW_V3_COMPLETION_MATRIX.md
