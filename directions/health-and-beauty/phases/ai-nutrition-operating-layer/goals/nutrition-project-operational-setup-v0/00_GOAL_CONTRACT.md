# Goal Contract — nutrition-project-operational-setup-v0

```yaml
artifact_control:
  artifact_name: "Goal Contract - Project Питание v0"
  schema: goal_contract.v1
  owner_layer: direction_goal
  status: active
  direction_path: "directions/health-and-beauty"
  phase_path: "directions/health-and-beauty/phases/ai-nutrition-operating-layer"
  goal_path: "directions/health-and-beauty/phases/ai-nutrition-operating-layer/goals/nutrition-project-operational-setup-v0"
  goal_id: nutrition-project-operational-setup-v0
  formalized_by_stage: G1_GOAL_SHAPE
  formalized_at: "2026-05-19"
  source_decision: "S3_DECIDE selected standalone repo-backed ChatGPT Project `Питание` v0"
  next_route: E1_EXECUTION_BRIEF
```

## Title

Собрать repo-backed standalone ChatGPT Project “Питание” v0 as a low-friction nutrition operating loop.

## WHAT

Create a repaired standalone ChatGPT Project package `Питание` v0 that can operate outside Workflow while using repository-backed durable state under:

```text
directions/health-and-beauty/projects/nutrition/**
```

The future execution outcome must produce a manual-install-ready Project package containing:

```text
directions/health-and-beauty/projects/nutrition/
  README.md
  CHATGPT_PROJECT_INSTRUCTIONS.md
  PROJECT_FILES_MANIFEST.md
  project_files/
    00_NUTRITION_START_HERE.md
    01_NUTRITION_BASE.md
    02_MENU_PREFERENCES.md
    03_ACTIVE_CYCLE.md
    04_TRACKING_AND_EXCEPTIONS.md
    05_REVIEW_AND_SYNC.md
  protocols/
    CODEX_SAVE_OPERATOR.md
    DRY_RUN_ACCEPTANCE.md
```

## WHY now

The active Health and Beauty initiative is outcome-first: lose approximately 20 kg and improve health, strength, appearance, energy, and routine quality through low-burden evidence-based systems. S3 selected Project `Питание` v0 as the repaired container/tool for the nutrition loop, not as the objective itself.

The current Phase remains focused on creating a convenient, evidence-aware nutrition process without heavy manual tracking. This Goal converts the selected container policy into an executable target while keeping execution out of G1.

## DONE

This Goal is complete only when a later execution/review path has produced and validated a Project `Питание` v0 package that can:

1. Start or resume from durable state.
2. Plan a current nutrition cycle/menu-default structure from baseline and preferences.
3. Process a meal/photo/voice-style event with missing-answer defaults.
4. Correct the current day after off-menu eating or overeating.
5. Perform a day/week review.
6. Emit a compact `nutrition_state_update_packet.v1`.
7. Preserve strict role boundaries:
   - Dietitian: evidence-aware nutrition guidance boundaries; no medical diagnosis or clinical protocol.
   - Menu Planner: cycle/menu/defaults/prep-note planning; no full recipe database.
   - Food Tracker: low-friction event intake, exceptions, and summaries; no heavy macro/calorie ledger by default.
   - Codex Save Operator: applies approved state-update packets to repository files and returns read-back/diff evidence; does not give nutrition advice.

## Acceptance floor

A repo-backed, manual-install-ready Project package plus three synthetic dry-runs:

1. Cycle planning / restart dry-run.
2. Meal event + exception dry-run.
3. Review + sync dry-run.

## Validation signal

A fresh Project `Питание` chat can complete the three dry-runs and produce expected outputs without knowing Workflow, and Codex Save Operator policy can save/read back state updates without interpreting nutrition content.

## Validation method

E1_EXECUTION_BRIEF defines the execution envelope, artifact surfaces, validators, and route. A later execution stage creates the package and runs the synthetic dry-runs. R1_GOAL_REVIEW_DISTILL may review completion only after dry-run evidence exists.

## Smallest testable slice

One install-ready Project package plus three synthetic dry-runs plus save/read-back protocol. No live user diet, no actual menu deployment, no Project UI installation, and no required usage trial.

## Scope in

- Repaired standalone Project `Питание` v0 package.
- Minimum complete v0 nutrition loop.
- Strict role boundaries.
- Strict repository folder/file structure.
- Project Files set for the standalone ChatGPT Project.
- Codex Save Operator protocol at policy level.
- Dry-run acceptance floor.

## Non-goals

- Actual diet/menu generation for the user.
- Installing/configuring the ChatGPT Project UI.
- Running E1 inside G1.
- Workflow-managed usage/trial goals.
- Training/cardio/recovery integration.
- Supplements, fasting, labs, or clinical nutrition research.
- MacroFactor or heavy tracking as default.
- Full food database/API automation.
- Full body-transformation roadmap.

## Constraints

- Outcome-first; tooling supports the nutrition/body objective.
- Standalone Project `Питание` usable outside Workflow.
- Durable state outside chat history.
- Low friction, but not cut below one usable loop.
- No heavy calorie/macro ledger by default.
- Sensitive nutrition/health data must stay scoped.

## Escalation triggers

- User wants live diet/menu generation during this Goal.
- Project UI installation becomes part of this Goal.
- Durable state root changes away from `directions/health-and-beauty/projects/nutrition/**`.
- External app/tool binding becomes required.
- Codex is asked to make nutrition decisions rather than save/read back approved state packets.
- Project `Питание` starts depending on Workflow stage/goal/phase machinery.

## Map binding

```yaml
map_binding:
  initiative_id: body-transformation-20kg-strength-health
  node_or_edge: d_nutrition_loop_shape_and_tooling
  expected_map_delta: "Active front advances from decision_required to implementation_goal_shaped_pending_E1."
  why_this_goal_is_minimal: "It creates one complete low-friction nutrition operating loop with durable state, without expanding into training/cardio/recovery or full body-transformation planning."
  why_not_premature_or_optional_expansion: "S3 selected Project `Питание` v0 as the repaired container; this Goal only makes that selected container executable and testable."
```

## Close path

```text
G1_GOAL_SHAPE formalized
-> repository maintenance apply/read-back and Project Files refresh
-> E1_EXECUTION_BRIEF
-> implementation/validation route selected by E1
-> package creation and dry-run evidence
-> R1_GOAL_REVIEW_DISTILL
```

## End-of-file marker

`END_OF_FILE: directions/health-and-beauty/phases/ai-nutrition-operating-layer/goals/nutrition-project-operational-setup-v0/00_GOAL_CONTRACT.md`
