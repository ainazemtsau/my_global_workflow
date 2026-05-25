# Workflow Source of Truth

Status: active

Canonical AI workflow source: GitHub repository `ainazemtsau/my_global_workflow`.

Active workflow authority: `proof_workflow/**`.

## Active Semantic Kernel

The active Proof-Carrying Workflow OS semantic kernel is limited to:

- Ledger
- Obligation
- Operator
- Receipt
- Invariant

## Active Runtime Protocols

Active runtime protocol and policy sources:

- `proof_workflow/02_RUNTIME_PROTOCOLS.md`
- `proof_workflow/03_PROOF_AND_COMMIT_POLICY.md`
- `proof_workflow/04_TRANSPORT_PROTOCOL.md`
- `proof_workflow/10_CONTEXT_AUTHORITY_POLICY.md`
- `proof_workflow/11_HUMAN_INPUT_NORMALIZATION_POLICY.md`
- `proof_workflow/12_HUMAN_FACING_RUN_CLOSURE_POLICY.md`
- `proof_workflow/13_RECURSIVE_CHILD_HANDOFF_POLICY.md`

## Active Project Setup

Active shared setup sources:

- `proof_workflow/08_CHATGPT_PROJECT_SETUP.md`
- `proof_workflow/09_STORAGE_LAYOUT_POLICY.md`
- `proof_workflow/project_setup/UNIVERSAL_DIRECTION_PROJECT_INSTALLER.md`
- `proof_workflow/project_setup/UNIVERSAL_DIRECTION_PROJECT_INSTRUCTIONS.md`
- `proof_workflow/project_setup/UNIVERSAL_PROJECT_FILES_MANIFEST_TEMPLATE.md`
- `proof_workflow/project_setup/PROJECT_SETUP_VALIDATION_CHECKLIST.md`

Project pack runtime-cache files live under:

- `proof_workflow/project_packs/`

Project packs are upload convenience/runtime cache only. Canonical source files listed by each pack remain authority.

Per-Direction proof project setup files live under:

- `directions/<direction-id>/proof/project_setup/`

Per-Direction manifests use the active pack model: three shared packs plus six Direction payload files.

Project Instructions are behavior/setup instructions. Direction payload files are live state.

## Active Direction State Model

Accepted Direction proof state is stored under:

- `directions/<direction-id>/proof/LEDGER.md`
- `directions/<direction-id>/proof/OBLIGATIONS.md`
- `directions/<direction-id>/proof/RECEIPTS_INDEX.md`
- `directions/<direction-id>/proof/COMMIT_SCOPES.md`
- `directions/<direction-id>/proof/DASHBOARD.md`
- `directions/<direction-id>/proof/MIGRATION_RECEIPT.md`
- `directions/<direction-id>/proof/receipts/`
- `directions/<direction-id>/proof/projections/`

Only verified Receipts committed to the Ledger create accepted state.

Documents and projections do not create truth.

ChatGPT Project Files are runtime cache, not source of truth.

## Legacy vNext-R Preservation

The pre-proof vNext-R main snapshot is preserved at:

- legacy branch: `legacy/vnext-r-main-before-proof-os-2026-05-25`
- legacy tag: `vnext-r-main-before-proof-os-2026-05-25`

The top-level `workflow/` directory has been removed from active `main`.

Old vNext-R workflow files are available only from the legacy branch/tag if historical evidence is needed.

Old `directions/*/project_files/**` files are legacy evidence only unless explicitly imported through Legacy Import Receipt + Verify + Commit.

Old Direction Map, Active Goal, Current Phase, and Portfolio Queue files are not accepted Proof Ledger state.

The old vNext-R runtime, project_files/00-08 model, Direction Map, Phase, Goal, Portfolio Queue, and `repository_patch.v1` are demoted from active default authority.

## Long File And Read Completeness Rule

A truncated, omitted, or tail-unverified repository read is not sufficient authority for material workflow work.

If material work depends on a file whose full content cannot be verified, return a Context Request naming the exact path and blocker.

In the proof workflow, read-completeness and context-authority behavior is governed by `proof_workflow/**` policies plus future setup docs. Old vNext-R guard files are legacy evidence available from the legacy branch/tag only.

## Admin Documentation

Repository setup docs under `docs/` may explain setup and transition procedure, but they do not override `proof_workflow/**`.

Migration/admin docs remain historical context unless a proof workflow Obligation explicitly admits them as legacy evidence.

END_OF_FILE: WORKFLOW_SOURCE_OF_TRUTH.md
