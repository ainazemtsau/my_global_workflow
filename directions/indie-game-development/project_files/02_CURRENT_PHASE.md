# 02\_CURRENT\_PHASE.md

```yaml
project_file_control:
  file: 02_CURRENT_PHASE.md
  schema: project_file_projection.v1
  direction: directions/indie-game-development
  source_files:
    - "directions/indie-game-development/project_files/02_CURRENT_PHASE.md"
  activated_at: "2026-05-11"
  source_freshness: active_git_file
  canonical_source: GitHub repository file
  conflict_rule: if this file conflicts with another current GitHub Direction file, return Context Request; do not invent state
  default_load: yes

```

```yaml
current_phase:
  state: active
  phase_name: Expedition First Proof Checkpoint
  phase_path: "directions/indie-game-development/phases/expedition-first-proof-checkpoint"
  critical_constraint: "Preserve current Expedition checkpoint and Game Documentation while using vNext-R structure."
  minimum_outcome: "Active Phase exists, active Goal is preserved under it, next route is Goal shaping."

```

## Guard state

*   Active Goal unresolved: `yes, requires G1_GOAL_SHAPE before execution`
*   Phase can close now: `no`
*   Blocker: `Goal Contract needs shaping and project/tool bindings need verification before Codex execution.`
