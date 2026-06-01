# Evidence and Hypothesis Protocol

status: active_evidence_hypothesis_protocol

## Purpose

Use this protocol to keep candidate steering entities evidence-aware without pretending uncertainty has been resolved.

## Core terms

`hypothesis`: a testable claim that may guide the entity but is not yet proven.

`assumption`: a dependency accepted only for the current reasoning scope.

`proof_signal`: an observable result that would support the claim.

`evidence_class`: accepted record, verified repository source, current human input, run evidence, check finding, legacy_evidence, candidate context, or unknown.

`cheapest_useful_test`: the smallest bounded check or run that can change the decision.

`failure_condition`: what would make the candidate wrong, unsafe, or not worth continuing.

`enough_for_now`: the explicit threshold for proceeding as candidate without pretending final proof exists.

## Labels

Use these labels where claims are not uniformly accepted:

- `validated`
- `candidate`
- `unresolved`
- `hypothetical`

## Required evidence summary

```text
accepted_evidence:
current_human_input:
candidate_context:
hypotheses:
assumptions:
proof_signals:
cheapest_useful_tests:
failure_conditions:
enough_for_now_threshold:
labels_used:
```

## Boundary

Evidence supports formation and acceptance, but evidence does not mutate accepted state by itself.

END_OF_FILE: workflow_v3/formation/EVIDENCE_AND_HYPOTHESIS_PROTOCOL.md
