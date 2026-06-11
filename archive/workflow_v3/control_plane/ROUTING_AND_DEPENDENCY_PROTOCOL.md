# Routing and Dependency Protocol

status: active_control_plane

## Purpose

This protocol owns deterministic routing and dependency decisions after request classification and during RUN when the selected owner cannot proceed with same-chat work only.

It does not select registry entrypoints by itself. It does not execute work, mutate repository or runtime state, or replace lifecycle or selected-procedure completion.

## Authority

- `PROCEDURE_REGISTRY.md` owns owner procedure selection.
- `CHAT_LIFECYCLE_PROTOCOL.md` owns the START/RUN/CHECK/FINISH/CLOSED state machine and hard gates.
- `ROUTING_AND_DEPENDENCY_PROTOCOL.md` owns dependency type selection and wrong-surface handling.
- `CODE_REPOSITORY_DEPENDENCY_PROCEDURE.md` owns code repository dependency packet schema.
- `CODE_REPOSITORY_DEPENDENCY_RETURN_VERIFICATION_PROCEDURE.md` owns code repository dependency return verification.
- `CURRENT_NEXT_MOVE_FORMATION_PROCEDURE.md` owns post-closed `NEXT_CHAT_CARD` continuation.

## Core Rule

One material chat has one selected owner procedure. The execution or dependency surface is separate from that owner procedure.

External work needed before the current goal can complete opens one typed dependency and blocks the parent RUN until the matching return is verified or the result is explicitly blocked. New independent work after closure uses `NEXT_CHAT_CARD` only.

## Dependency Types

### `support_dependency`

Non-mutating check, research, analysis, evidence gathering, or bounded human decision support.

It must not mutate repository or runtime state, accept output, persist state, or close the parent lifecycle.

### `code_repository_dependency`

Repository or code mutation, patching, branch creation, commits, pushes, implementation work, file writes, write probes, and repository-side validation requiring writes.

Execution surface: Codex/code assistant only.

The ChatGPT parent may draft the dependency packet and verify the returned evidence only. The ChatGPT parent must not write, probe writes, create branches, commit, push, apply patches, or execute repository mutation.

### `core_lifecycle_dependency`

A separate registered core procedure lifecycle blocks the current RUN.

The parent does not switch procedures. The target chat runs its own START/RUN/CHECK/FINISH. The parent resumes only after the target returns a verified FINISH or blocked result.

### `storage_persistence_dependency`

Accepted-state persistence or update authority.

`storage_update` validates and authorizes package boundaries. Repository writes still require an admitted write executor and verified return unless separately and explicitly admitted by the storage procedure.

### `human_decision_dependency`

A real human choice needed before the selected owner can continue.

It is not a placeholder to avoid a known packet, dependency type, storage package, or code-repository dependency.

## Routing Decision Ladder

1. Classify the request and split independent material work before RUN when needed.
2. Select the owner via `PROCEDURE_REGISTRY.md` when the request is material or state-sensitive.
3. Execute same-chat non-mutating work when the selected owner and lifecycle allow it.
4. If work must leave the same-chat boundary, choose exactly one dependency type.
5. If the work items are ambiguous or multiple independent dependency items are bundled, return `SPLIT_REQUIRED` or an explicit blocked result.
6. If a code/repository mutation packet is pasted into ChatGPT for execution, return `wrong_execution_surface` and instruct the operator to run it in Codex/code assistant.

## Packet Shapes

Canonical dependency call shape:

```text
DEPENDENCY_CALL:
  dependency_id:
  dependency_type:
  selected_entrypoint:
  selected_procedure_path:
  why_needed:
  execution_surface:
  packet_or_call_boundary:
  expected_return:
  verification_required_on_return:
  same_main_procedure_resume:
  unresolved_until_returned: true
```

Canonical dependency return shape:

```text
DEPENDENCY_RETURN:
  dependency_id:
  dependency_type:
  selected_entrypoint:
  selected_procedure_path:
  returned_artifacts:
  verification_result:
  evidence_status:
  gaps_or_blockers:
  resume_decision:
```

Prior dependency packet labels are unsupported. A packet that uses a prior packet label must be rejected or rewritten to the canonical dependency shape before the parent RUN can rely on it.

## Waiting State

Canonical lifecycle terms:

- `RUN_WAITING_FOR_DEPENDENCY_RETURN`;
- `DEPENDENCY_RETURN_VERIFICATION`;
- `open_dependencies`;
- `missing_dependency_return`;
- `unverified_dependency_return`.

Prior waiting-state labels are unsupported. Active RUN state uses the canonical dependency fields above.

## Wrong-Surface Behavior

ChatGPT must not execute code/repository mutation packets. When a code/repository mutation packet is presented to ChatGPT as executable work, ChatGPT returns `wrong_execution_surface` and instructs the operator to run the packet in Codex/code assistant.

Codex/code assistant must not perform ChatGPT CHECK, FINISH, CLOSED, acceptance, or Project UI updates.

`NEXT_CHAT_CARD` must not carry unfinished current-goal dependency work. It is post-closed continuation only.

## Closure Blockers

CHECK, FINISH, and CLOSED are blocked by:

- open dependency return;
- missing dependency return;
- unverified dependency return;
- missing validation or evidence;
- packet-only, handoff-only, card-only, or dependency-envelope-only result;
- hidden write, hidden launch, hidden acceptance, or hidden procedure switch;
- code/repository mutation attempted on the ChatGPT parent surface.

END_OF_FILE: workflow_v3/control_plane/ROUTING_AND_DEPENDENCY_PROTOCOL.md
