# STAGE_REGISTRY

Status: active
Workflow version: vNext-R
Source GitHub repository file: `workflow/stage_registry/STAGE_REGISTRY.md`
Authority: GitHub runtime stage registry after file read-back / diff verification / commit verification.
Freshness: refresh when stage prompt files, stage IDs, stage availability, target runtime, or allowed transitions change.

## Purpose

This file is the GitHub-native runtime registry for Workflow vNext-R stages.

Packet contracts live in `workflow/runtime/WF_VNEXT_R_RUNTIME_CORE.md`.

This file is only stage registry / stage identity / prompt path / allowed transitions. It does not define packet schemas, launch/result field lists, stage packet bodies, or prompt internals.

Prompt source root: `workflow/stage_prompts/`

## Registry Rules

Use canonical stage IDs as the primary identifiers for runtime routing.

Short labels such as `D0`, `P0`, or `G1` are read-only compatibility aliases. They are not canonical stage IDs.

Before running a stage, load only the exact prompt file for that stage. Do not bulk-load all stage prompts into a Direction Project.

If a prompt is marked `missing_prompt`, the stage is registered but unavailable for runtime execution until the prompt file is installed and verified.

## Canonical Stage IDs

```text
ROUTER_STAGE_LAUNCHER
D0_DIRECTION_SETUP
P0_PHASE_START
I0_CAPTURE
G0_GOAL_SELECT
G1_GOAL_SHAPE
S3_DECIDE
D1_DEEP_RESEARCH
A1_AUDIT
E1_EXECUTION_BRIEF
F0_FAST_DIRECT
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
| D0_DIRECTION_SETUP | Direction Setup | Create or repair a Direction container and hand off to phase start when ready. | `workflow/stage_prompts/D0_DIRECTION_SETUP.md` | present | chatgpt_direction_project | available | P0_PHASE_START |
| P0_PHASE_START | Phase Start | Start or update current Phase by Critical Constraint and Minimum Outcome. | `workflow/stage_prompts/P0_PHASE_START.md` | present | chatgpt_direction_project | available | I0_CAPTURE, G0_GOAL_SELECT, G1_GOAL_SHAPE |
| I0_CAPTURE | Capture / Triage | Route raw inputs without doing the downstream work. | `workflow/stage_prompts/I0_CAPTURE.md` | present | chatgpt_direction_project | available | G0_GOAL_SELECT, G1_GOAL_SHAPE, S3_DECIDE, B1_PROBLEM, Stop |
| G0_GOAL_SELECT | Goal Select | Select or create one candidate for Goal shaping. | `workflow/stage_prompts/G0_GOAL_SELECT.md` | present | chatgpt_direction_project | available | G1_GOAL_SHAPE |
| G1_GOAL_SHAPE | Goal Shape / Ruthless Cut | Shape WHAT / WHY / DONE and cut scope before HOW. | `workflow/stage_prompts/G1_GOAL_SHAPE.md` | present | chatgpt_direction_project | available | F0_FAST_DIRECT, E1_EXECUTION_BRIEF, S3_DECIDE, D1_DEEP_RESEARCH, A1_AUDIT, B1_PROBLEM, Stop |
| S3_DECIDE | Decide | Resolve a real decision with options, constraints, and human conclusion. | `workflow/stage_prompts/S3_DECIDE.md` | present | chatgpt_direction_project | available | G1_GOAL_SHAPE, E1_EXECUTION_BRIEF, R1_GOAL_REVIEW_DISTILL, Stop |
| D1_DEEP_RESEARCH | Deep Research | Research external evidence gaps and synthesize decision implications. | `workflow/stage_prompts/D1_DEEP_RESEARCH.md` | present | chatgpt_direction_project | available | S3_DECIDE, G1_GOAL_SHAPE, E1_EXECUTION_BRIEF, Stop |
| A1_AUDIT | Audit / Challenge | Challenge high-risk, failed, irreversible, or unsupported plans and claims. | `workflow/stage_prompts/A1_AUDIT.md` | present | chatgpt_direction_project | available | S3_DECIDE, G1_GOAL_SHAPE, E1_EXECUTION_BRIEF, R1_GOAL_REVIEW_DISTILL, Stop |
| E1_EXECUTION_BRIEF | Execution Brief | Produce minimum HOW, validation, context, and Codex card if needed. | `workflow/stage_prompts/E1_EXECUTION_BRIEF.md` | present | chatgpt_direction_project | available | F0_FAST_DIRECT, C1_CODEX_GRAPH_PLAN, B1_PROBLEM, Stop |
| F0_FAST_DIRECT | Fast Direct | Execute small reversible non-Codex work directly with verification. | `workflow/stage_prompts/F0_FAST_DIRECT.md` | present | chatgpt_direction_project | available | R1_GOAL_REVIEW_DISTILL, E1_EXECUTION_BRIEF, B1_PROBLEM, Stop |
| C1_CODEX_GRAPH_PLAN | Codex Graph Plan | Build and validate project-local Codex execution graph from accepted context. | `workflow/stage_prompts/C1_CODEX_GRAPH_PLAN.md` | present | chatgpt_direction_project | available | C2_CODEX_EXECUTE, Context Request, Human Decision, Stop |
| C2_CODEX_EXECUTE | Codex Execute | Execute a validated Codex graph and return evidence / return-state. | `workflow/stage_prompts/C2_CODEX_EXECUTE.md` | present | codex | available | R1_GOAL_REVIEW_DISTILL, E1_EXECUTION_BRIEF, B1_PROBLEM, Stop |
| B1_PROBLEM | Problem Router | Classify blockers before solving and route recovery. | `workflow/stage_prompts/B1_PROBLEM.md` | present | chatgpt_direction_project | available | continue_current_stage, E1_EXECUTION_BRIEF, G1_GOAL_SHAPE, S3_DECIDE, R1_GOAL_REVIEW_DISTILL, Stop |
| R1_GOAL_REVIEW_DISTILL | Goal Review / Distill | Review Goal outcome, distill durable knowledge, and update state / docs. | `workflow/stage_prompts/R1_GOAL_REVIEW_DISTILL.md` | present | chatgpt_direction_project | available | G0_GOAL_SELECT, G1_GOAL_SHAPE, P9_PHASE_CLOSE, P0_PHASE_START, Stop |
| P9_PHASE_CLOSE | Phase Close | Close or pause Phase and distill phase-level outcomes. | `workflow/stage_prompts/P9_PHASE_CLOSE.md` | present | chatgpt_direction_project | available | P0_PHASE_START, G0_GOAL_SELECT, Direction pause/archive, Stop |
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
5. Packet contracts live in `workflow/runtime/WF_VNEXT_R_RUNTIME_CORE.md`.
6. Direction Project Files must not contain stage prompt bodies.
7. Stage prompt paths must use `workflow/stage_prompts/<STAGE_ID>.md`.

If a launch card names an unknown stage ID, return a Context Request or registry amendment request instead of guessing.
