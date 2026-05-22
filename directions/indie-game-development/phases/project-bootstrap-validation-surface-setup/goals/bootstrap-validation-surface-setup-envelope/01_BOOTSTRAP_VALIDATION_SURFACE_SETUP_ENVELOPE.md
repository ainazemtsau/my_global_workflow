# Bootstrap Validation Surface Setup Envelope

```yaml
artifact_control:
  artifact_name: "Bootstrap Validation Surface Setup Envelope"
  schema: bootstrap_validation_surface_setup_envelope.v1
  owner_layer: direction_goal_artifact
  status: bootstrap_validation_surface_setup_envelope_formalized
  direction_id: indie_game_development
  phase_id: project-bootstrap-validation-surface-setup
  goal_id: bootstrap-validation-surface-setup-envelope
  repo_path: "directions/indie-game-development/phases/project-bootstrap-validation-surface-setup/goals/bootstrap-validation-surface-setup-envelope/01_BOOTSTRAP_VALIDATION_SURFACE_SETUP_ENVELOPE.md"
  formalized_by_stage: F0_FAST_DIRECT
  formalization_trigger: APPROVE_AND_FORMALIZE
  formalized_at: "2026-05-22"
  scope_lock: readiness_envelope_only
  implementation_allowed_now: false
  codex_product_execution_allowed_now: false
  unity_bootstrap_allowed_now: false
  product_repository_creation_allowed_now: false
  product_code_allowed_now: false
  task_master_graph_allowed_now: false
  real_internal_tool_setup_allowed_now: false
  unity_mcp_setup_allowed_now: false
  old_code_transfer_allowed_now: false
  old_code_audit_as_starting_point_allowed_now: false
  game_documentation_promotion_allowed_now: false
```

## 1. Purpose

This envelope converts accepted H1_G3 readiness into a bounded setup/validation control surface before H1_G4 durable technical nucleus work is scoped.

It does not execute setup. It defines what may be checked, what must be requested, what remains forbidden, what evidence later routes must return, and which stop rules prevent premature bootstrap or product execution.

## 2. Source basis / scope lock

```yaml
source_basis:
  direction: Indie Game Development
  phase: Project Bootstrap and Validation Surface Setup
  active_goal: bootstrap-validation-surface-setup-envelope
  previous_accepted_gate: H1_G3_project_bootstrap_tool_binding_validation_scene_readiness
  accepted_profile_surface: H1_G2 Gas Coop Game Project Execution Profile / addendum
  target_horizon_gate: H1_G3 -> H1_G4 durable technical nucleus
scope_lock:
  allowed_result: "setup/validation envelope only"
  not_allowed_result: "bootstrap, product execution, implementation, or tool setup"
```

The envelope is a gate/checklist artifact. It is not a product setup script, Unity bootstrap guide, implementation plan, Codex execution work package, or Task Master graph.

## 3. Target / workspace status table

| Surface | Known / accepted basis | Unknown / must verify before execution | Required treatment |
| --- | --- | --- | --- |
| Direction runtime | Indie Game Development is active in Workflow vNext-R. | None for this artifact. | Use current Direction-local paths only. |
| Current Phase | `project-bootstrap-validation-surface-setup`. | None for this artifact. | Keep work inside this Phase. |
| Active Goal | `bootstrap-validation-surface-setup-envelope`. | None for this artifact. | This artifact is the Goal output candidate. |
| Product workspace | Prior H1_G3 evidence points to Gas Coop Game setup/readiness surfaces. | Current local existence, exact path state, Unity project state, and repository status must be verified before setup or execution. | Later route must inspect or request evidence. |
| Product repository | Expected standalone external product repository/workspace. | Actual git remote/status and safe working tree state must be verified. | Do not mutate product repo from this F0. |
| Unity editor/project | Unity project readiness is relevant for later validation surfaces. | Installed Unity version, project openability, package state, scenes, validators, and compile state are not verified by this artifact. | Later U1/X0/X1 route must verify before relying on Unity. |
| Codex executor binding | Codex is expected as primary executor route after readiness. | Actual product-local `AGENTS.md`, `.codex`, permissions, validation commands, and adapter status must be verified. | No Codex product/project execution until verified through a later route. |
| Task Master | May be relevant later if executor workflow requires it. | Graph/config/status not verified. | Do not create graph here. |
| Serena / Basic Memory | May be relevant later as tool bindings. | Availability/config/status not verified. | Treat as unknown until verified. |
| Unity MCP | Deferred/blocked surface. | Utility and safe integration are not authorized by this artifact. | No installation or configuration here. |
| Old code / old project | Reference/evidence only after requirements are clear. | Transfer safety not selected for this Phase. | No transfer and no old-code audit as starting point. |

## 4. Allowed setup/readiness surfaces

Later routes may use this envelope to perform only bounded readiness/setup classification work:

- verify whether the target product workspace exists;
- verify whether the expected product repository and Unity project are present;
- inspect whether required local workflow files or tool-binding files exist;
- classify tool bindings as present, absent, incomplete, stale, unsafe, or unknown;
- inventory validation surfaces without implementing them;
- request missing context with exact paths or evidence requests;
- route to U1 when human local UI/tool operation is needed;
- route to X0 only when the setup request, target, evidence requirements, and permissions are concrete;
- route to E1 when execution envelope planning remains insufficient;
- route to D1 when current external tool/platform facts are required;
- route to A1/B1/S3/Human Decision/Stop when conflicts, risk, ambiguity, or human-owned tradeoffs appear.

## 5. Forbidden setup/execution surfaces

This envelope explicitly blocks:

- Unity bootstrap;
- product repository creation;
- product repository mutation;
- product code;
- Codex product/project execution;
- X1 executor run;
- Task Master graph creation;
- real internal tool setup;
- Unity MCP installation/configuration;
- old-code transfer;
- old-code audit as starting point;
- Game Documentation promotion;
- broad engineering handbook creation;
- final DI package selection;
- concrete Unity folder layout selection;
- validator implementation;
- validation scene implementation;
- H1_G4 durable technical nucleus implementation.

## 6. Validation-surface inventory

This artifact inventories validation surfaces only. It does not implement them.

Required validation surfaces for this envelope itself:

| Validation surface | Required evidence |
| --- | --- |
| Artifact inspection | File exists at the approved path and contains required anchors. |
| Forbidden-scope check | Diff touches only the approved Direction-local artifact/log files. |
| Read-back anchor check | Required anchors are visible after repository maintenance. |
| EOF integrity | The EOF marker appears exactly once and is final non-whitespace content. |
| Execution log check | Log entry exists and does not claim product execution. |

Candidate validation surfaces for later setup or implementation routes:

| Candidate surface | Later use | Current status |
| --- | --- | --- |
| Pure/domain unit tests | Validate gameplay/domain logic outside Unity presentation where possible. | Candidate only. |
| Integration tests | Validate linked systems after bounded implementation. | Candidate only. |
| Unity validation scene | Let the user observe practical behavior in editor/game. | Candidate only. |
| Debug/inspector/overlay evidence | Make system state visible for validation. | Candidate only. |
| Manual playtest checklist | Use when automation is not yet sensible. | Candidate only. |
| Network harness | Validate host/client behavior when multiplayer work begins. | Candidate only. |

## 7. Tool-binding verification checklist

Before X0/X1/product work, a later route must verify or request:

- exact product workspace path;
- whether the workspace exists locally;
- whether it is a git repository;
- remote URL and branch/worktree state when relevant;
- Unity project version and openability;
- compile/test/validation command status;
- product-local `AGENTS.md` or equivalent;
- Codex configuration status;
- Task Master status;
- Serena status;
- Basic Memory status;
- validation-scene or harness status;
- whether secrets, credentials, paid services, or permissions are involved;
- whether any step requires human UI confirmation or screenshot evidence.

Unknown must remain unknown. Do not infer tool bindings from governance notes, old chats, or accepted profile intent.

## 8. Evidence checklist

Any later setup/execution route must return compact evidence, not only claims:

- checked path(s);
- files found / missing;
- git status / remote summary if relevant;
- Unity version / project openability result if relevant;
- tool-binding status matrix;
- validator or validation-scene status;
- exact blocker list;
- forbidden-scope confirmation;
- screenshots or copied logs only when U1/human-visible confirmation is needed;
- next-route recommendation based on observed evidence.

## 9. Stop-rule matrix

| Condition | Required response |
| --- | --- |
| Product workspace path is missing or contradictory | Context Request or Human Decision. |
| Unity project cannot be found/opened and Unity work is needed | U1 or Context Request. |
| Required tool binding is missing or unsafe | E1 replanning, U1, X0 setup planning, or Stop. |
| Product code change is needed | Do not execute here; route through E1/X1 only after setup readiness. |
| Current external tool/platform facts are needed | D1_DEEP_RESEARCH. |
| Human-owned scope/risk choice appears | S3_DECIDE or Human Decision. |
| Source-of-truth conflict appears | A1_AUDIT, B1_PROBLEM, Context Request, or Stop. |
| Target or validation path is unclear | E1 replanning or Context Request. |
| Task Master graph is requested before route authorization | Stop or route correction. |
| Unity MCP setup is requested before explicit route authorization | Stop or route correction. |
| Old-code transfer is requested as starting point | Stop or route correction. |
| Any forbidden action is requested | Stop or route correction. |

## 10. Next-route recommendation

After this artifact is applied and read back, F0 should validate the repository maintenance return in the same stage thread.

If validation passes, the expected next workflow route is:

```yaml
next_stage_after_successful_apply_readback_validation: R1_GOAL_REVIEW_DISTILL
reason: >
  The envelope artifact is the expected parent Goal outcome candidate.
  R1 should review whether it satisfies the Goal Contract and whether the
  Phase should continue, route to setup, or remain blocked.
```

Operational recommendation for after R1 acceptance:

- Use `E1_EXECUTION_BRIEF` when a concrete setup/request envelope still needs planning.
- Use `U1_USER_GUIDED_EXECUTION` when the next safe action requires the human to operate local UI/tools.
- Use `X0_EXECUTOR_PROJECT_SETUP` only when target, permissions, setup request, and evidence expectations are explicit.
- Use `X1_EXECUTOR_RUN` only after acceptable setup status and an approved execution work package.
- Use `D1_DEEP_RESEARCH` when current external tool/platform facts affect the route.
- Use `A1_AUDIT` or `B1_PROBLEM` when evidence conflicts or framing is unsafe.
- Use Human Decision or Stop when the user must choose risk/scope or a forbidden action is requested.

Rejected alternatives for immediate execution:

| Alternative | Rejection reason |
| --- | --- |
| Direct Unity bootstrap | Forbidden by Goal/E1 scope. |
| Direct product repository creation | Forbidden by Goal/E1 scope. |
| Direct X1 executor run | No accepted setup state or execution work package. |
| Task Master graph creation | Forbidden until later route authorizes it. |
| Unity MCP setup | Deferred/blocked until separately justified and routed. |
| Old-code transfer | Out of scope; old material is reference/evidence only. |
| Game Documentation promotion | Requires explicit later documentation route/patch. |

## 11. Read-back / validation anchors

Repository maintenance must verify these anchors:

```text
status: bootstrap_validation_surface_setup_envelope_formalized
scope_lock: readiness_envelope_only
implementation_allowed_now: false
codex_product_execution_allowed_now: false
unity_bootstrap_allowed_now: false
task_master_graph_allowed_now: false
unity_mcp_setup_allowed_now: false
old_code_transfer_allowed_now: false
game_documentation_promotion_allowed_now: false
## 3. Target / workspace status table
## 4. Allowed setup/readiness surfaces
## 5. Forbidden setup/execution surfaces
## 6. Validation-surface inventory
## 7. Tool-binding verification checklist
## 8. Evidence checklist
## 9. Stop-rule matrix
## 10. Next-route recommendation
```

## End-of-file marker

END_OF_FILE: directions/indie-game-development/phases/project-bootstrap-validation-surface-setup/goals/bootstrap-validation-surface-setup-envelope/01_BOOTSTRAP_VALIDATION_SURFACE_SETUP_ENVELOPE.md
