# Workflow v3 Runtime Model

status: active_skeleton_namespace_corrected

## Overview model

Object hierarchy:

```text
Direction Spine -> Direction Map -> Active Front -> Work Graph -> Work Contract
```

Operational movement:

```text
Signal -> Handler -> Candidate Output -> Event Loop Closure -> Progression Router -> Transition Packet / Next Move -> Acceptance/update path
```

This model describes how future Workflow v3 work should be structurally bounded, operationally routed, executed, evidenced, accepted, remembered, and resumed.

Detailed interface contracts live under `workflow_v3/interfaces/**`. Future work must reconcile with that interface layer instead of redefining Direction structure, lifecycle routing, packets, storage, or adapter boundaries independently.

Steering entities are formed through `workflow_v3/formation/**` before templates are filled or candidates are proposed for acceptance.

## Setup-only root and Direction Definition

Ordinary Direction Project root/bootstrap is technical setup only.

Setup-only root may create placeholder pending semantic state, Project Binding, per-Direction Project setup sources, `CURRENT_STATUS = setup_only_root_created`, and `CURRENT_NEXT_MOVE = launch_direction_definition`.

Setup-only root must not require or accept root outcome, Direction Spine, Direction Map, Active Front, Work Graph, or product strategy.

Direction Definition is the separate semantic formation process that forms candidate Direction Spine, Direction Map, and first Active Front after setup-only root exists.

## Direction Spine

Direction Spine is the stable axis of one Direction: root result, success conditions, spine points, and tracks. It is not a complete roadmap and not a backlog.

Direction Spine formation uses `workflow_v3/formation/DIRECTION_SPINE_FORMATION_RUNBOOK.md`.

Direction Spine changes only through an explicit acceptance/update path.

## Direction Map

Direction Map is the global structural map between Direction Spine and Active Front. It contains map areas, track relationships, strategic dependencies, strategic uncertainties, candidate fronts, closed fronts, blocked areas, evidence links, and accepted/candidate/unresolved labels.

Direction Map is not a roadmap, backlog, Work Graph, or Action Inbox.

Direction Map formation uses `workflow_v3/formation/DIRECTION_MAP_FORMATION_RUNBOOK.md`.

Direction Map changes only through an explicit acceptance/update path.

## Active Front

Active Front is the accepted focus selected from the Direction Map that is moving now. It limits attention and prevents the whole project from becoming active at once.

Active Front is not global backlog state.

Active Front formation uses `workflow_v3/formation/ACTIVE_FRONT_FORMATION_RUNBOOK.md`.

## Work Graph

Work Graph is local to the Active Front. It derives from Front Exit Criteria and identifies bounded nodes, dependencies, and the next useful result.

Work Graph is not a copy of the Direction Spine, not the Direction Map, and not a permanent graph for the whole Direction.

Work Graph formation uses `workflow_v3/formation/WORK_GRAPH_FORMATION_RUNBOOK.md`.

## Work Contract / Run / Evidence / Acceptance

Work Contract states the bounded target, allowed and forbidden surfaces, expected result, and evidence requirements.

Work Contract formation uses `workflow_v3/formation/WORK_CONTRACT_FORMATION_RUNBOOK.md`.

Run is execution of that contract through an adapter or human action.

Evidence is the verifiable output of a Run. Evidence alone does not change accepted state.

Acceptance is the explicit decision to accept, reject, or return a result for repair. Accepted State changes only through the explicit acceptance/update path.

Acceptance Decision formation uses `workflow_v3/formation/ACCEPTANCE_DECISION_FORMATION_RUNBOOK.md`.

## Memory

Memory stores useful promoted context for later continuation. Raw chat output, Result Packets, Signals, run logs, or notes are not Memory Artifacts automatically.

Memory requires promotion and does not replace canonical storage.

Memory Artifact promotion uses `workflow_v3/formation/MEMORY_ARTIFACT_PROMOTION_RUNBOOK.md`.

## Signals / Handlers / Action Inbox

The operational event loop is defined in `workflow_v3/SIGNALS_HANDLERS_ACTION_INBOX.md`.

Signal is an emitted event/fact record. It does not mutate state.

Signal is not an Action Inbox item.

Handler reacts to a Signal by creating candidate outputs only. It does not execute work and does not accept state.

Action Inbox stores candidate actions, not raw signals.

Action Inbox stores candidate actions for later review, conversion, or closure. It is not an automatic execution queue and not a roadmap.

## Next Move

Next Move is the exact next instruction after material work or review. It tells the user what to open, paste, verify, decide, or stop.

Next Move is not accepted state.

Current Next Move formation uses `workflow_v3/formation/CURRENT_NEXT_MOVE_FORMATION_RUNBOOK.md`.

When material work closes, the next concrete step is selected through Event Loop Closure and `progression_router_handler`.

The progression output remains candidate until accepted or explicitly launched.

If transfer is needed, the router assembles the complete Transition Packet for the selected next step.

Chat does not choose route by intuition. Route-changing steps must be visible through Signal, Handler, Event Loop Closure, Progression Router, Transition Packet/Next Move, and acceptance/update path when state changes.

## Adapter boundary

ChatGPT, Codex, Claude Code/future code assistants, Deep Research/research agents, GitHub access, future AI providers, and human actions are adapters or role implementations.

Adapters may perform a Run and return candidate result/evidence. They do not decide acceptance, route, product meaning, scope expansion, or Direction adoption.

## No hidden accepted state

Accepted State does not live in chat memory, Project Files/Sources, candidate docs, Codex output, Result Packets, Signals, Handler results, Action Inbox items, or document existence.

If accepted state matters, use canonical repository storage and explicit acceptance/update records.

## Runtime Console boundary

Runtime Console is read-only. It may summarize status, show uncertainty, list candidate actions, and draft candidate Launch Packets or Next Moves.

Runtime Console must not execute material work, mutate accepted state, accept evidence, promote Memory, launch Codex directly, or become a hidden controller.

END_OF_FILE: workflow_v3/RUNTIME_MODEL.md
