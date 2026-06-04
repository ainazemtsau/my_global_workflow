# Procedure: <Name>

status: draft_procedure

## Status

`draft_procedure` until accepted by the relevant repository update path.

## Canonical Location

Target path:

```text
workflow_v3/procedures/<NAME>_PROCEDURE.md
```

For self-contained stubs:

```text
status: stub_procedure_pending_authoring
target_role:
workflow_integration:
future_body_outline:
required_outputs_when_authored:
stop_behavior_until_authored:
```

Procedure Definition Framework procedures should not use `*_RUNBOOK.md`, `*_PLAYBOOK.md`, or obsolete runbook/playbook directory placement unless an explicit bounded exception is justified.

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

## Self-contained Stub Mode

Use this section when the detailed body is not authored yet:

```text
status: stub_procedure_pending_authoring
target_role:
workflow_integration:
future_body_outline:
required_outputs_when_authored:
stop_behavior_until_authored:
```

Stub mode must be self-contained enough to author the future procedure body without reading deleted or obsolete procedure sources. If selected for execution before authored, the procedure must STOP with `PROCEDURE_BODY_NOT_AUTHORED`.

## Context Classification

Classify relevant context as canonical source, accepted record, current human input, verified excerpt, Project Files cache/context, candidate context, legacy_evidence, or unknown/unverified.

## Complexity Selector

- `inline`:
- `standard`:
- `checkpointed`:
- `research_backed`:
- `delegated_or_tool_mediated`:

## Stage Cards

```text
stage_id:
purpose:
activation conditions:
inputs:
required intermediate output:
gate:
checkpoint rule:
expansion rule:
stop behavior:
```

## Gate Outcomes

Use `PASS`, `PASS_WITH_RISK`, `REWORK`, `EXPAND`, `STOP`, and `TRANSFER` where applicable.

## Optional Expansion

Name any allowed research, child, check, Codex, or tool-mediated expansion and its boundary.

## Research Policy

State whether research is forbidden, optional, or required, and which sources are allowed.

## Checkpoint Policy

State when internal RUN checkpoints are required. State when no checkpoint is needed by default.

## Output Contract

```text
field:
field:
limitations:
exact_next_move:
```

## Eval / Quality Checks

- Required sources were read or limitations stated.
- Required stages passed or stopped.
- Output satisfies downstream use.
- Procedure path and filename follow canonical procedure location/naming policy or declare an explicit exception.
- Stub procedures include target role, workflow integration, future body outline, required outputs, and STOP behavior.

## Stop Conditions

- Stop when ...
- Stop if a procedure preserves obsolete runbook/playbook path or naming without explicit exception.

## Procedure Closure

Return FINISH_REQUEST when lifecycle requires FINISH, then close through FINISH_PACKET, Result Packet, and Next Move Packet after explicit FINISH.

## Examples

- Good use:
- Bad use:

END_OF_FILE: workflow_v3/procedures/PROCEDURE_TEMPLATE.md
