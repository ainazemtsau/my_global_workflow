RESULT s-health-ai-core-shape-001-approval (call: c-health-ai-core-shape-001)
direction: health   play: shape   node/task: g-health-ai-core

outcome: |
  Owner approved activation option A for the shaped g-health-ai-core bet.

  Approved bet:
  - node: g-health-ai-core
  - status: active
  - appetite: 6 calendar days
  - kill_by: 2026-06-19
  - tasks: t-1, t-2, t-3
  - next: c-health-ai-core-t-1-work-001

evidence: |
  Owner approval in-session:
  - "A"

  This approves the option from decisions_needed in RESULT s-health-ai-core-shape-001:
  "A — Approve activation as shaped: 6 calendar days, 3 tasks, kill_by 2026-06-19,
  next CALL c-health-ai-core-t-1-work-001."

state_changes: |
  TREE.md:
  - owner_approved: true
  - approval_evidence: >
      Owner selected option A after the shape RESULT:
      "A"
  - For node g-health-ai-core:
      status: active
      appetite: 6 calendar days
      kill_by: >
        2026-06-19: if there is no usable Health AI Core Contract, no minimal source-of-truth skeleton,
        or the five required dry-runs cannot be completed without raw Direction OS logs,
        kill/review instead of extending.

  NOW.md:
  - Replace active_bet with:
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

  - Replace tasks with:
      - id: t-1
        node: g-health-ai-core
        status: open
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

      - id: t-2
        node: g-health-ai-core
        status: open
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

      - id: t-3
        node: g-health-ai-core
        status: open
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

  - Set recurring: []
  - Set open_calls: []
  - Set decisions: []
  - Set next to:
      CALL c-health-ai-core-t-1-work-001
      to: session
      direction: health
      play: work
      node: g-health-ai-core
      task: t-1
      goal: |
        Produce work/health-ai-core-contract-v0.md: the minimal Health AI Core Contract with
        source-of-truth boundaries, state model, new-chat operating protocol, planning/menu/training/
        food-log/recipe/review loops, explicit non-goals, and five dry-run scenarios.
      context: |
        Read live/health/CHARTER.md, live/health/TREE.md, live/health/NOW.md,
        live/health/history/2026-06-13-s-health-starter-kit-t-2-guide-003.md,
        and RESULT s-health-ai-core-shape-001 plus approval RESULT s-health-ai-core-shape-001-approval.

        Owner rejected work/health-starter-kit-v0.md as the wrong artifact shape and asked not
        to spend more time polishing it.

        The Health AI core must support:
        - AI chats from anywhere asking for today's menu or today's training;
        - detecting missing weekly plan and guiding creation;
        - food logging from text/voice/photo-style input with limited skippable follow-ups;
        - saving available data with confidence and giving same-day advice;
        - durable recipe artifacts, likely GitHub-backed initially;
        - Direction OS receiving only summary/problems/decisions/CALLs, not daily raw logs.
      boundaries: |
        Do not build an app.
        Do not choose Hevy/Strava-like/wearable/VR/recipe-manager integrations.
        Do not create a long-term detailed diet or full progressive training program.
        Do not store daily raw health data in Direction OS.
        Do not ask for raw logs.
        Do not make medical prescriptions.
        Do not polish or revive work/health-starter-kit-v0.md.
      done_when: |
        work/health-ai-core-contract-v0.md content is ready for writer application and contains:
        - source-of-truth boundaries;
        - minimal state model;
        - new-chat operating protocol;
        - planning/menu/training/food-log/recipe/review loops;
        - explicit non-goals and cut list;
        - five dry-run scenarios that test cross-chat continuation and missing-state behavior.
      return: |
        RESULT with artifact content or exact work/ file addition, evidence mapped to done_when,
        no raw daily logs, and next CALL for t-2.
      budget: one work session
      surface: chatgpt

  LOG.md:
  - Append:
      2026-06-13 — health/g-health-ai-core shape approval: owner approved option A;
      g-health-ai-core activated with 6-day appetite, kill_by 2026-06-19, tasks t-1..t-3;
      next c-health-ai-core-t-1-work-001.

captures: []

decisions_needed: []

play_check:
  - "9 Close: done. Owner approved option A: \"A\". Activation state_changes are now owner_approved."

log: "shape approval: owner approved option A; g-health-ai-core activation ready for writer; next t-1 work CALL ready."

next: |
  CALL c-health-ai-core-t-1-work-001
  to: session
  direction: health
  play: work
  node: g-health-ai-core
  task: t-1
  goal: |
    Produce work/health-ai-core-contract-v0.md: the minimal Health AI Core Contract with
    source-of-truth boundaries, state model, new-chat operating protocol, planning/menu/training/
    food-log/recipe/review loops, explicit non-goals, and five dry-run scenarios.
  context: |
    Read live/health/CHARTER.md, live/health/TREE.md, live/health/NOW.md,
    live/health/history/2026-06-13-s-health-starter-kit-t-2-guide-003.md,
    and RESULT s-health-ai-core-shape-001 plus approval RESULT s-health-ai-core-shape-001-approval.

    Owner rejected work/health-starter-kit-v0.md as the wrong artifact shape and asked not
    to spend more time polishing it.

    The Health AI core must support:
    - AI chats from anywhere asking for today's menu or today's training;
    - detecting missing weekly plan and guiding creation;
    - food logging from text/voice/photo-style input with limited skippable follow-ups;
    - saving available data with confidence and giving same-day advice;
    - durable recipe artifacts, likely GitHub-backed initially;
    - Direction OS receiving only summary/problems/decisions/CALLs, not daily raw logs.
  boundaries: |
    Do not build an app.
    Do not choose Hevy/Strava-like/wearable/VR/recipe-manager integrations.
    Do not create a long-term detailed diet or full progressive training program.
    Do not store daily raw health data in Direction OS.
    Do not ask for raw logs.
    Do not make medical prescriptions.
    Do not polish or revive work/health-starter-kit-v0.md.
  done_when: |
    work/health-ai-core-contract-v0.md content is ready for writer application and contains:
    - source-of-truth boundaries;
    - minimal state model;
    - new-chat operating protocol;
    - planning/menu/training/food-log/recipe/review loops;
    - explicit non-goals and cut list;
    - five dry-run scenarios that test cross-chat continuation and missing-state behavior.
  return: |
    RESULT with artifact content or exact work/ file addition, evidence mapped to done_when,
    no raw daily logs, and next CALL for t-2.
  budget: one work session
  surface: chatgpt
