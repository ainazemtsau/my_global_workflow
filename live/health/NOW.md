# NOW — health

active_bet:
  id: g-health-starter-kit
  status: done
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
    status: done
    goal: >
      Guide the owner through compressed feedback on corrected work/health-starter-kit-v0.md
      and turn that feedback into a concise next-step adjustment without storing daily raw health data
      in Direction OS.
    done_when:
      - Owner feedback is compressed into what worked, what failed, safety/Achilles flags,
        nutrition adjustment, training/activity adjustment, and next recommended action.
      - Direction OS receives only summary/problems/decisions/next CALL, not daily raw logs.
    evidence:
      - owner compressed feedback in session s-health-starter-kit-t-2-guide-003
      - work/health-starter-kit-v0.md rejected as an artifact to iterate
    note: >
      Owner rejected the starter-kit document as a bad artifact and explicitly asked not
      to spend more time polishing it. The useful output is compressed feedback and a
      pivot to Health AI System core/source-of-truth work.

recurring: []

open_calls: []

decisions: []

next: |
  CALL c-health-ai-core-shape-001
  to: session
  direction: health
  play: shape
  node: g-health-ai-core
  goal: |
    Shape the first Health AI System core slice: source-of-truth, operating protocol,
    and minimal state model for planning, food logging, recipes, training/activity
    outputs, and cross-chat continuation.
  context: |
    Read live/health/CHARTER.md, live/health/TREE.md, live/health/NOW.md, and
    the t-2 guide RESULT s-health-starter-kit-t-2-guide-003.

    Owner rejected work/health-starter-kit-v0.md as the wrong artifact shape and asked
    not to spend more time polishing that file.

    Owner's intended system, compressed:
    - system stores data, metrics, preferences, plans, recipes, feedback, and state;
    - owner can open an AI chat from anywhere and ask for today's menu or today's training;
    - if no weekly plan exists, AI should detect that and guide creation of one;
    - food logging should accept text/voice/photo-style input, ask follow-up questions,
      allow skipped questions, save with available data, and give same-day advice;
    - recipes should be durable stored artifacts, probably GitHub-backed as source-of-truth;
    - later research may evaluate a self-hosted open-source recipe manager/API integration,
      but this session must not choose that integration;
    - Direction OS must remain strategic and receive only summary/problems/decisions/CALLs,
      not daily raw logs.

    This CALL is node-level shape work. It intentionally does not refer to a pre-existing
    g-health-ai-core/t-1 task. The shape RESULT should create any valid active_bet/tasks
    with appetite/kill_by if activation is approved.
  boundaries: |
    Do not create a long-term detailed diet or full progressive training program.
    Do not build the implementation.
    Do not choose Hevy/Strava-like/wearable/VR/recipe-manager integrations.
    Do not store daily raw weight/food/set/activity data in Direction OS.
    Do not ask for raw logs.
    Do not make medical prescriptions.
  done_when: |
    A concise shape exists for the first Health AI System core slice:
    - source-of-truth boundaries;
    - minimal state model;
    - operating protocol for new chats;
    - planning/menu/training/logging/review loops;
    - what lives in GitHub/work files vs future app/tool integrations vs Direction OS;
    - whether to activate g-health-ai-core now, with valid appetite/kill_by and tasks if yes;
    - first implementation-ready next CALL if activation is approved.
  return: |
    RESULT with shaped core slice, explicit non-goals, any owner_approved state_changes,
    decisions_needed, and next CALL or awaiting_decision.
  budget: one shape session
  surface: chatgpt

END_OF_FILE: live/health/NOW.md
