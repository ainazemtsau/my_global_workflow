---
artifact_control:
  namespace: workflow
  artifact_type: technical_memory_policy
  status: gate_2_initial
  owner: workflow_os
---

# Technical Memory Policy

## Boundary

Technical memory lives in the target product/project repository.

The workflow governance repository stores shared workflow specifications.

Business and workflow documents receive clean projections only.

## Required Project-Local Layout

Target product/project repositories should maintain:

```text
AGENTS.md
.execution/project_profile.md
.execution/validation_profile.md
.execution/module_map.md
.execution/technical_ledger.md
.execution/known_risks.md
.execution/receipts/
.execution/plans/
```

## Update Rule

Technical receipts must update `.execution/module_map.md` and `.execution/technical_ledger.md` when implementation changes architecture, modules, validation expectations, integration boundaries, or known risks.

If required technical memory is not updated, the execution receipt is incomplete.

## Reuse Rule

Operators must inspect `.execution/module_map.md` before creating new modules or duplicating code.

Do not duplicate code when an existing module or extension point is already identified by project-local technical memory.

## Projection Rule

Business-facing projections may summarize accepted technical evidence, but must not expose raw implementation detail as accepted business fact beyond what accepted Receipts prove.

END_OF_FILE: execution/07_TECHNICAL_MEMORY_POLICY.md
