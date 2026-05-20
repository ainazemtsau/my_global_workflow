# Goal Contract — H1_G3 Project Bootstrap / Tool Binding / Validation Scene Readiness

```yaml
artifact_control:
  artifact_name: "Goal Contract — H1_G3 Project Bootstrap / Tool Binding / Validation Scene Readiness"
  schema: goal_contract.v1
  owner_layer: persistence
  status: goal_shaped_pending_E1_execution_brief
  repo_path: "directions/indie-game-development/phases/core-coop-technical-foundation-selection/goals/project-bootstrap-tool-binding-validation-scene-readiness/00_GOAL_CONTRACT.md"
  created_by_stage: G1_GOAL_SHAPE
  created_at: "2026-05-20"
goal:
  goal_id: H1_G3_project_bootstrap_tool_binding_validation_scene_readiness
  title: "Сформировать readiness-пакет для project bootstrap, tool-binding и validation scenes первого technical nucleus"
  phase_id: core-coop-technical-foundation-selection
  direction_id: indie_game_development
  status: goal_shaped_pending_E1_execution_brief
  next_route: E1_EXECUTION_BRIEF
  implementation_allowed_now: false
  codex_product_execution_allowed_now: false
  unity_bootstrap_allowed_now: false
  task_master_graph_allowed_now: false
```

## WHY now

H1_G2 accepted the minimal Gas Coop Game project execution profile/addendum.

The next blocker is no longer workflow/profile readiness. The next blocker is project/bootstrap/tool-binding/validation-scene readiness before any real setup, Unity bootstrap, product repository creation, Codex product/project execution, Task Master graph creation, Unity MCP setup, or implementation.

H1_G3 is the direct readiness gate between the accepted execution profile and any later E1 planning, U1 guided setup, C1/C2 execution envelope, or durable technical nucleus implementation.

## WHAT

Produce a compact Bootstrap / Tool-Binding / Validation-Scene Readiness Packet for the first technical nucleus.

The packet must define the minimum safe readiness state for later project bootstrap, tool binding, and validation-surface setup.

It must answer:

- what project/workspace target is intended;
- what is known, unknown, or human-owned about product repository and Unity project state;
- which tools/bindings must be verified before product execution;
- what evidence is required for each readiness surface;
- what validation scenes, harnesses, tests, debug views, or manual checks are needed;
- what remains blocked;
- which lifecycle route should run next.

## DONE

H1_G3 is complete only when a readiness packet exists and is accepted or route-gated.

The packet must include:

1. Bootstrap target definition without creation.
2. Tool-binding readiness matrix.
3. Validation-scene / harness readiness requirements.
4. Evidence requirements for each surface.
5. Stop rules.
6. Next-route recommendation.

## Minimum Complete Outcome

A single accepted readiness packet that lets the next stage choose a safe setup route without guessing.

The packet must cover:

- product workspace / repository target;
- Unity project readiness state;
- Codex workspace/tool binding readiness;
- AGENTS.md / .codex/config.toml readiness;
- Task Master readiness;
- Serena readiness;
- Basic Memory readiness;
- Unity MCP readiness policy;
- validators / tests / manual evidence;
- validation scenes and harnesses;
- stop rules;
- next route.

## Acceptance floor

The Goal passes only if the readiness packet:

- names all bootstrap/tool-binding/validation surfaces required before product execution;
- defines concrete evidence required for each surface;
- preserves no-bootstrap / no-product-execution boundaries;
- identifies missing information precisely enough for Context Request or Human Decision;
- recommends a registry-valid next route;
- states what remains blocked;
- can be used by a fresh next-stage chat without old-chat memory.

## Validation signal

A fresh next-stage run can decide whether to proceed to E1_EXECUTION_BRIEF, U1_USER_GUIDED_EXECUTION, D1_DEEP_RESEARCH, A1_AUDIT, S3_DECIDE, Context Request, Human Decision, or Stop without inventing project/tool state.

## Validation method

Review the readiness packet against these checks:

- no Unity bootstrap occurred;
- no product repository was created;
- no product code was written;
- no real tool setup was performed;
- every readiness surface has evidence requirement or explicit unresolved status;
- every unresolved blocker has a route;
- next route is registry-valid;
- Codex product/project execution remains blocked until a later valid route.

## Smallest testable slice

One compact readiness packet plus a next-route recommendation.

Not included:

- full engineering handbook;
- project bootstrap procedure;
- product repo layout finalization;
- Unity project creation;
- validation scene creation;
- Task Master graph creation;
- Codex product execution envelope;
- implementation.

## Scope in

- H1_G3 readiness packet requirements.
- Bootstrap target readiness definition.
- Tool-binding surface inventory.
- Evidence matrix schema.
- Validation-scene / harness readiness requirements.
- Stop rules.
- Next route gates.

## Non-goals / forbidden in this Goal

This Goal must not:

- run Unity bootstrap;
- create product repository;
- create Unity project;
- write product code;
- run Codex product/project execution;
- create Task Master graph;
- configure AGENTS.md or .codex/config.toml;
- configure Serena;
- configure Basic Memory;
- install or configure Unity MCP;
- mutate scenes, prefabs, assets, or scripts;
- transfer old code;
- use old-code audit as starting point;
- select final DI package;
- promote Game Documentation;
- execute H1_G3 work inside G1.

## Tool-binding readiness matrix requirements

The later readiness packet must classify each surface as one of:

- ready_evidence_present
- needs_user_guided_check
- needs_research
- needs_audit
- needs_human_decision
- blocked
- deferred_not_blocking

Required surfaces:

- product repository target;
- local workspace path;
- Git/worktree policy;
- Unity Editor version / install state;
- Unity project existence;
- Codex workspace binding;
- AGENTS.md readiness;
- .codex/config.toml readiness;
- Task Master readiness;
- Serena readiness;
- Basic Memory readiness;
- Unity MCP readiness;
- validators/test runners;
- validation scenes/harnesses;
- manual evidence/checklist path.

## Candidate validation surfaces

Candidate surfaces to evaluate, not create inside H1_G3:

- GasSimLab;
- GridTopologyLab;
- NetworkHarness;
- GameplayInteractionLab;
- FirstNucleusScene;
- unit tests for pure/domain logic;
- integration tests for linked systems;
- debug view / inspector / overlay;
- manual playtest checklist.

## Stop rules

Stop or route away if:

- repository target is ambiguous;
- Unity project ownership or location is ambiguous;
- local tool state cannot be verified;
- credentials/secrets may be exposed;
- setup requires destructive or irreversible action;
- external/current tool documentation is required before safe instruction;
- old project material is being treated as production base;
- Codex product/project execution is attempted before verified bindings;
- user-owned decision is required.

## Map binding

```yaml
map_binding:
  initiative_id: innovative-commercial-expedition-gas-sim-game
  node_or_edge: H1_G3_project_bootstrap_tool_binding_validation_scene_readiness
  expected_map_delta: goal_shaped_pending_E1_execution_brief
  why_this_goal_is_minimal: >
    H1_G3 is the direct readiness gate between the accepted H1_G2 execution
    profile and any later bootstrap, U1 guided setup, Codex graph, or implementation route.
  why_not_premature_or_optional_expansion: >
    It does not create a product repo, Unity project, tool config, validation scene,
    Codex graph, or implementation slice; it only defines readiness evidence and route gates.
```

## Proof status

```yaml
map_frontier_binding_status: proven_from_M0_active_front_review
next_action_proof_status: inherited_from_08_DIRECTION_MAP
minimum_complete_outcome: >
  Accepted H1_G3 readiness packet defining target setup surfaces, required evidence,
  validation-scene/harness readiness requirements, stop rules, and next route.
MSSP_status: proven_compact
user_example_classification: not_present
```

## Route decision

Selected next stage:

`E1_EXECUTION_BRIEF`

Route reason:

E1 is the smallest safe next route because H1_G3 involves multiple setup/tool/validation surfaces and must plan a concrete execution envelope without prematurely running setup or product execution.

Rejected alternatives:

- direct P9_PHASE_CLOSE: premature while H1_G3 remains active-front readiness node;
- direct F0_FAST_DIRECT: too narrow for multi-surface readiness;
- direct U1_USER_GUIDED_EXECUTION: premature until E1 defines exact user-guided checks;
- direct C1_CODEX_GRAPH_PLAN / C2_CODEX_EXECUTE: blocked until project/tool bindings are verified;
- direct Unity bootstrap / product repo creation: explicitly forbidden.

## Next route

`E1_EXECUTION_BRIEF` — prepare the concrete H1_G3 readiness execution brief without running bootstrap, product repository creation, real tool setup, Task Master graph creation, Unity MCP setup, product code, or Codex product/project execution directly.

## Close path

H1_G3 should close through a later accepted readiness packet and then route according to evidence:

- E1_EXECUTION_BRIEF for setup/execution envelope;
- U1_USER_GUIDED_EXECUTION for human-guided local UI/tool checks;
- D1_DEEP_RESEARCH for current external tooling uncertainty;
- A1_AUDIT for high-risk setup/procedure conflict;
- S3_DECIDE / Human Decision for human-owned tradeoffs;
- Context Request for missing exact state/files;
- Stop for unsafe or contradictory state.

## End-of-file marker

`END_OF_FILE: directions/indie-game-development/phases/core-coop-technical-foundation-selection/goals/project-bootstrap-tool-binding-validation-scene-readiness/00_GOAL_CONTRACT.md`
