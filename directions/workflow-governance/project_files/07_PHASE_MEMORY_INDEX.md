# 07 Phase Memory Index - Workflow Governance

```yaml
artifact_control:
  artifact_name: "07 Phase Memory Index - Workflow Governance"
  schema: phase_memory_index.v1
  owner_layer: persistence
  status: canonical
  repo_path: "directions/workflow-governance/project_files/07_PHASE_MEMORY_INDEX.md"
  default_load: yes
  freshness: fresh
  last_updated: "2026-05-15"

phase_memory_status:
  latest_closed_phase_id: null
  latest_closed_phase_name: null
  latest_closed_phase_summary_path: null
  latest_closed_at: null
  history_backfill_status: no_closed_phase_history_to_backfill
  current_phase_id: workflow_steward_bootstrap
  current_phase_type: maintenance_container
```

## Purpose

Compact default-loaded Phase Memory Bridge for Workflow Governance.

Use this file before creating a materially new normal lifecycle Phase after a Phase close.

Workflow Governance currently operates as an ongoing maintenance workbench. The current `workflow_steward_bootstrap` phase is an active maintenance container, not a closed lifecycle phase.

Do not use old chats, execution logs, or migration/admin docs as a substitute for this index.

## Closed phase ledger

No closed Workflow Governance Phase has been recorded yet.

Therefore there is no closed-phase summary to backfill.

## Current maintenance container

Current container:

```text
workflow_steward_bootstrap
```

Interpretation:

- active maintenance workbench container;
- supports iterative workflow audit/repair/cleanup across chats;
- does not require an Active Goal for maintenance work;
- does not require `P0_PHASE_START`, `G0_GOAL_SELECT`, or `G1_GOAL_SHAPE` unless the user explicitly asks for normal lifecycle operation.

## Open carryovers

- Continue iterative workflow maintenance through natural-language issue/request -> audit or patch plan -> approval -> Codex apply/read-back -> validation.
- Report Project Files / Project Instructions refresh requirements whenever changed files affect ChatGPT Project runtime cache.
- Keep runtime core split deferred until a separate read-only design audit and explicit patch approval.
- Keep Workflow Governance separate from product/project execution Directions.
- Use GitHub repository files as source of truth; Project Files are runtime cache only.

## Do-not-repeat / duplicate patterns

- Do not force `G0_GOAL_SELECT`, `G1_GOAL_SHAPE`, or `P0_PHASE_START` merely because Active Goal is `none`.
- Do not patch before explicit approval unless the user directly asks Codex to execute an approved change.
- Do not treat Project Files cache as source of truth when verified GitHub read-back disagrees.
- Do not split shared runtime files without cross-Direction rollout analysis.
- Do not create fake closed Phase history from old chats or migration/admin notes.

## Recommended next phase candidates

These are candidates only if the user explicitly asks to run normal lifecycle planning:

- Runtime Split Design / Contract Modularization.
- Governance Audit Loop Establishment.
- Workflow Usage Friction Evaluation.
- Phase Memory / lifecycle hygiene hardening.

## Recommended next phase not

- Do not start a new normal lifecycle Phase just to continue maintenance work.
- Do not close `workflow_steward_bootstrap` without an explicit phase-close request and source-backed closure evidence.
- Do not start runtime core split as a blind large patch.
- Do not duplicate previous cleanup cycles without a concrete delta.

## Detail pointers

No detailed `phase_close_summary.md` exists because no Workflow Governance Phase has been closed.

If `workflow_steward_bootstrap` is later closed through normal lifecycle operation, create a proper phase close summary under:

```text
directions/workflow-governance/phases/workflow_steward_bootstrap/phase_close_summary.md
```

## End-of-file marker

`END_OF_FILE: directions/workflow-governance/project_files/07_PHASE_MEMORY_INDEX.md`
