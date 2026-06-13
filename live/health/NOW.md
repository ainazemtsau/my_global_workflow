# NOW — health

active_bet:
  id: g-health-starter-kit
  status: active
  appetite: 7 calendar days
  kill_by: >
    2026-06-19: if corrected starter kit v0 and compressed feedback path are not usable by then,
    stop and review instead of extending the bet.
  goal: >
    Стартовый комплект питания и тренировок выдан и пригоден к немедленному началу:
    owner может начать есть и тренироваться по первому рабочему варианту до завершения
    Health AI System.
  done_when:
    - work/health-starter-kit-v0.md exists.
    - Artifact covers first nutrition starter and first training/activity starter.
    - Artifact includes safety stop/escalation gates.
    - Artifact includes bad-week minimum.
    - Artifact states what not to track in Direction OS.
    - Artifact includes exact compressed feedback prompt for t-2.
    - No daily raw health data is stored in Direction OS.
    - No long-term detailed diet, full progressive training program, Health AI System core, or app integration choice is created.
  reconstructed_by: s-health-repair-starter-kit-state-002
  reconstruction_reason: >
    Previous work/repair RESULT could not apply because NOW.md still had active_bet: null and tasks: [].
    This repair reconstructs the missing shaped state and records the owner-approved A+ / A-food starter.
  cut_list:
    - Do not create a detailed long-term diet.
    - Do not create a full progressive training program.
    - Do not build Health AI System core or data architecture.
    - Do not choose Hevy/Strava-like/wearable/VR integrations.
    - Do not store daily raw weight/food/set/activity data in Direction OS.
    - Do not make medical prescriptions.
    - Do not include squats, single-leg lower-body work, running, jumps, or calf work in v0.
  lens_sweep:
    - weight-nutrition: >
        Covered by A-food: omelet, chicken + rice/pasta + Greek salad, творог + strawberries,
        simple first-week prep and no raw food logs in Direction OS.
    - strength-body-composition: >
        Covered by A+: 3 home strength sessions using dumbbells and bands, with protein anchors
        and no full progressive program.
    - activity-conditioning: >
        Covered by morning VR/Beat Saber and bicycle as easy/moderate low-impact activity.
    - adherence-relapse: >
        Covered by bad-week minimum and exact compressed feedback prompt for t-2.
    - medical-safety: >
        Covered by Achilles-specific exclusions, pain/recovery red flags, urgent stop signs,
        and clinician-baseline gate before intensification.
    - ai-system-data-architecture: >
        Covered by explicit Direction OS exclusions; Health AI System and integrations are deferred.

tasks:
  - id: t-1
    node: g-health-starter-kit
    status: done
    goal: >
      Produce work/health-starter-kit-v0.md: one practical starter artifact with
      initial nutrition starter, initial training/activity starter, safety boundaries,
      bad-week minimum, and compressed feedback path.
    done_when:
      - work/health-starter-kit-v0.md exists.
      - It covers nutrition starter.
      - It covers training/activity starter.
      - It covers safety stop/escalation gates.
      - It covers bad-week minimum.
      - It states what not to track in Direction OS.
      - It includes exact owner feedback prompt for t-2.
    evidence:
      - work/health-starter-kit-v0.md
      - live/health/history/2026-06-13-s-health-repair-starter-kit-state-002.md
    note: >
      Corrected A+ / A-food version supersedes earlier generic/unapplyable drafts.

  - id: t-2
    node: g-health-starter-kit
    status: open
    goal: >
      Guide the owner through compressed feedback on corrected work/health-starter-kit-v0.md
      and turn that feedback into a concise next-step adjustment without storing daily raw health data
      in Direction OS.
    done_when:
      - Owner feedback is compressed into what worked, what failed, safety/Achilles flags,
        nutrition adjustment, training/activity adjustment, and next recommended action.
      - Direction OS receives only summary/problems/decisions/next CALL, not daily raw logs.
    evidence: []

recurring: []

open_calls: []

decisions: []

next: |
  CALL c-health-starter-kit-t-2-guide-001
  to: session
  direction: health
  play: guide
  node: g-health-starter-kit
  task: t-2
  goal: |
    Guide the owner through compressed feedback on corrected work/health-starter-kit-v0.md
    and turn that feedback into a concise next-step adjustment without storing
    daily raw health data in Direction OS.
  context: |
    Read live/health/CHARTER.md, live/health/TREE.md, live/health/NOW.md,
    work/health-starter-kit-v0.md, and
    live/health/history/2026-06-13-s-health-repair-starter-kit-state-002.md.

    Corrected starter kit:
    - training frame A+:
      - 3 strength sessions/week is the normal minimum;
      - strength is at home with dumbbells + long bands + short fabric bands;
      - no bench;
      - morning VR/Beat Saber; pre-lunch strength;
      - bicycle as low-impact cardio;
      - no squats, no single-leg lower body, no running, no jumps, no calf work;
      - prior Achilles irritation is a safety constraint;
      - optional 4th upper/back/arms pump only if safety markers are green.
    - nutrition frame A-food:
      - breakfast: omelet with meat/tuna/beans;
      - main meals: chicken + rice/pasta + Greek salad;
      - dessert/snack: творог + strawberries;
      - tools: multicooker, air fryer, oven, gas stove, pans;
      - no microwave;
      - simple first-week restoration, not interesting cooking yet.

    Owner should paste the exact feedback prompt from section "6. Exact feedback prompt for t-2".
  boundaries: |
    Do not store daily raw weight/food/set/activity data in Direction OS.
    Do not ask for raw logs.
    Do not build Health AI System core or data architecture.
    Do not choose Hevy/Strava-like/wearable/VR integrations.
    Do not make medical prescriptions.
    Do not create a long-term detailed diet or full progressive training program.
    If owner reports safety red flags or Achilles worsening, prioritize safety escalation/regression over optimization.
  done_when: |
    Owner feedback on corrected starter kit v0 is compressed into:
    - what worked;
    - what failed;
    - safety/Achilles flags;
    - nutrition adjustment needed;
    - training/activity adjustment needed;
    - whether to keep A+ / A-food, add 4th upper pump, lighten, add simple recipe variety, or redesign;
    - next recommended action.
    Direction OS receives only summary/problems/decisions/next CALL, not daily raw logs.
  return: |
    RESULT with compressed feedback summary, safety assessment, suggested v1 adjustment
    or escalation, any decisions_needed, NOW task status update, and next CALL.
  budget: one guide session
  surface: chatgpt

END_OF_FILE: live/health/NOW.md
