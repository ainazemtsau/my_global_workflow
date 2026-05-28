---
artifact_control:
  namespace: workflow
  artifact_type: storage_layout_policy
  status: u2_pack_model
  owner: workflow_os
---

# Storage Layout Policy

## Tier 3 Boundary

Storage is physical persistence and tooling.

Storage does not create truth without Commit.

GitHub files, Markdown documents, YAML sidecars, ChatGPT Project Files, API databases, Codex workspaces, external tools, MCP, Project setup files, and Project pack files are storage or tooling surfaces, not semantic primitives.

## Shared Workflow Namespace

The `workflow/` namespace stores shared workflow specifications:

- semantic kernel
- runtime protocols
- execution harness specifications
- verify and commit policy
- transport protocol
- operator catalog policy
- projection policy
- migration protocol
- ChatGPT setup principles
- storage layout policy
- transport card definitions
- invariant definitions
- validation checklists

Canonical shared workflow source files remain under `workflow/**`.

Shared execution specs live under:

```text
workflow/execution/
```

## Project Setup And Packs

Universal setup docs live under:

```text
workflow/project_setup/
```

`workflow/project_setup/` stores installer, template, and validation docs for restoring Direction Workflow Projects.

Project pack files live under:

```text
workflow/project_packs/
```

`workflow/project_packs/` stores runtime cache / upload convenience files for ChatGPT Project Files.

Packs are not canonical semantic authority.

Canonical source files listed by each pack remain the authority. If a pack conflicts with a verified canonical source file, the canonical source wins.

Direction Project manifests use pack-based default upload: three shared packs plus six Direction payload files from the Direction's active payload directory.

## Direction Proof Storage

Per-Direction proof state uses:

```text
directions/<direction-id>/<active-direction-state>/
```

Active payload and setup paths:

```text
directions/<direction-id>/<active-direction-state>/LEDGER.md
directions/<direction-id>/<active-direction-state>/OBLIGATIONS.md
directions/<direction-id>/<active-direction-state>/RECEIPTS_INDEX.md
directions/<direction-id>/<active-direction-state>/COMMIT_SCOPES.md
directions/<direction-id>/<active-direction-state>/DASHBOARD.md
directions/<direction-id>/<active-direction-state>/MIGRATION_RECEIPT.md
directions/<direction-id>/<active-direction-state>/receipts/
directions/<direction-id>/<active-direction-state>/projections/
directions/<direction-id>/<active-project-setup>/CHATGPT_PROJECT_INSTRUCTIONS.md
directions/<direction-id>/<active-project-setup>/PROJECT_FILES_MANIFEST.md
```

For the inspected active Directions, `direction.meta.yml` and the Project Files manifests resolve `<active-direction-state>` to `workflow` and `<active-project-setup>` to `workflow/project_setup`.

Creating or updating a Direction payload path requires an explicit admitted setup or migration action.

## File Roles

`LEDGER.md` stores accepted Ledger state.

`OBLIGATIONS.md` stores open, blocked, satisfied, and invalidated Obligations.

`RECEIPTS_INDEX.md` stores accepted Receipt references.

`COMMIT_SCOPES.md` stores runtime authority policy over Ledger mutation.

`DASHBOARD.md` stores a projection, not authority.

`MIGRATION_RECEIPT.md` stores the initial migration Receipt for a Direction when created.

Direction `<active-project-setup>/` stores restorable Project Instructions and Project Files manifests.

`receipts/` stores Receipt records.

`projections/` stores generated projection documents.

## Project Files

ChatGPT Project Files may act as runtime cache.

Project Files are not source of truth for accepted state unless they reflect committed Ledger state.

If Project Files conflict with committed Ledger state, the Ledger wins.

If Project pack files conflict with their canonical source files, the canonical source files win.

## Product/Project Technical Memory

Project-specific technical memory lives in the target product/project repository, not in the workflow governance repository.

Required project-local execution memory:

```text
AGENTS.md
.execution/project_profile.md
.execution/validation_profile.md
.execution/module_map.md
.execution/technical_ledger.md
.execution/known_risks.md
.execution/receipts/
.execution/plans/
```

Workflow/business documents receive clean projections only. They must not become the source of project-specific technical truth.

END_OF_FILE: workflow/policies/09_STORAGE_LAYOUT_POLICY.md
