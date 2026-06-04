# No Hidden State or Route Eval

status: active_repository_completion_framework

## Purpose

Validate that Workflow v3 state, procedure selection, and next movement are explicit.

## Sources to inspect

- `workflow_v3/RUNTIME_MODEL.md`
- `workflow_v3/interfaces/**`
- relevant FINISH_PACKET, Result Packets, Next Move Packets, Acceptance Decisions, and Project setup reports

## Evidence required

- exact source authority;
- candidate versus accepted classification;
- FINISH_PACKET;
- Result Packet;
- Next Move Packet;
- Acceptance Decision when state changes;
- Project setup refresh classification when setup surfaces are touched.

## PASS criteria

- Accepted state lives only in canonical storage and accepted records.
- Result Packet, Evidence, Next Move Packet, Transfer Packet, Check Job, Codex output, and Project Files/Sources remain candidate/context until accepted.
- FINISH selects the next move visibly.
- Repository commit is not treated as actual ChatGPT Project update.

## WARN criteria

- Candidate content is useful but not accepted.
- Project setup refresh is needed but not performed.
- Exact source read limitation is named.

## FAIL criteria

- Chat intuition route replaces procedure registry and FINISH closure.
- Result Packet treated as accepted state.
- Evidence treated as acceptance.
- Project Files/Sources cache treated as source authority.
- Codex commit treated as Direction acceptance.
- Project Instructions source commit treated as actual UI update.
- More than one primary next move is launched.

## Required recovery/repair action

Block the route/state claim, produce or repair FINISH_PACKET and Next Move Packet, create or request the missing Acceptance Decision/update path, and re-verify source authority before continuing.

END_OF_FILE: workflow_v3/evals/NO_HIDDEN_STATE_OR_ROUTE_EVAL.md
