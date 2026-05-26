# Workflow Namespace

Status: active

`workflow/` is the active Workflow OS namespace for shared kernel, policy, transport, setup, pack, invariant, and evaluation sources.

The old `proof_workflow` namespace is gone. The old vNext-R workflow layout is legacy-only evidence preserved on the legacy branch/tag and is not active authority.

Direction accepted state remains under `directions/<direction-id>/proof/`.

## Layout

- `core/`: semantic kernel and runtime protocol entry points.
- `policies/`: Verify/Commit, transport, operator catalog, projection, migration, setup, storage, context authority, input normalization, run closure, and child handoff policies.
- `transport/`: canonical transport card schemas.
- `execution/`: request-only execution harness protocols.
- `project_setup/`: universal Direction Project setup templates, installer, and validation checklist.
- `project_packs/`: ChatGPT Project Files runtime-cache packs.
- `invariants/`: core and execution invariant lists.
- `evals/`: workflow validation and migration evaluation checklists.

END_OF_FILE: workflow/README.md
