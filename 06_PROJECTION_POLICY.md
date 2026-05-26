---
artifact_control:
  namespace: workflow
  artifact_type: projection_policy
  status: gate_1_initial
  owner: workflow_os
---

# Projection Policy

## Projection Boundary

A projection renders accepted Ledger state for human orientation.

Documents cannot create truth.

Projection documents may not introduce claims unsupported by accepted Receipts.

Every projection claim must list source Receipt IDs or be marked unsupported, unresolved, or hypothetical.

## Projection Document

A Projection Document is any Markdown file, dashboard, map, view, or exported artifact that summarizes or arranges accepted state.

Required fields or sections:

- projection_id
- source_ledger_ref
- source_receipt_ids
- generated_at
- unsupported_or_unresolved_claims
- refresh_policy

## Dashboard

A Dashboard is a projection over current Ledger state, open Obligations, blocked Obligations, recent Receipts, Commit Scope, and required gates.

Dashboard rows must cite accepted Receipt IDs or open Obligation IDs.

## Roadmap Projection

A roadmap is a projection over Obligations, constraints, and accepted strategic Receipts.

Roadmap item without Obligation is invalid.

A roadmap item may be tentative only if it is explicitly marked as unsupported or proposed.

## Strategic Path Map Projection

Strategic Path Map is a governed projection from accepted strategic Receipts.

It is not primary truth.

It may show themes, choices, commitments, risks, and sequencing only when backed by accepted Receipts.

## Horizon Projection

Horizon is committed orientation state backed by accepted Receipts.

Horizon Projection renders that orientation for planning and selection, including active constraints, strategic commitments, and known uncertainty.

Arbitrary planning text is not Horizon.

## Active Frontier View

Active Frontier is a computed eligibility view over open Obligations under current Horizon, constraints, verification policy, and gate status.

It is not a standalone truth object.

Active Frontier may identify:

- eligible next Obligations
- blocked Obligations
- required context
- required human gates
- required tool gates

## Projection Refresh Rule

Projection update happens after committed Ledger delta.

If a projection conflicts with accepted Ledger state, the Ledger wins and the projection must be refreshed.

END_OF_FILE: 06_PROJECTION_POLICY.md
