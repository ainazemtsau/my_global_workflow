# 01_DIRECTION_STATE.md

```yaml
project_file_control:
  file: 01_DIRECTION_STATE.md
  schema: project_file_projection.v1
  direction: directions/indie-game-development
  source_files:
    - "directions/indie-game-development/project_files/01_DIRECTION_STATE.md"
  activated_at: "2026-05-13"
  source_freshness: active_git_file_after_p0_repository_apply_readback
  canonical_source: GitHub repository file
  conflict_rule: if this file conflicts with another current GitHub Direction file, return Context Request; do not invent state
  default_load: yes
```

```yaml
direction:
  name: Indie Game Development
  id: indie_game_development
  state: active
  workflow_version: vNext-R
  current_phase_pointer: "directions/indie-game-development/phases/core-coop-technical-foundation-selection"
  active_goal_pointer: "directions/indie-game-development/phases/core-coop-technical-foundation-selection/goals/core-technical-foundation-decision-brief"
  active_goal_contract: "directions/indie-game-development/phases/core-coop-technical-foundation-selection/goals/core-technical-foundation-decision-brief/00_GOAL_CONTRACT.md"
  recommended_first_goal_candidate: null
  last_closed_phase_pointer: "directions/indie-game-development/phases/expedition-first-proof-checkpoint"
  last_closed_phase_result: p9_closed
  previous_active_phase_pointer: "directions/indie-game-development/phases/expedition-first-playable-proof-slice"
  previous_active_phase_status: paused_superseded_not_closed
  previous_active_goal_pointer: "directions/indie-game-development/phases/expedition-first-playable-proof-slice/goals/first-playable-proof-slice-brief"
  previous_active_goal_status: paused_superseded_partial_progress_not_accepted
  last_completed_goal_pointer: "directions/indie-game-development/phases/expedition-first-proof-checkpoint/goals/minimum-proof-core-first-expedition-proof"
  last_completed_goal_result: r1_reviewed_accepted
  accepted_goal_artifact: "directions/indie-game-development/phases/expedition-first-proof-checkpoint/goals/minimum-proof-core-first-expedition-proof/03_MINIMUM_EXPEDITION_PROOF_CORE.md"
  next_route: E1_EXECUTION_BRIEF
  last_updated: "2026-05-14"
```

## Purpose / thesis

Build a commercially viable indie game direction focused on Expedition product judgment, game meaning, clean technical base, durable documentation, and selective transfer from prior work.

## Durable commitments

- Expedition remains the active product hypothesis.
- The first proof should test game meaning and system synergy, not gas simulation alone.
- Gas-only proof remains rejected.
- This is a new project; old project material is evidence/source material, not automatic production base.
- Multiplayer technology and architecture are foundation decisions because the game is co-op.
- FishNet was used before but is not final for the new project until selected with evidence.
- Gas Simulation gameplay logic must be durable/extensible from the first real implementation, not hardcoded/disposable.
- Grid/Topology old modules may be transferable, but transfer requires audit and boundary decision.
- The active technical foundation Goal must use staged decision mapping, not one-shot closure of all technical details.
- Codex-driven development requires foundation-level engineering guardrails before implementation: modularity, testability, dependency/composition boundaries, validation gates, and separation of gameplay/domain logic from multiplayer transport.
- Game truths produced by Goals may move into permanent `Game Documentation` only through an explicit later documentation stage or approved documentation-maintenance patch.
- Codex product/project execution requires verified concrete project/tool bindings.

## Current Phase

- Phase: `Core Co-op Technical Foundation Selection`
- Path: `directions/indie-game-development/phases/core-coop-technical-foundation-selection`
- Status: `active_after_g1_goal_shape_pending_E1`
- Started by: `P0_PHASE_START`
- Started at: `2026-05-13`
- Current Critical Constraint: high-lock-in co-op technical foundation choices are unresolved.
- Minimum Outcome: accepted `Core Technical Foundation Decision Brief`.
- Validation Signal: accepted foundation decision covers multiplayer stack/architecture, Grid/Topology transfer boundary, Gas Simulation durable logic architecture, smallest durable technical nucleus, and explicit route gates for unresolved foundation surfaces.
- Active Goal: `core-technical-foundation-decision-brief`
- Active Goal Contract: `directions/indie-game-development/phases/core-coop-technical-foundation-selection/goals/core-technical-foundation-decision-brief/00_GOAL_CONTRACT.md`
- Next route: `E1_EXECUTION_BRIEF`

## Previous active Phase / Goal

- Phase: `Expedition First Playable Proof Slice`
- Path: `directions/indie-game-development/phases/expedition-first-playable-proof-slice`
- Status: `paused_superseded_not_closed`
- Reason: user challenged the bottleneck; playable-slice brief is premature until technical foundation selection is resolved.
- Goal: `first-playable-proof-slice-brief`
- Status: `paused_superseded_partial_progress_not_accepted`
- F0 artifact: preserved as scaffold/evidence, not accepted completion.
- P9 launched: `false`

## Last closed Phase

- Phase: `Expedition First Proof Checkpoint`
- Path: `directions/indie-game-development/phases/expedition-first-proof-checkpoint`
- Close stage: `P9_PHASE_CLOSE`
- Close result: `closed`
- Closed at: `2026-05-12`
- Next route after close: `P0_PHASE_START`

## Project Files export state

- Last refresh: `2026-05-13 after P0 repository maintenance apply/read-back`
- Required refresh: `before G1_GOAL_SHAPE`
- Current route: `G1_GOAL_SHAPE`
- Active Phase: `Core Co-op Technical Foundation Selection`
- Active Goal: `none_pending_G1`
