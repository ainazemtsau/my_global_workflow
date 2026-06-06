# Workflow v3 Runtime Model

status: active_skeleton_namespace_corrected

## Overview Model

Workflow v3 runtime is main-procedure driven:

```text
Registry selects exactly one main procedure
-> START shows the selected procedure contract and waits
-> RUN executes the declared stage sequence
-> child procedure calls support RUN only when required
-> child procedure returns are matched and verified
-> CHECK compares actual result to selected completion
-> FINISH audits open gates and closes
-> CLOSED carries only post-closed continuation or no continuation
```

Detailed interface summaries live under `workflow_v3/interfaces/**`. Runtime authority lives under `workflow_v3/control_plane/**` and selected procedure files.

## Lifecycle Movement

```text
START
-> RUN_STAGE
-> STAGE_RESULT
-> RUN_WAITING_FOR_CHILD_RETURN when a child call is required
-> CHILD_RETURN_VERIFICATION
-> RUN_STAGE or CHECK
-> CHECK
-> FINISH
-> CLOSED

CHECK -> RUN repair
CHECK -> blocked escalation
FINISH -> RUN repair or blocked escalation if audit fails
```

START performs no material work. It selects one main procedure through the registry, reads that procedure, shows its completion contract, shows material stages and boundaries, and waits for START / СТАРТ.

RUN executes the selected main procedure only. Runtime must execute the selected procedure's declared stages. It must not invent ad hoc simple, compact, shortcut, or single-stage compression that bypasses declared stages. A stage may end quickly or be marked not_applicable with evidence, but applicable declared stages remain represented in progression. RUN emits `STAGE_RESULT` after each material stage and waits for CONTINUE / ДАЛЬШЕ before the next material stage unless the next step is `internal_check`.

`CHILD_PROCEDURE_CALL` is the canonical runtime object for external or subordinate work. Codex, child chat, check job, storage update, research agent, GitHub/file access, human decision, and future providers are child/adapters under this model. `UTILITY_CALL` and `UTILITY_RETURN` may remain as adapter-level compatibility labels, but they are not a separate lifecycle model.

`CHILD_PROCEDURE_RETURN` is evidence and must be matched to the open child call, verified, and integrated before reliance.

CHECK emits `CLOSURE_CHECK` against the selected procedure `completion:` contract.

FINISH closes only when audit passes. CLOSED means no new material START in the same chat.

## Closure Blockers

The following invariants block CHECK, FINISH, and CLOSED:

- `open_child_calls != empty`;
- `missing_child_return`;
- `unverified_child_return`;
- missing required validation or evidence;
- actual result is only a handoff, card, package, copy-paste packet, Codex package, check packet, storage packet, child-chat card, or other child-call artifact.

## Object Hierarchy

```text
Direction Spine -> Direction Map / Goal Evidence Graph -> Active Front -> Work Graph -> Work Contract
```

Steering entities are formed through registered procedures before templates are filled or candidates are proposed for acceptance.

## Work Contract / Run / Evidence / Acceptance

Work Contract states a bounded target, allowed and forbidden execution boundaries, expected result, and evidence requirements.

Run is execution of that contract by the selected main procedure, with optional child/adaptor support. Evidence is the verifiable output of a Run. Evidence alone does not change accepted state.

Acceptance is the explicit decision to accept, reject, or return a result for repair. Accepted State changes only through the explicit acceptance/update path.

## Closure Output Model

Procedure closure uses:

- `CLOSURE_CHECK` comparing actual result to selected procedure completion;
- `FINISH_PACKET` after explicit FINISH and passed audit;
- human-readable result and evidence;
- post-closed `NEXT_CHAT_CARD` when a new independent lifecycle is needed, otherwise `no_next_chat_needed` with reason.

NEXT_CHAT_CARD is post-closed continuation only. It is not a child call, not a utility launch, and not evidence that the current START goal has completed. It must not carry unfinished child work required by the current START goal.

## Direction Entities

Direction Spine is the stable axis of one Direction: root result, success conditions, spine points, and tracks. It is not a complete roadmap and not a backlog.

Direction Map is the structural map between Direction Spine and Active Front. It contains map areas, track relationships, strategic dependencies, strategic uncertainties, candidate fronts, closed fronts, blocked areas, evidence links, and accepted/candidate/unresolved labels.

Goal Evidence Graph traces root outcome through claims, alternatives, obstacles, evidence requirements, and candidate focus choices. It is candidate until accepted through the explicit acceptance/update path.

Active Front is the accepted focus selected from the Direction Map that is moving now. Work Graph is local to the Active Front. Work Contract is the bounded executable unit.

## Adapter Boundary

ChatGPT, Codex, Claude Code/future code assistants, research agents, GitHub/file access, future AI providers, and human actions are adapters or role implementations.

Adapters may perform utility work and return candidate result/evidence. They do not decide acceptance, route, product meaning, scope expansion, or Direction adoption.

## No Hidden Accepted State

Accepted State does not live in chat memory, Project Files/Sources, candidate docs, code-assistant output, STAGE_RESULTs, FINISH_PACKETs, NEXT_CHAT_CARDs, transfer packets, check-job output, or document existence.

If accepted state matters, use canonical repository storage and explicit acceptance/update records.

## Runtime Console Boundary

Runtime Console is read-only. It may summarize status, show uncertainty, list candidate actions, and draft candidate launch packets or next-chat cards.

Runtime Console must not execute material work, mutate accepted state, accept evidence, promote Memory, launch utilities directly, or become a hidden controller.

END_OF_FILE: workflow_v3/RUNTIME_MODEL.md
