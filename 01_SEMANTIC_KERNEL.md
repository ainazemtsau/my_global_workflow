---
artifact_control:
  namespace: workflow
  artifact_type: semantic_kernel
  status: gate_1_initial
  owner: workflow_os
---

# Semantic Kernel

## Authority Boundary

The semantic kernel has exactly five primitives:

- Ledger
- Obligation
- Operator
- Receipt
- Invariant

No other concept is a semantic primitive in this workflow.

## Ledger

The Ledger is the accepted state of the workflow. It contains committed Receipts, accepted Ledger deltas, open Obligations, closed Obligations, active Commit Scopes, and invariant status.

Schema:

```yaml
ledger:
  ledger_id: string
  scope_id: string
  accepted_receipt_ids: [string]
  open_obligation_ids: [string]
  closed_obligation_ids: [string]
  active_commit_scope_ids: [string]
  invariant_set_ref: string
  last_committed_at: string
```

Rules:

- The Ledger changes only through Commit.
- A proposed delta is not accepted until Verify and Commit pass.
- Physical files may store the Ledger, but storage is not the Ledger authority without commit.

## Obligation

An Obligation is a unit of work, inquiry, decision, validation, or migration that the workflow is authorized to address.

Schema:

```yaml
obligation:
  obligation_id: string
  obligation_type: string
  statement: string
  status: proposed | open | blocked | satisfied | invalidated
  source_receipt_ids: [string]
  parent_obligation_id: string | null
  acceptance_conditions: [string]
  required_proof_policy: string
  constraints: [string]
  owner_gate: none | human | tool | execution
```

Rules:

- No obligation -> no work.
- Work that discovers missing scope must request or propose an Obligation before continuing.
- Compound Obligations must be decomposed when one Operator invocation cannot handle them atomically.

## Operator

An Operator is the semantic function invoked over one Obligation to produce a Receipt.

Schema:

```yaml
operator:
  operator_id: string
  family: string
  purpose: string
  valid_obligation_types: [string]
  input_requirements: [string]
  output_receipt_type: string
  proof_policy_ref: string
  human_gate_policy_ref: string | null
  tool_gate_policy_ref: string | null
```

Rules:

- An Operator does not mutate the Ledger directly.
- Operator invocation is serialized by a Launch Card or equivalent adapter.
- Operator output is a Receipt candidate until committed.

## Receipt

A Receipt records the outcome of one Operator invocation over one Obligation.

Schema:

```yaml
receipt:
  receipt_id: string
  obligation_id: string
  operator_id: string
  verdict: satisfied | partial | blocked | invalidated | split_required | failed
  produced_claims:
    - claim: string
      role: string
      evidence_refs: [string]
  evidence: [object]
  assumptions: [string]
  residual_obligation_ids: [string]
  ledger_delta_proposal: object | null
  proof_policy_result: pass | fail | needs_input
  invariant_check_summary: string
  commit_recommendation: commit | do_not_commit | needs_human_gate
```

Rules:

- No receipt -> no progress.
- A Receipt does not change the Ledger automatically.
- A Receipt becomes accepted state only after Verify and Commit.

## Invariant

An Invariant is a hard rule that all accepted workflow movement must preserve.

Schema:

```yaml
invariant:
  invariant_id: string
  statement: string
  severity: hard | gate | warning
  check_method: manual | static | protocol | tool
  failure_action: block_commit | require_human_gate | open_obligation
```

Rules:

- Invariants are checked during Verify and Commit.
- A hard invariant failure blocks commit.
- Invariants may force a Context Request, Human Decision Card, or residual Obligation.

## Kernel Laws

- No obligation -> no work.
- No receipt -> no progress.
- No verification -> no commit.
- No commit -> no accepted state.
- No accepted receipts -> no confident document claim.

## Explicit Non-Primitives

The following are not semantic primitives: `Layer`, `Sub-workflow`, `Entity`, `Stage`, `Goal`, `Phase`, `Roadmap`, `Document`, and `Process Template`.

If these terms appear in future material, they must be legacy terms, non-authoritative adapters, projections, macros, compatibility concepts, or examples of concepts demoted by this kernel.

END_OF_FILE: 01_SEMANTIC_KERNEL.md
