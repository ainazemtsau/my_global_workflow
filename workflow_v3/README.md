# Workflow v3 Production Namespace Skeleton

status: active_skeleton_namespace_corrected

## Purpose

`workflow_v3/**` is the Workflow v3 production namespace skeleton for runtime rules, setup templates, and future pack sources.

This slice activates only the documentation/setup skeleton under `workflow_v3/**`. It does not activate a live runtime, does not adopt any Direction, does not migrate or import old Direction state, and does not update actual ChatGPT Projects.

The current Workflow OS remains the legacy and rollback system until a later explicit activation and adoption package says otherwise.

The repository-side completion framework adds clean-start adoption templates, canonical procedure files, validation evals, setup protocols, and a final completion matrix. Procedure implementation status is authoritative only in each procedure file header. This slice remains documentation/setup only.

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
- generated pack uploads;
- old Workflow OS deletion, rename, move, replacement, or decommission.

## Source boundary

The candidate design baseline lives under `workflow/candidates/workflow_runtime_rebuild/**`. This production skeleton summarizes boundaries from that candidate without making any Direction adopted and without importing legacy Direction proof state.

Repository files under `workflow_v3/**` are future Workflow v3 setup/rule sources only within the limits stated here. They are not proof that any Direction runtime state exists.

## Interface package

`workflow_v3/interfaces/**` is the active Workflow v3 interface layer for this skeleton. It locks the Direction structure, Direction Map, Goal Evidence Graph, Active Unresolved Cut, lifecycle outputs, Active Front selection, Work Graph/node model, parent integration/impact outputs, chat handoffs, packets, storage, adapter boundaries, Project setup context, quality/recovery gates, and coverage matrix.

Future detailed docs and workstreams must reconcile with the interface layer instead of redefining those contracts independently.

## Procedure layer

`workflow_v3/procedures/**` defines the repository-side procedure layer for steering entities and runtime operations. Direction Spine, Direction Map with associated Goal Evidence Graph, Active Front, Work Graph, Work Contract, Work Contract execution, Parent Integration, Impact Propagation, Current Next Move, Acceptance Decision, Memory Artifact promotion, and Storage Update use canonical procedure files.

Unauthored procedure bodies are represented by self-contained stubs that stop when selected. Accepted state still requires explicit Acceptance Decision or accepted update path.

## Setup-only root and Direction Definition

Ordinary Direction Project root/bootstrap is setup-only. It may create future technical placeholders and binding, but must not require or accept root outcome, Direction Spine, Direction Map, Active Front, Work Graph, or product strategy.

The registered setup/root bootstrap entrypoint is `direction_project_root_bootstrap`, with run surface type `setup_only_root_bootstrap` and procedure source `workflow_v3/procedures/DIRECTION_PROJECT_ROOT_BOOTSTRAP_PROCEDURE.md`.

Direction Definition is the separate semantic process after setup-only root. It selects one next procedure step at a time, starting with Direction Spine formation; later Map and Active Front formation require explicit Next Move / Transfer Packet or separately admitted lifecycle boundaries until detailed bodies are authored.

## File index

- `workflow_v3/README.md` - namespace overview and index.
- `workflow_v3/interfaces/README.md` - Workflow v3 interface package index.
- `workflow_v3/interfaces/00_ENTITY_REGISTRY.md` - canonical Workflow v3 entity registry.
- `workflow_v3/interfaces/01_DIRECTION_STRUCTURE_INTERFACE.md` - Direction structure interface.
- `workflow_v3/interfaces/02_DIRECTION_MAP_INTERFACE.md` - Direction Map interface.
- `workflow_v3/interfaces/03_DIRECTION_LIFECYCLE_OUTPUT_INTERFACE.md` - Direction lifecycle output interface.
- `workflow_v3/interfaces/04_ACTIVE_FRONT_SELECTION_INTERFACE.md` - Active Front selection interface.
- `workflow_v3/interfaces/05_WORK_GRAPH_AND_NODE_INTERFACE.md` - Work Graph and node interface.
- `workflow_v3/interfaces/06_CHAT_LIFECYCLE_AND_HANDOFF_INTERFACE.md` - chat lifecycle and handoff interface.
- `workflow_v3/interfaces/08_PACKET_AND_TRANSFER_INTERFACE.md` - packet and transfer interface.
- `workflow_v3/interfaces/09_STORAGE_STATE_INTERFACE.md` - storage and state interface.
- `workflow_v3/interfaces/10_ADAPTER_CODEX_PROVIDER_INTERFACE.md` - adapter, Codex, and provider interface.
- `workflow_v3/interfaces/11_PROJECT_SETUP_CONTEXT_INTERFACE.md` - Project setup/context interface.
- `workflow_v3/interfaces/12_QUALITY_RECOVERY_INTERFACE.md` - quality and recovery interface.
- `workflow_v3/interfaces/13_PARALLEL_WORKSTREAM_BRANCH_POLICY.md` - branch/workstream policy interface.
- `workflow_v3/interfaces/14_GOAL_EVIDENCE_GRAPH_INTERFACE.md` - Goal Evidence Graph and Active Unresolved Cut interface.
- `workflow_v3/interfaces/15_PARENT_INTEGRATION_AND_IMPACT_INTERFACE.md` - parent integration and impact interface.
- `workflow_v3/interfaces/99_COVERAGE_MATRIX.md` - entity/interface coverage matrix.
- `workflow_v3/ACTIVATION_STATUS.md` - current activation status matrix and allowed next packages.
- `workflow_v3/RUNTIME_MODEL.md` - compact Workflow v3 runtime model and boundaries.
- `workflow_v3/control_plane/README.md` - Workflow v3 action-admission control plane index.
- `workflow_v3/control_plane/ACTION_ADMISSION_PROTOCOL.md` - before-action admission sequence, stop conditions, and Admission Packet rules.
- `workflow_v3/control_plane/PROCEDURE_REGISTRY.md` - registered entrypoints, procedure refs, run surface types, procedure classes, and embedded use policies.
- `workflow_v3/control_plane/RUN_SURFACE_CONTRACTS.md` - allowed/forbidden operations by run surface.
- `workflow_v3/control_plane/CHAT_LIFECYCLE_PROTOCOL.md` - material chat phases from intake through closure/transfer.
- `workflow_v3/control_plane/UTILITY_ADAPTER_PROTOCOL.md` - utility/adapter taxonomy, embedded use, RUN_EXTERNAL_HANDOFF/RETURN, same-owner resume, and storage/verification boundaries.
- `workflow_v3/control_plane/SOURCE_INTEGRITY_PROTOCOL.md` - exact source read, EOF, and source lock rules.
- `workflow_v3/control_plane/EXCEPTION_PROTOCOL.md` - blocked exception packet and exception types.
- `workflow_v3/control_plane/STORAGE_UPDATE_PROTOCOL.md` - storage update adapter package and write boundary.
- `workflow_v3/STORAGE_LAYOUT.md` - production rules/setup namespace and future Direction runtime state root.
- `workflow_v3/PROJECT_SETUP_MODEL.md` - future ChatGPT Project setup model and refresh categories.
- `workflow_v3/LEGACY_EVIDENCE_POLICY.md` - legacy/rollback and old Direction evidence policy.
- `workflow_v3/QUALITY_AND_RECOVERY.md` - quality gates and recovery outcomes.
- `workflow_v3/completion/README.md` - repository-side completion package index.
- `workflow_v3/completion/WORKFLOW_V3_COMPLETION_MATRIX.md` - final surface and entity coverage matrix.
- `workflow_v3/completion/WORKFLOW_V3_REPOSITORY_COMPLETION_AUDIT.md` - completion validation audit.
- `workflow_v3/completion/POST_COMPLETION_REMAINING_NON_GOALS.md` - intentionally remaining non-goals.
- `workflow_v3/adoption/README.md` - clean-start Direction adoption package model.
- `workflow_v3/adoption/CLEAN_START_DIRECTION_ADOPTION_PACKAGE_TEMPLATE.md` - future adoption package template.
- `workflow_v3/adoption/SETUP_ONLY_DIRECTION_RUNTIME_ROOT_PACKAGE_TEMPLATE.md` - future setup-only runtime root package template.
- `workflow_v3/adoption/DIRECTION_RUNTIME_ROOT_MANIFEST_TEMPLATE.md` - future runtime root manifest template.
- `workflow_v3/adoption/DIRECTION_BOOTSTRAP_DECISION_TEMPLATE.md` - explicit bootstrap decision template.
- `workflow_v3/adoption/DIRECTION_RUNTIME_CREATION_CHECKLIST.md` - future runtime creation checklist.
- `workflow_v3/adoption/LEGACY_EVIDENCE_REVIEW_TEMPLATE.md` - legacy evidence review template.
- `workflow_v3/adoption/ADOPTION_RESULT_PACKET_TEMPLATE.md` - adoption result packet template.
- `workflow_v3/procedures/DIRECTION_SPINE_FORMATION_PROCEDURE.md` - Direction Spine formation procedure source. Status is authoritative in the file header.
- `workflow_v3/procedures/DIRECTION_MAP_FORMATION_PROCEDURE.md` - Direction Map formation procedure source. Status is authoritative in the file header.
- `workflow_v3/procedures/ACTIVE_FRONT_FORMATION_PROCEDURE.md` - Active Front formation procedure source. Status is authoritative in the file header.
- `workflow_v3/procedures/WORK_GRAPH_FORMATION_PROCEDURE.md` - Work Graph formation procedure source. Status is authoritative in the file header.
- `workflow_v3/procedures/WORK_CONTRACT_FORMATION_PROCEDURE.md` - Work Contract formation procedure source. Status is authoritative in the file header.
- `workflow_v3/procedures/WORK_CONTRACT_EXECUTION_PROCEDURE.md` - Work Contract execution procedure source. Status is authoritative in the file header.
- `workflow_v3/procedures/PARENT_INTEGRATION_CHECK_PROCEDURE.md` - Parent Integration Check procedure source. Status is authoritative in the file header.
- `workflow_v3/procedures/IMPACT_PROPAGATION_PROCEDURE.md` - Impact Propagation procedure source. Status is authoritative in the file header.
- `workflow_v3/procedures/CURRENT_NEXT_MOVE_FORMATION_PROCEDURE.md` - Current Next Move formation procedure source. Status is authoritative in the file header.
- `workflow_v3/procedures/ACCEPTANCE_DECISION_FORMATION_PROCEDURE.md` - Acceptance Decision formation procedure source. Status is authoritative in the file header.
- `workflow_v3/procedures/MEMORY_ARTIFACT_PROMOTION_PROCEDURE.md` - Memory Artifact promotion procedure source. Status is authoritative in the file header.
- `workflow_v3/evals/README.md` - validation eval index.
- `workflow_v3/evals/WORKFLOW_V3_COMPLETION_VALIDATION_CHECKLIST.md` - completion validation checklist.
- `workflow_v3/evals/DIRECTION_RUNTIME_BOOTSTRAP_EVAL.md` - Direction runtime bootstrap eval.
- `workflow_v3/evals/DIRECTION_PROJECT_SETUP_EVAL.md` - ordinary Direction Project setup behavior eval.
- `workflow_v3/evals/DIRECTION_SETUP_ONLY_BOOTSTRAP_EVAL.md` - setup-only bootstrap eval.
- `workflow_v3/evals/DIRECTION_DEFINITION_EVAL.md` - Direction Definition eval.
- `workflow_v3/evals/DIRECTION_SPINE_FORMATION_EVAL.md` - Direction Spine formation eval.
- `workflow_v3/evals/DIRECTION_MAP_FORMATION_EVAL.md` - Direction Map formation eval.
- `workflow_v3/evals/ACTIVE_FRONT_FORMATION_EVAL.md` - Active Front formation eval.
- `workflow_v3/evals/WORK_GRAPH_FORMATION_EVAL.md` - Work Graph formation eval.
- `workflow_v3/evals/WORK_CONTRACT_FORMATION_EVAL.md` - Work Contract formation eval.
- `workflow_v3/evals/CURRENT_NEXT_MOVE_FORMATION_EVAL.md` - Current Next Move formation eval.
- `workflow_v3/evals/ACCEPTANCE_DECISION_FORMATION_EVAL.md` - Acceptance Decision formation eval.
- `workflow_v3/evals/MEMORY_ARTIFACT_PROMOTION_EVAL.md` - Memory Artifact promotion eval.
- `workflow_v3/evals/DIRECTION_MAP_FRONT_GRAPH_EVAL.md` - Direction Map, Active Front, and Work Graph eval.
- `workflow_v3/evals/GOAL_EVIDENCE_GRAPH_EVAL.md` - Goal Evidence Graph eval.
- `workflow_v3/evals/ACTIVE_UNRESOLVED_CUT_EVAL.md` - Active Unresolved Cut eval.
- `workflow_v3/evals/PARENT_INTEGRATION_RESULT_EVAL.md` - Parent Integration Result eval.
- `workflow_v3/evals/IMPACT_PROPAGATION_EVAL.md` - Impact Propagation eval.
- `workflow_v3/evals/DERIVED_GATE_CHECK_EVAL.md` - Derived Gate Check eval.
- `workflow_v3/evals/MEMORY_INDEX_EVAL.md` - Memory Index eval.
- `workflow_v3/evals/NO_HOLLOW_LAYER_EVAL.md` - no hollow parent layer eval.
- `workflow_v3/evals/NO_SINGLE_TRACK_COLLAPSE_EVAL.md` - no single-track collapse eval.
- `workflow_v3/evals/FINISH_PACKET_EVAL.md` - FINISH_PACKET validation eval.
- `workflow_v3/evals/NEXT_MOVE_PACKET_EVAL.md` - Next Move Packet validation eval.
- `workflow_v3/evals/CHAT_LIFECYCLE_HANDOFF_EVAL.md` - chat lifecycle/handoff eval.
- `workflow_v3/evals/CODEX_HANDOFF_RESULT_EVAL.md` - Codex handoff result eval.
- `workflow_v3/evals/PROJECT_SETUP_ROLLOUT_EVAL.md` - Project setup rollout eval.
- `workflow_v3/evals/LEGACY_EVIDENCE_BOUNDARY_EVAL.md` - legacy evidence boundary eval.
- `workflow_v3/evals/NO_HIDDEN_STATE_OR_ROUTE_EVAL.md` - no hidden state or route eval.
- `workflow_v3/evals/ACTION_ADMISSION_EVAL.md` - action admission eval.
- `workflow_v3/evals/CHAT_LIFECYCLE_EVAL.md` - control-plane chat lifecycle eval.
- `workflow_v3/evals/SOURCE_INTEGRITY_EVAL.md` - exact source authority eval.
- `workflow_v3/evals/PROCEDURE_DEFINITION_EVAL.md` - procedure definition quality eval.
- `workflow_v3/evals/PROCEDURE_EXECUTION_EVAL.md` - procedure execution lifecycle/gate eval.
- `workflow_v3/evals/STORAGE_UPDATE_PACKAGE_EVAL.md` - storage update adapter package eval.
- `workflow_v3/project_setup/CHATGPT_PROJECT_CREATION_GUIDE.md` - future Project creation guide and naming rules.
- `workflow_v3/project_setup/README.md` - Workflow v3 Project setup index.
- `workflow_v3/project_setup/UNIVERSAL_DIRECTION_PROJECT_INSTALLER.md` - installer for a future ordinary Direction ChatGPT Project.
- `workflow_v3/project_setup/UNIVERSAL_DIRECTION_PROJECT_INSTRUCTIONS.md` - compact future UI payload source for ordinary Direction Projects.
- `workflow_v3/project_setup/UNIVERSAL_DIRECTION_PROJECT_FILES_MANIFEST_TEMPLATE.md` - ordinary Direction Project Files/Sources manifest template.
- `workflow_v3/project_setup/DIRECTION_ROOT_BOOTSTRAP_LAUNCH_PACKET_TEMPLATE.md` - first-chat root bootstrap launch packet template.
- `workflow_v3/project_setup/DIRECTION_SETUP_ONLY_ROOT_BOOTSTRAP_PROTOCOL.md` - setup-only root bootstrap protocol.
- `workflow_v3/project_setup/DIRECTION_DEFINITION_LAUNCH_PACKET_TEMPLATE.md` - Direction Definition launch packet template.
- `workflow_v3/project_setup/DIRECTION_PROJECT_BINDING_AND_CONTINUATION_PROTOCOL.md` - ordinary Direction Project binding and later-chat continuation protocol.
- `workflow_v3/project_setup/PER_DIRECTION_PROJECT_INSTRUCTIONS_SOURCE_TEMPLATE.md` - future per-Direction Project Instructions source template.
- `workflow_v3/project_setup/PER_DIRECTION_PROJECT_FILES_MANIFEST_TEMPLATE.md` - future per-Direction Project Files/Sources manifest template.
- `workflow_v3/project_setup/DIRECTION_PROJECT_SETUP_VALIDATION_CHECKLIST.md` - manual ordinary Direction Project setup validation checklist.
- `workflow_v3/project_setup/GOVERNANCE_MAINTENANCE_PROJECT_INSTRUCTIONS.md` - compact future UI payload source for the Governance Maintenance Console.
- `workflow_v3/project_setup/PROJECT_FILES_MANIFEST_TEMPLATE.md` - template for future Project Files/Sources manifests.
- `workflow_v3/project_setup/rollouts/GOVERNANCE_MAINTENANCE_PROJECT_ROLLOUT_PACKET.md` - manual rollout packet for Workflow v3 Governance Maintenance Console Project Instructions UI.
- `workflow_v3/project_setup/rollouts/GOVERNANCE_MAINTENANCE_PROJECT_ROLLOUT_RESULT.md` - recorded manual UI update evidence for Workflow v3 Governance Maintenance Console.
- `workflow_v3/project_setup/GENERIC_AI_PROVIDER_SETUP.md` - setup contract for ChatGPT, Codex, Claude Code/future assistants, research agents, GitHub access, human actions, and future providers.
- `workflow_v3/project_packs/README.md` - future pack source model.
- `workflow_v3/templates/README.md` - Workflow v3 template package index for operational records, runtime state, front/graph/node records, evidence/acceptance records, memory, and recovery.
- `workflow_v3/templates/CHECK_JOB_TEMPLATE.md` - Check Job template.
- `workflow_v3/templates/FINISH_PACKET_TEMPLATE.md` - FINISH_PACKET template.
- `workflow_v3/templates/NEXT_MOVE_PACKET_TEMPLATE.md` - Next Move Packet template.
- `workflow_v3/templates/TRANSFER_PACKET_TEMPLATE.md` - Transfer Packet template.
- `workflow_v3/templates/NEXT_CHAT_PROMPT_TEMPLATE.md` - Next chat prompt template.
- `workflow_v3/templates/RUN_ADMISSION_PACKET_TEMPLATE.md` - run admission packet template.
- `workflow_v3/templates/WORK_PLAN_TEMPLATE.md` - admitted work plan template.
- `workflow_v3/templates/SOURCE_LOCK_TEMPLATE.md` - source lock template.
- `workflow_v3/templates/TYPED_GATE_OUTPUT_TEMPLATE.md` - typed gate output template.
- `workflow_v3/templates/STORAGE_UPDATE_PACKAGE_TEMPLATE.md` - storage update package template.
- `workflow_v3/templates/EXCEPTION_PACKET_TEMPLATE.md` - exception packet template.
- `workflow_v3/procedures/PROCEDURE_DEFINITION_CANON.md` - canonical Workflow v3 procedure definition framework.
- `workflow_v3/procedures/PROCEDURE_AUTHORING_GUIDE.md` - guide for writing Workflow v3 procedure files.
- `workflow_v3/procedures/PROCEDURE_TEMPLATE.md` - reusable template for new Workflow v3 procedures.
- `workflow_v3/procedures/PROCEDURE_AUTHORING_AND_INTEGRATION_PROCEDURE.md` - procedure authoring and integration procedure source. Status is authoritative in the file header.
- `workflow_v3/procedures/GENERIC_ANSWER_PROCEDURE.md` - generic answer procedure source. Status is authoritative in the file header.
- `workflow_v3/procedures/STATUS_REVIEW_PROCEDURE.md` - status review procedure source. Status is authoritative in the file header.
- `workflow_v3/procedures/CODEX_HANDOFF_PROCEDURE.md` - Codex handoff procedure source. Status is authoritative in the file header.
- `workflow_v3/procedures/CODEX_RESULT_VERIFICATION_PROCEDURE.md` - Codex result verification procedure source. Status is authoritative in the file header.
- `workflow_v3/procedures/RECOVERY_REVIEW_PROCEDURE.md` - recovery review procedure source. Status is authoritative in the file header.
- `workflow_v3/procedures/DIRECTION_PROJECT_ROOT_BOOTSTRAP_PROCEDURE.md` - setup-only root bootstrap procedure source. Status is authoritative in the file header.
- `workflow_v3/procedures/DIRECTION_DEFINITION_PROCEDURE.md` - Direction Definition procedure source. Status is authoritative in the file header.
- `workflow_v3/procedures/DIRECTION_SPINE_FORMATION_PROCEDURE.md` - Direction Spine formation procedure source. Status is authoritative in the file header.
- `workflow_v3/procedures/DIRECTION_MAP_FORMATION_PROCEDURE.md` - Direction Map formation procedure source. Status is authoritative in the file header.
- `workflow_v3/procedures/ACTIVE_FRONT_FORMATION_PROCEDURE.md` - Active Front formation procedure source. Status is authoritative in the file header.
- `workflow_v3/procedures/WORK_GRAPH_FORMATION_PROCEDURE.md` - Work Graph formation procedure source. Status is authoritative in the file header.
- `workflow_v3/procedures/WORK_CONTRACT_FORMATION_PROCEDURE.md` - Work Contract formation procedure source. Status is authoritative in the file header.
- `workflow_v3/procedures/WORK_CONTRACT_EXECUTION_PROCEDURE.md` - Work Contract execution procedure source. Status is authoritative in the file header.
- `workflow_v3/procedures/PARENT_INTEGRATION_CHECK_PROCEDURE.md` - Parent Integration Check procedure source. Status is authoritative in the file header.
- `workflow_v3/procedures/IMPACT_PROPAGATION_PROCEDURE.md` - Impact Propagation procedure source. Status is authoritative in the file header.
- `workflow_v3/procedures/CURRENT_NEXT_MOVE_FORMATION_PROCEDURE.md` - Current Next Move formation procedure source. Status is authoritative in the file header.
- `workflow_v3/procedures/ACCEPTANCE_DECISION_FORMATION_PROCEDURE.md` - Acceptance Decision formation procedure source. Status is authoritative in the file header.
- `workflow_v3/procedures/MEMORY_ARTIFACT_PROMOTION_PROCEDURE.md` - Memory Artifact promotion procedure source. Status is authoritative in the file header.
- `workflow_v3/procedures/STORAGE_UPDATE_PROCEDURE.md` - Storage Update procedure source. Status is authoritative in the file header.
- `workflow_v3/templates/DIRECTION_PROJECT_BINDING_TEMPLATE.md` - future runtime Project Binding config template.
- `workflow_v3/templates/DIRECTION_CONSOLE_TEMPLATE.md` - future read-only Direction Console template.
- `workflow_v3/templates/GOAL_EVIDENCE_GRAPH_TEMPLATE.md` - Goal Evidence Graph template.
- `workflow_v3/templates/GOAL_EVIDENCE_NODE_TEMPLATE.md` - Goal Evidence Node template.
- `workflow_v3/templates/ACTIVE_UNRESOLVED_CUT_TEMPLATE.md` - Active Unresolved Cut template.
- `workflow_v3/templates/PARENT_INTEGRATION_RESULT_TEMPLATE.md` - Parent Integration Result template.
- `workflow_v3/templates/GRAPH_DELTA_TEMPLATE.md` - Graph Delta template.
- `workflow_v3/templates/UPSTREAM_ESCALATION_PACKET_TEMPLATE.md` - Upstream Escalation Packet template.
- `workflow_v3/templates/DOWNSTREAM_DELTA_PACKET_TEMPLATE.md` - Downstream Delta Packet template.
- `workflow_v3/templates/DERIVED_GATE_CHECK_TEMPLATE.md` - Derived Gate Check template.
- `workflow_v3/templates/MEMORY_INDEX_TEMPLATE.md` - Memory Index template.
- `workflow_v3/evals/DIRECTION_PROJECT_CONTINUATION_EVAL.md` - later-chat binding/status/continuation eval.

END_OF_FILE: workflow_v3/README.md
