# Workflow Governance Audits

This folder supports Workflow Steward Audit work.

## Audit modes

### weekly_light

Fast recurring check for drift, open findings, recent real-use friction, and small governance issues.

### monthly_deep

Deeper audit across runtime contracts, stage prompts, lifecycle logic, transport packets, real Direction behavior, and research-backed improvement candidates.

### triggered

Audit launched because a specific failure, regression, confusing workflow output, or repeated user burden was observed.

### focused_scope

Narrow audit for one stage, packet, Direction behavior, lifecycle transition, or approval/control issue.

## Rules

- Use source-backed facts vs inference.
- No repository patch until approval.
- Stage prompts are request-only by exact stage ID.
- No bulk-loading all stage prompts.
- No product/project execution.
