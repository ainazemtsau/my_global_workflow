# 07 Phase Memory Index - Indie Game Development

```yaml
artifact_control:
  artifact_name: "07 Phase Memory Index - Indie Game Development"
  schema: phase_memory_index.v1
  owner_layer: persistence
  status: canonical
  repo_path: "directions/indie-game-development/project_files/07_PHASE_MEMORY_INDEX.md"
  default_load: yes
  freshness: fresh_after_p9_project_bootstrap_validation_surface_setup_close
  last_updated: "2026-05-22"

phase_memory_status:
  latest_closed_phase_id: project-bootstrap-validation-surface-setup
  latest_closed_phase_name: "Project Bootstrap and Validation Surface Setup"
  latest_closed_phase_summary_path: "directions/indie-game-development/phases/project-bootstrap-validation-surface-setup/phase_close_summary.md"
  latest_closed_at: "2026-05-22"
  history_backfill_status: partial
```

## Purpose

Compact default-loaded Phase Memory Bridge for Indie Game Development.

Use this file before creating a materially new Phase after a Phase close. Do not use old chats, execution logs, or archived material as a substitute for this index.

## Closed phase ledger

### expedition-first-proof-checkpoint

```yaml
phase_id: expedition-first-proof-checkpoint
phase_name: "Expedition First Proof Checkpoint"
status: closed_by_P9
started_at: unknown_from_available_index
closed_at: unknown_from_available_index
critical_constraint: unknown_from_available_index
minimum_outcome: unknown_from_available_index
completion_verdict: "closed_by_P9 according to current 06_CONTEXT_LIBRARY_INDEX.md"
delivered_outcomes:
  - "Minimum proof-core artifact accepted by R1 and closed by P9."
durable_decisions:
  - "Closed phase remains request-only context, not default archive loading."
files_or_docs_created:
  - "directions/indie-game-development/phases/expedition-first-proof-checkpoint/00_PHASE_BRIEF.md"
  - "directions/indie-game-development/phases/expedition-first-proof-checkpoint/05_PHASE_REVIEW.md"
  - "directions/indie-game-development/phases/expedition-first-proof-checkpoint/phase_execution_log.md"
  - "directions/indie-game-development/phases/expedition-first-proof-checkpoint/goals/minimum-proof-core-first-expedition-proof/03_MINIMUM_EXPEDITION_PROOF_CORE.md"
carryovers:
  - "Use accepted minimum proof-core artifact only when shaping the next proof-related Phase or Goal."
do_not_repeat:
  - "Do not treat the accepted proof-core artifact as a prototype design, implementation plan, Game Documentation promotion, or Codex execution brief."
duplicate_phase_patterns_to_avoid:
  - "Do not recreate Expedition First Proof Checkpoint as a new Phase without a concrete delta."
recommended_next_phase_candidates:
  - "Not backfilled. Requires P0 review of current Direction state and this Phase Memory Index."
recommended_next_phase_not:
  - "Do not create a duplicate Expedition First Proof Checkpoint."
close_summary_path: "directions/indie-game-development/phases/expedition-first-proof-checkpoint/phase_close_summary.md"
evidence_pointer:
  - "directions/indie-game-development/project_files/06_CONTEXT_LIBRARY_INDEX.md"
backfill_quality: partial
```

### core-coop-technical-foundation-selection

```yaml
phase_id: core-coop-technical-foundation-selection
phase_name: "Core Co-op Technical Foundation Selection"
status: closed_complete_by_P9
started_at: "2026-05-13"
closed_at: "2026-05-21"
critical_constraint: "The Direction could not safely move toward the playable technical nucleus while foundation choices and Codex-development architecture protocols were not reconciled into an accepted, reviewable foundation decision."
minimum_outcome: "Accepted or review-routed Core Technical Foundation Decision Brief / Decision Map plus enough specification/profile/readiness evidence to route next lifecycle work without guessing."
completion_verdict: "closed_complete_by_P9"
delivered_outcomes:
  - accepted Core Technical Foundation Decision Brief / Decision Map
  - accepted First Technical Nucleus Functional Specification
  - accepted Gas Coop Game Project Execution Profile
  - accepted H1_G3 readiness packet
durable_decisions:
  - "Unity bootstrap, product repository creation, product code, Codex product/project execution, Task Master graph creation, real internal tool setup, Unity MCP setup, old-code transfer, and Game Documentation promotion remain blocked until later basis-valid route."
  - "Old project material remains reference/evidence only."
  - "P0_PHASE_START is the next lifecycle route after Phase close."
files_or_docs_created:
  - directions/indie-game-development/phases/core-coop-technical-foundation-selection/phase_close_summary.md
  - directions/indie-game-development/phases/core-coop-technical-foundation-selection/goals/core-technical-foundation-decision-brief/04_CORE_TECHNICAL_FOUNDATION_DECISION_BRIEF.md
  - directions/indie-game-development/phases/core-coop-technical-foundation-selection/goals/first-technical-nucleus-functional-spec/01_FIRST_TECHNICAL_NUCLEUS_FUNCTIONAL_SPEC.md
  - directions/indie-game-development/phases/core-coop-technical-foundation-selection/goals/codex-development-operating-model-and-architecture-protocols/01_GAS_COOP_GAME_PROJECT_EXECUTION_PROFILE.md
  - directions/indie-game-development/phases/core-coop-technical-foundation-selection/goals/project-bootstrap-tool-binding-validation-scene-readiness/00_GOAL_CONTRACT.md
  - directions/indie-game-development/phases/core-coop-technical-foundation-selection/goals/project-bootstrap-tool-binding-validation-scene-readiness/execution_log.md
carryovers:
  - "P0 must decide the next Phase from Phase Memory + Direction Map, not by repeating foundation selection."
  - "P0 must preserve no-product-execution boundary until E1/X0/X1 readiness is proven."
do_not_repeat:
  - "Do not recreate Core Co-op Technical Foundation Selection without a concrete new delta."
  - "Do not treat readiness packet as product execution approval."
duplicate_phase_patterns_to_avoid:
  - "Broad foundation/planning phase that repeats accepted decision/spec/profile/readiness work."
recommended_next_phase_candidates:
  - "P0 candidate only: project bootstrap / validation surface setup."
  - "P0 candidate only: durable technical nucleus implementation readiness."
  - "P0 candidate only: bounded H1_G4 durable technical nucleus execution envelope."
recommended_next_phase_not:
  - "Do not start direct product execution, old-code transfer, broad commercialization, or Game Documentation promotion as the next Phase."
close_summary_path: "directions/indie-game-development/phases/core-coop-technical-foundation-selection/phase_close_summary.md"
evidence_pointer:
  - "directions/indie-game-development/project_files/02_CURRENT_PHASE.md"
  - "directions/indie-game-development/project_files/08_DIRECTION_MAP.md"
  - "directions/indie-game-development/phases/core-coop-technical-foundation-selection/phase_close_summary.md"
backfill_quality: current_phase_fresh
```

### project-bootstrap-validation-surface-setup

```yaml
phase_id: project-bootstrap-validation-surface-setup
phase_name: "Project Bootstrap and Validation Surface Setup"
status: closed_complete_by_P9
started_at: "2026-05-21"
closed_at: "2026-05-22"
critical_constraint: "The Direction could not safely proceed from accepted H1_G3 readiness into durable technical nucleus work until concrete project setup boundaries, tool-binding route, validation surfaces, stop rules, and allowed execution route were selected and scoped."
minimum_outcome: "Accepted or route-gated project bootstrap / validation-surface setup envelope."
completion_verdict: "closed_complete_by_P9"
delivered_outcomes:
  - "Accepted setup/validation envelope: bootstrap-validation-surface-setup-envelope."
  - "Phase close summary created."
  - "Direction runtime projection updated for P0_PHASE_START."
durable_decisions:
  - "The setup/validation envelope satisfies this Phase minimum outcome."
  - "P0_PHASE_START is the next lifecycle route after repository maintenance and manual Project Files refresh."
  - "Unity bootstrap, product repository creation, product code, Codex product/project execution, Task Master graph creation, Unity MCP setup, old-code transfer, and Game Documentation promotion remain blocked."
files_or_docs_created:
  - directions/indie-game-development/phases/project-bootstrap-validation-surface-setup/phase_close_summary.md
  - directions/indie-game-development/phases/project-bootstrap-validation-surface-setup/goals/bootstrap-validation-surface-setup-envelope/01_BOOTSTRAP_VALIDATION_SURFACE_SETUP_ENVELOPE.md
  - directions/indie-game-development/phases/project-bootstrap-validation-surface-setup/goals/bootstrap-validation-surface-setup-envelope/execution_log.md
carryovers:
  - "P0 must select or reframe the next Phase using Phase Memory and Direction Map."
  - "Manual Project Files refresh is required before the next material run."
  - "H1_G4 durable technical nucleus remains premature until P0/G1/E1 or a later route selects and scopes it."
do_not_repeat:
  - "Do not recreate the setup/validation envelope as a new Phase without a concrete new delta."
  - "Do not treat the accepted envelope as product execution approval."
duplicate_phase_patterns_to_avoid:
  - "Broad planning phase that restates accepted foundation/spec/profile/readiness/envelope work."
  - "Bootstrap readiness phase that repeats the accepted setup/validation envelope."
recommended_next_phase_candidates:
  - "P0 candidate only: H1_G4 durable technical nucleus implementation readiness."
  - "P0 candidate only: bounded durable technical nucleus setup/execution envelope."
  - "P0 candidate only: route-gated project setup validation campaign."
recommended_next_phase_not:
  - "Do not start direct Unity bootstrap, product repository creation, product code, Codex product/project execution, Task Master graph creation, Unity MCP setup, old-code transfer, or Game Documentation promotion."
close_summary_path: "directions/indie-game-development/phases/project-bootstrap-validation-surface-setup/phase_close_summary.md"
evidence_pointer:
  - "directions/indie-game-development/phases/project-bootstrap-validation-surface-setup/phase_close_summary.md"
  - "directions/indie-game-development/phases/project-bootstrap-validation-surface-setup/00_PHASE_BRIEF.md"
  - "directions/indie-game-development/phases/project-bootstrap-validation-surface-setup/goals/bootstrap-validation-surface-setup-envelope/execution_log.md"
  - "directions/indie-game-development/project_files/08_DIRECTION_MAP.md"
backfill_quality: current_phase_fresh
```

## Open carryovers

- Use accepted minimum proof-core artifact only when shaping the next proof-related Phase or Goal.
- Load detail files before creating a new proof-related Phase if the compact index is insufficient.
- P0 must decide the next Phase from Phase Memory + Direction Map, not by repeating foundation selection.
- P0 must preserve no-product-execution boundary until E1/X0/X1 readiness is proven.
- P0 must not repeat Project Bootstrap and Validation Surface Setup; it must select a concrete new phase-level delta after this Phase closure.
- H1_G4 durable technical nucleus remains premature until a later route selects and scopes it.

## Do-not-repeat / duplicate patterns

- Do not create a new Phase that merely repeats Expedition First Proof Checkpoint.
- Do not treat accepted proof-core artifact as prototype design, implementation plan, Game Documentation promotion, or Codex execution brief.
- Do not recreate Core Co-op Technical Foundation Selection without a concrete new delta.
- Do not treat readiness packet as product execution approval.
- Do not create a broad foundation/planning phase that repeats accepted decision/spec/profile/readiness work.
- Do not recreate Project Bootstrap and Validation Surface Setup without a concrete new delta.
- Do not treat the accepted setup/validation envelope as product execution approval.

## Recommended next phase candidates

- P0 candidate only: project bootstrap / validation surface setup.
- P0 candidate only: durable technical nucleus implementation readiness.
- P0 candidate only: bounded H1_G4 durable technical nucleus execution envelope.
- P0 candidate only: route-gated project setup validation campaign, if P0 proves setup must be separated from implementation.

## Recommended next phase not

- Do not create a duplicate Expedition First Proof Checkpoint.
- Do not start direct product execution, old-code transfer, broad commercialization, or Game Documentation promotion as the next Phase.
- Do not start direct Unity bootstrap, product repository creation, product code, Codex product/project execution, Task Master graph creation, or Unity MCP setup as the next Phase.

## Detail pointers

- `directions/indie-game-development/phases/expedition-first-proof-checkpoint/phase_close_summary.md`
- `directions/indie-game-development/phases/expedition-first-proof-checkpoint/00_PHASE_BRIEF.md`
- `directions/indie-game-development/phases/expedition-first-proof-checkpoint/05_PHASE_REVIEW.md`
- `directions/indie-game-development/phases/expedition-first-proof-checkpoint/phase_execution_log.md`
- `directions/indie-game-development/phases/expedition-first-proof-checkpoint/goals/minimum-proof-core-first-expedition-proof/03_MINIMUM_EXPEDITION_PROOF_CORE.md`
- `directions/indie-game-development/phases/core-coop-technical-foundation-selection/phase_close_summary.md`
- `directions/indie-game-development/phases/core-coop-technical-foundation-selection/00_PHASE_BRIEF.md`
- `directions/indie-game-development/phases/core-coop-technical-foundation-selection/phase_execution_log.md`
- `directions/indie-game-development/phases/project-bootstrap-validation-surface-setup/phase_close_summary.md`
- `directions/indie-game-development/phases/project-bootstrap-validation-surface-setup/00_PHASE_BRIEF.md`
- `directions/indie-game-development/phases/project-bootstrap-validation-surface-setup/goals/bootstrap-validation-surface-setup-envelope/execution_log.md`
