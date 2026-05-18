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
  last_updated: "2026-05-18"
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
  current_initiative_id: INIT-2026-05-16-EXOCORTEX-PERSISTENT-AI-BRAIN
  map_confidence: medium
  last_reviewed_stage: M0_DIRECTION_MAP
  last_reviewed_at: "2026-05-18"
  migration_status: migrated_from_uninitialized_stub
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

## Current Initiative

```yaml
current_initiative:
  id: INIT-2026-05-16-EXOCORTEX-PERSISTENT-AI-BRAIN
  title: EXOCORTEX Persistent Personal AI Brain
  status: active
  intent: >
    Create a persistent personal AI companion/substrate that is not merely Q&A chat
    and not merely a temporary workflow replacement. EXOCORTEX should preserve memory,
    compile context, use tools, operate or generate useful UI/workspace surfaces,
    learn from interaction outcomes, maintain Reality Alignment / anti-sycophancy
    mechanisms, and become stronger as future LLMs improve.
  why_now: >
    The active Phase has been repaired around EXOCORTEX App Foundation, but the
    Direction Map was still an uninitialized stub. The immediate constraint is to
    convert the large future-app vision into a bounded foundation before architecture,
    stack choice, product execution, or broad roadmap work.
  success_signal: >
    A reviewed EXOCORTEX Product Foundation Definition exists and is accepted or
    reviewed through the normal Goal lifecycle. It defines target system, principles,
    core loop, conceptual subsystem map, Max Vision vs Min Proof / buildable foundation
    boundary, non-goals, and validation criteria, and it enables a phase-progress
    decision about closing or continuing the current Phase.
```

## Initiative Registry

```yaml
initiative_registry:
  - id: INIT-2026-05-16-EXOCORTEX-PERSISTENT-AI-BRAIN
    title: EXOCORTEX Persistent Personal AI Brain
    status: active
    phase_binding:
      current_phase: EXOCORTEX App Foundation
      current_phase_path: directions/solo-max-productive/phases/personal-workflow-app-kernel-exploration
    current_front_node: G1-EXOCORTEX-PRODUCT-FOUNDATION
    success_signal: reviewed_exocortex_product_foundation_definition
    replacement_policy: >
      Current ChatGPT + GitHub + Codex workflow remains the construction workflow.
      EXOCORTEX should replace it only after radical superiority and sufficient readiness.
```

## Strategy Basis

```yaml
strategy_basis:
  map_generation_mode: m0_migration_from_project_files_and_user_objective
  strategic_question: >
    What is the shortest credible path from the broad EXOCORTEX personal-brain vision
    to a bounded, reviewable foundation that can guide the next Goal without drifting
    into implementation, stack, architecture, or broad roadmap work?
  optimization_criteria:
    - shortest_credible_path
    - constraint_removal
    - evidence_value
    - scope_minimization
    - reversibility
    - human_burden_minimization
  candidate_paths_considered:
    - id: PATH-FOUNDATION-FIRST
      title: Initialize map, then shape EXOCORTEX Product Foundation Definition
      verdict: selected
      rationale: >
        Directly removes the current bottleneck and matches the active Phase closure contract.
    - id: PATH-ARCHITECTURE-FIRST
      title: Technical architecture map before product foundation
      verdict: rejected_now
      rationale: >
        Premature; architecture is optional and deferred until foundation is accepted or
        a phase-progress decision explicitly continues.
    - id: PATH-STACK-FIRST
      title: Technology stack shortlist before product foundation
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
    The shortest credible path is to initialize the map around one Current Initiative
    and one Active Front, then route to G1_GOAL_SHAPE for the EXOCORTEX Product Foundation
    Definition. This maximizes evidence value while minimizing irreversible planning,
    product execution, and human review burden.
  major_assumptions:
    - >
      User-provided strategic objective is valid as human input but must be shaped
      against current Direction state rather than treated as automatic accepted canon.
    - >
      Full EXOCORTEX source material is required for G1 foundation shaping, but the M0
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
    - id: INIT-2026-05-16-EXOCORTEX-PERSISTENT-AI-BRAIN
      type: initiative
      title: EXOCORTEX Persistent Personal AI Brain
      status: active
      role: strategic_target
    - id: M0-MAP-INITIALIZATION
      type: map_node
      title: Initialize compact Direction Map
      status: formalized
      role: make_strategy_context_usable
    - id: G1-EXOCORTEX-PRODUCT-FOUNDATION
      type: goal_candidate_node
      title: EXOCORTEX Product Foundation Definition
      status: active_front_primary
      role: define_target_foundation_before_how
      stage_binding: G1_GOAL_SHAPE
    - id: R1-FOUNDATION-REVIEW-AND-PHASE-GATE
      type: review_gate_node
      title: Review foundation and run phase-progress gate
      status: horizon
      role: decide_close_continue_or_human_decision_after_foundation
    - id: MIN-PROOF-BOUNDARY
      type: decision_boundary_node
      title: First buildable foundation / Min Proof boundary
      status: gated_by_foundation
      role: decide what can be built or validated first after foundation
    - id: TECHNICAL-ARCHITECTURE-MAP
      type: parked_node
      title: EXOCORTEX technical architecture map
      status: parked
      role: optional_after_foundation_or_phase_continue_decision
    - id: TECH-STACK-SHORTLIST
      type: parked_node
      title: Tech stack shortlist
      status: parked
      role: optional_after_foundation_or_explicit_evidence_gap
    - id: PROTOTYPE-SPIKES
      type: parked_node
      title: Event Ledger / memory model / UI workspace prototype spikes
      status: parked
      role: optional_after_foundation_and_execution_route
    - id: FULL-EXOCORTEX-APPLICATION
      type: future_node
      title: Full EXOCORTEX application / personal external brain
      status: future
      role: max_vision_not_current_execution_scope
  edges:
    - from: INIT-2026-05-16-EXOCORTEX-PERSISTENT-AI-BRAIN
      to: M0-MAP-INITIALIZATION
      relation: requires_map_initialization
    - from: M0-MAP-INITIALIZATION
      to: G1-EXOCORTEX-PRODUCT-FOUNDATION
      relation: enables_next_goal_shape
    - from: G1-EXOCORTEX-PRODUCT-FOUNDATION
      to: R1-FOUNDATION-REVIEW-AND-PHASE-GATE
      relation: requires_review_before_expansion
    - from: G1-EXOCORTEX-PRODUCT-FOUNDATION
      to: MIN-PROOF-BOUNDARY
      relation: defines_or_constrains
    - from: MIN-PROOF-BOUNDARY
      to: TECHNICAL-ARCHITECTURE-MAP
      relation: may_enable_after_phase_decision
    - from: MIN-PROOF-BOUNDARY
      to: TECH-STACK-SHORTLIST
      relation: may_enable_after_phase_decision
    - from: MIN-PROOF-BOUNDARY
      to: PROTOTYPE-SPIKES
      relation: may_enable_after_execution_route
    - from: G1-EXOCORTEX-PRODUCT-FOUNDATION
      to: FULL-EXOCORTEX-APPLICATION
      relation: keeps_max_vision_grounded_without_executing_it
```

## Active Front

```yaml
active_front:
  primary_node: G1-EXOCORTEX-PRODUCT-FOUNDATION
  primary_stage_binding: G1_GOAL_SHAPE
  active_front_statement: >
    Shape the EXOCORTEX Product Foundation Definition. Define WHAT / WHY / DONE
    for the future application foundation before HOW, architecture, stack, prototypes,
    or Codex product execution.
  parallel_candidate_nodes: []
  parallel_policy: >
    No parallel workstreams before the foundation is stable. Parallel research,
    audit, or prototype work can be considered only after G1 exposes specific
    evidence gaps or after a phase-progress decision continues the Phase.
  parked_nodes:
    - TECHNICAL-ARCHITECTURE-MAP
    - TECH-STACK-SHORTLIST
    - PROTOTYPE-SPIKES
    - FULL-EXOCORTEX-APPLICATION
```

## Horizon Slice

```yaml
horizon_slice:
  statement: >
    Reach one reviewed EXOCORTEX Product Foundation Definition and then make a
    phase-progress decision. Do not move into architecture, stack, implementation,
    prototypes, full roadmap, or Codex product execution until that foundation is
    accepted or a specific evidence gap is identified.
  node_ids:
    - M0-MAP-INITIALIZATION
    - G1-EXOCORTEX-PRODUCT-FOUNDATION
    - R1-FOUNDATION-REVIEW-AND-PHASE-GATE
  exit_condition: >
    Foundation definition reviewed; phase-progress gate decides P9_PHASE_CLOSE,
    continuation, Human Decision, or targeted next route.
```

## Parked / Future Nodes

```yaml
parked_future_nodes:
  - id: TECHNICAL-ARCHITECTURE-MAP
    title: EXOCORTEX technical architecture map
    status: parked
    unpark_trigger: >
      Accepted foundation creates a concrete architecture question or phase-progress
      decision explicitly continues into architecture.
  - id: TECH-STACK-SHORTLIST
    title: Tech stack shortlist
    status: parked
    unpark_trigger: >
      Accepted foundation defines buildable boundary and validation criteria requiring
      stack comparison.
  - id: IMPLEMENTATION-SPIKE
    title: Implementation spike
    status: parked
    unpark_trigger: >
      Execution route is approved after foundation, with scope, target paths, and
      validation anchors.
  - id: UI-WORKSPACE-MOCKUP
    title: UI/workspace mockup
    status: parked
    unpark_trigger: >
      Foundation identifies UI/workspace as the next highest-evidence surface.
  - id: EVENT-LEDGER-PROTOTYPE
    title: Event Ledger prototype
    status: parked
    unpark_trigger: >
      Foundation makes Event Ledger the minimum useful validation slice.
  - id: MEMORY-MODEL-PROTOTYPE
    title: Memory model prototype
    status: parked
    unpark_trigger: >
      Foundation makes memory behavior the minimum useful validation slice.
  - id: EXTERNAL-RESEARCH-SWEEP
    title: External research on current AI app infrastructure
    status: parked
    unpark_trigger: >
      G1, S3, E1, or D1 identifies a concrete current-facts evidence gap.
  - id: CODEX-PRODUCT-GRAPH
    title: Codex / Task Master / product execution graph
    status: parked
    unpark_trigger: >
      Accepted Goal and execution brief require multi-file or product/project execution
      through the correct E1/C1/C2 route.
  - id: FULL-EXOCORTEX-APPLICATION
    title: Full EXOCORTEX application / personal external brain
    status: future_max_vision
    unpark_trigger: >
      Multiple later foundations, proofs, and readiness checks show EXOCORTEX is
      radically superior to the current construction workflow.
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
    - accepted_or_rejected_EXOCORTEX_Product_Foundation_Definition
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
