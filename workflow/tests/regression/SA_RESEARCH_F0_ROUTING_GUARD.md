# SA Research/F0 Routing Guard Regression Tests

Status: active regression
Workflow version: vNext-R
Source GitHub repository file: `workflow/tests/regression/SA_RESEARCH_F0_ROUTING_GUARD.md`
Authority: GitHub repository canonical after file read-back / diff verification / commit verification.
Purpose: prevent E1/F0/Router from bypassing D1 or entering F0 when research/planning/tooling ambiguity is unresolved.

## Test 1 — E1 current-platform research gap

Input:
- Stage: E1_EXECUTION_BRIEF
- Goal requires a nutrition operating layer.
- Execution depends on current ChatGPT Projects/connectors/storage/restart behavior.

Expected:
- `research_required: true`
- selected route: `D1_DEEP_RESEARCH`, or route-conflict Context Request/B1 if registry disallows D1.
- forbidden: `F0_FAST_DIRECT`
- forbidden: research findings inside E1

## Test 2 — User explicitly confirms research during E1

Input:
- E1 preview initially proposes execution.
- User says: "да, проведем research".

Expected:
- E1 revises route only.
- E1 does not perform research.
- E1 emits D1 launch or route-conflict blocker.

## Test 3 — Registry/prompt route mismatch

Input:
- Prompt-selected route is allowed by prompt but missing from STAGE_REGISTRY.

Expected:
- route_conflict is reported.
- terminal output is Context Request or B1_PROBLEM.
- forbidden: silently choose F0.
- forbidden: execute downstream work inside current stage.

## Test 4 — Router refuses F0 when readiness is unknown

Input:
- Active Goal exists.
- User asks for a seemingly small implementation.
- Target paths, validation, and research_required=false are not explicit.

Expected:
- Router does not route to F0.
- Router routes to E1_EXECUTION_BRIEF or Context Request.
- Visible explanation includes "Почему не F0".

## Test 5 — F0 intake refuses hidden planning risk

Input:
- F0 launch exists.
- During intake, F0 detects hidden implementation/code/tooling risk or unclear validation.

Expected:
- F0 returns `result_state: escalated | needs_context`.
- Repository Patch: explicit none.
- Next safe route: E1_EXECUTION_BRIEF, B1_PROBLEM, or C1 through E1/B1.
- Visible explanation includes failed readiness item.

## Test 6 — Valid F0

Input:
- One active Goal.
- One bounded execution slice.
- Exact artifact and target path.
- Acceptance checks are concrete.
- research_required=false.
- no current external facts needed.
- no architecture/tooling decision.
- no graph/wave planning.
- no multi-file coordination.

Expected:
- E1 or Router may route to F0_FAST_DIRECT.
- F0 may produce Work Product Preview first.
- F0 may produce repository_patch only after approval/formalization.
- F0 may route to R1 only after apply/read-back/diff/commit evidence.

## Test 7 — F0 completed one gated block under incomplete parent Goal

Input:
- Parent Goal contains multiple gated blocks.
- Topology: `gated_sequential`.
- F0 completed `gas_simulation_capability_frame` only.
- Later blocks remain blocked placeholders.
- Parent Goal completion state: incomplete.

Expected:
- F0 must not select normal parent-level `R1_GOAL_REVIEW_DISTILL`.
- Next route must be `E1_EXECUTION_BRIEF` continuation.
- Parent Goal must not be marked complete.
- `phase_progress_gate` must not run.
- Later blocks remain blocked until valid continuation planning.

## Read-back anchors

- "Research/F0 Routing Guard"
- "research_required: true"
- "Почему не F0"
- "route_conflict"
- "F0 Intake Readiness Gate"
- "Fast-Failure Pattern Gate"
- "gas_simulation_capability_frame"
- "gated_sequential"
