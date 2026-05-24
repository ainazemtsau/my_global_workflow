---
artifact_control:
  namespace: proof_workflow
  artifact_type: runtime_protocols
  status: gate_1_initial
  owner: proof_carrying_workflow_os
---

# Runtime Protocols

## Type Boundaries

Semantic primitives are Ledger, Obligation, Operator, Receipt, and Invariant.

Runtime protocols govern how primitives move.

Adapters serialize protocol inputs and outputs.

Projections render accepted state for human use.

Storage preserves files, records, and tool state.

## Core Invocation Formula

```text
Operator(Obligation) -> Receipt
```

One ChatGPT chat = one Operator invocation over one Obligation.

If a chat receives a compound Obligation that cannot be completed atomically, it must return `split_required` or produce child Obligations through Decompose.

## Obligation Admission

Purpose: decide whether a proposed work item may become an open Obligation.

Inputs:

- proposed obligation statement
- source Receipt or human request
- acceptance conditions
- proof policy
- constraints

Output: open Obligation, rejected proposal, or Context Request Card.

## Run Admission

Purpose: decide whether an Operator invocation may begin.

Checks:

- target Obligation is open
- Operator is eligible
- required context is present
- Commit Scope is known
- human and tool gates are satisfied or explicitly deferred
- forbidden actions are clear

Output: approved Launch Card or blocking card.

## Obligation Selection

Purpose: choose the next eligible open Obligation under the current Commit Scope, Horizon orientation, constraints, and proof policy.

Output: selected Obligation or no eligible Obligation.

## Operator Selection

Purpose: choose the Operator whose purpose, evidence policy, and gate requirements fit the selected Obligation.

Output: selected Operator and selection rationale.

## Decompose

Purpose: split a compound Obligation into child Obligations that can each be handled by one Operator invocation.

Recursion:

```text
compound Obligation -> child Obligations -> child Receipts -> Synthesize -> parent Receipt
```

## Invoke

Purpose: execute one approved Operator invocation over one Obligation.

Inputs are serialized by an Operator Launch Card or equivalent adapter.

Output is a Receipt Card or a blocking transport card.

## Verify

Purpose: test whether a Receipt satisfies its proof policy and preserves invariants.

Output: pass, fail, or needs input.

## Commit

Purpose: apply a verified Ledger delta to the target Commit Scope.

Commit accepts, rejects, or defers a Receipt's delta proposal.

## Commit Scope Policy

Purpose: define which part of the Ledger an approved commit may mutate.

Commit Scope is runtime authority policy over the Ledger. It is not a sixth semantic primitive.

## Synthesize

Purpose: combine accepted child Receipts into a parent Receipt without inventing unsupported claims.

Synthesis must cite child Receipt IDs.

## Project

Purpose: render accepted Ledger state into documents, dashboards, maps, or views.

Projection output must cite source Receipt IDs or mark claims unsupported or unresolved.

## Learn

Purpose: create learning Obligations or operator notes from failures, uncertainty, validation results, or repeated patterns.

Learning notes are not accepted state until represented by verified Receipts and committed.

## Transport

Purpose: serialize context and handoff between chats, humans, tools, and storage.

Transport artifacts are not authority unless they contain or point to valid Receipts.

## Proof Policy

Purpose: define required claim roles, evidence kinds, confidence labels, and verification checks for a Receipt.

Proof policy is typed by claim and risk, not a linear hierarchy.

## Human Gate Policy

Purpose: identify decisions that belong to the human and must not be written by the workflow.

Human gates block commit or invocation until the required decision is supplied.

## Tool / Execution Gate Policy

Purpose: define when external tools, Codex workspace activity, repository mutation, product execution, release, or irreversible action may be invoked.

Codex and product execution are future gated Operator concepts in this namespace. This Gate 1 install does not implement execution workflow.

END_OF_FILE: proof_workflow/02_RUNTIME_PROTOCOLS.md
