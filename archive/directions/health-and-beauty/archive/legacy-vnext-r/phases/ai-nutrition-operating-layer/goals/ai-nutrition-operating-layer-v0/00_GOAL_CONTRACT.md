# Goal Contract — AI Nutrition Operating Layer v0

```yaml
goal:
  id: ai-nutrition-operating-layer-v0
  title: "Собрать AI Nutrition Operating Layer v0"
  state: active
  direction: directions/health-and-beauty
  phase: directions/health-and-beauty/phases/ai-nutrition-operating-layer
  created_by_stage: G1_GOAL_SHAPE
  created_at: "2026-05-12"
  workflow_version: vNext-R
  next_stage: E1_EXECUTION_BRIEF
```

## WHAT

Build a compact AI Nutrition Operating Layer v0: Nutrition State Packet, Active Menu object, operating modes, exception-only correction logic, recipe/prep support, review/state-update protocol, storage/save rules, restart/context-refresh rules, and sample flows.

## WHY now

The current bottleneck is not absence of one menu or MacroFactor setup. The bottleneck is absence of a stable AI process that connects menu, recipes, exceptions, daily corrections, long-term conclusions, and persistent state without heavy tracking or reliance on one long ChatGPT chat.

## DONE

A fresh next chat can use the v0 layer to handle the core nutrition scenarios:

1. Create or update menu.
2. Advise on the current day.
3. Correct the rest of the day after overeating or off-menu eating.
4. Add a recipe or prep note.
5. Run day/week summary and produce durable state-update/save output.

## Acceptance floor

The Goal is acceptable when the v0 layer includes:

- Minimal Nutrition State Packet schema.
- Minimal Active Menu object schema.
- Four operating modes:
  - Daily Nutrition Operator.
  - Menu Architect.
  - Recipe / Prep Builder.
  - Review / State Update.
- Exception-only tracking rules.
- Day-correction logic for overeating, off-menu eating, strong hunger, cravings, social meals, and menu failure.
- Storage/save protocol for durable state updates.
- Restart/context-refresh rules.
- Five sample flows for validation.
- Explicit non-goals to prevent drift into tracker/database/menu-only work.

## Validation signal

The v0 layer passes the Phase’s typical scenarios with clear inputs, outputs, exception handling, and save/update behavior.

## Validation method

Paper-test five sample flows and verify that each produces:

- user-facing answer;
- state implications;
- exception handling where relevant;
- save/update block when durable state changes.

## Smallest testable slice

One self-contained operating-layer document/packet with schemas, mode prompts, correction rules, storage protocol, restart rules, and sample flows. Missing user-specific nutrition details may remain as explicit placeholders.

## Close path

1. E1_EXECUTION_BRIEF defines minimum HOW and validation.
2. Execution builds v0.
3. R1_GOAL_REVIEW_DISTILL verifies the result and updates durable state/docs.
