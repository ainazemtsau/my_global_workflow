# Workflow v3 Coverage Matrix

status: interface_summary

This matrix records interface/coverage mapping only. Current procedure implementation status is authoritative only in the referenced procedure file header.

## Control Plane Coverage

| Surface | Authority | Coverage |
| --- | --- | --- |
| Procedure selection | `workflow_v3/control_plane/PROCEDURE_REGISTRY.md` | START selects exactly one main procedure from compact registry table. |
| Lifecycle kernel | `workflow_v3/control_plane/CHAT_LIFECYCLE_PROTOCOL.md` | START, declared RUN stages, RUN_WAITING_FOR_CHILD_RETURN, CHILD_RETURN_VERIFICATION, CHECK, FINISH, CLOSED. |
| Child/adaptor calls | `workflow_v3/control_plane/UTILITY_ADAPTER_PROTOCOL.md` | Provider-neutral CHILD_PROCEDURE_CALL/CHILD_PROCEDURE_RETURN, same main procedure resume, verification before reliance. |
| Finish audit | `workflow_v3/control_plane/CHAT_FINISH_PROTOCOL.md` | Final audit closes only after CHECK passes or blocked completion is explicit. |
| Procedure framework | `workflow_v3/procedures/PROCEDURE_DEFINITION_CANON.md` | Completion block, material stage, internal check, child-call policy, closure requirements. |
| Packet and transfer | `workflow_v3/interfaces/08_PACKET_AND_TRANSFER_INTERFACE.md` | START_CONTRACT, STAGE_RESULT, CHILD_PROCEDURE_CALL, CHILD_PROCEDURE_RETURN, CLOSURE_CHECK, FINISH_PACKET, post-closed NEXT_CHAT_CARD. |
| Procedure status/index sync | `workflow_v3/tools/check_procedure_status_index_sync.py` | Verifies registry entries, procedure files, status headers, and index labels remain synchronized. |
| Project setup | `workflow_v3/PROJECT_SETUP_MODEL.md`; `workflow_v3/project_setup/**` | Project Instructions source files are canonical copy sources; repository commits do not update actual Project UI. |
| Legacy evidence | `workflow_v3/LEGACY_EVIDENCE_POLICY.md`; `directions/README_LEGACY_EVIDENCE_ONLY.md`; `directions/MIGRATION_EVIDENCE_INDEX.md` | Old Direction files remain legacy_evidence only; no automatic import or discard. |

## Removed Authority

Workflow v3 lifecycle authority is consolidated in `CHAT_LIFECYCLE_PROTOCOL.md`.

No separate start protocol, before-action protocol, or old operation-surface contract is active authority.

## Required Invariants

- START selects one main procedure.
- The selected procedure owns completion through `completion:`.
- RUN emits `STAGE_RESULT` one material stage at a time.
- Child/adaptor calls use `CHILD_PROCEDURE_CALL` / `CHILD_PROCEDURE_RETURN`, enter `RUN_WAITING_FOR_CHILD_RETURN`, and resume the same main procedure after verification.
- Legacy `UTILITY_CALL` / `UTILITY_RETURN` labels are compatibility aliases only and do not define standalone completion.
- CHECK emits `CLOSURE_CHECK` against actual result and selected completion.
- FINISH closes only when audit passes.
- CLOSED includes `NEXT_CHAT_CARD` when workflow continuation is needed, otherwise `no_next_chat_needed` with reason.

END_OF_FILE: workflow_v3/interfaces/99_COVERAGE_MATRIX.md
