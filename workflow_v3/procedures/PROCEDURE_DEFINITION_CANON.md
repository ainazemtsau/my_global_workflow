# Procedure Definition Canon

status: active_procedure_framework

## Purpose

A Workflow v3 procedure defines the work, stages, child/adaptor boundaries, output, and completion contract for one selectable main procedure or callable child/adaptor schema.

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

Child procedure calls may support the selected main procedure under `workflow_v3/control_plane/UTILITY_ADAPTER_PROTOCOL.md`, but they always return to the same selected main procedure. Adapter labels such as `UTILITY_CALL` / `UTILITY_RETURN` are compatibility names for `CHILD_PROCEDURE_CALL` / `CHILD_PROCEDURE_RETURN`.

## Procedure Kind Model

Procedure files should align with the registry `kind`:

- `core` - selectable main procedure for material workflow work.
- `utility` - child/adaptor schema callable during RUN under a selected main/core parent; not a standalone terminal artifact.
- `verification` - child/adaptor verification schema callable under the same parent lifecycle or admitted verification owner; not standalone package completion.
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
- `result` must not be only a handoff, package, Codex package, check packet, storage packet, child-chat card, copy-paste packet, or `NEXT_CHAT_CARD`.

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

Runtime must execute the selected procedure's declared stages. START/RUN must not invent ad hoc simple, compact, shortcut, or single-stage compression that bypasses declared stages. A procedure may be designed with a small declared stage list, but runtime cannot merge multiple declared stages into one undeclared stage. A declared stage may end quickly or be marked not_applicable with evidence, but it must still be represented in progression when applicable. Each material stage emits `STAGE_RESULT` and waits for CONTINUE / ДАЛЬШЕ unless the next step is `internal_check`.

## Child Call Policy

A procedure that may use child/adaptor work should state:

```text
child_call_policy:
  allowed_when:
  common_targets:
  forbidden_when:
  return_verification:
  same_main_procedure_resume:
```

Procedure-specific child-call policy may narrow or explain adapter use. Provider-neutral child-call authority remains in `UTILITY_ADAPTER_PROTOCOL.md`.

## Closure

Procedure closure must:

- produce or explicitly fail its `completion:` contract;
- state source limitations and unresolved gates;
- verify any required `CHILD_PROCEDURE_RETURN` before reliance;
- block CHECK, FINISH, and CLOSED while `open_child_calls != empty`, a required return is missing, a required return is unverified, or required validation/evidence is missing;
- emit `CLOSURE_CHECK` against the selected completion contract;
- request FINISH only after CHECK passes or the blocked completion condition is explicit;
- include post-closed `NEXT_CHAT_CARD` when a new independent lifecycle is needed, otherwise `no_next_chat_needed` with reason;
- never start a new material lifecycle after CLOSED in the same chat.

NEXT_CHAT_CARD is post-closed continuation only. It is not a child call, not a utility launch, and not evidence that the current START goal has completed. It must not represent unfinished child work needed by the current START goal.

END_OF_FILE: workflow_v3/procedures/PROCEDURE_DEFINITION_CANON.md
