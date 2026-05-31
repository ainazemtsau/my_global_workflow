# Workflow v3 Interface Canon

status: active_interface_layer

## Purpose

This file defines global interface principles and locked vocabulary for Workflow v3.

## Owner/surface

Owner/surface: Workflow v3 interface canon and integration review.

## Persistence target

Persistence target: `workflow_v3/interfaces/00_INTERFACE_CANON.md`.

## Strict/flexible design principle

Workflow v3 uses strict contracts at boundaries and flexible implementation inside owned surfaces.

Strict boundary rules:

- no hidden state;
- no hidden controller;
- no black-box adapter;
- no implicit acceptance;
- no user-forced schema/YAML;
- no silent source promotion;
- no implicit Direction adoption;
- AI receives bounded context and returns bounded evidence.

Flexible implementation rules:

- a surface may choose its internal organization when it preserves its published inputs, outputs, mutation rights, evidence requirements, and failure paths;
- a provider may use its own tools when it obeys the Launch Packet and returns limitations;
- a Project may choose compact setup payloads when source authority, cache/context, and request-only boundaries remain explicit.

## Locked namespaces

- `workflow_v3/**` - Workflow v3 shared rules/setup namespace and interface layer.
- `directions_v3/<direction-id>/runtime/**` - future per-Direction Workflow v3 runtime state only after explicit adoption.
- `workflow/**` - current Workflow OS and rollback context.
- `directions/**` - old Direction namespace treated as `legacy_evidence` for Workflow v3 unless an explicit bridge/import/adoption package says otherwise.

## Locked terms

These terms are locked at Workflow v3 boundaries:

- Direction Spine
- Active Front
- Work Graph
- Work Contract
- Run
- Evidence
- Acceptance
- Accepted State
- Memory
- Signal
- Handler
- Action Inbox/Q
- Check Job
- Event Loop Closure
- Progression Router
- Next Move
- Transition Packet
- Launch Packet
- Result Packet
- Project Instructions UI
- Project Files/Sources
- request-only sources
- legacy_evidence
- accepted_v3_state
- clean_start
- bridge_only
- selective_import
- full_migration
- no_adoption

Locked terms may not be redefined by a workstream without integration review and an explicit interface-layer update.

## Inputs

Inputs are verified `workflow_v3/**` source files, exact repo/path/ref reads, current human instructions, and bounded workstream design evidence.

## Outputs

Outputs are locked vocabulary, interface principles, and change-control constraints for future Workflow v3 packages.

## State mutation rights

This canon may mutate only repository interface documentation when an authorized package edits it.

It does not mutate accepted Direction state, Project UI state, Project Files/Sources state, Direction adoption state, legacy import state, or current Workflow OS state.

## Allowed producers

Allowed producers are integration review packages, repository-maintenance packages, and bounded Codex packages authorized to edit the interface layer.

## Allowed consumers

Allowed consumers are all Workflow v3 workstreams, provider handoffs, Project setup packages, quality checks, and adoption packages.

## Validation/evidence requirement

Any change must show exact source authority, changed files, allowed paths, EOF markers, and a compatibility check against `workflow_v3/RUNTIME_MODEL.md`, `workflow_v3/SIGNALS_HANDLERS_ACTION_INBOX.md`, `workflow_v3/STORAGE_LAYOUT.md`, `workflow_v3/PROJECT_SETUP_MODEL.md`, `workflow_v3/LEGACY_EVIDENCE_POLICY.md`, and `workflow_v3/QUALITY_AND_RECOVERY.md`.

## Forbidden behaviors

- Redefining a locked term in a child workstream.
- Treating an implementation convenience as a boundary contract.
- Hiding accepted state in chat, packs, adapter output, or Project Files/Sources.
- Treating provider-specific features as Workflow v3 authority.
- Making users assemble partial fragments into hidden schemas or prompts.
- Claiming adoption, import, Project update, or runtime activation by implication.

## Failure/recovery path

If a locked term is ambiguous or contradictory in verified sources, stop and return a Context Request naming the exact path/ref/question.

If a proposed change would cross multiple surfaces, split it into an integration package before implementation.

If validation fails but the scope remains allowed, repair in the same package and revalidate.

## Dependencies

- `workflow_v3/RUNTIME_MODEL.md`
- `workflow_v3/SIGNALS_HANDLERS_ACTION_INBOX.md`
- `workflow_v3/STORAGE_LAYOUT.md`
- `workflow_v3/PROJECT_SETUP_MODEL.md`
- `workflow_v3/LEGACY_EVIDENCE_POLICY.md`
- `workflow_v3/QUALITY_AND_RECOVERY.md`

END_OF_FILE: workflow_v3/interfaces/00_INTERFACE_CANON.md
