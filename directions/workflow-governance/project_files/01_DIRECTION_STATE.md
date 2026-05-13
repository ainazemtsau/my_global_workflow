# 01 Direction State - Workflow Governance

```yaml
artifact_control:
  artifact_name: "01 Direction State - Workflow Governance"
  schema: direction_state.v1
  owner_layer: persistence
  status: canonical
  repo_path: "directions/workflow-governance/project_files/01_DIRECTION_STATE.md"
  default_load: yes
  freshness: fresh
  last_updated: "2026-05-12"
```

## State summary

- Purpose: maintain and improve Workflow vNext-R.
- Source of truth: GitHub repository markdown.
- Current Phase: `Workflow Steward Bootstrap`.
- Active Goal: `none`.
- Default next route: Workflow Governance Maintenance Mode for workflow repair, audit, cleanup, validation, and repository maintenance requests.

## Direction role

Workflow Governance owns workflow stewardship work:

- runtime contract audits;
- stage prompt consistency audits;
- lifecycle logic audits;
- UX and human-burden audits;
- context hygiene audits;
- real usage friction audits;
- external best-practice and research audits;
- finding triage;
- controlled workflow improvement proposals.

It does not own product/project execution.

## Default routing

Workflow Governance defaults to Maintenance Mode for workflow repair, audit, cleanup, validation, and repository maintenance requests.

If the user asks to improve, audit, debug, simplify, restructure, or patch workflow behavior, do not force `G0_GOAL_SELECT` or another lifecycle stage. Work directly in maintenance mode:

- identify the relevant workflow surface;
- inspect current repository files or request missing context;
- produce findings and patch plan;
- wait for approval before emitting repository_patch.v1 operations unless the user directly asks Codex to execute the changes;
- prepare Codex repository maintenance apply/read-back instructions;
- validate Codex return evidence.

If the user explicitly asks to select a durable governance objective or run normal Direction lifecycle, route to `G0_GOAL_SELECT`.

If the user explicitly asks to run Workflow Steward Audit as a staged workflow process, use `directions/workflow-governance/audits/WORKFLOW_STEWARD_AUDIT_LAUNCH_PROMPT.md`.

If the user asks for a repository patch, first produce reviewable work product and wait for approval unless direct formalization is explicitly approved by the current launch context.
