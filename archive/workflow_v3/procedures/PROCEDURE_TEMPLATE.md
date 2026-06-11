# Procedure: <Name>

status: draft_procedure

## Canonical Location

```text
workflow_v3/procedures/<NAME>_PROCEDURE.md
```

## Registry Alignment

```text
entrypoint:
kind: core | dependency_schema | verification | storage | readonly
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

The selected procedure owns these completion semantics. CHECK compares actual result to this block. The result must not be only a handoff, package, Codex package, check packet, storage packet, dependency packet, copy-paste packet, or `NEXT_CHAT_CARD`.

## START Output Support

START must be operator-readable first and must not perform material work.

```text
## Коротко

В этом чате я буду <простое описание работы>.

Зачем:
<1-3 строки простым языком>.

Какая процедура ведёт чат:
<entrypoint>. Она выбрана потому, что <простая причина>.

Когда задача будет считаться завершённой:
<проверяемое завершение>. Если понадобится внешняя зависимость для текущей цели, я открою DEPENDENCY_CALL и остановлюсь ждать return.

На что тебе смотреть:
<короткий список важных проверок>. Если всё стандартно: "Особого решения сейчас не нужно; проверь только цель и target."

Что будет дальше:
После START / СТАРТ я пройду stage 0. После каждого важного stage дам короткое резюме и остановлюсь на CONTINUE / ДАЛЬШЕ.

## Техническая часть

START_CONTRACT:
  selected_entrypoint:
  selected_procedure_path:
  kind:
  start_goal:
  terminal_condition:
  completion_contract:
  material_stages:
  routing_dependency_policy:
  required_sources:
  write_boundaries:
  user_confirmation_required: START | СТАРТ
```

START must not describe any package, handoff, card, or dependency envelope as the terminal condition.

## Self-contained Stub Mode

Use this section when the detailed body is not authored yet:

```text
title:
status: stub_procedure_pending_authoring
canonical_location:
entrypoint:
kind:
procedure_boundary:
target_role:
workflow_integration:
future_body_scope:
future_body_must_not:
required_outputs_when_authored:
stop_behavior_until_authored:
completion:
  result: blocked stub result explaining PROCEDURE_BODY_NOT_AUTHORED
  proof: canonical stub source and target role are present
  blocked_if: selected for execution before detailed body is authored
```

Stub mode must be self-contained enough to author the future procedure body without reading removed or obsolete sources. If selected for execution before authored, the procedure must stop with `PROCEDURE_BODY_NOT_AUTHORED`.

## Context Classification

Classify relevant context as canonical source, accepted record, current human input, verified excerpt, Project Files cache/context, candidate context, dependency evidence, historical evidence, or unknown/unverified.

## Stage Model

Material stages are user-visible and run one at a time. Internal checks are mechanical checks inside a material stage.

```text
stage_id:
stage_type: material stage
purpose:
inputs:
required_stage_result:
gate:
dependency_allowed_if:
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

STAGE_RESULT must be operator-readable first when the stage contains material conclusions, blockers, repair needs, or dependency calls. When the operator writes Russian, use the Russian human-facing shape below.

```text
## Коротко по шагу

Что сделал:
<простое описание>.

Что нашёл:
<no issue / issue / blocker / dependency required>.

На что тебе смотреть:
<что проверить, либо "ничего особого; это стандартный шаг">.

Что будет дальше:
<next stage / dependency wait / blocked / check>.

## Техническая часть

STAGE_RESULT:
  stage:
  result:
  proof:
  limitations:
  dependencies_opened:
  dependency_returns_verified:
  required_dependency_work_detected:
  dependency_call_opened:
  next_state:
  next_stage_or_check:
  user_confirmation_required:
```

STAGE_RESULT does not accept state, close the chat, or launch hidden dependency work.

## Routing / Dependency Policy

```text
routing_dependency_policy:
  same_chat_allowed_work:
  allowed_dependency_types:
  code_repository_dependency_route:
  support_dependency_route:
  core_lifecycle_dependency_route:
  storage_persistence_dependency_route:
  human_decision_dependency_route:
  forbidden_when:
  return_verification:
  unsupported_prior_labels:
  same_main_procedure_resume:
  closure_blockers:
```

Dependency type selection is governed by `workflow_v3/control_plane/ROUTING_AND_DEPENDENCY_PROTOCOL.md`. Support dependency packet shape is governed by `workflow_v3/control_plane/SUPPORT_DEPENDENCY_PROTOCOL.md`.

Dependency calls use `DEPENDENCY_CALL` / `DEPENDENCY_RETURN` and must resume this selected procedure. Prior packet labels are unsupported. `open_dependencies != empty`, a missing dependency return, an unverified dependency return, or missing required validation/evidence blocks CHECK, FINISH, and CLOSED.

Code/repository mutation, patching, branch creation, commits, pushes, file writes, implementation, write probes, and repository-side validation requiring writes route only through `code_repository_dependency` to Codex/code assistant. ChatGPT parent may draft the packet and verify return evidence only.

If the procedure detects required current-goal dependency repair and the parent cannot complete directly, the stage output must open `DEPENDENCY_CALL`, include the dependency id in `open_dependencies`, set `next_state: RUN_WAITING_FOR_DEPENDENCY_RETURN`, and wait for matching `DEPENDENCY_RETURN` / `CODEX_RETURN_PACKET`. CONTINUE / ДАЛЬШЕ, CHECK, FINISH, and CLOSED are invalid until the return is verified or the result is explicitly blocked.

## Output Contract

```text
field:
field:
limitations:
continuation:
```

## Quality Checks

- Required sources were read or limitations stated.
- Purpose, trigger/non-trigger, required inputs, source requirements, context classification, completion contract, stages, dependency policy, stop conditions, and output contract are explicit.
- Procedure gates have real outcomes and remain internal checks rather than separate route authority.
- Material stages emitted `STAGE_RESULT`.
- User confirmation occurred before the next material stage when required.
- Dependency calls returned to the same selected procedure and were verified before reliance.
- Runtime did not compress declared stage progression.
- Output satisfies the procedure's `completion:` block or names the blocker.
- `CLOSURE_CHECK` compares actual result to the selected completion block.
- Closure includes post-closed `NEXT_CHAT_CARD` when a new independent lifecycle is needed or `no_next_chat_needed` with reason.
- Handoff/card/package/dependency artifacts are not used as terminal parent completion.

## Stop Conditions

- Stop when required sources are missing or conflicting.
- Stop when requested work exceeds this procedure boundary.
- Stop when dependency use would become hidden mutation, hidden acceptance, procedure switching, wrong-surface execution, or unbounded wait.
- Stop when completion proof cannot be produced.
- Stop when required dependency returns are open, missing, unverified, or required validation/evidence is absent.

## Procedure Closure

Return `CLOSURE_CHECK` when RUN reaches completion or blocked state. Request FINISH only when the selected procedure completion contract is satisfied or explicitly blocked. After FINISH passes, the same chat is CLOSED for material work.

NEXT_CHAT_CARD is post-closed continuation only. It is not a dependency call, not a support dependency launch, and not evidence that the current START goal has completed. It must not represent unfinished dependency work from the current START goal.

END_OF_FILE: workflow_v3/procedures/PROCEDURE_TEMPLATE.md
