# Goal Contract — Bootstrap Validation Surface Setup Envelope

```yaml
artifact_control:
  artifact_name: "Bootstrap Validation Surface Setup Envelope Goal Contract"
  schema: goal_contract.v1
  direction: indie_game_development
  phase_id: project-bootstrap-validation-surface-setup
  goal_id: bootstrap-validation-surface-setup-envelope
  status: goal_shaped_pending_E1_execution_brief
  shaped_by_stage: G1_GOAL_SHAPE
  formalization_trigger: APPROVE_AND_FORMALIZE
  created_at: "2026-05-22"
  next_stage: E1_EXECUTION_BRIEF
  repository_patch_id: g1_formalize_bootstrap_validation_surface_setup_envelope_2026_05_22
```

## 1. Goal identity

Goal ID: `bootstrap-validation-surface-setup-envelope`

Goal title:

`Сформировать setup/validation envelope для project bootstrap перед H1_G4`

Phase:

`Project Bootstrap and Validation Surface Setup`

Map binding:

`H1_playable_technical_nucleus / H1_G3_project_bootstrap_tool_binding_validation_scene_readiness -> H1_G4_durable_technical_nucleus`

## 2. WHAT

Create a bounded project bootstrap / validation-surface setup envelope.

The envelope must define:

- concrete setup target or exact missing target evidence;
- allowed setup/readiness surfaces;
- forbidden setup/execution surfaces;
- tool-binding verification requirements;
- validation surface requirements;
- evidence requirements;
- stop rules;
- next safe route toward H1_G4.

This Goal is not setup execution. It is the contract that prevents setup from starting without boundaries.

## 3. WHY now

The previous Phase accepted H1_G3 readiness. The current Phase exists because that accepted readiness still must be converted into a bounded setup/validation envelope before H1_G4 durable technical nucleus work is scoped.

Without this envelope, a later stage could accidentally treat readiness as permission to create a Unity project, mutate a product repository, run Codex product/project execution, create a Task Master graph, install/configure Unity MCP, transfer old code, or write product code.

## 4. DONE

This Goal is done when the repository contains an accepted or route-gated setup/validation envelope that allows E1 to prepare execution without inventing project/tool state.

DONE requires that the envelope answer:

1. What target project/workspace/repository state is known, unknown, or missing.
2. What setup surfaces are allowed for the next route.
3. What setup/execution surfaces remain forbidden.
4. What validation surfaces must exist or be prepared before product work is accepted.
5. What evidence must be returned by the next execution route.
6. What conditions force Context Request, Human Decision, A1, D1, U1, X0, X1, E1 replanning, or Stop.
7. Which next stage is safe after this Goal is shaped.

## 5. Minimum complete outcome

One compact, usable setup/validation envelope that binds:

- target;
- allowed surfaces;
- forbidden surfaces;
- validation expectations;
- evidence requirements;
- stop rules;
- next route.

Anything less still forces the next stage to invent project/tool state.

## 6. Acceptance floor

The accepted envelope must include:

- target/workspace status table: known / unknown / must request;
- allowed actions table;
- forbidden actions table;
- validation-surface inventory;
- tool-binding verification checklist;
- evidence checklist;
- stop-rule matrix;
- next-route recommendation with rejected alternatives.

## 7. Validation signal

Later `E1_EXECUTION_BRIEF`, `U1_USER_GUIDED_EXECUTION`, `X0_EXECUTOR_PROJECT_SETUP`, `X1_EXECUTOR_RUN`, or H1_G4 scoping can proceed without inventing project/tool state.

## 8. Validation method

Validate the produced envelope against:

- current Phase frame;
- accepted H1_G3 readiness evidence;
- accepted H1_G2 Gas Coop Game Project Execution Profile;
- Direction Map H1_G3 -> H1_G4 boundary;
- forbidden-action list in current runtime files.

Validation fails if the envelope silently authorizes real setup, product code, repo creation, Unity bootstrap, Codex product/project execution, Task Master graph creation, Unity MCP setup, old-code transfer, or Game Documentation promotion.

## 9. Smallest testable slice

A single repository-backed envelope artifact plus execution-log entry.

The slice excludes implementation, validator implementation, validation scene creation, tool setup, Unity bootstrap, product repository mutation, and product code.

## 10. Scope in

- Define setup/validation envelope.
- Define target evidence requirements.
- Define allowed setup/readiness surfaces.
- Define forbidden setup/execution surfaces.
- Define validation surface requirements.
- Define tool-binding verification requirements.
- Define evidence requirements.
- Define stop rules.
- Define next safe route.

## 11. Non-goals

- Unity bootstrap.
- Product repository creation.
- Product code.
- Codex product/project execution.
- Task Master graph creation.
- Real internal tool setup.
- Unity MCP setup/configuration.
- Old-code transfer.
- Old-code audit as starting point.
- Game Documentation promotion.
- Broad engineering handbook.
- Final DI package selection.
- Concrete Unity folder layout.
- Validator implementation.
- Validation scene implementation.
- H1_G4 durable technical nucleus implementation.

## 12. Scope cuts / deferred candidates

Deferred unless selected by later route:

- final DI package selection;
- concrete Unity folder layout;
- validation scene creation;
- Unity MCP install/configuration;
- Task Master graph creation;
- old-code reference audit;
- Game Documentation promotion;
- H1_G4 implementation planning.

## 13. Constraints

- G1 shapes the Goal; it does not execute it.
- Product/project execution remains blocked.
- Repository maintenance is allowed only for this approved workflow/Direction patch.
- E1 owns the next execution brief.
- Any later executor setup/run route must prove target project, setup state, tool bindings, validation, scope, and permissions.

## 14. Escalation triggers

Route to Context Request if:

- target project/workspace evidence is missing or contradictory;
- accepted H1_G3 evidence cannot be located;
- required Project Files are stale or conflicting;
- exact stage prompt or required context is unavailable.

Route to Human Decision or S3 if:

- there are multiple valid setup targets or setup routes with material tradeoffs;
- the human owner must choose between manual UI setup and automated/Codex setup.

Route to D1 if:

- current external tool/platform facts are required before safe setup planning.

Route to A1 if:

- source-of-truth conflict, stale readiness evidence, or unsafe execution boundary is discovered.

Route to U1 if:

- the next safe action requires the user to operate an external/local UI step by step.

Route to X0 only through E1 if:

- executor project setup is the selected next execution route and setup request/evidence requirements are explicit.

Stop if:

- any stage attempts to perform product execution, Unity bootstrap, tool setup, or product repository mutation without a valid later route.

## 15. Route recommendation

Selected next stage:

`E1_EXECUTION_BRIEF`

Route reason:

E1 is the smallest safe next route because the next work is not direct execution. It requires a compact execution brief defining target, route, validation, evidence, allowed surfaces, forbidden surfaces, and potential handoff to U1/X0/X1/D1/A1/S3/Context Request/Human Decision/Stop.

Alternatives rejected:

- `F0_FAST_DIRECT`: rejected because the work is not a tiny direct reversible patch.
- Direct `X0_EXECUTOR_PROJECT_SETUP`: rejected because G1 does not launch executor setup directly.
- Direct `X1_EXECUTOR_RUN`: rejected because there is no execution work package or accepted setup state.
- Direct Unity/project bootstrap: rejected because execution remains forbidden.
- `M0_DIRECTION_MAP`: rejected because current Phase and seed are already selected.

## 16. Proof status

```yaml
proof_status:
  map_frontier_binding: sufficient_for_G1
  next_action_proof: inherited_from_P0_current_phase_launch
  minimum_complete_outcome: >
    One compact setup/validation envelope binding target, allowed and
    forbidden surfaces, validation expectations, evidence, stop rules,
    and next route.
  mssp_status: proven_compact
  user_example_classification: not_present
```

## 17. Close path

After repository maintenance apply/read-back succeeds:

- Active Goal becomes `bootstrap-validation-surface-setup-envelope`.
- Goal status becomes `goal_shaped_pending_E1_execution_brief`.
- Next route becomes `E1_EXECUTION_BRIEF`.
- Product/project execution remains blocked.

## End-of-file marker

`END_OF_FILE: directions/indie-game-development/phases/project-bootstrap-validation-surface-setup/goals/bootstrap-validation-surface-setup-envelope/00_GOAL_CONTRACT.md`
