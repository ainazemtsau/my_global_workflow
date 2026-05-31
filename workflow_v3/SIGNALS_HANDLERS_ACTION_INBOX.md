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

Handler output may be no action, inline note, Action Inbox candidate, Check Job, blocked result, repair Next Move, primary Next Move, secondary candidate, candidate Launch Packet, Transition Packet, next-chat prompt, stop condition, or human decision request.

Action Inbox/Q is the candidate action queue.

Action Inbox stores candidate actions, not raw signals.

Action Inbox/Q is not raw signal storage, not a roadmap, not a hidden project manager, and not an automatic execution queue.

Check Job is bounded verification. It answers a scoped question, checks evidence/source/consistency, and returns candidate findings for review.

Event Loop Closure is the required closure phase for material work/review. It summarizes emitted Signals, Handler matches, candidate outputs, accepted conversions if any, persistence needs, and exact Next Move.

No accepted-state mutation from Signal, Handler, or Action Inbox.

Accepted State changes only through the explicit acceptance/update path defined by the runtime model.

## Progression Router

Progression Router is a default handler class that runs during Event Loop Closure after ordinary handler matches are visible.

It consumes closure Signals and Handler Results, then selects one `primary_next_move` and optional `secondary_candidates`.

It may produce a candidate Launch Packet, next-chat prompt, or Transition Packet for the selected next step.

It must not execute work, accept state, launch Codex, launch child chats, mutate files, bypass acceptance, import legacy state, use Action Inbox as a hidden roadmap, or continue product work after a blocking signal.

`progression_router_handler` matches closure Signals and Handler Results for:

- `material_run_closed`;
- `check_job_closed`;
- `codex_result_verified`;
- `acceptance_decision_recorded`;
- `work_contract_complete`;
- `active_front_complete`;
- `blocked_result_returned`.

`progression_router_handler` outputs:

- `primary_next_move`;
- `optional_secondary_candidates`;
- `same_chat_allowed`;
- `new_chat_needed`;
- candidate Launch Packet, next-chat prompt, or Transition Packet when transfer is needed;
- `stop` when no safe next move exists.

`progression_router_handler` must not:

- execute the next step;
- silently launch child chats;
- bypass acceptance;
- import legacy state;
- use Action Inbox as a hidden roadmap;
- continue product work after a blocking signal.

## Progression priority ladder

Use this priority order when routing a closed material run or review:

1. Blocking source, validation, or recovery issue -> block or Check Job.
2. Unclear acceptance -> human/parent decision.
3. Accepted result needs persistence -> Codex package.
4. Persistence result needs verification -> Codex result verification.
5. Current Work Contract complete and accepted -> next Work Graph node or close Active Front.
6. Active Front complete -> propose next Active Front or Direction-level decision.
7. Off-scope useful candidate -> Action Inbox candidate.
8. No safe useful next move -> stop.

## Transition Packet

Transition Packet is the complete copy-paste packet assembled by `progression_router_handler` for the selected next step when the step requires transfer to a human, Codex, Check Job, child chat, next material chat, or other external run surface.

The router must produce a complete packet, not merely say "create package". The `copy_paste_packet` must be sufficient for the user to paste into the selected surface without manually building Codex, check, child-chat, or next-chat prompts.

`transition_packet_type` enum:

- `human_decision_request`;
- `codex_handoff`;
- `codex_result_verification_request`;
- `check_job_launch`;
- `child_chat_launch`;
- `next_material_chat_launch`;
- `stop`;
- `blocked_result`.

Transition Packet fields:

- `transition_packet_type`;
- `same_chat_allowed`;
- `external_run_needed`;
- `external_run_type`;
- `returns_to_current_chat`;
- `next_material_chat_needed`;
- `copy_paste_packet`.

`same_chat_allowed` states whether the selected next move can be completed in the current chat without losing source, scope, or acceptance clarity.

`external_run_needed` states whether the next move requires a separate surface.

`external_run_type` identifies that surface, such as `human`, `codex`, `codex_verification`, `check_job`, `child_chat`, `next_material_chat`, or `none`.

`returns_to_current_chat` states whether the external run result must come back to the current chat for verification, acceptance review, or Event Loop Closure.

`next_material_chat_needed` states whether the next accepted unit of material work needs a new material chat.

Codex handoff returns to the same current chat for verification and closure.

Next material chat starts only after the current material target is accepted, persisted, verified, or explicitly stopped.

## Normal progress routing

Normal progress is not a hard-coded chain.

Direction Spine -> Direction Map -> Active Front -> Work Graph -> Work Contract is the object hierarchy.

The next concrete step is routed by Event Loop Closure and `progression_router_handler`.

Handler output is candidate until accepted or explicitly launched.

Chat intuition is not route authority.

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
- `lifecycle_signal` - Direction lifecycle facts about runtime adoption, Direction Spine, Direction Map, Active Front, Work Graph, Work Contract, front closure, map staleness, track imbalance, or blocked lifecycle transitions.

## Direction lifecycle signals

Lifecycle signals are facts only. They do not execute work or mutate accepted state.

Baseline lifecycle signals:

- `direction_runtime_missing`;
- `direction_adoption_needed`;
- `direction_spine_missing`;
- `direction_spine_candidate_returned`;
- `direction_spine_accepted`;
- `direction_map_missing`;
- `direction_map_candidate_returned`;
- `direction_map_accepted`;
- `active_front_missing`;
- `active_front_candidate_returned`;
- `active_front_accepted`;
- `work_graph_missing`;
- `work_graph_created`;
- `work_graph_node_ready`;
- `work_contract_created`;
- `work_contract_complete`;
- `active_front_complete`;
- `direction_map_update_needed`;
- `direction_map_stale`;
- `track_imbalance_detected`;
- `blocked_lifecycle_transition`.

Lifecycle transitions are not a hard-coded chain and are not selected by chat intuition. They become visible through Signal, Handler, Event Loop Closure, Progression Router, and acceptance/update path when state changes.

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
| `direction_adoption_guard_handler` | `lifecycle_signal` where runtime is missing, adoption is needed, or lifecycle transition would imply adoption. | Blocked result, adoption decision request, or bounded adoption package candidate. | Create runtime state, import legacy state, or adopt a Direction by implication. | Inline, Check Job, blocked result, repair Next Move, human decision request, candidate Launch Packet. |
| `direction_spine_creation_handler` | `lifecycle_signal` for missing, returned, or accepted Direction Spine facts. | Candidate Spine review packet, acceptance/update request, or blocked result if source is missing. | Invent Spine state or mutate accepted Spine directly. | Inline, Check Job, blocked result, candidate Launch Packet, human decision request. |
| `direction_map_creation_handler` | `lifecycle_signal` for missing, returned, or accepted Direction Map facts. | Candidate Direction Map review packet, acceptance/update request, or source/evidence Check Job. | Treat roadmap, backlog, Work Graph, or Action Inbox as Direction Map. | Inline, Check Job, blocked result, candidate Launch Packet, human decision request. |
| `active_front_selection_handler` | `lifecycle_signal` for missing Active Front or candidate Active Front returned. | Candidate front selection packet with map areas, alternatives, exit criteria, and acceptance question. | Select Active Front by chat intuition or accept the front directly. | Inline, Action Inbox candidate, Check Job, candidate Launch Packet, human decision request. |
| `work_graph_opening_handler` | `lifecycle_signal` where accepted Active Front lacks local Work Graph. | Candidate local Work Graph seed or opening packet. | Build global roadmap/backlog or overwrite Direction Map. | Inline, Check Job, candidate Launch Packet, repair Next Move. |
| `work_contract_creation_handler` | `lifecycle_signal` where a Work Graph node is ready for bounded execution. | Candidate Work Contract or Launch Packet. | Execute work directly or expand node scope. | Inline, candidate Launch Packet, human decision request. |
| `front_closure_handler` | `lifecycle_signal` where Active Front exit criteria appear complete. | Candidate front closure summary, acceptance question, map update candidate, or Check Job. | Close the front without evidence/acceptance or silently open a new front. | Inline, Check Job, human decision request, transition_packet. |
| `direction_map_update_handler` | `lifecycle_signal` where map update is needed, stale, or track imbalance appears. | Candidate Direction Map update packet, Check Job, or human decision request. | Mutate Direction Map without accepted update path. | Inline, Check Job, action_inbox_candidate, human decision request, transition_packet. |
| `progression_router_handler` | Closure Signals and Handler Results for `material_run_closed`, `check_job_closed`, `codex_result_verified`, `acceptance_decision_recorded`, `work_contract_complete`, `active_front_complete`, or `blocked_result_returned`. | One `primary_next_move`, optional `secondary_candidates`, `same_chat_allowed`, `new_chat_needed`, Transition Packet or next-chat prompt if needed, or stop. | Execute the next step, silently launch child chats, bypass acceptance, import legacy state, use Action Inbox as a hidden roadmap, or continue product work after a blocking signal. | Primary next move, secondary candidate, next-chat prompt, Transition Packet, stop condition. |

## Execution order

Run handler matching in this order when multiple Signals are present:

1. Blocking source, validation, and recovery handlers first.
2. Acceptance handlers before continuation.
3. Scope and legacy guard before product work.
4. Inbox hygiene after material closure unless it is blocking.
5. Non-blocking watch items last.
6. Progression router after candidate outputs and blockers are visible.

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
6. Run `progression_router_handler`.
7. Provide exact Next Move and a complete Transition Packet when transfer is needed.

New chat is required only for Child Chat, Check Job with separate context, Codex package, long parent review, or human action.

Handler outputs are candidate until accepted or converted.

Do not run handlers as hidden automation. The manual closure must make Signal, Handler, and candidate-action reasoning visible enough for review.

## Persistence rule

Event Loop Closure can remain in chat unless persistence is needed.

Persist Signals, Action Inbox/Q updates, Check Jobs, or handler registry changes only through explicit acceptance/update package.

Persisted Check Jobs and persisted Event Loop Closures require explicit acceptance/update package. These operational records do not mutate accepted state.

Direction runtime storage location for persisted signals:

```text
directions_v3/<direction-id>/runtime/operations/signals/
```

Direction action inbox:

```text
directions_v3/<direction-id>/runtime/operations/action_inbox/
```

Direction Check Jobs:

```text
directions_v3/<direction-id>/runtime/operations/check_jobs/
```

Direction Event Loop Closures:

```text
directions_v3/<direction-id>/runtime/operations/event_loop_closures/
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
- `workflow_v3/templates/EVENT_LOOP_CLOSURE_TEMPLATE.md`;
- `workflow_v3/templates/PROGRESSION_ROUTER_RESULT_TEMPLATE.md`;
- `workflow_v3/templates/TRANSITION_PACKET_TEMPLATE.md`;
- `workflow_v3/templates/NEXT_CHAT_PROMPT_TEMPLATE.md`.

END_OF_FILE: workflow_v3/SIGNALS_HANDLERS_ACTION_INBOX.md
