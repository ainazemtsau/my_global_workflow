# 04_ACTIVE_GOAL.md

```yaml
project_file_control:
  file: 04_ACTIVE_GOAL.md
  schema: project_file_projection.v1
  direction: directions/health-and-beauty
  source_files:
    - "directions/health-and-beauty/project_files/04_ACTIVE_GOAL.md"
  activated_at: "2026-05-12"
  source_freshness: active_git_file
  canonical_source: GitHub repository file
  conflict_rule: if this file conflicts with another current GitHub Direction file, return Context Request; do not invent state
  default_load: yes
```

```yaml
active_goal:
  state: no_active_goal
  goal_id: null
  goal_name: null
  goal_path: null
  phase_path: null
  current_wave: none
  current_stage: none
  status: none
  next_route: P0_PHASE_START
  use_policy: "No active Goal remains after P9 closed Phase ai-nutrition-operating-layer. Do not execute old E1/U1/R1 Project `Питание` setup routes. Next material route is P0_PHASE_START after repository maintenance/read-back and Project Files refresh."
```

## Latest completed Goal snapshot

```yaml
latest_completed_goal:
  goal_id: nutrition-project-operational-setup-v0
  goal_name: "Починить Project `Питание` как repo-backed multi-chat nutrition loop"
  goal_path: "directions/health-and-beauty/phases/ai-nutrition-operating-layer/goals/nutrition-project-operational-setup-v0"
  closed_under_phase: ai-nutrition-operating-layer
  phase_path: "directions/health-and-beauty/phases/ai-nutrition-operating-layer"
  review_verdict: accepted_complete
  goal_state: closed_under_closed_phase
```

## R1 Review Result

```yaml
verdict: accepted_complete
review_date: "2026-05-21"
evidence_basis: "User-confirmed U1/setup/real-use validation: Project `Питание` is in process, menu composed, setup works."
nonblocking_deferrals:
  - Mealie recipe sync / meal planner sync not proven installed/tested; deferred as optional/nonblocking.
  - Training/cardio/supplements excluded from this Goal.
phase_gate: "Completed Goal satisfied Phase Minimum Outcome; P9 closed the Phase as close_complete."
```

## Goal Contract snapshot

* WHAT: Create a minimal repo-backed multi-chat Project `Питание` nutrition loop where GitHub markdown files are durable nutrition state, ChatGPT Project Files are a refreshable runtime cache, chat memory is non-authoritative, and Codex is save-only repository maintenance writer.
* WHY: The previous Project `Питание` path was stale / not basis-valid after Objective Architecture correction; S3 selected the repaired shape that keeps Project `Питание` as UI while moving authority to repository-backed state.
* DONE: One complete low-friction loop is proven: baseline/current plan -> weekly menu -> tracking/adaptation -> review -> save to GitHub -> Project Files refresh -> fresh chat continuation.
* Acceptance floor: `first_week_bootstrap_from_empty_state`, `later_week_bootstrap_from_saved_state`, `fresh_menu_chat_from_saved_plan`, `fresh_tracking_chat_from_saved_plan_and_menu`, `week_review_from_saved_report`, and `project_files_refresh_reproducibility`.
* Validation: Historical E1 validation targets included repository read-back, dry-runs, Project Files refresh reproducibility, and fresh-chat continuation without hidden memory or manual giant packets; R1 accepted user-confirmed U1/setup/real-use validation as sufficient for this Goal.

This snapshot reflects the repaired G1 Goal shape as historical context. R1 accepted the Goal complete and P9 closed the Phase, so the current route is P0_PHASE_START rather than E1 execution planning.

## Prior artifact input

```yaml
prior_artifact_input:
  goal_id: ai-nutrition-operating-layer-v0
  status: design_protocol_artifact_input_not_operational_setup
```

## Preserved history

The prior MacroFactor active Goal is preserved as historical evidence under:

`directions/health-and-beauty/phases/macrofactor-nutrition-ai-support-setup/goals/ai-support-nutrition-recipes-menu-macrofactor`

It must not be executed as current work unless explicitly reshaped.
