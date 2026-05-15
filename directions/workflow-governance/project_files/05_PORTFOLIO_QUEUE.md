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

## Maintenance backlog

These items may be handled directly in Workflow Governance Maintenance Mode without creating an Active Goal:

| Item | Status | Route |
| --- | --- | --- |
| Continue focused workflow cleanup / repair cycles | active_backlog | Maintenance Mode |
| Run targeted read-only control audits | active_backlog | Maintenance Mode |
| Harden runtime validation checks | active_backlog | Maintenance Mode |
| Triage accepted/open workflow findings | active_backlog | Maintenance Mode or Workflow Steward Audit by explicit request |
| Evaluate real Direction friction | candidate | Workflow Steward Audit or Maintenance Mode |
| Research external workflow best practices | candidate | D1 or Workflow Steward Audit with `research_scan` by explicit request |

## Candidate governance goals

These are durable normal-lifecycle candidates. They are not active Goals until explicitly selected and shaped.

| Candidate | Status | Route |
| --- | --- | --- |
| Establish weekly_light audit loop | candidate | G0/G1 before formalization |
| Establish monthly_deep audit loop | candidate | G0/G1 before formalization |
| Build stage regression baseline | candidate | G0/G1 before formalization |

## Queue rules

- Maintenance backlog items may be handled directly in Workflow Governance Maintenance Mode.
- Candidate governance goals are not active Goals until selected and shaped.
- Findings do not become patches automatically.
- No repository patch until approval.
- Do not run normal lifecycle stages merely because Active Goal is `none`.
- Use G0/G1 only when the user explicitly wants to select and shape a durable governance goal.
