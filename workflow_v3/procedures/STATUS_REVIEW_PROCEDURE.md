# Status Review Procedure

status: active_procedure

## Purpose

Use `status_review` to answer current status questions without executing material work or mutating state.

## Trigger / When to Use

- User asks for current accepted status.
- User asks what the current Next Move is.
- User asks for a read-only status review of a bound Direction/runtime state.

## When Not to Use

- Do not use to execute material work.
- Do not use to mutate repository/runtime state.
- Do not use to accept evidence or candidate output.
- Do not use to launch next work.

## Required Inputs

- direction binding or exact runtime state path when status is Direction-specific;
- status question or requested status scope.

## Source Requirements

Where Direction-specific state is relevant:

- resolve binding before status;
- read exact `CURRENT_STATUS.md`;
- read exact `CURRENT_NEXT_MOVE.md`;
- verify EOF/source integrity where markers exist.

Use exact repository/path/ref authority. Treat Project Files/Sources and chat memory as cache/context only.

## Context Classification

Classify binding and status sources as canonical repository source, accepted record, verified excerpt, Project Files cache/context, candidate context, legacy_evidence, or unknown/unverified.

## Complexity Selector

- `standard`: default.
- `checkpointed`: use only when binding/source conflicts must be surfaced before summary.
- `research_backed`: not used.
- `delegated_or_tool_mediated`: not used unless a separate check job is admitted after STOP.

## Stage Cards

```text
stage_id: binding_and_source
purpose: Resolve binding and verify exact current status sources.
activation conditions: Always when status depends on Direction/runtime state.
inputs: Direction binding or exact runtime state path.
required intermediate output: Binding source, CURRENT_STATUS ref, CURRENT_NEXT_MOVE ref, EOF/source limitations.
gate: PASS if exact sources are available and consistent; STOP if binding/source/state is missing or conflicting.
checkpoint rule: None by default.
expansion rule: Request exact binding or source path only when missing.
stop behavior: Return source/binding blocker without inventing status.
```

```text
stage_id: status_summary
purpose: Summarize accepted current status and admission need for any next action.
activation conditions: binding_and_source passes or user supplied exact verified non-Direction status source.
inputs: Verified status and next move sources.
required intermediate output: Status review output.
gate: PASS if summary is grounded in exact sources; PASS_WITH_RISK if source limitations are stated and non-blocking.
checkpoint rule: None.
expansion rule: None.
stop behavior: Return limitations and required admission path.
```

## Gate Outcomes

- `PASS`: exact sources are available, consistent, and sufficient.
- `PASS_WITH_RISK`: review is bounded but limitations must be stated.
- `STOP`: binding, source, or state is missing or conflicting.

## Optional Expansion

No expansion by default. Missing or conflicting sources require STOP or a separately admitted check/source retrieval path.

## Research Policy

External research is forbidden. Status must come from exact current repository/runtime sources or verified excerpts.

## Checkpoint Policy

No checkpoint by default. Surface binding/source conflicts before any summary.

## Output Contract

```text
status_review:
binding_source:
current_status_ref:
current_next_move_ref:
source_read_limitations:
admission_needed_for_next_action:
```

## Eval / Quality Checks

- Binding is resolved where relevant.
- Exact `CURRENT_STATUS.md` and `CURRENT_NEXT_MOVE.md` are read where relevant.
- EOF/source integrity is verified where markers exist.
- Status summary does not execute, mutate, accept, or launch work.
- Next action is framed as admission need, not hidden execution.

## Stop Conditions

- missing binding;
- unreadable required status source;
- missing EOF where required;
- conflicting status or next move state;
- user asks to execute, mutate, accept, or launch next work.

## Procedure Closure

Return the output contract with source limitations. If lifecycle FINISH is active, close through FINISH_REQUEST, FINISH_PACKET, Result Packet, and Next Move Packet.

END_OF_FILE: workflow_v3/procedures/STATUS_REVIEW_PROCEDURE.md
