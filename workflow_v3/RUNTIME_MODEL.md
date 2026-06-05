# Workflow v3 Runtime Model

status: active_skeleton_namespace_corrected

## Overview Model

Workflow v3 runtime is main-procedure driven:

```text
Registry selects exactly one main procedure
-> selected procedure defines completion
-> chat executes stages
-> optional utility calls support the same procedure
-> CHECK compares actual result to completion
-> FINISH audits and closes
-> CLOSED includes NEXT_CHAT_CARD or no_next_chat_needed
```

Detailed interface summaries live under `workflow_v3/interfaces/**`. Runtime authority lives under `workflow_v3/control_plane/**` and selected procedure files.

## Lifecycle Movement

```text
START -> RUN -> CHECK -> FINISH -> CLOSED
RUN -> UTILITY_CALL -> UTILITY_RETURN -> RUN
CHECK -> RUN repair
CHECK -> blocked escalation
FINISH -> RUN repair or blocked escalation if audit fails
```

START performs no material work. It selects one main procedure through the registry, reads that procedure, shows its completion contract, shows material stages and boundaries, and waits for START / СТАРТ.

RUN executes the selected main procedure only. It emits `STAGE_RESULT` after each material stage and waits for CONTINUE / ДАЛЬШЕ before the next material stage unless the next step is `internal_check`.

UTILITY_CALL is a visible supporting call to Codex, another code assistant, child chat, check job, research agent, GitHub/file access, storage update, human decision, or future admitted provider. UTILITY_RETURN is evidence and must be verified before reliance.

CHECK emits `CLOSURE_CHECK` against the selected procedure `completion:` contract.

FINISH closes only when audit passes. CLOSED means no new material START in the same chat.

## Object Hierarchy

```text
Direction Spine -> Direction Map / Goal Evidence Graph -> Active Front -> Work Graph -> Work Contract
```

Steering entities are formed through registered procedures before templates are filled or candidates are proposed for acceptance.

## Work Contract / Run / Evidence / Acceptance

Work Contract states a bounded target, allowed and forbidden execution boundaries, expected result, and evidence requirements.

Run is execution of that contract by the selected main procedure, with optional utility support. Evidence is the verifiable output of a Run. Evidence alone does not change accepted state.

Acceptance is the explicit decision to accept, reject, or return a result for repair. Accepted State changes only through the explicit acceptance/update path.

## Closure Output Model

Procedure closure uses:

- `CLOSURE_CHECK` comparing actual result to selected procedure completion;
- `FINISH_PACKET` after explicit FINISH and passed audit;
- human-readable result and evidence;
- `NEXT_CHAT_CARD` when workflow continuation is needed, otherwise `no_next_chat_needed` with reason.

NEXT_CHAT_CARD is not a hardcoded next-step enum. It is derived from selected main procedure, actual result, completion check, unresolved work, and the next intended workflow step.

## Direction Entities

Direction Spine is the stable axis of one Direction: root result, success conditions, spine points, and tracks. It is not a complete roadmap and not a backlog.

Direction Map is the structural map between Direction Spine and Active Front. It contains map areas, track relationships, strategic dependencies, strategic uncertainties, candidate fronts, closed fronts, blocked areas, evidence links, and accepted/candidate/unresolved labels.

Goal Evidence Graph traces root outcome through claims, alternatives, obstacles, evidence requirements, and candidate focus choices. It is candidate until accepted through the explicit acceptance/update path.

Active Front is the accepted focus selected from the Direction Map that is moving now. Work Graph is local to the Active Front. Work Contract is the bounded executable unit.

## Adapter Boundary

ChatGPT, Codex, Claude Code/future code assistants, research agents, GitHub/file access, future AI providers, and human actions are adapters or role implementations.

Adapters may perform utility work and return candidate result/evidence. They do not decide acceptance, route, product meaning, scope expansion, or Direction adoption.

## No Hidden Accepted State

Accepted State does not live in chat memory, Project Files/Sources, candidate docs, code-assistant output, Result Packets, transfer packets, check-job output, or document existence.

If accepted state matters, use canonical repository storage and explicit acceptance/update records.

## Runtime Console Boundary

Runtime Console is read-only. It may summarize status, show uncertainty, list candidate actions, and draft candidate launch packets or next-chat cards.

Runtime Console must not execute material work, mutate accepted state, accept evidence, promote Memory, launch utilities directly, or become a hidden controller.

END_OF_FILE: workflow_v3/RUNTIME_MODEL.md