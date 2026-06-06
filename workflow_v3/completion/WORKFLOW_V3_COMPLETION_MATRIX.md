# Workflow v3 Completion Matrix

status: active_completion_summary

## Purpose

This matrix summarizes repository-side Workflow v3 framework coverage under the main-procedure runtime kernel.

Completion here means repository-side framework coverage. It does not mean live Direction runtime activation, Direction adoption, legacy migration/import, Project UI update, Project Files/Sources refresh, product execution, or old Workflow OS decommission.

## Authority Coverage

| Area | Authority | Templates / Interfaces | Evals | Status | Notes |
| --- | --- | --- | --- | --- | --- |
| Namespace/source authority | `WORKFLOW_SOURCE_OF_TRUTH.md`; `workflow_v3/README.md`; `workflow_v3/ACTIVATION_STATUS.md` | no-template rule | `workflow_v3/evals/NO_HIDDEN_STATE_OR_ROUTE_EVAL.md` | repository_framework_coverage_complete | Future packages must name exact ref/path and avoid stale Project cache. |
| Procedure selection | `workflow_v3/control_plane/PROCEDURE_REGISTRY.md` | `workflow_v3/interfaces/99_COVERAGE_MATRIX.md` | `workflow_v3/evals/PROCEDURE_EXECUTION_EVAL.md` | repository_framework_coverage_complete | Registry is compact: entrypoint, procedure_path, kind, trigger. |
| Lifecycle kernel | `workflow_v3/control_plane/CHAT_LIFECYCLE_PROTOCOL.md` | `workflow_v3/templates/START_CONTRACT_TEMPLATE.md` | `workflow_v3/evals/START_CONTRACT_EVAL.md`; `workflow_v3/evals/CHAT_LIFECYCLE_PROTOCOL_EVAL.md`; `workflow_v3/evals/CHAT_LIFECYCLE_EVAL.md` | repository_framework_coverage_complete | START/RUN/UTILITY/CHECK/FINISH/CLOSED is the active runtime model. |
| Procedure completion | `workflow_v3/procedures/PROCEDURE_DEFINITION_CANON.md`; selected procedure files | `workflow_v3/procedures/PROCEDURE_TEMPLATE.md` | `workflow_v3/evals/PROCEDURE_EXECUTION_EVAL.md` | repository_framework_coverage_complete | Completion contract lives in selected procedure `completion:` block; procedure implementation status remains authoritative in the selected procedure file header; status/index consistency is validated by `workflow_v3/tools/check_procedure_status_index_sync.py`. |
| Utility calls | `workflow_v3/control_plane/UTILITY_ADAPTER_PROTOCOL.md` | `workflow_v3/interfaces/10_ADAPTER_CODEX_PROVIDER_INTERFACE.md` | `workflow_v3/evals/CHAT_LIFECYCLE_HANDOFF_EVAL.md` | repository_framework_coverage_complete | Utility calls are provider-neutral and return to same main procedure. |
| Finish and closure | `workflow_v3/control_plane/CHAT_FINISH_PROTOCOL.md` | `workflow_v3/templates/FINISH_PACKET_TEMPLATE.md` | `workflow_v3/evals/FINISH_PACKET_EVAL.md` | repository_framework_coverage_complete | FINISH closes only after CLOSURE_CHECK/audit pass. |
| Continuation | `workflow_v3/control_plane/CHAT_LIFECYCLE_PROTOCOL.md`; `workflow_v3/control_plane/CHAT_FINISH_PROTOCOL.md` | `workflow_v3/templates/NEXT_CHAT_PROMPT_TEMPLATE.md`; `workflow_v3/templates/TRANSFER_PACKET_TEMPLATE.md` | `workflow_v3/evals/NEXT_MOVE_PACKET_EVAL.md` | repository_framework_coverage_complete | Material closure includes NEXT_CHAT_CARD or no_next_chat_needed; the retained eval filename is a file reference for NEXT_CHAT_CARD checks. |
| Direction structure and storage | `workflow_v3/RUNTIME_MODEL.md`; `workflow_v3/STORAGE_LAYOUT.md`; `workflow_v3/interfaces/09_STORAGE_STATE_INTERFACE.md` | Direction/state templates under `workflow_v3/templates/**` | `workflow_v3/evals/DIRECTION_RUNTIME_BOOTSTRAP_EVAL.md`; `workflow_v3/evals/STORAGE_UPDATE_PACKAGE_EVAL.md` | repository_framework_coverage_complete | No accepted per-Direction runtime state is created in this slice. |
| Project setup | `workflow_v3/PROJECT_SETUP_MODEL.md`; `workflow_v3/project_setup/**` | Project setup manifests and instruction sources | `workflow_v3/evals/DIRECTION_PROJECT_SETUP_EVAL.md`; `workflow_v3/evals/DIRECTION_PROJECT_CONTINUATION_EVAL.md` | repository_framework_coverage_complete | Repository commits do not update actual Project UI or files; source files are canonical copy sources. |
| Legacy evidence | `workflow_v3/LEGACY_EVIDENCE_POLICY.md`; `workflow_v3/adoption/LEGACY_EVIDENCE_REVIEW_TEMPLATE.md` | legacy review template | `workflow_v3/evals/LEGACY_EVIDENCE_BOUNDARY_EVAL.md` | repository_framework_coverage_complete | Old Direction state remains evidence only unless explicitly reviewed and accepted through a future package. |

## Removed Authority

The active architecture has no separate start protocol, before-action protocol, or old operation-surface contract. Runtime authority is consolidated in `CHAT_LIFECYCLE_PROTOCOL.md`.

## Completion Rule

CHECK compares actual result to the selected procedure completion contract. No global fixed list of done/result types is defined here.

END_OF_FILE: workflow_v3/completion/WORKFLOW_V3_COMPLETION_MATRIX.md
