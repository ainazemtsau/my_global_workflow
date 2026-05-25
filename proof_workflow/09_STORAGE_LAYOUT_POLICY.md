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
- execution harness specifications
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

Shared execution specs live under:

```text
proof_workflow/execution/
```

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
  project_setup/
    CHATGPT_PROJECT_INSTRUCTIONS.md
    PROJECT_FILES_MANIFEST.md
  receipts/
  projections/
```

This storage policy describes where Direction proof state lives. Creating or updating a Direction proof path requires an explicit admitted setup or migration action.

## File Roles

`LEDGER.md` stores accepted Ledger state.

`OBLIGATIONS.md` stores open, blocked, satisfied, and invalidated Obligations.

`RECEIPTS_INDEX.md` stores accepted Receipt references.

`COMMIT_SCOPES.md` stores runtime authority policy over Ledger mutation.

`DASHBOARD.md` stores a projection, not authority.

`MIGRATION_RECEIPT.md` stores the initial migration Receipt for a Direction when created.

`project_setup/` stores restoration source for ChatGPT Project setup.

`project_setup/CHATGPT_PROJECT_INSTRUCTIONS.md` stores restorable Project Instructions.

`project_setup/PROJECT_FILES_MANIFEST.md` stores the Project Files upload manifest.

`receipts/` stores Receipt records.

`projections/` stores generated projection documents.

## Project Setup Files

Project setup files are storage/adapter surfaces, not semantic primitives.

They do not create accepted Ledger state.

They define how to restore the Project context safely.

## Project Files

ChatGPT Project Files may act as runtime cache.

Project Files are not source of truth for accepted state unless they reflect committed Ledger state.

If Project Files conflict with committed Ledger state, the Ledger wins.

## Product/Project Technical Memory

Project-specific technical memory lives in the target product/project repository, not in the workflow governance repository.

Required project-local execution memory:

```text
AGENTS.md
.execution/project_profile.md
.execution/validation_profile.md
.execution/module_map.md
.execution/technical_ledger.md
.execution/receipts/
```

Workflow/business documents receive clean projections only. They must not become the source of project-specific technical truth.

END_OF_FILE: proof_workflow/09_STORAGE_LAYOUT_POLICY.md
