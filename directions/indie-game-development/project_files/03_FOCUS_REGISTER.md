# 03_FOCUS_REGISTER.md

```yaml
project_file_control:
  file: 03_FOCUS_REGISTER.md
  schema: project_file_projection.v1
  direction: directions/indie-game-development
  source_files:
    - "directions/indie-game-development/project_files/03_FOCUS_REGISTER.md"
  activated_at: "2026-05-13"
  source_freshness: active_git_file_after_p0_repository_apply_readback
  canonical_source: GitHub repository file
  conflict_rule: if this file conflicts with another current GitHub Direction file, return Context Request; do not invent state
  default_load: yes
```

```yaml
focus:
  current_focus: "Run G1_GOAL_SHAPE repair/update for active Goal core-technical-foundation-decision-brief after P0 map-alignment repository maintenance apply/read-back and Project Files refresh."
  route_stage: G1_GOAL_SHAPE
  route_mode: repair_update_existing_active_goal_against_initialized_direction_map_and_existing_artifact
  same_chat_allowed: false
  boundary_trigger: p0_phase_start_map_alignment_after_m0
  pending_state_carried: true
  pending_patch_pointer: p0_phase_start_indie_game_development_map_alignment_2026_05_15
  last_stage_result_pointer: "P0_PHASE_START formalized current Phase keep/update, map_binding to H1, and G1 repair/update route."
  last_codex_scope_validation: "Codex repository maintenance only; Codex product/project execution remains blocked until project/tool bindings and execution route are verified."
  active_goal:
    goal_id: core-technical-foundation-decision-brief
    goal_title: "Сформировать Core Technical Foundation Decision Brief"
    goal_path: "directions/indie-game-development/phases/core-coop-technical-foundation-selection/goals/core-technical-foundation-decision-brief"
    goal_contract: "directions/indie-game-development/phases/core-coop-technical-foundation-selection/goals/core-technical-foundation-decision-brief/00_GOAL_CONTRACT.md"
    existing_goal_artifact: "directions/indie-game-development/phases/core-coop-technical-foundation-selection/goals/core-technical-foundation-decision-brief/04_CORE_TECHNICAL_FOUNDATION_DECISION_BRIEF.md"
    status: artifact_exists_pending_G1_repair_update
  active_phase:
    phase_id: core-coop-technical-foundation-selection
    phase_name: Core Co-op Technical Foundation Selection
    phase_path: "directions/indie-game-development/phases/core-coop-technical-foundation-selection"
    status: active_after_p0_map_alignment_pending_g1_repair_update
    map_binding: H1_playable_technical_nucleus
    next_route: G1_GOAL_SHAPE
```

## Blockers / required inputs

- Missing context: `none blocking for P0 formalization after user approval`
- Human decision: `none pending for Phase start`
- Source conflict: `resolved by approved P0 patch; Project Files must be refreshed after apply`
- Tool/runtime blocker: `project/tool bindings must be verified before Codex product/project execution`
- Required attachments/context for next stage:
  - exact `workflow/stage_prompts/G1_GOAL_SHAPE.md`
  - current Project Files 00-07 after P0 read-back
  - new Phase Brief: `directions/indie-game-development/phases/core-coop-technical-foundation-selection/00_PHASE_BRIEF.md`

## Current focus boundary

G1 should repair/update the existing active Goal against the initialized Direction Map and existing decision brief artifact.

G1 must decide whether `04_CORE_TECHNICAL_FOUNDATION_DECISION_BRIEF.md` is:

- review-ready and should be routed toward R1 through a registry-valid path;
- incomplete and needs a bounded repair/update;
- blocked by current external evidence and should route to `D1_DEEP_RESEARCH`;
- blocked by old project evidence and should route to `A1_AUDIT` or Context Request;
- blocked by a human-owned tradeoff and should route to `S3_DECIDE`;
- stale/partial evidence only.

G1 must not silently turn this into:

- E1 execution decomposition before artifact-state reconciliation;
- technical audit execution;
- external research synthesis without D1;
- final technology selection without evidence/review;
- Unity project creation;
- code transfer;
- Codex product/project execution;
- Task Master graph creation;
- throwaway gas prototype;
- visual gas proof;
- full engineering handbook;
- Game Documentation promotion.
