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
  current_focus: "Run P9_PHASE_CLOSE for Expedition First Proof Checkpoint after corrected R1 Phase Progress Gate selected formal Phase close."
  route_stage: P9_PHASE_CLOSE
  same_chat_allowed: false
  boundary_trigger: phase_close
  pending_state_carried: true
  pending_patch_pointer: r1_corrected_phase_progress_gate_to_p9_2026-05-12
  last_stage_result_pointer: "Corrected R1_GOAL_REVIEW_DISTILL accepted minimum proof-core Goal and superseded old G0 route."
  last_codex_scope_validation: "Codex repository maintenance only; Codex product/project execution remains blocked until project/tool bindings are verified."
  last_accepted_goal_artifact: "directions/indie-game-development/phases/expedition-first-proof-checkpoint/goals/minimum-proof-core-first-expedition-proof/03_MINIMUM_EXPEDITION_PROOF_CORE.md"
  phase_progress_gate:
    last_completed_goal: minimum-proof-core-first-expedition-proof
    gate_status: "closure_selected_by_human"
    next_route: P9_PHASE_CLOSE
    no_phase_auto_close: true
    g0_allowed_only_after: P9_handoff_or_explicit_phase_continue_decision
```

## Blockers / required inputs

* Missing context: `none blocking for corrected R1; P9 prompt and Phase files required before running P9`
* Human decision: `completed; selected p9_phase_close_review`
* Source conflict: `old G0 route superseded by corrected R1 Phase Progress Gate after this patch is applied and read back`
* Tool/runtime blocker: `project/tool bindings must be verified before Codex product/project execution`
* Required attachments for next stage: exact `workflow/stage_prompts/P9_PHASE_CLOSE.md`, current Project Files 00-06, Phase Brief, Phase Working Context, Phase Review, accepted proof-core artifact, and Goal execution log after read-back.

## Current focus boundary

The accepted proof-core artifact is not a prototype design and not an implementation plan.

Next work must not skip Phase Progress Gate or silently turn the accepted proof core into:
* playable proof design;
* prototype scene specification;
* code tasks;
* exact cargo/carrying/death/lift/procgen/tool/economy/progression decisions;
* Game Documentation promotion;
* Codex product/project execution.
