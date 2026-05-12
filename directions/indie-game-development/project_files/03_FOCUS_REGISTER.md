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
  current_focus: "Run E1_EXECUTION_BRIEF for the active Goal first-playable-proof-slice-brief."
  route_stage: E1_EXECUTION_BRIEF
  same_chat_allowed: false
  boundary_trigger: g1_goal_shape_after_repository_maintenance
  pending_state_carried: true
  pending_patch_pointer: g1_goal_shape_first_playable_proof_slice_brief_2026-05-12
  last_stage_result_pointer: "G1_GOAL_SHAPE shaped active Goal first-playable-proof-slice-brief."
  last_codex_scope_validation: "Codex repository maintenance only; Codex product/project execution remains blocked until project/tool bindings are verified."
  active_goal:
    goal_id: first-playable-proof-slice-brief
    goal_title: "Сформировать минимальный playable proof slice для Expedition"
    goal_path: "directions/indie-game-development/phases/expedition-first-playable-proof-slice/goals/first-playable-proof-slice-brief"
    goal_contract: "directions/indie-game-development/phases/expedition-first-playable-proof-slice/goals/first-playable-proof-slice-brief/00_GOAL_CONTRACT.md"
    status: active
  last_accepted_goal_artifact: "directions/indie-game-development/phases/expedition-first-proof-checkpoint/goals/minimum-proof-core-first-expedition-proof/03_MINIMUM_EXPEDITION_PROOF_CORE.md"
  required_proof_slice_handoff: "directions/indie-game-development/domain_docs/game_documentation/expedition-proof-handoff.md"
  active_phase:
    phase_id: expedition-first-playable-proof-slice
    status: active
    next_route: E1_EXECUTION_BRIEF
```

## Blockers / required inputs

* Missing context: `none blocking for E1 after G1 repository maintenance apply/read-back`
* Human decision: `none pending`
* Source conflict: `none known after this patch is applied and read back`
* Tool/runtime blocker: `project/tool bindings must be verified before Codex product/project execution`
* Required attachments for next stage:
  * exact `workflow/stage_prompts/E1_EXECUTION_BRIEF.md`
  * current Project Files 00-06 after G1 read-back
  * active Goal Contract: `directions/indie-game-development/phases/expedition-first-playable-proof-slice/goals/first-playable-proof-slice-brief/00_GOAL_CONTRACT.md`
  * active Phase Brief: `directions/indie-game-development/phases/expedition-first-playable-proof-slice/00_PHASE_BRIEF.md`
  * accepted proof core: `directions/indie-game-development/phases/expedition-first-proof-checkpoint/goals/minimum-proof-core-first-expedition-proof/03_MINIMUM_EXPEDITION_PROOF_CORE.md`
  * proof handoff: `directions/indie-game-development/domain_docs/game_documentation/expedition-proof-handoff.md`

## Current focus boundary

The accepted proof handoff/core already define what the first proof must test.

The active Goal is now `first-playable-proof-slice-brief`.

Next work must not silently turn E1 execution briefing into:

* another abstract readiness/boundary document;
* playable prototype implementation;
* code tasks;
* Codex product/project execution;
* exact cargo/carrying/death/lift/procgen/tool/economy/progression system design;
* Game Documentation promotion;
* Expedition versus Containment reopening.

E1 may produce the minimum execution brief required to create the `First Playable Proof Slice Brief`.

If E1 discovers that a blocking mechanics decision is required before slice brief creation can continue, route to `S3_DECIDE` or another valid decision route instead of silently deciding it.
