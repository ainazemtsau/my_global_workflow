# Runtime State Interface

status: active_interface_layer

## Purpose

This file defines accepted-state and current-state surfaces for Workflow v3.

## Owner/surface

Owner/surface: runtime state boundaries across Direction Spine, Active Front, Work Graph, current status, current next move, Memory, and Runtime Console.

## Persistence target

Persistence target: `workflow_v3/interfaces/02_RUNTIME_STATE_INTERFACE.md` for shared rules; future adopted Direction state belongs only under `directions_v3/<direction-id>/runtime/**` after explicit adoption.

## State surfaces

Direction Spine is the stable axis of one Direction: root result, success conditions, spine points, and tracks.

Active Front is the selected part of the Direction Spine moving now.

Work Graph is local to the Active Front and identifies bounded work nodes, dependencies, and next useful results.

Current Status is a small readable summary of verified current state after acceptance.

Current Next Move is the exact next instruction after closure. It is not accepted state unless persisted through an explicit update path.

Memory stores promoted useful context. Raw chat output, Result Packets, Signals, run logs, or notes are not Memory Artifacts automatically.

## Accepted state vs candidate state

Accepted State changes only through explicit acceptance/update paths.

Candidate state includes chat output, child output, Codex output, Result Packets, Evidence, Signals, Handler results, Action Inbox items, Check Job findings, Progression Router output, Transition Packets, Project Files/Sources, packs, candidate docs, and document existence.

Candidate state may inform an Acceptance Decision, but it does not mutate accepted state by existing.

## What can mutate accepted state

Only an explicit acceptance/update path with adequate evidence may mutate accepted state.

After future Direction adoption, accepted-state mutations must target the adopted Direction runtime storage under `directions_v3/<direction-id>/runtime/**` and preserve evidence links.

## What cannot mutate accepted state

The following cannot mutate accepted state by themselves:

- chat memory;
- Project Files/Sources;
- uploaded files;
- candidate docs;
- Codex output;
- Result Packets;
- Evidence records;
- Signals;
- Handler results;
- Action Inbox/Q items;
- Check Job findings;
- Runtime Console output;
- Transition Packets;
- file existence alone.

## Runtime Console boundary

Runtime Console is read-only.

It may summarize status, show uncertainty, list candidate actions, and draft candidate Launch Packets or Next Moves.

It must not execute material work, mutate accepted state, accept evidence, promote Memory, launch Codex directly, close Action Inbox items silently, or become a hidden controller.

## State read/write preconditions

State reads require exact source authority and must classify cache/context separately from accepted records.

State writes require:

- explicit adoption if writing per-Direction Workflow v3 runtime state;
- explicit Work Contract or acceptance/update scope;
- evidence sufficient for the update;
- allowed path confirmation;
- validation of EOF markers and forbidden path non-mutation when Markdown files are changed;
- rollback/coexistence check when old Workflow OS or old Direction files are near the boundary.

## Inputs

Inputs are accepted records, exact repository reads, Work Contracts, Evidence, Acceptance Decisions, promoted Memory updates, and explicit human decisions.

## Outputs

Outputs are state reads, candidate state summaries, accepted-state updates after approval, Memory promotion candidates, and exact Next Move records.

## State mutation rights

This interface has no direct runtime mutation rights.

Future per-Direction state may be mutated only by explicit acceptance/update packages after adoption. Shared `workflow_v3/**` documentation/setup files may be edited by repository-maintenance packages.

## Allowed producers

Allowed producers are acceptance/update packages, repository-maintenance packages, validated Codex packages, and human decisions routed through explicit acceptance.

## Allowed consumers

Allowed consumers are Work Contracts, parent chats, Check Jobs, Runtime Console views, Event Loop Closure, Progression Router, Project setup, and adapter handoffs.

## Validation/evidence requirement

Validation must show the source of accepted state, whether candidate state is separated, what evidence supports mutation, and the exact paths changed or not changed.

## Forbidden behaviors

- Inferring accepted state from document existence.
- Treating current chat memory as runtime storage.
- Creating `directions_v3/<direction-id>/runtime/**` without an explicit adoption package.
- Letting Runtime Console become a controller.
- Promoting Memory without an explicit promotion/update path.
- Treating old `directions/**` files as `accepted_v3_state`.

## Failure/recovery path

If accepted state cannot be identified, stop with a Context Request.

If candidate and accepted state conflict, run a bounded Check Job or request human acceptance review.

If a state write would require adoption/import/project update outside scope, stop and split into a future package.

## Dependencies

- `workflow_v3/RUNTIME_MODEL.md`
- `workflow_v3/STORAGE_LAYOUT.md`
- `workflow_v3/LEGACY_EVIDENCE_POLICY.md`
- `workflow_v3/QUALITY_AND_RECOVERY.md`

END_OF_FILE: workflow_v3/interfaces/02_RUNTIME_STATE_INTERFACE.md
