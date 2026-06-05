# Procedure Definition Canon

status: active_procedure_framework

## Purpose

A Workflow v3 procedure defines the work, stages, utility boundaries, output, and completion contract for one selectable main procedure or callable utility.

The lifecycle selects exactly one main procedure through `workflow_v3/control_plane/PROCEDURE_REGISTRY.md`. RUN executes that selected procedure stage-by-stage. CHECK and FINISH use the selected procedure's own `completion:` block; they do not invent a global completion enum.

## Boundaries

A procedure is not:

- a prompt;
- a template;
- the registry;
- the chat lifecycle;
- acceptance by itself;
- hidden state mutation;
- permission to switch procedures during RUN.

Utility calls may support the selected main procedure under `workflow_v3/control_plane/UTILITY_ADAPTER_PROTOCOL.md`, but they always return to the same selected main procedure.

## Procedure Kind Model

Procedure files should align with the registry `kind`:

- `core` - selectable main procedure for material workflow work.
- `utility` - selectable as a utility artifact or callable during RUN.
- `verification` - selectable for verification or callable during RUN.
- `storage` - selectable for admitted bounded persistence.
- `readonly` - selectable for non-material reads or answers.

Kind does not define completion. Completion belongs to the selected procedure file.

## Required Completion Block

Every selectable procedure must include a compact block with this shape:

```text
completion:
  result:
  proof:
  blocked_if:
```

- `result` names the procedure-specific output that satisfies the procedure.
- `proof` names the evidence or checks needed to trust that output.
- `blocked_if` names the procedure-specific conditions that prevent completion.

Do not define a repository-wide fixed list of done or result types. The selected procedure's completion block is the authority for CHECK.

## Stage Model

Procedures may define two step types:

- `material stage` - user-visible work that emits `STAGE_RESULT` and requires user `CONTINUE` / `ДАЛЬШЕ` before the next material stage.
- `internal_check` - mechanical check inside a material stage; it does not require a separate user confirmation unless it changes scope, needs a utility call, or blocks.

A material stage should include:

```text
stage_id:
stage_type: material stage
purpose:
inputs:
required_stage_result:
gate:
utility_allowed_if:
blocked_if:
```

An internal check should include:

```text
check_id:
stage_type: internal_check
purpose:
pass_if:
blocked_if:
```

Runtime output should be simple `STAGE_RESULT`, not schema-heavy stage cards.

## Utility Policy

A procedure that may use utilities should state:

```text
utility_policy:
  allowed_when:
  common_targets:
  forbidden_when:
  return_verification:
  same_main_procedure_resume:
```

Procedure-specific utility policy may narrow or explain utility use. Provider-neutral utility-call authority remains in `UTILITY_ADAPTER_PROTOCOL.md`.

## Closure

Procedure closure must:

- produce or explicitly fail its `completion:` contract;
- state source limitations and unresolved gates;
- verify any required utility return before reliance;
- emit `CLOSURE_CHECK` against the selected completion contract;
- request FINISH only after CHECK passes or the blocked completion condition is explicit;
- include `NEXT_CHAT_CARD` when workflow continuation is needed, otherwise `no_next_chat_needed` with reason;
- never start a new material lifecycle after CLOSED in the same chat.

END_OF_FILE: workflow_v3/procedures/PROCEDURE_DEFINITION_CANON.md