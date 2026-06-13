# NOW — health

active_bet:
  status: none
  note: >
    No active bet after review `s-health-ai-core-review-001`; waiting for the owner
    to choose the next health bet.

tasks: []

recurring: []

open_calls: []

decisions:
  - q: >
      Choose the next health bet.
    options:
      - A — Shape `g-health-nutrition-system` next: turn the verified core into the
        first practical nutrition system slice for weekly plan, menu today, food logging,
        recipes, fallback meals, and nutrition review.
      - B — Shape `g-health-training-activity-system` next: turn the verified core into
        the first training/activity system slice for today training, safety state,
        activity options, and training review.
      - C — Pause active betting in health for now: keep the direction idle until owner
        energy/context is available for the next bet.
    recommendation: >
      A, because nutrition is the highest-frequency operational loop and tests the
      Health AI Core against menu, recipe, logging, fallback, and adherence behavior
      without storing raw daily data in Direction OS.

next: |
  awaiting_decision

END_OF_FILE: live/health/NOW.md
