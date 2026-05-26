# 01 Phase Working Context

## Working interpretation

This Phase is not about writing one menu or creating one nutrition chat. It is about building an AI nutrition operating layer: a practical ChatGPT-based process that can handle menu planning, daily food decisions, exceptions, recipes, prep, state summaries, and context refresh.

## Core objects

- Nutrition State Packet.
- Active Menu.
- Daily Nutrition Operator.
- Menu Architect.
- Recipe / Prep Builder.
- Review / State Update.
- Storage Protocol.
- Restart / Context Refresh Rules.

## Tracking stance

Default stance: if the user eats according to the active menu, no detailed food logging is required.

Track/report only decision-useful exceptions:

- overeating;
- off-menu eating;
- sweet/craving episodes;
- strong hunger;
- social meals;
- menu failure;
- recipe/prep failure;
- adjustment needs.

## Storage stance

ChatGPT must not be the only memory layer. Meaningful sessions should produce a save/update block when durable state changes.

Save durable objects, not daily noise:

- state packet updates;
- active menu changes;
- approved recipes;
- prep notes;
- review summaries;
- rules/adjustments.

## Caution

Do not turn this Phase into:

- MacroFactor replacement by another heavy tracker;
- self-hosted tracker setup;
- perfect recipe database;
- daily food log;
- automation project;
- full nutrition redesign.
