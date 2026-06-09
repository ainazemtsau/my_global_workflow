# Procedure Authoring Guide

status: active_procedure_framework

## Purpose

Use this guide when writing Workflow v3 procedure files. A good procedure names the work boundary, required sources, completion contract, material stages, internal checks, child/adaptor boundaries, stop conditions, and output contract.

## Canonical Procedure Location

Write procedures under:

```text
workflow_v3/procedures/**
```

Name procedure files as:

```text
*_PROCEDURE.md
```

When a detailed body is not authored yet, create a self-contained stub target spec that identifies:

```text
title:
status: stub_procedure_pending_authoring
canonical_location:
entrypoint:
kind:
procedure_boundary:
target_role:
workflow_integration:
future_body_scope:
future_body_must_not:
required_outputs_when_authored:
stop_behavior_until_authored:
completion:
  result:
  proof:
  blocked_if:
```

The registry must point to the canonical procedure file. A stub may serve as the canonical procedure source only to stop execution until a later bounded authoring run fills the detailed body.

## Write the Boundary First

Keep the trigger short and concrete. If the boundary touches accepted state, Direction runtime, Codex, Project setup, repository mutation, utility calls, or storage, say so directly.

## Required Completion Block

Every selectable procedure must include:

```text
completion:
  result:
  proof:
  blocked_if:
```

Use the procedure's own purpose and output contract as the source. Do not copy a global done list. The result must not be only a handoff, package, Codex package, check packet, storage packet, child-chat card, copy-paste packet, or `NEXT_CHAT_CARD`.

## START Output Requirements

Procedure authors must support the lifecycle START format. START must begin with a short operator-readable plain-language block before technical fields. When the operator writes Russian, use `## Коротко` first and put canonical technical fields under `## Техническая часть`. The human-facing block must state what this chat will do, why the selected procedure applies, what completion means, what the operator should review, whether this step is default/no-action or requires attention, and what happens after START / СТАРТ.

Technical START fields must include:

```text
selected_entrypoint:
selected_procedure_path:
kind:
start_goal:
terminal_condition:
completion_contract:
material_stages:
child_call_policy:
required_sources:
write_boundaries:
user_confirmation_required: START | СТАРТ
```

START must not perform material work and must not describe a package, handoff, card, or child-call envelope as the terminal condition.

## Sources

Required inputs are what the user or START must provide before RUN can proceed. Source requirements are exact files, bindings, refs, EOF checks, and authority rules that must be satisfied before material claims are made.

Good source requirement:

```text
Read exact CURRENT_STATUS.md and CURRENT_NEXT_MOVE.md through the resolved binding; verify EOF where markers exist.
```

## Context Classification

Classify input as canonical source, accepted record, current human input, verified excerpt, Project Files cache/context, candidate context, adapter evidence, historical evidence, or unknown/unverified when source or state matters.

## Stage Design

Use material stages only when the user needs to see progress or make a continuation decision. Each material stage emits `STAGE_RESULT` and waits for `CONTINUE` / `ДАЛЬШЕ` before the next material stage.

Use `internal_check` for mechanical checks inside a material stage. Internal checks do not require separate user confirmation unless they change scope, need a child call, or block.

Runtime must execute the selected procedure's declared stages. START/RUN must not invent ad hoc simple, compact, shortcut, or single-stage compression that bypasses declared stages. A procedure may define a small declared stage list, but runtime cannot merge declared stages into one undeclared stage. A declared stage may end quickly or be marked not_applicable with evidence, but it must still be represented in progression when applicable.

Good material stage:

```text
stage_id: source_check
stage_type: material stage
purpose: Confirm exact source authority before status summary.
inputs: Binding, CURRENT_STATUS.md, CURRENT_NEXT_MOVE.md.
required_stage_result: Source refs and read limitations.
gate: PASS if exact sources are available and consistent; STOP otherwise.
utility_allowed_if: exact source access requires an admitted file/GitHub utility.
blocked_if: source binding is missing or conflicting.
```

Good internal check:

```text
check_id: eof_check
stage_type: internal_check
purpose: Confirm required markdown source markers.
pass_if: required files are readable and markers match.
blocked_if: required marker is missing or source is truncated.
```

STAGE_RESULT must be operator-readable first when the stage contains material conclusions, blockers, repair needs, or child calls. When the operator writes Russian, use `## Коротко по шагу` first and `## Техническая часть` for compact fields. The human-facing block must say what was done, what was found, what the human should review, and what happens next. Technical fields follow:

```text
stage:
result:
proof:
limitations:
child_calls_opened:
child_returns_verified:
required_child_work_detected:
child_call_opened:
next_state:
next_stage_or_check:
user_confirmation_required:
```

STAGE_RESULT does not accept state, close the chat, or launch hidden child work.

## Child Procedure Calls

Research, child chats, check jobs, Codex, file/GitHub access, storage updates, human decisions, or future providers must stay subordinate to the selected procedure. They must not become independent material work, mutate state silently, accept output, or switch the selected procedure.

State allowed child/adaptor use with:

```text
child_call_policy:
  allowed_when:
  common_targets:
  forbidden_when:
  return_verification:
  same_main_procedure_resume:
```

Use `CHILD_PROCEDURE_CALL` and `CHILD_PROCEDURE_RETURN` as canonical lifecycle terms. `UTILITY_CALL` and `UTILITY_RETURN` may appear only as adapter-level compatibility aliases. `open_child_calls != empty`, a missing child return, an unverified child return, or missing required validation/evidence blocks CHECK, FINISH, and CLOSED.

Required current-goal repair has no draft-only child/adaptor mode. If a stage detects required child/adaptor repair and the parent cannot mutate directly, the stage must open `CHILD_PROCEDURE_CALL`, enter `RUN_WAITING_FOR_CHILD_RETURN`, and require matching `CHILD_PROCEDURE_RETURN` / `CODEX_RETURN_PACKET` before CONTINUE / ДАЛЬШЕ, CHECK, FINISH, or CLOSED.

## Keep Project Instructions Small

Project Instructions are bootloader-level. They may say which registry to read first and how START/RUN/CHECK/FINISH behave. They should not contain full procedures, long routing cards, or execution logic that belongs in repository procedure files.

## Keep Small Procedures Small

A small procedure can use one declared material stage, no child calls, and a compact completion contract. Do not add research, child chats, or check jobs unless the procedure genuinely needs them. A small stage list is authored in the procedure; it is not runtime compression of a larger declared stage sequence.

## NEXT_CHAT_CARD Boundary

NEXT_CHAT_CARD is post-closed continuation only. It is not a child call, not a utility launch, and not evidence that the current START goal has completed. It must not represent unfinished child work from the current START goal or replace `CHILD_PROCEDURE_CALL`.

## Authoring Quality Checks

Use these owner checks when drafting or revising a procedure:

- Define purpose, trigger, non-trigger, required inputs, source requirements, context classification, completion contract, stage model, child/adaptor policy, stop conditions, and output contract before detailed body polish.
- Keep runtime gate lenses inside the procedure; do not create a separate route controller, separate check runner, mandatory check-file loading, or hidden procedure switch.
- For non-trivial authoring, explain target identity and method/checkpoints before drafting the detailed body.
- Permit exact-source expansion or research only when it is relevant to method, source authority, or high-impact/non-obvious procedure design.
- Preserve canonical `workflow_v3/procedures/**` location and `*_PROCEDURE.md` naming unless a bounded exception is explicit.
- When authoring a stub body, extract role, integration, future scope, must-not constraints, required outputs, and STOP behavior from the self-contained stub instead of removed or obsolete sources.

END_OF_FILE: workflow_v3/procedures/PROCEDURE_AUTHORING_GUIDE.md
