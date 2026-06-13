# NOW — health

active_bet:
  status: none
  note: >
    No active bet after review `s-health-ai-core-review-001`; waiting for the owner
    to choose the next health bet.

tasks: []

recurring: []

open_calls: []

decisions: []

next: |
  CALL c-health-nutrition-system-shape-001
  to: session
  direction: health
  play: shape
  node: g-health-nutrition-system
  goal: |
    The first practical nutrition-system bet is shaped and ready for owner activation.
  context: |
    Read live/health/CHARTER.md, live/health/TREE.md, live/health/NOW.md,
    live/health/knowledge/health-ai-core-guidance-governance.md,
    work/health-ai-core-contract-v0.md,
    work/health-ai-core-state-skeleton-v0.md,
    work/health-ai-core-validation-summary-v0.md,
    live/health/history/2026-06-13-s-health-ai-core-review-001.md,
    live/health/history/2026-06-13-s-health-ai-core-review-001-approval.md,
    and live/health/history/2026-06-13-s-health-starter-kit-t-2-guide-003.md.

    Owner selected option A after review: shape `g-health-nutrition-system` next.
    The verified Health AI Core can support weekly planning, menu today, food logs
    with skipped follow-ups, recipes, fallback meals, reviews/incidents, pending
    patches, and Direction OS escalation without storing raw daily data in Direction OS.
  boundaries: |
    Do not build an app or implementation.
    Do not choose recipe-manager, grocery, wearable, Hevy, Strava-like, VR, or other integrations.
    Do not create a long-term detailed diet.
    Do not request raw daily food logs.
    Do not store daily raw food, weight, training, activity, photo, or check-in data in Direction OS.
    Do not make medical prescriptions.
    Do not polish or revive work/health-starter-kit-v0.md.
  done_when: |
    Shape RESULT for `g-health-nutrition-system` is ready and includes an owner activation
    decision for a small first nutrition-system bet, or `awaiting_decision` if activation
    is not approved.
  return: |
    RESULT with shaped nutrition slice, cut list, lens sweep, appetite/kill_by/tasks if
    activation is approved, decisions_needed, and next CALL or awaiting_decision.
  budget: one shape session
  surface: chatgpt

END_OF_FILE: live/health/NOW.md
