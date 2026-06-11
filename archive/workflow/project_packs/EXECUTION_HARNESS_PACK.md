---
artifact_control:
  namespace: workflow_project_packs
  artifact_type: project_pack
  pack_name: EXECUTION_HARNESS_PACK
  pack_type: runtime_cache_upload_convenience
  intended_load_mode: request_only
  status: u1_initial
  owner: workflow_os
  generated_from_ref: main@14bc73b11c609787e5919989a6e3fb6de2450c9e
  do_not_use_as_authority: true
  refresh_rule: "Regenerate and refresh this pack if any source_manifest file changes."
source_manifest:
  - workflow/execution/00_EXECUTION_HARNESS.md
  - workflow/execution/01_PROJECT_SETUP_PROTOCOL.md
  - workflow/execution/02_EXECUTION_OBLIGATIONS.md
  - workflow/execution/03_CODEX_OPERATOR_PROTOCOL.md
  - workflow/execution/04_VALIDATION_PROTOCOL.md
  - workflow/execution/05_COMPLEX_TECHNICAL_MISSION_PROTOCOL.md
  - workflow/execution/06_HUMAN_GUIDED_EXECUTION_PROTOCOL.md
  - workflow/execution/07_TECHNICAL_MEMORY_POLICY.md
  - workflow/execution/08_EXECUTION_EVALS.md
  - workflow/invariants/EXECUTION_INVARIANTS.md
  - workflow/transport/CODEX_EXECUTION_LAUNCH_CARD.md
  - workflow/transport/EXECUTION_RECEIPT_CARD.md
  - workflow/transport/PROJECT_SETUP_RECEIPT_CARD.md
  - workflow/transport/VALIDATION_RECEIPT_CARD.md
  - workflow/transport/HUMAN_ACTION_CARD.md
---

# Execution Harness Pack

## Cache Boundary

This pack is a ChatGPT Project Files runtime cache / upload convenience artifact.

It is not semantic authority.

Canonical source files listed in `source_manifest` remain authority.

If this pack conflicts with a verified canonical source file, the canonical source wins.

If any `source_manifest` file changes, regenerate and refresh this pack before using it as Project Files cache.

This is a request-only capability pack. It should not be default-loaded into every chat unless the Direction Project intentionally works on execution readiness.

## Execution Boundary

Execution is not a semantic primitive.

Codex is not the execution system.

CodexRun is one Operator family inside execution.

Execution remains kernel-derived:

```text
Obligation -> Operator -> Receipt -> Verify -> Commit
```

## Hard Gates

No execution-ready receipt means no CodexRun.

No target binding means no CodexRun.

No validation plan means no CodexRun.

No validation receipt means no done.

No commit receipt means no accepted execution state.

Direct implementation is denied for mission-scale complex technical work. Complex technical missions must route through frame, discovery, architecture options, validation harness, spike, decision, slice plan, slice execution, integration validation, and technical memory update.

## Validation

Validation is an Obligation, not an afterthought.

The validation ladder is:

- L0 self-check
- L1 static / compile / lint / type / schema
- L2 unit
- L3 integration
- L4 runtime
- L5 user-visible / screenshot / manual / UI/gameplay
- L6 regression
- L7 independent review / subagent

Each required level must pass or block commit. Each omitted level must be marked `not_required` with a reason.

## Human-Guided Execution

Use a Human Action Card for external, manual, sensitive, unavailable automation, account, purchase, credential, permission, local device, website, app, UI, or validation-gap steps.

The workflow may guide. The human performs sensitive or manual action. Human confirmation is required before the action supports a Receipt.

## Product Repository Technical Memory

Product/project technical memory belongs in the target product repository, not this workflow governance repository.

Target product repositories should maintain:

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

Do not create those product repo files in the workflow governance repository.

## Exact Schema Fallback

When launch, execution, setup, validation, or human action card schemas are material, load the canonical source card from `source_manifest`.

END_OF_FILE: workflow/project_packs/EXECUTION_HARNESS_PACK.md
