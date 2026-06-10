# Workflow v3 Runtime Model

status: active_skeleton_namespace_corrected

## Overview Model

Workflow v3 runtime is main-procedure driven:

```text
Registry selects exactly one main procedure
-> START shows the selected procedure contract and waits
-> RUN executes the declared stage sequence
-> dependency calls support RUN only when required
-> dependency returns are matched and verified
-> CHECK compares actual result to selected completion
-> FINISH audits open gates and closes
-> CLOSED carries only post-closed continuation or no continuation
```

Detailed interface summaries live under `workflow_v3/interfaces/**`. Runtime authority lives under `workflow_v3/control_plane/**` and selected procedure files. Dependency type selection and wrong-surface behavior live in `workflow_v3/control_plane/ROUTING_AND_DEPENDENCY_PROTOCOL.md`.

## Lifecycle Movement

```text
START
-> RUN_STAGE
-> STAGE_RESULT
-> RUN_WAITING_FOR_DEPENDENCY_RETURN when a dependency is required
-> DEPENDENCY_RETURN_VERIFICATION
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

`DEPENDENCY_CALL` is the canonical runtime object for external or subordinate work needed before the selected owner can complete. Prior packet labels are unsupported and must be rejected or rewritten before the parent RUN relies on them.

Required current-goal repair through a dependency is deterministic. If RUN detects repair needed and the selected parent cannot complete directly, RUN emits/opens `DEPENDENCY_CALL`, records the call in `open_dependencies`, enters `RUN_WAITING_FOR_DEPENDENCY_RETURN`, and waits for matching `DEPENDENCY_RETURN` / `CODEX_RETURN_PACKET`. CONTINUE / ДАЛЬШЕ, CHECK, FINISH, and CLOSED are invalid until the return is verified or an explicit blocked result is produced.

`DEPENDENCY_RETURN` is evidence and must be matched to the open dependency call, verified, and integrated before reliance.

CHECK emits `CLOSURE_CHECK` against the selected procedure `completion:` contract.

FINISH closes only when audit passes. CLOSED means no new material START in the same chat.

## Closure Blockers

The following invariants block CHECK, FINISH, and CLOSED:

- `open_dependencies != empty`;
- `missing_dependency_return`;
- `unverified_dependency_return`;
- `required_dependency_work_detected = true` with `dependency_call_opened = false`;
- missing required validation or evidence;
- actual result is only a handoff, card, package, copy-paste packet, Codex package, check packet, storage packet, dependency packet, or other dependency artifact.

## Object Hierarchy

```text
Direction Spine -> Direction Map / Goal Evidence Graph -> Active Front -> Work Graph -> Work Contract
```

Steering entities are formed through registered procedures before templates are filled or candidates are proposed for acceptance.

## Work Contract / Run / Evidence / Acceptance

Work Contract states a bounded target, allowed and forbidden execution boundaries, expected result, and evidence requirements.

Run is execution of that contract by the selected main procedure, with optional dependency support. Evidence is the verifiable output of a Run. Evidence alone does not change accepted state.

Acceptance is the explicit decision to accept, reject, or return a result for repair. Accepted State changes only through the explicit acceptance/update path.

## Closure Output Model

Procedure closure uses:

- `CLOSURE_CHECK` comparing actual result to selected procedure completion;
- `FINISH_PACKET` after explicit FINISH and passed audit;
- human-readable result and evidence;
- post-closed `NEXT_CHAT_CARD` when a new independent lifecycle is needed, otherwise `no_next_chat_needed` with reason.

NEXT_CHAT_CARD is post-closed continuation only. It is not a dependency call, not a support launch, and not evidence that the current START goal has completed. It must not carry unfinished dependency work required by the current START goal.

## Direction Entities

Direction Spine is the stable axis of one Direction: root result, success conditions, spine points, and tracks. It is not a complete roadmap and not a backlog.

Direction Map is the structural map between Direction Spine and Active Front. It contains map areas, track relationships, strategic dependencies, strategic uncertainties, candidate fronts, closed fronts, blocked areas, evidence links, and accepted/candidate/unresolved labels.

Goal Evidence Graph traces root outcome through claims, alternatives, obstacles, evidence requirements, and candidate focus choices. It is candidate until accepted through the explicit acceptance/update path.

Active Front is the accepted focus selected from the Direction Map that is moving now. Work Graph is local to the Active Front. Work Contract is the bounded executable unit.

## Dependency Boundary

Execution/dependency surface is separate from the selected owner procedure. Workflow v3 recognizes typed dependencies including support dependency, code repository, core lifecycle, storage persistence, and human decision dependencies.

Code/repository mutation routes only through Codex/code assistant as `code_repository_dependency`. ChatGPT parent may draft packets and verify returns, but must not write, probe writes, create branches, commit, push, or apply patches.

Dependencies may return candidate result/evidence. They do not decide acceptance, product meaning, scope expansion, Direction adoption, CHECK, FINISH, or CLOSED.

## No Hidden Accepted State

Accepted State does not live in chat memory, Project Files/Sources, candidate docs, code-assistant output, STAGE_RESULTs, FINISH_PACKETs, NEXT_CHAT_CARDs, transfer packets, dependency output, check-job output, or document existence.

If accepted state matters, use canonical repository storage and explicit acceptance/update records.

## Runtime Console Boundary

Runtime Console is read-only. It may summarize status, show uncertainty, list candidate actions, and draft future launch or next-chat cards when no current-goal repair is required.

Runtime Console must not execute material work, mutate accepted state, accept evidence, promote Memory, launch dependencies directly, defer required current-goal dependency repair into future operator action while continuing, or become a hidden controller.

END_OF_FILE: workflow_v3/RUNTIME_MODEL.md
