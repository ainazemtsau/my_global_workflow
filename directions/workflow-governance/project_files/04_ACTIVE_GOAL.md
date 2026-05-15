# 04 Active Goal - Workflow Governance

```yaml
artifact_control:
  artifact_name: "04 Active Goal - Workflow Governance"
  schema: active_goal.v1
  owner_layer: persistence
  status: canonical
  repo_path: "directions/workflow-governance/project_files/04_ACTIVE_GOAL.md"
  default_load: yes
  freshness: fresh
  last_updated: "2026-05-12"
```

## Active Goal

```yaml
active_goal:
  state: none
  goal_id: null
  goal_name: null
  maintenance_workbench_active: true
  normal_lifecycle_required: false
  default_next_route: "Workflow Governance Maintenance Mode for workflow audit/repair/cleanup; G0_GOAL_SELECT only when explicitly requested"
```

## Notes

No Workflow Governance Goal is currently active.

Active Goal `none` is not a blocker for workflow maintenance work.

Workflow Governance currently operates as a maintenance workbench. Use Workflow Governance Maintenance Mode for workflow audit, repair, cleanup, validation, source-of-truth review, repository patch preparation, and Codex repository maintenance.

Use `G0_GOAL_SELECT` only when the user explicitly asks to choose a durable governance goal or run the normal Goal lifecycle.

Use `audits/WORKFLOW_STEWARD_AUDIT_LAUNCH_PROMPT.md` only when the user explicitly asks to run that staged audit process.
