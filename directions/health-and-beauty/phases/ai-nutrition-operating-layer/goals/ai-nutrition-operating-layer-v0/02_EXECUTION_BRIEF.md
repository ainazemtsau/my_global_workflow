# E1 Execution Brief — AI Nutrition Operating Layer v0

```yaml
artifact_control:
  artifact_name: "E1 Execution Brief — AI Nutrition Operating Layer v0"
  schema: execution_brief.v1
  owner_stage: E1_EXECUTION_BRIEF
  status: formalized
  updated_at: "2026-05-13"
  direction: directions/health-and-beauty
  phase: directions/health-and-beauty/phases/ai-nutrition-operating-layer
  goal: directions/health-and-beauty/phases/ai-nutrition-operating-layer/goals/ai-nutrition-operating-layer-v0
  source_state: post_D1_architecture_decision
```

## Route decision

Selected route: `F0_FAST_DIRECT`

E1 rejects a second `D1_DEEP_RESEARCH` pass because D1 has already resolved the architecture decision for v0:

- one private ChatGPT Project `Питание`;
- short separate chats per operational episode;
- Project Instructions as durable policy layer;
- two explicit project sources: Snapshot and Current Loop;
- Memory is optional accelerator only, not source of truth;
- connectors and automation are not required for v0.

E1 selects `F0_FAST_DIRECT` because the next work is one bounded, reversible, checkable markdown artifact with an exact target path.

## F0 readiness summary

```yaml
f0_entry_from_e1:
  research_required: false
  current_external_facts_required: false
  architecture_or_tooling_decision_required: false
  graph_or_wave_planning_required: false
  multi_file_or_multi_tool_coordination_required: false
  acceptance_concrete_and_checkable: true
  exact_artifacts_and_target_paths_known: true
  validation_checks_known: true
```

## Objective for F0

Create one self-contained AI Nutrition Operating Layer v0 document that a fresh nutrition chat can use immediately.

Target artifact:

```text
directions/health-and-beauty/phases/ai-nutrition-operating-layer/goals/ai-nutrition-operating-layer-v0/03_AI_NUTRITION_OPERATING_LAYER_V0.md
```

## Required artifact substance

F0 should create a compact but usable operating-layer document with these sections:

1. Operating architecture:
   - Private ChatGPT Project `Питание`.
   - Project Instructions as policy layer.
   - Short separate chats per operational episode.
   - Snapshot and Current Loop as explicit project sources.
   - Memory as optional accelerator only.
   - Connectors and automation not required for v0.

2. Minimal Nutrition State Packet schema:
   - goal/context;
   - preferences and constraints;
   - current strategy;
   - active rules;
   - durable decisions;
   - open questions;
   - last review summary.

3. Minimal Active Menu object schema:
   - current menu;
   - substitutions;
   - prep notes;
   - failure signals;
   - update rules.

4. Four operating modes:
   - Daily Nutrition Operator.
   - Menu Architect.
   - Recipe / Prep Builder.
   - Review / State Update.

5. Exception-only tracking rules:
   - no default meal-by-meal logging;
   - report only decision-useful exceptions.

6. Day-correction logic:
   - overeating;
   - off-menu eating;
   - strong hunger;
   - cravings;
   - social meals;
   - menu failure.

7. Storage/save protocol:
   - save durable objects only;
   - produce save/update blocks when durable state changes;
   - never make one long ChatGPT chat the sole memory layer.

8. Restart/context-refresh rules:
   - how a new chat loads Snapshot and Current Loop;
   - how missing inputs are requested;
   - how updates are returned.

9. Five paper-test sample flows:
   - create/update menu;
   - advise on current day;
   - correct after overeating/off-menu eating;
   - add recipe/prep note;
   - run day/week summary and produce state-update/save block.

10. Explicit non-goals:
    - no MacroFactor-centered workflow;
    - no heavy calorie/macro ledger;
    - no tracker/database setup;
    - no API/import automation;
    - no huge recipe vault;
    - no clinical nutrition layer;
    - no menu-only artifact.

## Acceptance to validation map

| Acceptance-floor item | Artifact/check | Evidence required |
|---|---|---|
| Minimal Nutrition State Packet schema | Section `Nutrition State Packet` | Fields for current state, goals, constraints, preferences, rules, open questions, and last review. |
| Minimal Active Menu object schema | Section `Active Menu` | Fields for menu, substitutions, prep notes, failure signals, and update rules. |
| Four operating modes | Section `Operating Modes` | Daily Nutrition Operator, Menu Architect, Recipe / Prep Builder, Review / State Update. |
| Exception-only tracking rules | Section `Exception-only Tracking` | No default full food logging; only decision-useful exceptions. |
| Day-correction logic | Section `Correction Logic` | Rules for overeating, off-menu eating, strong hunger, cravings, social meals, and menu failure. |
| Storage/save protocol | Section `Storage / Save Protocol` | Durable save/update blocks for state, active menu, recipes, prep notes, and review summaries. |
| Restart/context-refresh rules | Section `Restart / Context Refresh` | Private project, short chats, Snapshot + Current Loop loading rules. |
| Five sample flows | Section `Paper-test Sample Flows` | Each flow includes input, user-facing output, state implications, exception handling, and save/update behavior. |
| Explicit non-goals | Section `Non-goals` | No tracker/database/MacroFactor/menu-only drift. |

## Scope lock

In scope:

- AI nutrition operating layer v0.
- Nutrition State Packet.
- Active Menu object.
- Daily Nutrition Operator.
- Menu Architect.
- Recipe / Prep Builder.
- Review / State Update.
- Exception-only tracking.
- Day-correction logic.
- Storage/save protocol.
- Restart/context-refresh rules.
- Five sample flows.

Out of scope:

- MacroFactor-centered workflow.
- Heavy calorie/macro ledger.
- Tracking every meal by default.
- Self-hosted tracker setup.
- API/import automation.
- Perfect Notion/Trillium/GitHub database design.
- Huge recipe vault.
- Daily food log as source of truth.
- Medical or clinical nutrition plan.
- Full health architecture redesign.
- Menu-only output.

## F0 launch constraint

Artifact formalization for `03_AI_NUTRITION_OPERATING_LAYER_V0.md` is not pre-approved by E1.

F0 must first return a Work Product Preview / Reviewable Brief. F0 may emit a non-empty repository patch for the v0 artifact only after approval in the F0 stage thread.

## Stop conditions for F0

Stop and return Context Request / Human Decision / B1_PROBLEM if:

- F0 stage prompt is missing or incomplete;
- this E1 patch has not been applied and read back;
- target artifact already exists with conflicting content;
- storage/tooling architecture is changed by the user;
- connectors, automation, database, or tracker setup becomes required;
- clinical nutrition advice enters scope;
- validation cannot be performed through the five paper-test flows.

## Expected next route after F0

After F0 creates and validates the v0 artifact, route to:

```text
R1_GOAL_REVIEW_DISTILL
```

for Goal review, durable distillation, and state/doc updates.
