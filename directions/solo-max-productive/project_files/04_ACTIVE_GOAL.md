# 04_ACTIVE_GOAL.md

```yaml
artifact_control:
  artifact_name: "04 Active Goal"
  schema: active_goal.v1
  owner_layer: persistence
  status: projection
  source_file: "directions/solo-max-productive/project_files/04_ACTIVE_GOAL.md"
  default_load: yes
  freshness: fresh
  last_refresh_at: "2026-05-13"
  refresh_source: "B1-2026-05-13-active-goal-misframed-recovery"

active_goal:
  state: contested_superseded_pending_replacement
  goal_id: personal-workflow-app-kernel-min-proof
  goal_name: Personal Workflow App Kernel Min Proof
  goal_path: "directions/solo-max-productive/phases/personal-workflow-app-kernel-exploration/goals/personal-workflow-app-kernel-min-proof"
  phase_path: "directions/solo-max-productive/phases/personal-workflow-app-kernel-exploration"
  current_wave: none
  next_route: G1_GOAL_SHAPE
  invalidation_reason: "The Goal asks for a Kernel Min Proof Brief, but the user states the current ChatGPT + GitHub + Codex workflow has already proven the kernel/workflow loop enough. The next useful Goal is core/base system or MVP definition."

replacement_goal_candidate:
  id: G1-CAND-2026-05-13-SYSTEM-CORE-MVP
  name: Personal Workflow System Core and MVP Definition
  status: proposed_needs_g1_shape
  expected_route: G1_GOAL_SHAPE
  expected_intent: "Define the smallest core/base personal workflow system or MVP that can become more useful than the current workflow while preserving the kernel loop."

stale_previous_candidate:
  name: Create Lightweight Codex Small-Fix Lane
  status: superseded_not_current
  reactivation_rule: "Only continue if the user explicitly reactivates it."
```

## Active Goal summary

The old active Goal is preserved as superseded/replaced provenance.

It must not proceed to `E1_EXECUTION_BRIEF`, and `03_KERNEL_MIN_PROOF_BRIEF.md` must not be created.

The next valid step is `G1_GOAL_SHAPE` for `Personal Workflow System Core and MVP Definition`.

Core principle preserved: future LLMs are upgradable cognitive engines; the kernel is the persistent substrate of context, memory, tools, surfaces, feedback loops, rules, and Reality Alignment mechanisms.
