# Chat Lifecycle Protocol

status: active_control_plane

## Material chat lifecycle

```text
Phase 0 Intake
Phase 1 Admission / Source Read
Phase 2 Admission Packet + Work Plan
Phase 3 Execution
Phase 4 Review / Acceptance handling
Phase 5 Persistence / Adapter Run
Phase 6 Verification
Phase 7 Closure / Transfer
```

Not every chat enters every phase. Skipped phases require reason.

## Phase rules

Phase 0 Intake:
- classify requested action, context, role, and materiality;
- normalize bounded user request into a registered entrypoint when safe.

Phase 1 Admission / Source Read:
- resolve procedure registry entry;
- read exact procedure source;
- verify source integrity and EOF status;
- identify `run_surface_type`.

Phase 2 Admission Packet + Work Plan:
- show Admission Packet and Work Plan before state-sensitive or material execution;
- default start condition for material/governance work is `user_start_required` unless the user already explicitly asked for immediate execution and the action is non-mutating.

Phase 3 Execution:
- perform only allowed operations for the admitted run surface;
- stop on boundary crossing.

Phase 4 Review / Acceptance handling:
- treat acceptance-like input as a signal unless admitted acceptance review resolves it;
- do not mutate state.

Phase 5 Persistence / Adapter Run:
- enter only through `storage_update_adapter` admission with Storage Update Package.

Phase 6 Verification:
- verify exact changed files, validation, source integrity, EOF markers, payload counts when relevant, and return fields.

Phase 7 Closure / Transfer:
- closure selects next move but does not launch it invisibly;
- provide Transition Packet or next-chat prompt when transfer is needed.

## Surface crossing

Crossing `run_surface_type` requires a new admission decision. A formation chat cannot become an acceptance review or storage update adapter by continuing the same reasoning thread.

END_OF_FILE: workflow_v3/control_plane/CHAT_LIFECYCLE_PROTOCOL.md
