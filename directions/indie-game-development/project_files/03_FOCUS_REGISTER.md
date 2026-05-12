# 03_FOCUS_REGISTER.md

```yaml
project_file_control:
  file: 03_FOCUS_REGISTER.md
  schema: project_file_projection.v1
  direction: directions/indie-game-development
  source_files:
    - "directions/indie-game-development/project_files/03_FOCUS_REGISTER.md"
  activated_at: "2026-05-12"
  source_freshness: active_git_file
  canonical_source: GitHub repository file
  conflict_rule: if this file conflicts with another current GitHub Direction file, return Context Request; do not invent state
  default_load: yes
```

```yaml
focus:
  current_focus: "Select the next Goal after R1 accepted the Minimum Expedition Proof Core."
  route_stage: G0_GOAL_SELECT
  same_chat_allowed: false
  boundary_trigger: new_goal
  pending_state_carried: false
  pending_patch_pointer: none
  last_stage_result_pointer: "R1_GOAL_REVIEW_DISTILL accepted minimum proof-core Goal"
  last_codex_scope_validation: "Codex repository maintenance only; Codex product/project execution remains blocked until project/tool bindings are verified."
  last_accepted_goal_artifact: "directions/indie-game-development/phases/expedition-first-proof-checkpoint/goals/minimum-proof-core-first-expedition-proof/03_MINIMUM_EXPEDITION_PROOF_CORE.md"
```

## Blockers / required inputs

* Missing context: `none known for next Goal selection`
* Human decision: `required only if choosing to close/pause the Phase instead of selecting the next Goal`
* Source conflict: `none known after this patch is applied and read back`
* Tool/runtime blocker: `project/tool bindings must be verified before Codex product/project execution`
* Required attachments for next stage: exact `workflow/stage_prompts/G0_GOAL_SELECT.md` prompt and specific request-only context only if the next stage asks for it.

## Current focus boundary

The accepted proof-core artifact is not a prototype design and not an implementation plan.

Next work must not silently turn the accepted proof core into:
* playable proof design;
* prototype scene specification;
* code tasks;
* exact cargo/carrying/death/lift/procgen/tool/economy/progression decisions;
* Game Documentation promotion;
* Codex product/project execution.
