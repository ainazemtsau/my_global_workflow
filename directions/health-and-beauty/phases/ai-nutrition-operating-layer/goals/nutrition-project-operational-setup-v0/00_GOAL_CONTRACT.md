# Goal Contract — Repaired repo-backed Project `Питание` nutrition loop

```yaml
artifact_control:
  artifact_name: "Goal Contract — Repaired repo-backed Project `Питание` nutrition loop"
  schema: goal_contract.v1
  owner_layer: direction_goal
  status: active
  direction: directions/health-and-beauty
  phase_path: directions/health-and-beauty/phases/ai-nutrition-operating-layer
  goal_path: directions/health-and-beauty/phases/ai-nutrition-operating-layer/goals/nutrition-project-operational-setup-v0
  shaped_by_stage: G1_GOAL_SHAPE
  shaped_at: "2026-05-20"
  source_decision_stage: S3_DECIDE
  lifecycle_state: goal_shaped_pending_E1
```

## Goal

**goal_id:** `nutrition-project-operational-setup-v0`

**Title:** Починить Project `Питание` как repo-backed multi-chat nutrition loop.

## WHAT

Создать минимальный рабочий nutrition operating loop, где:

- GitHub markdown files являются durable source of truth для nutrition state.
- ChatGPT Project `Питание` остаётся пользовательским UI-контейнером.
- ChatGPT Project Files являются refreshable runtime cache, а не источником истины.
- Chat memory не считается authoritative state.
- Codex используется только как save-only repository maintenance writer.
- Weekly fresh chats могут продолжать работу из сохранённого state без manual giant packets.

## WHY now

Предыдущий путь Project `Питание` был признан stale / not basis-valid после Objective Architecture correction. S3 выбрал repaired shape: сохранить Project `Питание`, но перевести его в repo-backed multi-chat loop. Поэтому текущий Goal должен быть reshaped перед E1 execution planning.

## Minimum Complete Outcome

Один полный low-friction nutrition loop:

`baseline/current plan -> weekly menu -> tracking/adaptation -> review -> save to GitHub -> Project Files refresh -> fresh chat continuation`

Если убрать GitHub state, Project Files refresh или save boundary, fresh chats снова зависят от скрытой chat memory или ручной вставки больших state packets. Это ниже minimum complete outcome.

## DONE

Goal complete только когда подтверждено:

- существует минимальный набор repository-backed nutrition state/protocol files;
- first-week chat может запросить только missing baseline inputs и создать initial plan/save card;
- later-week chat может прочитать saved state и не переопрашивать baseline полностью;
- fresh menu chat может построить weekly menu по saved plan;
- fresh tracking/adaptation chat может обработать food event/photo/deviation без default heavy macro ledger;
- review/sync chat может обновить review decisions and next week inputs;
- Codex save boundary явно описывает, какие файлы меняются и как они возвращаются в GitHub;
- после manual Project Files refresh fresh chats продолжают без hidden memory and giant manual packets.

## Acceptance floor

Required acceptance tests:

1. `first_week_bootstrap_from_empty_state`
2. `later_week_bootstrap_from_saved_state`
3. `fresh_menu_chat_from_saved_plan`
4. `fresh_tracking_chat_from_saved_plan_and_menu`
5. `week_review_from_saved_report`
6. `project_files_refresh_reproducibility`

## Validation signal

A fresh Project `Питание` chat can continue from saved repository-backed Project Files cache, ask only missing/stale inputs, create/update menu/tracking/review outputs, and emit save cards for Codex without relying on hidden chat memory or manual giant packets.

## Validation method

E1 must plan the minimum execution route and validation map. Execution must later prove the acceptance tests through repository read-back, dry-runs, and Project Files refresh evidence before R1 can review parent Goal completion.

## Smallest testable slice

First execution slice should establish the minimum state/protocol skeleton and prove:

- first-week bootstrap from empty/missing state;
- later-week continuation from saved state.

Menu generation alone is not sufficient.

## Map binding

```yaml
map_binding:
  initiative_id: body-transformation-20kg-strength-health
  node_or_edge: d_nutrition_loop_shape_and_tooling
  expected_map_delta: "Goal moves from stale blocked decision target to repaired implementation target pending E1."
  why_this_goal_is_minimal: "It repairs the nutrition loop/state/tooling bottleneck without expanding into training/cardio/recovery/supplements or a full body-transformation roadmap."
  why_not_premature_or_optional_expansion: "Nutrition loop persistence is the active blocker; broader health/fitness work remains parked until this loop is usable."
```

## Proof statuses

```yaml
map_frontier_binding_status: inherited_and_sufficient
next_action_proof_status: inherited_from_S3_and_G1_validated
minimum_complete_outcome: "One complete repo-backed low-friction weekly nutrition loop."
MSSP_status: proven_compact
user_example_classification:
  Project_Pitanie: explicit_selected_container_not_objective
  GitHub_markdown_state: explicit_requirement
  multi_chat_roles: explicit_selected_solution_shape
  manual_giant_packets: anti_example
  detailed_macro_calorie_ledger_default: constraint_rejected_for_default
  training_cardio_recovery_supplements: deferred_out_of_current_goal
```

## Scope in

- repo-backed state policy;
- Project Files runtime-cache policy;
- multi-chat role topology;
- first-week vs later-week behavior;
- Codex save-only boundary;
- minimum protocol/state file targets for E1 to evaluate;
- acceptance dry-runs and refresh reproducibility.

## Non-goals

- live diet/menu generation in G1;
- actual nutrition prescription in G1;
- implementation writes under `directions/health-and-beauty/projects/nutrition/**` in G1;
- R1 closure;
- Phase close;
- MacroFactor/heavy tracker revival;
- training/cardio/recovery/supplements/labs/fasting expansion;
- manual giant state-packet workaround.

## Route recommendation

Next stage: `E1_EXECUTION_BRIEF`.

E1 must create the minimum HOW, validation plan, Codex repository maintenance envelope, and any U1 handoff needed for ChatGPT Project UI setup. G1 must not execute implementation.

## Close path

`G1_GOAL_SHAPE -> E1_EXECUTION_BRIEF -> execution route selected by E1 -> R1_GOAL_REVIEW_DISTILL only after parent Goal completion evidence exists`.

## Failure conditions

- implementation depends on hidden chat memory;
- user must paste giant state packets as normal workflow;
- default path requires detailed macro/calorie ledger;
- Project `Питание` is treated as the objective instead of a UI container;
- files are created but fresh-chat continuation is not proven;
- Codex mutates nutrition implementation files outside approved execution route.

## End-of-file marker

`END_OF_FILE: directions/health-and-beauty/phases/ai-nutrition-operating-layer/goals/nutrition-project-operational-setup-v0/00_GOAL_CONTRACT.md`
