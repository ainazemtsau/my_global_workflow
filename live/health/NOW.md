# NOW — health

active_bet:
  id: g-health-ai-core
  status: active
  appetite: 6 calendar days
  kill_by: >
    2026-06-19: if there is no usable Health AI Core Contract, no minimal source-of-truth skeleton,
    or the five required dry-runs cannot be completed without raw Direction OS logs,
    kill/review instead of extending.
  goal: >
    Ядро Health AI System создано как расширяемый продукт внутри направления health:
    оно умеет хранить health-состояние, принимать апдейты, поддерживать AI-роли/процедуры
    и служить основой для будущих nutrition/training/activity модулей.
  done_when:
    - There is a Health AI Core Contract artifact covering source-of-truth boundaries,
      minimal state model, AI operating protocol, loops, and non-goals.
    - There is a minimal source-of-truth skeleton for profile, preferences, metrics summaries,
      active plans, food logs, recipes, training/activity state, feedback, reviews/incidents,
      and pending patches.
    - The five core flows are dry-run without storing raw daily health data in Direction OS.
    - The core stays integration-neutral and does not choose Hevy/Strava-like/wearable/VR/recipe-manager tools.
    - Direction OS receives only summary/problems/decisions/CALLs.
  cut_list:
    - Cut dedicated app UI.
    - Cut API/database implementation.
    - Cut recipe-manager selection.
    - Cut Hevy/Strava/wearable/VR integration decisions.
    - Cut full macro/calorie algorithm.
    - Cut full long-term training progression.
    - Cut raw logs in Direction OS.
    - Cut photo-understanding pipeline; accept photo-style owner descriptions for now.
    - Cut automatic cross-tool sync.
    - Cut broad health dashboard.
  lens_sweep:
    - weight-nutrition: >
        Needs work; covered by state model for preferences, plans, recipes, food logs,
        same-day advice, and planning/menu loop.
    - strength-body-composition: >
        Needs work; covered by training_activity state, current plan/today output protocol,
        safety gates, and no full progressive program.
    - activity-conditioning: >
        Needs work; covered by activity options, current-week outputs, summaries,
        and future integration pointers without choosing tools now.
    - adherence-relapse: >
        Needs work; covered by low-friction logging, skippable questions, fallback plans,
        weekly review, and escalation when the system becomes too heavy.
    - medical-safety: >
        Needs work; covered by safety flags, pain/fatigue checks, non-prescriptive boundaries,
        and escalation/stop logic for concerning signals.
    - ai-system-data-architecture: >
        Primary lens; covered by source-of-truth boundaries, minimal state model,
        chat protocol, writer/update boundary, and Direction OS bridge.
  assumptions:
    - GitHub-backed minimal state/protocol layer can support useful cross-chat continuation before app/integration work.
    - Owner will tolerate a small amount of structured health state if it produces useful daily outputs.
    - AI chats can follow the operating protocol without turning Direction OS into a diary.
    - Recipes/plans/logs can start as durable artifacts and later migrate/sync without rework.
    - Dry-run scenarios can reveal the biggest schema/protocol flaws before implementation.
  forecast: >
    The first slice can be made useful without building an app or choosing integrations.
  against: >
    The core may still feel like another document unless dry-runs prove it answers real menu/training/logging flows.

tasks:
  - id: t-1
    node: g-health-ai-core
    status: done
    kind: session
    goal: >
      Produce work/health-ai-core-contract-v0.md: the minimal Health AI Core Contract with
      source-of-truth boundaries, state model, new-chat operating protocol, loops, non-goals,
      and five dry-run scenarios.
    done_when:
      - Artifact defines Direction OS vs Health AI System vs future integrations boundaries.
      - Artifact defines minimal state model.
      - Artifact defines operating protocol for new chats.
      - Artifact covers planning/menu/training/food-log/recipe/review loops.
      - Artifact includes five dry-run scenarios.
      - Artifact does not choose integrations, build implementation, request raw logs,
        or store raw daily data in Direction OS.
    evidence:
      - work/health-ai-core-contract-v0.md
      - session s-health-ai-core-t-1-work-001 self-check matched every t-1 done_when item

  - id: t-2
    node: g-health-ai-core
    status: done
    kind: session
    goal: >
      Produce work/health-ai-core-state-skeleton-v0.md: a minimal source-of-truth skeleton
      for profile, preferences, metrics summaries, active plans, food logs, recipes,
      training/activity state, feedback, reviews/incidents, and pending patches.
    done_when:
      - Skeleton lists concrete files/records and required fields.
      - Skeleton states which records may contain operational raw data inside Health AI System.
      - Skeleton states that Direction OS receives only strategic summary/problem/decision/CALL output.
      - Skeleton includes recipe-card, food-log-entry, weekly-plan, training-output, and review/incident templates.
      - Skeleton remains integration-neutral.
    evidence:
      - work/health-ai-core-state-skeleton-v0.md
      - session s-health-ai-core-t-2-work-001 incorporated owner-accepted guidance/governance contour

  - id: t-3
    node: g-health-ai-core
    status: done
    kind: guide
    goal: >
      Validate the contract and skeleton by running the five core flows with synthetic or minimal seed data,
      producing only a compact validation summary for Direction OS.
    done_when:
      - Flow 1 tested: no weekly plan exists → system guides plan creation.
      - Flow 2 tested: today's menu requested → system answers from plan/preferences or marks missing plan.
      - Flow 3 tested: food log with skipped follow-ups → system saves available data with confidence and gives same-day advice.
      - Flow 4 tested: today's training requested → system answers from current plan/safety state or marks missing plan.
      - Flow 5 tested: review/incident → system compresses summary and Direction OS escalation.
      - Validation identifies blockers or confirms the slice is usable enough for next nutrition/training-system shaping.
    evidence:
      - work/health-ai-core-validation-summary-v0.md
      - session s-health-ai-core-t-3-guide-001 dry-ran five flows plus guidance/governance with synthetic/minimal seeds; no raw daily data entered Direction OS

recurring: []

open_calls: []

decisions: []

next: |
  CALL c-health-ai-core-review-001
  to: session
  direction: health
  play: review
  node: g-health-ai-core
  goal: |
    The g-health-ai-core bet has a verified review verdict, harvested learnings,
    and a ready owner decision for the next health bet.
  context: |
    Read live/health/CHARTER.md, live/health/TREE.md, live/health/NOW.md,
    work/health-ai-core-contract-v0.md,
    work/health-ai-core-state-skeleton-v0.md,
    work/health-ai-core-validation-summary-v0.md,
    live/health/history/2026-06-13-s-health-ai-core-t-1-work-001.md,
    live/health/history/2026-06-13-s-health-ai-core-t-2-work-001.md,
    live/health/history/2026-06-13-s-health-ai-core-t-3-guide-001.md,
    live/health/history/2026-06-13-s-health-starter-kit-t-2-guide-003.md,
    and live/health/history/2026-06-13-s-health-ai-core-shape-001-approval.md.

    The active bet's tasks are complete:
    - t-1 produced the Health AI Core Contract v0.
    - t-2 produced the State Skeleton v0 with the owner-accepted guidance/governance contour.
    - t-3 produced the compact validation summary and found the slice usable enough
      for review and next nutrition/training-system shaping.

    Known non-blocking gap from t-3:
    - the contract implies guidance through protocol/loops, while the skeleton makes
      guidance/governance first-class. A later contract revision can promote this
      if the core continues.
  boundaries: |
    Do not build an app or implementation.
    Do not choose Hevy/Strava-like/wearable/VR/recipe-manager integrations.
    Do not create a long-term detailed diet or full progressive training program.
    Do not store daily raw health data in Direction OS.
    Do not ask for raw logs.
    Do not make medical prescriptions.
    Do not polish or revive work/health-starter-kit-v0.md.
  done_when: |
    Review RESULT gives a verdict for g-health-ai-core, preserves the no-raw-daily-data
    boundary, records any approved TREE/knowledge/NOW updates, and leaves a next-bet
    owner decision or awaiting_decision state.
  return: |
    RESULT with verdict, evidence, harvested learnings, approved state_changes only,
    decisions_needed for the next bet, and a ready next CALL or awaiting_decision.
  budget: one review session
  surface: chatgpt

END_OF_FILE: live/health/NOW.md
