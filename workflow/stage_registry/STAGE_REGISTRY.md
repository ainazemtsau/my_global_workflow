# STAGE_REGISTRY

Status: active
Workflow version: vNext-R
Source GitHub repository file: `workflow/stage_registry/STAGE_REGISTRY.md`
Authority: GitHub runtime stage registry after file read-back / diff verification / commit verification.
Freshness: refresh when stage prompt files, stage IDs, stage availability, target runtime, or allowed transitions change.

## Purpose

This file is the GitHub-native runtime registry for Workflow vNext-R stages.

This file is the sole authority for:

- canonical stage IDs;
- stage identity;
- stage prompt path;
- prompt status as repository-file existence;
- target runtime;
- stage activation availability;
- normal stage-to-stage `allowed_next` transitions.

Packet schema templates are owned by:

```text
workflow/transport/*.md
```

Runtime packet-use behavior, formalization coupling, repository maintenance policy, and runtime precedence remain owned by:

```text
workflow/runtime/WF_VNEXT_R_RUNTIME_CORE.md
```

This file does not define packet schemas, launch/result field lists, stage packet bodies, prompt internals, or stage-specific reasoning.

Terminal card types such as `Context Request`, `Human Decision`, and `Stop` are terminal outputs, not stage IDs. If they appear in `allowed_next`, they are allowed terminal outcomes and not stage-to-stage transition authority.

Special `allowed_next` tokens:

- `continue_current_stage` is a B1-only continuation token, not a stage ID.
- `Direction pause/archive` is a P9-only lifecycle terminal token, not a stage ID.
- Transport/schema concepts such as `topology_launch_bundle` and `codex_return` must not appear as `allowed_next` tokens.

Prompt source root: `workflow/stage_prompts/`

## Registry Rules

Use canonical stage IDs as the primary identifiers for runtime routing.

Short labels such as `D0`, `P0`, or `G1` are read-only compatibility aliases. They are not canonical stage IDs.

Before running a stage, load only the exact prompt file for that stage. Do not bulk-load all stage prompts into a Direction Project.

If a prompt is marked `missing_prompt`, the stage is registered but unavailable for runtime execution until the prompt file is installed and verified.

### GitHub prompt read completeness

A registry row with `prompt_status: present` means the prompt file exists in the repository. It does not prove that a given ChatGPT run received the full prompt text.

Registry `prompt_status: present` proves repository file existence only. Current-run prompt acquisition is governed by `workflow/runtime/CONTEXT_ACQUISITION_POLICY.md`; GitHub read completeness remains governed by `workflow/runtime/GITHUB_LONG_FILE_READ_GUARD.md`.

Before running a stage, the exact prompt file for that stage must be available without truncation or omitted-content markers.

If a GitHub read of the exact stage prompt is truncated, omitted due to tool response token budget, or lacks tail verification, the prompt is considered unavailable for that run. Return Context Request for the exact prompt path. Do not run the stage and do not reconstruct the prompt from memory.

## Route Conflict Rule

Route conflict is selected-route-vs-registry.

A selected next stage is valid only when it is allowed by the current stage row in the Runtime Registry.

Stage prompts may describe route-selection criteria, but stage prompts must not be treated as independent authority for `allowed_next` transition tables. If a stage prompt contains an old route list, the registry wins.

If a running stage selects a next stage that is not allowed by the current stage row in `STAGE_REGISTRY.md`, the stage must not silently choose another route and must not execute the downstream stage's work inside the current stage.

Required behavior on mismatch:

```yaml
route_conflict:
  status: blocking
  conflict_model: selected_route_vs_registry
  selected_next_stage:
  allowed_by_registry: false
  required_output: Context Request, B1_PROBLEM, Human Decision, or Stop
  forbidden_behavior:
    - silently_route_to_another_stage
    - perform_downstream_stage_work_inside_current_stage
    - invent_unregistered_route
    - treat_prompt_route_list_as_authority
```

Unknown stage IDs must produce a Context Request or registry amendment request instead of guessing.

## Canonical Stage IDs

```text
ROUTER_STAGE_LAUNCHER
D0_DIRECTION_SETUP
M0_DIRECTION_MAP
P0_PHASE_START
I0_CAPTURE
G0_GOAL_SELECT
G1_GOAL_SHAPE
S3_DECIDE
D1_DEEP_RESEARCH
A1_AUDIT
E1_EXECUTION_BRIEF
F0_FAST_DIRECT
U1_USER_GUIDED_EXECUTION
C1_CODEX_GRAPH_PLAN
C2_CODEX_EXECUTE
B1_PROBLEM
R1_GOAL_REVIEW_DISTILL
P9_PHASE_CLOSE
R0_RECOVERY_CLOSE
```

## Runtime Registry

| stage_id | stage_name | runtime_role | prompt_path | prompt_status | target_runtime | activation | allowed_next |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ROUTER_STAGE_LAUNCHER | Router / Stage Launcher | Determine the smallest safe next action and produce Launch Card / Context Request / Human Decision / Stop. | `workflow/stage_prompts/ROUTER_STAGE_LAUNCHER.md` | present | chatgpt_direction_project | available | any appropriate stage, Context Request, Human Decision, Stop |
| D0_DIRECTION_SETUP | Direction Setup | Create or repair a Direction container and hand off to phase start when ready. | `workflow/stage_prompts/D0_DIRECTION_SETUP.md` | present | chatgpt_direction_project | available | M0_DIRECTION_MAP, P0_PHASE_START |
| M0_DIRECTION_MAP | Direction Map | Create, review, update, or migrate compact Direction Map / Current Initiative / Active Front / Horizon Slice without doing downstream work. | `workflow/stage_prompts/M0_DIRECTION_MAP.md` | present | chatgpt_direction_project | available | P0_PHASE_START, G0_GOAL_SELECT, G1_GOAL_SHAPE, S3_DECIDE, D1_DEEP_RESEARCH, A1_AUDIT, Context Request, Human Decision, Stop |
| P0_PHASE_START | Phase Start | Start or update current Phase by Critical Constraint and Minimum Outcome. | `workflow/stage_prompts/P0_PHASE_START.md` | present | chatgpt_direction_project | available | I0_CAPTURE, M0_DIRECTION_MAP, G0_GOAL_SELECT, G1_GOAL_SHAPE |
| I0_CAPTURE | Capture / Triage | Route raw inputs without doing the downstream work. | `workflow/stage_prompts/I0_CAPTURE.md` | present | chatgpt_direction_project | available | G0_GOAL_SELECT, G1_GOAL_SHAPE, S3_DECIDE, B1_PROBLEM, Stop |
| G0_GOAL_SELECT | Goal Select | Select or create one candidate for Goal shaping. | `workflow/stage_prompts/G0_GOAL_SELECT.md` | present | chatgpt_direction_project | available | M0_DIRECTION_MAP, G1_GOAL_SHAPE |
| G1_GOAL_SHAPE | Goal Shape / Ruthless Cut | Shape WHAT / WHY / DONE and cut scope before HOW. | `workflow/stage_prompts/G1_GOAL_SHAPE.md` | present | chatgpt_direction_project | available | M0_DIRECTION_MAP, F0_FAST_DIRECT, E1_EXECUTION_BRIEF, S3_DECIDE, D1_DEEP_RESEARCH, A1_AUDIT, B1_PROBLEM, Stop |
| S3_DECIDE | Decide | Resolve a real decision with options, constraints, and human conclusion. | `workflow/stage_prompts/S3_DECIDE.md` | present | chatgpt_direction_project | available | G1_GOAL_SHAPE, E1_EXECUTION_BRIEF, R1_GOAL_REVIEW_DISTILL, Context Request, Human Decision, Stop |
| D1_DEEP_RESEARCH | Deep Research | Research external evidence gaps and synthesize decision implications. | `workflow/stage_prompts/D1_DEEP_RESEARCH.md` | present | chatgpt_direction_project | available | S3_DECIDE, G1_GOAL_SHAPE, E1_EXECUTION_BRIEF, B1_PROBLEM, Context Request, Human Decision, Stop |
| A1_AUDIT | Audit / Challenge | Challenge high-risk, failed, irreversible, or unsupported plans and claims. | `workflow/stage_prompts/A1_AUDIT.md` | present | chatgpt_direction_project | available | S3_DECIDE, G1_GOAL_SHAPE, E1_EXECUTION_BRIEF, R1_GOAL_REVIEW_DISTILL, B1_PROBLEM, Context Request, Human Decision, Stop |
| E1_EXECUTION_BRIEF | Execution Brief | Produce minimum HOW, validation, context, and Codex card if needed. | `workflow/stage_prompts/E1_EXECUTION_BRIEF.md` | present | chatgpt_direction_project | available | M0_DIRECTION_MAP, F0_FAST_DIRECT, U1_USER_GUIDED_EXECUTION, C1_CODEX_GRAPH_PLAN, D1_DEEP_RESEARCH, A1_AUDIT, S3_DECIDE, B1_PROBLEM, Context Request, Human Decision, Stop |
| F0_FAST_DIRECT | Fast Direct | Execute small reversible non-Codex work directly with verification. | `workflow/stage_prompts/F0_FAST_DIRECT.md` | present | chatgpt_direction_project | available | R1_GOAL_REVIEW_DISTILL, E1_EXECUTION_BRIEF, U1_USER_GUIDED_EXECUTION, B1_PROBLEM, Context Request, Human Decision, Stop |
| U1_USER_GUIDED_EXECUTION | User Guided Execution | Guide the human operator through an external app, website, local program, ChatGPT UI, or tool setup when no verified automation/tool binding exists or human operation is safer. | `workflow/stage_prompts/U1_USER_GUIDED_EXECUTION.md` | present | chatgpt_direction_project | available | E1_EXECUTION_BRIEF, B1_PROBLEM, D1_DEEP_RESEARCH, A1_AUDIT, S3_DECIDE, R1_GOAL_REVIEW_DISTILL, Context Request, Human Decision, Stop |
| C1_CODEX_GRAPH_PLAN | Codex Graph Plan | Prepare a bounded Codex execution envelope from accepted workflow context; require Codex-side technical discovery when project-local architecture/reuse decisions are needed. | `workflow/stage_prompts/C1_CODEX_GRAPH_PLAN.md` | present | chatgpt_direction_project | available | C2_CODEX_EXECUTE, Context Request, Human Decision, Stop |
| C2_CODEX_EXECUTE | Codex Execute | Execute a validated Codex graph and return evidence / return-state. | `workflow/stage_prompts/C2_CODEX_EXECUTE.md` | present | codex | available | R1_GOAL_REVIEW_DISTILL, E1_EXECUTION_BRIEF, B1_PROBLEM, Context Request, Human Decision, Stop |
| B1_PROBLEM | Problem Router | Classify blockers before solving and route recovery. | `workflow/stage_prompts/B1_PROBLEM.md` | present | chatgpt_direction_project | available | continue_current_stage, E1_EXECUTION_BRIEF, G1_GOAL_SHAPE, S3_DECIDE, R1_GOAL_REVIEW_DISTILL, Context Request, Human Decision, Stop |
| R1_GOAL_REVIEW_DISTILL | Goal Review / Distill | Review Goal outcome, distill durable knowledge, and update state / docs. | `workflow/stage_prompts/R1_GOAL_REVIEW_DISTILL.md` | present | chatgpt_direction_project | available | M0_DIRECTION_MAP, G0_GOAL_SELECT, G1_GOAL_SHAPE, P9_PHASE_CLOSE, P0_PHASE_START, E1_EXECUTION_BRIEF, B1_PROBLEM, Context Request, Human Decision, Stop |
| P9_PHASE_CLOSE | Phase Close | Close or pause Phase and distill phase-level outcomes. | `workflow/stage_prompts/P9_PHASE_CLOSE.md` | present | chatgpt_direction_project | available | M0_DIRECTION_MAP, P0_PHASE_START, G0_GOAL_SELECT, B1_PROBLEM, Context Request, Human Decision, Direction pause/archive, Stop |
| R0_RECOVERY_CLOSE | Recovery Close | Close mixed or interrupted sessions and reconstruct a safe handoff. | `workflow/stage_prompts/R0_RECOVERY_CLOSE.md` | missing_prompt | mixed | unavailable_until_prompt_installed | ROUTER_STAGE_LAUNCHER, Context Request, Stop |

## Compatibility Aliases

| alias | canonical_stage_id | status | rule |
| --- | --- | --- | --- |
| D0 | D0_DIRECTION_SETUP | read_only_compatibility_label | Accept only as an alias; emit canonical ID in runtime packets. |
| P0 | P0_PHASE_START | read_only_compatibility_label | Accept only as an alias; emit canonical ID in runtime packets. |
| G1 | G1_GOAL_SHAPE | read_only_compatibility_label | Accept only as an alias; emit canonical ID in runtime packets. |

## Validation Rules

Registry validation must check:

1. Every canonical stage ID appears exactly once as a row in the Runtime Registry.
2. Every `present` prompt has a corresponding file under `workflow/stage_prompts/`.
3. `R0_RECOVERY_CLOSE` remains `missing_prompt` until `workflow/stage_prompts/R0_RECOVERY_CLOSE.md` exists and is verified.
4. This registry does not define packet schemas.
5. Packet schema templates live in `workflow/transport/*.md`.
6. Runtime packet-use behavior, formalization coupling, repository maintenance policy, and runtime precedence remain in `workflow/runtime/WF_VNEXT_R_RUNTIME_CORE.md`.
7. Direction Project Files must not contain stage prompt bodies.
8. Stage prompt paths must use `workflow/stage_prompts/<STAGE_ID>.md`.
9. Runtime core must not maintain a second full `allowed_next` transition table.
10. Stage prompts must not be treated as authority for `allowed_next` transition lists.
11. Stage registry interface files, if present, are derived/reference surfaces only and must not override this registry.
12. Transport route fields, if present, are snapshots only and must not override this registry.
13. Terminal card types are not canonical stage IDs.

If a launch card names an unknown stage ID, return a Context Request or registry amendment request instead of guessing.

## End-of-file marker

`END_OF_FILE: workflow/stage_registry/STAGE_REGISTRY.md`
