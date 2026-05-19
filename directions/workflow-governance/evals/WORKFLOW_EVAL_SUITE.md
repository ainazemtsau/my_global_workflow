# WORKFLOW_EVAL_SUITE

This file defines audit lenses for Workflow Governance.

## Audit lenses

### runtime contract audit

Checks whether runtime packets, formalization control, repository patch behavior, and stage launch/return contracts remain coherent.

### lifecycle logic audit

Checks phase, goal, review, closure, router, and recovery transitions.

### UX/human burden audit

Checks whether the workflow asks too much of the user, produces wall-of-text, hides decisions, or fails to provide reviewable work product before formalization.

### context hygiene audit

Checks default loads, stage prompt request rules, Direction boundaries, and whether context is stale, excessive, or cross-contaminated.

### real usage friction audit

Checks issues observed in real Direction use, including confusing next routes, approval ambiguity, or Codex repository maintenance friction.

### external best-practice/research audit

Checks source-backed facts vs inference from external research and whether any workflow change is justified.

## Direction Map / M0 regression cases

These cases verify that `08_DIRECTION_MAP.md` is routing context, not a backlog, dated roadmap, or replacement for Phase/Goal lifecycle stages.

| ID | Case | Expected behavior |
| --- | --- | --- |
| DMAP-001 | Missing or uninitialized `08_DIRECTION_MAP.md` with no active Phase | Router/D0/P0 routes to `M0_DIRECTION_MAP` before material strategic Phase selection. |
| DMAP-002 | Uninitialized map with active Goal in progress | Safe local execution continues unless the user asks for map review or the missing map blocks routing. |
| DMAP-003 | User asks for parked or future node | Router/G0 routes to `M0_DIRECTION_MAP` or Human Decision before Goal shaping or execution. |
| DMAP-004 | P0 selects new Phase | P0 cites Direction Map Active Front/Horizon Slice and the Phase Memory anti-duplicate line. |
| DMAP-005 | G1 shapes Goal from map context | Goal Contract includes `map_binding`, `expected_map_delta`, why the Goal is minimal, and why it is not premature. |
| DMAP-006 | E1 sees evidence or decision node gap | E1 routes to D1/A1/S3 or decision topology instead of F0 when evidence or decision gaps remain. |
| DMAP-007 | Parallel branch state safety | Branch chat cannot mutate `08_DIRECTION_MAP.md`; it returns Evidence Packet / Node Result Card for parent synthesis. |
| DMAP-008 | R1 reviews Goal with map impact | R1 proposes `map_delta` and runs `phase_progress_gate` before any next G0. |
| DMAP-009 | P9 closes or pauses Phase | P9 updates Phase Memory and proposes Direction Map frontier changes or `M0_DIRECTION_MAP` review. |
| DMAP-010 | M0 prompt or registry availability unknown | Return Context Request or registry amendment need; do not guess M0 execution. |
| DMAP-011 | Map bloat prevention | Direction Map stays compact; excessive nodes are cut, parked, split, or deferred. |
| DMAP-012 | Cross-Direction refresh after shared runtime/cache change | Return refresh requirements for all active Direction Projects, including `08_DIRECTION_MAP.md` impact. |

## Lifecycle State Reconciliation / EOF regression cases

These cases verify that Workflow does not launch a next material stage through stale or contradictory runtime projections.

| ID | Case | Expected behavior |
| --- | --- | --- |
| LSRG-001 | Final F0 synthesis creates parent completion candidate and next route R1 while Project Files still say E1. | Fail closed unless runtime projection files are updated, an explicit stale-but-nonblocking R1 override is supplied, or Context Request is returned. |
| LSRG-002 | Gated slice complete but parent Goal incomplete tries normal parent-level R1. | Reject R1; route to E1 continuation or correction. |
| LSRG-003 | R1 launch has stale Project Files and no fresh evidence bundle. | Return Context Request; do not review or close. |
| LSRG-004 | R1 launch has stale Project Files, explicit stale override, and fresh verified sources. | Allow R1 review using the named fresh sources only. |
| LSRG-005 | `END_OF_FILE` marker appears before later content. | Structural validation fails; next material launch blocked until repaired. |
| LSRG-006 | `append_section` appends below EOF. | Repository maintenance return fails structural validation. |
| LSRG-007 | Codex reports `project_files_cache_refresh_required: false` while logical runtime state changed and Project Files are stale. | Return validation failure; require lifecycle projection classification. |
| LSRG-008 | R1 accepts Goal and routes to G0 without phase_progress_gate. | Fail; R1 must run Phase Progress Gate first. |

## Rule

Findings must go through `FINDING_REGISTER.md`. No repository patch until approval.
