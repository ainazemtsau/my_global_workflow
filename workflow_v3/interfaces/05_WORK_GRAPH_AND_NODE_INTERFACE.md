# Work Graph and Node Interface

status: active_interface_layer

## Purpose

This interface defines the local Work Graph and node model under an Active Front.

## Work Graph

Work Graph is local to one Active Front.

Work Graph is derived from Front Exit Criteria, parent graph/map claims, and current evidence. It identifies bounded nodes, dependencies, local sequencing, and the next useful result inside the Active Front.

Work Graph is not:

- Direction Map;
- Direction Spine;
- roadmap;
- backlog;
- unreviewed task list;
- permanent graph for the whole Direction.

## Work Graph Node

A Work Graph Node must have:

- purpose;
- relation to Active Front, map area, and parent Goal Evidence Graph node or Direction Map claim when available;
- relation to parent;
- dependencies;
- boundaries;
- expected evidence;
- closure condition;
- current status;
- known blockers or uncertainties.

## Work Contract

One Work Contract may execute:

- one bounded Work Graph Node; or
- one bounded slice of a node when the node is too large.

The Work Contract must state target, parent_graph_node_ref, parent_front_ref, parent_work_graph_node_ref, relation_to_parent, source_authority, in_scope, out_of_scope, allowed_surfaces, forbidden_surfaces, expected_result, evidence_required, validation_required, return_destination, and stop_conditions.

Repository path boundaries are required only when repository/file mutation or inspection makes paths material.

## Node closure

When a node closes, a Node Closure summary is required.

The closure summary must include:

- node result;
- evidence links;
- acceptance decision or acceptance status;
- unresolved blockers;
- effects on Front Exit Criteria;
- whether Direction Map update is needed;
- next node/front candidate if any.

Node closure is not implicit from a chat answer, file existence, or Codex commit.

END_OF_FILE: workflow_v3/interfaces/05_WORK_GRAPH_AND_NODE_INTERFACE.md
