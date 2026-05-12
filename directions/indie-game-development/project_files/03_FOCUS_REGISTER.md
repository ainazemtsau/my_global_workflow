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
  current_focus: "Run P0_PHASE_START to start the next post-proof-core Phase after P9 closed Expedition First Proof Checkpoint."
  route_stage: P0_PHASE_START
  same_chat_allowed: false
  boundary_trigger: phase_start_after_close
  pending_state_carried: true
  pending_patch_pointer: p9_phase_close_expedition_first_proof_checkpoint_2026-05-12
  last_stage_result_pointer: "P9_PHASE_CLOSE closed Expedition First Proof Checkpoint."
  last_codex_scope_validation: "Codex repository maintenance only; Codex product/project execution remains blocked until project/tool bindings are verified."
  last_accepted_goal_artifact: "directions/indie-game-development/phases/expedition-first-proof-checkpoint/goals/minimum-proof-core-first-expedition-proof/03_MINIMUM_EXPEDITION_PROOF_CORE.md"
  closed_phase:
    phase_id: expedition-first-proof-checkpoint
    status: closed
    next_route: P0_PHASE_START
```

## Blockers / required inputs

* Missing context: `none blocking for P0 after P9 repository maintenance apply/read-back`
* Human decision: `none pending`
* Source conflict: `none known after this patch is applied and read back`
* Tool/runtime blocker: `project/tool bindings must be verified before Codex product/project execution`
* Required attachments for next stage: exact `workflow/stage_prompts/P0_PHASE_START.md`, current Project Files 00-06 after P9 read-back, closed Phase Brief, Phase Review, accepted proof-core artifact, and Phase Execution Log.

## Current focus boundary

The accepted proof-core artifact is not a prototype design and not an implementation plan.

Next work must not silently turn the accepted proof core into:
* playable proof design;
* prototype scene specification;
* code tasks;
* exact cargo/carrying/death/lift/procgen/tool/economy/progression decisions;
* Game Documentation promotion;
* Codex product/project execution.

P0 may start a new Phase that defines the next smallest useful post-proof-core outcome.
