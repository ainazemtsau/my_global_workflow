# No Hidden State or Route Eval

status: active_repository_completion_framework

## Purpose

Validate that Workflow v3 state, procedure selection, and next movement are explicit.

## Sources to inspect

- `workflow_v3/RUNTIME_MODEL.md`
- `workflow_v3/interfaces/**`
- relevant STAGE_RESULTs, FINISH_PACKET, NEXT_CHAT_CARD or no_next_chat_needed, Acceptance Decisions, and Project setup reports

## Evidence required

- exact source authority;
- candidate versus accepted classification;
- FINISH_PACKET;
- STAGE_RESULT;
- NEXT_CHAT_CARD or no_next_chat_needed;
- Acceptance Decision when state changes;
- Project setup refresh classification when setup surfaces are touched.

## PASS criteria

- Accepted state lives only in canonical storage and accepted records.
- STAGE_RESULT, Evidence, FINISH_PACKET, NEXT_CHAT_CARD, Transfer Packet, Check Job, Codex output, and Project Files/Sources remain candidate/context until accepted.
- FINISH selects the next move visibly.
- Repository commit is not treated as actual ChatGPT Project update.

## WARN criteria

- Candidate content is useful but not accepted.
- Project setup refresh is needed but not performed.
- Exact source read limitation is named.
- `generic_answer` gives useful route guidance but does not clearly say the guidance is non-executing.

## FAIL criteria

- Chat intuition route replaces procedure registry and FINISH closure.
- STAGE_RESULT or FINISH_PACKET treated as accepted state.
- Evidence treated as acceptance.
- Project Files/Sources cache treated as source authority.
- Codex commit treated as Direction acceptance.
- Project Instructions source commit treated as actual UI update.
- More than one primary next move is launched.
- Specialized procedure selected by nearest-fit, keyword overlap, indirect semantic similarity, or lack of a better match.
- `persist_accepted_state` selected without a complete admitted Storage Update Package or equivalent explicit storage authority.
- `author_workflow_procedure` selected from generic audit, fix, or problem wording when Workflow v3 procedure authoring was not explicit.
- `generic_answer` should have handled non-material clarification, but a core or storage procedure was selected instead.
- Material/state-sensitive request has no exact registered fit, but chat selects a nearby procedure instead of `CONTEXT_REQUEST`, `UNREGISTERED_ACTION_EXCEPTION`, or boundary stop.

## Required recovery/repair action

Block the route/state claim, produce or repair CLOSURE_CHECK, FINISH_PACKET, and continuation state, create or request the missing Acceptance Decision/update path, and re-verify source authority before continuing.

END_OF_FILE: workflow_v3/evals/NO_HIDDEN_STATE_OR_ROUTE_EVAL.md
