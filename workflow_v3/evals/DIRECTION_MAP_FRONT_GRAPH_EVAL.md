# Direction Map, Active Front, and Work Graph Eval

status: active_repository_completion_framework

## Source files to inspect

- `workflow_v3/interfaces/02_DIRECTION_MAP_INTERFACE.md`
- `workflow_v3/interfaces/04_ACTIVE_FRONT_SELECTION_INTERFACE.md`
- `workflow_v3/interfaces/05_WORK_GRAPH_AND_NODE_INTERFACE.md`
- `workflow_v3/interfaces/14_GOAL_EVIDENCE_GRAPH_INTERFACE.md`
- `workflow_v3/templates/DIRECTION_MAP_TEMPLATE.md`
- `workflow_v3/templates/GOAL_EVIDENCE_GRAPH_TEMPLATE.md`
- `workflow_v3/templates/ACTIVE_UNRESOLVED_CUT_TEMPLATE.md`
- `workflow_v3/templates/ACTIVE_FRONT_TEMPLATE.md`
- `workflow_v3/templates/WORK_GRAPH_TEMPLATE.md`
- `workflow_v3/procedures/DIRECTION_MAP_FORMATION_PROCEDURE.md`
- `workflow_v3/procedures/ACTIVE_FRONT_FORMATION_PROCEDURE.md`
- `workflow_v3/procedures/WORK_GRAPH_FORMATION_PROCEDURE.md`

## Evidence required

- Direction Map with map areas, tracks, dependencies, uncertainties, evidence links, and labels;
- Goal Evidence Graph or explicit reason it is not present;
- Active Unresolved Cut when graph exists;
- Active Front candidate with source map areas, touched tracks, why-now, selection evidence, rejected/deferred alternatives, exit criteria, and acceptance question;
- local Work Graph derived from Front Exit Criteria;
- acceptance/update status for any state change.

## PASS criteria

- Direction Map is present and distinct from Direction Spine.
- Direction Map is not roadmap, backlog, Work Graph, or unreviewed task list.
- Goal Evidence Graph remains a steering/control projection and not accepted state by existence.
- Active Unresolved Cut derives from unresolved graph/root paths when graph exists.
- Active Front selection cites map areas, touched tracks, why-now, evidence, alternatives, exit criteria, and acceptance question.
- Work Graph is local to one Active Front, contains bounded nodes, and preserves parent graph/map/front trace.

## WARN criteria

- Map has candidate or unresolved labels that need later evidence but are explicitly marked.
- Active Front candidate is valid but awaits human acceptance.
- Work Graph opening is deferred because exit criteria need repair.

## FAIL criteria

- Direction Map missing or flattened into Direction Spine.
- Direction Map used as roadmap/backlog.
- Work Graph inflated into roadmap/backlog/global map.
- Active Front selected without map areas/evidence.
- Active Front selected without Active Unresolved Cut when graph context exists.
- Work Graph Node is arbitrary TODO without boundaries/evidence/closure condition.

## Common failure modes

- Treating all active work as Active Front.
- Treating unreviewed task-list candidates as map areas.
- Selecting front by chat intuition.

## Required recovery/repair action

Block continuation, restore the missing distinct surface, rerun the appropriate procedure, and require acceptance/update before any state mutation.

END_OF_FILE: workflow_v3/evals/DIRECTION_MAP_FRONT_GRAPH_EVAL.md
