# Chat Lifecycle Protocol

status: active_control_plane

## Authority

This file is the Workflow v3 runtime kernel for material and state-sensitive chats.

Procedure selection is owned by `workflow_v3/control_plane/PROCEDURE_REGISTRY.md`. Child procedure calls and adapter aliases are governed by `workflow_v3/control_plane/UTILITY_ADAPTER_PROTOCOL.md`. Final audit is governed by `workflow_v3/control_plane/CHAT_FINISH_PROTOCOL.md`.

## State Model

```text
START
-> RUN_STAGE
-> STAGE_RESULT
-> RUN_WAITING_FOR_CHILD_RETURN when a child call is required
-> CHILD_RETURN_VERIFICATION
-> RUN_STAGE or CHECK
-> CHECK
-> FINISH
-> CLOSED

CHECK -> RUN repair
CHECK -> blocked escalation
FINISH -> RUN repair
FINISH -> blocked escalation
```

`CHILD_PROCEDURE_CALL` and `CHILD_PROCEDURE_RETURN` are the canonical lifecycle terms for external or subordinate work. Existing `UTILITY_CALL` and `UTILITY_RETURN` labels may be used only as adapter-level compatibility names under this model. They do not define a separate runtime loop and never switch the selected main procedure.

## Universal Rules

- One material chat selects exactly one main procedure.
- The selected main procedure defines completion through its `completion:` block.
- Runtime executes the selected procedure's declared stage sequence one material stage at a time.
- START/RUN must not invent ad hoc simple, compact, shortcut, or single-stage compression that bypasses declared stages.
- A declared stage may finish quickly or be marked not_applicable with evidence, but applicable declared stages remain represented in progression.
- Child procedure calls return to the same selected main procedure and are verified before reliance.
- `open_child_calls != empty` blocks CHECK, FINISH, and CLOSED.
- `missing_child_return` blocks CHECK, FINISH, and CLOSED.
- `unverified_child_return` blocks CHECK, FINISH, and CLOSED.
- If `required_child_work_detected = true` and the parent cannot satisfy the current START goal directly, the parent must emit/open `CHILD_PROCEDURE_CALL`; `child_call_opened = false` blocks CHECK, FINISH, and CLOSED.
- Missing required validation or evidence blocks CHECK, FINISH, and CLOSED.
- A handoff, card, package, copy-paste packet, Codex package, check packet, storage packet, child-chat card, or `NEXT_CHAT_CARD` cannot satisfy a parent START goal by itself.
- CHECK compares actual result to the selected procedure completion contract.
- FINISH closes only after CHECK passes or the selected procedure's blocked completion condition is explicit.
- CLOSED chats do not start new material work.
- `NEXT_CHAT_CARD` is post-closed continuation only. It is not a child call, not a utility launch, and not evidence that the current START goal has completed.

## START

START selects and prepares the main procedure. It must not perform material work and must not describe any package, handoff, or card as the terminal condition.

START must:

- classify the user request and identify one concrete work item;
- return `SPLIT_REQUIRED` if multiple independent work items are requested;
- read `PROCEDURE_REGISTRY.md` and select exactly one main procedure;
- read the selected procedure file and verify source availability;
- begin with a short operator-readable plain-language block;
- when the operator writes Russian, put the human-facing block in Russian before technical fields;
- state what this chat will do, why the selected procedure applies, what completion means, what the operator should review, whether the step is default/no-action or requires attention, and what happens after START / СТАРТ;
- show the selected procedure's `completion:` contract;
- show the procedure's material stages when present;
- show allowed boundaries, including write and child-call boundaries;
- wait for standalone `START` or `СТАРТ` before RUN.

START output shape:

```text
## Коротко

В этом чате я буду <простое описание работы>.

Зачем:
<1-3 строки простым языком>.

Какая процедура ведёт чат:
<entrypoint>. Она выбрана потому, что <простая причина>.

Когда задача будет считаться завершённой:
<проверяемое завершение>. Если понадобится Codex или другой child для текущей цели, я открою CHILD_PROCEDURE_CALL и остановлюсь ждать return.

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
  child_call_policy:
  required_sources:
  write_boundaries:
  user_confirmation_required: START | СТАРТ
```

Compact example:

```text
## Коротко

В этом чате я буду чинить одно правило в источнике Workflow v3.

Зачем:
Нужно убрать устаревшее правило закрытия, чтобы процедура не закрывала чат раньше проверки.

Какая процедура ведёт чат:
author_workflow_procedure. Она выбрана потому, что запрос меняет authority процедуры Workflow v3 и связанные eval-проверки.

Когда задача будет считаться завершённой:
Изменение будет подтверждено источниками, diff/validation и CLOSURE_CHECK. Если потребуется Codex для записи в репозиторий, я открою CHILD_PROCEDURE_CALL и остановлюсь ждать return.

На что тебе смотреть:
Проверь цель, target-файл и границы записи. Особого решения сейчас не нужно, если они верны.

Что будет дальше:
После START / СТАРТ я пройду stage 0. После каждого важного stage дам короткое резюме и остановлюсь на CONTINUE / ДАЛЬШЕ.

## Техническая часть

START_CONTRACT:
  selected_entrypoint: author_workflow_procedure
  selected_procedure_path: workflow_v3/procedures/PROCEDURE_AUTHORING_AND_INTEGRATION_PROCEDURE.md
  kind: core
  start_goal: remove stale closure rule from one procedure source
  terminal_condition: verified completion or explicit blocked result, not a handoff/card/package
  completion_contract: <selected procedure completion block>
  material_stages: <declared stage sequence>
  child_call_policy: visible CHILD_PROCEDURE_CALL required before external work; unresolved until CHILD_PROCEDURE_RETURN verification
  required_sources: <exact source paths>
  write_boundaries: <none in parent chat unless admitted write path exists>
  user_confirmation_required: START | СТАРТ
```

## RUN

RUN executes only the selected main procedure.

RUN must:

- execute one visible material stage at a time;
- represent each applicable declared material stage in progression;
- emit `STAGE_RESULT` after each material stage;
- wait for user `CONTINUE` or `ДАЛЬШЕ` before the next material stage unless the next step is explicitly `internal_check`;
- run `internal_check` steps only as mechanical checks inside the current stage;
- keep child procedure calls subordinate to the same selected main procedure;
- enter `RUN_WAITING_FOR_CHILD_RETURN` when required external or subordinate work is opened;
- verify every required `CHILD_PROCEDURE_RETURN` before the returned evidence can affect CHECK or FINISH;
- when a stage determines that external child/adaptor repair is required for the current START goal and the parent cannot mutate directly, emit/open `CHILD_PROCEDURE_CALL`, record the call id in `open_child_calls`, set `next_state: RUN_WAITING_FOR_CHILD_RETURN`, and require matching `CHILD_PROCEDURE_RETURN` / `CODEX_RETURN_PACKET`;
- reject any later-stage, CHECK, FINISH, or CLOSED progression while required child/adaptor repair has not been opened, returned, and verified;
- prevent direct mutation unless the selected main procedure or a verified child/adaptor write path admits exact writes;
- avoid hidden launches, hidden acceptance, and procedure switching.

STAGE_RESULT must be operator-readable first when the stage contains material conclusions, blockers, repair needs, or child calls. When the operator writes Russian, the human-facing block is Russian. It must say what happened, what was found, what the human should review, and what happens next. Technical fields follow. STAGE_RESULT does not accept state, close the chat, or launch hidden child work.

STAGE_RESULT output shape:

```text
## Коротко по шагу

Что сделал:
<простое описание>.

Что нашёл:
<no issue / issue / blocker / child required>.

На что тебе смотреть:
<что проверить, либо "ничего особого; это стандартный шаг">.

Что будет дальше:
<next stage / child wait / blocked / check>.

## Техническая часть

STAGE_RESULT:
  stage:
  result:
  proof:
  limitations:
  child_calls_opened:
  child_returns_verified:
  required_child_work_detected:
  child_call_opened:
  next_state:
  next_stage_or_check:
  user_confirmation_required:
```

## CHILD PROCEDURE CALLS

Child procedure work is a supporting call made during RUN because the selected procedure or current stage needs external or subordinate evidence.

CHILD_PROCEDURE_CALL must:

- state why the child/adaptor is needed;
- name the target child or adapter surface;
- include a complete packet or call boundary when external user action is required;
- state expected return;
- resume the same selected main procedure;
- verify returned evidence before relying on it;
- remain unresolved until the matching `CHILD_PROCEDURE_RETURN` is received and verified.

Required current-goal repair has no separate prepared-only state. If the stage output says `repair_needed: true` and the selected parent cannot mutate directly, the same visible output must open `CHILD_PROCEDURE_CALL`, include the call id in `open_child_calls`, enter `RUN_WAITING_FOR_CHILD_RETURN`, and make CONTINUE / ДАЛЬШЕ invalid until the matching return is verified.

Codex, child chat, check job, storage update, research agent, GitHub/file access, human decision, and future providers are child/adapters under this model. Use `CHILD_PROCEDURE_CALL` / `CHILD_PROCEDURE_RETURN`; `UTILITY_CALL` / `UTILITY_RETURN` are compatibility aliases only where older adapter packets still name them.

## CHECK

CHECK compares the actual result against the selected procedure's completion contract.

CLOSURE_CHECK must:

```text
CLOSURE_CHECK:
  selected_entrypoint:
  selected_procedure_path:
  completion_contract:
  actual_result:
  proof:
  open_child_calls:
  missing_child_returns:
  unverified_child_returns:
  required_child_work_detected:
  child_call_opened:
  required_validation_evidence:
  gaps:
  decision: pass | return_to_run_repair | blocked
  next_action:
```

CHECK may request FINISH only when the contract is satisfied or when the selected procedure explicitly allows blocked completion. If gaps remain, return to RUN repair or blocked escalation. If any child call is open, missing, unverified, or required evidence/validation is absent, CHECK must block or return to RUN repair and must not pass. If `required_child_work_detected = true` and `child_call_opened = false`, CHECK must block or return to RUN repair. The invalid transition is: required repair found -> draft/package-only output -> next stage/CHECK/FINISH. The valid transition is: required repair found -> `CHILD_PROCEDURE_CALL` -> `RUN_WAITING_FOR_CHILD_RETURN`.

## FINISH

FINISH is final audit and closure after CHECK passes or blocks according to the selected procedure.

FINISH must:

- read `CHAT_FINISH_PROTOCOL.md`;
- audit the run against START and the selected procedure completion contract;
- confirm declared stage progression was not compressed;
- confirm no open, missing, or unverified child procedure return is being relied on;
- confirm required child/adaptor repair was either opened, returned, and verified or explicitly blocked;
- confirm actual result is not only a handoff, card, package, copy-paste packet, Codex package, check packet, storage packet, child-chat card, or `NEXT_CHAT_CARD`;
- close only if the audit passes;
- return to RUN repair or blocked escalation if the audit fails;
- include a human-readable result;
- include post-closed `NEXT_CHAT_CARD` when a new independent lifecycle is needed, or `no_next_chat_needed` with reason.

## CLOSED

CLOSED means the material workflow chat is complete or explicitly blocked for the selected main procedure. No new material START may occur in the same chat.

A closed material workflow chat must include either a post-closed continuation:

```text
NEXT_CHAT_CARD:
  title:
  why:
  main_procedure_to_start:
  context_to_paste:
  expected_result:
  evidence_or_return_needed:
  start_instruction:
```

or:

```text
no_next_chat_needed:
  reason:
```

NEXT_CHAT_CARD must not represent unfinished child work from the current START goal. It must not replace `CHILD_PROCEDURE_CALL`, must not make the user assemble a missing child call from scattered previous text, and must appear only inside FINISH_PACKET after FINISH audit passes or as a clearly named post-closed continuation.

## STOP / Blocked Escalation

Use a blocked escalation when the lifecycle cannot safely proceed because source, boundary, child return, validation, completion proof, or user authority is missing.

Common blocked reasons:

- `SPLIT_REQUIRED`
- `CONTEXT_REQUEST`
- `UNREGISTERED_ACTION_EXCEPTION`
- `SOURCE_AUTHORITY_CONFLICT`
- `BOUNDARY_CROSSING_STOP`
- `WRITE_NOT_ADMITTED`
- `VALIDATION_REQUIRED_STOP`
- `SOURCE_INTEGRITY_STOP`
- `CHILD_PROCEDURE_RETURN_REQUIRED_STOP`
- `COMPLETION_CONTRACT_NOT_SATISFIED`

END_OF_FILE: workflow_v3/control_plane/CHAT_LIFECYCLE_PROTOCOL.md
