---
artifact_control:
  namespace: proof_workflow
  artifact_type: transport_protocol
  status: gate_1_initial
  owner: proof_carrying_workflow_os
---

# Transport Protocol

## Transport Boundary

Transport is serialization, not semantic authority.

Transport artifacts carry instructions, context, missing-context requests, decisions, receipts, and commit proposals. They do not create accepted state unless Verify and Commit produce a committed Ledger delta.

Transport may carry accepted state, candidate context, projections, or legacy evidence.

Transport must label authority status when material.

## Transport Flow

Chat A does not communicate by memory with Chat B.

Chat A emits transport artifact.

Chat B consumes transport artifact.

Durable state changes only through committed Ledger delta.

## Launch Card

Launch Card serializes Operator invocation over one Obligation.

It binds:

- target Obligation
- selected Operator
- Ledger snapshot reference
- Commit Scope reference
- accepted state references
- candidate context references
- projection context references
- legacy context references
- proof policy
- human and tool gates
- stop conditions
- return target

Launch Card should separate `accepted_state_refs` from `candidate_context_refs` and `legacy_context_refs`.

Launch Card is not a legacy stage launch and does not authorize work outside its target Obligation.

## Receipt Card

Receipt Card serializes a Receipt.

It records the outcome of one Operator invocation and includes produced claims, evidence, assumptions, residual Obligations, invariant checks, proof policy result, and commit recommendation.

Receipt Card is candidate state until committed.

## Context Request Card

Context Request Card serializes missing blocking context.

It must name the smallest sufficient context needed to continue and explain why continuing without it is unsafe.

## Human Decision Card

Human Decision Card serializes a human-owned decision request.

It may present options, consequences, and recommendation if any. It must not write the user's decision for them.

## Commit Packet

Commit Packet serializes proposed commit and verification state.

It connects Receipt IDs, target Commit Scope, proposed Ledger delta, verification results, invariant results, proof policy result, human gate result, and storage or projection updates required after commit.

## Proof Relationship

Transport artifacts are not proof unless they contain or point to a valid Receipt.

A transport artifact may support verification, but accepted state requires a committed Ledger delta.

END_OF_FILE: proof_workflow/04_TRANSPORT_PROTOCOL.md
