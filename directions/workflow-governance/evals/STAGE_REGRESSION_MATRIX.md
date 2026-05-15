# Stage Regression Matrix

Use this matrix to track stage-level regression checks.

## Matrix columns

| Stage ID | Area | Expected behavior | Regression risk | Last checked | Result | Finding ID |
| --- | --- | --- | --- | --- | --- | --- |

## Current entries

| Stage ID | Area | Expected behavior | Regression risk | Last checked | Result | Finding ID |
| --- | --- | --- | --- | --- | --- | --- |
| ROUTER_STAGE_LAUNCHER | Direction Map awareness | Checks map status and routes to `M0_DIRECTION_MAP` only when a material strategic Phase/Goal choice depends on missing, stale, disputed, or uninitialized map context. | Forcing M0 on every launch or bypassing M0 when map state blocks routing. | 2026-05-15 | Added regression expectation | N/A |
| D0_DIRECTION_SETUP | Direction setup handoff | Verifies `08_DIRECTION_MAP.md` presence/state and recommends M0 before P0 when map migration is material; does not build the map itself. | D0 populates map content or skips needed M0 migration. | 2026-05-15 | Added regression expectation | N/A |
| M0_DIRECTION_MAP | Conditional map optimizer/review | Creates, reviews, updates, or migrates compact Direction Map / Current Initiative / Active Front / Horizon Slice without doing P0/G0/G1/E1/R1/P9 work. | Treating M0 as lifecycle replacement, execution planner, or broad backlog builder. | 2026-05-15 | Added regression expectation | N/A |
| P0_PHASE_START | Phase map binding | Selects a new or changed Phase from initialized Active Front/Horizon Slice when relevant and keeps Phase Memory anti-duplicate checks active. | Inventing a Phase from uninitialized map context or ignoring Phase Memory. | 2026-05-15 | Added regression expectation | N/A |
| G0_GOAL_SELECT | Candidate filter | Prefers candidates that advance current Phase plus map node/edge when initialized; parked/future or initiative-switch requests route to M0/Human Decision. | Selecting future-node work as normal Goal execution. | 2026-05-15 | Added regression expectation | N/A |
| G1_GOAL_SHAPE | Goal map binding | Includes compact `map_binding` and `expected_map_delta` when applicable, while preserving WHY/WHAT/DONE scope discipline. | Expanding Goal into map planning or omitting needed map binding. | 2026-05-15 | Added regression expectation | N/A |
| E1_EXECUTION_BRIEF | Map topology gate | Uses map node type, dependencies, and parallel-safety flags to choose F0/Codex/D1/A1/S3/decision topology; branch outputs cannot mutate 08. | Sending evidence/decision gaps to F0 or letting branch chats update the map. | 2026-05-15 | Added regression expectation | N/A |
| R1_GOAL_REVIEW_DISTILL | Goal map delta | Proposes `map_delta` when Goal outcome affects strategy and runs `phase_progress_gate` before any next G0. | Silent map rewrite or next-goal routing without phase progress check. | 2026-05-15 | Added regression expectation | N/A |
| P9_PHASE_CLOSE | Frontier review | Updates Phase Memory and adds compact Direction Map frontier review or M0 route before next P0 when map repair/initiative switch is needed. | Replacing Phase Memory with map notes or creating a broad future plan. | 2026-05-15 | Added regression expectation | N/A |

This matrix is behavioral coverage only. `allowed_next` transition authority remains registry-owned in `workflow/stage_registry/STAGE_REGISTRY.md`; do not duplicate it here.
