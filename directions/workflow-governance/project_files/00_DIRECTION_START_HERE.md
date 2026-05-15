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
  next_action: "Use Workflow Governance Maintenance Mode for workflow audit/repair/cleanup. Use G0_GOAL_SELECT only when the user explicitly asks for normal Goal lifecycle operation."
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

Workflow Governance should be run in a separate ChatGPT Project, not the old Workflow Rebuild Project.

## Workflow Governance Maintenance Mode

Workflow Governance is the maintenance workbench for the shared workflow layer.

Use this Project for iterative workflow governance work such as:

- workflow audit;
- workflow repair;
- cleanup;
- source-of-truth review;
- routing repair;
- prompt-boundary repair;
- transport/schema cleanup;
- cache/setup consistency work;
- validation hardening;
- Codex repository maintenance.

This maintenance work may be performed across many separate chats using the maintenance loop:

```text
natural-language issue/request
-> inspect relevant workflow files
-> produce findings and patch plan
-> wait for approval
-> prepare Codex repository maintenance apply/read-back card
-> validate Codex return evidence
-> continue with the next focused audit/fix cycle
```

In direct maintenance mode:

- accept natural-language maintenance requests;
- inspect the relevant workflow files;
- produce findings and patch plans;
- wait for approval before repository patch operations unless the user directly asks Codex to execute the changes;
- prepare Codex repository maintenance apply/read-back cards after approval;
- validate Codex return evidence;
- report Project Files / Project Instructions refresh requirements.

Do not route to `G0_GOAL_SELECT`, `G1_GOAL_SHAPE`, `P0_PHASE_START`, or another lifecycle stage merely because Active Goal is `none`.

Use normal workflow lifecycle stages only when the user explicitly asks to run Workflow Governance as a normal Direction lifecycle.

The current `Workflow Steward Bootstrap` Phase is a maintenance container for this workbench. It is not a requirement to run every maintenance task through the normal lifecycle.

## Current pointers

| Pointer | Value | Canonical target |
| --- | --- | --- |
| Current Phase | `Workflow Steward Bootstrap` | `directions/workflow-governance/project_files/02_CURRENT_PHASE.md` |
| Active Goal | `none` | `directions/workflow-governance/project_files/04_ACTIVE_GOAL.md` |
| Findings register | `FINDING_REGISTER` | `directions/workflow-governance/findings/FINDING_REGISTER.md` |
| Evaluation suite | `WORKFLOW_EVAL_SUITE` | `directions/workflow-governance/evals/WORKFLOW_EVAL_SUITE.md` |
| Audit launch prompt | `Workflow Steward Audit` | `directions/workflow-governance/audits/WORKFLOW_STEWARD_AUDIT_LAUNCH_PROMPT.md` |
| Context load rules | Direction Context Loading Index | `directions/workflow-governance/project_files/06_CONTEXT_LIBRARY_INDEX.md` |
| Direction Map | initial stub / needs M0 review | `directions/workflow-governance/project_files/08_DIRECTION_MAP.md` |
| ChatGPT Project Instructions | `Workflow Governance` | `directions/workflow-governance/project_setup/CHATGPT_PROJECT_INSTRUCTIONS.md` |

## Default Project Files to load

Load these Direction Project Files by default:

1. `00_DIRECTION_START_HERE.md`
2. `01_DIRECTION_STATE.md`
3. `02_CURRENT_PHASE.md`
4. `03_FOCUS_REGISTER.md`
5. `04_ACTIVE_GOAL.md`
6. `05_PORTFOLIO_QUEUE.md`
7. `06_CONTEXT_LIBRARY_INDEX.md`
8. `07_PHASE_MEMORY_INDEX.md`
9. `08_DIRECTION_MAP.md`

Also load shared runtime cache files defined in:

```text
workflow/runtime/WORKFLOW_RUNTIME_CACHE_MANIFEST.md
```

If `08_DIRECTION_MAP.md` is uninitialized or marked `needs_m0_review`, run `M0_DIRECTION_MAP` to migrate/build the map from current `00-07` progress and user-provided initiative context before relying on it for strategic Phase/Goal selection.

## Shared runtime file

Load shared runtime core separately from `workflow/runtime/WF_VNEXT_R_RUNTIME_CORE.md`.

Do not create or require a local runtime-core copy under this Direction `project_files/` folder.

## Normal next route

- Use Workflow Governance Maintenance Mode by default when the user asks to audit, repair, simplify, restructure, validate, or patch workflow behavior.
- Do not route to `G0_GOAL_SELECT` merely because Active Goal is `none`.
- Use `G0_GOAL_SELECT` only when the user explicitly wants to choose a durable Workflow Governance Goal and run the normal lifecycle.
- Use `Workflow Steward Audit` only when the user explicitly asks to run that audit launch prompt as a workflow stage/process.
- No repository patch until approval or direct user request to execute the approved maintenance changes.
- No product/project execution.
