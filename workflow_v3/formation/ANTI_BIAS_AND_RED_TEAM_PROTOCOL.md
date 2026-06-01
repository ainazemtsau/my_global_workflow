# Anti-Bias and Red-Team Protocol

status: active_anti_bias_red_team_protocol

## Purpose

Use this protocol before returning any steering-entity candidate.

## Contradiction attack

Ask what source, accepted record, stated constraint, or user goal contradicts the candidate.

## Premortem

State how this candidate could fail after acceptance.

## What would make this wrong?

Name missing evidence, false assumptions, overbroad scope, stale context, and incentives to agree too quickly.

## User impulse and over-agreement check

Treat user phrasing as important input, not as automatic final content.

Flag when the candidate merely restates the user's first framing without alternatives, criteria, or evidence.

## Stale-context check

Do not rely on Project Files/Sources, chat memory, generated packs, or prior summaries when exact source authority is required.

## Over-planning check

Flag when the entity contains future roadmap/backlog material beyond its role.

## False-certainty check

Mark unsupported claims as `candidate`, `unresolved`, or `hypothetical`.

## Output

```text
contradictions_checked:
premortem:
what_would_make_wrong:
over_agreement_risk:
stale_context_risk:
over_planning_risk:
false_certainty_risk:
repair_or_cut:
```

END_OF_FILE: workflow_v3/formation/ANTI_BIAS_AND_RED_TEAM_PROTOCOL.md
