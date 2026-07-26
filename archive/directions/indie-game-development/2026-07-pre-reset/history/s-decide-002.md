# s-decide-002 — decide (g-9c41): owner resolves d-converge-001 = A (feed the converge set into the live PLAN)

- **date:** 2026-06-14
- **play:** decide (owner-decision resolution; cf. s-decide-001 precedent — no `decide` play exists, logged as friction)
- **node:** g-9c41
- **input:** owner plain message «давай вариант A / запушь и синхронизируй ветки»
- **role:** session → became its own writer after RESULT (agent-CLI on this repo)

## What was decided

d-converge-001 (raised at s-converge-001): should the g-9c41 converge set feed the in-flight c-exec-003
PLAN before ADR-0003 freezes the stream magnitudes, or stay parallel/demonstrative? **Owner chose A**
(the recommended option): feed work/converge-g-9c41.md into the c-exec-003 interactive PLAN as mandatory
input evidence. The owner's live instruction outranks the prior CALL's "don't touch the bet" boundary
(authority order: live owner instruction > kernel > play > state), so wiring the converge set into the
c-exec-003 CALL is now authorized.

## RESULT

```yaml
RESULT s-decide-002 (owner decision: d-converge-001 = A)
direction: indie-game-development   play: decide   node/task: g-9c41
outcome: |
  d-converge-001 resolved = A. The converge set work/converge-g-9c41.md is wired into the in-flight
  c-exec-003 executor CALL as mandatory PLAN input evidence: (1) a ⭐ context pointer naming it the
  binding input the PLAN ratifies (not a binding spec — PLAN still owns design), listing the C1–C22
  named parameter questions + the 4 the CALL left implicit (C19/C20/C21/C22); (2) a leg_opens_with
  FIRST-PLAN-STEP directive: read the converge set and freeze ADR-0003 AGAINST the named set, explicitly
  resolving C19/C20/C21/C22. This realizes the retrofit's value on the live build: ADR-0003 ratifies the
  converge questions instead of re-inventing them. converge-arch (c-converge-002) stays parallel and
  ungated (under A it refines the B-row contracts but does not gate the PLAN).
evidence: |
  NOW.md decision_inbox d-converge-001 status open→answered (owner words «давай вариант A»); NOW.next
  c-exec-003 context gained the ⭐ converge-set pointer; NOW.next leg_opens_with gained the FIRST-PLAN-STEP
  ratify directive; c-exec-003 open_call note records the wiring. Cross-repo note: the converge doc lives
  in the OS state repo, so the relay dispatching c-exec-003 must carry its §WHAT-C + §COVERAGE + WITNESS
  CHECK to the product-repo PLAN session.
state_changes: |
  NOW.md: decision_inbox d-converge-001 → answered (A, owner words); next: c-exec-003 context += converge-set
    pointer; next: c-exec-003 leg_opens_with += FIRST-PLAN-STEP ratify directive; open_calls c-exec-003 note
    += wiring ref; open_calls c-converge-002 note: gating line → "resolved = A, parallel/ungated".
    active_bet, active_tasks (t-1/t-2/t-3 goals/status), kill_by UNCHANGED; only the c-exec-003 CALL's
    input-evidence pointers changed (authorized by the owner's live A decision).
  LOG.md: + decide line → history/s-decide-002.md.
  history/: + s-decide-002.md (this RESULT). No TREE/CHARTER/work change.
captures:
  - "friction (re-occurrence, already noted s-repair-007): no `decide` play exists; owner-decision resolutions are logged ad hoc as s-decide-NNN. Candidate maintenance item, not fixed here."
decisions_needed: []
play_check:
  - "resolve: done — owner «давай вариант A» applied; d-converge-001 → answered."
  - "wire: done — converge set added to c-exec-003 context + leg_opens_with as mandatory PLAN input; boundary lift authorized by the live owner decision."
  - "close: this RESULT; bet/tasks untouched beyond the authorized CALL-input wiring; next = the c-exec-003 PLAN consumes it (in the product repo) + converge-arch c-converge-002 in parallel."
log: "2026-06-14 — decide (g-9c41): owner resolved d-converge-001 = A — converge set work/converge-g-9c41.md wired into the in-flight c-exec-003 CALL (context + leg_opens_with FIRST-PLAN-STEP) as mandatory input; ADR-0003 ratifies the named §WHAT-C questions (C1–C22, incl. the implicit C19/C20/C21/C22) instead of re-deriving. converge-arch c-converge-002 stays parallel/ungated. → history/s-decide-002.md"
next: |
  Two parallel threads, both ready:
  - c-exec-003 (build, in the product repo GasCoopGame_dev) — the interactive PLAN now opens by consuming
    work/converge-g-9c41.md and ratifying C1–C22 into ADR-0003 (owner present, frontier model).
  - c-converge-002 (converge-arch, OS state repo) — declare the §WHAT-B cross-node contracts; refines what
    the magnitudes must satisfy; parallel to the build under decision A.
```

END_OF_FILE: live/indie-game-development/history/s-decide-002.md
