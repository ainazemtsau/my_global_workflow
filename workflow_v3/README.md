# Workflow v3 Production Namespace Skeleton

status: active_skeleton_namespace_corrected

## Purpose

`workflow_v3/**` is the Workflow v3 production namespace skeleton for runtime rules, setup templates, and future pack sources.

This slice activates only the documentation/setup skeleton under `workflow_v3/**`. It does not activate a live runtime, does not adopt any Direction, does not migrate or import old Direction state, and does not update actual ChatGPT Projects.

The current Workflow OS remains the legacy and rollback system until a later explicit activation and adoption package says otherwise.

## Scope of this slice

Created in this slice:

- production namespace boundary docs;
- future Project setup source docs;
- future project pack source model docs.

Not created in this slice:

- `directions_v3/<direction-id>/runtime/**` state;
- Project Instructions UI updates;
- Project Files/Sources refreshes;
- request-only source refreshes;
- old Workflow OS deletion, rename, move, replacement, or decommission.

## Source boundary

The candidate design baseline lives under `workflow/candidates/workflow_runtime_rebuild/**`. This production skeleton summarizes boundaries from that candidate without making any Direction adopted and without importing legacy Direction proof state.

Repository files under `workflow_v3/**` are future Workflow v3 setup/rule sources only within the limits stated here. They are not proof that any Direction runtime state exists.

## File index

- `workflow_v3/README.md` - namespace overview and index.
- `workflow_v3/ACTIVATION_STATUS.md` - current activation status matrix and allowed next packages.
- `workflow_v3/RUNTIME_MODEL.md` - compact Workflow v3 runtime model and boundaries.
- `workflow_v3/SIGNALS_HANDLERS_ACTION_INBOX.md` - operational event loop for Signals, Handlers, Action Inbox/Q, Check Jobs, Progression Router, Transition Packets, and Event Loop Closure.
- `workflow_v3/STORAGE_LAYOUT.md` - production rules/setup namespace and future Direction runtime state root.
- `workflow_v3/PROJECT_SETUP_MODEL.md` - future ChatGPT Project setup model and refresh categories.
- `workflow_v3/LEGACY_EVIDENCE_POLICY.md` - legacy/rollback and old Direction evidence policy.
- `workflow_v3/QUALITY_AND_RECOVERY.md` - quality gates and recovery outcomes.
- `workflow_v3/interfaces/README.md` - Workflow v3 interface layer index.
- `workflow_v3/interfaces/**` - cross-surface contracts for source/context, runtime state, work/run/acceptance, event loop/routing, packets/transfer, storage/adoption/legacy, adapters/Codex/providers, Project setup/packs, quality/recovery, and parallel workstream branch policy.
- `workflow_v3/project_setup/CHATGPT_PROJECT_CREATION_GUIDE.md` - future Project creation guide and naming rules.
- `workflow_v3/project_setup/UNIVERSAL_DIRECTION_PROJECT_INSTRUCTIONS.md` - compact future UI payload source for ordinary Direction Projects.
- `workflow_v3/project_setup/GOVERNANCE_MAINTENANCE_PROJECT_INSTRUCTIONS.md` - compact future UI payload source for the Governance Maintenance Console.
- `workflow_v3/project_setup/PROJECT_FILES_MANIFEST_TEMPLATE.md` - template for future Project Files/Sources manifests.
- `workflow_v3/project_setup/GENERIC_AI_PROVIDER_SETUP.md` - setup contract for ChatGPT, Codex, Claude Code/future assistants, research agents, GitHub access, human actions, and future providers.
- `workflow_v3/project_packs/README.md` - future pack source model.
- `workflow_v3/templates/SIGNAL_RECORD_TEMPLATE.md` - Signal record template.
- `workflow_v3/templates/HANDLER_RESULT_TEMPLATE.md` - Handler result template.
- `workflow_v3/templates/ACTION_INBOX_ITEM_TEMPLATE.md` - Action Inbox/Q item template.
- `workflow_v3/templates/CHECK_JOB_TEMPLATE.md` - Check Job template.
- `workflow_v3/templates/EVENT_LOOP_CLOSURE_TEMPLATE.md` - Event Loop Closure template.
- `workflow_v3/templates/PROGRESSION_ROUTER_RESULT_TEMPLATE.md` - Progression Router result template.
- `workflow_v3/templates/TRANSITION_PACKET_TEMPLATE.md` - Transition Packet template.
- `workflow_v3/templates/NEXT_CHAT_PROMPT_TEMPLATE.md` - Next chat prompt template.

END_OF_FILE: workflow_v3/README.md
