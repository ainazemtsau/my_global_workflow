# Goal Evidence Graph Eval

status: active_eval

## Purpose

Validate Goal Evidence Graph structure and its boundary from Direction Map, Work Graph, backlog, and accepted state.

## PASS checks

- Graph traces root outcome to claims, evidence requirements, obstacles, alternatives, and evidence gaps.
- Nodes have `relation_to_parent` and status.
- OR alternatives and AND-required paths are visible.
- No roadmap, backlog, task-list, or global Work Graph drift appears.
- Accepted/candidate boundaries are visible.
- Evidence requirements and evidence refs are visible.

## WARN checks

- Some nodes are unresolved or hypothetical, but labels and evidence needs are explicit.
- Graph is embedded in Direction Map instead of split, and the relationship is clear.

## FAIL checks

- Work lacks parent trace.
- Graph claims are treated as accepted by existence.
- OR/AND alternatives are unclear.
- Graph becomes a roadmap, backlog, or task list.

## Required recovery/repair action

Block continuation, restore claim/status/source labels, and require Direction Map or acceptance/update repair before stateful use.

END_OF_FILE: workflow_v3/evals/GOAL_EVIDENCE_GRAPH_EVAL.md
