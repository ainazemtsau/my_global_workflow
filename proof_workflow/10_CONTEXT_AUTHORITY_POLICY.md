---
artifact_control:
  namespace: proof_workflow
  artifact_type: context_authority_policy
  status: gate_2_1_initial
  owner: proof_carrying_workflow_os
---

# Context Authority Policy

## Purpose

Context Authority Protocol defines how loaded context may be used during Operator invocation, decision framing, Receipt creation, verification, and commit.

Context Authority is a runtime protocol and policy. It is not a semantic primitive.

Context does not become truth by being loaded.

## Core Rules

Loaded context is not accepted state.

Project Files are not accepted domain truth unless they reflect committed Ledger state.

Candidate context may generate options or questions.

Candidate context may not be promoted to accepted state without Receipt + Verify + Commit.

Human Decision options must not silently embed unaccepted candidate constraints.

## Context Categories

| Category | Definition | Allowed Use |
| --- | --- | --- |
| accepted_ledger_state | State recorded in the current Ledger after Commit. | May support accepted claims, selection, projection, and commit decisions. |
| committed_receipt | Receipt accepted through Verify + Commit. | May support accepted claims and projection updates. |
| current_human_input | User input supplied in the current invocation or decision response. | May define decision, preference, or constraint claims when captured in a Receipt and committed. |
| candidate_context | Loaded or remembered information not yet accepted by Ledger. | May generate options, questions, assumptions, or candidate Obligations. |
| projection_context | Dashboard, map, view, or document projecting accepted state or unresolved state. | May orient the operator; must trace material claims to accepted receipts before use as truth. |
| legacy_evidence | Old workflow or old Direction material. | May support Legacy Import Receipts; may not define accepted state directly. |
| instruction_context | System, developer, project, or user instruction that governs behavior. | May constrain the run; does not create domain truth. |
| unknown | Context whose authority cannot be classified. | Must not support accepted claims; request context or mark uncertainty. |

## Required Behavior For Candidate Context

When candidate_context appears to imply root objective, constraints, Horizon, Active Frontier, execution readiness, or roadmap:

1. Label it as candidate_context.
2. Do not present it as accepted Ledger state.
3. Do not narrow all major Human Decision options around it unless the decision explicitly asks the user to accept that constraint.
4. Include a broader, neutral, or custom option unless the constraint is already accepted in Ledger.
5. Capture any user acceptance in a Receipt before Commit.
6. Block projection or execution readiness claims until accepted Receipts exist.

## Decision Framing Guard

Human Decision Cards must audit option framing.

If a material option embeds unaccepted candidate context, the card must label the embedded constraint and authority status.

If all major options embed the same candidate constraint, the card is invalid unless the decision statement explicitly asks the user to accept that constraint.

At least one broader, custom, or neutral option must be included unless the constraint is already accepted in Ledger.

## Context Authority Audit

Every material Operator invocation must classify context before using it as a claim basis.

Receipt Cards must report:

- accepted state used
- committed Receipts used
- candidate context used
- projection context used
- legacy evidence used
- whether assumptions were promoted to claims
- whether unaccepted constraints were embedded

Verification must fail or return `needs_input` when candidate_context is promoted to accepted claim without human decision or committed Receipt.

## Examples

`co-op game` in loaded files is candidate_context unless accepted in Ledger or supplied as current human decision.

Old Direction Map is legacy_evidence, not Strategic Path Map truth.

Dashboard is projection_context, not truth, unless traced to accepted Receipts.

END_OF_FILE: proof_workflow/10_CONTEXT_AUTHORITY_POLICY.md
