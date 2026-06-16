# NOW — health

active_bet:
  status: none
  note: >
    2026-06-16 nutrition converge-verify failed clean pass: independent oracle
    found blocker gaps in core review consumption, regular nutrition procedure
    extension points, and NCA8 day_type producer wording/evidence. Next =
    converge-arch correction.

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
  CALL c-health-nutrition-converge-arch-correction-001
  to: session
  direction: health
  play: converge-arch
  node: g-health-nutrition-system
  goal: |
    g-health-nutrition-system contract/architecture closure is corrected so verifier blockers
    are closed and the node is ready for fresh verification.
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
    - health-ai core/review.md
    - health-ai core/progression/cadence.md
    - health-ai core/procedures/template-contract.md
    - health-ai core/provenance/day-type.md
    - health-ai core/profile/owner-facts.md
    - health-ai core/profile/derived-anchors.md
    - health-ai core/intake/non-blocking-questions.md
    - health-ai core/parser/materiality.md
    - health-ai core/principles/minimum-tracked-signals.md
    - health-ai core/phases.md

    Correct these converge-verify blockers exactly:
    - B1: NCA1/NCA4 do not explicitly bind nutrition review to core-owned review policy/cadence/procedure.
      Core evidence says review is a core-owned reconciliation step; current NCA4 can read as a duplicated
      nutrition review engine.
    - B2: TREE's regular nutrition process extension points are not contract-covered as core procedure-template
      invocations. Current coverage maps them only weakly via W1/W13/NCA1; examples include new dish search,
      fallback refresh, pantry-based recipes, and low-time-week adaptation.
    - B3: NCA8 overstates the current planned day_type producer. Core evidence proves CA5 as a provenance
      contract only; either cite an actual current core planned day_type source or make the nutrition dependency
      explicitly non-blocking/fallback-safe without requiring a core rewrite.
  boundaries: |
    Do not shape the node or create executor CALLs.
    Do not add UI/app/Mealie/runtime/DB/server/cron/scheduler requirements.
    Do not rewrite g-health-core.
    Do not reopen owner-signed nutrition WHAT unless a blocker proves a true WHAT-level gap.
    Do not store raw daily food/weight/photo/check-in logs in Direction OS.
  done_when: |
    B1-B3 are closed in the nutrition contract/architecture artifact or explicitly routed as unresolved.
    No new current app/runtime/UI requirement is introduced.
    No g-health-core rewrite requirement is introduced.
    Open/deferred high-risk architecture rows are zero, or exact remaining blockers are returned.
    Next route is a fresh converge-verify CALL.
  return: |
    RESULT with corrected contract/architecture rows, evidence against B1-B3, state_changes, play_check,
    and next CALL.
  budget: one focused correction movement
  surface: any capable session

END_OF_FILE: live/health/NOW.md
