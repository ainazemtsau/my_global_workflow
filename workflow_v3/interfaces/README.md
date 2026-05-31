# Workflow v3 Interface Layer

status: active_interface_layer

## Purpose

This directory indexes the Workflow v3 interface layer.

The interface layer defines cross-surface contracts for Workflow v3 development so future workstreams use the same boundaries for source/context, runtime state, work/run/acceptance, event loop/routing, packets/transfer, storage/adoption/legacy, adapters/providers, Project setup/packs, quality/recovery, and parallel workstream branch policy.

## Source authority

Exact repository files at a named repo/path/ref are source authority.

Project Files/Sources, uploaded files, pasted excerpts, prior chats, generated packs, and candidate docs are cache/context unless verified against exact repository state.

Detailed model files under `workflow_v3/**` remain canonical for their owned surfaces. Interface files define contracts between surfaces and must not silently redefine the detailed model files.

## Current skeleton boundary

`workflow_v3/**` is a Workflow v3 documentation/setup skeleton and rule source namespace.

This interface package does not activate a live runtime, adopt a Direction, import old Direction state, update actual ChatGPT Project Instructions UI, refresh Project Files/Sources, refresh request-only sources, or decommission the current Workflow OS.

## Owner/surface

Owner/surface: Workflow v3 governance and interface integration.

## Persistence target

Persistence target: `workflow_v3/interfaces/**`.

## Interface files

- `workflow_v3/interfaces/README.md` - interface layer index.
- `workflow_v3/interfaces/00_INTERFACE_CANON.md` - global interface principles and locked vocabulary.
- `workflow_v3/interfaces/01_CONTEXT_AND_SOURCE_INTERFACE.md` - context entry and source authority contract.
- `workflow_v3/interfaces/02_RUNTIME_STATE_INTERFACE.md` - accepted-state and current-state surfaces.
- `workflow_v3/interfaces/03_WORK_RUN_ACCEPTANCE_INTERFACE.md` - bounded work, runs, evidence, results, and acceptance.
- `workflow_v3/interfaces/04_EVENT_LOOP_AND_ROUTING_INTERFACE.md` - Signals, Handlers, Action Inbox/Q, Check Jobs, closure, and Progression Router.
- `workflow_v3/interfaces/05_PACKET_AND_TRANSFER_INTERFACE.md` - packets and transfer between work surfaces.
- `workflow_v3/interfaces/06_STORAGE_ADOPTION_LEGACY_INTERFACE.md` - storage, adoption, legacy evidence, and coexistence seams.
- `workflow_v3/interfaces/07_ADAPTER_CODEX_PROVIDER_INTERFACE.md` - ChatGPT, Codex, human, GitHub, research, and future-provider boundaries.
- `workflow_v3/interfaces/08_PROJECT_SETUP_PACKS_INTERFACE.md` - Project setup, upload/cache, request-only sources, and pack boundaries.
- `workflow_v3/interfaces/09_QUALITY_EVAL_RECOVERY_INTERFACE.md` - quality gates, evaluation checks, and recovery paths.
- `workflow_v3/interfaces/10_PARALLEL_WORKSTREAM_BRANCH_POLICY.md` - parallel workstream ownership and branch policy.

## How future workstreams must use this package

Future Workflow v3 workstreams must read the relevant interface file before changing any surface it connects.

Workstreams may refine implementation inside their owned surface, but they must preserve interface contracts at boundaries unless an integration review explicitly updates the interface layer.

When a workstream needs to change a locked term, packet boundary, source-loading rule, state mutation rule, storage/adoption rule, adapter rule, or Project setup boundary, it must route through integration review before implementation proceeds.

## Inputs

Inputs are exact repository source reads, accepted records when they exist, current human instructions, verified excerpts, and bounded Launch Packets or workstream packages.

## Outputs

Outputs are interface contracts, candidate workstream constraints, validation requirements, and exact boundary language for future packages.

## State mutation rights

These files may define repository documentation/setup rules for Workflow v3 interfaces.

They do not mutate accepted per-Direction runtime state, Project UI state, Project Files/Sources state, old Workflow OS state, or Direction adoption state.

## Allowed producers

Allowed producers are explicit repository-maintenance packages, reviewed interface-integration workstreams, and bounded Codex packages authorized to edit `workflow_v3/interfaces/**`.

## Allowed consumers

Allowed consumers are Workflow v3 parent chats, child design chats, Codex packages, Check Jobs, Project setup rollout packages, adapter setup packages, quality/eval packages, and future adoption packages.

## Validation/evidence requirement

Validation must show changed files, allowed paths, EOF markers, source authority used, no forbidden path changes, no Direction runtime creation, no actual Project update, no Project Files/Sources refresh, and no contradiction with current `workflow_v3/**` model files.

## Forbidden behaviors

- Treating interface files as proof that a live runtime exists.
- Treating interface files as Direction adoption.
- Treating interface files as Project Instructions UI update or Project Files/Sources refresh.
- Treating candidate docs, packs, chats, or document existence as accepted state.
- Redefining detailed surface models without integration review.
- Using these files to decommission the current Workflow OS.

## Failure/recovery path

If an interface decision conflicts with current `workflow_v3/**` source authority, stop and return a Context Request or contradiction report naming the exact file/path/ref and question.

If validation fails inside the allowed scope, use same-package repair. If repair would require forbidden paths, Project update, Direction adoption, or legacy import, stop and split into a future package or human decision request.

## Dependencies

- `WORKFLOW_SOURCE_OF_TRUTH.md`
- `README.md`
- `directions_v3/README.md`
- `workflow_v3/README.md`
- `workflow_v3/ACTIVATION_STATUS.md`
- `workflow_v3/RUNTIME_MODEL.md`
- `workflow_v3/STORAGE_LAYOUT.md`
- `workflow_v3/PROJECT_SETUP_MODEL.md`
- `workflow_v3/LEGACY_EVIDENCE_POLICY.md`
- `workflow_v3/QUALITY_AND_RECOVERY.md`
- `workflow_v3/SIGNALS_HANDLERS_ACTION_INBOX.md`
- `workflow_v3/project_setup/**`
- `workflow_v3/templates/**`

END_OF_FILE: workflow_v3/interfaces/README.md
