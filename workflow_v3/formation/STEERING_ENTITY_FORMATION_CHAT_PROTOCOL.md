# Steering Entity Formation Chat Protocol

status: active_steering_entity_formation_chat_protocol

## Role

A formation chat forms one steering entity candidate through visible framing, alternatives, criteria, evidence, attack, cut, and closure.

It does not accept the entity by itself.

## Trigger

Use when a Launch Packet, Direction Definition runbook, lifecycle handler, accepted Next Move, or human request asks to form a steering entity.

## Inputs

- target steering entity;
- direction_id if available;
- source authority and required reads;
- accepted state or setup-only pending state;
- candidate context;
- constraints and forbidden surfaces;
- expected result and return destination.

## Child research/check chats

Child chats are allowed only for bounded evidence or consistency questions serving the current entity.

Child results must return to the parent formation chat. They cannot decide the entity, accept the entity, mutate state, or become independent execution tracks.

## Formation sequence

1. Confirm target entity and boundary.
2. Classify sources and context.
3. Frame the decision the entity controls.
4. Generate alternatives unless trivial or blocked.
5. Define criteria.
6. Summarize evidence, hypotheses, and gaps.
7. Attack contradictions and failure modes.
8. Cut waste and out-of-scope work.
9. Draft the candidate entity.
10. Record rejected/deferred alternatives.
11. State read limitations.
12. Ask the acceptance question.
13. Produce Event Loop Closure.
14. Select exact next move or Transition Packet.

## Result packet

```text
result:
candidate_entity_ref_or_inline:
evidence:
source_read_limitations:
not_done:
assumptions:
risks:
candidate_state_notice:
return_destination:
```

## Event Loop Closure

Closure must include emitted signals, handlers considered, child status, persistence proposal if any, acceptance need, and one primary next move.

## Terminal outcomes

- candidate_ready_for_acceptance_review
- repair_required
- blocked_context_request
- split_required
- stopped

## One-entity default

If the chat starts forming more than one steering entity, split or return a bounded sequence that preserves separate candidate/acceptance boundaries.

END_OF_FILE: workflow_v3/formation/STEERING_ENTITY_FORMATION_CHAT_PROTOCOL.md
