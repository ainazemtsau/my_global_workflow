# 08 Direction Map - Solo Max Productive

```yaml
artifact_control:
  artifact_name: "08 Direction Map - Solo Max Productive"
  schema: direction_map.v1
  owner_layer: persistence
  status: projection
  repo_path: "directions/solo-max-productive/project_files/08_DIRECTION_MAP.md"
  default_load: yes
  freshness: fresh
  last_updated: "2026-05-19"
```

## Purpose

Compact strategic routing context for the Direction's current initiative, active front, horizon slice, and map-linked Phase/Goal selection.

This file does not replace:

- `01_DIRECTION_STATE.md`
- `02_CURRENT_PHASE.md`
- `04_ACTIVE_GOAL.md`
- `05_PORTFOLIO_QUEUE.md`
- `06_CONTEXT_LIBRARY_INDEX.md`
- `07_PHASE_MEMORY_INDEX.md`

It should stay compact. It is not a calendar roadmap, backlog, implementation plan, architecture document, stack decision, or product execution graph.

## Direction map status

```yaml
direction_map_status:
  map_state: initialized
  current_initiative_id: INIT-EXOCORTEX-PERSISTENT-PERSONAL-AI-BRAIN
  map_confidence: medium
  last_reviewed_stage: M0_DIRECTION_MAP
  last_reviewed_at: "2026-05-18"
  migration_status: migrated_from_uninitialized_stub
  objective_architecture_migration_at: "2026-05-19"
  source_commit_from_launch_bundle: "06a7b20cf23bcb632f1d47ede18d44f740737fe6"
  migration_inputs_used:
    - project_files/00_DIRECTION_START_HERE.md
    - project_files/01_DIRECTION_STATE.md
    - project_files/02_CURRENT_PHASE.md
    - project_files/03_FOCUS_REGISTER.md
    - project_files/04_ACTIVE_GOAL.md
    - project_files/05_PORTFOLIO_QUEUE.md
    - project_files/06_CONTEXT_LIBRARY_INDEX.md
    - project_files/07_PHASE_MEMORY_INDEX.md
    - project_files/08_DIRECTION_MAP.md
    - user_provided_current_initiative_or_strategic_objective
    - codex_verified_m0_migration_launch_bundle
  update_policy: "M0 owns shared map review/update; R1/P9/parent synthesis may propose controlled map deltas; branch chats emit delta proposals only."
```

## Direction Objective

```yaml
direction_objective:
  id: OBJ-EXOCORTEX-AI-BRAIN
  statement: >
    Build EXOCORTEX as a persistent personal AI brain / external-brain application
    that preserves memory, compiles context, uses tools and workspace surfaces,
    learns from outcomes, maintains Reality Alignment, and compounds with future
    LLM improvements.
  active_horizon:
    id: HORIZON-EXOCORTEX-CORE-FOUNDATION
    statement: >
      Active Horizon: Accepted EXOCORTEX Core Foundation exists.
    coverage:
      - memory/context persistence
      - model interoperability
      - tools/actions extensibility
      - interaction/process loops
      - workspace surfaces
      - learning from outcomes
      - Reality Alignment
      - first buildable foundation boundary
```

## Current Initiative

```yaml
current_initiative:
  id: INIT-EXOCORTEX-PERSISTENT-PERSONAL-AI-BRAIN
  title: EXOCORTEX Persistent Personal AI Brain
  status: active
  intent: >
    Build EXOCORTEX as the persistent personal AI brain / external-brain application
    described by the Direction Objective.
  why_now: >
    The Direction Map is initialized and the accepted migration target is EXOCORTEX
    Core Foundation. The immediate constraint is converting the large vision into
    a bounded foundation before architecture, stack choice, product execution, or
    broad roadmap work.
  success_signal: >
    A reviewed EXOCORTEX Core Foundation Definition exists and is accepted through
    the normal Goal lifecycle. It defines core substrate, memory/context persistence,
    model interoperability, tools/actions extensibility, interaction/process loops,
    workspace surfaces, learning from outcomes, Reality Alignment, first buildable
    foundation boundary, non-goals, and validation criteria.
```

## Initiative Registry

```yaml
initiative_registry:
  - id: INIT-EXOCORTEX-PERSISTENT-PERSONAL-AI-BRAIN
    title: EXOCORTEX Persistent Personal AI Brain
    status: active
    phase_binding:
      current_phase: EXOCORTEX App Foundation
      current_phase_path: directions/solo-max-productive/phases/personal-workflow-app-kernel-exploration
    current_front_node: NODE-DEFINE-CORE-FOUNDATION
    current_goal_node: GOAL-G1-EXOCORTEX-PRODUCT-FOUNDATION
    success_signal: reviewed_exocortex_core_foundation_definition
    horizon: HORIZON-EXOCORTEX-CORE-FOUNDATION
```

## Strategy Basis

```yaml
strategy_basis:
  map_generation_mode: m0_migration_from_project_files_and_user_objective
  strategic_question: >
    What is the shortest credible path from the broad EXOCORTEX personal-brain vision
    to a bounded, reviewable Core Foundation that can guide the next Goal without
    drifting into implementation, stack, architecture, or broad roadmap work?
  optimization_criteria:
    - shortest_credible_path
    - constraint_removal
    - evidence_value
    - scope_minimization
    - reversibility
    - human_burden_minimization
  candidate_paths_considered:
    - id: PATH-FOUNDATION-FIRST
      title: Shape EXOCORTEX Core Foundation through the existing Product Foundation candidate
      verdict: selected
      rationale: >
        Directly removes the current bottleneck and matches the active Phase closure contract.
    - id: PATH-ARCHITECTURE-FIRST
      title: Technical architecture map before Core Foundation
      verdict: rejected_now
      rationale: >
        Premature; architecture is optional and deferred until foundation is accepted or
        a phase-progress decision explicitly continues.
    - id: PATH-STACK-FIRST
      title: Technology stack shortlist before Core Foundation
      verdict: rejected_now
      rationale: >
        Premature; stack choice depends on accepted foundation and validation criteria.
    - id: PATH-PROTOTYPE-FIRST
      title: Event Ledger, memory model, or UI prototype first
      verdict: parked
      rationale: >
        Potentially useful later, but currently out of scope and likely to create rabbit-hole work.
    - id: PATH-RESEARCH-FIRST
      title: Broad external research sweep before foundation
      verdict: parked
      rationale: >
        No explicit external evidence gap blocks map migration. Research should be targeted
        only when G1 exposes a concrete decision/evidence gap.
    - id: PATH-OLD-KERNEL-PROOF
      title: Continue old Personal Workflow App Kernel Min Proof
      verdict: rejected
      rationale: >
        Superseded provenance only; not executable unless explicitly reactivated through
        a later Human Decision.
    - id: PATH-FULL-ROADMAP
      title: Build full roadmap/backlog for EXOCORTEX
      verdict: rejected
      rationale: >
        Violates current constraints. The map is a compact strategic routing context,
        not a calendar roadmap or backlog.
  selected_path_rationale: >
    The shortest credible path is to route the initialized map to G1_GOAL_SHAPE for
    the existing EXOCORTEX Product Foundation Definition candidate, clarified as
    EXOCORTEX Core Foundation Definition. This maximizes evidence value while
    minimizing irreversible planning, product execution, and human review burden.
  major_assumptions:
    - >
      User-provided strategic objective is valid as human input but must be shaped
      against current Direction state rather than treated as automatic accepted canon.
    - >
      Full EXOCORTEX source material is required for G1 Core Foundation shaping, but the M0
      map can rely on current Project Files plus the Codex-verified launch bundle summary
      without producing the foundation itself.
    - >
      No safely backfilled closed Phase memory is available, so no closed-phase lessons
      are inferred.
  scope_cuts:
    - app implementation
    - tech stack choice
    - full architecture
    - Task Master graph
    - Codex product/project execution
    - broad product roadmap
    - UI mockups
    - Event Ledger prototype
    - memory model prototype
    - external research sweep without explicit evidence gap
    - old kernel-proof Goal execution
```

## Compact Initiative Graph

```yaml
compact_initiative_graph:
  nodes:
    - id: OBJ-EXOCORTEX-AI-BRAIN
      type: objective
      title: EXOCORTEX persistent personal AI brain / external-brain application
      status: accepted
      role: direction_objective
    - id: INIT-EXOCORTEX-PERSISTENT-PERSONAL-AI-BRAIN
      type: initiative
      title: EXOCORTEX Persistent Personal AI Brain
      status: active
      role: objective_carrier
    - id: HORIZON-EXOCORTEX-CORE-FOUNDATION
      type: horizon
      title: EXOCORTEX Core Foundation
      status: accepted
      role: active_horizon
    - id: NODE-DEFINE-CORE-FOUNDATION
      type: frontier_node
      title: Define EXOCORTEX Core Foundation
      status: ready
      role: selected_frontier_node
      stage_binding: G1_GOAL_SHAPE
    - id: GOAL-G1-EXOCORTEX-PRODUCT-FOUNDATION
      type: goal_candidate_node
      title: EXOCORTEX Product Foundation Definition
      status: active_front_primary
      role: existing_goal_candidate_for_core_foundation_definition
      candidate_id: G1-CAND-2026-05-13-EXOCORTEX-PRODUCT-FOUNDATION
      candidate_title_compatibility: EXOCORTEX Product Foundation Definition
      clarified_meaning: EXOCORTEX Core Foundation Definition
      stage_binding: G1_GOAL_SHAPE
    - id: REVIEW-R1-FOUNDATION-AND-PHASE-GATE
      type: review_gate_node
      title: Review foundation and run phase-progress gate
      status: blocked_until_goal_output_exists
      role: decide_close_continue_or_human_decision_after_foundation
    - id: DECISION-FIRST-BUILDABLE-FOUNDATION-BOUNDARY
      type: decision_boundary_node
      title: First buildable foundation boundary
      status: blocked_until_core_foundation_accepted
      role: decide first buildable boundary after accepted Core Foundation
    - id: PARKED-EXPANSIONS
      type: parked_node_group
      title: Parked expansions
      status: parked
      role: architecture_stack_prototypes_research_product_execution_and_full_app_are_not_current_scope
  edges:
    - from: OBJ-EXOCORTEX-AI-BRAIN
      to: INIT-EXOCORTEX-PERSISTENT-PERSONAL-AI-BRAIN
      relation: drives
    - from: INIT-EXOCORTEX-PERSISTENT-PERSONAL-AI-BRAIN
      to: HORIZON-EXOCORTEX-CORE-FOUNDATION
      relation: selects_active_horizon
    - from: HORIZON-EXOCORTEX-CORE-FOUNDATION
      to: NODE-DEFINE-CORE-FOUNDATION
      relation: requires_definition
    - from: NODE-DEFINE-CORE-FOUNDATION
      to: GOAL-G1-EXOCORTEX-PRODUCT-FOUNDATION
      relation: maps_to_existing_goal_candidate
    - from: GOAL-G1-EXOCORTEX-PRODUCT-FOUNDATION
      to: REVIEW-R1-FOUNDATION-AND-PHASE-GATE
      relation: requires_review_before_expansion
    - from: REVIEW-R1-FOUNDATION-AND-PHASE-GATE
      to: DECISION-FIRST-BUILDABLE-FOUNDATION-BOUNDARY
      relation: enables_boundary_decision_after_accepted_foundation
    - from: DECISION-FIRST-BUILDABLE-FOUNDATION-BOUNDARY
      to: PARKED-EXPANSIONS
      relation: may_unpark_specific_expansion_after_later_route
```

## Active Front

```yaml
active_front:
  primary_node: NODE-DEFINE-CORE-FOUNDATION
  mapped_goal_node: GOAL-G1-EXOCORTEX-PRODUCT-FOUNDATION
  mapped_goal_candidate_id: G1-CAND-2026-05-13-EXOCORTEX-PRODUCT-FOUNDATION
  primary_stage_binding: G1_GOAL_SHAPE
  active_front_statement: >
    Shape EXOCORTEX Core Foundation through the existing EXOCORTEX Product Foundation
    Definition candidate. Define WHAT / WHY / DONE for the core substrate before HOW,
    architecture, stack, prototypes, or Codex product execution.
  parallel_candidate_nodes: []
  parallel_policy: >
    No parallel workstreams before the foundation is stable. Parallel research,
    audit, or prototype work can be considered only after G1 exposes specific
    evidence gaps or after a phase-progress decision continues the Phase.
  parked_nodes:
    - PARKED-EXPANSIONS
```

## Horizon Slice

```yaml
horizon_slice:
  statement: >
    Reach one reviewed EXOCORTEX Core Foundation Definition and then make a
    phase-progress decision. Do not move into architecture, stack, implementation,
    prototypes, full roadmap, or Codex product execution until that foundation is
    accepted or a specific evidence gap is identified.
  node_ids:
    - HORIZON-EXOCORTEX-CORE-FOUNDATION
    - NODE-DEFINE-CORE-FOUNDATION
    - GOAL-G1-EXOCORTEX-PRODUCT-FOUNDATION
    - REVIEW-R1-FOUNDATION-AND-PHASE-GATE
  exit_condition: >
    Foundation definition reviewed; phase-progress gate decides P9_PHASE_CLOSE,
    continuation, Human Decision, or targeted next route.
```

## Parked / Future Nodes

```yaml
parked_future_nodes:
  - id: PARKED-EXPANSIONS
    title: Parked expansions
    status: parked
    contains:
      - EXOCORTEX technical architecture map
      - tech stack shortlist
      - implementation spike
      - UI/workspace mockup
      - Event Ledger prototype
      - memory model prototype
      - external research on current AI app infrastructure
      - Codex / Task Master / product execution graph
      - full EXOCORTEX application / personal external brain
    unpark_trigger: >
      A later accepted Core Foundation, phase-progress decision, or explicit evidence
      gap selects one expansion through the correct workflow route.
```

## Next Action Proof

```yaml
next_action_proof:
  proposed_stage_after_migration_repair: G1_GOAL_SHAPE
  selected_frontier_node: NODE-DEFINE-CORE-FOUNDATION
  mapped_goal_node: GOAL-G1-EXOCORTEX-PRODUCT-FOUNDATION
  mapped_goal_candidate_id: G1-CAND-2026-05-13-EXOCORTEX-PRODUCT-FOUNDATION
  basis_valid: true
  route_valid: true
  launch_allowed: false
  launch_blockers:
    - exact G1_GOAL_SHAPE prompt unavailable in current run
    - EXOCORTEX_CONCEPT_SEED_FULL.md required
    - Project Files refresh required after this patch
```

## Map Update Policy

```yaml
map_update_policy:
  branch_chats_may_mutate_map: false
  allowed_mutation_points:
    - M0_DIRECTION_MAP
    - R1_GOAL_REVIEW_DISTILL
    - P9_PHASE_CLOSE
    - parent_synthesis_after_parallel_branches
  update_triggers:
    - accepted_or_rejected_EXOCORTEX_Core_Foundation_Definition
    - phase_progress_gate_decision_after_foundation_review
    - human_decision_changes_current_initiative
    - concrete_evidence_gap_requires_research_or_audit_route
    - accepted_goal_result_changes_active_front_or_horizon
  forbidden_behavior:
    - branch_chat_direct_map_mutation
    - backlog_expansion_without_active_front_reason
    - calendar_roadmap_creation
    - replacing_phase_or_goal_state
    - treating_EXOCORTEX_CONCEPT_SEED_FULL_as_implementation_roadmap
    - starting_app_implementation_from_map
    - choosing_tech_stack_from_map
    - designing_full_architecture_from_map
```

## End-of-file marker

`END_OF_FILE: directions/solo-max-productive/project_files/08_DIRECTION_MAP.md`
