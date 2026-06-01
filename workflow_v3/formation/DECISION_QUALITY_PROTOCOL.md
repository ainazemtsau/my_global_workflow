# Decision Quality Protocol

status: active_decision_quality_protocol

## Purpose

Use this protocol when a steering entity requires a real choice rather than transcription into a template.

## Decision frame

State:

- what decision the entity controls;
- why the decision is needed now;
- what accepted state or candidate context it depends on;
- what happens if no decision is made.

## Alternatives

Normally produce 2-3 candidate alternatives before selecting one.

If only one alternative is available, state why: trivial, blocked, externally constrained, or source-limited. A no-alternatives result must carry a quality warning unless the reason is genuinely trivial.

## Criteria

Define criteria before selection. Criteria may include leverage, evidence strength, risk, constraint relief, dependency unlock, scope control, reversibility, user priority, and cost of delay.

## Evidence

Separate accepted evidence, current human input, candidate context, legacy_evidence, assumptions, and unknowns.

Evidence may support a decision, but evidence alone does not accept state.

## Tradeoffs

Show the material tradeoffs behind the selected candidate without exposing hidden chain-of-thought.

## Rejected alternatives

Record rejected or deferred alternatives and the reason for rejection or deferral.

## Acceptance question

End with an explicit question that lets the human accept, reject, repair, block, or park the candidate.

## Blocked decision

Return a blocked decision when required source, evidence, scope, authority, or human judgment is missing.

## Required output fields

```text
decision_frame:
alternatives:
criteria:
evidence_summary:
selected_candidate:
tradeoffs:
rejected_or_deferred:
blocked_if_any:
acceptance_question:
```

END_OF_FILE: workflow_v3/formation/DECISION_QUALITY_PROTOCOL.md
