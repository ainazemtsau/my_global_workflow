# 07 Phase Memory Index - Indie Game Development

```yaml
artifact_control:
  artifact_name: "07 Phase Memory Index - Indie Game Development"
  schema: phase_memory_index.v1
  owner_layer: persistence
  status: canonical
  repo_path: "directions/indie-game-development/project_files/07_PHASE_MEMORY_INDEX.md"
  default_load: yes
  freshness: fresh
  last_updated: "2026-05-12"

phase_memory_status:
  latest_closed_phase_id: expedition-first-proof-checkpoint
  latest_closed_phase_name: "Expedition First Proof Checkpoint"
  latest_closed_phase_summary_path: "directions/indie-game-development/phases/expedition-first-proof-checkpoint/phase_close_summary.md"
  latest_closed_at: unknown_from_available_index
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

## Open carryovers

- Use accepted minimum proof-core artifact only when shaping the next proof-related Phase or Goal.
- Load detail files before creating a new proof-related Phase if the compact index is insufficient.

## Do-not-repeat / duplicate patterns

- Do not create a new Phase that merely repeats Expedition First Proof Checkpoint.
- Do not treat accepted proof-core artifact as prototype design, implementation plan, Game Documentation promotion, or Codex execution brief.

## Recommended next phase candidates

- Not backfilled. P0 must decide from current Direction state and the compact phase memory.

## Recommended next phase not

- Do not create a duplicate Expedition First Proof Checkpoint.

## Detail pointers

- `directions/indie-game-development/phases/expedition-first-proof-checkpoint/phase_close_summary.md`
- `directions/indie-game-development/phases/expedition-first-proof-checkpoint/00_PHASE_BRIEF.md`
- `directions/indie-game-development/phases/expedition-first-proof-checkpoint/05_PHASE_REVIEW.md`
- `directions/indie-game-development/phases/expedition-first-proof-checkpoint/phase_execution_log.md`
- `directions/indie-game-development/phases/expedition-first-proof-checkpoint/goals/minimum-proof-core-first-expedition-proof/03_MINIMUM_EXPEDITION_PROOF_CORE.md`