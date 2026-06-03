# Chat Lifecycle Protocol Eval

status: active_eval

## Purpose

Validate that material and state-sensitive Workflow v3 chats follow START -> RUN -> FINISH.

## PASS checks

- START_PACKET appears before material RUN.
- START_PACKET selects exactly one work item.
- START_PACKET names selected_entrypoint, selected_procedure_ref, and run_surface_type.
- START_PACKET includes source_lock with EOF status for required markdown sources.
- RUN starts only after standalone user token START or СТАРТ.
- RUN executes only the procedure selected in START.
- RUN emits FINISH_REQUEST before FINISH.
- FINISH starts only after standalone user token FINISH or ФИНИШ.
- FINISH_PACKET includes finish_self_audit.
- Result Packet includes status, result, evidence, changed_files, validation, source_read_limitations, not_done, project_refresh_requirements, residual_risks, and exact_next_move.
- Event Loop Closure includes one primary_next_move.
- Typed STOP is emitted when START, RUN, or FINISH cannot proceed.

## WARN checks

- START_PACKET is present but source_lock lacks commit SHA while EOF status is present.
- FINISH_PACKET is present but residual risks are incomplete.
- User provides compound input and assistant selects one work item but deferred work is not named.

## FAIL checks

- Material work starts before START_PACKET.
- RUN starts without START or СТАРТ.
- FINISH starts without FINISH or ФИНИШ.
- START selects more than one independent work item.
- Compound input is executed without SPLIT_REQUIRED.
- RUN executes a procedure not selected in START.
- RUN switches from one steering entity to another.
- RUN mutates state without storage_update_adapter.
- Producing chat accepts its own output.
- FINISH is missing.
- FINISH_PACKET is missing finish_self_audit.
- Event Loop Closure is missing.
- exact_next_move is missing.
- Required validation is absent while result claims done.

## Required recovery action

Return repair_required and identify the first failed lifecycle state.

END_OF_FILE: workflow_v3/evals/CHAT_LIFECYCLE_PROTOCOL_EVAL.md
