# NOW — health

active_bet:
  status: none
  note: >
    2026-06-16 nutrition converge closed WHAT: personalized nutrition process on
    g-health-core, mandatory nutrition tracking, no current vitrine/Mealie/UI
    requirement, future integration seam only. Next = converge-arch.

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
  CALL c-health-nutrition-converge-arch-001
  to: session
  direction: health
  play: converge-arch
  node: g-health-nutrition-system
  goal: |
    g-health-nutrition-system has a closed architecture/contract surface for implementing the signed nutrition
    WHAT on g-health-core without duplicating core, without current vitrine/app requirements, and with mandatory
    nutrition tracking/review/base-prep semantics.
  context: |
    Read:
    - live/health/CHARTER.md
    - live/health/TREE.md
    - live/health/NOW.md
    - live/health/work/converge-g-health-nutrition-system.md
    - live/health/work/converge-g-health-core.md
    - health-ai core files/evidence as needed:
      acceptance/core/evidence-summary.md
      acceptance/core/matrix.json
      core/metrics.md
      core/extensions/attach-contract.md
      core/profile/owner-facts.md
      core/profile/derived-anchors.md
      core/intake/non-blocking-questions.md
      core/parser/materiality.md
      core/principles/minimum-tracked-signals.md
      core/phases.md

    Owner-signed nutrition WHAT highlights:
    - nutrition is a module on g-health-core;
    - expert variables are system-decided; owner facts only are askable and non-blocking;
    - first cycle must be personalized, not generic quick menu;
    - nutrition tracking is mandatory and low-friction via text/voice/photo;
    - tracking must feed review and artifact mutation;
    - recipes/instructions must support base-prep/reuse and grocery/prep correctness;
    - no current Mealie/vitrine/UI/app/image-sync requirement;
    - keep only future integration seam.
  boundaries: |
    Do not build implementation.
    Do not create product repo code.
    Do not require Mealie, UI, app integration, recipe image generation, runtime, DB, server, cron, or scheduler.
    Do not build training/activity.
    Do not store raw daily food, weight, photo, or check-in logs in Direction OS.
    Do not make medical prescriptions.
    Do not rewrite g-health-core; nutrition consumes it.
  done_when: |
    - Architecture/contract surface decomposes each signed WHAT mechanism into build-deciding contracts:
      nutrition artifacts, attach namespace, tracking LOG shape, review mutation path, base-prep/reuse semantics,
      grocery/prep derivation, bad-week mode, safety interaction, and future integration seam.
    - Every architecture decision is either answered with citation to signed WHAT/core contract or routed to PLAN.
    - No open/deferred rows remain, or genuine owner decisions are batched with options and recommendation.
    - Next route is converge-verify if closed; otherwise awaiting_decision.
  return: |
    RESULT with architecture artifact path, coverage evidence, state_changes, decisions_needed, and next CALL.
  budget: one focused converge-arch movement
  surface: any capable session

END_OF_FILE: live/health/NOW.md
