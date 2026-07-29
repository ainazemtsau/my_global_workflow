RESULT s-health-repair-before-nutrition-converge-001 (call: c-health-repair-before-nutrition-converge-001)
direction: health   play: repair   node/task: g-health-core + g-health-nutrition-system/repair

outcome: |
  live/health/TREE.md already matches the accepted state after corrected g-health-core G5:
  g-health-core is done and g-health-nutrition-system is parked.

  live/health/NOW.md was repaired: the stale next CALL to nutrition shape was replaced with
  c-health-nutrition-converge-001. The next leg now routes nutrition through converge as a module
  on g-health-core, while treating prior nutrition v1 and paused Define artifacts as dirty input
  evidence only.

evidence: |
  Contradiction named:
  - The CALL described an older visible state where g-health-core closure was still pending, but the
    local repo already contains the corrected review evidence, owner approval, TREE close, and no active bet.
  - The remaining live contradiction was NOW.next = c-health-nutrition-shape-001, while nutrition reset
    evidence, core-first map evidence, and the current owner/CALL instruction require nutrition converge
    if core closure evidence is sufficient.

  Reconstruction newest-first:
  - Current live/health/TREE.md: g-health-core.status = done; g-health-nutrition-system.status = parked.
  - Current live/health/knowledge/health-core-corrected-g5-review.md exists and records c-health-core-review-002:
    corrected binding G5 met; fresh separate review/refutation satisfied G5; cross-family review is optional
    unless explicitly requested; product blocker gaps 0 at health-ai commit 8bc980ad21d3f54cbd27b28dcb363e0198c46751.
  - live/health/history/2026-06-15-c-health-core-review-002.md records corrected_binding_g5_verdict: met and
    proposes owner decision d-health-core-close-and-next-bet.
  - live/health/history/2026-06-15-s-health-core-review-002-approval.md records owner words "approve" and applied
    g-health-core active -> done. This supports core closure and nutrition as next node, but its next CALL used
    the stale shape route.
  - live/health/history/2026-06-13-s-health-nutrition-reset-001.md records owner-approved reset of nutrition:
    node back to parked, all v1 decisions/data/architecture dirty, next = c-health-nutrition-converge-001 in a fresh chat.
  - live/health/history/2026-06-14-s-health-reframe-map-001.md records owner "ok" to the core-first map:
    build order core -> nutrition -> training, with nutrition/training as modules on core; paused nutrition Define
    and recon work are input evidence, not authority.
  - live/health/work/converge-health-nutrition-input.md and
    live/health/work/converge-nutrition-define-draft.md are present and explicitly marked dirty/unratified input.

  Sufficiency:
  - Core closure evidence is sufficient: corrected review met + owner "approve" + TREE already done.
  - Nutrition converge evidence is sufficient: owner-approved reset explicitly set next = converge from scratch,
    and the current CALL says next must be nutrition converge, not shape, when evidence supports closure.
  - No raw daily food, weight, or check-in logs were stored in Direction OS.

state_changes: |
  NOW.md:
  - Replace active_bet.note with:
      No active bet after owner-approved close of g-health-core. Corrected G5 verdict
      was met in c-health-core-review-002; owner approved closing the node with
      "approve". Nutrition is parked after its 2026-06-13 reset; prior v1 and
      paused Define artifacts are dirty input evidence only, so the next route is
      c-health-nutrition-converge-001, not shape.
  - Keep active_bet.status: none.
  - Keep tasks: [].
  - Keep recurring: [].
  - Keep open_calls: [].
  - Keep decisions: [].
  - Replace next with:
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

  TREE.md:
  - No change. Current TREE already matches accepted state: g-health-core done; g-health-nutrition-system parked.
  - No new owner_approved mark is added. Existing TREE approvals are the cited owner words "approve" for core
    closure and the 2026-06-13 reset instruction for nutrition.

  LOG.md:
  - Append:
      - 2026-06-16 — health repair before nutrition converge: reconciled visible core-closed state with nutrition reset/core-first evidence; TREE already matched accepted state, NOW rerouted from stale shape CALL to c-health-nutrition-converge-001. → history/2026-06-16-s-health-repair-before-nutrition-converge-001.md

  history/:
  - Add live/health/history/2026-06-16-s-health-repair-before-nutrition-converge-001.md containing this RESULT.

captures: []

decisions_needed: []

play_check:
  - 1 Name the contradiction: done — CALL's old visible-state description is superseded locally by core close; live contradiction is stale nutrition shape next vs reset/core-first/current CALL converge route.
  - 2 Reconstruct: done — newest-first through current TREE/NOW/knowledge, LOG tail, 2026-06-15 review/approval history, 2026-06-13 nutrition reset, 2026-06-14 core-first map, and dirty work artifacts.
  - 3 Propose corrected state: done — TREE no-op; NOW note and next CALL corrected to c-health-nutrition-converge-001 with dirty-input boundaries.
  - 4 Confirm: done — current owner/CALL explicitly says if core closure evidence is sufficient, next is nutrition converge, not shape; no new TREE/CHARTER change needs G9 approval.
  - 5 Friction: skipped — no new OS rule defect isolated; this is a one-off stale next-route repair over already logged desync/fresh-review routing history.

log: >
  2026-06-16 — health repair before nutrition converge: reconciled visible core-closed state with nutrition reset/core-first evidence; TREE already matched accepted state, NOW rerouted from stale shape CALL to c-health-nutrition-converge-001.

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

END_OF_FILE: live/health/history/2026-06-16-s-health-repair-before-nutrition-converge-001.md
