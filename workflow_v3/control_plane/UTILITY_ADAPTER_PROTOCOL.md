# Utility Adapter Protocol

status: active_control_plane

## Authority

This file is the authoritative Workflow v3 protocol for procedure classes, utility categories, embedded adapter use, RUN external handoff/return, and the boundary between mid-RUN external work and FINISH / Next Move closure.

This protocol keeps the Procedure Registry as the single START routing source. It does not create a second router or a procedure call graph.

## Procedure classes

Allowed `procedure_class` values:

- `core_material` - owns a material workflow task selected by START and executed through RUN.
- `utility_adapter` - prepares bounded supporting packets or external-surface handoffs. It may be selected standalone only when the user's primary request is the utility artifact.
- `verification_adapter` - verifies returned evidence. It may be selected standalone only when the user's primary request is verification.
- `storage_adapter` - mutates allowed repository/runtime state only from an admitted storage update package. Storage execution is never embedded inside another procedure.
- `readonly_console` - reads or summarizes bounded state/context without material execution or mutation.

## Owner procedure rule

START selects exactly one owner procedure for a material chat.

During RUN, the selected owner procedure remains fixed. Embedded utility/adapter use does not change `selected_entrypoint`, does not change `selected_procedure_ref`, and does not authorize a second START.

A core/material procedure does not call another procedure. It may emit typed utility packets or use embedded adapter checks only when its selected procedure source and matching run surface allow the relevant utility category.

## Utility categories

Allowed `utility_category` values:

- `codex_handoff_packet` - complete copy-paste package for a bounded Codex run.
- `codex_return_verification` - verification of the returned result for a Codex handoff emitted by the same owner procedure or by an explicitly supplied handoff.
- `check_job_packet` - bounded source/evidence/consistency/validation question for a check surface.
- `child_chat_packet` - bounded child-chat package for delegated supporting work.
- `child_research_packet` - bounded child research package with questions, evidence plan, and source policy.
- `storage_update_package` - package for later storage execution after acceptance/update authority is clear; it is not embedded storage execution.
- `project_refresh_instruction_packet` - reporting instruction for Project UI or Project Files refresh; it does not perform refresh.

## Standalone utility selection

A utility or verification adapter may be selected directly by START only when the user request is primarily to prepare or verify that adapter artifact.

Examples:

- use `codex_handoff` directly when the selected work is only to package bounded Codex work;
- use `codex_result_verification` directly when the selected work is only to verify a returned Codex result.

Standalone selection still obeys START -> RUN -> FINISH and must not mutate, accept, or launch another material step unless the selected run surface explicitly allows that operation.

## Embedded utility use

Embedded utility use is internal to RUN of the selected owner procedure.

Embedded utility use is allowed only when all are true:

1. the selected procedure source allows the utility category;
2. the matching run surface contract allows the utility category;
3. the utility packet is bounded and complete;
4. no state mutation, acceptance, or procedure switch is implied;
5. external return expectations are explicit when the owner procedure needs the result before completion.

Embedded utility use is represented as a typed intermediate output, not as a new procedure selection.

## RUN_EXTERNAL_HANDOFF

Use `RUN_EXTERNAL_HANDOFF` when the selected owner procedure requires an external utility result before it can complete RUN.

`RUN_EXTERNAL_HANDOFF` is an internal RUN gate. It is not FINISH_REQUEST, not FINISH, not Next Move Packet closure, and not procedure switching.

Required shape:

```text
RUN_EXTERNAL_HANDOFF:
  lifecycle_state: RUN_WAITING_FOR_EXTERNAL_RETURN
  owner_entrypoint:
  owner_procedure_ref:
  utility_category:
  external_surface:
  handoff_purpose:
  copy_paste_packet:
  expected_return_packet:
  validation_required_before_resume:
  resume_rule:
```

`resume_rule` must state that the same selected owner procedure resumes after the user returns external results.

While a required `RUN_EXTERNAL_HANDOFF` is pending, RUN must not emit FINISH_REQUEST.

## RUN_EXTERNAL_RETURN

Use `RUN_EXTERNAL_RETURN` when the user returns evidence from a prior `RUN_EXTERNAL_HANDOFF`.

Required checks:

- match the return to the pending owner procedure and utility category;
- classify the return as adapter evidence, not accepted state;
- verify required branch, commit, changed files, diff, validation, EOF, push, and residual-risk evidence where applicable;
- continue the same selected owner procedure only after required verification passes or returns a typed blocked/failed result.

External tools and Codex must return evidence. They must not perform ChatGPT lifecycle FINISH or decide acceptance.

## Embedded verification

`codex_return_verification` may be embedded when the same owner procedure emitted the Codex handoff and the user returns the corresponding result.

Embedded verification uses the verification adapter's schema and quality checks as a RUN gate. It does not select `codex_result_verification` as a new owner procedure.

If the original handoff is missing, the return does not match, or required evidence is absent, return a typed blocked result or request exact missing evidence. Do not guess from summaries.

## Storage boundary

Storage execution is never embedded inside another owner procedure.

A selected owner procedure may emit a `storage_update_package` only as candidate next-surface output after acceptance/update authority is clear. Actual storage mutation requires a separate admitted `storage_adapter` run with exact allowed files and validation.

## FINISH and Next Move boundary

FINISH_REQUEST may be emitted only after required external handoffs have returned, been verified, or been explicitly abandoned as blocked/stopped.

Next Move Packet is for closure after the selected procedure completes or stops. It is not the mid-RUN external handoff mechanism.

Do not use `human_decision` to avoid producing a required transfer packet when the next external surface is materially known and the selected procedure is responsible for producing the packet.

After FINISH, the chat is closed for material work. A new material START in the same chat is forbidden. Post-FINISH responses may explain the closed result or point to emitted packets; they must not begin a new material lifecycle.

## Eval lenses

A valid execution must preserve these invariants:

- one owner procedure selected by START;
- no procedure switch during RUN;
- embedded utility packets are typed, bounded, and allowed;
- required external returns are resolved before FINISH_REQUEST;
- returned external evidence is verified before reliance;
- no unadmitted mutation, acceptance, or launch;
- no material START after FINISH in the same chat.

END_OF_FILE: workflow_v3/control_plane/UTILITY_ADAPTER_PROTOCOL.md
