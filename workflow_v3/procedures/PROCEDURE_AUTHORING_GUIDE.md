# Procedure Authoring Guide

status: active_procedure_framework

## Purpose

Use this guide when writing Workflow v3 procedure files. A good procedure names the work boundary, required sources, completion contract, material stages, internal checks, utility boundaries, stop conditions, and output contract.

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

Use the procedure's own purpose and output contract as the source. Do not copy a global done list.

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

Use `internal_check` for mechanical checks inside a material stage. Internal checks do not require separate user confirmation unless they change scope, need a utility call, or block.

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

## Utility Calls

Research, child chats, check jobs, Codex, file/GitHub access, storage updates, human decisions, or future providers must stay subordinate to the selected procedure. They must not become independent material work, mutate state silently, accept output, or switch the selected procedure.

State allowed utility use with:

```text
utility_policy:
  allowed_when:
  common_targets:
  forbidden_when:
  return_verification:
  same_main_procedure_resume:
```

## Keep Project Instructions Small

Project Instructions are bootloader-level. They may say which registry to read first and how START/RUN/CHECK/FINISH behave. They should not contain full procedures, long routing cards, or execution logic that belongs in repository procedure files.

## Keep Simple Procedures Simple

A simple procedure can use one material stage, no utility calls, and a compact completion contract. Do not add research, child chats, or check jobs unless the procedure genuinely needs them.

END_OF_FILE: workflow_v3/procedures/PROCEDURE_AUTHORING_GUIDE.md
