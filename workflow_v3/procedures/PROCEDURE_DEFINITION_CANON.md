# Procedure Definition Canon

status: active_procedure_framework

## Purpose

A Workflow v3 procedure defines the work, stages, routing/dependency boundaries, output, and completion contract for one selectable main procedure or callable dependency schema.

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

Dependency calls may support the selected main procedure under `workflow_v3/control_plane/ROUTING_AND_DEPENDENCY_PROTOCOL.md`, but they always return to the same selected main procedure. Prior packet labels are unsupported; active procedure definitions use `DEPENDENCY_CALL` and `DEPENDENCY_RETURN`.

## Procedure Kind Model

Procedure files should align with the registry `kind`:

- `core` - selectable main procedure for material workflow work.
- `dependency` - dependency schema callable during RUN under a selected main/core parent; not a standalone terminal artifact.
- `verification` - dependency verification schema callable under the same parent lifecycle or admitted verification owner; not standalone package completion.
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
- `result` must not be only a handoff, package, Codex package, check packet, storage packet, dependency packet, copy-paste packet, or `NEXT_CHAT_CARD`.

Do not define a repository-wide fixed list of done or result types. The selected procedure's completion block is the authority for CHECK.

## Stage Model

Procedures may define two step types:

- `material stage` - user-visible work that emits `STAGE_RESULT` and requires user `CONTINUE` / `ДАЛЬШЕ` before the next material stage.
- `internal_check` - mechanical check inside a material stage; it does not require a separate user confirmation unless it changes scope, needs a dependency call, or blocks.

A material stage should include:

```text
stage_id:
stage_type: material stage
purpose:
inputs:
required_stage_result:
gate:
dependency_allowed_if:
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

When the operator writes Russian, START and STAGE_RESULT human-facing summaries should use the Russian operator-first shapes from the lifecycle/template files: `## Коротко` for START, `## Коротко по шагу` for STAGE_RESULT, and `## Техническая часть` for compact canonical fields. The human summary must be enough to understand the goal, result, review need, and next step without reading raw technical fields first.

## Routing / Dependency Policy

A procedure that may use dependency work should state:

```text
routing_dependency_policy:
  same_chat_allowed_work:
  allowed_dependency_types:
  code_repository_dependency_route:
  forbidden_when:
  return_verification:
  unsupported_prior_labels:
  same_main_procedure_resume:
  closure_blockers:
```

Procedure-specific dependency policy may narrow or explain dependency use. Dependency type selection and wrong-surface behavior remain in `ROUTING_AND_DEPENDENCY_PROTOCOL.md`; support dependency packet shape remains in `SUPPORT_DEPENDENCY_PROTOCOL.md`.

## Closure

Procedure closure must:

- produce or explicitly fail its `completion:` contract;
- state source limitations and unresolved gates;
- verify any required `DEPENDENCY_RETURN` before reliance;
- open `DEPENDENCY_CALL` when required dependency repair is detected and the parent cannot complete directly;
- route code/repository mutation only through `code_repository_dependency` to Codex/code assistant;
- block CHECK, FINISH, and CLOSED while `open_dependencies != empty`, a required return is missing, a required return is unverified, or required validation/evidence is missing;
- emit `CLOSURE_CHECK` against the selected completion contract;
- request FINISH only after CHECK passes or the blocked completion condition is explicit;
- include post-closed `NEXT_CHAT_CARD` when a new independent lifecycle is needed, otherwise `no_next_chat_needed` with reason;
- never start a new material lifecycle after CLOSED in the same chat.

NEXT_CHAT_CARD is post-closed continuation only. It is not a dependency call, not a support launch, and not evidence that the current START goal has completed. It must not represent unfinished dependency work needed by the current START goal.

## Definition Quality Checks

Procedure definition quality checks live in this framework and in the procedure file itself. They are internal authoring and closure checks, not a separate route authority.

- Purpose is specific and bounded; trigger, non-trigger, required inputs, source requirements, and context classification are explicit.
- Completion uses the procedure-specific `completion:` block; CHECK must not invent global done semantics or accept handoff/package/card-only outputs.
- Material stages and internal checks are distinguishable; gates have real outcomes such as PASS, PASS_WITH_RISK, REWORK, EXPAND, STOP, TRANSFER, or DEPENDENCY_CALL where applicable.
- Derived gates are generated from boundary crossings, evidence gaps, risks, or required decisions, name the blocked action, and remain internal procedure checks.
- Dependency policy is explicit where dependency work can affect completion; common dependency choices may be named without becoming an exhaustive whitelist.
- Route-changing outputs use typed packets/cards and continuation boundaries; a procedure must not create hidden route authority, switch procedures during RUN, or use `human_decision` to avoid a required packet.
- Stub procedures are self-contained, include target role, workflow integration, future body scope, required outputs, and STOP behavior, and stop with `PROCEDURE_BODY_NOT_AUTHORED` until authored.

END_OF_FILE: workflow_v3/procedures/PROCEDURE_DEFINITION_CANON.md
