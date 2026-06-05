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
procedure_class:
target_role:
workflow_integration:
future_body_outline:
required_outputs_when_authored:
stop_behavior_until_authored:
```

Procedure Definition Framework procedures should not use `*_RUNBOOK.md`, `*_PLAYBOOK.md`, or obsolete runbook/playbook directory placement unless an explicit bounded exception is justified.

## Procedure Class

Declare the registry-aligned class:

```text
procedure_class: core_material | utility_adapter | verification_adapter | storage_adapter | readonly_console
```

Class and embedded utility semantics are controlled by:

```text
workflow_v3/control_plane/UTILITY_ADAPTER_PROTOCOL.md
```

START selects one owner procedure. Embedded utility/adapter use does not select a new owner procedure.

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
procedure_class:
target_role:
workflow_integration:
future_body_outline:
required_outputs_when_authored:
stop_behavior_until_authored:
```

Stub mode must be self-contained enough to author the future procedure body without reading deleted or obsolete procedure sources. If selected for execution before authored, the procedure must STOP with `PROCEDURE_BODY_NOT_AUTHORED`.

## Context Classification

Classify relevant context as canonical source, accepted record, current human input, verified excerpt, Project Files cache/context, candidate context, adapter evidence, legacy_evidence, or unknown/unverified.

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

Use `PASS`, `PASS_WITH_RISK`, `REWORK`, `EXPAND`, `STOP`, `TRANSFER`, `RUN_EXTERNAL_HANDOFF`, and `RUN_EXTERNAL_RETURN` where applicable.

## Optional Expansion

Name any allowed research, child, check, Codex, provider, or tool-mediated expansion and its boundary.

Expansion must remain subordinate to the selected owner procedure and must not become hidden mutation, acceptance, or procedure switching.

## Research Policy

State whether research is forbidden, optional, or required, and which sources are allowed.

## Utility / Adapter Policy

Use this section when the procedure can produce utility packets, wait for external return, or use embedded verification:

```text
allowed_utility_categories:
external_handoff_policy:
external_return_policy:
embedded_verification_policy:
storage_boundary:
```

Reference `workflow_v3/control_plane/UTILITY_ADAPTER_PROTOCOL.md` for category semantics.

## External Handoff and Resume Policy

State whether the procedure may emit `RUN_EXTERNAL_HANDOFF`.

If allowed, define:

```text
external_surface:
copy_paste_packet_required:
expected_return_packet:
validation_required_before_resume:
resume_rule: resume the same selected owner procedure
```

FINISH_REQUEST must not be emitted while a required external return is pending.

## Checkpoint Policy

State when internal RUN checkpoints are required. State when no checkpoint is needed by default.

## Output Contract

```text
field:
field:
limitations:
external_handoff_status:
exact_next_move:
```

## Eval / Quality Checks

- Required sources were read or limitations stated.
- Required stages passed or stopped.
- Output satisfies downstream use.
- Procedure class matches registry metadata.
- Utility/adapter policy is explicit when the procedure can use utility categories.
- External handoff/resume policy is explicit when the procedure can wait for external return.
- Procedure path and filename follow canonical procedure location/naming policy or declare an explicit exception.
- Stub procedures include procedure class, target role, workflow integration, future body outline, required outputs, and STOP behavior.

## Stop Conditions

- Stop when ...
- Stop if a procedure preserves obsolete runbook/playbook path or naming without explicit exception.
- Stop if embedded utility use would become procedure switching, hidden mutation, hidden acceptance, or an unbounded external wait.

## Procedure Closure

Return FINISH_REQUEST when lifecycle requires FINISH, only after required external handoffs have returned, been verified, or been explicitly stopped/abandoned. Then close through FINISH_PACKET, Result Packet, and Next Move Packet after explicit FINISH.

After FINISH, the same chat must not open a new material START.

## Examples

- Good use:
- Bad use:

END_OF_FILE: workflow_v3/procedures/PROCEDURE_TEMPLATE.md
