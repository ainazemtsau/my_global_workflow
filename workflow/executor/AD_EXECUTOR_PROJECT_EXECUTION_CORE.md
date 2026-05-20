# AD Executor Project Execution Core

artifact_control:
  artifact_name: "Executor Project Execution Core Architecture Decision"
  schema: workflow_executor_architecture_decision.v1
  owner_layer: executor_project_execution_core
  status: accepted_design_baseline
  repo_path: "workflow/executor/AD_EXECUTOR_PROJECT_EXECUTION_CORE.md"
  authority: "GitHub repository canonical after file read-back, diff verification, commit verification, and push"
  activation_scope: workflow_design_reference
  freshness: refresh_when_executor_core_changes

## Decision

Adopt an executor-generic Project Execution Core for product/project implementation handoff. ChatGPT Direction Projects retain orchestration, planning, review, scope, acceptance, and DONE authority. External executors operate inside target project workspaces and own technical discovery, implementation planning, tool use, validation, repair, and evidence return.

Codex is accepted as the first/default executor adapter. Codex-specific setup and execution behavior must remain adapter-scoped so the architecture can support other executors later.

This decision creates documentation only. It does not change runtime behavior, register stages, alter stage prompts, create transport templates, or update Direction Project Files.

## Why Now

The current workflow has Codex-oriented C1/C2 compatibility paths and Codex project setup contracts, but it needs a clearer generic execution layer that:

- separates workflow repository maintenance from product/project execution
- defines setup as a product execution gate
- makes local project technical context durable and discoverable
- prevents ChatGPT history from becoming the technical source of truth
- preserves ChatGPT ownership of intent, acceptance, and review
- preserves executor ownership of implementation mechanics and validation evidence
- supports Codex now without locking future architecture to Codex

## Authority Boundary

ChatGPT owns:

- WHY
- WHAT
- DONE
- target and target binding expectations
- acceptance criteria
- scope and forbidden changes
- evidence requirements
- approval of readable plans for nontrivial autonomous execution

Executor owns:

- HOW
- codebase discovery
- implementation planning
- tool selection inside approved setup
- project-local technical context usage
- validation
- bounded repair
- evidence return

Task Master is an operational task/dependency graph substrate for complex executor work. It is not execution authority, DONE authority, process authority, or the control plane.

## Accepted Decisions

### D1 Product/project execution requires completed Executor Project Setup

No product/project execution may proceed unless the target project has completed Executor Project Setup and the setup status is acceptable for the requested work.

### D2 Setup has Core Bootstrap plus optional Stack-Specific Setup Tuning Pass

Executor Project Setup has a Required Core Bootstrap and an Optional Stack-Specific Setup Tuning Pass.

### D3 Core-only setup is complete

Core-only setup is a valid complete setup. Stack-specific tuning can improve execution quality, but it is not required for readiness.

### D4 Codex adapter setup verifies Task Master, subagents, validation, module map, profiles, and doctor

Codex adapter setup must install, configure, and verify:

- Task Master
- subagents and reviewer roles
- validation profile
- module map
- `AGENTS.md`
- project profile
- executor profile
- doctor checks

Task Master is required and verified during setup. P2/P3 tasks must use a Task Master graph.

### D5 Optional stack-specific tooling is enable-now, park, or reject, not blind install

Optional stack-specific tools, MCP servers, skills, validators, and conventions must be evaluated before enabling. Decisions are explicit: enable now, use core-only, park, research more, or reject.

### D6 External/current tooling facts route to D1 or research-needed note

If current external facts or current tool behavior materially affect setup, the setup process may route to `D1_DEEP_RESEARCH` or return a research-needed note. It must not guess or install blindly.

### D7 Subagent fallback only setup-time

Subagents and reviewer roles are setup-time requirements for the Codex adapter. If true subagents cannot be configured, setup stops for a setup-time fallback decision. Normal execution assumes setup is complete and does not renegotiate fallback.

### D8 Full-trust target-bound execution

After user authorization and completed setup, execution is full-trust inside the target project workspace. Full trust is limited to the approved target and plan.

### D9 Target binding mandatory

The executor must confirm target binding before work. Required target binding fields are:

- `direction_id`
- `project_id`
- `project_name`
- `project_root_pointer`
- `expected_repo_or_workspace`
- `executor_setup_status`

Wrong target or workspace blocks execution.

### D10 Project Setup Wizard is workflow capability available to Directions

The Project Setup Wizard is a workflow capability available to Directions. It is not registered as a stage in this pass.

### D11 Wizard returns Executor Setup Result

The Project Setup Wizard returns an Executor Setup Result that records setup status, customization mode, generated files, tool validation, doctor result, and any approved fallback.

## Consequences

- Product/project execution has a setup gate.
- Project technical context lives in the project workspace, not ChatGPT history.
- Direction Project Files store compact outcome summaries, approval-relevant decisions, risk notes, and pointers.
- Codex becomes an adapter, not the architecture itself.
- C1/C2 remain compatibility paths until later approved migration work.
- Future transport and registry work must preserve these boundaries.

## Deferred Items

Deferred to later approved passes:

- runtime behavior changes
- `STAGE_REGISTRY.md` updates
- stage prompt changes
- transport templates
- Project Instructions updates
- Direction Project Files 00-08 refreshes
- project-local setup file generation
- stack-specific tuning packages
- machine-readable canonical executor transport schemas

## Rollback / Compatibility

Rollback is documentation-only: remove or supersede these executor core docs if the design is rejected before runtime integration.

Compatibility is preserved because this pass does not change runtime files, registry files, stage prompts, transport templates, or project artifacts. Current `C1_CODEX_GRAPH_PLAN` and `C2_CODEX_EXECUTE` remain the active compatibility path.

## Registry Boundary

No registry change is made in this pass. No new stage is registered by this architecture decision. Any future capability or action named in executor documentation remains a future concept until a later approved registry update.

END_OF_FILE: workflow/executor/AD_EXECUTOR_PROJECT_EXECUTION_CORE.md
