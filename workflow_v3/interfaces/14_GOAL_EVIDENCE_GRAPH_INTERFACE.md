# Goal Evidence Graph Interface

status: active_interface_layer

## Purpose

Goal Evidence Graph is a Direction Map-associated steering/control artifact that traces a Direction root outcome through claims, alternatives, obstacles, evidence requirements, and candidate work focus.

It helps select the Active Unresolved Cut and Active Front without converting the Direction into a roadmap, backlog, or task list.

## Non-primitive boundary

Goal Evidence Graph is not a semantic primitive.

It does not replace Direction Spine, Direction Map, Active Front, Work Graph, Work Contract, Evidence, or Acceptance Decision.

Graph existence does not accept graph claims, launch work, close a parent, mutate state, or create accepted Direction proof.

## Relation to Direction Map

Goal Evidence Graph may be embedded in `state/DIRECTION_MAP.md` or stored as an associated split file after a future accepted runtime package.

Direction Map remains the structural map. Goal Evidence Graph is the evidence/control projection that explains:

- required claims;
- alternative paths;
- obstacles and blockers;
- evidence gaps;
- candidate Active Unresolved Cuts;
- candidate fronts;
- relation from local work to root outcome.

## Minimal graph schema

```text
graph_id:
direction_id:
source_spine_ref:
direction_map_ref:
root_outcome_ref:
success_dimensions:
nodes:
active_paths:
active_unresolved_cut_ref:
evidence_index_ref:
decision_index_ref:
status:
limitations:
```

## Goal Evidence Node schema

```text
node_id:
node_type:
statement:
status:
parent_refs:
relation_to_parent:
source_refs:
evidence_required:
evidence_refs:
open_questions:
blockers:
success_dimensions_touched:
acceptance_policy:
next_action_hint:
```

## relation_to_parent values

- `AND_REQUIRED`
- `OR_STRATEGY`
- `ENABLES`
- `BLOCKS`
- `DE_RISKS`
- `VALIDATES`
- `OBSERVES`
- `PRODUCES`
- `CONSTRAINS`
- `INVALIDATES`

## Node statuses

- `candidate`
- `admitted`
- `active`
- `satisfied`
- `partial`
- `blocked`
- `invalidated`
- `superseded`
- `stale`

## Active Unresolved Cut

Active Unresolved Cut is the selected frontier of unresolved graph nodes whose resolution would materially advance, de-risk, unblock, validate, or invalidate the root outcome path.

It is a selection mechanism for Active Front formation. It is not a Work Graph, backlog, roadmap, launch packet, or accepted state by itself.

## Quality Checks

- Graph structure traces root outcome to claims, evidence, obstacles, alternatives, gaps, and candidate focus.
- Every material node has relation_to_parent and status; AND-required and OR-strategy relationships are visible.
- Active Unresolved Cut derives from unresolved root-path nodes and does not make the whole Direction active.
- Candidate fronts trace to cut, graph nodes, or map claims and preserve accepted/candidate/unresolved boundaries.

## Hard rules

- No work may proceed without trace to a Goal Evidence Graph node, Active Front, Work Graph node, or Direction Map claim.
- No parent closure may be claimed without required child/work evidence or an explicit missing-evidence block.
- Graph output is candidate until accepted through the explicit acceptance/update path.
- Goal Evidence Graph must not drift into roadmap, backlog, task list, or global Work Graph.
- Active Unresolved Cut must not make the whole Direction active.

END_OF_FILE: workflow_v3/interfaces/14_GOAL_EVIDENCE_GRAPH_INTERFACE.md
