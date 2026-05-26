---
artifact_control:
  namespace: workflow
  artifact_type: execution_harness
  status: gate_2_initial
  owner: workflow_os
---

# Execution Harness

## Boundary

Execution Harness is the Gate 2 runtime extension for making product, project, repository, tool, and external work receipt-backed.

Execution is not a semantic primitive.

Execution is not a stage system.

Execution is not Codex.

Codex is one Operator family that may act inside execution when the gate admits it.

The semantic path remains:

```text
Obligation -> Operator -> Receipt -> Verify -> Commit
```

## Execution Flow

Execution work should move through:

```text
Business/Strategic Receipt
-> Execution Obligation
-> Target Binding Receipt
-> Technical Context / Discovery Receipt
-> Execution Readiness Receipt
-> Operator Invocation
-> Implementation Receipt
-> Validation Receipt
-> Repair if needed
-> Commit Receipt
-> Projection Summary
```

The flow may stop at any point with a blocking Receipt, Context Request Card, Human Action Card, or residual Obligation.

## Evidence Boundaries

Implementation evidence records what was changed, generated, configured, or performed.

Validation evidence records what was checked, how it was checked, what passed, what failed, and what could not be run.

Commit acceptance records that a verified Receipt delta was accepted into the Ledger under the target Commit Scope.

Implementation evidence alone is not validation.

Validation evidence alone is not commit acceptance.

Commit acceptance must not claim more than the accepted implementation and validation Receipts prove.

## Governance Patch Boundary

This Gate 2 patch defines shared workflow specifications under `workflow/**`.

It does not authorize product/project execution inside the Workflow Governance maintenance repository.

No product/project repository mutation may be performed by a Workflow Governance maintenance patch unless a separate admitted execution Obligation targets that product/project repository.

## Projection Boundary

Business-facing documents may receive clean projection summaries after accepted technical Receipts.

Projection summaries must cite accepted Receipt IDs or mark claims unsupported, unresolved, or hypothetical.

END_OF_FILE: workflow/execution/00_EXECUTION_HARNESS.md
