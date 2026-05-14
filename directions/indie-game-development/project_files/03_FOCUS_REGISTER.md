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
  current_focus: "Run E1_EXECUTION_BRIEF for active Goal core-technical-foundation-decision-brief after G1 repository maintenance apply/read-back and Project Files refresh."
  route_stage: E1_EXECUTION_BRIEF
  same_chat_allowed: false
  boundary_trigger: g1_goal_shape_after_repository_maintenance
  pending_state_carried: true
  pending_patch_pointer: g1_goal_shape_core_technical_foundation_decision_map_2026-05-14
  last_stage_result_pointer: "G1_GOAL_SHAPE shaped Core Technical Foundation Decision Brief as staged decision map."
  last_codex_scope_validation: "Codex repository maintenance only; Codex product/project execution remains blocked until project/tool bindings and execution route are verified."
  active_goal:
    goal_id: core-technical-foundation-decision-brief
    goal_title: "Сформировать Core Technical Foundation Decision Brief"
    goal_path: "directions/indie-game-development/phases/core-coop-technical-foundation-selection/goals/core-technical-foundation-decision-brief"
    goal_contract: "directions/indie-game-development/phases/core-coop-technical-foundation-selection/goals/core-technical-foundation-decision-brief/00_GOAL_CONTRACT.md"
    status: active_goal_shaped_pending_E1
  active_phase:
    phase_id: core-coop-technical-foundation-selection
    phase_name: Core Co-op Technical Foundation Selection
    phase_path: "directions/indie-game-development/phases/core-coop-technical-foundation-selection"
    status: active
    next_route: E1_EXECUTION_BRIEF
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

E1 should prepare the minimum execution brief for producing the accepted `Core Technical Foundation Decision Brief` / Decision Map.

E1 must preserve the staged decision-map model. It must classify each foundation surface as one of:

- `decided`;
- `decision_gate`;
- `research_needed_D1`;
- `audit_needed_A1`;
- `human_decision_needed_S3`;
- `deferred_not_blocking_for_bootstrap`.

E1 must cover these foundation surfaces:

- multiplayer technology and host-player architecture;
- Grid/Topology transfer boundary;
- Gas Simulation durable logic architecture;
- smallest durable technical nucleus;
- Project Engineering & Codex Development Operating Model.

E1 must not silently turn this into:

- technical audit execution;
- external research synthesis without routing to D1 when needed;
- final technology selection without evidence;
- Unity project creation;
- code transfer;
- Codex product/project execution;
- Task Master graph creation;
- throwaway gas prototype;
- visual gas proof;
- full engineering handbook;
- Game Documentation promotion.

If E1 discovers that current external multiplayer/tooling evidence is required, route to `D1_DEEP_RESEARCH`.

If E1 discovers that a human-owned strategic tradeoff is blocking, route to `S3_DECIDE`.

If E1 discovers that old project docs/code are blocking, return Context Request or route to `A1_AUDIT` with exact file needs.
