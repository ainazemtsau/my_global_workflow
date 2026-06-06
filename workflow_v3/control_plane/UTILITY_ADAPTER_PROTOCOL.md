# Utility Adapter Protocol

status: active_control_plane

## Authority

This file governs provider-neutral child procedure calls and adapter aliases made by a selected Workflow v3 main procedure during RUN.

It does not choose the main procedure. It does not create a second router. It does not allow a child/adaptor to become the selected main procedure.

## Purpose

A child procedure call helps the selected main procedure complete a stage, verification need, external mutation, research/check need, or human decision need. Child return is evidence, not accepted state by itself.

`CHILD_PROCEDURE_CALL` and `CHILD_PROCEDURE_RETURN` are the canonical lifecycle terms. Existing `UTILITY_CALL` and `UTILITY_RETURN` labels may be retained only as compatibility names for adapter-level packets.

## Child / Adapter Surfaces

Child/adaptor surfaces may include:

- Codex;
- Claude Code or future code assistants;
- child chat;
- check job;
- research agent;
- GitHub or file access;
- storage update;
- human decision;
- future admitted providers.

Codex is one possible child/adaptor surface, not the default or only path.

## Child Call Rule

A selected main procedure may use a child/adaptor only when all are true:

- the selected main procedure or current stage needs the child/adaptor to complete;
- the child/adaptor boundary is visible to the user;
- the call is bounded by exact task, scope, expected return, and verification;
- any external user action receives a complete copy-paste packet;
- the return resumes the same selected main procedure;
- returned evidence is verified before reliance;
- the child/adaptor does not mutate state unless an admitted write path, exact paths, validation, and return evidence are present.

## CHILD_PROCEDURE_CALL

Use `CHILD_PROCEDURE_CALL` when supporting work must leave the current chat, use a tool/provider, ask a human, or wait for external evidence.

Required shape:

```text
CHILD_PROCEDURE_CALL:
  child_call_id:
  selected_entrypoint:
  selected_procedure_path:
  why_needed:
  target_child_or_adapter:
  packet_or_call_boundary:
  expected_return:
  verification_required_on_return:
  same_main_procedure_resume:
  unresolved_until_returned:
```

When external user action is required, `packet_or_call_boundary` must contain complete copy-paste content. Placeholders are invalid.

Adapter compatibility alias:

```text
UTILITY_CALL:
  compatibility_for: CHILD_PROCEDURE_CALL
```

## CHILD_PROCEDURE_RETURN

Use `CHILD_PROCEDURE_RETURN` when evidence or output comes back from a previous `CHILD_PROCEDURE_CALL`.

Required shape:

```text
CHILD_PROCEDURE_RETURN:
  child_call_id:
  selected_entrypoint:
  selected_procedure_path:
  returned_artifacts:
  verification_result:
  evidence_status:
  gaps_or_blockers:
  resume_decision:
```

Required checks:

- match the return to the emitted child call;
- confirm the same selected main procedure resumes;
- classify the return as evidence, not accepted state;
- verify required branch, commit, changed files, validation, EOF, source, or decision evidence where applicable;
- rely on the return only after verification passes or a blocked result is explicit.

Adapter compatibility alias:

```text
UTILITY_RETURN:
  compatibility_for: CHILD_PROCEDURE_RETURN
```

## Storage Boundary

Direct in-chat mutation is allowed only when the selected main procedure is a storage_update and the package includes authority, exact paths, exact changes, validation, and verification.

A core procedure may use an external storage or code child/adaptor only through a visible `CHILD_PROCEDURE_CALL` with exact write boundaries and verified `CHILD_PROCEDURE_RETURN`. If write authority, path boundaries, or validation are absent, return a blocked result or a candidate child-call packet instead of writing.

## Finish Boundary

CHECK and FINISH must not rely on unresolved child returns. If a required child return is missing or unverified, return to RUN repair or blocked escalation. `open_child_calls != empty`, `missing_child_return`, `unverified_child_return`, or missing required validation/evidence blocks CHECK, FINISH, and CLOSED.

A handoff, package, Codex package, check packet, child-chat card, storage packet, copy-paste packet, or child-call envelope is never parent lifecycle completion. These are technical forms of `CHILD_PROCEDURE_CALL` or child evidence until verified by the parent RUN.

NEXT_CHAT_CARD is post-closed continuation only. It is not a child call, not a utility launch, and not evidence that the current START goal has completed. It must not carry unfinished child work from the current START goal.

## Forbidden Patterns

- switching the selected main procedure during RUN;
- hiding a child/adaptor launch behind a summary;
- treating child return as accepted state;
- relying on unverified returned evidence;
- asking an external utility to perform ChatGPT FINISH;
- using a human decision placeholder to avoid a known required packet;
- performing writes without exact authority, paths, validation, and return evidence;
- closing while a required child return is unresolved.

END_OF_FILE: workflow_v3/control_plane/UTILITY_ADAPTER_PROTOCOL.md
