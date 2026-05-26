---
artifact_control:
  namespace: workflow
  artifact_type: execution_invariants
  status: gate_2_initial
  owner: workflow_os
---

# Execution Invariants

## Boundary

Execution invariants do not add semantic primitives.

They constrain execution movement under the existing primitives: Ledger, Obligation, Operator, Receipt, and Invariant.

## Hard Execution Invariants

- No execution-ready receipt -> no CodexRun.
- No target binding -> no CodexRun.
- No validation plan -> no CodexRun.
- No validation receipt -> no done.
- No commit receipt -> no accepted execution state.
- No direct implementation for mission-scale complex technical work.
- No required subagent/reviewer omission -> no valid execution receipt.
- No product/project technical memory update when required -> execution receipt incomplete.
- No business-facing done claim beyond accepted technical receipt evidence.
- No product/project repository mutation from Workflow Governance maintenance patch.
- No execution claim bypasses `Obligation -> Operator -> Receipt -> Verify -> Commit`.
- No CodexRun may treat Codex as the execution system.

## Recovery Routes

When an invariant blocks execution, return one of:

- Context Request Card
- Human Action Card
- Project Setup Receipt with `setup_gap`
- Validation Receipt with `validation_gap`
- residual execution Obligation
- repair Obligation
- Complex Technical Mission routing Receipt

Hard invariant failure blocks commit.

END_OF_FILE: invariants/EXECUTION_INVARIANTS.md
