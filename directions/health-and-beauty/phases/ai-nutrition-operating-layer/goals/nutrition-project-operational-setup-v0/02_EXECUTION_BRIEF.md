# 02_EXECUTION_BRIEF — Repaired repo-backed Project `Питание` nutrition loop

```yaml
artifact_control:
  artifact_name: "02_EXECUTION_BRIEF — Repaired repo-backed Project `Питание` nutrition loop"
  schema: execution_brief.v1
  owner_layer: direction_goal
  status: formalized
  direction: directions/health-and-beauty
  phase_path: directions/health-and-beauty/phases/ai-nutrition-operating-layer
  goal_id: nutrition-project-operational-setup-v0
  goal_path: directions/health-and-beauty/phases/ai-nutrition-operating-layer/goals/nutrition-project-operational-setup-v0
  formalized_by_stage: E1_EXECUTION_BRIEF
  formalized_at: "2026-05-20"
  source_stage: G1_GOAL_SHAPE
  selected_next_stage: C1_CODEX_GRAPH_PLAN
```

## Route decision

```yaml
route_decision:
  selected_route: C1_CODEX_GRAPH_PLAN
  execution_topology: codex_graph
  execution_readiness_status: ready
  next_action_proof_status: inherited
  mssp_status: proven_compact
  component_necessity_status: passed_with_file_surface_cuts
  route_basis:
    - repaired Goal Contract
    - Goal Working Context
    - Objective Architecture Model
    - Stage Registry
  why_this_route: "The Goal requires coordinated repository-backed state/protocol files, save boundaries, dry-run acceptance, Project Files refresh reproducibility, and possible later ChatGPT Project UI setup. This requires Codex graph planning before execution."
  f0_rejected:
    reason: multi_file_coordination
    explanation: "F0 is too direct for a multi-file repo-backed loop with validation and refresh requirements."
  u1_rejected_as_first_route:
    reason: "Human-guided ChatGPT Project UI setup may be required later, but repository state/protocol files must exist first."
  d1_rejected:
    reason: "No current external research question blocks the implementation envelope."
  a1_rejected:
    reason: "Stale-cache risk is handled by explicit source evidence and stale override."
  r1_rejected:
    reason: "Parent Goal completion evidence does not exist."
```

## Execution brief

```yaml
objective: "Create the minimum repo-backed multi-chat Project `Питание` nutrition loop."
smallest_safe_slice:
  - first_week_bootstrap_from_empty_state
  - later_week_bootstrap_from_saved_state
implementation_target: "directions/health-and-beauty/projects/nutrition/**"
allowed_surfaces:
  - nutrition state templates
  - nutrition runtime/cache protocol files
  - save/update boundary
  - dry-run acceptance protocol
  - ChatGPT Project `Питание` instructions source
validation_surface:
  - repository read-back
  - EOF marker validation
  - dry-run acceptance
  - Project Files refresh reproducibility
  - fresh-chat continuation without hidden memory
acceptance_or_review_path: "C1 -> C2 -> optional U1 -> R1 only after parent Goal completion evidence exists"
```

## Component Necessity Test

```yaml
component_necessity:
  kept_state_files:
    - file: USER_NUTRITION_BASELINE.md
      supports:
        - first_week_bootstrap_from_empty_state
        - later_week_bootstrap_from_saved_state
      if_removed_what_fails: "Fresh chats cannot distinguish missing baseline from saved baseline."
    - file: CURRENT_NUTRITION_PLAN.md
      supports:
        - later_week_bootstrap_from_saved_state
        - fresh_menu_chat_from_saved_plan
      if_removed_what_fails: "Menu/tracking/review cannot anchor to a saved current plan."
    - file: ACTIVE_WEEK_MENU.md
      supports:
        - fresh_menu_chat_from_saved_plan
        - fresh_tracking_chat_from_saved_plan_and_menu
      if_removed_what_fails: "Tracking cannot compare events/deviations against the current week menu."
    - file: WEEK_TRACKING_REPORT.md
      supports:
        - fresh_tracking_chat_from_saved_plan_and_menu
        - week_review_from_saved_report
      if_removed_what_fails: "Review has no durable report input."
    - file: REVIEW_AND_NEXT_WEEK.md
      supports:
        - week_review_from_saved_report
        - project_files_refresh_reproducibility
      if_removed_what_fails: "Next week continuation has no durable review/next input."
  cut_or_merged_files:
    - MENU_PREFERENCES.md -> USER_NUTRITION_BASELINE.md
    - WEEK_SHOPPING_LIST.md -> ACTIVE_WEEK_MENU.md
    - WEEK_PREP_PLAN.md -> ACTIVE_WEEK_MENU.md
    - REVIEW_DECISIONS.md -> REVIEW_AND_NEXT_WEEK.md
    - NEXT_WEEK_INPUTS.md -> REVIEW_AND_NEXT_WEEK.md
  kept_protocol_files:
    - 00_NUTRITION_START_HERE.md
    - 01_NUTRITION_LOOP_PROTOCOL.md
    - 02_STATE_AND_SAVE_PROTOCOL.md
    - 03_DRY_RUN_ACCEPTANCE.md
  cut_or_merged_protocol_files:
    - separate plan/menu/tracking/review protocols -> 01_NUTRITION_LOOP_PROTOCOL.md
    - CODEX_SAVE_OPERATOR.md -> 02_STATE_AND_SAVE_PROTOCOL.md
    - CHAT_LAUNCHERS.md -> 00_NUTRITION_START_HERE.md
```

## Target file surface for C1 to plan

```text
directions/health-and-beauty/projects/nutrition/state/USER_NUTRITION_BASELINE.md
directions/health-and-beauty/projects/nutrition/state/CURRENT_NUTRITION_PLAN.md
directions/health-and-beauty/projects/nutrition/state/ACTIVE_WEEK_MENU.md
directions/health-and-beauty/projects/nutrition/state/WEEK_TRACKING_REPORT.md
directions/health-and-beauty/projects/nutrition/state/REVIEW_AND_NEXT_WEEK.md

directions/health-and-beauty/projects/nutrition/project_files/00_NUTRITION_START_HERE.md
directions/health-and-beauty/projects/nutrition/project_files/01_NUTRITION_LOOP_PROTOCOL.md
directions/health-and-beauty/projects/nutrition/project_files/02_STATE_AND_SAVE_PROTOCOL.md
directions/health-and-beauty/projects/nutrition/project_files/03_DRY_RUN_ACCEPTANCE.md

directions/health-and-beauty/project_setup/pitanie/CHATGPT_PROJECT_INSTRUCTIONS.md
```

## Acceptance → validation map

| Acceptance-floor item | Artifact/check | Evidence required |
|---|---|---|
| `first_week_bootstrap_from_empty_state` | start file + baseline/current plan templates | Fresh chat asks only missing baseline inputs and emits save card |
| `later_week_bootstrap_from_saved_state` | saved state files + save protocol | Fresh chat reads saved state and does not re-ask full baseline |
| `fresh_menu_chat_from_saved_plan` | current plan + active week menu | Menu derives from saved plan/preferences, not memory |
| `fresh_tracking_chat_from_saved_plan_and_menu` | tracking report + loop protocol | Food event/deviation handled exception-only, no default macro ledger |
| `week_review_from_saved_report` | review/next-week file | Review decisions and next-week inputs generated from saved report |
| `project_files_refresh_reproducibility` | Project instructions + state/save protocol | Manual refresh sequence proves fresh-chat continuation |

## Human Burden Budget

```yaml
human_burden_budget:
  recurring_user_actions:
    - action: "Provide missing baseline only when absent or stale."
      frequency: first_bootstrap_or_change_only
      burden: low
    - action: "Report food events/deviations by simple text/photo/voice summary."
      frequency: exception_or_daily_if_user_chooses
      burden: low
    - action: "Run weekly review/sync."
      frequency: weekly
      burden: low
    - action: "Manual Project Files refresh after GitHub state changes."
      frequency: after Codex save/update
      burden: acceptable_if_explicit_and_infrequent
  rejected_default:
    - detailed calorie ledger
    - detailed macro ledger
    - manual giant state packets
  burden_verdict: acceptable
```

## C1 requirements

C1 must plan repository implementation only. It must not execute.

Required C1 outputs:

- exact Codex execution graph or wave plan;
- existing-file inspection requirement before mutation;
- exact create/update/delete policy;
- validation commands/checks;
- read-back and EOF marker requirements;
- dry-run acceptance map;
- Project Files refresh protocol;
- optional U1 handoff only if ChatGPT Project UI setup must be done by the user.

## Scope cuts and forbidden work

```yaml
explicit_non_goals:
  - live diet/menu generation
  - actual nutrition prescription
  - MacroFactor revival
  - detailed calorie or macro ledger as default
  - training/cardio/recovery/supplements/labs/fasting expansion
  - food database/API automation
  - broad body-transformation roadmap
  - hidden chat memory
  - manual giant packets as normal workflow
forbidden_in_C1:
  - repository mutation
  - parent Goal closure
  - R1 launch before C2/U1 evidence
  - Project Files state mutation unless explicitly planned for later approved execution
```

## Lifecycle state reconciliation

```yaml
lifecycle_state_reconciliation:
  active_goal_state_from: goal_shaped_pending_E1
  active_goal_state_to: e1_formalized_pending_C1
  next_route_from: E1_EXECUTION_BRIEF
  next_route_to: C1_CODEX_GRAPH_PLAN
  project_files_runtime_projection: stale_but_nonblocking_for_named_next_stage
  allowed_next_stage_when_stale: C1_CODEX_GRAPH_PLAN
  fresh_sources_for_next_stage:
    - directions/health-and-beauty/phases/ai-nutrition-operating-layer/goals/nutrition-project-operational-setup-v0/00_GOAL_CONTRACT.md
    - directions/health-and-beauty/phases/ai-nutrition-operating-layer/goals/nutrition-project-operational-setup-v0/01_GOAL_WORKING_CONTEXT.md
    - directions/health-and-beauty/phases/ai-nutrition-operating-layer/goals/nutrition-project-operational-setup-v0/02_EXECUTION_BRIEF.md
    - C1 launch card emitted by E1
```

## End-of-file marker

`END_OF_FILE: directions/health-and-beauty/phases/ai-nutrition-operating-layer/goals/nutrition-project-operational-setup-v0/02_EXECUTION_BRIEF.md`
