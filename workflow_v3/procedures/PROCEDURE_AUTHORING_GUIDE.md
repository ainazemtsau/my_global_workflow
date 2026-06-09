# Procedure Authoring Guide

status: active_procedure_framework

## Purpose

Use this guide when writing Workflow v3 procedure files. A good procedure names the work boundary, required sources, completion contract, material stages, internal checks, routing/dependency boundaries, stop conditions, and output contract.

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
routing_dependency_policy:
required_sources:
write_boundaries:
user_confirmation_required: START | СТАРТ
```

START must not perform material work and must not describe a package, handoff, card, or dependency envelope as the terminal condition.

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

Use `internal_check` for mechanical checks inside a material stage. Internal checks do not require separate user confirmation unless they change scope, need a dependency call, or block.

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

STAGE_RESULT must be operator-readable first when the stage contains material conclusions, blockers, repair needs, or dependency calls. When the operator writes Russian, use `## Коротко по шагу` first and `## Техническая часть` for compact fields. The human-facing block must say what was done, what was found, what the human should review, and what happens next. Technical fields follow:

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

STAGE_RESULT does not accept state, close the chat, or launch hidden dependency work.

## Routing / Dependency Guidance

Use `workflow_v3/control_plane/ROUTING_AND_DEPENDENCY_PROTOCOL.md` for dependency type selection and wrong-surface behavior. Use `workflow_v3/control_plane/UTILITY_ADAPTER_PROTOCOL.md` only for non-mutating support adapter packet shape and compatibility aliases.

State the valid route first:

- same-chat non-mutating work when the selected owner can complete directly;
- `support_adapter_dependency` for non-mutating check, research, analysis, evidence, or real human decision support;
- `code_repository_dependency` through Codex/code assistant only for repository/code mutation, patching, branch creation, commits, pushes, implementation, file writes, write probes, and write validation;
- `core_lifecycle_dependency` when another registered core procedure lifecycle blocks the current RUN;
- `storage_persistence_dependency` when accepted-state persistence or update authority is the work;
- `human_decision_dependency` only for real human choices.

Add prohibitions only for real capabilities or risks in that procedure. Do not write broad negative lists that imply all providers are equivalent execution surfaces.

State dependency use with:

```text
routing_dependency_policy:
  same_chat_allowed_work:
  allowed_dependency_types:
  code_repository_dependency_route:
  forbidden_when:
  return_verification:
  compatibility_aliases:
  same_main_procedure_resume:
```

Use `DEPENDENCY_CALL` and `DEPENDENCY_RETURN` as preferred lifecycle terms. `CHILD_PROCEDURE_CALL` / `CHILD_PROCEDURE_RETURN` and `UTILITY_CALL` / `UTILITY_RETURN` may appear only as compatibility aliases or subtype labels. `open_dependencies != empty`, a missing dependency return, an unverified dependency return, or missing required validation/evidence blocks CHECK, FINISH, and CLOSED.

Required current-goal repair has no draft-only dependency mode. If a stage detects required dependency repair and the parent cannot complete directly, the stage must open `DEPENDENCY_CALL`, enter `RUN_WAITING_FOR_DEPENDENCY_RETURN`, and require matching `DEPENDENCY_RETURN` / `CODEX_RETURN_PACKET` before CONTINUE / ДАЛЬШЕ, CHECK, FINISH, or CLOSED.

## Keep Project Instructions Small

Project Instructions are bootloader-level. They may say which registry to read first and how START/RUN/CHECK/FINISH behave. They should not contain full procedures, long routing cards, or execution logic that belongs in repository procedure files.

## Keep Small Procedures Small

A small procedure can use one declared material stage, no dependencies, and a compact completion contract. Do not add support adapters, code-repository dependencies, or checks unless the procedure genuinely needs them. A small stage list is authored in the procedure; it is not runtime compression of a larger declared stage sequence.

## NEXT_CHAT_CARD Boundary

NEXT_CHAT_CARD is post-closed continuation only. It is not a dependency call, not a utility launch, and not evidence that the current START goal has completed. It must not represent unfinished dependency work from the current START goal or replace `DEPENDENCY_CALL`.

END_OF_FILE: workflow_v3/procedures/PROCEDURE_AUTHORING_GUIDE.md
