---
artifact_control:
  namespace: proof_workflow
  artifact_type: storage_layout_policy
  status: gate_1_initial
  owner: proof_carrying_workflow_os
---

# Storage Layout Policy

## Tier 3 Boundary

Storage is physical persistence and tooling.

Storage does not create truth without Commit.

GitHub files, Markdown documents, YAML sidecars, ChatGPT Project Files, API databases, Codex workspaces, and external tools / MCP are storage or tooling surfaces, not semantic primitives.

## Shared Kernel Namespace

`proof_workflow/` stores shared proof workflow specifications:

- semantic kernel
- runtime protocols
- proof and commit policy
- transport protocol
- operator catalog policy
- projection policy
- migration protocol
- future ChatGPT setup principles
- storage layout policy
- transport card definitions
- invariant definitions
- validation checklists

## Future Direction Proof Storage

Future per-Direction proof state should use:

```text
directions/<direction-id>/proof/
```

Approximate future structure:

```text
directions/<direction-id>/proof/
  LEDGER.md
  OBLIGATIONS.md
  RECEIPTS_INDEX.md
  COMMIT_SCOPES.md
  DASHBOARD.md
  MIGRATION_RECEIPT.md
  receipts/
  projections/
```

This run does not create any `directions/<direction-id>/proof/` path.

## File Roles

`LEDGER.md` stores accepted Ledger state.

`OBLIGATIONS.md` stores open, blocked, satisfied, and invalidated Obligations.

`RECEIPTS_INDEX.md` stores accepted Receipt references.

`COMMIT_SCOPES.md` stores runtime authority policy over Ledger mutation.

`DASHBOARD.md` stores a projection, not authority.

`MIGRATION_RECEIPT.md` stores the initial migration Receipt for a Direction when created.

`receipts/` stores Receipt records.

`projections/` stores generated projection documents.

## Project Files

ChatGPT Project Files may act as runtime cache.

Project Files are not source of truth for accepted state unless they reflect committed Ledger state.

If Project Files conflict with committed Ledger state, the Ledger wins.

END_OF_FILE: proof_workflow/09_STORAGE_LAYOUT_POLICY.md
