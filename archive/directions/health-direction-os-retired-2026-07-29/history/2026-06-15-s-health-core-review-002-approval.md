RESULT s-health-core-review-002-approval (call: c-health-core-review-002)
direction: health   play: review   node/task: g-health-core/review

outcome: |
  Owner approved closing g-health-core as done and accepted recommendation A from
  d-health-core-close-and-next-bet.

  g-health-core is now closed in TREE as done. NOW has no active bet and the next
  ready CALL is c-health-nutrition-shape-001 to shape g-health-nutrition-system
  as the first module-on-core bet.

evidence: |
  Owner answer in-session:
  - "approve"

  This answers decision d-health-core-close-and-next-bet:
  - A: Approve g-health-core done; shape g-health-nutrition-system next.
  - B: Approve g-health-core done; shape g-health-training-activity-system next.
  - C: Approve g-health-core done; pause the direction after core.

  Because the decision carried recommendation A and the owner answered "approve",
  this is interpreted as approval of recommendation A.

state_changes: |
  TREE.md:
  - owner_approved: true
  - approval_evidence: >
      Owner answered the pending decision with:
      "approve"
  - For node g-health-core:
      status: active -> done
  - Keep appetite and kill_by as historical evidence.
  - Keep children: [].

  NOW.md:
  - Replace active_bet with:
      status: none
      note: >
        No active bet after owner-approved close of g-health-core. Corrected G5 verdict
        was met in c-health-core-review-002; owner approved closing the node and taking
        recommendation A, shaping g-health-nutrition-system next.
  - Replace tasks with [].
  - Keep recurring: [].
  - Keep open_calls: [].
  - Replace decisions with [].
  - Set next to:
      CALL c-health-nutrition-shape-001
      to: session
      direction: health
      play: shape
      node: g-health-nutrition-system
      goal: |
        g-health-nutrition-system is shaped as the first module-on-core bet after g-health-core closure.
      context: |
        Owner approved decision d-health-core-close-and-next-bet with: "approve".
        This closes g-health-core as done and selects recommendation A: shape g-health-nutrition-system next.

        c-health-core-review-002 returned corrected binding G5 verdict met for g-health-core.

        Read:
        - live/health/CHARTER.md
        - live/health/TREE.md
        - live/health/NOW.md
        - live/health/knowledge/health-core-corrected-g5-review.md
        - health-ai commit 8bc980ad21d3f54cbd27b28dcb363e0198c46751
        - acceptance/core/evidence-summary.md
        - acceptance/core/matrix.json

        Core contract to consume:
        - nutrition is a module on g-health-core, not a duplicate core
        - consume core-owned metrics, phase, PLAN-vs-LOG, review, parser/library, value grammar, and safety floor
        - raw daily food/weight data stays in Health AI, not Direction OS
      boundaries: |
        Do not store raw daily food, weight, or check-in logs in Direction OS.
        Do not build product repo implementation during shape.
        Do not build training/activity module.
        Do not build app UI, runtime, DB, server, cron, or scheduler.
        Do not make medical prescriptions.
        Do not rewrite g-health-core; nutrition consumes it.
      done_when: |
        - One shaped g-health-nutrition-system bet draft exists with appetite, kill_by, cut list, lens sweep, and tasks.
        - The first task tests the riskiest nutrition-module assumption on top of g-health-core.
        - TREE/NOW state_changes only enter after explicit owner approval under G9.
      return: |
        RESULT with shaped bet draft, proposed state_changes, decisions_needed, and next CALL/awaiting_decision.
      budget: one focused shape session
      surface: any capable session

  LOG.md:
  - Append:
      - 2026-06-15 — health/g-health-core review approval: owner approved closing g-health-core as done and chose recommendation A; next c-health-nutrition-shape-001. → history/2026-06-15-s-health-core-review-002-approval.md

  history/:
  - Add live/health/history/2026-06-15-s-health-core-review-002-approval.md containing this RESULT.

captures: []

decisions_needed: []

play_check:
  - 1 Verify by refutation: skipped — inherited from c-health-core-review-002, which returned corrected binding G5 verdict met.
  - 2 Harvest per lens: skipped — inherited from c-health-core-review-002.
  - 3 Update the tree: done — owner approved the pending TREE close with "approve"; g-health-core.status set active -> done.
  - 4 Add-back check: skipped — inherited from c-health-core-review-002, add-back 0/8.
  - 5 Knowledge: skipped — inherited from c-health-core-review-002, knowledge already promoted.
  - 6 Select next: done — owner approved recommendation A with "approve"; next is c-health-nutrition-shape-001.
  - 7 Close: done — decision cleared, NOW has no active bet, next shape CALL prepared.

log: >
  2026-06-15 — health/g-health-core review approval: owner approved closing g-health-core
  as done and chose recommendation A; next c-health-nutrition-shape-001.

next: |
  CALL c-health-nutrition-shape-001
  to: session
  direction: health
  play: shape
  node: g-health-nutrition-system
  goal: |
    g-health-nutrition-system is shaped as the first module-on-core bet after g-health-core closure.
  context: |
    Owner approved decision d-health-core-close-and-next-bet with: "approve".
    This closes g-health-core as done and selects recommendation A: shape g-health-nutrition-system next.

    c-health-core-review-002 returned corrected binding G5 verdict met for g-health-core.

    Read:
    - live/health/CHARTER.md
    - live/health/TREE.md
    - live/health/NOW.md
    - live/health/knowledge/health-core-corrected-g5-review.md
    - health-ai commit 8bc980ad21d3f54cbd27b28dcb363e0198c46751
    - acceptance/core/evidence-summary.md
    - acceptance/core/matrix.json

    Core contract to consume:
    - nutrition is a module on g-health-core, not a duplicate core
    - consume core-owned metrics, phase, PLAN-vs-LOG, review, parser/library, value grammar, and safety floor
    - raw daily food/weight data stays in Health AI, not Direction OS
  boundaries: |
    Do not store raw daily food, weight, or check-in logs in Direction OS.
    Do not build product repo implementation during shape.
    Do not build training/activity module.
    Do not build app UI, runtime, DB, server, cron, or scheduler.
    Do not make medical prescriptions.
    Do not rewrite g-health-core; nutrition consumes it.
  done_when: |
    - One shaped g-health-nutrition-system bet draft exists with appetite, kill_by, cut list, lens sweep, and tasks.
    - The first task tests the riskiest nutrition-module assumption on top of g-health-core.
    - TREE/NOW state_changes only enter after explicit owner approval under G9.
  return: |
    RESULT with shaped bet draft, proposed state_changes, decisions_needed, and next CALL/awaiting_decision.
  budget: one focused shape session
  surface: any capable session

END_OF_FILE: live/health/history/2026-06-15-s-health-core-review-002-approval.md
