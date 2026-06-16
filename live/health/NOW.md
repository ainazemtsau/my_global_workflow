# NOW — health

active_bet:
  status: none
  note: >
    2026-06-16 nutrition converge closed WHAT and converge-arch is closed on paper after
    writer-safe repair of B1-B3 correction. Next = converge-verify.

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
    Verify that g-health-nutrition-system architecture/contract surface is actually closed
    after writer-safe repair, before any executor CALL.
  context: |
    Read:
    - live/health/NOW.md
    - live/health/work/converge-g-health-nutrition-system.md
    - live/health/work/converge-g-health-nutrition-system-arch.md
    - live/health/knowledge/health-core-corrected-g5-review.md
    - relevant history RESULTs for:
      - c-health-nutrition-converge-arch-001
      - c-health-nutrition-converge-arch-correction-001
      - c-health-nutrition-converge-arch-writer-repair-001
    - Health AI core evidence as needed:
      acceptance/core/evidence-summary.md
      acceptance/core/matrix.json
      core/extensions/attach-contract.md
      core/procedures/template-contract.md
      core/provenance/day-type.md

    Verify especially:
    - B1: core review binding is file-backed by knowledge/history/product evidence, not CALL-only import.
    - B2: regular nutrition procedure extension points are covered by core procedure template plus
      nutrition operator-invoked procedure seam, without scheduler/runtime/cron/background jobs.
    - B3: core day_type is provenance only; nutrition owns any later namespaced nutrition day_type/target.
  boundaries: |
    Do not implement.
    Do not create product repo code.
    Do not redo nutrition WHAT.
    Do not rewrite g-health-core.
    Do not add UI/app/runtime/DB/server/cron/scheduler requirements.
    Do not proceed to executor CALL unless converge-verify passes.
  done_when: |
    - Try to refute the closed architecture/contract claim against signed WHAT and file-backed core evidence.
    - Confirm no open/deferred/blocker rows remain in the corrected arch surface.
    - Confirm no conflicting old §CONTRACTS/§ARCH/§ROUTE rows remain after §COVERAGE.
    - Confirm B1-B3 are corrected exactly as stated above.
    - Next route is executor/shape only if verification passes; otherwise repair/awaiting_decision.
  return: |
    RESULT with verification verdict, refutation evidence, state_changes, decisions_needed, and next CALL.
  budget: one tight converge-verify movement
  surface: any capable session

END_OF_FILE: live/health/NOW.md
