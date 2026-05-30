# Workflow v3 Runtime Model

status: active_skeleton_namespace_corrected

## One-line model

Direction Spine -> Active Front -> Work Graph -> Work Contract / Run / Evidence / Acceptance -> Memory -> Signals / Handlers / Action Inbox -> Next Move

This model describes how future Workflow v3 work should be bounded, executed, evidenced, accepted, remembered, and resumed.

## Direction Spine

Direction Spine is the stable axis of one Direction: root result, success conditions, spine points, and tracks. It is not a complete roadmap and not a backlog.

Direction Spine changes only through an explicit acceptance/update path.

## Active Front

Active Front is the selected part of the Direction Spine that is moving now. It limits attention and prevents the whole project from becoming active at once.

Active Front is not global backlog state.

## Work Graph

Work Graph is local to the Active Front. It identifies bounded nodes, dependencies, and the next useful result.

Work Graph is not a copy of the Direction Spine and not a permanent graph for the whole Direction.

## Work Contract / Run / Evidence / Acceptance

Work Contract states the bounded target, allowed and forbidden surfaces, expected result, and evidence requirements.

Run is execution of that contract through an adapter or human action.

Evidence is the verifiable output of a Run. Evidence alone does not change accepted state.

Acceptance is the explicit decision to accept, reject, or return a result for repair. Accepted State changes only through the explicit acceptance/update path.

## Memory

Memory stores useful promoted context for later continuation. Raw chat output, Result Packets, Signals, run logs, or notes are not Memory Artifacts automatically.

Memory requires promotion and does not replace canonical storage.

## Signals / Handlers / Action Inbox

Signal is a recorded fact. It does not mutate state.

Handler reacts to a Signal by creating candidate actions only. It does not execute work and does not accept state.

Action Inbox stores candidate actions for later review, conversion, or closure. It is not an automatic execution queue and not a roadmap.

## Next Move

Next Move is the exact next instruction after material work or review. It tells the user what to open, paste, verify, decide, or stop.

Next Move is not accepted state.

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
