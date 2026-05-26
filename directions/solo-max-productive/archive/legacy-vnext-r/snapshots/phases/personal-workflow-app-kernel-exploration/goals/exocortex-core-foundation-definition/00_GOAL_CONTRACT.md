# 00 Goal Contract — EXOCORTEX Core Foundation Definition

```yaml
artifact_control:
  artifact_name: "00 Goal Contract — EXOCORTEX Core Foundation Definition"
  schema: goal_contract.v1
  owner_layer: persistence
  status: active
  source_file: "directions/solo-max-productive/phases/personal-workflow-app-kernel-exploration/goals/exocortex-core-foundation-definition/00_GOAL_CONTRACT.md"
  freshness: fresh
  created_at: "2026-05-19"
  created_by_stage: G1_GOAL_SHAPE
  stage_result_id: G1-2026-05-19-exocortex-core-foundation-definition

goal:
  id: exocortex-core-foundation-definition
  title: EXOCORTEX Core Foundation Definition
  lifecycle_state: goal_shaped_pending_E1
  direction_id: solo-max-productive
  direction_name: Solo Max Productive
  phase_id: personal-workflow-app-kernel-exploration
  phase_name: EXOCORTEX App Foundation
  phase_path: "directions/solo-max-productive/phases/personal-workflow-app-kernel-exploration"
  source_candidate_id: G1-CAND-2026-05-13-EXOCORTEX-PRODUCT-FOUNDATION
  source_candidate_title: EXOCORTEX Product Foundation Definition
  clarified_title: EXOCORTEX Core Foundation Definition
  next_route: E1_EXECUTION_BRIEF
  implementation_allowed_now: false
```

## Goal decision

Shape one Goal: define the EXOCORTEX Core Foundation.

This Goal defines the expandable product-level core of the personal AI brain / external-brain application. It is not implementation, stack choice, full architecture, prototype work, or product roadmap execution.

## Goal Contract

### WHAT

Define the product-level Core Foundation for EXOCORTEX: the expandable substrate of a persistent personal AI brain / external-brain application.

The definition must make clear:

- what belongs to the EXOCORTEX core;
- what is an extension or future surface;
- what is Max Vision;
- what is first buildable foundation / Min Proof;
- what must not be implemented yet;
- what validation criteria prove the definition is usable.

The Core Foundation must cover:

- persistent memory and context substrate;
- model interoperability / model-agnostic cognitive engine;
- Context Compiler / relevant-context selection;
- tools/actions extensibility as the system body;
- interaction and process loops;
- workspace surfaces as extensible environments, not isolated UI features;
- learning from outcomes / prediction error;
- Reality Alignment / anti-sycophancy;
- first buildable foundation boundary;
- non-goals and validation criteria.

### WHY now

The active Phase is blocked on foundation definition. The EXOCORTEX concept is broad and implementation-attractive. Without a bounded Core Foundation, downstream work would prematurely drift into architecture, stack choice, prototypes, roadmap expansion, or Codex product execution.

### DONE

A single coherent Core Foundation Definition exists and is ready for review.

A reviewer can distinguish:

1. EXOCORTEX Core Foundation;
2. Max Vision;
3. first buildable foundation / Min Proof;
4. deferred extensions and future surfaces;
5. explicit non-goals;
6. validation criteria;
7. what must not be implemented yet.

### Acceptance floor

One compact but complete definition covering:

- memory/context persistence;
- model interoperability;
- tools/actions extensibility;
- interaction/process loops;
- workspace surfaces;
- learning from outcomes / prediction error;
- Reality Alignment;
- first buildable foundation boundary;
- non-goals;
- validation criteria.

### Validation signal

A reviewer can read the final definition and classify a proposed feature or subsystem as:

- core;
- extension / future surface;
- first buildable foundation;
- Max Vision;
- not now.

### Validation method

E1 must prepare the minimum HOW and validation envelope for producing the definition. The resulting definition must later be reviewed by R1_GOAL_REVIEW_DISTILL against this acceptance floor and the Phase closure contract.

### Smallest testable slice

A definition artifact, not a prototype.

It must be strong enough to guide the first buildable foundation but must not choose stack, architecture, APIs, storage model, provider, UI mockups, or implementation route.

## Scope boundary

### In scope

- EXOCORTEX Core Foundation definition
- product/application principles
- core substrate definition
- memory/context persistence
- model interoperability
- tools/actions extensibility
- interaction/process loops
- workspace surfaces
- learning from outcomes / prediction error
- Reality Alignment / anti-sycophancy
- Max Vision vs Min Proof / buildable foundation split
- first buildable foundation boundary
- non-goals
- validation criteria

### Non-goals

- app implementation
- tech stack choice
- full technical architecture
- database/storage architecture
- model provider selection
- API design
- UI mockups
- Event Ledger prototype
- Memory Model prototype
- Tool registry implementation
- MCP integration plan
- automation implementation
- mobile/desktop/omnichannel buildout
- Task Master graph
- Codex product execution
- full product roadmap

### Deferred candidates

- EXOCORTEX technical architecture map
- tech stack shortlist
- implementation spike
- UI/workspace mockup
- Event Ledger prototype
- memory model prototype
- targeted external research if E1 exposes a concrete evidence gap
- Codex/Task Master/product execution graph
- full EXOCORTEX application

### Constraints

- Do not execute the Goal inside G1.
- Do not treat EXOCORTEX_CONCEPT_SEED_FULL.md as an executable implementation roadmap.
- Do not continue the superseded Personal Workflow App Kernel Min Proof Goal.
- Do not revive old workflow/replacement framing.
- Do not choose architecture, stack, implementation route, or prototype before Goal shaping.
- Cut scope aggressively while preserving one complete useful foundation definition.

## Map binding

```yaml
map_binding:
  initiative_id: INIT-EXOCORTEX-PERSISTENT-PERSONAL-AI-BRAIN
  node_or_edge: NODE-DEFINE-CORE-FOUNDATION
  mapped_goal_node: GOAL-G1-EXOCORTEX-PRODUCT-FOUNDATION
  expected_map_delta: >
    After R1 reviews the Goal outcome, the map may mark Core Foundation
    accepted/rejected/rework and update the next active frontier.
    G1 itself does not mutate 08_DIRECTION_MAP.md.
  why_this_goal_is_minimal: >
    It defines the foundation before architecture, stack, prototype,
    broad research, or product execution.
  why_not_premature_or_optional_expansion: >
    It is the active front and required for Phase closure; downstream
    expansions are parked.
```

## Close path

```text
G1_GOAL_SHAPE formalization
-> Codex repository maintenance apply/read-back
-> manual Project Files refresh
-> E1_EXECUTION_BRIEF
-> execution route selected by E1
-> R1_GOAL_REVIEW_DISTILL reviews the Core Foundation Definition
-> phase-progress gate decides P9_PHASE_CLOSE / continuation / Human Decision / targeted next route
```
