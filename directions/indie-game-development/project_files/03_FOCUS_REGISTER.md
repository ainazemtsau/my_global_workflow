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
  current_focus: "Run G1_GOAL_SHAPE to shape the first Goal for Expedition First Playable Proof Slice."
  route_stage: G1_GOAL_SHAPE
  same_chat_allowed: false
  boundary_trigger: phase_start_after_P0
  pending_state_carried: true
  pending_patch_pointer: p0_phase_start_expedition_first_playable_proof_slice_2026-05-12
  last_stage_result_pointer: "P0_PHASE_START created active Phase Expedition First Playable Proof Slice."
  last_codex_scope_validation: "Codex repository maintenance only; Codex product/project execution remains blocked until project/tool bindings are verified."
  last_accepted_goal_artifact: "directions/indie-game-development/phases/expedition-first-proof-checkpoint/goals/minimum-proof-core-first-expedition-proof/03_MINIMUM_EXPEDITION_PROOF_CORE.md"
  required_proof_slice_handoff: "directions/indie-game-development/domain_docs/game_documentation/expedition-proof-handoff.md"
  active_phase:
    phase_id: expedition-first-playable-proof-slice
    status: active
    next_route: G1_GOAL_SHAPE
```

## Blockers / required inputs

* Missing context: `none blocking for G1 after P0 repository maintenance apply/read-back`
* Human decision: `none pending`
* Source conflict: `none known after this patch is applied and read back`
* Tool/runtime blocker: `project/tool bindings must be verified before Codex product/project execution`
* Required attachments for next stage:
  * exact `workflow/stage_prompts/G1_GOAL_SHAPE.md`
  * current Project Files 00-06 after P0 read-back
  * active Phase Brief: `directions/indie-game-development/phases/expedition-first-playable-proof-slice/00_PHASE_BRIEF.md`
  * accepted proof core: `directions/indie-game-development/phases/expedition-first-proof-checkpoint/goals/minimum-proof-core-first-expedition-proof/03_MINIMUM_EXPEDITION_PROOF_CORE.md`
  * proof handoff: `directions/indie-game-development/domain_docs/game_documentation/expedition-proof-handoff.md`

## Current focus boundary

The accepted proof handoff/core already define what the first proof must test.

Next work must not silently turn proof-slice shaping into:

* another abstract readiness/boundary document;
* playable prototype implementation;
* code tasks;
* Codex product/project execution;
* exact cargo/carrying/death/lift/procgen/tool/economy/progression system design;
* Game Documentation promotion;
* Expedition versus Containment reopening.

G1 may shape a Goal that creates the smallest playable proof slice brief.

If G1 discovers that a blocking mechanics decision is required before slice shaping can continue, route to `S3_DECIDE` or another valid decision route instead of silently deciding it.