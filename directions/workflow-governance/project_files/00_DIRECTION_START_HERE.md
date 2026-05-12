# 00 START HERE - Workflow Governance

```yaml
artifact_control:
  artifact_name: "00 START HERE - Workflow Governance"
  schema: direction_start_here.v1
  owner_layer: persistence
  status: canonical
  repo_path: "directions/workflow-governance/project_files/00_DIRECTION_START_HERE.md"
  default_load: yes
  freshness: fresh
  last_updated: "2026-05-12"
  next_action: "Use G0_GOAL_SELECT for a concrete stewardship goal, or run Workflow Steward Audit when the user asks for audit."
```

## Direction identity

- Direction name: `Workflow Governance`
- Direction ID: `workflow_governance`
- Current state: `active`
- Workflow version: `vNext-R`
- Source of truth: GitHub repository markdown

## Purpose / thesis

Maintain and improve Workflow vNext-R through iterative workflow auditing, research, findings, evaluation, decision records, and controlled improvement proposals.

Workflow Governance is separate from Solo Max Productive and real product/game Directions.

## Source-of-truth rule

This file is an active GitHub Direction runtime file. `WORKFLOW_SOURCE_OF_TRUTH.md` is the active source-of-truth marker. If required state is missing, stale, or conflicting, return Context Request; do not invent state.

## Current pointers

| Pointer | Value | Canonical target |
| --- | --- | --- |
| Current Phase | `Workflow Steward Bootstrap` | `directions/workflow-governance/project_files/02_CURRENT_PHASE.md` |
| Active Goal | `none` | `directions/workflow-governance/project_files/04_ACTIVE_GOAL.md` |
| Findings register | `FINDING_REGISTER` | `directions/workflow-governance/findings/FINDING_REGISTER.md` |
| Evaluation suite | `WORKFLOW_EVAL_SUITE` | `directions/workflow-governance/evals/WORKFLOW_EVAL_SUITE.md` |
| Audit launch prompt | `Workflow Steward Audit` | `directions/workflow-governance/audits/WORKFLOW_STEWARD_AUDIT_LAUNCH_PROMPT.md` |
| Context load rules | Direction Context Loading Index | `directions/workflow-governance/project_files/06_CONTEXT_LIBRARY_INDEX.md` |

## Default Project Files to load

1. `00_DIRECTION_START_HERE.md`
2. `01_DIRECTION_STATE.md`
3. `02_CURRENT_PHASE.md`
4. `03_FOCUS_REGISTER.md`
5. `04_ACTIVE_GOAL.md`
6. `05_PORTFOLIO_QUEUE.md`
7. `06_CONTEXT_LIBRARY_INDEX.md`

## Shared runtime file

Load shared runtime core separately from `workflow/runtime/WF_VNEXT_R_RUNTIME_CORE.md`.

Do not create or require a local runtime-core copy under this Direction `project_files/` folder.

## Normal next route

- Use `G0_GOAL_SELECT` when the user wants to choose a concrete Workflow Governance goal.
- Use `Workflow Steward Audit` when the user asks for audit, research, findings, evaluation, or controlled improvement proposals.
- No repository patch until approval.
- No product/project execution.
