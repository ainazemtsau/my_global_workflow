---
artifact_control:
  namespace: proof_workflow
  artifact_type: proof_and_commit_policy
  status: gate_1_initial
  owner: proof_carrying_workflow_os
---

# Proof And Commit Policy

## Policy Shape

Proof policy is typed, not a linear proof hierarchy.

Different claims require different evidence. A preference, a test result, a human decision, and a forecast are not proven by the same standard.

## Claim Roles

Allowed claim roles:

- fact
- inference
- assumption
- preference
- decision
- validation
- forecast
- constraint
- artifact_quality

Every produced claim in a Receipt must declare a role.

## Evidence Kinds

Allowed evidence kinds:

- source_backed
- tested_result
- human_decision
- expert_audit
- reasoned_inference
- direct_observation
- tool_return
- codex_validation

Evidence must identify enough source detail for later verification.

## Verify Protocol

Verify checks a Receipt before commit:

1. The Receipt references one open Obligation.
2. The Operator is valid for that Obligation.
3. Each claim has a claim role.
4. Evidence kinds satisfy the applicable proof policy.
5. Assumptions are explicit.
6. Uncertainty is labeled.
7. Residual Obligations are listed when work is partial.
8. Invariants are checked.
9. Required human and tool gates are resolved.

Verification result is `pass`, `fail`, or `needs_input`.

## Commit Protocol

Commit applies a verified Ledger delta to a Commit Scope.

Required checks:

- Verify result is pass.
- Commit Scope permits the proposed mutation.
- Hard invariants pass.
- Human Gate requirements are satisfied.
- Tool / Execution Gate requirements are satisfied.
- Projection updates are identified but not treated as accepted state.

Receipt does not mutate Ledger automatically.

Projection update happens after committed Ledger delta.

## Commit Scope Policy

Commit Scope is runtime authority policy over the Ledger. It limits where a commit may write accepted state, close Obligations, open residual Obligations, or update accepted Receipt indexes.

Commit Scope is not a sixth semantic primitive.

Commit Scope records:

```yaml
commit_scope:
  commit_scope_id: string
  target_ledger_ref: string
  allowed_mutations: [string]
  forbidden_mutations: [string]
  required_gates: [string]
  projection_update_policy: string
```

## Human Approval Gates

Human approval is required before commit or invocation for:

- high-impact strategic decision
- repository mutation
- product/project execution
- release/launch/publishing
- irreversible or high-risk action

The workflow must request the decision. It must not write the user's decision for them.

## Commit Outcomes

Commit verdicts:

- committed
- rejected
- blocked_needs_context
- blocked_needs_human_gate
- blocked_invariant_failure
- blocked_scope_violation

Only `committed` creates accepted state.

END_OF_FILE: proof_workflow/03_PROOF_AND_COMMIT_POLICY.md
