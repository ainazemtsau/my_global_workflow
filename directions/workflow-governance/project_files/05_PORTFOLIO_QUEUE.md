# 05 Portfolio Queue - Workflow Governance

```yaml
artifact_control:
  artifact_name: "05 Portfolio Queue - Workflow Governance"
  schema: portfolio_queue.v1
  owner_layer: persistence
  status: canonical
  repo_path: "directions/workflow-governance/project_files/05_PORTFOLIO_QUEUE.md"
  default_load: yes
  freshness: fresh
  last_updated: "2026-05-12"
```

## Candidate governance goals

| Candidate | Status | Route |
| --- | --- | --- |
| Establish weekly_light audit loop | candidate | G0/G1 before formalization |
| Establish monthly_deep audit loop | candidate | G0/G1 before formalization |
| Build stage regression baseline | candidate | G0/G1 before formalization |
| Triage open workflow findings | candidate | Workflow Steward Audit or G0 |
| Evaluate real Direction friction | candidate | Workflow Steward Audit |
| Research external workflow best practices | candidate | D1 or Workflow Steward Audit with research_scan |

## Queue rules

- Candidates are not active Goals until selected and shaped.
- Findings do not become patches automatically.
- No repository patch until approval.
