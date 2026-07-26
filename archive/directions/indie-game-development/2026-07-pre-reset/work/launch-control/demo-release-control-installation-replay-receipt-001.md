# Demo Release Control installation - deterministic replay receipt 001

evaluated: 2026-07-24
policy: `knowledge/g-b847-demo-release-control-policy-v1.md` @ `e171a512af7a25dc0468e677c3997c08645d3435`
controller: `c-work-launch-control-demo-release-control-cycle-001`
method: specified synthetic input projected directly through current policy; no
live status substituted.
DCR authority reads/edits during evaluation: **0 / 0**

| # | scenario | expected | actual | verdict |
|---:|---|---|---|---|
| 1 | NO-BASIS | `R0 GAP; UNFORECASTABLE / NO DATE BASIS; affected work WAIT; definition launch NONE` | `R0 GAP; UNFORECASTABLE / NO DATE BASIS; affected work WAIT; definition launch NONE` | **PASS** |
| 2 | MISSED | `MISSED wins; February inactive without owner words` | `MISSED wins; February inactive without owner words` | **PASS** |
| 3 | CREDIBLE | `CREDIBLE; conservative upper bound + owner margin clear every gate; blocker NONE` | `CREDIBLE; conservative upper bound + owner margin clear every gate; blocker NONE` | **PASS** |
| 4 | AT-RISK | `AT RISK; optional Press Preview cut/owner decision named; recompute; no route switch` | `AT RISK; optional Press Preview cut/owner decision named; recompute; no route switch` | **PASS** |
| 5 | BASIS-STALE | `exclude B1 launch; target-owned RECONCILE; controller paste NONE` | `exclude B1 launch; target-owned RECONCILE; controller paste NONE` | **PASS** |
| 6 | INDEPENDENT | `rank Grid and Gas; Character WAITING and Program BLOCKED are not global gates` | `rank Grid and Gas; Character WAITING and Program BLOCKED are not global gates` | **PASS** |
| 7 | RESOURCE-UNKNOWN | `PROTECT/exclude only UNKNOWN shared surface; unrelated candidate survives` | `PROTECT/exclude only UNKNOWN shared surface; unrelated candidate survives` | **PASS** |
| 8 | ZERO | `launch set 0; exact blockers; controller READY; busywork NONE` | `launch set 0; exact blockers; controller READY; busywork NONE` | **PASS** |
| 9 | MANY | `show both independent outcomes; owner chooses 0..N; no auto-launch/foreign mutation` | `show both independent outcomes; owner chooses 0..N; no auto-launch/foreign mutation` | **PASS** |
| 10 | RECOVERY | `STABILIZE affected proof; bounded PROBATION of missing mechanism; broader invalidation REPLAN; copied status NONE` | `STABILIZE affected proof; bounded PROBATION of missing mechanism; broader invalidation REPLAN; copied status NONE` | **PASS** |

Readback: **10 scenarios; 10 PASS; 0 FAIL; DCR authority reads/edits 0/0.**
This is not the seven-day material-return probe, release progress or binding
post-install G5.

END_OF_FILE: live/indie-game-development/work/launch-control/demo-release-control-installation-replay-receipt-001.md
