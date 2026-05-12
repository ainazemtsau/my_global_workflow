# 02 Current Phase - Workflow Governance

```yaml
artifact_control:
  artifact_name: "02 Current Phase - Workflow Governance"
  schema: current_phase.v1
  owner_layer: persistence
  status: canonical
  repo_path: "directions/workflow-governance/project_files/02_CURRENT_PHASE.md"
  default_load: yes
  freshness: fresh
  last_updated: "2026-05-12"
```

## Current Phase

```yaml
phase:
  id: workflow_steward_bootstrap
  name: Workflow Steward Bootstrap
  state: active
  source_of_truth: github_markdown
  minimum_outcome: "Workflow Governance has a usable audit, findings, research, eval, decision, patch, and execution-log structure."
  active_goal: none
  default_next_route: "G0_GOAL_SELECT or Workflow Steward Audit Launch depending on user intent"
```

## Closure criteria

The phase can close when:

- baseline governance files exist;
- audit modes are defined;
- finding schema is defined;
- evaluation suite exists;
- research source-quality rules exist;
- audit launch prompt can run full or focused audits;
- no repository patch is produced without approval.

## Non-goals

- Do not alter runtime behavior from this bootstrap file.
- Do not run product/project execution.
- Do not modify sibling Directions.
