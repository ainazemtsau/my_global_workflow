# Entity Formation Canon

status: active_entity_formation_canon

## Canon

Formation is not template filling.

A template gives the candidate or accepted entity a shape. Formation decides whether the content is strong enough to become a candidate and what evidence, risks, alternatives, and next move must remain visible.

## Acceptance boundary

- Entity formation produces candidate entities by default.
- An accepted entity requires an explicit Acceptance Decision or accepted update path.
- User input is current human input or candidate context until accepted.
- Model agreement is not acceptance.
- Child research/check results are evidence inputs, not decisions.
- No adapter may accept its own output.

## Human input boundary

Human input may be normalized into Workflow v3 terms, but normalization must not create hidden agreement or hidden acceptance.

The user must not be forced into YAML. If structured output is needed, the model may produce it after understanding the user's natural-language input.

## Default formation scope

One steering entity per material formation chat is the default.

Combining entities is allowed only when a bounded launch packet explicitly admits it and the output still separates each entity's candidate, evidence, risks, cuts, acceptance question, closure, and next move.

## Required formation output shape

Every steering-entity formation returns:

```text
target_entity:
source_context_classification:
frame:
candidate_alternatives:
selection_criteria:
evidence_and_hypotheses:
selected_candidate_summary:
rejected_or_deferred_alternatives:
risk_and_contradiction_attack:
focus_and_waste_cuts:
source_read_limitations:
candidate_entity:
acceptance_question:
event_loop_closure:
exact_next_move_or_transition_packet:
```

## Stop rule

Stop with a Context Request when exact source authority is required and cannot be read, when the entity would need to be invented, or when acceptance is being implied instead of requested.

END_OF_FILE: workflow_v3/formation/ENTITY_FORMATION_CANON.md
