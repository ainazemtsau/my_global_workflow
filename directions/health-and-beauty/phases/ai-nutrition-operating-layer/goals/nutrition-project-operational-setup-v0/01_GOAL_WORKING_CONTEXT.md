# Goal Working Context — nutrition-project-operational-setup-v0

```yaml
artifact_control:
  artifact_name: "Goal Working Context - Project Питание v0"
  schema: goal_working_context.v1
  owner_layer: direction_goal
  status: active
  direction_path: "directions/health-and-beauty"
  phase_path: "directions/health-and-beauty/phases/ai-nutrition-operating-layer"
  goal_path: "directions/health-and-beauty/phases/ai-nutrition-operating-layer/goals/nutrition-project-operational-setup-v0"
  goal_id: nutrition-project-operational-setup-v0
  formalized_by_stage: G1_GOAL_SHAPE
  formalized_at: "2026-05-19"
  next_route: E1_EXECUTION_BRIEF
```

## Runtime posture

Project `Питание` v0 is an autonomous nutrition operating layer. It must be usable outside Workflow and must not know Workflow stage/goal/phase machinery.

Workflow may develop, repair, validate, and review the Project package. The installed Project package itself should only know its own nutrition files, roles, state, protocols, and save/read-back rules.

## Direction / Phase fit

Direction: `directions/health-and-beauty`.

Active initiative: `body-transformation-20kg-strength-health`.

Active Phase: `directions/health-and-beauty/phases/ai-nutrition-operating-layer`.

The Goal advances the Phase by turning the selected low-friction nutrition container into a concrete execution target. It does not close the Phase and does not claim a working Project exists before validation.

## Required Project package target

Later execution must produce:

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

## Minimum complete loop

The package must support one complete loop:

1. Load/start/resume from durable state.
2. Plan cycle/menu defaults from baseline and preferences.
3. Intake meal/photo/voice-style event with missing-answer defaults.
4. Correct the current day after off-menu eating or overeating.
5. Review day/week.
6. Emit compact state-update/sync packet.

## Role boundaries

### Dietitian

Provides evidence-aware nutrition guidance inside non-clinical boundaries. Must not diagnose, prescribe clinical protocols, or replace medical advice.

### Menu Planner

Produces cycle/menu/default/prep-note planning. Must not become a full recipe database or API automation layer.

### Food Tracker

Handles low-friction event intake, exceptions, summaries, and correction prompts. Must not require heavy calorie/macro ledger by default.

### Codex Save Operator

Applies approved state-update packets to repository files and returns read-back/diff evidence. Must not interpret nutrition content or make nutrition decisions.

## Durable state policy

Durable state root:

```text
directions/health-and-beauty/projects/nutrition/**
```

Chat history is not durable state. The Project must emit compact update packets that can be applied by the Codex Save Operator protocol.

## Synthetic dry-runs required for acceptance

### Dry-run 1 — cycle planning / restart

Input: synthetic baseline and menu preferences.

Expected: current cycle/default plan and clear durable state outputs.

### Dry-run 2 — meal event + exception

Input: simulated meal/photo/voice event with missing fields and one off-menu/overeating event.

Expected: missing-answer defaults, current-day correction, no heavy ledger requirement.

### Dry-run 3 — review + sync

Input: synthetic day/week events.

Expected: compact summary and `nutrition_state_update_packet.v1`.

## Allowed actions for E1

- Define the execution envelope.
- Define exact artifact writes and validators.
- Decide whether implementation routes through F0, C1/C2, or U1.
- Define dry-run validation prompts/cases.
- Define repository maintenance/read-back requirements.
- Keep implementation inside the approved Project package root.

## Forbidden actions for E1

- Generate actual live user diet/menu.
- Install/configure ChatGPT Project UI.
- Run unapproved repository mutation.
- Expand into training/cardio/recovery.
- Expand into supplements/labs/fasting research.
- Make MacroFactor/heavy tracking the default.
- Create a full food database/API automation layer.
- Treat Project `Питание` as the objective instead of a tool.

## Required context for E1

Default-load after repository maintenance and manual Project Files refresh:

- Direction Project Files 00-08.
- Shared runtime cache files.
- `00_GOAL_CONTRACT.md`.
- `01_GOAL_WORKING_CONTEXT.md`.
- Exact stage prompt: `workflow/stage_prompts/E1_EXECUTION_BRIEF.md`.

Request-only context if E1 needs it:

- Prior AI Nutrition Operating Layer v0 design artifact.
- Prior Project `Питание` historical contract/context.
- Existing menu or baseline/preference materials.
- Tool/storage availability notes.
- Current kitchen equipment and prep notes.

## Source freshness notes

- S3 result is fresh enough for G1 only.
- E1 must not execute from Project Files that still show S3 pending.
- Repository maintenance and Project Files refresh are blocking before material E1 execution.

## Failure conditions

- Project package requires Workflow machinery.
- Dry-runs cannot complete from Project package files.
- Durable state update packet is unclear or not saveable.
- Codex Save Operator protocol makes nutrition decisions.
- Low-friction loop is cut below usability.
- Heavy tracking becomes required by default.

## End-of-file marker

`END_OF_FILE: directions/health-and-beauty/phases/ai-nutrition-operating-layer/goals/nutrition-project-operational-setup-v0/01_GOAL_WORKING_CONTEXT.md`
