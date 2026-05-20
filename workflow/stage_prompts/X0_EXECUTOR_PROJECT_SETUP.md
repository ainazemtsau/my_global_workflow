# X0_EXECUTOR_PROJECT_SETUP - Executor Project Setup Stage Prompt

```yaml
artifact_control:
  artifact_name: "X0 Executor Project Setup Stage Prompt"
  schema: stage_prompt.v1
  stage_id: X0_EXECUTOR_PROJECT_SETUP
  target_runtime: codex
  status: active
  repo_path: workflow/stage_prompts/X0_EXECUTOR_PROJECT_SETUP.md
```

## Authority Boundary

AD-WF-RT-001 applies. `workflow/stage_registry/STAGE_REGISTRY.md` owns stage identity and route validity. `workflow/transport/*.md` owns packet shape. Runtime behavior remains in `workflow/runtime/WF_VNEXT_R_RUNTIME_CORE.md`.

X0 is the only registered setup stage for Executor Project Setup. Project Setup Wizard is a capability/action executed inside X0. `EXECUTOR_PROJECT_SETUP` is not a stage ID.

## Mission

Run Executor Project Setup Wizard for the approved target project/workspace and return setup evidence.

X0 does not require prior completed Executor Project Setup. The setup action itself is the exception to the normal product/project setup gate.

X0 must not perform product/project execution beyond setup. It must not perform workflow repository maintenance unless that maintenance is separately approved under the repository maintenance route.

## Inputs

Input is a human-readable Project Setup Request. In J1, no canonical `EXECUTOR_SETUP_REQUEST.md` transport exists yet; do not duplicate a future schema in this prompt.

The request must include or X0 must ask for:

- `direction_id`
- `project_id`
- `project_name`
- `project_root_pointer`
- `expected_repo_or_workspace`
- `requested_executor_adapter`
- setup objective

If target identity, workspace, permissions, or setup objective are ambiguous, return `NEEDS_INPUT` with the exact missing input.

## Required Behavior

Before any mutation, confirm that the current workspace matches `project_root_pointer` and `expected_repo_or_workspace`. Wrong target blocks mutation.

Create or verify Required Core Bootstrap for the requested executor adapter. For the Codex adapter, Task Master, subagents, and reviewer roles are setup requirements. They are resolved during setup, not renegotiated during normal execution.

Run Core Doctor and record evidence. There is no `DONE` without doctor evidence.

Optional Stack-Specific Setup Tuning Pass may recommend tools, MCP servers, validators, skills, or stack conventions. Optional tooling must not be installed blindly. Unity, MCP, C#, game-editor, or other stack-specific tooling requires an explicit enable-now, park, reject, or research decision.

Core-only setup is a valid complete setup. `complete_with_approved_fallback` is valid only when the fallback is explicit, bounded, approved during setup, and recorded in the setup result.

Full-trust executor operation, when later authorized, applies only inside the approved target project/workspace. It does not apply to sibling Directions, workflow repository maintenance paths, unrelated repositories, or external systems outside the approved target.

Do not mirror full product technical context into Direction Project Files. Store full technical setup detail in project-local artifacts and return compact pointers or summaries for workflow review.

## Outputs

Return a human-readable setup result first.

The evidence must be mappable to:

```text
workflow/transport/EXECUTOR_SETUP_RESULT.md
schema: executor_setup_result.v1
```

Include target confirmation, adapter, setup status, core bootstrap evidence, doctor result, stack-specific decisions if any, approved fallback if any, blockers, and recommended next route.

Return states:

- `DONE`: setup completed or completed with approved fallback and evidence is present.
- `NEEDS_INPUT`: required target, permission, credential, setup decision, current fact, or external action is missing before safe setup can continue.
- `STUCK`: setup began but cannot safely complete after bounded correction or the target state is inconsistent.

## Route Behavior

Use `workflow/stage_registry/STAGE_REGISTRY.md` as route authority. X0 may recommend a next route only if it is registry-valid for X0.

If external/current facts materially affect setup, recommend `D1_DEEP_RESEARCH` when that selected next stage is registry-valid.

If external UI or local tool operation is required, recommend `U1_USER_GUIDED_EXECUTION` when that selected next stage is registry-valid.

Use `E1_EXECUTION_BRIEF` for follow-on execution briefing, `B1_PROBLEM` for unclear blockers, `R1_GOAL_REVIEW_DISTILL` when setup completes a parent Goal review boundary, or Context Request / Human Decision / Stop as appropriate.

## End-of-file marker

END_OF_FILE: workflow/stage_prompts/X0_EXECUTOR_PROJECT_SETUP.md
