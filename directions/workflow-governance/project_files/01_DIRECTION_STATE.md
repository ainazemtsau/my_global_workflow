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
- Default next route: `G0_GOAL_SELECT` or `Workflow Steward Audit Launch`, depending on user intent.

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

If the user asks to improve or audit workflow behavior, use `directions/workflow-governance/audits/WORKFLOW_STEWARD_AUDIT_LAUNCH_PROMPT.md`.

If the user asks to select a durable governance objective, route to `G0_GOAL_SELECT`.

If the user asks for a repository patch, first produce reviewable work product and wait for approval unless direct formalization is explicitly approved by the current launch context.
