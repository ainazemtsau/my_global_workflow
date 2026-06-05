# Utility Adapter Protocol

status: active_control_plane

## Authority

This file governs provider-neutral utility calls made by a selected Workflow v3 main procedure during RUN.

It does not choose the main procedure. It does not create a second router. It does not allow a utility to become the selected main procedure unless START selected that utility entrypoint as the user's primary request.

## Purpose

A utility call helps the selected main procedure complete a stage or verification need. Utility return is evidence, not accepted state by itself.

## Utility Surfaces

Utility surfaces may include:

- Codex;
- Claude Code or future code assistants;
- child chat;
- check job;
- research agent;
- GitHub or file access;
- storage update;
- human decision;
- future admitted providers.

Codex is one possible utility surface, not the default or only path.

## Utility Call Rule

A selected main procedure may use a utility only when all are true:

- the selected main procedure or current stage needs the utility to complete;
- the utility boundary is visible to the user;
- the call is bounded by exact task, scope, expected return, and verification;
- any external user action receives a complete copy-paste packet;
- the return resumes the same selected main procedure;
- returned evidence is verified before reliance;
- the utility does not mutate state unless an admitted write path, exact paths, validation, and return evidence are present.

## UTILITY_CALL

Use `UTILITY_CALL` when supporting work must leave the current chat, use a tool/provider, ask a human, or wait for external evidence.

Required shape:

```text
UTILITY_CALL:
  utility_call_id:
  selected_entrypoint:
  selected_procedure_path:
  why_needed:
  target_utility_or_surface:
  packet_or_call_boundary:
  expected_return:
  verification_required_on_return:
  same_main_procedure_resume:
  unresolved_until_returned:
```

When external user action is required, `packet_or_call_boundary` must contain complete copy-paste content. Placeholders are invalid.

## UTILITY_RETURN

Use `UTILITY_RETURN` when evidence or output comes back from a previous `UTILITY_CALL`.

Required shape:

```text
UTILITY_RETURN:
  utility_call_id:
  selected_entrypoint:
  selected_procedure_path:
  returned_artifacts:
  verification_result:
  evidence_status:
  gaps_or_blockers:
  resume_decision:
```

Required checks:

- match the return to the emitted utility call;
- confirm the same selected main procedure resumes;
- classify the return as evidence, not accepted state;
- verify required branch, commit, changed files, validation, EOF, source, or decision evidence where applicable;
- rely on the return only after verification passes or a blocked result is explicit.

## Storage Boundary

Direct in-chat mutation is allowed only when the selected main procedure is a storage_update and the package includes authority, exact paths, exact changes, validation, and verification.

A core procedure may use an external storage or code utility only through a visible `UTILITY_CALL` with exact write boundaries and verified `UTILITY_RETURN`. If write authority, path boundaries, or validation are absent, return a blocked result or a candidate package instead of writing.

## Finish Boundary

CHECK and FINISH must not rely on unresolved utility returns. If a required utility return is missing or unverified, return to RUN repair or blocked escalation.

A closure continuation uses `NEXT_CHAT_CARD` or a complete Transfer Packet; it is not a hidden utility launch.

## Forbidden Patterns

- switching the selected main procedure during RUN;
- hiding a utility launch behind a summary;
- treating utility return as accepted state;
- relying on unverified returned evidence;
- asking an external utility to perform ChatGPT FINISH;
- using a human decision placeholder to avoid a known required packet;
- performing writes without exact authority, paths, validation, and return evidence;
- closing while a required utility return is unresolved.

END_OF_FILE: workflow_v3/control_plane/UTILITY_ADAPTER_PROTOCOL.md