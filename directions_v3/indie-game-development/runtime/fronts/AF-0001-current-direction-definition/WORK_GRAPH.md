# Work Graph

status: active
front_id: AF-0001-current-direction-definition
direction_id: indie-game-development
graph_scope: local_active_front
adoption_mode: clean_start
legacy_import: none

## Graph Boundary

This Work Graph is local to the Active Front. It is not a full Direction backlog and does not import old Direction state.

## Nodes

| Node ID | Status | Depends On | Result |
| --- | --- | --- | --- |
| N-0001-current-human-decision | pending_current_human_decision | none | Current product root result and success conditions are supplied by the human. |
| N-0002-draft-direction-spine | blocked_by_N-0001 | N-0001-current-human-decision | Candidate Direction Spine is drafted from current human decision. |
| N-0003-accept-direction-spine | blocked_by_N-0002 | N-0002-draft-direction-spine | Explicit acceptance/update path records accepted Direction Spine state. |
| N-0004-select-next-active-front | blocked_by_N-0003 | N-0003-accept-direction-spine | Next Active Front is selected after Direction Spine acceptance. |

## Current Next Node

current_next_node: N-0001-current-human-decision

next move: define current Direction Spine from current human decision

## Legacy Boundary

Old directions/indie-game-development/** files are legacy_evidence only.

END_OF_FILE: directions_v3/indie-game-development/runtime/fronts/AF-0001-current-direction-definition/WORK_GRAPH.md
