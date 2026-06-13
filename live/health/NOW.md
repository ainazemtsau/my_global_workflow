# NOW — health

active_bet:
  id: g-health-nutrition-system
  status: active
  appetite: 1 week (set 2026-06-13 by repair s-health-nutrition-repair-001)
  kill_by: >
    2026-06-20: if the chat-first weekly-plan experience is not usable to the owner after a real
    live run, or write-back cannot persist logs/recipes to GitHub without the owner editing files,
    reshape instead of building more.
  goal: >
    Nutrition system is live and usable by the owner through chat, from the single GitHub
    source of truth (product repo health-ai) — not as a document.
  shipped: >
    v1 co-created with the owner and pushed to product repo health-ai
    (github.com/ainazemtsau/health-ai, commit 6c1f651): SYSTEM brain, evidence-base v1,
    five processes, owner state, templates. Built this session from owner co-creation plus a
    verified deep-research pass (workflow w8l06dhq0). Design chosen with owner: "leader with
    brakes" operating mode; an updatable evidence base rather than research-from-scratch each time.
  done_when:
    - Owner has connected a ChatGPT or Claude project to the system and run at least one live
      weekly-plan request he accepts (or rejects with a concrete reason).
    - A write-back path exists so food logs and recipes persist to the GitHub source of truth
      without the owner editing files by hand.
    - Evidence-base round-2 fills the four flagged gaps (tracking precision, maintenance-vs-regain
      predictors, calorie floors / red-flag list, recalc & diet-break cadence) or defers each explicitly.
  forecast: >
    The chat-first system can be made genuinely usable within a week because the content is already
    owner-validated and grounded; the main open risk is write-back without owner file-editing.
  against: >
    It may still feel heavy if the live weekly-plan flow asks too much or write-back forces manual
    steps — that is exactly what t-1 tests first.

tasks:
  - id: t-1
    node: g-health-nutrition-system
    kind: guide
    status: open
    goal: >
      Owner runs the system live for one weekly plan and judges whether the chat-first experience
      is the convenience he wanted; missing preferences are captured into the product repo.
    done_when:
      - Owner connected a ChatGPT or Claude project to repo health-ai (or loaded its files).
      - Owner made at least one real "plan my week" request and got a plan with the "why".
      - Owner's verdict (usable / not, and why) is recorded.
      - Missing preferences (disliked foods, allergies, real cooking time, budget, meals/day)
        are captured into state/preferences.md of the product repo.
      - No raw daily food/weight/training data is stored in Direction OS.

  - id: t-2
    node: g-health-nutrition-system
    kind: executor
    status: open
    repo: health-ai
    goal: >
      Food logs and recipes saved through a chat persist to the GitHub source of truth without
      the owner editing files.
    done_when:
      - Owner can log a meal or save a recipe in a chat and it lands in repo health-ai.
      - Verified by a real commit produced from a chat action, with the owner touching no files.
      - Mechanism stays simple and is documented in the repo (writer chat / HomeLab service / app).

  - id: t-3
    node: g-health-nutrition-system
    kind: session
    status: open
    goal: >
      The four flagged evidence-base gaps are answered with current cited evidence or explicitly
      deferred, and evidence-base.md is updated.
    done_when:
      - Round-2 research covers tracking precision, maintenance-vs-regain predictors, calorie floors /
        red-flag list, and recalc / diet-break cadence.
      - evidence-base.md gets a round-2 section with sources and confidence tags, or a clear
        "still open" note per gap.

recurring: []

open_calls: []

decisions: []

next: |
  CALL c-health-nutrition-live-week-001
  to: session
  direction: health
  play: guide
  node: g-health-nutrition-system
  task: t-1
  goal: |
    Owner has run the health-ai system live for one weekly plan and judged whether the
    chat-first experience is usable, with missing preferences captured into the product repo.
  context: |
    Product repo: github.com/ainazemtsau/health-ai (private). Brain = SYSTEM.md; defaults =
    evidence-base.md; flows = processes.md; owner state = state/. v1 was co-created with the
    owner this session and verified by deep-research workflow w8l06dhq0.
    Owner interacts ONLY through chat and never edits files.
  boundaries: |
    Do not store raw daily food/weight/training data in Direction OS.
    Do not rebuild the system; this is a live usability run plus preference capture.
    Safety and training-intensity changes need the owner's explicit ok (leader with brakes).
    Do not make medical prescriptions.
  done_when: |
    Owner completed at least one live weekly-plan run and gave a usable/not verdict, and missing
    preferences are captured into the product repo's state/preferences.md.
  return: |
    RESULT with the owner's verdict, captured preferences, any problems, and next CALL
    (write-back t-2 and/or round-2 research t-3), or awaiting_decision.
  budget: one guide session
  surface: chatgpt-or-claude-project

END_OF_FILE: live/health/NOW.md
