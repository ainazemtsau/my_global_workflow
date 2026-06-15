RESULT s-health-core-cross-family-repair-001 (call: owner-message-2026-06-15)
direction: health   play: repair   node/task: g-health-core/repair
outcome: |
  The hard cross-family G5 requirement for g-health-core has been removed.
  The active bet remains active, but the next continuation is now a corrected fresh
  review/refutation session, not a Claude/non-OpenAI-only gate.
evidence: |
  Owner approval: "A, снимаем hard cross-family requirement".
  Current state before repair had cross-family as a hard blocker in:
  - live/health/NOW.md active_bet.evaluator
  - live/health/NOW.md open_calls and next CALL c-health-core-cross-family-g5-002
  - live/health/knowledge/health-core-g5-evidence-rule.md
  - AGENTS.md and .agents/skills/parallel-verify/SKILL.md Codex guidance

  Reconstructed source:
  - c-health-core-review-001 had clean product pre-pass evidence but marked partially_met
    only because it treated cross-family verification as required.
  - Owner explicitly rejected that as unnecessary complexity.
state_changes: |
  live/health/NOW.md:
  - Keep active_bet g-health-core active.
  - Replace evaluator with corrected rule:
      After t-3, review/refutation must try to break the done claim in a fresh session
      separate from the executor. Cross-family review may be used as extra rigor when
      explicitly requested, but it is not a hard G5 gate for this bet.
  - Change review_status from partially_met_pending_cross_family_g5 to
    partially_met_pending_corrected_g5_review.
  - Change binding_g5_status from missing_cross_family to pending_corrected_review.
  - Replace open_call c-health-core-cross-family-g5-002 with c-health-core-review-002.
  - Rename decision d-health-next-bet-after-core-g5 to d-health-next-bet-after-core-review
    and set activation_condition to corrected G5 review, not cross-family G5.
  - Replace NOW.next with CALL c-health-core-review-002.

  live/health/LOG.md:
  - Append:
      2026-06-15 — health/g-health-core repair: owner removed the hard cross-family G5
      requirement ("A, снимаем hard cross-family requirement"); NOW rerouted from
      c-health-core-cross-family-g5-002 to c-health-core-review-002, g-health-core remains
      active pending corrected fresh review. → history/2026-06-15-s-health-core-cross-family-repair-001.md

  live/health/knowledge/health-core-g5-evidence-rule.md:
  - Delete the knowledge entry because it promoted the rejected hard requirement.

  os/FRICTION.md:
  - Append the 2026-06-15 health/Codex guidance friction line for the hard cross-family gate.

  AGENTS.md:
  - Replace the rule requiring Claude/different-model-family G5 with:
      fresh separate G5 review is required; cross-family is optional unless explicitly requested.

  .agents/skills/parallel-verify/SKILL.md:
  - Replace authoritative cross-family gate wording with:
      in-session validators are pre-pass only; binding G5 is a fresh separate session;
      cross-family is optional unless requested.

  live/health/history/2026-06-15-s-health-core-cross-family-repair-001.md:
  - Store this full RESULT.
captures: []
decisions_needed: []
play_check:
  - "1 Name the contradiction: done — NOW/knowledge/guidance required cross-family G5, owner said: \"A, снимаем hard cross-family requirement\"."
  - "2 Reconstruct: done — newest checkpoint c-health-core-review-001 made product evidence clean but blocked only on cross-family routing."
  - "3 Propose corrected state: done — keep bet active, reroute to corrected review, remove hard cross-family status/knowledge."
  - "4 Confirm: done — owner approved option A: \"A, снимаем hard cross-family requirement\"."
  - "5 Friction: done — logged cross-family hard gate as a rule/guidance defect fixed in this commit."
log: >
  repair: owner removed hard cross-family G5 requirement; NOW rerouted to corrected review
  c-health-core-review-002; g-health-core remains active pending fresh review.
next: |
  CALL c-health-core-review-002
  to: session
  direction: health
  play: review
  node: g-health-core
  goal: |
    g-health-core has a corrected binding G5 review verdict: met, partially met, or not met.
  context: |
    Previous review checkpoint: c-health-core-review-001 returned partially_met because product
    evidence is clean but it treated cross-family verification as a hard requirement.
    Owner removed that hard requirement on 2026-06-15: "A, снимаем hard cross-family requirement".

    Corrected evaluator:
    - G5 requires a fresh review/refutation session separate from executor t-3.
    - A different model family may be used as extra rigor when explicitly requested.
    - A different model family is not required to close this bet.

    Direction OS state:
    - live/health/CHARTER.md
    - live/health/TREE.md
    - live/health/NOW.md
    - live/health/work/converge-g-health-core.md

    health-ai product evidence:
    - t-1 commit a67a34e109aac5f70284b048af4480be38fb8cd5
      "core acceptance harness: map converged spec"
    - t-2 commit ee25a894e22d83485525f7d798f02e0fa9d48189
      "core slice: replace v1 structure"
    - t-3 commit 8bc980ad21d3f54cbd27b28dcb363e0198c46751
      "core evidence: package t-3 dry-run proof"
  boundaries: |
    Do not store raw daily health data in Direction OS.
    Do not build or change product repo implementation during review.
    Do not build nutrition/training/activity modules, app UI, runtime, DB, server, cron, or scheduler.
    Do not make medical prescriptions.
    Do not require a non-OpenAI model family as a hard gate.
    Do not close the bet merely because the cross-family requirement was removed; still run refutation
    against the evidence and done_when.
  done_when: |
    - Fresh review/refutation explicitly handles WA1-WA12 + W69/W70/W72/W73/W74 + CA1-CA9.
    - It explicitly handles check output, gap classification, product scope cuts, owner clearance, and Direction OS boundary.
    - It returns a corrected binding G5 review verdict: met, partially met, or not met.
  return: |
    RESULT with corrected binding G5 verdict, refutation evidence, state_changes, decisions_needed, and next CALL/awaiting_decision.
  budget: one focused review session
  surface: any capable fresh review session; cross-family optional, not required

END_OF_FILE: live/health/history/2026-06-15-s-health-core-cross-family-repair-001.md
