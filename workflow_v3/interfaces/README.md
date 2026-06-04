# Workflow v3 Interface Layer

status: active_interface_layer

## Purpose

This directory is the canonical Workflow v3 interface layer for the current skeleton boundary.

Exact repository files at repo/path/ref are the source authority. Project Files/Sources, pasted excerpts, uploaded files, prior chat summaries, candidate docs, and generated packs are cache/context unless verified against exact repository state.

## Skeleton boundary

This interface layer refines repository documentation/setup only. It does not adopt any Direction, create accepted per-Direction state, update a Project Instructions UI, refresh Project Files/Sources, refresh request-only sources, import legacy state, or decommission the old Workflow OS.

Future adopted Direction state belongs under `directions_v3/<direction-id>/runtime/**` only after a separate accepted adoption package.

## Relationship to detailed docs

Files in this directory define the stable interface contracts that detailed `workflow_v3/**` source docs and templates must follow.

Detailed files may explain examples, storage shape, setup model, and operational details, but future workstreams must not redefine the interfaces here. If a detailed file conflicts with this interface layer, reconcile the detailed file through an explicit repository maintenance package.

## Interface file index

- `workflow_v3/interfaces/README.md` - interface layer index and boundary.
- `workflow_v3/interfaces/00_ENTITY_REGISTRY.md` - canonical entity registry.
- `workflow_v3/interfaces/01_DIRECTION_STRUCTURE_INTERFACE.md` - Direction structure and hierarchy.
- `workflow_v3/interfaces/02_DIRECTION_MAP_INTERFACE.md` - Direction Map interface.
- `workflow_v3/interfaces/03_DIRECTION_LIFECYCLE_SIGNAL_INTERFACE.md` - lifecycle facts and typed outputs.
- `workflow_v3/interfaces/04_ACTIVE_FRONT_SELECTION_INTERFACE.md` - Active Front selection protocol.
- `workflow_v3/interfaces/05_WORK_GRAPH_AND_NODE_INTERFACE.md` - Work Graph and node model.
- `workflow_v3/interfaces/06_CHAT_LIFECYCLE_AND_HANDOFF_INTERFACE.md` - chat lifecycle and handoff boundaries.
- `workflow_v3/interfaces/08_PACKET_AND_TRANSFER_INTERFACE.md` - packet and transfer surfaces.
- `workflow_v3/interfaces/09_STORAGE_STATE_INTERFACE.md` - storage and state mapping.
- `workflow_v3/interfaces/10_ADAPTER_CODEX_PROVIDER_INTERFACE.md` - adapter and provider boundaries.
- `workflow_v3/interfaces/11_PROJECT_SETUP_CONTEXT_INTERFACE.md` - Project setup/context boundaries.
- `workflow_v3/interfaces/12_QUALITY_RECOVERY_INTERFACE.md` - quality gates and recovery outcomes.
- `workflow_v3/interfaces/13_PARALLEL_WORKSTREAM_BRANCH_POLICY.md` - branch and workstream policy.
- `workflow_v3/interfaces/99_COVERAGE_MATRIX.md` - entity/interface coverage matrix.

END_OF_FILE: workflow_v3/interfaces/README.md
