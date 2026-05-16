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
  current_focus: "Run B1_PROBLEM route-integrity recovery / review handoff repair for active Goal core-technical-foundation-decision-brief after G1 repository maintenance apply/read-back and Project Files refresh."
  route_stage: B1_PROBLEM
  route_mode: route_integrity_recovery_for_review_ready_decision_brief
  same_chat_allowed: false
  boundary_trigger: p0_phase_start_map_alignment_after_m0
  pending_state_carried: true
  pending_patch_pointer: g1_goal_shape_route_repair_core_technical_foundation_decision_brief_2026_05_16
  last_stage_result_pointer: "G1_GOAL_SHAPE formalized decision brief classification as review-ready candidate and selected B1 route-integrity repair."
  last_codex_scope_validation: "Codex repository maintenance only; Codex product/project execution remains blocked until project/tool bindings and execution route are verified."
  active_goal:
    goal_id: core-technical-foundation-decision-brief
    goal_title: "Сформировать Core Technical Foundation Decision Brief"
    goal_path: "directions/indie-game-development/phases/core-coop-technical-foundation-selection/goals/core-technical-foundation-decision-brief"
    goal_contract: "directions/indie-game-development/phases/core-coop-technical-foundation-selection/goals/core-technical-foundation-decision-brief/00_GOAL_CONTRACT.md"
    existing_goal_artifact: "directions/indie-game-development/phases/core-coop-technical-foundation-selection/goals/core-technical-foundation-decision-brief/04_CORE_TECHNICAL_FOUNDATION_DECISION_BRIEF.md"
    status: review_ready_candidate_pending_B1_route_repair_not_R1_accepted
  active_phase:
    phase_id: core-coop-technical-foundation-selection
    phase_name: Core Co-op Technical Foundation Selection
    phase_path: "directions/indie-game-development/phases/core-coop-technical-foundation-selection"
    status: active_after_g1_repair_update_pending_b1_route_repair
    map_binding: H1_playable_technical_nucleus
    next_route: B1_PROBLEM
```

## Blockers / required inputs

- Missing context: `none blocking for G1 route repair after user approval`
- Human decision: `none pending for Phase start`
- Source conflict: `resolved by approved G1 patch; Project Files must be refreshed after apply`
- Tool/runtime blocker: `project/tool bindings must be verified before Codex product/project execution`
- Required attachments/context for next stage:
  - exact `workflow/stage_prompts/B1_PROBLEM.md`
  - current Project Files 00-06 after G1 read-back
  - active Phase Brief: `directions/indie-game-development/phases/core-coop-technical-foundation-selection/00_PHASE_BRIEF.md`
  - active Goal Contract: `directions/indie-game-development/phases/core-coop-technical-foundation-selection/goals/core-technical-foundation-decision-brief/00_GOAL_CONTRACT.md`

## Current focus boundary

B1 should repair the route/state handoff created by G1's classification of the existing decision brief as review-ready candidate.

B1 must decide whether the next registry-valid route should be:

- `R1_GOAL_REVIEW_DISTILL` if the artifact can be reviewed as-is;
- `E1_EXECUTION_BRIEF` if execution/decomposition is still needed before review;
- `A1_AUDIT` if source-backed challenge of Grid/Gas/old-project evidence blocks review;
- `D1_DEEP_RESEARCH` if current external evidence blocks review;
- `S3_DECIDE` if a human-owned tradeoff is reopened;
- `Stop` if route/state is contradictory.

B1 must not silently turn this into:

- R1 review execution inside B1;
- technical audit execution;
- external research synthesis without D1;
- Unity project creation;
- code transfer;
- Codex product/project execution;
- Task Master graph creation;
- throwaway gas prototype;
- visual gas proof;
- full engineering handbook;
- Game Documentation promotion.
