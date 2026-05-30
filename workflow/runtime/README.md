# Workflow v3 Production Namespace Skeleton

status: active_skeleton

## Purpose

`workflow/runtime/**` is the Workflow v3 production namespace skeleton for runtime rules, setup templates, and future pack sources.

This slice activates only the documentation/setup skeleton under `workflow/runtime/**`. It does not activate a live runtime, does not adopt any Direction, does not migrate or import old Direction state, and does not update actual ChatGPT Projects.

The current Workflow OS remains the legacy and rollback system until a later explicit activation and adoption package says otherwise.

## Scope of this slice

Created in this slice:

- production namespace boundary docs;
- future Project setup source docs;
- future project pack source model docs.

Not created in this slice:

- `directions/<direction-id>/runtime/**` state;
- Project Instructions UI updates;
- Project Files/Sources refreshes;
- request-only source refreshes;
- old Workflow OS deletion, rename, move, replacement, or decommission.

## Source boundary

The candidate design baseline lives under `workflow/candidates/workflow_runtime_rebuild/**`. This production skeleton summarizes boundaries from that candidate without making any Direction adopted and without importing legacy Direction proof state.

Repository files under `workflow/runtime/**` are future Workflow v3 setup/rule sources only within the limits stated here. They are not proof that any Direction runtime state exists.

## File index

- `workflow/runtime/README.md` - namespace overview and index.
- `workflow/runtime/ACTIVATION_STATUS.md` - current activation status matrix and allowed next packages.
- `workflow/runtime/RUNTIME_MODEL.md` - compact Workflow v3 runtime model and boundaries.
- `workflow/runtime/STORAGE_LAYOUT.md` - production rules/setup namespace and future Direction runtime state root.
- `workflow/runtime/PROJECT_SETUP_MODEL.md` - future ChatGPT Project setup model and refresh categories.
- `workflow/runtime/LEGACY_EVIDENCE_POLICY.md` - legacy/rollback and old Direction evidence policy.
- `workflow/runtime/QUALITY_AND_RECOVERY.md` - quality gates and recovery outcomes.
- `workflow/runtime/project_setup/CHATGPT_PROJECT_CREATION_GUIDE.md` - future Project creation guide and naming rules.
- `workflow/runtime/project_setup/UNIVERSAL_DIRECTION_PROJECT_INSTRUCTIONS.md` - compact future UI payload source for ordinary Direction Projects.
- `workflow/runtime/project_setup/GOVERNANCE_MAINTENANCE_PROJECT_INSTRUCTIONS.md` - compact future UI payload source for the Governance Maintenance Console.
- `workflow/runtime/project_setup/PROJECT_FILES_MANIFEST_TEMPLATE.md` - template for future Project Files/Sources manifests.
- `workflow/runtime/project_setup/GENERIC_AI_PROVIDER_SETUP.md` - setup contract for ChatGPT, Codex, Claude Code/future assistants, research agents, GitHub access, human actions, and future providers.
- `workflow/runtime/project_packs/README.md` - future pack source model.

END_OF_FILE: workflow/runtime/README.md
