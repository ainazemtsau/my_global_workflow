# Parent Integration and Impact Interface

status: active_interface_layer

## Purpose

This interface defines the parent integration and impact propagation boundary for returned work, dependency results, graph deltas, upstream escalation, downstream deltas, and derived gate checks.

## Parent integration boundary

Parent Integration compares returned dependency/work outputs and evidence against the parent target criteria.

The parent target may be a Work Graph node, Active Front, Direction Map claim, or Goal Evidence Graph node.

Parent Integration may synthesize a candidate decision, repair need, local replan, closure candidate, Graph Delta, Upstream Escalation Packet, Downstream Delta Packet, Derived Gate Check, or NEXT_CHAT_CARD.

It does not accept state, invent missing evidence, mutate graph/state, or launch next work by itself.

## Fan-in rule

When parent closure depends on multiple required dependency/work results, all required results must be accounted for before synthesis.

Each required input must be classified as present, missing, conflicting, blocked, deferred by explicit parent policy, or no longer required by accepted parent change.

## Missing required dependency blocks synthesis

If a required dependency/work result is missing, Parent Integration must block closure synthesis unless the parent acceptance policy explicitly allows partial closure.

Missing evidence must be named. It must not be replaced with inference, confidence, chat memory, or producer self-approval.

## Graph Delta semantics

Graph Delta is a candidate record describing proposed changes to Goal Evidence Graph nodes, statuses, relations, or evidence links.

Graph Delta may propose candidate status updates. It does not mutate accepted state until accepted through the explicit acceptance/update path.

## Upstream Escalation semantics

Upstream Escalation Packet carries a problem from a lower layer to the lowest parent layer that must decide it.

Use it when local repair cannot absorb the issue because parent acceptance policy, root claim, interface boundary, or higher Direction route may be affected.

## Downstream Delta semantics

Downstream Delta Packet carries an accepted or candidate parent-context change to affected dependency/work surfaces.

Affected work must pause, repair, replan, continue with new constraints, or close according to the packet. It must not keep executing against stale parent context.

## Impact radius levels

- `work_contract`
- `work_graph`
- `active_front`
- `direction_map`
- `direction_spine`

## Lowest absorbing layer rule

Repair locally at the lowest layer that can absorb the change without altering parent acceptance policy, higher claims, interface dependencies, or accepted Direction meaning.

Escalate only when the local layer cannot absorb the issue or when evidence invalidates a higher claim.

## Mutation boundary

Parent Integration Result, Graph Delta, Upstream Escalation Packet, Downstream Delta Packet, and Derived Gate Check are typed outputs/records.

They do not mutate accepted state, accept evidence, launch work, or change route by existence alone.

END_OF_FILE: workflow_v3/interfaces/15_PARENT_INTEGRATION_AND_IMPACT_INTERFACE.md
