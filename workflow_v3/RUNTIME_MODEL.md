# Workflow v3 Runtime Model

status: active_skeleton_namespace_corrected

## Overview model

Object hierarchy:

```text
Direction Spine -> Direction Map / Goal Evidence Graph -> Active Unresolved Cut -> Active Front -> Work Graph -> Work Contract
```

Procedure movement:

```text
START -> RUN -> FINISH -> FINISH_PACKET + Result Packet + Next Move Packet
```

Control-plane movement:

```text
Intake -> Procedure Registry -> Procedure Source Read -> Run Surface Contract -> START_PACKET -> admitted RUN or typed STOP
```

This model describes how future Workflow v3 work is structurally bounded, executed, evidenced, accepted, remembered, transferred, and resumed.

Detailed interface contracts live under `workflow_v3/interfaces/**`. Future work must reconcile with that interface layer instead of redefining Direction structure, lifecycle closure, packets, storage, or adapter boundaries independently.

Steering entities are formed through registered procedures before templates are filled or candidates are proposed for acceptance.

Object movement:

```text
Direction Spine
-> Direction Map / Goal Evidence Graph
-> Active Unresolved Cut
-> Active Front
-> Work Graph
-> Work Contract
-> Run/Evidence
-> Parent Integration
-> Graph Delta / Escalation / Downstream Delta / Acceptance
-> Next Move Packet
```

## Control-plane boundary

Workflow movement passes through action admission before material action.

Next Move Packet output is not launch authority by itself. FINISH output does not silently launch next work.

Every material action has `run_surface_type` and explicit allowed and forbidden operations.

Storage mutation is a separate `storage_update_adapter` run. GitHub write tools are default-denied by workflow policy unless that adapter is admitted by exact package.

Accepted state remains canonical repository state only after accepted update path and verification.

## Setup-only root and Direction Definition

Ordinary Direction Project root/bootstrap is technical setup only.

Setup-only root may create placeholder pending semantic state, Project Binding, per-Direction Project setup sources, `CURRENT_STATUS = setup_only_root_created`, and `CURRENT_NEXT_MOVE = launch_direction_definition`.

Setup-only root must not require or accept root outcome, Direction Spine, Direction Map, Active Front, Work Graph, or product strategy.

Direction Definition is the separate semantic formation process that forms candidate Direction Spine, Direction Map, and first Active Front after setup-only root exists.

## Direction Spine

Direction Spine is the stable axis of one Direction: root result, success conditions, spine points, and tracks. It is not a complete roadmap and not a backlog.

Direction Spine changes only through an explicit acceptance/update path.

## Direction Map

Direction Map is the global structural map between Direction Spine and Active Front. It contains map areas, track relationships, strategic dependencies, strategic uncertainties, candidate fronts, closed fronts, blocked areas, evidence links, and accepted/candidate/unresolved labels.

Direction Map is not a roadmap, backlog, Work Graph, or unreviewed task list.

Direction Map changes only through an explicit acceptance/update path.

## Goal Evidence Graph

Goal Evidence Graph is a Direction Map-associated steering/control artifact. It traces the root outcome through claims, alternatives, obstacles, evidence requirements, and candidate focus choices.

It is not a semantic primitive and is not accepted state by existence.

Goal Evidence Graph output is candidate until accepted through the explicit acceptance/update path. It may be embedded in Direction Map or associated as a split artifact after a future accepted runtime package.

Route-changing effects from graph review are represented by typed outputs such as Parent Integration Result, Graph Delta, Upstream Escalation Packet, Downstream Delta Packet, Derived Gate Check, Acceptance Decision, and Next Move Packet, not by legacy event/signal routing.

## Active Front

Active Front is the accepted focus selected from the Direction Map that is moving now. It limits attention and prevents the whole project from becoming active at once.

Active Front is not global backlog state.

When a Goal Evidence Graph exists, Active Front selection should reference the Active Unresolved Cut and explain why the selected unresolved nodes matter now.

## Work Graph

Work Graph is local to the Active Front. It derives from Front Exit Criteria and identifies bounded nodes, dependencies, and the next useful result.

Work Graph is not a copy of the Direction Spine, not the Direction Map, and not a permanent graph for the whole Direction.

Work Graph nodes preserve trace to their parent front, map claim, or Goal Evidence Graph node.

## Work Contract / Run / Evidence / Acceptance

Work Contract states the bounded target, allowed and forbidden surfaces, expected result, and evidence requirements.

Run is execution of that contract through an adapter or human action.

Evidence is the verifiable output of a Run. Evidence alone does not change accepted state.

Acceptance is the explicit decision to accept, reject, or return a result for repair. Accepted State changes only through the explicit acceptance/update path.

## Procedure Closure Output Model

Procedure closure uses:

- FINISH_REQUEST when RUN reaches completion or a terminal blocked state;
- FINISH_PACKET after explicit user FINISH;
- one Result Packet;
- one Next Move Packet.

The Result Packet carries status, result, evidence, changed files, validation, source limits, not done, refresh requirements, residual risks, and exact next move.

The Next Move Packet selects exactly one primary next move and names its type, return destination, transfer packet if needed, persistence boundary, acceptance boundary, and blocking reason if any.

FINISH output may request a same-chat continuation, next material chat, child chat, check job, Codex run, Codex verification, human decision, storage update, or stop. It must not launch any of them invisibly.

## Typed procedure outputs

Procedure stages and gates return typed outputs:

- `PASS`
- `PASS_WITH_RISK`
- `REWORK`
- `EXPAND`
- `STOP`
- `TRANSFER`

Future typed output packets may include Parent Integration Result, Graph Delta, Upstream Escalation Packet, Downstream Delta Packet, Derived Gate Check, and Memory Candidate. These are candidate outputs until accepted or routed through an admitted procedure.

Procedure gate lenses are internal procedure checks, not separate runtime entities:

- `strategy`
- `discovery`
- `delivery_flow`
- `verification`
- `interface_dependency`
- `risk_gate`
- `memory_learning`

## Next Move

Next Move is the exact next instruction after material work or review. It tells the user what to open, paste, verify, decide, or stop.

Next Move is not accepted state.

Current Next Move formation remains a bounded procedure. When material work closes, FINISH selects one primary next move inside the Next Move Packet.

If transfer is needed, FINISH includes or references a complete Transfer Packet for the selected next step.

Chat does not choose route by intuition. Route-changing steps must be visible through FINISH_PACKET, Result Packet, Next Move Packet, and acceptance/update path when state changes.

## Memory

Memory stores useful promoted context for later continuation. Raw chat output, Result Packets, run logs, or notes are not Memory Artifacts automatically.

Memory requires promotion and does not replace canonical storage.

## Adapter boundary

ChatGPT, Codex, Claude Code/future code assistants, Deep Research/research agents, GitHub access, future AI providers, and human actions are adapters or role implementations.

Adapters may perform a Run and return candidate result/evidence. They do not decide acceptance, route, product meaning, scope expansion, or Direction adoption.

## No hidden accepted state

Accepted State does not live in chat memory, Project Files/Sources, candidate docs, Codex output, Result Packets, transfer packets, check-job output, or document existence.

If accepted state matters, use canonical repository storage and explicit acceptance/update records.

## Runtime Console boundary

Runtime Console is read-only. It may summarize status, show uncertainty, list candidate actions, and draft candidate launch packets or Next Moves.

Runtime Console must not execute material work, mutate accepted state, accept evidence, promote Memory, launch Codex directly, or become a hidden controller.

END_OF_FILE: workflow_v3/RUNTIME_MODEL.md
