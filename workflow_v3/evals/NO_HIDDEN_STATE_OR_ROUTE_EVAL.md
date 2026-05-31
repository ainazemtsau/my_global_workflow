# No Hidden State or Route Eval

status: active_repository_completion_framework

## Source files to inspect

- `workflow_v3/RUNTIME_MODEL.md`
- `workflow_v3/QUALITY_AND_RECOVERY.md`
- `workflow_v3/SIGNALS_HANDLERS_ACTION_INBOX.md`
- `workflow_v3/interfaces/**`
- relevant Result Packets, Event Loop Closures, Acceptance Decisions, and Project setup reports

## Evidence required

- exact source authority;
- candidate versus accepted classification;
- Event Loop Closure;
- Progression Router Result;
- Acceptance Decision when state changes;
- Project setup refresh classification when setup surfaces are touched.

## PASS criteria

- Accepted state lives only in canonical storage and accepted records.
- Result Packet, Evidence, Signal, Handler Result, Action Inbox item, Check Job, Codex output, and Project Files/Sources remain candidate/context until accepted.
- Event Loop Closure and Progression Router select the next move visibly.
- Repository commit is not treated as actual ChatGPT Project update.

## WARN criteria

- Candidate context is useful but clearly labeled and not used as authority.
- Next Move is candidate transport and not accepted state.

## FAIL criteria

- Chat intuition route replaces Signal/Handler/Closure/Router.
- Result Packet treated as accepted state.
- Evidence treated as acceptance.
- Acceptance Decision treated as Codex commit or vice versa.
- Codex commit treated as done.
- Project Files/Sources treated as authority.
- Repository commit treated as actual Project UI update.
- Runtime Console acts as hidden controller.

## Common failure modes

- "The chat decided" becomes route authority.
- "The file exists" becomes acceptance.
- "The pack was generated/uploaded" becomes source authority.

## Required recovery/repair action

Block the route/state claim, rerun Event Loop Closure, create or request the missing Acceptance Decision/update path, and re-verify source authority before continuing.

END_OF_FILE: workflow_v3/evals/NO_HIDDEN_STATE_OR_ROUTE_EVAL.md
