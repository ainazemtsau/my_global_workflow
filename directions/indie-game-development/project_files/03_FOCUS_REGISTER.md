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
  current_focus: "Run G1_GOAL_SHAPE for candidate core-technical-foundation-decision-brief."
  route_stage: G1_GOAL_SHAPE
  same_chat_allowed: false
  boundary_trigger: p0_phase_start_after_repository_maintenance
  pending_state_carried: true
  pending_patch_pointer: p0_phase_start_core_coop_technical_foundation_selection_2026-05-13
  last_stage_result_pointer: "P0_PHASE_START created Core Co-op Technical Foundation Selection."
  last_codex_scope_validation: "Codex repository maintenance only; Codex product/project execution remains blocked until project/tool bindings and execution route are verified."
  active_goal:
    goal_id: null
    goal_title: null
    goal_path: null
    goal_contract: null
    status: none_pending_G1
  recommended_first_goal_candidate:
    goal_candidate_id: core-technical-foundation-decision-brief
    goal_title: "Сформировать Core Technical Foundation Decision Brief"
    recommended_next_stage: G1_GOAL_SHAPE
  active_phase:
    phase_id: core-coop-technical-foundation-selection
    phase_name: Core Co-op Technical Foundation Selection
    phase_path: "directions/indie-game-development/phases/core-coop-technical-foundation-selection"
    status: active
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

G1 should shape one Goal: `Core Technical Foundation Decision Brief`.

G1 must not silently turn this into:

- technical audit execution;
- external research synthesis without routing to D1 when needed;
- final technology selection without evidence;
- Unity project creation;
- code transfer;
- Codex product/project execution;
- throwaway gas prototype;
- visual gas proof;
- Game Documentation promotion.

If G1 discovers that current external multiplayer technology evidence is required, route to `D1_DEEP_RESEARCH`.

If G1 discovers that a human-owned strategic tradeoff is blocking, route to `S3_DECIDE`.

If G1 discovers that old project/docs are blocking, return Context Request naming exact files.
