# 02_CURRENT_PHASE.md

```yaml
project_file_control:
  file: 02_CURRENT_PHASE.md
  schema: project_file_projection.v1
  direction: directions/indie-game-development
  source_files:
    - "directions/indie-game-development/project_files/02_CURRENT_PHASE.md"
  activated_at: "2026-05-12"
  source_freshness: active_git_file
  canonical_source: GitHub repository file
  conflict_rule: if this file conflicts with another current GitHub Direction file, return Context Request; do not invent state
  default_load: yes
```

```yaml
current_phase:
  state: active
  phase_name: Expedition First Proof Checkpoint
  phase_id: expedition-first-proof-checkpoint
  phase_path: "directions/indie-game-development/phases/expedition-first-proof-checkpoint"
  critical_constraint: "Preserve current Expedition checkpoint and Game Documentation while using vNext-R structure."
  minimum_outcome: "Accepted minimum proof core exists for the first Expedition proof; Phase Progress Gate must determine whether this satisfies the current Phase Minimum Outcome or whether required Phase work remains."
  next_route: phase_progress_gate_check

phase_progress_gate:
  last_completed_goal: minimum-proof-core-first-expedition-proof
  last_completed_goal_path: "directions/indie-game-development/phases/expedition-first-proof-checkpoint/goals/minimum-proof-core-first-expedition-proof"
  gate_status: "missing / needs_check"
  current_next_route: phase_progress_gate_check
  no_phase_auto_close: true
  g0_allowed_only_after: continue_with_required_goals
  phase_continue_decision_required: true
```

## Guard state

* Active Goal unresolved: `no`
* Active Goal: `none`
* Last completed Goal: `Определить минимальное доказательное ядро первого proof Expedition`
* Last completed Goal status: `r1_reviewed_accepted`
* Accepted artifact: `directions/indie-game-development/phases/expedition-first-proof-checkpoint/goals/minimum-proof-core-first-expedition-proof/03_MINIMUM_EXPEDITION_PROOF_CORE.md`
* Phase can close now: `not automatically; requires Phase Progress Gate and P9/Human Decision when closure is plausible`
* Blocker: `none for the reviewed proof-core Goal`
* Tool/runtime blocker: `Codex product/project execution still requires verified concrete project/tool bindings before any product/project work.`

## Current phase meaning

The Phase remains active. One checkpoint Goal has completed: the minimum proof core for Expedition has been accepted.

The next safe workflow route is `phase_progress_gate_check`, not blind `G0_GOAL_SELECT`.

G0 is allowed only after `continue_with_required_goals` / Phase Continue decision confirms that required Phase work remains. This file does not close the Phase automatically.
