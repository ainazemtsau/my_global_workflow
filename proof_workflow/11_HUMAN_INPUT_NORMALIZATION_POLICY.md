---
artifact_control:
  namespace: proof_workflow
  artifact_type: human_input_normalization_policy
  status: gate_2_3_initial
  owner: proof_carrying_workflow_os
---

# Human Input Normalization Policy

## Purpose

Human Input Normalization converts clear natural-language human intent into structured workflow fields when it is safe to do so.

Human Input Normalization is a runtime policy, not a semantic primitive.

User input may be terse, informal, voice-transcribed, incomplete, or unstructured.

The workflow must normalize clear human intent into structured fields when safe.

User must not be required to answer in YAML or schema format.

## Option Selection Rule

If a Human Decision Card presents options with `option_id` values, a reply like `B`, `Decision B`, `беру B`, `второй вариант`, or equivalent counts as selecting option B when unambiguous.

If a selected option has enough content to define the decision, the Operator should create a Receipt with verdict `satisfied` or `partial_success_with_residuals`, not `needs_input`.

## Default Completion Policy

If `success_semantics` are not explicitly supplied, the default may be:

```yaml
success_semantics: delegate_to_child_obligation
```

This default is allowed only when the target Obligation allows delegation.

If constraints are not explicitly supplied, classify constraints from the selected option:

```yaml
constraints:
  accepted: constraints explicitly chosen by the selected option
  candidate: details implied but not decided
  unknown: missing specifics
```

Residual Obligations should be opened for genuinely unresolved future work.

## Follow-Up Threshold

Ask a follow-up question only if:

- user intent is ambiguous
- multiple options match
- the selected option lacks enough content
- a high-impact constraint would be accepted silently
- the default would violate an invariant

## Context Authority Preservation

Human input normalization must preserve Context Authority.

It may turn `current_human_input` into a candidate Receipt.

It must not treat prior `candidate_context` as accepted unless the user selected or accepted it.

## No Hidden Acceptance

Human Input Normalization must not create hidden acceptance.

Normalization may:

- identify the selected option from terse input
- copy the selected option's already-visible text into the interpreted decision
- apply safe procedural defaults that do not accept substantive claims, such as delegating `success_semantics` to a child Obligation when allowed
- classify unresolved details as candidate or unknown
- create residual Obligations

Normalization must not:

- accept substantive claims that were not explicit in the selected option or current human input
- silently add revenue targets, platform, engine, genre, timeline, visual style, launch strategy, or execution scope
- convert `candidate_context` into accepted constraints without explicit human acceptance
- hide defaults from the Receipt
- return verdict `satisfied` when material ambiguity remains about what the user accepted

Every normalized Receipt must include:

- `raw_user_input_ref`
- `interpreted_decision`
- `selected_option_id` if applicable
- `selected_option_text` if applicable
- `defaults_applied`
- `fields_not_accepted`
- `residual_obligations`
- `ambiguity_remaining`

If a field is defaulted only to avoid burden, the default may only preserve openness, delegate to child Obligation, or classify as unknown/candidate. It must not create accepted domain content.

## Examples

### Example 1: Terse Option Choice

Human Decision Card options A/B/C/D.

User says: `Decision B`.

Result:

```yaml
selected_option: B
human_input_normalized: true
success_semantics: delegate_to_child_obligation by default if allowed
constraints: option B accepted/candidate/unknown classification
receipt_verdict: satisfied if root objective is clear
```

### Example 2: Messy Voice Input

User voice input is long and messy but clearly chooses option B.

Result:

- summarize interpreted decision
- ask for confirmation only if material ambiguity remains

### Example 3: Informal Constraint Acceptance

User says: `давай co-op gas`.

Result:

- classify as `current_human_input`
- accept co-op/gas as a constraint only if context makes it clearly related to the active Human Decision
- record the accepted text, defaults, and unresolved details in the Receipt

END_OF_FILE: proof_workflow/11_HUMAN_INPUT_NORMALIZATION_POLICY.md
