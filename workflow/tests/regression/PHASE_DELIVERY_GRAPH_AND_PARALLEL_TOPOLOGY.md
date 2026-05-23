# Phase Delivery Graph and Parallel Topology Regression Cases

Status: active regression
Workflow version: vNext-R
Source GitHub repository file: `workflow/tests/regression/PHASE_DELIVERY_GRAPH_AND_PARALLEL_TOPOLOGY.md`
Authority: GitHub repository canonical after file read-back / diff verification / commit verification.
Purpose: catch regressions where large Phases lose coherence across Goals, graph-bound routing is bypassed, branch/workstream outputs mutate parent state, or parallelism becomes unsafe/default.

```yaml
artifact_control:
  artifact_name: "Phase Delivery Graph and Parallel Topology Regression Cases"
  schema: workflow_regression_cases.v1
  owner_layer: validation
  status: active
  repo_path: "workflow/tests/regression/PHASE_DELIVERY_GRAPH_AND_PARALLEL_TOPOLOGY.md"
  freshness: refresh_when_phase_delivery_graph_parallel_topology_or_phase_progress_rules_change
```

## Purpose

This file catches regressions where:

- a large Phase loses coherence across multiple Goals;
- Goals are selected outside `phase_delivery_graph.v1`;
- support gates, research branches, or audit branches become required chains without graph basis;
- branch/workstream outputs mutate parent state or bypass parent synthesis;
- R1 accepts a Goal without `graph_delta` or `no_graph_delta_reason`;
- P9 closes from last-Goal optimism instead of graph Completion Logic + Evidence Ledger;
- parallelism is used without speed/quality benefit or acceptable safety;
- graph state becomes backlog, roadmap, WBS, calendar, or architecture dump;
- `maintenance_direct` governance mode is accidentally forced into normal lifecycle graph requirements.

## Authority references

- `workflow/runtime/OBJECTIVE_ARCHITECTURE_MODEL.md`: Phase Delivery Graph, Phase Graph Validity, Parallel Delivery Topology, `parallel_safety_gate`, Minimum Sufficient Solution Proof.
- `workflow/runtime/WF_VNEXT_R_RUNTIME_CORE.md`: Phase Progress Gate and Phase Closure Contract, Branch / Workstream Execution Topology, Parallel safety gate, Lifecycle State Reconciliation Gate, Compatibility / black-box stage rule.
- `workflow/stage_prompts/ROUTER_STAGE_LAUNCHER.md`
- `workflow/stage_prompts/P0_PHASE_START.md`
- `workflow/stage_prompts/G0_GOAL_SELECT.md`
- `workflow/stage_prompts/G1_GOAL_SHAPE.md`
- `workflow/stage_prompts/E1_EXECUTION_BRIEF.md`
- `workflow/stage_prompts/R1_GOAL_REVIEW_DISTILL.md`
- `workflow/stage_prompts/P9_PHASE_CLOSE.md`
- `workflow/stage_prompts/M0_DIRECTION_MAP.md`

## Scope / non-goals

- These are regression cases, not new runtime authority.
- This file does not override runtime, stage prompts, stage registry, transport schemas, or Direction Project Files.
- This file does not create new stage IDs.
- This file does not change `allowed_next`.
- This file does not require a new default Project File.
- This file does not mutate Direction state.
- This file must not turn Phase Delivery Graph into backlog/project-management doctrine.
- This file must not make parallelism the default workflow mode.

## Required case format

```yaml
case:
  id:
  name:
  setup:
  trigger:
  expected_result:
  must_not:
  authority_checks:
  pass_condition:
  fail_condition:
```

## Cases

```yaml
case:
  id: phase_with_8_goals_loses_coherence
  name: Large Phase stays coherent through graph-bound Goal selection
  setup:
    - Active Phase has one Direction-visible outcome.
    - phase_delivery_graph.v1 exists with multiple required and optional nodes.
    - Previous Goal completed and R1 accepted it.
    - Active Goal is none.
    - Several candidate Goals are plausible.
  trigger:
    - Router/G0 selects next Goal.
  expected_result:
    - Router/G0 uses phase_delivery_graph.v1 next_node or ready required node.
    - Optional/parked nodes remain parked unless activation trigger exists.
    - Next Goal binds to graph node and Phase outcome.
    - If graph is stale or contradictory, route to repair/M0/B1/Context Request/Human Decision/Stop.
  must_not:
    - Select next Goal solely from local plausibility.
    - Treat unresolved surfaces as automatic required Goals.
    - Expand graph into backlog/WBS.
  authority_checks:
    - Phase Delivery Graph
    - Phase Graph Validity
    - Router graph-aware routing
    - G0 graph node selection
  pass_condition:
    - Selected Goal has graph node binding and why_this_node_now.
    - Selected node is ready/required or admitted with activation basis.
  fail_condition:
    - Goal is selected outside graph without graph_delta/reframe/human decision.
```

```yaml
case:
  id: goal_selected_outside_phase_delivery_graph
  name: Outside-graph Goal requires graph repair or decision
  setup:
    - phase_delivery_graph.v1 exists.
    - User or assistant proposes a useful but outside-graph Goal.
    - Proposal does not include graph_delta, reframe, or human decision.
  trigger:
    - G0/G1 attempts to select/shape the Goal.
  expected_result:
    - Reject or route to graph repair, P0/R1/P9 repair, M0, B1, Context Request, Human Decision, or Stop.
    - Do not silently shape outside-graph Goal.
  must_not:
    - Treat usefulness as sufficient.
    - Bypass graph node selection.
  authority_checks:
    - Phase Graph Validity
    - G0 graph node selection
    - G1 Goal-to-node binding
  pass_condition:
    - outside_graph_candidate: true and graph_delta_needed_before_goal: true, or route away.
  fail_condition:
    - Goal Contract is shaped without graph binding or approved graph update.
```

```yaml
case:
  id: support_gate_becomes_required_goal_chain
  name: Support gates do not become default required Goal chains
  setup:
    - phase_delivery_graph has support_gate, research_gate, or audit_gate nodes.
    - One support gate completes.
    - Another support/research/audit gate is proposed as next required Goal.
  trigger:
    - R1/Router/G0 considers continuation.
  expected_result:
    - Continuation shows what the support node unlocks/proves for Phase outcome.
    - If it does not unlock/prove a required result condition, park/cut it.
    - Use Documentation Admission Test / Direction Value Anchor when documentation-shaped artifact is material.
  must_not:
    - Build support-gate chains by default.
    - Convert every readiness/check into required Goal.
  authority_checks:
    - Phase Graph Validity
    - Minimum Sufficient Solution Proof
    - Result-first support-artifact guard
  pass_condition:
    - Support/research/audit Goal is admitted only with graph basis and result unlock/proof.
  fail_condition:
    - Support-gate chain continues because the surface remains unresolved.
```

```yaml
case:
  id: branch_result_mutates_phase_state
  name: Branch result cannot mutate parent lifecycle state
  setup:
    - E1 creates parallel_workstreams or parallel_then_gated_synthesis.
    - Branch returns workstream_result_card with evidence and recommendations.
    - Branch suggests state update.
  trigger:
    - Parent receives branch result.
  expected_result:
    - Branch output is input to parent synthesis only.
    - Branch does not mutate Direction/Phase/Goal/Map/Project Files.
    - R1/P9 or approved parent synthesis owns state integration.
  must_not:
    - Let branch close parent Goal/Phase.
    - Let branch run parent R1 or phase_progress_gate.
    - Let branch emit parent-state repository patch.
  authority_checks:
    - Branch / Workstream Execution Topology
    - branch state policy
    - parent synthesis
  pass_condition:
    - state_policy_confirmation says no parent state mutation.
    - parent synthesis required before state update.
  fail_condition:
    - Branch output directly changes parent lifecycle state.
```

```yaml
case:
  id: r1_accepts_goal_without_graph_delta
  name: R1 acceptance includes graph_delta or explicit no_delta reason
  setup:
    - Parent Goal is accepted by R1.
    - Active Phase has phase_delivery_graph.v1.
    - Goal touched graph-bound work.
  trigger:
    - R1 produces review output.
  expected_result:
    - R1 emits phase_delivery_graph_delta or explicit no_graph_delta_reason.
    - Delta records completed_node_id, node_status_after, output_classification, evidence_added, closure predicates, optional parked nodes, next recommended node or closure candidate.
  must_not:
    - Accept Goal and route onward without graph implications.
    - Route to G0 just because Active Goal is none.
  authority_checks:
    - R1 graph_delta
    - Lifecycle State Reconciliation Gate
    - Phase Progress Gate
  pass_condition:
    - phase_delivery_graph_delta present or no_graph_delta_reason justified.
  fail_condition:
    - R1 acceptance lacks graph delta and still launches next material work.
```

```yaml
case:
  id: p9_closes_phase_from_last_goal_only
  name: P9 closes only by aggregate graph evidence
  setup:
    - Last Goal was successful.
    - Phase has phase_delivery_graph.v1 with required nodes, alternatives, and Evidence Ledger.
    - Some required evidence is missing or optional nodes remain parked.
  trigger:
    - P9 evaluates Phase closure.
  expected_result:
    - P9 runs phase_close_graph_check.
    - Closure depends on Completion Logic + Evidence Ledger + required nodes done/superseded.
    - Optional/parked nodes do not block closure.
    - Missing required evidence blocks closure or routes repair.
  must_not:
    - Close Phase because the latest Goal looked complete.
    - Keep optional parked work as blocker.
  authority_checks:
    - Phase Progress Gate and Phase Closure Contract
    - Completion Logic
    - Evidence Ledger
    - P9 aggregate graph closure
  pass_condition:
    - close_allowed matches aggregate graph evidence.
  fail_condition:
    - Phase closes or stays open from last-Goal optimism / optional-node confusion.
```

```yaml
case:
  id: parallel_write_conflict_without_safety_gate
  name: Parallel writers require safety gate and disjoint integration proof
  setup:
    - E1 considers parallel Codex worktrees/tasks or parallel writers.
    - Branches may touch shared mutable repository/product surfaces.
    - Disjoint paths/worktrees or integration order are not proven.
  trigger:
    - E1 selects execution topology.
  expected_result:
    - parallel_safety_gate fails.
    - Use sequential, gated_sequential, one-writer default, or review-only/read-only branches.
    - Parallel write-heavy work allowed only with disjoint paths/worktrees, integration order, validation after integration, and parent integrator.
  must_not:
    - Run multiple writers against shared mutable surfaces.
    - Treat Codex subagents as safe for write-heavy tasks by default.
  authority_checks:
    - Parallel Delivery Topology
    - parallel_safety_gate
    - one-writer default
  pass_condition:
    - repository_mutation: unsafe or disjoint proof missing -> parallel_allowed: false.
  fail_condition:
    - Parallel writers launch without path/worktree/integration proof.
```

```yaml
case:
  id: parallelism_requested_without_speed_or_quality_benefit
  name: Parallelism requires material speed or quality value
  setup:
    - User or assistant asks to parallelize.
    - Work could be done sequentially with similar speed/quality.
    - Coordination overhead is nontrivial.
  trigger:
    - E1 or planner evaluates parallel mode.
  expected_result:
    - parallel_safety_gate value_check rejects parallelism.
    - Simpler sequential option is selected.
  must_not:
    - Use parallelism because it seems systematic or impressive.
    - Increase coordination cost without material benefit.
  authority_checks:
    - Minimum Sufficient Solution Proof
    - parallel_safety_gate
    - Parallel Delivery Topology
  pass_condition:
    - expected_speedup_material or quality_improves_or_stays_same is proven; otherwise sequential.
  fail_condition:
    - Parallelism selected without benefit proof.
```

```yaml
case:
  id: codex_subagents_without_parent_synthesis
  name: Subagent and branch outputs require parent synthesis
  setup:
    - Codex subagents or ChatGPT branch chats are launched for read/review/audit/research.
    - Each returns compact result.
  trigger:
    - Parent chat receives outputs.
  expected_result:
    - Parent synthesis reads Workstream Result Cards first.
    - Material conflicts, missing branches, or insufficient synthesis readiness are handled explicitly.
    - Only parent synthesis/R1/P9 can update graph/state.
  must_not:
    - Average conflicting outputs silently.
    - Let subagent decide final parent-level decision.
    - Skip synthesis.
  authority_checks:
    - Branch / Workstream Execution Topology
    - parent synthesis
    - R1 branch result handling
  pass_condition:
    - parent_synthesis_decision exists before next material route.
  fail_condition:
    - Branch/subagent output becomes final decision without synthesis.
```

```yaml
case:
  id: graph_bloat_exceeds_compact_limit
  name: Phase graph stays compact or triggers reframe/split
  setup:
    - phase_delivery_graph grows beyond compact limits.
    - Many optional/future nodes or edges appear.
    - Graph starts becoming backlog/roadmap/WBS/calendar/architecture dump.
  trigger:
    - P0/R1/P9/M0 tries to update graph.
  expected_result:
    - Optional/future nodes grouped or parked.
    - If graph cannot stay compact, route to M0/P0/Human Decision for reframe/split.
    - Do not expand default Project Files into backlog.
  must_not:
    - Store detailed branch artifacts or reports in Project Files.
    - Add full architecture plan to graph.
  authority_checks:
    - Phase Delivery Graph compactness guards
    - Phase Graph Validity
    - M0 map-owner boundary
  pass_condition:
    - Graph stays compact or triggers reframe/split.
  fail_condition:
    - Graph becomes project-management artifact.
```

```yaml
case:
  id: governance_maintenance_direct_mode_not_broken
  name: Governance maintenance_direct mode does not require normal lifecycle graph
  setup:
    - Direction is Workflow Governance or another maintenance_direct container.
    - User requests workflow audit/repair/cleanup/repository maintenance.
    - Active Goal is none.
    - Normal lifecycle graph is absent.
  trigger:
    - Router or maintenance chat handles request.
  expected_result:
    - Maintenance Mode may proceed without P0/G0/G1 and without normal lifecycle Phase Delivery Graph seeding.
    - Use natural-language maintenance loop: inspect files -> findings/patch plan -> approval -> Codex apply/read-back -> validation -> refresh report.
    - If user explicitly asks for normal lifecycle operation, normal graph requirements may apply.
  must_not:
    - Force normal lifecycle graph seeding merely because Active Goal is none.
    - Break Workflow Governance maintenance_direct operation.
  authority_checks:
    - P0 maintenance_direct exception
    - Router graph-aware routing
    - Codex repository maintenance role separation
  pass_condition:
    - maintenance_direct exception respected.
  fail_condition:
    - Workflow governance maintenance request is blocked only because no normal phase_delivery_graph exists.
```

## Regression checklist

- One Direction-visible Phase outcome identified.
- `phase_delivery_graph.v1` or legacy `phase_work_map` handled.
- Selected Goal binds to one ready graph node.
- Optional/parked nodes remain nonblocking unless activated.
- Support/research/audit gates explain what they unlock/prove.
- Fallback nodes activate only by trigger.
- Graph bloat guard checked.
- One Active Goal preserved.
- branches/workstreams are not Active Goals.
- Parallelism admitted only by `parallel_safety_gate`.
- one-writer default preserved.
- Parent synthesis required before R1/P9/state update.
- R1 emits `graph_delta` or `no_graph_delta_reason`.
- P9 closes by Completion Logic + Evidence Ledger.
- M0 remains Direction Map owner, not routine graph owner.
- Transport schemas untouched.
- STAGE_REGISTRY `allowed_next` untouched.
- Direction state untouched by branch/workstream outputs.
- `maintenance_direct` exception considered where relevant.

## Read-back anchors

- "phase_with_8_goals_loses_coherence"
- "goal_selected_outside_phase_delivery_graph"
- "support_gate_becomes_required_goal_chain"
- "branch_result_mutates_phase_state"
- "r1_accepts_goal_without_graph_delta"
- "p9_closes_phase_from_last_goal_only"
- "parallel_write_conflict_without_safety_gate"
- "parallelism_requested_without_speed_or_quality_benefit"
- "codex_subagents_without_parent_synthesis"
- "graph_bloat_exceeds_compact_limit"
- "governance_maintenance_direct_mode_not_broken"
- "Phase Delivery Graph"
- "phase_delivery_graph.v1"
- "parallel_safety_gate"
- "one Active Goal"
- "branches/workstreams are not Active Goals"
- "parent synthesis"
- "one-writer default"
- "Completion Logic"
- "Evidence Ledger"
- "maintenance_direct"

## End-of-file marker

`END_OF_FILE: workflow/tests/regression/PHASE_DELIVERY_GRAPH_AND_PARALLEL_TOPOLOGY.md`
