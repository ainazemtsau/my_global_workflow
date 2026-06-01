# Focus and Waste Cut Protocol

status: active_focus_waste_cut_protocol

## Purpose

Use this protocol when selecting focus, opening Work Graphs, forming Work Contracts, or choosing Current Next Move.

## Bottleneck or constraint check

Ask what currently constrains progress toward the Direction or current Active Front.

Candidate work should either reduce the main constraint, answer a critical uncertainty, unlock a dependency, or provide evidence needed for an acceptance decision.

## Value check

Each included item must change one of:

- evidence;
- acceptance;
- closure;
- next decision;
- dependency state;
- risk visibility.

If it changes none of these, cut or defer it.

## Scope cut

Remove work outside the current steering entity, Active Front, Work Graph, Work Contract, or accepted Next Move.

Do not turn Work Graph into roadmap, Direction Map into backlog, or Action Inbox into hidden plan.

## Proof path cut

Prefer the smallest path that can produce useful evidence or close the current decision.

Do not add completeness work unless it affects proof, acceptance, or an explicit dependency.

## Premature work detection

Flag:

- product work before Direction Definition;
- Work Graph before accepted Active Front;
- multiple independent Work Contracts in one contract;
- future backlog disguised as graph nodes;
- polish before evidence.

## Deferred work

Record deferred work explicitly with the reason it is not part of the current entity.

## Relation to Work Graph and Work Contract

Work Graph contains the minimum local node graph needed to close the Active Front.

Work Contract contains one bounded run target. If the target is compound, return `split_required` instead of widening the contract.

END_OF_FILE: workflow_v3/formation/FOCUS_AND_WASTE_CUT_PROTOCOL.md
