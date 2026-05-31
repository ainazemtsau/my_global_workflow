# Signals / Handlers / Action Inbox

status: active_skeleton_namespace_corrected

## Purpose

This file defines the production Workflow v3 operational event loop for Signals, Handlers, Action Inbox/Q, Check Jobs, and Event Loop Closure.

The loop restores this intended flow:

```text
Signal -> Handler -> Candidate Action / Check Job / Next Move -> Event Loop Closure
```

It is an operational control layer for noticing workflow facts and proposing bounded follow-up. It is not an accepted-state path, automation engine, backlog, or product execution authority.

## Core semantics

Signal is an emitted workflow event/fact record.

Signal is not an Action Inbox item.

Signal is not a task, command, acceptance, mutation, Q item, or Action Inbox item.

Signal records what happened or was observed. It does not decide what must be done.

Handler is a registry rule/process that reacts to Signal.

Handler output is candidate only.

Handler output may be no action, inline note, Action Inbox candidate, Check Job, blocked result, repair Next Move, candidate Launch Packet, or human decision request.

Action Inbox/Q is the candidate action queue.

Action Inbox stores candidate actions, not raw signals.

Action Inbox/Q is not raw signal storage, not a roadmap, not a hidden project manager, and not an automatic execution queue.

Check Job is bounded verification. It answers a scoped question, checks evidence/source/consistency, and returns candidate findings for review.

Event Loop Closure is the required closure phase for material work/review. It summarizes emitted Signals, Handler matches, candidate outputs, accepted conversions if any, persistence needs, and exact Next Move.

No accepted-state mutation from Signal, Handler, or Action Inbox.

Accepted State changes only through the explicit acceptance/update path defined by the runtime model.

## Minimal emit points

Emit a Signal when a notable workflow fact is observed, especially at these minimum points:

- material run closed;
- blocking condition observed;
- scope drift observed;
- legacy boundary touched;
- validation failed;
- acceptance unclear;
- Action Inbox hygiene needed;
- parent/child coordination issue.

Do not emit Signals for every ordinary thought or minor preference. Emit only facts useful for closure, review, recovery, or later verification.

## Minimal Signal/Event fields

Use a lightweight record. Required fields:

- `signal_id`;
- `emitted_at`;
- `event_type`;
- `category`;
- `observed_fact`;
- `source_or_origin`;
- `related_direction/front/node/work_contract/run if known`;
- `severity`;
- `handler_status`;
- `resulting_candidate_action_id if any`;
- `limitations`.

Recommended severity values:

- `info`;
- `watch`;
- `needs_attention`;
- `blocking`.

Recommended handler status values:

- `not_handled`;
- `handled_inline`;
- `candidate_created`;
- `check_job_created`;
- `blocked`;
- `ignored_with_reason`;
- `superseded`.

## Minimal categories

- `source_signal` - source access, freshness, missing files, stale cache, or source authority facts.
- `scope_signal` - scope drift, mixed jobs, phase jumps, or boundary pressure.
- `evidence_signal` - missing, weak, conflicting, or failed evidence.
- `acceptance_signal` - unclear acceptance, hidden acceptance risk, rejected result, or candidate needing review.
- `adapter_signal` - facts from ChatGPT, Codex, Claude Code/future assistants, research agents, GitHub access, future providers, or human actions.
- `inbox_signal` - Action Inbox/Q growth, duplicate candidates, stale items, or handler flood.
- `recovery_signal` - blocked runs, missing child results, failed validation, lost parent context, or recovery needs.
- `legacy_signal` - old Workflow OS, old Direction state, legacy evidence, import boundary, rollback, or coexistence facts.

## Default handler registry

The default registry is the baseline for future per-Direction handler config. Direction-specific handlers may extend it, but they must not bypass the core rule that Handler output is candidate only.

| Handler | Matches | Outputs | Must not do | Allowed output forms |
| --- | --- | --- | --- | --- |
| `missing_source_handler` | `source_signal` where required source/path/ref is missing, unreadable, or incomplete. | Blocked result naming the missing source, source retrieval Check Job, or repair Next Move. | Guess repository state, continue material work from stale context, or mark source as accepted. | Inline, Check Job, blocked result, repair Next Move, human decision request. |
| `stale_context_handler` | `source_signal` where Project Files/Sources, pasted excerpts, memory, or supplied context may be stale. | Candidate verification action before material work, source freshness Check Job, or warning in Event Loop Closure. | Treat cache/context as canonical source or silently refresh Project state. | Inline, Action Inbox candidate, Check Job, repair Next Move. |
| `scope_drift_handler` | `scope_signal` where work expands, mixes jobs, touches forbidden paths, or jumps phase. | Candidate split/park action, narrowed Launch Packet, or repair Next Move back to the Work Contract. | Continue the expanded scope, rewrite accepted scope, or launch residual work silently. | Inline, Action Inbox candidate, blocked result, repair Next Move, candidate Launch Packet, human decision request. |
| `failed_validation_handler` | `evidence_signal` or `recovery_signal` where validation failed, evidence contradicts the done claim, or required checks were not run. | Same-scope repair Next Move, Codex/package repair candidate, Check Job, or blocked result. | Claim done, accept failed evidence, broaden allowed paths, or suppress failed validation. | Inline, Action Inbox candidate, Check Job, blocked result, repair Next Move, candidate Launch Packet. |
| `unclear_acceptance_handler` | `acceptance_signal` where result exists but explicit acceptance/update path is absent or ambiguous. | Acceptance review request, human decision request, or candidate Next Move to perform parent review. | Treat candidate output as accepted, mutate state, or let an adapter accept its own result. | Inline, Action Inbox candidate, blocked result, repair Next Move, human decision request. |
| `child_missing_handler` | `recovery_signal` or `adapter_signal` where Child Chat, Codex, Check Job, or other child result is missing, incomplete, or did not return. | Parent Recovery Block, rerun/narrow candidate, missing-result request, or blocked result. | Synthesize missing evidence, assume child completion, or accept partial child output silently. | Inline, Action Inbox candidate, Check Job, blocked result, repair Next Move, human decision request. |
| `inbox_hygiene_handler` | `inbox_signal` where Action Inbox/Q has duplicates, stale candidates, vague items, handler flood, or no run condition. | Merge/drop/supersede candidate, hygiene Check Job, or prioritized candidate list. | Store raw untriaged Signals as backlog, auto-run items, or close items without reason. | Inline, Action Inbox candidate, Check Job, repair Next Move, human decision request. |
| `legacy_import_guard_handler` | `legacy_signal` where old Workflow OS, old Direction files, legacy evidence, import, rollback, or coexistence boundary is touched. | Blocked result, candidate legacy import receipt path, rollback/coexistence warning, or human decision request. | Invent Direction proof state, import/migrate by implication, weaken rollback, or mutate `directions/**`. | Inline, Action Inbox candidate, Check Job, blocked result, repair Next Move, candidate Launch Packet, human decision request. |

## Execution order

Run handler matching in this order when multiple Signals are present:

1. Blocking source, validation, and recovery handlers first.
2. Acceptance handlers before continuation.
3. Scope and legacy guard before product work.
4. Inbox hygiene after material closure unless it is blocking.
5. Non-blocking watch items last.

No handler may silently launch work.

Handler output remains candidate until a user, parent review, or explicit acceptance/update path accepts, converts, drops, or persists it.

## ChatGPT manual execution protocol

At the end of material work, ChatGPT must include EVENT LOOP CLOSURE.

Default is same-message inline processing:

1. State the material Result Packet.
2. Emit Signals for notable closure facts.
3. Match the handler registry.
4. List candidate outputs.
5. State whether anything needs persistence.
6. Provide exact Next Move.

New chat is required only for Child Chat, Check Job with separate context, Codex package, long parent review, or human action.

Handler outputs are candidate until accepted or converted.

Do not run handlers as hidden automation. The manual closure must make Signal, Handler, and candidate-action reasoning visible enough for review.

## Persistence rule

Event Loop Closure can remain in chat unless persistence is needed.

Persist Signals, Action Inbox/Q updates, Check Jobs, or handler registry changes only through explicit acceptance/update package.

Direction runtime storage location for persisted signals:

```text
directions_v3/<direction-id>/runtime/operations/signals/
```

Direction action inbox:

```text
directions_v3/<direction-id>/runtime/operations/action_inbox/
```

Direction handler registry:

```text
directions_v3/<direction-id>/runtime/config/HANDLERS.md
```

This file does not create any per-Direction runtime state and does not authorize changes under `directions_v3/**`.

## Template index

- `workflow_v3/templates/SIGNAL_RECORD_TEMPLATE.md`;
- `workflow_v3/templates/HANDLER_RESULT_TEMPLATE.md`;
- `workflow_v3/templates/ACTION_INBOX_ITEM_TEMPLATE.md`;
- `workflow_v3/templates/CHECK_JOB_TEMPLATE.md`;
- `workflow_v3/templates/EVENT_LOOP_CLOSURE_TEMPLATE.md`.

END_OF_FILE: workflow_v3/SIGNALS_HANDLERS_ACTION_INBOX.md
