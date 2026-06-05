# Utility Adapter Protocol

status: active_control_plane

## Authority

This file is the authoritative Workflow v3 protocol for procedure classes, utility categories, embedded adapter use, RUN external handoff/return, and the boundary between mid-RUN external work and FINISH / Next Move closure.

This protocol keeps the Procedure Registry as the single START routing source. It does not create a second router or a procedure call graph.

## Purpose

This protocol lets one selected owner procedure emit and resume from typed utility/adapter packets during RUN without switching procedures, opening a second material START, or hiding mutation/acceptance behind adapter work.

It defines standalone adapter use, embedded adapter use, RUN_EXTERNAL_HANDOFF, RUN_EXTERNAL_RETURN, embedded verification, and storage boundaries.

## Procedure classes

Allowed `procedure_class` values:

- `core_material` - owns a material workflow task selected by START and executed through RUN.
- `utility_adapter` - prepares bounded supporting packets or external-surface handoffs. It may be selected standalone only when the user's primary request is the utility artifact.
- `verification_adapter` - verifies returned evidence. It may be selected standalone only when the user's primary request is verification.
- `storage_adapter` - mutates allowed repository/runtime state only from an admitted storage update package. Storage execution is never embedded inside another procedure.
- `readonly_console` - reads or summarizes bounded state/context without material execution or mutation.

Allowed `embedded_use_policy` values:

- `may_use_global_utility_layer` - core/material owner may invoke registered utilities through the Utility Use Gate.
- `callable_utility` - utility adapter may be called as a resource or selected standalone when it is the primary work item.
- `callable_verification_utility` - verification adapter may be called as a verification resource or selected standalone when it is the primary work item.
- `callable_persistence_utility_with_write_gate` - storage utility requires admitted storage write gate and exact package.
- `no_material_utility_by_default` - read-only surface does not perform material utility work by default.

## Owner procedure rule

START selects exactly one owner procedure for a material chat.

During RUN, the selected owner procedure remains fixed. Embedded utility/adapter use does not change `selected_entrypoint`, does not change `selected_procedure_ref`, and does not authorize a second START.

A core/material procedure does not call another core/material procedure. Utility procedures are callable resource protocols/functions, not owner procedure switches.

## Global Utility Resource Rule

Any `core_material` owner procedure may invoke any registered `utility_adapter`, `verification_adapter`, storage utility package, or utility child resource needed to complete the current owner work.

Utility invocation stays inside RUN of the same owner procedure. The utility result returns to that same owner RUN as adapter evidence, verification evidence, or a typed blocked result.

Procedure-specific docs may name common utility choices or explicit forbiddances, but absence from a procedure or run-surface prelist does not block global utility access.

## Utility Use Gate

A selected owner procedure may invoke a utility resource only when all are true:

1. START has selected exactly one owner procedure;
2. the utility is registered or otherwise admitted as a bounded utility child resource;
3. the utility is needed to complete the current owner work;
4. source authority, policy, safety, and write boundaries do not forbid it;
5. storage mutation uses the storage write gate and is not hidden inside another owner procedure;
6. the handoff is bounded, has expected return fields, and cannot become an unbounded external wait;
7. the utility result will be integrated, verified, or explicitly blocked before FINISH_REQUEST when required.

Utility use must not become procedure switching, hidden mutation, hidden acceptance, hidden next work, or unbounded external wait.

## Utility categories

Allowed `utility_category` values:

- `codex_handoff_packet` - complete copy-paste package for a bounded Codex run.
- `codex_return_verification` - verification of the returned result for a Codex handoff emitted by the same owner procedure or by an explicitly supplied handoff.
- `check_job_packet` - bounded source/evidence/consistency/validation question for a check surface.
- `child_chat_packet` - bounded child-chat package for delegated supporting work.
- `child_research_packet` - bounded child research package with questions, evidence plan, and source policy.
- `storage_update_package` - package for later storage execution after acceptance/update authority is clear; it is not embedded storage execution.
- `project_refresh_instruction_packet` - reporting instruction for Project UI or Project Files refresh; it does not perform refresh.

## Standalone vs embedded use

A utility or verification adapter may be selected directly by START only when the user request is primarily to prepare or verify that adapter artifact.

Examples:

- use `codex_handoff` directly when the selected work is only to package bounded Codex work;
- use `codex_result_verification` directly when the selected work is only to verify a returned Codex result.

Standalone selection still obeys START -> RUN -> FINISH and must not mutate, accept, or launch another material step unless the selected run surface explicitly allows that operation.

Embedded utility use is internal to RUN of the selected owner procedure.

Embedded utility use is allowed through the global Utility Use Gate, not through hardcoded per-core or per-run-surface whitelists.

Embedded utility use is represented as a typed intermediate output, not as a new procedure selection.

## RUN_EXTERNAL_HANDOFF

Use `RUN_EXTERNAL_HANDOFF` when the selected owner procedure requires an external utility result before it can complete RUN.

`RUN_EXTERNAL_HANDOFF` is an internal RUN gate. It is not FINISH_REQUEST, not FINISH, not Next Move Packet closure, and not procedure switching.

Required shape:

```text
RUN_EXTERNAL_HANDOFF:
  handoff_id:
  lifecycle_state: RUN_WAITING_FOR_EXTERNAL_RETURN
  owner_entrypoint:
  owner_procedure_ref:
  utility_category:
  external_surface:
  handoff_reason:
  copy_paste_packet:
  expected_return_packet:
  validation_required_on_return:
  resume_rule:
  unresolved_until_returned:
```

`resume_rule` must state that the same selected owner procedure resumes after the user returns external results.

While a required `RUN_EXTERNAL_HANDOFF` is pending, RUN must not emit FINISH_REQUEST.

## RUN_EXTERNAL_RETURN

Use `RUN_EXTERNAL_RETURN` when the user returns evidence from a prior `RUN_EXTERNAL_HANDOFF`.

Required shape:

```text
RUN_EXTERNAL_RETURN:
  lifecycle_state:
  owner_entrypoint:
  matching_handoff_id:
  returned_artifacts:
  verification_result:
  unresolved_items:
  resume_decision:
```

Required checks:

- match the return to the pending owner procedure and utility category;
- match the return to the emitted handoff id or exact emitted packet;
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

A selected owner procedure may emit a `storage_update_package` only as candidate next-surface output after acceptance/update authority is clear, unless the selected run surface is already `storage_update_adapter`. Actual storage mutation requires a separate admitted `storage_adapter` run with exact allowed files and validation.

## Finish and Next Move boundary

FINISH_REQUEST may be emitted only after required external handoffs have returned, been verified, or been explicitly abandoned as blocked/stopped.

Next Move Packet is for closure after the selected procedure completes or stops. It is not the mid-RUN external handoff mechanism.

Do not use `human_decision` to avoid producing a required transfer packet when the next external surface is materially known and the selected procedure is responsible for producing the packet.

After FINISH, the chat is closed for material work. A new material START in the same chat is forbidden. Post-FINISH responses may explain the closed result or point to emitted packets; they must not begin a new material lifecycle.

## Forbidden patterns

- selecting `codex_handoff` or `codex_result_verification` as a new owner procedure inside an active RUN;
- forcing a separate next material lifecycle solely because needed utility use was not prelisted;
- emitting FINISH_REQUEST while a required external return is unresolved;
- using Next Move Packet for a mid-RUN external handoff;
- asking Codex or another external surface to perform ChatGPT FINISH;
- treating embedded verification as acceptance;
- using `human_decision` to avoid a materially known complete transfer packet;
- embedding storage execution as hidden mutation.

## Output envelopes

Use these envelopes for embedded handoff and return gates:

```text
RUN_EXTERNAL_HANDOFF:
  handoff_id:
  lifecycle_state:
  owner_entrypoint:
  owner_procedure_ref:
  utility_category:
  external_surface:
  handoff_reason:
  copy_paste_packet:
  expected_return_packet:
  validation_required_on_return:
  resume_rule:
  unresolved_until_returned:
```

```text
RUN_EXTERNAL_RETURN:
  lifecycle_state:
  owner_entrypoint:
  matching_handoff_id:
  returned_artifacts:
  verification_result:
  unresolved_items:
  resume_decision:
```

## Eval hooks

A valid execution must preserve these invariants:

- one owner procedure selected by START;
- no procedure switch during RUN;
- utility use passes the global Utility Use Gate;
- utility packets are typed, bounded, and returned to the same owner RUN;
- required external returns are resolved before FINISH_REQUEST;
- returned external evidence is verified before reliance;
- no unadmitted mutation, acceptance, or launch;
- no material START after FINISH in the same chat.

END_OF_FILE: workflow_v3/control_plane/UTILITY_ADAPTER_PROTOCOL.md
