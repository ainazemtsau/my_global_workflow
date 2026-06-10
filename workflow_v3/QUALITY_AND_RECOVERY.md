# Workflow v3 Quality and Recovery

status: active_repository_completion_framework

## Purpose

This file defines quality gates and recovery actions for Workflow v3 repository packages and future Direction runtime work.

No validation means no done claim.

Chat output, Codex output, Project Files/Sources, STAGE_RESULTs, FINISH_PACKETs, NEXT_CHAT_CARDs, Transfer Packets, Check Jobs, dependency returns, and document existence do not create accepted state or parent lifecycle completion by themselves.

## Context/source gate

Checks:

- exact source path/ref is named;
- Project Files/Sources and pasted excerpts are treated as cache/context unless verified;
- source read limitations are named;
- stale or missing source blocks material claims.

Fails when source authority is guessed or stale cache is treated as canonical.

Recovery:

- stop the material claim;
- request or read the exact source;
- rerun the same procedure with source limitations visible.

## Entity coverage gate

Checks:

- each entity has a canonical definition file/interface;
- storage location is identified when applicable;
- related packets/templates, state mutation rights, and acceptance/update requirements are visible where applicable;
- unresolved risks are named instead of hidden.

Fails when a package invents an entity, storage path, or mutation right.

Recovery:

- block the package;
- add or cite the missing interface/template/eval;
- return bounded repair guidance or a NEXT_CHAT_CARD when a new material chat is needed.

## Formation quality gate

Checks:

- Direction Spine, Direction Map, Active Front, Work Graph, Work Contract, Current Next Move, Acceptance Decision, and Memory Artifact promotion use registered procedures before template filling;
- alternatives, criteria, evidence, risks, rejected/deferred options, focus/waste cuts, source limits, acceptance question, STAGE_RESULT, FINISH_PACKET, and continuation state are visible when applicable;
- support research/check dependencies are bounded support only, return to the parent formation chat, and require verified dependency return before reliance;
- candidate and accepted boundaries are preserved.

Fails when formation becomes roadmap drafting, backlog dumping, or hidden acceptance.

Recovery:

- stop formation;
- restate the selected procedure and source boundaries;
- produce a blocked or repair STAGE_RESULT or FINISH_PACKET, depending on lifecycle position.

## Direction lifecycle gate

Checks:

- lifecycle transitions are visible as typed procedure outputs;
- Direction Spine, Direction Map, Active Front, Work Graph, and Work Contract transitions are not selected by chat intuition;
- every state-changing lifecycle transition has CLOSURE_CHECK, FINISH_PACKET, continuation state, and acceptance/update path;
- blocked lifecycle transition stops product work until repaired, accepted, or split.

Fails when lifecycle state changes by implication.

Recovery:

- stop continuation;
- return a human decision request or repair continuation card;
- require explicit acceptance/update before mutation.

## Evidence gate

Checks:

- evidence backs every done or accepted claim;
- validation output is included when validation is required;
- failed validation forces blocked or repair_required status;
- source limitations are not hidden.

Fails when result quality is asserted without evidence.

Recovery:

- block done claim;
- request same-scope repair or verification;
- return a check job or repair continuation card.

## Acceptance gate

Checks:

- candidate result remains candidate until explicit Acceptance Decision/update path;
- dependency output is not self-accepted;
- human approval is separated from storage authorization unless an admitted package grants write scope.

Fails when acceptance is inferred or hidden.

Recovery:

- block mutation;
- request explicit decision or storage package;
- name acceptance boundary in FINISH_PACKET or NEXT_CHAT_CARD.

## Procedure output misuse gate

Checks:

- procedure outputs remain candidate unless accepted;
- Check Job remains bounded verification;
- FINISH_PACKET appears after material work/review when lifecycle FINISH is active;
- no accepted-state mutation occurs from packet output alone.

Fails when packet output executes work, accepts state, or becomes hidden automation.

Recovery:

- block or reject the unsafe result;
- rerun same-scope FINISH closure;
- convert only the selected primary next move into a Transfer Packet, Check Job, repair Next Move, or human decision request.

## Continuation misuse gate

Checks:

- FINISH selects one continuation outcome;
- transfer steps include a complete Transfer Packet or post-closed NEXT_CHAT_CARD;
- Codex/code-assistant calls use `code_repository_dependency` and return to the same current chat for verification and closure;
- next material chat waits until the current material target is completed or explicitly blocked, with required dependency returns verified and any acceptance/persistence boundary preserved;
- unreviewed task lists remain candidate context, not roadmap.

Fails when:

- next step is guessed without FINISH closure;
- multiple next steps are launched silently;
- unreviewed task list becomes roadmap;
- acceptance or persistence is skipped;
- a transfer step only says to create a package instead of providing the complete packet;
- a transfer, handoff, card, package, check packet, storage packet, or copy-paste packet is treated as current-goal completion by itself.

Recovery:

- stop the unsafe continuation;
- repair FINISH_PACKET and continuation state;
- choose one continuation outcome;
- provide a complete Transfer Packet when transfer is needed, or a visible `DEPENDENCY_CALL` when current-goal dependency work is required before closure;
- preserve acceptance/update boundary.

## Parent/Dependency Recovery Gate

Checks:

- dependency result returns to parent;
- parent remains synthesis authority;
- missing or unverified required dependency result blocks synthesis, CHECK, FINISH, and CLOSED;
- Parent Recovery Block is used when multiple dependencies or missing returns create ambiguity.

Fails when dependency output becomes independent execution track or missing dependency result is invented.

Recovery:

- stop parent synthesis;
- request missing dependency result or rerun a narrowed dependency prompt;
- produce Parent Recovery Block;
- rerun FINISH closure after dependency/parent status is clear.

## Codex validation gate

Checks:

- branch/commit/diff is named;
- changed files match allowed paths;
- validation commands and outputs are present;
- EOF markers are checked where repository convention requires them;
- project refresh requirements are separated.

Fails when Codex result is accepted without verification.

Recovery:

- block acceptance;
- request same-scope repair or verification;
- return exact residual risks and next move.

END_OF_FILE: workflow_v3/QUALITY_AND_RECOVERY.md
