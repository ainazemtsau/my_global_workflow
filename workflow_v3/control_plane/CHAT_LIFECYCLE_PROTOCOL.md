# Chat Lifecycle Protocol

status: active_control_plane

## Authority

This file is the Workflow v3 runtime kernel for material and state-sensitive chats.

Procedure selection is owned by `workflow_v3/control_plane/PROCEDURE_REGISTRY.md`. Utility calls are governed by `workflow_v3/control_plane/UTILITY_ADAPTER_PROTOCOL.md`. Final audit is governed by `workflow_v3/control_plane/CHAT_FINISH_PROTOCOL.md`.

## State Model

```text
START -> RUN -> CHECK -> FINISH -> CLOSED
RUN -> UTILITY -> RUN
CHECK -> RUN
CHECK -> blocked escalation
FINISH -> RUN repair
FINISH -> blocked escalation
```

`UTILITY` is optional and subordinate to the selected main procedure. It never switches the selected main procedure.

## Universal Rules

- One material chat selects exactly one main procedure.
- The selected main procedure defines completion through its `completion:` block.
- Runtime executes visible material stages one at a time.
- Utility calls return to the same selected main procedure and are verified before reliance.
- CHECK compares actual result to the selected procedure completion contract.
- FINISH closes only after CHECK passes or the selected procedure's blocked completion condition is explicit.
- CLOSED chats do not start new material work.

## START

START selects and prepares the main procedure. It must not perform material work.

START must:

- classify the user request and identify one concrete work item;
- return `SPLIT_REQUIRED` if multiple independent work items are requested;
- read `PROCEDURE_REGISTRY.md` and select exactly one main procedure;
- read the selected procedure file and verify source availability;
- show a human-readable start contract;
- show the selected procedure's `completion:` contract;
- show the procedure's material stages when present;
- show allowed boundaries, including write and utility boundaries;
- wait for standalone `START` or `СТАРТ` before RUN.

START contract shape:

```text
START_CONTRACT:
  selected_entrypoint:
  selected_procedure_path:
  kind:
  task:
  completion_contract:
  material_stages:
  allowed_boundaries:
  required_sources:
  user_confirmation_required: START | СТАРТ
```

## RUN

RUN executes only the selected main procedure.

RUN must:

- execute one visible material stage at a time;
- emit `STAGE_RESULT` after each material stage;
- wait for user `CONTINUE` or `ДАЛЬШЕ` before the next material stage unless the next step is explicitly `internal_check`;
- run `internal_check` steps only as mechanical checks inside the current stage;
- keep utility calls subordinate to the same selected main procedure;
- prevent direct mutation unless the selected main procedure or a verified utility write path admits exact writes;
- avoid hidden launches, hidden acceptance, and procedure switching.

STAGE_RESULT shape:

```text
STAGE_RESULT:
  stage:
  result:
  proof:
  limitations:
  next_stage_or_check:
  user_confirmation_required:
```

## UTILITY

UTILITY is a supporting call made during RUN because the selected procedure or current stage needs help.

UTILITY must:

- state why the utility is needed;
- name the target utility or surface;
- include a complete packet or call boundary when external user action is required;
- state expected return;
- resume the same selected main procedure;
- verify returned evidence before relying on it.

Use `UTILITY_CALL` and `UTILITY_RETURN` from `UTILITY_ADAPTER_PROTOCOL.md`.

## CHECK

CHECK compares the actual result against the selected procedure's completion contract.

CLOSURE_CHECK must:

```text
CLOSURE_CHECK:
  selected_entrypoint:
  selected_procedure_path:
  completion_contract:
  actual_result:
  proof:
  gaps:
  decision: pass | return_to_run_repair | blocked
  next_action:
```

CHECK may request FINISH only when the contract is satisfied or when the selected procedure explicitly allows blocked completion. If gaps remain, return to RUN repair or blocked escalation.

## FINISH

FINISH is final audit and closure after CHECK passes or blocks according to the selected procedure.

FINISH must:

- read `CHAT_FINISH_PROTOCOL.md`;
- audit the run against START and the selected procedure completion contract;
- confirm no unresolved utility return is being relied on;
- close only if the audit passes;
- return to RUN repair or blocked escalation if the audit fails;
- include a human-readable result;
- include `NEXT_CHAT_CARD` when workflow continuation is needed, or `no_next_chat_needed` with reason.

## CLOSED

CLOSED means the material workflow chat is complete for the selected main procedure. No new material START may occur in the same chat.

A closed material workflow chat must include either:

```text
NEXT_CHAT_CARD:
  title:
  why:
  main_procedure_to_start:
  context_to_paste:
  expected_result:
  evidence_or_return_needed:
  start_instruction:
```

or:

```text
no_next_chat_needed:
  reason:
```

## STOP / Blocked Escalation

Use a blocked escalation when the lifecycle cannot safely proceed because source, boundary, utility return, validation, completion proof, or user authority is missing.

Common blocked reasons:

- `SPLIT_REQUIRED`
- `CONTEXT_REQUEST`
- `UNREGISTERED_ACTION_EXCEPTION`
- `SOURCE_AUTHORITY_CONFLICT`
- `BOUNDARY_CROSSING_STOP`
- `WRITE_NOT_ADMITTED`
- `VALIDATION_REQUIRED_STOP`
- `SOURCE_INTEGRITY_STOP`
- `UTILITY_RETURN_REQUIRED_STOP`
- `COMPLETION_CONTRACT_NOT_SATISFIED`

END_OF_FILE: workflow_v3/control_plane/CHAT_LIFECYCLE_PROTOCOL.md