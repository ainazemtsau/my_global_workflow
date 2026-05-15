# 08 Direction Map - Solo Max Productive

```yaml
artifact_control:
  artifact_name: "08 Direction Map - Solo Max Productive"
  schema: direction_map.v1
  owner_layer: persistence
  status: draft_needs_m0_review
  repo_path: "directions/solo-max-productive/project_files/08_DIRECTION_MAP.md"
  default_load: yes
  freshness: needs_m0_review
  last_updated: null
```

## Purpose

Compact strategic routing context for the Direction's current initiative, active front, horizon slice, and map-linked Phase/Goal selection.

This file does not replace:

- `01_DIRECTION_STATE.md`
- `02_CURRENT_PHASE.md`
- `04_ACTIVE_GOAL.md`
- `05_PORTFOLIO_QUEUE.md`
- `06_CONTEXT_LIBRARY_INDEX.md`
- `07_PHASE_MEMORY_INDEX.md`

## Direction map status

```yaml
direction_map_status:
  map_state: uninitialized
  current_initiative_id: null
  map_confidence: low
  last_reviewed_stage: null
  migration_status: needs_m0_direction_map
  migration_inputs_to_read:
    - project_files/00_DIRECTION_START_HERE.md
    - project_files/01_DIRECTION_STATE.md
    - project_files/02_CURRENT_PHASE.md
    - project_files/03_FOCUS_REGISTER.md
    - project_files/04_ACTIVE_GOAL.md
    - project_files/05_PORTFOLIO_QUEUE.md
    - project_files/06_CONTEXT_LIBRARY_INDEX.md
    - project_files/07_PHASE_MEMORY_INDEX.md
    - user_provided_current_initiative_or_strategic_objective_if_available
  update_policy: "M0 owns shared map review/update; branch chats emit delta proposals only."
```

## Post-rollout migration note

This Direction Map is an initial runtime stub.

Before using it for material Phase/Goal selection, run `M0_DIRECTION_MAP` to build the real map from current Direction progress.

M0 migration must read current Direction state from:

```text
project_files/00_DIRECTION_START_HERE.md
project_files/01_DIRECTION_STATE.md
project_files/02_CURRENT_PHASE.md
project_files/03_FOCUS_REGISTER.md
project_files/04_ACTIVE_GOAL.md
project_files/05_PORTFOLIO_QUEUE.md
project_files/06_CONTEXT_LIBRARY_INDEX.md
project_files/07_PHASE_MEMORY_INDEX.md
project_files/08_DIRECTION_MAP.md
```

If the user provides a Current Initiative / strategic Direction objective, M0 may use it as human input, but must validate and shape it against current progress instead of inventing missing state.

## Current Initiative

```yaml
current_initiative:
  id: null
  title: null
  status: null
  intent: null
  why_now: null
  success_signal: null
```

## Initiative Registry

```yaml
initiative_registry: []
```

## Strategy Basis

```yaml
strategy_basis:
  map_generation_mode: not_generated
  strategic_question: null
  optimization_criteria:
    - shortest_credible_path
    - constraint_removal
    - evidence_value
    - scope_minimization
    - reversibility
    - human_burden_minimization
  candidate_paths_considered: []
  selected_path_rationale: null
  major_assumptions: []
  scope_cuts: []
```

## Compact Initiative Graph

```yaml
compact_initiative_graph:
  nodes: []
  edges: []
```

## Active Front

```yaml
active_front:
  primary_node: null
  parallel_candidate_nodes: []
  parked_nodes: []
```

## Horizon Slice

```yaml
horizon_slice:
  statement: null
  node_ids: []
```

## Map Update Policy

```yaml
map_update_policy:
  branch_chats_may_mutate_map: false
  allowed_mutation_points:
    - M0_DIRECTION_MAP
    - R1_GOAL_REVIEW_DISTILL
    - P9_PHASE_CLOSE
    - parent_synthesis_after_parallel_branches
  forbidden_behavior:
    - branch_chat_direct_map_mutation
    - backlog_expansion_without_active_front_reason
    - calendar_roadmap_creation
    - replacing_phase_or_goal_state
```

## End-of-file marker

`END_OF_FILE: directions/solo-max-productive/project_files/08_DIRECTION_MAP.md`
