# Direction Structure Interface

status: active_interface_layer

## Purpose

This interface defines Direction as the long-lived runtime state system for Workflow v3.

## Direction is not just a file

A Direction is a long-lived project/result system with canonical state, evidence, acceptance records, operational surfaces, and adapter handoffs after adoption.

A Direction is not:

- a single markdown file;
- a chat thread;
- a Project Files/Sources upload;
- a roadmap;
- a backlog;
- a Codex branch;
- old Direction proof state by implication.

No chat may invent Direction state. When Direction state matters, use exact repository sources and accepted records.

## Object hierarchy

The structural object hierarchy is:

```text
Direction Spine -> Direction Map -> Active Front -> Work Graph -> Work Contract
```

Direction Spine is the stable axis: root result, success conditions, spine points, and tracks.

Direction Map is the global structural map between the Spine and the currently selected Active Front.

Active Front is the accepted current focus selected from the Direction Map.

Work Graph is local execution structure under one Active Front.

Work Contract is one bounded execution agreement for a node or node slice.

## Operational movement

The operational movement is:

```text
Procedure output -> FINISH_PACKET -> Result Packet -> Next Move Packet -> Transfer Packet if needed -> Acceptance/update path
```

Operational movement does not replace object hierarchy. Procedure output cannot mutate the Spine, Map, Active Front, Work Graph, or accepted state by itself.

## Movement rules

- Direction Spine changes only through an explicit acceptance/update path.
- Direction Map changes only through an explicit acceptance/update path.
- Active Front selection must reference Direction Map areas.
- Work Graph is derived from the accepted Active Front and Front Exit Criteria.
- Work Contract scope must stay bounded to one node or bounded node slice.
- Chat intuition does not choose route, front, or next material target.
- Adapter output is candidate until verified and accepted.

END_OF_FILE: workflow_v3/interfaces/01_DIRECTION_STRUCTURE_INTERFACE.md
