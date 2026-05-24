---
artifact_control:
  namespace: proof_workflow
  artifact_type: operator_catalog_policy
  status: gate_1_initial
  owner: proof_carrying_workflow_os
---

# Operator Catalog Policy

## Catalog Boundary

Operator is a semantic primitive.

Operator Catalog is a runtime adapter and policy surface for storing, discovering, and selecting Operators. It is not a legacy stage registry and is not semantic authority by itself.

The catalog may list Operators, families, authoring notes, examples, and learning history. Accepted work still requires `Operator(Obligation) -> Receipt` and Commit.

## Operator Schema

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
  forbidden_outputs: [string]
  history_ref: string | null
```

## Operator Selection Policy

Operator Selection must check:

- the target Obligation is open
- the Operator accepts the Obligation type
- required context is present
- proof policy fits the claim risk
- human and tool gates are known
- forbidden actions are clear
- expected Receipt type is compatible with Commit Scope

If no Operator fits, create a residual Obligation or Context Request Card.

## Operator Authoring Policy

New Operators must define:

- purpose
- valid inputs
- required output Receipt type
- proof policy
- gate requirements
- stop conditions
- forbidden actions

An Operator must not mark its own result committed.

## Operator History And Learning Notes

Operator history may record repeated failures, useful prompts, evidence patterns, and validation lessons.

History notes are advisory until a learning Receipt is verified and committed.

## Initial Operator Families

Minimal initial families:

- ClarifyObjective
- DecomposeObligation
- ResearchEvidence
- ChallengeAssumption
- AskHumanDecision
- SynthesizeReceipts
- VerifyReceipt
- CommitLedgerDelta
- ProjectDashboard
- LegacyImport
- PrepareExecutionObligation
- CodexExecutionPlaceholder
- LearnFromFailure

`CodexExecutionPlaceholder` is gated and intentionally minimal. This namespace does not implement product/project execution workflow in Gate 1.

END_OF_FILE: proof_workflow/05_OPERATOR_CATALOG_POLICY.md
