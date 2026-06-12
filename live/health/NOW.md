# NOW — health

active_bet: null

tasks: []

recurring: []

open_calls: []

decisions: []

next: |
  CALL c-health-shape-starter-kit-001
  to: session
  direction: health
  play: shape
  node: g-health-starter-kit
  goal: |
    Shape g-health-starter-kit into the first actionable bet that produces a practical starter kit:
    initial nutrition starter plus initial training/activity starter, so the owner can begin immediately
    while Health AI System is built in parallel.
  context: |
    Read live/health/CHARTER.md, live/health/TREE.md, live/health/NOW.md,
    live/health/history/2026-06-12-s-health-map-evidence-001.md,
    and live/health/history/2026-06-12-s-health-map-001.md.

    Approved map summary:
    - g-health-root has 4 top-level children:
      1. g-health-starter-kit
      2. g-health-ai-core
      3. g-health-nutrition-system
      4. g-health-training-activity-system
    - Next work should start with g-health-starter-kit.
    - Owner intent:
      The first output should let him start eating/training now.
      Direction OS should not become a daily health tracker.
      Health AI System will later handle tracking/state/procedures/integrations.
      Starter kit should become a seed for later nutrition and training/activity systems, not a random one-off.

    Relevant owner assets:
    - 35-year-old male, 182 cm, 125 kg, BMI approx 37.7.
    - No stated injuries, diagnoses, medications, or restrictions.
    - Assets: VR, bicycle, 24 kg dumbbells, gym access, cooking equipment, scales.
    - Likes gameful/competitive activity, including Beat Saber and VR boxing/fitness.
    - Interested in Strava-like or self-hosted activity tools later.
    - Has prior sport and diet experience.
  boundaries: |
    Do not create a detailed long-term diet or full training program.
    Do not store daily raw weight/food/set/activity data in Direction OS.
    Do not build Health AI System core in this shape; only shape starter-kit.
    Do not make medical prescriptions.
    Include safety/medical escalation gates at the level needed for a starter kit.
    Respect G6: shape output must include appetite, kill_by, cut list, lens sweep verdict per lens,
    and tasks that test the riskiest assumption.
    Respect G9 if TREE/NOW edits require owner approval.
  done_when: |
    g-health-starter-kit is shaped into a valid bet with appetite, kill_by, cut list, lens sweep,
    and <=3 tasks sized to produce the first practical starter kit artifact:
    nutrition starter + training/activity starter + feedback path.
    No daily tracking data, full Health AI System build, or long-term detailed plan is created.
  return: |
    RESULT with approved shape edits, NOW active_bet/tasks proposal, evidence, play_check,
    and next CALL for work on the starter kit.
  budget: one shape session
  surface: chatgpt

END_OF_FILE: live/health/NOW.md
