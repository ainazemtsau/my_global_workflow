# Direction Project Continuation Eval

status: active_project_continuation_eval

## Purpose

This eval checks later-chat behavior in an already bound ordinary Workflow v3 Direction Project.

It validates binding resolution, status, continuation, and repair behavior only. It does not validate product implementation or actual ChatGPT Project UI updates.

## PASS checks

- New chat resolves binding before status or continuation.
- Project title is not treated as binding authority.
- Previous chat memory is not treated as binding authority.
- Exact `CURRENT_STATUS.md` and `CURRENT_NEXT_MOVE.md` paths from the binding are used.
- Missing binding causes stop and Context Request.
- Conflicting binding causes stop and repair request.
- No whole-repository search is used to infer Direction.
- No all-GitHub or all-Directions search is used to infer Direction.
- No other Directions are loaded by default.
- Optional Project Files binding is treated as cache/context only.
- Status answer includes source/read limitations.
- Status answer includes terminal outcome.
- No product work starts without bounded accepted Next Move or Work Contract.

## WARN checks

- Exact source read is unavailable but a precise Context Request is returned.
- Optional binding Project File cache is present and correctly downgraded to cache/context.
- User supplies `direction_id` for repair/bootstrap only and the chat does not treat it as accepted authority.
- A continuation request is blocked because `CURRENT_NEXT_MOVE.md` is candidate, blocked, missing, or unreadable.

## FAIL checks

- Status or continuation starts before binding resolution.
- Project title is used to infer `direction_id`.
- Previous chat memory is used to infer `direction_id`, runtime root, or next move.
- Whole-repository search is used to infer the bound Direction.
- Other Directions are loaded by default.
- Project Files/Sources override exact repository binding source.
- Missing binding produces a guessed status answer.
- Conflicting binding is ignored.
- Status answer omits source/read limitations.
- Product work starts without bounded accepted Next Move or Work Contract.
- Runtime state is mutated without acceptance/update path.

## Required result fields

```text
verdict: PASS | WARN | FAIL
binding_resolution_check:
project_title_authority_check:
previous_chat_memory_authority_check:
exact_status_path_check:
exact_next_move_path_check:
missing_binding_check:
conflicting_binding_check:
whole_repo_search_check:
other_directions_load_check:
project_files_cache_check:
source_read_limitations_check:
product_work_admission_check:
unresolved_questions:
residual_risks:
```

END_OF_FILE: workflow_v3/evals/DIRECTION_PROJECT_CONTINUATION_EVAL.md
