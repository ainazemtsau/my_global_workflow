# NOW — health

active_bet:
  status: none
  note: >
    2026-06-16 nutrition WHAT is signed; converge-arch was writer-safe repaired; fresh converge-verify passed.
    Architecture/contract surface is closed for shape. No executor CALL has been emitted yet.

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
  CALL c-health-nutrition-shape-001
  to: session
  direction: health
  play: shape
  node: g-health-nutrition-system
  goal: |
    Shape g-health-nutrition-system into an implementation bet on top of g-health-core,
    using the verified signed WHAT + corrected architecture/contract surface.
  context: |
    Read:
    - live/health/CHARTER.md
    - live/health/TREE.md
    - live/health/NOW.md
    - live/health/work/converge-g-health-nutrition-system.md
    - live/health/work/converge-g-health-nutrition-system-arch.md
    - live/health/knowledge/health-core-corrected-g5-review.md
    - health-ai acceptance/core/evidence-summary.md
    - health-ai acceptance/core/matrix.json
    - health-ai core/extensions/attach-contract.md
    - health-ai core/procedures/template-contract.md
    - health-ai core/provenance/day-type.md
    - health-ai core/review.md

    Verified surface to preserve:
    - Copy signed WHAT acceptance W1-W13 into the shape acceptance/evaluator surface:
      W1 source-of-truth; W2 core attach; W3 expert-variable boundary; W4 personalized first process;
      W5 practical outputs; W6 detailed recipes/instructions; W7 base-prep/reuse correctness;
      W8 nutrition tracking; W9 tracking-to-review mutation; W10 bad-week mode; W11 safety boundary;
      W12 no current vitrine/app requirement; W13 future integration seam.
    - Copy corrected §CONTRACTS NCA0-NCA9 into implementation constraints:
      NCA0 starter-kit seed intake; NCA1 core attach/nutrition namespace; NCA2 personalized cycle derivation;
      NCA3 nutrition LOG/low-friction tracking; NCA4 LOG-to-review mutation; NCA5 recipes/base-prep/grocery correctness;
      NCA6 bad-week and safety; NCA7 future integration seam; NCA8 operator-invoked regular nutrition procedures;
      NCA9 day_type provenance/cross-module coupling/Direction OS visibility.
    - Preserve corrected blockers:
      B1 core binding is file-backed by knowledge/history/product evidence, not CALL-only import.
      B2 procedures are nutrition-namespaced declarative operator-invoked seams; no scheduler/runtime/cron/background jobs.
      B3 core day_type is provenance only; nutrition owns any later x_nutrition_day_type/x_nutrition_target.

    PLAN-agenda to shape, not pre-decide here:
    - nutrition folder/domain layout and registry line
    - exact schema keys, enum tokens, source/confidence tokens
    - starter-kit seed promotion mechanics
    - owner-fact seed/intake surface
    - system-decided nutrition variables and evidence/magnitude policy
    - menu-cycle resolver, cycle length, and re-solve rules
    - LOG schema, photo/voice/text parse handling, portion estimation
    - recipe/instruction format, base-prep/reuse model, grocery/prep quantity math
    - review procedure specs, review checklist, mutation patch shape
    - bad-week entry/exit mechanics, fallback minimums, safety thresholds
    - optional future mirror/export/app seam only as non-current work
  boundaries: |
    Do not implement product repo code.
    Do not emit executor CALL until shape has an approved bet/task surface.
    Do not reopen signed nutrition WHAT unless shape finds a true contradiction.
    Do not rewrite g-health-core.
    Do not add UI/app/Mealie/Notion/runtime/server/DB/cron/scheduler/background-worker requirements.
    Do not store raw daily nutrition logs in Direction OS.
  done_when: |
    A shaped bet exists for g-health-nutrition-system with appetite, kill_by, cut list, lens sweep,
    and tasks sized at half-day or less.
    The first task tests the riskiest implementation assumption.
    Shape copies verified WHAT acceptance rows and corrected NCA0-NCA9 contract requirements into executor done_when/evidence expectations.
    PLAN details are explicit enough for executor CALLs, without adding forbidden runtime/app/core-rewrite requirements.
  return: |
    RESULT with shaped bet, task list, cut list, lens sweep, owner approvals if required by G9,
    state_changes, and next CALL.
  budget: one focused shape movement
  surface: any capable session

END_OF_FILE: live/health/NOW.md
