# Direction Customization Profile

status: candidate_draft

## Purpose

This file defines how a specific Direction may customize the Stage 3 operational control layer without changing the core runtime rules.

Direction customization exists because different long projects have different recurring risks.

A game development direction may need technical validation watches.

A health direction may need stale nutrition preference checks.

A workflow governance direction may need source authority checks.

Customization should reduce repeated manual explanation. It must not create hidden automation or hidden state mutation.

## Core boundary

Direction customization can tune how Signals, Handlers, Action Inbox rules, priorities and Runtime Console labels behave for a Direction.

It cannot change accepted-state rules.

It cannot make Handler output accepted.

It cannot make Action Inbox execute work automatically.

It cannot make adapters core runtime primitives.

It cannot bypass explicit Acceptance Decision.

## What may be customized

A Direction may customize:

1. custom signals
   Direction-specific facts worth noticing.

2. custom handlers
   Direction-specific candidate generators.

3. track-specific Action Inbox rules
   Rules for which items matter for a given track.

4. priority rules
   Local meaning of low, normal, high and blocking_candidate.

5. stale conditions
   Conditions that make a candidate item outdated or unsafe.

6. console views / labels
   Direction-specific labels for status views.

7. Check Job templates
   Recurring bounded checks for evidence, freshness or consistency.

8. wording preferences
   Human-readable names that make the console easier to understand.

## What must not be customized

A Direction must not customize:

1. accepted-state rules
   Accepted State still changes only through explicit acceptance/update path.

2. hidden automation
   No Handler, Signal or Action Inbox rule may silently execute work or update state.

3. adapter as core
   ChatGPT, Codex, Claude Code, Deep Research, GitHub, future AI providers and human actions remain adapters / role implementations.

4. direct state mutation by handlers
   Handler output remains candidate only.

5. evidence requirements
   A Direction may add stronger evidence rules, but cannot remove evidence required by the runtime boundary.

6. acceptance authority
   Direction customization cannot decide that a tool output is accepted by itself.

7. runtime activation
   A customization profile does not activate the candidate runtime.

## Customization proposal

A customization should be proposed when repeated friction appears.

Proposal should include:

- direction name;
- problem being solved;
- affected track or surface;
- proposed custom signals;
- proposed custom handlers;
- proposed Action Inbox rules;
- proposed priority/stale rules;
- console labels if needed;
- what remains forbidden;
- evidence that this customization is useful;
- risk of over-automation.

The proposal is candidate context until accepted.

## Customization acceptance

Customization is accepted only through explicit acceptance/update path.

Before acceptance, review must check:

- Does it preserve Direction Spine authority?
- Does it keep Active Front bounded?
- Does it avoid hidden automation?
- Does every custom Handler return candidate action only?
- Does it keep Action Inbox from becoming a trash bin?
- Does it preserve adapter boundary?
- Does it improve repeated work enough to justify extra rules?
- Is the profile still understandable to the user?

If review fails, customization should be narrowed, rejected or converted into ordinary Action Inbox items.

## Suggested profile shape

A profile can be human-readable.

YAML is not required.

Minimum practical sections:

- Direction name.
- Why customization exists.
- Custom signals.
- Custom handlers.
- Action Inbox rules.
- Priority rules.
- Stale conditions.
- Runtime Console labels.
- Forbidden automation.
- Review date or review condition.

## Example: game development direction

Direction:
  Indie Game Development.

Why customization exists:
  Game development has recurring technical/design risks that can appear before they are ready for execution.

Possible custom signals:

- game_design_risk_signal
  A design idea creates unresolved scope, player experience or mechanic consistency risk.

- technical_dependency_signal
  A technical decision depends on engine, architecture, simulation model or validation harness.

- prototype_validation_signal
  A prototype result exists but lacks playtest, runtime, screenshot or code validation evidence.

- scope_creep_signal
  The current work starts expanding from one technical nucleus into full game roadmap.

Possible custom handlers:

- game_design_risk_handler
  Creates candidate Check Job or parent review item, not a new roadmap.

- technical_dependency_handler
  Creates candidate item to verify dependency before Codex implementation.

- prototype_validation_handler
  Creates candidate validation Check Job before acceptance.

- scope_creep_handler
  Creates candidate scope split or parking item.

Track-specific Action Inbox rules:

- Technical foundation track:
  High priority for missing validation, unclear architecture boundary, forbidden path risk and Codex validation failure.

- Game design track:
  High priority for unresolved core loop contradiction or player-facing mechanic ambiguity.

- Research track:
  Stale condition triggers when evidence is old, source quality is weak or decision depends on current external facts.

Priority examples:

- blocking_candidate:
  Missing evidence prevents safe acceptance.

- high:
  Risk affects current Active Front.

- normal:
  Useful follow-up, but not blocking current work.

- low:
  Parked idea for later, with clear stale/drop rule.

Stale conditions:

- item no longer relates to current Active Front;
- accepted decision superseded it;
- evidence source became stale;
- item is duplicated by newer candidate;
- no clear when_to_run remains.

Console labels:

- "Current playable nucleus"
- "Technical validation watch"
- "Design risk watch"
- "Parked future mechanics"
- "Codex implementation readiness"

Forbidden automation:

- Do not auto-launch Codex when a technical_dependency_signal appears.
- Do not accept prototype evidence without explicit review.
- Do not move Active Front because a parked mechanic looks interesting.
- Do not turn the game direction into a global backlog.

## Good customization

Good:

- catches recurring real risks;
- creates fewer repeated explanations;
- keeps user-facing language simple;
- produces candidate actions only;
- makes stale/drop rules explicit.

## Bad customization

Bad:

- creates many custom signal types that nobody uses;
- auto-routes work;
- accepts tool output silently;
- treats Action Inbox as roadmap;
- makes every idea high priority;
- hides state changes behind Handler names.

## Review rule

If a customization profile becomes hard to explain in plain language, it is too complex.

Prefer fewer signals, fewer handlers and stronger hygiene rules.

END_OF_FILE: workflow/candidates/workflow_runtime_rebuild/DIRECTION_CUSTOMIZATION_PROFILE.md
