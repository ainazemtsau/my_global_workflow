# Goal Contract — nutrition-project-operational-setup-v0

```yaml
artifact_control:
  artifact_name: "Goal Contract — nutrition-project-operational-setup-v0"
  schema: goal_contract.v1
  owner_layer: goal
  status: active
  direction: health-and-beauty
  phase_id: ai-nutrition-operating-layer
  goal_id: nutrition-project-operational-setup-v0
  created_by_stage: G1_GOAL_SHAPE
  created_at: "2026-05-18"
```

## Goal

**Title:** Собрать отдельный рабочий ChatGPT Project `Питание` как low-friction nutrition operating system.

## WHAT

Prepare the minimum setup package for a separate ChatGPT Project `Питание` that can operate the nutrition layer without heavy tracking.

Required operating surfaces:

1. Personal Nutrition Base:
   - baseline metrics;
   - goal;
   - activity;
   - constraints;
   - preferences;
   - kitchen tools;
   - desired tracking precision;
   - old nutrition card as input/hypothesis if available.

2. Menu / Cycle Planning:
   - menu for a food cycle;
   - shopping list;
   - recipes;
   - prep plan;
   - batch cooking;
   - storage;
   - fallback options;
   - practical execution notes.

3. Photo / Voice Tracking:
   - photo;
   - voice note;
   - short text;
   - approximate grams;
   - exact grams when available;
   - clarifying questions;
   - pending / unknown / defaulted handling;
   - confidence labels.

4. Correction Layer:
   - overeating;
   - undereating;
   - off-menu eating;
   - replacements;
   - missed prep;
   - incomplete photo/data;
   - rough correction without heavy food ledger.

5. Review / Adaptation:
   - what worked;
   - what failed;
   - what to keep/remove;
   - menu/shopping/prep/tracking adjustments;
   - durable facts to save.

6. Persistence / Sync:
   - update packet for Project `Питание`;
   - compact sync packet for GitHub / Health and Beauty workflow.

## WHY now

AI Nutrition Operating Layer v0 exists as design/protocol input, but it is not evidence that a working Project `Питание` exists. Operational setup remains required before the Phase can close.

## DONE

DONE is reached when a fresh nutrition chat can use the setup package for Project `Питание`.

Minimum DONE:

- Project Instructions drafted or ready for manual install.
- Nutrition Base / Snapshot drafted or exact missing inputs listed.
- Menu Preferences drafted or exact missing inputs listed.
- Active Cycle structure drafted.
- Tracking Protocol drafted.
- Review & Sync Protocol drafted.
- 2-3 operational dry-runs completed or paper-tested.

## Acceptance floor

A new chat inside Project `Питание` can:

- create a starter food-cycle package;
- produce shopping list and prep plan;
- accept photo/voice meal event;
- ask clarifying questions without blocking;
- handle unanswered / unknown / defaulted data;
- produce rough estimate with confidence;
- correct an exception;
- prepare review/update/sync packet.

## Validation scenarios

1. Cycle planning dry-run returns menu + shopping list + prep plan + storage + fallback rules.
2. Meal-event dry-run accepts photo/voice/text and returns rough estimate + confidence + optional question.
3. Missing-answer dry-run marks pending/unknown/defaulted and continues.
4. Review/sync dry-run returns keep/change/remove decisions and update packet.

## Scope in

- Separate Project `Питание` setup package.
- Project Instructions.
- Nutrition Base / Snapshot.
- Menu Preferences.
- Active Cycle.
- Tracking Protocol.
- Review & Sync Protocol.
- Save/update behavior.
- GitHub / Health and Beauty sync packet shape.
- Dry-runs.

## Non-goals

- Creating Project `Питание` inside G1.
- Concrete menu for tomorrow.
- Exact diet prescription.
- Clinical nutrition.
- Disease-specific diet.
- MacroFactor-centered workflow.
- Heavy calorie/macro ledger.
- Food database.
- API/import automation.
- Huge recipe vault.
- Full body-transformation plan.
- P9 Phase Close.

## Scope cuts

- No exact nutrition strategy selection in G1.
- No menu generation in G1.
- No tool/storage automation in G1.
- No research report in G1.
- No execution of the setup package in G1.

## Escalation triggers

- Clinical/disease-specific nutrition enters scope.
- E1 tries to prescribe a diet without baseline/evidence gate.
- MacroFactor/heavy tracking is revived as default.
- Storage/tool binding is assumed without verification.
- Project `Питание` is claimed installed without evidence.
- Phase close is attempted before operational dry-run evidence.

## Map binding

```yaml
initiative_id: body-transformation-20kg-strength-health
node_or_edge: n1_repair_validate_ai_nutrition_layer_v0
expected_map_delta: "Goal shaped; route moves to E1_EXECUTION_BRIEF; operational validation still pending."
why_this_goal_is_minimal: "It fills missing Project `Питание` setup using existing v0 protocol as input."
why_not_premature_or_optional_expansion: "No training/cardio/recovery, supplements, full body plan, heavy tracker, or clinical diet."
```

## Close path

1. E1_EXECUTION_BRIEF defines HOW, required context, validation, and execution topology.
2. Execution creates setup package and dry-runs.
3. R1_GOAL_REVIEW_DISTILL reviews whether the Project `Питание` setup is operational.
4. P9_PHASE_CLOSE remains blocked until Phase closure criteria are supported by evidence.

## End-of-file marker

`END_OF_FILE: directions/health-and-beauty/phases/ai-nutrition-operating-layer/goals/nutrition-project-operational-setup-v0/00_GOAL_CONTRACT.md`
