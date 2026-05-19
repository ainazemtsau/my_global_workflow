# Goal Contract — H1_G2 Codex/project setup workflow fit-check

```yaml
artifact_control:
  artifact_name: "Goal Contract — H1_G2 Codex/project setup workflow fit-check"
  schema: goal_contract.v1
  owner_layer: persistence
  status: goal_shaped_pending_A1_audit
  repo_path: "directions/indie-game-development/phases/core-coop-technical-foundation-selection/goals/codex-development-operating-model-and-architecture-protocols/00_GOAL_CONTRACT.md"
  direction_id: indie_game_development
  phase_id: core-coop-technical-foundation-selection
  goal_id: H1_G2_codex_development_operating_model_and_architecture_protocols
  shaped_by_stage: G1_GOAL_SHAPE
  formalized_at: "2026-05-19"
  formalization_trigger: APPROVE_AND_FORMALIZE
  next_stage: A1_AUDIT
  implementation_allowed: false
  unity_bootstrap_allowed: false
  codex_product_execution_allowed: false
  task_master_graph_allowed: false
```

## 1. Goal identity

Goal ID:

`H1_G2_codex_development_operating_model_and_architecture_protocols`

Working title:

`Проверить и адаптировать существующую workflow-процедуру Codex/project setup под первый technical nucleus`

Map binding:

```yaml
map_binding:
  initiative_id: innovative-commercial-expedition-gas-sim-game
  node_or_edge: H1_playable_technical_nucleus / H1_G2_codex_development_operating_model_and_architecture_protocols
  expected_map_delta: >
    H1_G2 shaped as an audit-ready Goal. H1_G3 project/bootstrap/tool-binding
    readiness remains blocked until A1 validates the workflow setup procedure,
    accepts a minimal project-specific addendum/profile, or routes a Workflow
    Governance repair.
  why_this_goal_is_minimal: >
    It checks whether the existing workflow procedure is operational for the
    first real Codex/project setup case before creating any project-local
    process or launching bootstrap/implementation.
  why_not_premature_or_optional_expansion: >
    It does not implement, bootstrap Unity, set up tools, create a Task Master
    graph, transfer old code, or create a second workflow layer.
```

## 2. Goal Contract

### WHAT

Perform a first-use audit / fit-check of the existing workflow Codex/project setup and Codex execution-readiness procedure for the Indie Game Development first technical nucleus.

The Goal must determine one of four outcomes:

1. Existing workflow procedure is sufficient as-is.
2. Existing workflow procedure is sufficient with a minimal Indie Game project-specific addendum/profile.
3. Existing workflow procedure is incomplete or broken and requires a Workflow Governance repair ticket.
4. Blocking context is missing and must be requested by exact repository path.

### WHY now

The first technical nucleus functional/technical specification is accepted, but it does not authorize code, Unity work, Codex product/project execution, Task Master graph creation, old-code transfer, or project mutation.

Before bootstrap or implementation, the Direction must know whether the existing workflow procedure can actually handle:

- project/tool-binding verification;
- Codex execution envelope;
- internal tool setup/readiness;
- validators and validation evidence;
- bounded Codex slices;
- project-local technical memory/profile surfaces;
- evidence return and stop conditions.

### DONE

Done means there is an accepted A1-ready or A1-returned verdict that answers:

> Can the existing workflow project/Codex setup procedure be safely run for Gas Coop Game; if yes, with what exact inputs/checks/evidence; if not, what exact workflow issue blocks it?

### Acceptance floor

- Existing workflow setup/Codex readiness procedure is identified by exact files/stages/templates, or missing paths are requested.
- One paper dry-run is performed against the first technical nucleus setup scenario.
- Gaps are classified as:
  - covered by existing workflow;
  - project-specific input/addendum;
  - workflow defect;
  - missing context.
- No duplicate workflow layer is created.
- No Unity project is created.
- No product code is written.
- No real internal tools are configured.
- No Codex product/project execution is launched.
- No Task Master graph is created.
- No old-code audit or transfer is used as the starting point.
- Next lifecycle route is explicit.

### Validation signal

A reviewer can answer:

- what workflow procedure would be used for setup;
- what exact inputs it needs from this game project;
- what exact checks/evidence it returns;
- what it cannot cover;
- whether unresolved gaps are project-specific or workflow-governance defects.

### Validation method

Paper dry-run of the existing setup/Codex-readiness procedure against this scenario:

```text
Prepare a first Codex-ready project setup for the first technical nucleus:
Unity/C#, Gas/Grid/Topology, validation surfaces, internal tools,
validators, bounded Codex execution, and evidence return.
```

### Smallest testable slice

One audit verdict plus one dry-run setup scenario.

No implementation. No Unity bootstrap. No actual tool setup.

## 3. Key correction — do not create a second workflow layer

This Goal exists because the existing workflow project/Codex setup procedure has not yet been used in this Direction.

The Goal must not create an independent Indie-only Codex workflow.

Correct framing:

```text
Audit and fit-check existing workflow procedure first.
Add only minimal project-specific inputs/profile if needed.
If the workflow itself is broken, route repair to Workflow Governance.
```

Incorrect framing:

```text
Invent a new local operating model, new local setup process, or new Codex handbook.
```

## 4. Scope boundary

### In scope

- Locate and inspect the existing workflow procedure for project setup / Codex readiness.
- Inspect relevant stage prompts, runtime rules, transport templates, and setup docs.
- Dry-run the procedure against the first technical nucleus.
- Classify gaps.
- Define minimal Indie Game project addendum/profile only if needed.
- Define Workflow Governance repair-ticket scope only if the shared workflow is defective.

### Non-goals

- Full engineering handbook.
- Second workflow layer.
- Unity project creation.
- Unity scene creation.
- Product code.
- Test harness implementation.
- CI setup.
- Final DI/package choice.
- Final Unity folder layout.
- Task Master graph creation.
- Codex product/project execution.
- Old-code audit as starting point.
- Old-code transfer.
- Game Documentation promotion.

### Deferred

- Actual bootstrap/tool-binding execution: deferred until after A1 verdict and later E1/U1/C1/C2 route.
- Product-repo local profiles/artifacts: deferred until existing workflow requires them.
- Workflow repair implementation: deferred to Workflow Governance if A1 finds a shared workflow defect.

## 5. Required project-specific concerns for the fit-check

A1 must test whether the existing workflow can handle these Indie Game Development constraints:

- high volume of Codex-written code expected;
- Unity/C# project;
- FishNet/Steam multiplayer direction as accepted decision-map context;
- Gas/Grid/Topology as complex simulation foundation;
- no-code-without-validation rule;
- validation scenes/harnesses/debug telemetry;
- bounded Codex slices;
- module/dependency boundaries;
- old project material as reference/evidence only after requirements are clear;
- direct old-code transfer prohibited.

## 6. Outcome model

A1 should return one of:

```yaml
possible_a1_outcomes:
  - id: existing_workflow_sufficient
    next_route: E1_EXECUTION_BRIEF
    meaning: "Run existing workflow path with named inputs/checks/evidence."
  - id: existing_workflow_plus_minimal_project_profile
    next_route: E1_EXECUTION_BRIEF_or_G1_if_profile_goal_needed
    meaning: "Use existing workflow, with a minimal project-specific addendum/profile."
  - id: workflow_defect_repair_needed
    next_route: Workflow_Governance_repair_request_or_B1_PROBLEM
    meaning: "Shared workflow procedure is incomplete/broken for first real use."
  - id: missing_context
    next_route: Context_Request
    meaning: "Exact workflow files/templates/setup docs must be supplied."
```

## 7. A1 audit target

### Audit object

Existing workflow project setup / Codex readiness procedure.

### Audit criteria

A1 must check whether the procedure explicitly covers or safely routes:

- project/tool-binding verification;
- ChatGPT orchestration vs Codex product execution boundary;
- C1/C2 execution envelope;
- U1 user-guided setup when automation/tool binding is absent;
- internal tools such as AGENTS.md, .codex/config.toml, Task Master, Serena, Basic Memory, validators, if they are part of the workflow;
- project-local technical memory/profile surfaces;
- allowed/forbidden product paths;
- validation commands/checklists;
- evidence return;
- stop conditions;
- workflow repair route if setup procedure is non-operational.

### Candidate workflow files/templates to inspect or request

- `workflow/runtime/WF_VNEXT_R_RUNTIME_CORE.md`
- `workflow/runtime/OBJECTIVE_ARCHITECTURE_MODEL.md`
- `workflow/stage_registry/STAGE_REGISTRY.md`
- `workflow/stage_prompts/E1_EXECUTION_BRIEF.md`
- `workflow/stage_prompts/C1_CODEX_GRAPH_PLAN.md`
- `workflow/stage_prompts/C2_CODEX_EXECUTE.md`
- `workflow/stage_prompts/U1_USER_GUIDED_EXECUTION.md`
- `workflow/stage_prompts/A1_AUDIT.md`
- `workflow/transport/STAGE_LAUNCH_CARD.md`
- `workflow/transport/CODEX_REPOSITORY_MAINTENANCE_APPLY.md`
- `workflow/transport/CODEX_WAVE_CARD.md`
- `workflow/transport/CODEX_RETURN_PACKET.md`
- `workflow/transport/USER_GUIDED_STEP_CARD.md`
- `docs/CHATGPT_PROJECT_SETUP.md`
- Any exact project setup / tool-binding profile template discovered by A1.

If any required file is missing, truncated, or tail-unverified, A1 must return Context Request with exact path.

## 8. Route

Selected next stage:

`A1_AUDIT`

Reason:

This is a challenge/fit-check of an existing workflow procedure on first real use. It must not execute setup. It must determine whether the shared workflow is sufficient, needs minimal project-specific input, or needs Workflow Governance repair.

## 9. Explicit forbidden actions

- Do not run implementation.
- Do not run Unity bootstrap.
- Do not create Unity project.
- Do not run Codex product/project execution.
- Do not create Task Master graph.
- Do not configure internal tools for real.
- Do not transfer old code.
- Do not run old-code audit as starting point.
- Do not promote Game Documentation.
- Do not create a second workflow layer.

## End-of-file marker

`END_OF_FILE: directions/indie-game-development/phases/core-coop-technical-foundation-selection/goals/codex-development-operating-model-and-architecture-protocols/00_GOAL_CONTRACT.md`
