# Procedure Authoring Guide

status: active_procedure_framework

## Purpose

Use this guide when writing Workflow v3 procedure files. A good procedure is neither rigid micro-steps nor a vague "do well" instruction. It names the work boundary, required sources, material stages, gates, allowed expansion, stop conditions, and output contract.

## Canonical procedure location and naming

Write Procedure Definition Framework procedures under:

```text
workflow_v3/procedures/**
```

Name procedure files as:

```text
*_PROCEDURE.md
```

Do not preserve `*_RUNBOOK.md`, `*_PLAYBOOK.md`, or obsolete runbook/playbook directory placement as active procedure source.

When a detailed body is not authored yet, create a self-contained stub target spec that identifies:

```text
procedure_path:
registry_entrypoint:
registry_delta:
target_role:
workflow_integration:
future_body_outline:
required_outputs_when_authored:
stop_behavior_until_authored:
exception_if_not_canonical:
```

The registry must point to the canonical procedure file. A stub may serve as the canonical procedure source only to stop execution until a later bounded authoring run fills the detailed body.

A compatibility shim is allowed only when explicitly justified and separately admitted. It must not become controlling procedure source.

## Write the boundary first

Keep the trigger short:

- Good: "Use for current status questions without executing material work."
- Bad: "Use whenever the user asks anything about the project."

Keep the non-trigger equally clear:

- Good: "Do not use to accept candidate output or mutate state."
- Bad: "Do not use for inappropriate situations."

If the boundary touches accepted state, Direction runtime, Codex, Project setup, or repository mutation, say so directly.

## Required inputs and sources

Required inputs are what the user or START must provide before RUN can proceed.

Source requirements are exact files, bindings, refs, EOF checks, and authority rules that must be satisfied before material claims are made.

Good source requirement:

```text
Read exact CURRENT_STATUS.md and CURRENT_NEXT_MOVE.md through the resolved binding; verify EOF where markers exist.
```

Bad source requirement:

```text
Check the project files if useful.
```

## Context classification

Classify input as canonical source, accepted record, current human input, verified excerpt, Project Files cache/context, candidate context, legacy_evidence, or unknown/unverified when source or state matters.

Simple non-state-sensitive procedures may state that no state classification is required unless the answer becomes source-sensitive.

## Complexity selector

Choose the smallest level that works:

- `inline` for lightweight non-state-sensitive answers.
- `standard` for normal source-sensitive reads.
- `checkpointed` when later stages depend on an intermediate user-visible gate.
- `research_backed` when current external sources are needed.
- `delegated_or_tool_mediated` when child/check/Codex/provider work is needed.

Do not force a simple procedure into a complex run shape.

## Stage Cards

Stage Cards should be short and material. Each stage must produce an intermediate output and pass a gate.

Good Stage Card:

```text
stage_id: source_check
purpose: Confirm exact source authority before status summary.
activation conditions: Status depends on current runtime state.
inputs: Binding, CURRENT_STATUS.md, CURRENT_NEXT_MOVE.md.
required intermediate output: Source refs and read limitations.
gate: PASS if exact sources are available and consistent; STOP otherwise.
checkpoint rule: None by default.
expansion rule: Request exact source only if missing.
stop behavior: Return SOURCE_INTEGRITY_STOP or BINDING_CONFLICT.
```

Bad Stage Card:

```text
stage_id: do_status
purpose: Do a good status review.
gate: Make sure it is good.
```

## Gates

Material gates answer whether the stage is sufficient to continue, not whether the model feels confident.

Use real outcomes: `PASS`, `PASS_WITH_RISK`, `REWORK`, `EXPAND`, `STOP`, or `TRANSFER`.

Examples:

- `PASS if exact sources are available and agree.`
- `STOP if source binding is missing or conflicting.`
- `EXPAND only to a bounded check job when validation evidence is absent.`

## Checkpointing

Checkpoint when:

- a later stage would be wasteful without user review;
- source conflicts must be surfaced before drafting;
- research or child/check/Codex work changes the available evidence;
- a gate failure may require scope repair.

Do not checkpoint every minor stage. Ordinary checkpoints are internal RUN gates and return typed gate outputs when action is needed.

## Research and expansion

Research, child chats, check jobs, Codex, or tools must stay subordinate to the selected procedure. They must not become independent material work, mutate state, accept output, or switch the procedure.

State the allowed expansion path and stop when expansion exceeds it.

## Keep Project Instructions small

Project Instructions are bootloader-level. They may say which entrypoint to use and which registry to read first. They should not contain full procedures, long routing cards, or execution logic that belongs in repository procedure files.

## Keep simple procedures simple

A simple procedure can still use the framework with one Stage Card, one gate, no checkpoint, and a compact output contract. Do not add research, child chats, or check jobs unless the procedure genuinely needs them.

END_OF_FILE: workflow_v3/procedures/PROCEDURE_AUTHORING_GUIDE.md
