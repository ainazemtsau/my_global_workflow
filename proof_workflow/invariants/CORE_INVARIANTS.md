---
artifact_control:
  namespace: proof_workflow
  artifact_type: core_invariants
  status: gate_1_initial
  owner: proof_carrying_workflow_os
---

# Core Invariants

## Hard Invariants

- No obligation -> no work.
- No receipt -> no progress.
- No verification -> no commit.
- No commit -> no accepted state.
- No accepted receipts -> no confident document claim.
- No projection claim without accepted Receipt.
- No roadmap item without Obligation.
- No Codex/product execution without execution-ready Obligation and required precondition Receipts.
- No old workflow semantic authority in new proof workflow.
- No old Direction Map as Strategic Path Map truth.
- No old Active Goal as active Obligation.
- No child run mutates Ledger directly.
- No process macro marks work complete.
- No launch without Run Admission.
- No high-impact action without Human Gate where required.
- No single chat for non-atomic compound Obligation unless it returns split_required.
- No loaded context becomes accepted state without Receipt + Verify + Commit.
- No candidate context may be promoted to root objective, constraint, Horizon, Active Frontier, roadmap, or execution precondition without explicit acceptance.
- No Human Decision option may silently embed an unaccepted candidate constraint.
- No Project File or projection overrides committed Ledger state.

## Enforcement

Invariant checks run during Verify and Commit.

Hard invariant failure blocks commit.

Invariant uncertainty must produce a residual Obligation, Context Request Card, or Human Decision Card.

## Legacy Term Handling

Legacy terms such as `Direction Map`, `Active Goal`, and similar old workflow labels may appear only as demoted evidence, compatibility notes, or explicit non-authority examples.

They must not define accepted state in the new proof workflow.

END_OF_FILE: proof_workflow/invariants/CORE_INVARIANTS.md
