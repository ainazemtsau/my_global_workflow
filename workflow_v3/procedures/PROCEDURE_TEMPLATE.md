# Procedure: <Name>

status: draft_procedure

## Canonical Location

```text
workflow_v3/procedures/<NAME>_PROCEDURE.md
```

## Registry Alignment

```text
entrypoint:
kind: core | utility | verification | storage | readonly
```

## Purpose

State the bounded work this procedure performs.

## Trigger / When to Use

- Use when ...

## When Not to Use

- Do not use when ...

## Required Inputs

- target / question / artifact:
- source refs or bindings:
- expected output:

## Source Requirements

- Exact sources to read:
- EOF or integrity checks:
- Source limitations to report:

## Completion Contract

```text
completion:
  result:
  proof:
  blocked_if:
```

The selected procedure owns these completion semantics. CHECK compares actual result to this block. The result must not be only a handoff, package, Codex package, check packet, storage packet, child-chat card, copy-paste packet, or `NEXT_CHAT_CARD`.

## START Output Support

START must be operator-readable first and must not perform material work.

```text
## Operator Brief

- Goal:
- Selected main procedure:
- Why this procedure:
- Terminal condition:
- Child procedure calls:
- Before START / СТАРТ, review:

START_CONTRACT:
  selected_entrypoint:
  selected_procedure_path:
  kind:
  start_goal:
  terminal_condition:
  completion_contract:
  material_stages:
  child_call_policy:
  required_sources:
  write_boundaries:
  user_confirmation_required: START | СТАРТ
```

START must not describe any package, handoff, card, or child-call envelope as the terminal condition.

## Self-contained Stub Mode

Use this section when the detailed body is not authored yet:

```text
status: stub_procedure_pending_authoring
target_role:
workflow_integration:
future_body_outline:
required_outputs_when_authored:
stop_behavior_until_authored:
completion:
  result: blocked stub result explaining PROCEDURE_BODY_NOT_AUTHORED
  proof: canonical stub source and target role are present
  blocked_if: selected for execution before detailed body is authored
```

Stub mode must be self-contained enough to author the future procedure body without reading removed or obsolete sources. If selected for execution before authored, the procedure must stop with `PROCEDURE_BODY_NOT_AUTHORED`.

## Context Classification

Classify relevant context as canonical source, accepted record, current human input, verified excerpt, Project Files cache/context, candidate context, adapter evidence, historical evidence, or unknown/unverified.

## Stage Model

Material stages are user-visible and run one at a time. Internal checks are mechanical checks inside a material stage.

```text
stage_id:
stage_type: material stage
purpose:
inputs:
required_stage_result:
gate:
utility_allowed_if:
blocked_if:
```

```text
check_id:
stage_type: internal_check
purpose:
pass_if:
blocked_if:
```

RUN emits `STAGE_RESULT` after each material stage and waits for `CONTINUE` / `ДАЛЬШЕ` before the next material stage unless the next step is an `internal_check`.

Runtime must execute this procedure's declared stages. START/RUN must not invent ad hoc simple, compact, shortcut, or single-stage compression that bypasses declared stages. A procedure may define a small declared stage list, but runtime cannot merge declared stages into one undeclared stage. A declared stage may end quickly or be marked not_applicable with evidence, but it must still be represented in progression when applicable.

STAGE_RESULT must be operator-readable first when the stage contains material conclusions, blockers, repair needs, or child calls.

```text
## Operator Brief

- Stage:
- What changed:
- Evidence checked:
- Review before continuing:

STAGE_RESULT:
  stage:
  result:
  proof:
  limitations:
  child_calls_opened:
  child_returns_verified:
  next_stage_or_check:
  user_confirmation_required:
```

STAGE_RESULT does not accept state, close the chat, or launch hidden child work.

## Child Call Policy

```text
child_call_policy:
  allowed_when:
  common_targets:
  forbidden_when:
  return_verification:
  same_main_procedure_resume:
```

Child procedure calls use `CHILD_PROCEDURE_CALL` / `CHILD_PROCEDURE_RETURN` and must resume this selected procedure. `UTILITY_CALL` / `UTILITY_RETURN` may appear only as adapter-level compatibility aliases. `open_child_calls != empty`, a missing child return, an unverified child return, or missing required validation/evidence blocks CHECK, FINISH, and CLOSED.

## Output Contract

```text
field:
field:
limitations:
continuation:
```

## Eval / Quality Checks

- Required sources were read or limitations stated.
- Material stages emitted `STAGE_RESULT`.
- User confirmation occurred before the next material stage when required.
- Child procedure calls returned to the same selected procedure and were verified before reliance.
- Runtime did not compress declared stage progression.
- Output satisfies the procedure's `completion:` block or names the blocker.
- `CLOSURE_CHECK` compares actual result to the selected completion block.
- Closure includes post-closed `NEXT_CHAT_CARD` when a new independent lifecycle is needed or `no_next_chat_needed` with reason.
- Handoff/card/package/child-call artifacts are not used as terminal parent completion.

## Stop Conditions

- Stop when required sources are missing or conflicting.
- Stop when requested work exceeds this procedure boundary.
- Stop when child/adaptor use would become hidden mutation, hidden acceptance, procedure switching, or unbounded wait.
- Stop when completion proof cannot be produced.
- Stop when required child returns are open, missing, unverified, or required validation/evidence is absent.

## Procedure Closure

Return `CLOSURE_CHECK` when RUN reaches completion or blocked state. Request FINISH only when the selected procedure completion contract is satisfied or explicitly blocked. After FINISH passes, the same chat is CLOSED for material work.

NEXT_CHAT_CARD is post-closed continuation only. It is not a child call, not a utility launch, and not evidence that the current START goal has completed. It must not represent unfinished child work from the current START goal.

END_OF_FILE: workflow_v3/procedures/PROCEDURE_TEMPLATE.md
