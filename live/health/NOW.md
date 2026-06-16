# NOW — health

active_bet:
  status: none
  note: >
    No active bet after owner-approved close of g-health-core. Corrected G5 verdict
    was met in c-health-core-review-002; owner approved closing the node with
    "approve". Nutrition is parked after its 2026-06-13 reset; prior v1 and
    paused Define artifacts are dirty input evidence only, so the next route is
    c-health-nutrition-converge-001, not shape.

tasks: []

recurring: []

open_calls: []

decisions: []

next: |
  CALL c-health-nutrition-converge-001
  to: session
  direction: health
  play: converge
  node: g-health-nutrition-system
  goal: |
    g-health-nutrition-system has a closed, owner-signed WHAT spec for a nutrition
    module on g-health-core, with dirty v1 inputs refuted, re-derived, or rejected
    as authority.
  context: |
    Owner approved decision d-health-core-close-and-next-bet with: "approve".
    This closes g-health-core as done and selects g-health-nutrition-system next.

    c-health-core-review-002 returned corrected binding G5 verdict met for g-health-core.
    live/health/knowledge/health-core-corrected-g5-review.md records the accepted
    fact: fresh separate G5 review/refutation met; hard cross-family review is not
    a requirement unless explicitly requested.

    Nutrition was reset on 2026-06-13:
    - live/health/history/2026-06-13-s-health-nutrition-reset-001.md
    - TREE g-health-nutrition-system returned to parked
    - all v1 decisions/data/architecture are dirty input only
    - next route from reset was c-health-nutrition-converge-001 in a fresh chat

    Read:
    - live/health/CHARTER.md
    - live/health/TREE.md
    - live/health/NOW.md
    - live/health/knowledge/health-core-corrected-g5-review.md
    - live/health/history/2026-06-13-s-health-nutrition-reset-001.md
    - live/health/history/2026-06-14-s-health-reframe-map-001.md
    - live/health/work/converge-health-nutrition-input.md
    - live/health/work/converge-nutrition-define-draft.md
    - health-ai commit 8bc980ad21d3f54cbd27b28dcb363e0198c46751 and its acceptance/core evidence

    Core contract to consume:
    - nutrition is a module on g-health-core, not a duplicate core
    - consume core-owned metrics, phase, PLAN-vs-LOG, review, parser/library, value grammar, and safety floor
    - raw daily food/weight data stays in Health AI, not Direction OS
  boundaries: |
    Do not store raw daily food, weight, or check-in logs in Direction OS.
    Do not import prior nutrition v1, converge input, or paused Define draft as authority.
    Do not build product repo implementation.
    Do not build training/activity module.
    Do not build app UI, runtime, DB, server, cron, or scheduler.
    Do not make medical prescriptions.
    Do not rewrite g-health-core; nutrition consumes it.
  done_when: |
    - work/converge-g-health-nutrition-system.md has a closed nutrition WHAT spec with no open/deferred rows.
    - Dirty v1 inputs are refuted, re-derived, or explicitly rejected as authority.
    - The nutrition expert-variable vs irreducible-owner-fact boundary is owner-signed.
    - Nutrition is specified as a module on g-health-core, consuming core-owned shared concepts without duplicating them.
    - Next CALL routes to the next valid OS leg after converge.
  return: |
    RESULT with the converge artifact path, owner signoffs, evidence, state_changes, decisions_needed, and next CALL/awaiting_decision.
  budget: one focused converge movement
  surface: any capable session

END_OF_FILE: live/health/NOW.md
