# NOW — health

active_bet:
  status: none
  note: >
    2026-06-16 nutrition converge-arch closed contract/architecture-on-paper surface:
    NCA0-NCA9 cover starter seed, core attach, tracking LOG, review mutation,
    base-prep/grocery, bad-week/safety, future seam, training day_type via core,
    and Direction OS raw-data boundary. Next = converge-verify.

tasks: []

recurring: []

open_calls: []

decisions:
  - id: d-health-nutrition-define-signoff-001
    status: resolved
    owner_choice: A
    owner_words: "A — да, подписываем"
  - id: d-health-nutrition-what-signoff-001
    status: resolved
    owner_choice: A
    owner_words: "A"

next: |
  CALL c-health-nutrition-converge-verify-001
  to: session
  direction: health
  play: converge-verify
  node: g-health-nutrition-system
  goal: |
    g-health-nutrition-system contract/architecture closure is independently refuted and either
    passed clean for shape or bounced with exact blockers.
  context: |
    Read:
    - live/health/CHARTER.md
    - live/health/TREE.md
    - live/health/NOW.md
    - live/health/work/converge-g-health-nutrition-system.md
    - live/health/work/converge-g-health-nutrition-system-arch.md
    - live/health/work/converge-g-health-core.md
    - live/health/knowledge/health-core-corrected-g5-review.md
    - health-ai acceptance/core/evidence-summary.md
    - health-ai acceptance/core/matrix.json
    - health-ai core/extensions/attach-contract.md
    - health-ai core/metrics.md
    - health-ai core/profile/owner-facts.md
    - health-ai core/profile/derived-anchors.md
    - health-ai core/intake/non-blocking-questions.md
    - health-ai core/parser/materiality.md
    - health-ai core/principles/minimum-tracked-signals.md
    - health-ai core/phases.md

    Verify specifically:
    - §CONTRACTS NCA0-NCA9 cover every TREE/core/starter/training/Direction OS/future seam interaction.
    - There is no dangling current producer; future training logged day_type is correctly non-blocking.
    - Nutrition consumes core; it does not duplicate core profile, phase, metrics, parser/library/procedure, review, schema/versioning, or Direction OS boundary.
    - Mandatory tracking, tracking-to-review mutation, base-prep/reuse, grocery/prep derivation, bad-week mode, safety, and future integration seam are covered.
    - Architecture questions Q1-Q9 are closed with refuted alternatives and no open/deferred high-risk rows.
    - No HOW leakage appears in §CONTRACTS; HOW is routed to PLAN.
    - Architecture-on-paper is context-only and does not leak into executor done_when.
  boundaries: |
    Do not shape the node.
    Do not create executor CALL.
    Do not build implementation.
    Do not add UI/app/Mealie/runtime/DB/server/cron/scheduler requirements.
    Do not rewrite g-health-core.
    Do not store raw daily food/weight/photo/check-in logs in Direction OS.
    If blockers are found, return exact blockers; do not patch them silently unless they are purely mechanical wording fixes inside the verify result.
  done_when: |
    Independent verdict is pass/fail with evidence.
    Pass only if contract coverage is complete, no current producer dangles, no line cites an open WHAT/term,
    no HOW leaks into contract rows, mandatory nutrition tracking/review/base-prep semantics are covered,
    and architecture-on-paper remains input evidence only.
    If pass, next route is shape. If fail, next route is repair/converge-arch correction with exact blockers.
  return: |
    RESULT with verdict, evidence table, blocker list if any, state_changes, play_check, and next CALL.
  budget: one focused verify movement
  surface: any capable session

END_OF_FILE: live/health/NOW.md
