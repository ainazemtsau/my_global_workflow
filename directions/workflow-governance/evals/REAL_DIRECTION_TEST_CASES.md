# Real Direction Test Cases

Use this file to record real Direction behavior test cases.

## Test case shape

```yaml
test_case:
  test_id:
  direction_path:
  scenario:
  files_loaded:
  expected_behavior:
  actual_behavior:
  result:
  finding_id:
```

## Rules

- Use `directions/*/project_files/` only when auditing real Direction behavior.
- Do not load sibling Directions by default.
- Do not modify tested Direction files unless a separate approved repository patch authorizes it.

## Direction Map / M0 real Direction cases

These cases are generic regression scenarios only. They must not populate real `08_DIRECTION_MAP.md` files or invent Direction-specific strategy.

| Test ID | Direction path | Scenario | Files loaded | Expected behavior |
| --- | --- | --- | --- | --- |
| RD-DMAP-001 | `directions/workflow-governance/` | Workflow Governance maintenance request, Active Goal none | Target Direction Project Files `00-08`; maintenance packet | Maintenance mode continues; no forced G0; M0 only when map state is material to the maintenance route. |
| RD-DMAP-002 | `directions/solo-max-productive/` | Uninitialized 08 and new strategic Phase request | Target Direction Project Files `00-08`; user Phase request | Route to `M0_DIRECTION_MAP` migration before P0; do not invent Active Front or Horizon Slice. |
| RD-DMAP-003 | `directions/indie-game-development/` | User provides Current Initiative during M0 migration | Target Direction Project Files `00-08`; user-provided initiative | M0 reads `00-07`, validates/shapes the initiative against current progress, and only then proposes map acceptance. |
| RD-DMAP-004 | `directions/health-and-beauty/` | Active/local Goal continuation while 08 is uninitialized | Target Direction Project Files `00-08`; active Goal context | Do not interrupt safe local Goal work; schedule or route M0 when a strategic choice is needed. |
| RD-DMAP-005 | Any active Direction | User asks for parked or future node | Target Direction Project Files `00-08`; user request | Route to `M0_DIRECTION_MAP` or Human Decision before execution or normal Goal shaping. |
| RD-DMAP-006 | Any active Direction with parallel work | Parallel branch returns map-relevant output | Branch context plus parent synthesis packet | Branch returns Evidence Packet / Node Result Card only; parent synthesis owns any map update proposal. |

## Large Goal Branch/Workstream Test Case

Scenario:

A Direction has a large technical foundation Goal that requires:

- current external research;
- old project audit;
- architecture decision input;
- parent synthesis.

Expected behavior:

- E1 does not launch one monolithic execution thread.
- E1 produces Topology Preview or Topology Launch Bundle.
- D1 branch returns compact research Workstream Result Card.
- A1 branch returns compact audit Workstream Result Card.
- Parent synthesis reads cards first.
- Parent requests full artifacts only if conflict, low confidence, missing evidence, R1 challenge, or user request requires it.
- Branch chats do not mutate parent state.
- R1 reviews only the final parent synthesis artifact.

## Lifecycle State Reconciliation real Direction incident case

```yaml
test_case:
  test_id: RD-LSRG-001
  direction_path: directions/indie-game-development/
  scenario: >
    F0 final synthesis for first-technical-nucleus-functional-spec produced a
    synthesis_formalized parent Goal completion candidate and execution evidence
    for R1, while Direction Project Files and Phase Brief still showed
    goal_shaped_pending_E1 and next_route E1_EXECUTION_BRIEF.
  files_loaded:
    - directions/indie-game-development/phases/core-coop-technical-foundation-selection/goals/first-technical-nucleus-functional-spec/01_FIRST_TECHNICAL_NUCLEUS_FUNCTIONAL_SPEC.md
    - directions/indie-game-development/phases/core-coop-technical-foundation-selection/goals/first-technical-nucleus-functional-spec/execution_log.md
    - directions/indie-game-development/project_files/04_ACTIVE_GOAL.md
    - directions/indie-game-development/project_files/02_CURRENT_PHASE.md
    - directions/indie-game-development/phases/core-coop-technical-foundation-selection/00_PHASE_BRIEF.md
  expected_behavior: >
    Workflow must update runtime projection files, launch R1 with an explicit
    stale-but-nonblocking override and fresh sources, or return Context Request
    for state reconciliation. It must not silently route backward to E1.
  actual_behavior: "Recorded incident; fixed by shared LSRG hardening plus separate Direction incident repair."
  result: regression_added
  finding_id: WFG-FINDING-2026-05-18-001
```
