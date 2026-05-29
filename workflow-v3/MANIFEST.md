---
artifact_control:
  namespace: workflow_v3
  artifact_type: manifest
  status: candidate
  owner: workflow_governance
  authority: candidate_parallel_runtime_not_active
---

# Workflow v3 Manifest

This file is candidate v3 design material. It is not active Workflow OS authority and does not supersede `workflow/**`.

## Status

- `workflow-v3/**` is a candidate parallel design namespace.
- Status: candidate-only.
- Design role: parallel runtime design.
- Active authority: none.
- The active Workflow OS remains outside this scaffold.
- This scaffold does not mutate existing `directions/**`.

## Authority Boundary

- `workflow-v3/**` is review material, not process authority.
- It does not supersede `workflow/**`.
- It does not create accepted receipts, ledgers, obligations, project state, or Direction runtime state.
- It does not authorize product execution.
- It does not modify ChatGPT Project Instructions, project packs, source manifests, or request-only source sets.

## File Inventory

- `workflow-v3/MANIFEST.md`: scaffold index and safety boundary.
- `workflow-v3/README.md`: clean runtime concept and continuation model.
- `workflow-v3/core/00_CLEAN_RUNTIME_OVERVIEW.md`: architecture overview.
- `workflow-v3/core/01_DIRECTION_CONTROL.md`: root control surface.
- `workflow-v3/core/02_ACTIVE_FRONT_AND_LOCAL_MAPS.md`: active-front and local-map rules.
- `workflow-v3/core/03_NODE_LIFECYCLE.md`: node model, statuses, and closeout.
- `workflow-v3/core/04_MEMORY_SYSTEM.md`: memory scopes and promotion rules.
- `workflow-v3/core/05_EVENT_REVIEW_PATCH_SYSTEM.md`: events, reviews, and patches.
- `workflow-v3/core/06_PARALLEL_CHAT_RUNTIME.md`: parent-controlled parallel chat work.
- `workflow-v3/core/07_EXECUTION_AND_VALIDATION_BOUNDARY.md`: route, execution, and validation rules.
- `workflow-v3/core/08_LEGACY_BOUNDARY_AND_IMPORT.md`: preservation and future import boundary.
- `workflow-v3/templates/CONTINUATION_PACKET.md`: restart packet template.
- `workflow-v3/templates/CHILD_CHAT_PACKET.md`: child work packet template.
- `workflow-v3/templates/RESULT_REPORT.md`: result report template.
- `workflow-v3/templates/REVIEW_JOB.md`: review job template.
- `workflow-v3/templates/PATCH_PROPOSAL.md`: patch proposal template.
- `workflow-v3/templates/PARENT_INTEGRATION_REVIEW.md`: parent review template.
- `workflow-v3/templates/NODE_CLOSEOUT.md`: node closeout template.
- `workflow-v3/pilots/indie-game-development/README.md`: candidate pilot sketch.

## Preservation Boundary

- Legacy/current workflow data preserved in place.
- Old data may be imported later only by explicit import/review.
- Current workflow artifacts remain available as evidence.
- This scaffold does not move, delete, rename, rewrite, or reinterpret existing workflow files.
- Import is selective, reviewed, and recorded as a future action.

## Development Sequence

1. Review candidate architecture and boundaries.
2. Test the continuation, child work, result report, review, patch, parent integration, and closeout templates on a disposable pilot.
3. Define explicit import/review rules before reusing any legacy/current data.
4. Validate whether v3 reduces documentation loops and improves long-running project continuation.
5. Only after review, propose any separate migration plan outside this scaffold.

END_OF_FILE: workflow-v3/MANIFEST.md
