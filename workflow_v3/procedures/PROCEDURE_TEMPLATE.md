# Procedure: <Name>

status: draft_procedure

## Canonical Location

```text
workflow_v3/procedures/<NAME>_PROCEDURE.md
```

## Registry Alignment

```text
entrypoint:
kind: core | utility | verification | storage | readonly
```

## Purpose

State the bounded work this procedure performs.

## Trigger / When to Use

- Use when ...

## When Not to Use

- Do not use when ...

## Required Inputs

- target / question / artifact:
- source refs or bindings:
- expected output:

## Source Requirements

- Exact sources to read:
- EOF or integrity checks:
- Source limitations to report:

## Completion Contract

```text
completion:
  result:
  proof:
  blocked_if:
```

The selected procedure owns these completion semantics. CHECK compares actual result to this block.

## Self-contained Stub Mode

Use this section when the detailed body is not authored yet:

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
  result: blocked stub result explaining PROCEDURE_BODY_NOT_AUTHORED
  proof: canonical stub source and target role are present
  blocked_if: selected for execution before detailed body is authored
```

Stub mode must be self-contained enough to author the future procedure body without reading removed or obsolete sources. If selected for execution before authored, the procedure must stop with `PROCEDURE_BODY_NOT_AUTHORED`.

## Context Classification

Classify relevant context as canonical source, accepted record, current human input, verified excerpt, Project Files cache/context, candidate context, adapter evidence, historical evidence, or unknown/unverified.

## Stage Model

Material stages are user-visible and run one at a time. Internal checks are mechanical checks inside a material stage.

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

```text
check_id:
stage_type: internal_check
purpose:
pass_if:
blocked_if:
```

RUN emits `STAGE_RESULT` after each material stage and waits for `CONTINUE` / `ДАЛЬШЕ` before the next material stage unless the next step is an `internal_check`.

## Utility Policy

```text
utility_policy:
  allowed_when:
  common_targets:
  forbidden_when:
  return_verification:
  same_main_procedure_resume:
```

Utility calls use `UTILITY_CALL` / `UTILITY_RETURN` and must resume this selected procedure.

## Output Contract

```text
field:
field:
limitations:
continuation:
```

## Eval / Quality Checks

- Required sources were read or limitations stated.
- Material stages emitted `STAGE_RESULT`.
- User confirmation occurred before the next material stage when required.
- Utility calls returned to the same selected procedure and were verified before reliance.
- Output satisfies the procedure's `completion:` block or names the blocker.
- `CLOSURE_CHECK` compares actual result to the selected completion block.
- Closure includes `NEXT_CHAT_CARD` when continuation is needed or `no_next_chat_needed` with reason.

## Stop Conditions

- Stop when required sources are missing or conflicting.
- Stop when requested work exceeds this procedure boundary.
- Stop when utility use would become hidden mutation, hidden acceptance, procedure switching, or unbounded wait.
- Stop when completion proof cannot be produced.

## Procedure Closure

Return `CLOSURE_CHECK` when RUN reaches completion or blocked state. Request FINISH only when the selected procedure completion contract is satisfied or explicitly blocked. After FINISH passes, the same chat is CLOSED for material work.

END_OF_FILE: workflow_v3/procedures/PROCEDURE_TEMPLATE.md
