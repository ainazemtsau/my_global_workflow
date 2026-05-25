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

Context Authority classifies loaded context before it is used as a claim basis.

Human Input Normalization converts clear natural-language human choices into structured Receipt fields.

Human-Facing Run Closure packages terminal outcome and handoff for the user.

Adapters serialize protocol inputs and outputs.

Projections render accepted state for human use.

Storage preserves files, records, and tool state.

## Core Invocation Formula

```text
Operator(Obligation) -> Receipt
```

One ChatGPT chat = one Operator invocation over one Obligation.

If a chat receives a compound Obligation that cannot be completed atomically, it must return `split_required` or produce child Obligations through Decompose.

## Context Authority

Purpose: classify loaded context by authority before it is used in an Operator invocation, Human Decision Card, Receipt, projection, or commit.

Every material Operator invocation must classify context before using it as claim basis.

Candidate context cannot be used as accepted state.

Project Files, projections, legacy files, and loaded domain material provide context only unless traced to committed Ledger state or current human input.

Output: context authority classification, required caveats, and blockers when authority is unknown or insufficient.

## Human Input Normalization

Purpose: normalize clear terse, informal, spoken, messy, or unstructured human input into structured Receipt fields.

It runs before or during Human Gate and Receipt creation when user input is unstructured.

It converts clear natural-language human choices into structured Receipt fields.

It must preserve Context Authority.

It must not require users to answer in YAML or schema format when intent is clear.

It may apply explicit procedural defaults that preserve openness, delegate to child Obligations, or classify unresolved details as candidate/unknown.

It must not accept substantive claims that were not explicit in the selected option or current human input.

Output: normalized decision, selected option if any, defaults applied, fields not accepted, residual Obligations, and remaining ambiguity.

## Human-Facing Run Closure

Purpose: end every material Operator invocation with a clear human-facing terminal outcome and any needed handoff.

It runs at the end of every material Operator invocation.

It does not create new semantic work.

It packages terminal outcome and handoff for the user.

If a commit-worthy Receipt exists, it must provide a Codex Commit Handoff Card or an explicit deferral reason.

If another ChatGPT operator run is needed, it must provide a human-readable copy-paste prompt, not only an Obligation ID.

Output: terminal outcome, human-readable next action, optional Codex Commit Handoff Card, optional next-chat prompt, and technical appendix.

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
