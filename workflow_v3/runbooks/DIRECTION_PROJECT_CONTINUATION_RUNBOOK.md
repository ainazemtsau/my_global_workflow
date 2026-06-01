# Direction Project Continuation Runbook

status: active_project_continuation_runbook

## Purpose

This runbook defines how any new chat in an already bound ordinary Workflow v3 Direction Project resolves binding, answers status, and continues from accepted next move.

It does not create a runtime root, update Project Instructions UI, refresh Project Files/Sources, or execute product work by itself.

## Trigger

Use this runbook for any new chat in an already bound ordinary Direction Project, including vague requests such as:

- `какой статус проекта?`
- `what is the project status?`
- `продолжи`
- `continue`

## Initial action: resolve Project Binding

1. Read the Project Instructions UI binding capsule visible to the chat.
2. Identify `direction_id`, `runtime_root`, `current_status_path`, `current_next_move_path`, `project_binding_source_path`, `project_setup_source_path`, and `project_files_manifest_path`.
3. Treat the capsule as a locator, not final proof.
4. Verify exact repository source when material status, continuation, or state mutation depends on current state.

## If binding exists

Read or request exact repository source for:

```text
current_status_path
current_next_move_path
```

Use the bound Direction runtime root only.

Do not read other Directions by default.

Do not use Project title, prior chat memory, stale Project Files/Sources, or optional binding cache as binding authority.

## If binding is missing

Stop and return a Context Request.

Ask for one of:

- `direction_id` for repair/bootstrap only; or
- a binding repair/bootstrap packet naming exact repo/path/ref; or
- exact canonical binding path/ref.

Do not answer status or continue work.

## If binding conflicts

Stop and return a binding repair request.

Report:

- conflicting fields;
- sources that conflict;
- exact source needed to resolve;
- why Project title, previous chat memory, and Project Files/Sources cannot decide the conflict.

Do not continue until repaired.

## Missing GitHub access

If exact repository source cannot be read:

- stop;
- request the exact repo/path/ref for the binding, `CURRENT_STATUS.md`, or `CURRENT_NEXT_MOVE.md`;
- state that cache/context is not enough to continue.

## Status request flow

For `какой статус проекта?` or equivalent:

1. Resolve binding.
2. Read exact `current_status_path` or ask Context Request.
3. Read exact `current_next_move_path` or ask Context Request.
4. Summarize status from `CURRENT_STATUS.md`.
5. Report exact next move from `CURRENT_NEXT_MOVE.md`.
6. Include source/read limitations.
7. Include terminal outcome: answered, Context Request, binding repair required, or blocked.

## Continuation flow

For `продолжи` or equivalent:

1. Resolve binding.
2. Read exact `CURRENT_NEXT_MOVE.md`.
3. Confirm the next move is accepted, not candidate or blocked.
4. If it names a bounded Work Contract or Launch Packet, continue only within that boundary.
5. If no bounded next move exists, stop and request one.
6. Do not start product work unless the current next move admits it.

## No whole-repo search

Do not search the whole repository, all GitHub, or all Directions to infer binding.

Whole-repository search is not a continuation strategy for an ordinary bound Direction Project.

## No other Directions by default

Load only the bound Direction runtime root paths by default.

Other Directions require an explicit bounded request, accepted relation, Check Job, or named source path.

## Closure and terminal outcome

Every status/continuation/repair run returns:

```text
result:
binding_status:
direction_id:
sources_read:
source_read_limitations:
status_summary:
exact_next_move:
not_done:
unresolved_questions:
residual_risks:
terminal_outcome: answered | context_request | binding_repair_required | blocked
```

Material continuation also requires Event Loop Closure and a Result Packet.

END_OF_FILE: workflow_v3/runbooks/DIRECTION_PROJECT_CONTINUATION_RUNBOOK.md
