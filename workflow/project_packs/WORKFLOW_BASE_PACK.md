---
artifact_control:
  namespace: workflow_project_packs
  artifact_type: project_pack
  pack_name: WORKFLOW_BASE_PACK
  pack_type: runtime_cache_upload_convenience
  intended_load_mode: default_all_directions
  status: u1_initial
  owner: workflow_os
  generated_from_ref: main@14bc73b11c609787e5919989a6e3fb6de2450c9e
  do_not_use_as_authority: true
  refresh_rule: "Regenerate and refresh this pack if any source_manifest file changes."
source_manifest:
  - workflow/core/00_WORKFLOW_OS.md
  - workflow/core/01_SEMANTIC_KERNEL.md
  - workflow/core/02_RUNTIME_PROTOCOLS.md
  - workflow/policies/03_VERIFY_AND_COMMIT_POLICY.md
  - workflow/policies/05_OPERATOR_CATALOG_POLICY.md
  - workflow/policies/06_PROJECTION_POLICY.md
  - workflow/policies/07_MIGRATION_PROTOCOL.md
  - workflow/invariants/CORE_INVARIANTS.md
  - workflow/evals/MIGRATION_VALIDATION_CHECKLIST.md
---

# Workflow Base Pack

## Cache Boundary

This pack is a ChatGPT Project Files runtime cache / upload convenience artifact.

It is not semantic authority.

Canonical source files listed in `source_manifest` remain authority.

If this pack conflicts with a verified canonical source file, the canonical source wins.

If any `source_manifest` file changes, regenerate and refresh this pack before using it as Project Files cache.

## Semantic Kernel

Tier 0 semantic primitives are only:

- Ledger
- Obligation
- Operator
- Receipt
- Invariant

Execution, stage, layer, roadmap, Direction, pack, project, file, schema, dashboard, and document are not semantic primitives.

## Runtime Law

The workflow movement is:

```text
Obligation -> Operator -> Receipt -> Verify -> Commit
```

One material Operator invocation works over one Obligation and returns a Receipt or blocking card.

A Receipt is receipt-backed candidate state. It does not mutate the Ledger until Verify and Commit accept it under the relevant Commit Scope.

Commit Scope is runtime policy for Ledger mutation. It is not a semantic primitive.

## Truth And Projection

Documents, dashboards, maps, roadmaps, and projections do not create truth.

A Strategic Path Map is valid only as a projection from accepted Receipts and open Obligations.

A roadmap item without an Obligation is invalid.

Business-facing summaries must not claim more than accepted Receipts prove.

## Legacy And Migration

Old workflow files and old Direction files may become accepted state only through Legacy Import Receipt, Verify, and Commit.

Legacy data may be inspected as evidence when an admitted Obligation asks for that. Inspection alone does not import or accept the data.

## Execution Boundary

No Codex/product execution may begin without an execution-ready Obligation and required precondition Receipts.

Execution remains governed by the same kernel path:

```text
Obligation -> Operator -> Receipt -> Verify -> Commit
```

No validation means no done claim for execution work.

END_OF_FILE: workflow/project_packs/WORKFLOW_BASE_PACK.md
