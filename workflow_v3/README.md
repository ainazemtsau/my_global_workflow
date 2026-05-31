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

## Interface package

`workflow_v3/interfaces/**` is the active Workflow v3 interface layer for this skeleton. It locks the Direction structure, Direction Map, lifecycle Signals/Handlers, Active Front selection, Work Graph/node model, chat handoffs, Event Loop routing, packets, storage, adapter boundaries, Project setup context, quality/recovery gates, and coverage matrix.

Future detailed docs and workstreams must reconcile with the interface layer instead of redefining those contracts independently.

## File index

- `workflow_v3/README.md` - namespace overview and index.
- `workflow_v3/interfaces/README.md` - Workflow v3 interface package index.
- `workflow_v3/interfaces/00_ENTITY_REGISTRY.md` - canonical Workflow v3 entity registry.
- `workflow_v3/interfaces/01_DIRECTION_STRUCTURE_INTERFACE.md` - Direction structure interface.
- `workflow_v3/interfaces/02_DIRECTION_MAP_INTERFACE.md` - Direction Map interface.
- `workflow_v3/interfaces/03_DIRECTION_LIFECYCLE_SIGNAL_INTERFACE.md` - Direction lifecycle Signal/Handler interface.
- `workflow_v3/interfaces/04_ACTIVE_FRONT_SELECTION_INTERFACE.md` - Active Front selection interface.
- `workflow_v3/interfaces/05_WORK_GRAPH_AND_NODE_INTERFACE.md` - Work Graph and node interface.
- `workflow_v3/interfaces/06_CHAT_LIFECYCLE_AND_HANDOFF_INTERFACE.md` - chat lifecycle and handoff interface.
- `workflow_v3/interfaces/07_EVENT_LOOP_AND_ROUTING_INTERFACE.md` - Event Loop and routing interface.
- `workflow_v3/interfaces/08_PACKET_AND_TRANSFER_INTERFACE.md` - packet and transfer interface.
- `workflow_v3/interfaces/09_STORAGE_STATE_INTERFACE.md` - storage and state interface.
- `workflow_v3/interfaces/10_ADAPTER_CODEX_PROVIDER_INTERFACE.md` - adapter, Codex, and provider interface.
- `workflow_v3/interfaces/11_PROJECT_SETUP_CONTEXT_INTERFACE.md` - Project setup/context interface.
- `workflow_v3/interfaces/12_QUALITY_RECOVERY_INTERFACE.md` - quality and recovery interface.
- `workflow_v3/interfaces/13_PARALLEL_WORKSTREAM_BRANCH_POLICY.md` - branch/workstream policy interface.
- `workflow_v3/interfaces/99_COVERAGE_MATRIX.md` - entity/interface coverage matrix.
- `workflow_v3/ACTIVATION_STATUS.md` - current activation status matrix and allowed next packages.
- `workflow_v3/RUNTIME_MODEL.md` - compact Workflow v3 runtime model and boundaries.
- `workflow_v3/SIGNALS_HANDLERS_ACTION_INBOX.md` - operational event loop for Signals, Handlers, Action Inbox/Q, Check Jobs, Progression Router, Transition Packets, and Event Loop Closure.
- `workflow_v3/STORAGE_LAYOUT.md` - production rules/setup namespace and future Direction runtime state root.
- `workflow_v3/PROJECT_SETUP_MODEL.md` - future ChatGPT Project setup model and refresh categories.
- `workflow_v3/LEGACY_EVIDENCE_POLICY.md` - legacy/rollback and old Direction evidence policy.
- `workflow_v3/QUALITY_AND_RECOVERY.md` - quality gates and recovery outcomes.
- `workflow_v3/project_setup/CHATGPT_PROJECT_CREATION_GUIDE.md` - future Project creation guide and naming rules.
- `workflow_v3/project_setup/UNIVERSAL_DIRECTION_PROJECT_INSTRUCTIONS.md` - compact future UI payload source for ordinary Direction Projects.
- `workflow_v3/project_setup/GOVERNANCE_MAINTENANCE_PROJECT_INSTRUCTIONS.md` - compact future UI payload source for the Governance Maintenance Console.
- `workflow_v3/project_setup/PROJECT_FILES_MANIFEST_TEMPLATE.md` - template for future Project Files/Sources manifests.
- `workflow_v3/project_setup/GENERIC_AI_PROVIDER_SETUP.md` - setup contract for ChatGPT, Codex, Claude Code/future assistants, research agents, GitHub access, human actions, and future providers.
- `workflow_v3/project_packs/README.md` - future pack source model.
- `workflow_v3/templates/README.md` - Workflow v3 template package index for operational records, runtime state, front/graph/node records, evidence/acceptance records, memory, and recovery.
- `workflow_v3/templates/SIGNAL_RECORD_TEMPLATE.md` - Signal record template.
- `workflow_v3/templates/HANDLER_RESULT_TEMPLATE.md` - Handler result template.
- `workflow_v3/templates/ACTION_INBOX_ITEM_TEMPLATE.md` - Action Inbox/Q item template.
- `workflow_v3/templates/CHECK_JOB_TEMPLATE.md` - Check Job template.
- `workflow_v3/templates/EVENT_LOOP_CLOSURE_TEMPLATE.md` - Event Loop Closure template.
- `workflow_v3/templates/PROGRESSION_ROUTER_RESULT_TEMPLATE.md` - Progression Router result template.
- `workflow_v3/templates/TRANSITION_PACKET_TEMPLATE.md` - Transition Packet template.
- `workflow_v3/templates/NEXT_CHAT_PROMPT_TEMPLATE.md` - Next chat prompt template.

END_OF_FILE: workflow_v3/README.md
