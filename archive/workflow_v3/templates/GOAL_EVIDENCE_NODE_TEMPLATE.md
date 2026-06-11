# Goal Evidence Node Template

status: template

## Goal Evidence Node

`node_id`:

`node_type`:

`statement`:

`status`: candidate | admitted | active | satisfied | partial | blocked | invalidated | superseded | stale

`parent_refs`:

`relation_to_parent`: AND_REQUIRED | OR_STRATEGY | ENABLES | BLOCKS | DE_RISKS | VALIDATES | OBSERVES | PRODUCES | CONSTRAINS | INVALIDATES

`source_refs`:

`evidence_required`:

`evidence_refs`:

`open_questions`:

`blockers`:

`success_dimensions_touched`:

`acceptance_policy`:

`next_action_hint`:

## Boundary

Goal Evidence Node is a graph/control projection. It is not a Work Graph node unless a later accepted Work Graph explicitly derives local work from it.

Node status changes remain candidate until accepted through the explicit acceptance/update path.

END_OF_FILE: workflow_v3/templates/GOAL_EVIDENCE_NODE_TEMPLATE.md
