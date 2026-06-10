# Support Dependency Protocol

status: active_control_plane

## Authority

This file governs the `support_dependency` packet shape used by a selected Workflow v3 main procedure during RUN.

It does not choose the main procedure, choose the dependency type, decide execution surface, create a second router, or allow an execution surface to become the selected main procedure. Dependency type selection and wrong-surface behavior live in `workflow_v3/control_plane/ROUTING_AND_DEPENDENCY_PROTOCOL.md`.

## Purpose

A support dependency helps the selected main procedure complete a bounded non-mutating check, research, analysis, evidence, or human decision need.

Support dependency output is evidence only. It is not accepted state, persistence, parent completion, ChatGPT CHECK, ChatGPT FINISH, or a repository/code mutation route.

`DEPENDENCY_CALL` and `DEPENDENCY_RETURN` are the only supported support-dependency packet labels. Prior packet labels are unsupported and must be rejected or rewritten before use.

## Support Dependency Rule

A selected main procedure may use a support dependency only when all are true:

- the selected main procedure or current stage needs the support result to complete;
- the dependency boundary is visible to the user;
- the call is bounded by exact task, scope, expected return, and verification;
- any external user action receives a complete copy-paste packet;
- the return resumes the same selected main procedure;
- returned evidence is verified before reliance;
- the execution surface does not mutate repository state, runtime state, Project UI, Project Files/Sources, or accepted state.

If required support dependency work is needed to satisfy the current START goal, the parent opens a visible `DEPENDENCY_CALL`, records it in `open_dependencies`, enters `RUN_WAITING_FOR_DEPENDENCY_RETURN`, and waits for matching `DEPENDENCY_RETURN`.

## DEPENDENCY_CALL

Use `DEPENDENCY_CALL` with `dependency_type: support_dependency` when non-mutating support work must leave the current chat, use a provider, ask a real human decision, or wait for external evidence.

Required shape:

```text
DEPENDENCY_CALL:
  dependency_id:
  dependency_type: support_dependency
  selected_entrypoint:
  selected_procedure_path:
  why_needed:
  support_surface:
  packet_or_call_boundary:
  expected_return:
  verification_required_on_return:
  same_main_procedure_resume:
  unresolved_until_returned:
```

When external user action is required, `packet_or_call_boundary` must contain complete copy-paste content. Placeholders are invalid.

## DEPENDENCY_RETURN

Use `DEPENDENCY_RETURN` when evidence or output comes back from a previous support dependency.

Required shape:

```text
DEPENDENCY_RETURN:
  dependency_id:
  dependency_type: support_dependency
  selected_entrypoint:
  selected_procedure_path:
  returned_artifacts:
  verification_result:
  evidence_status:
  gaps_or_blockers:
  resume_decision:
```

Required checks:

- match the return to the emitted dependency call;
- confirm the same selected main procedure resumes;
- classify the return as evidence, not accepted state;
- verify required source, decision, consistency, or validation evidence where applicable;
- rely on the return only after verification passes or a blocked result is explicit.

## Repository and Storage Boundary

Code/repository mutation, patching, branch creation, commits, pushes, file writes, implementation, write probes, and repository-side validation requiring writes are not support dependencies. They are `code_repository_dependency` and route only to Codex/code assistant under `CODEX_HANDOFF_PROCEDURE.md` and `CODEX_RESULT_VERIFICATION_PROCEDURE.md`.

GitHub or file access from the ChatGPT parent is read or verification only unless a separately admitted write executor returns verifiable write evidence. It must not be named as a ChatGPT parent write surface.

Direct in-chat persistence is allowed only when the selected main procedure is `storage_update` and the package includes authority, exact paths, exact changes, validation, and verification. External repository writes still require an admitted write executor and verified return unless a storage authority separately and explicitly admits them.

## Finish Boundary

CHECK and FINISH must not rely on unresolved dependency returns. If a required dependency return is missing or unverified, return to RUN repair or blocked escalation. `open_dependencies != empty`, `missing_dependency_return`, `unverified_dependency_return`, or missing required validation/evidence blocks CHECK, FINISH, and CLOSED.

A handoff, package, Codex package, check packet, dependency packet, storage packet, copy-paste packet, or dependency envelope is never parent lifecycle completion. These are technical forms of dependency call or dependency evidence until verified by the parent RUN.

NEXT_CHAT_CARD is post-closed continuation only. It is not a dependency call, not a support dependency launch, and not evidence that the current START goal has completed. It must not carry unfinished dependency work from the current START goal.

## Forbidden Patterns

- switching the selected main procedure during RUN;
- hiding a dependency launch behind a summary;
- treating dependency return as accepted state;
- relying on unverified returned evidence;
- asking an external dependency surface to perform ChatGPT FINISH;
- using a human decision placeholder to avoid a known required packet;
- performing writes through a support dependency;
- treating GitHub or file access as a ChatGPT parent write surface;
- finding required current-goal dependency repair but continuing to later stages, CHECK, FINISH, or CLOSED without opening and verifying the dependency call;
- closing while a required dependency return is unresolved.

END_OF_FILE: workflow_v3/control_plane/SUPPORT_DEPENDENCY_PROTOCOL.md
