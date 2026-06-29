# NOW — health

active_bet:
  status: none
  note: |
    No active bet after the training/activity v0 product/process work and its 2026-06-28 repair.
    Product/process evidence before repair: health-ai c1bf61e for t-1 and health-ai 8aa14f8 for t-2;
    owner release acceptance from t-3: "Запускаем". On 2026-06-28 the owner supplied a correction
    showing that 8aa14f8 falsely resolved x_training_activity to ACTIVE/DAY_LOOP on sample-only
    evidence. Bounded product repair health-ai 1fe41c2 supersedes that false launch route:
    training/activity now resolves to PROGRAM awaiting Deep Research, blocks proposal/ACTIVE/week/
    session until a suitable returned research conclusion plus owner approval exists, and keeps
    first real performed session unclaimed.

    Owner clarified on 2026-06-28 that Direction OS must not track Health AI projects/processes by
    default: "мы не трэкаем проекты если только я прямо не попрошу". Health AI may continue its
    nutrition/training work outside Direction OS. Direction OS will handle nutrition/training issues,
    returned conclusions, repairs or process-development decisions only when the owner explicitly
    brings them back.

tasks: []

open_calls:
  - id: c-health-map-evidence-001
    to: research
    direction: health
    play: research
    node: g-health-root
    goal: |
      Produce fresh map_evidence for routing the owner's new health wants into the next planning target, parked item, or explicit defer.
    context: |
      State pointers:
      - live/health/CHARTER.md
      - live/health/TREE.md
      - live/health/NOW.md
      - live/health/knowledge/health-direction-os-tracking-boundary.md

      Current state summary:
      - active_bet: none.
      - tasks: [].
      - open_calls before this checkpoint: [].
      - g-health-core is done.
      - g-health-nutrition-system is parked with partial current progress as a thin Health AI nutrition domain.
      - g-health-training-activity-system is done as product/process work, with 2026-06-28 repair boundary: current authority is health-ai @1fe41c2; x_training_activity is PROGRAM awaiting Deep Research; no ACTIVE real training program, week, session, or first real performed session is claimed.
      - Direction OS boundary: do not track Health AI projects/processes or raw body/nutrition/training data by default. Health AI may operate internally; Direction OS receives only summary, decisions, problems, repairs, or explicitly requested process-development work.

      Owner candidates from this session:
      1. Cross-domain Health AI area/service:
         Aggregates information from all other Health AI domains; watches goal execution and metrics; checks consistency between domain reports/plans; proposes improvements; may customize domain processes; may run init by inspecting existing state, asking questions, researching, or defining what should be tracked.
      2. Gameful activity/training:
         Strava-like challenges, competitive/game mechanics, and more motivating activity/training loops.
      3. Separate cooking domain:
         A domain for richer cooking/recipes/process beyond currently simple recipes.
      4. Automation/integrations:
         Optional later work around apps such as Strava and Hevy, including pulling/pushing data or using external apps/storage rather than keeping everything in GitHub.

      The research should treat owner lines as candidates, not automatic priorities.
    boundaries: |
      Do not select or activate a bet.
      Do not design a full architecture.
      Do not create routine execution/tracking cycles.
      Do not poll nutrition/training research status.
      Do not include raw health/training/nutrition/body-execution data.
      Keep Direction OS at strategy, decisions, summary, repairs, and bounded routing.
    done_when: |
      A compact map_evidence brief exists that:
      - maps each owner candidate to health charter success criteria and lenses;
      - evaluates leverage, sequencing, risk, and whether it is top-level TREE-worthy, a child/domain concern, recurring lane, or parked capture;
      - identifies overlaps/conflicts between candidates, especially cross-domain review vs Health AI core responsibilities;
      - includes one non-obvious path, outlier, or far analogy relevant to achieving the health direction's success criteria;
      - recommends input for the next map skeleton without activating any bet.
    return: |
      RESULT with outcome, evidence, candidate routing table, recommended skeleton input, captures, no TREE/NOW state_changes except returning to parent, and next return-to-parent c-health-owner-wants-planning-001.
    budget: one research session
    parent: c-health-owner-wants-planning-001

recurring:
  - id: r-health-ai-minor-fix-lane
    goal: >
      Keep a lightweight intake lane for minor Health AI UX/contract/prompt
      papercuts that do not justify a full direction bet.
    done_when: >
      Due minor Health AI issues are batched into a bounded repair/executor CALL
      or explicitly deferred/dropped; no raw health diary enters Direction OS.
    cadence: on_demand
    lens: ai-system-data-architecture
    last_done: 2026-06-28
    note: >
      Post-1338a35 bounded work was reconciled into this lane: menu workflow
      structure repair and owner_fact_delta/assumption hardening
      (7cd962a, 83dba88, 77a0ed), followed by fixed-menu/recipe support through
      health-ai 8246cec. On 2026-06-28 the lane handled the training/activity false
      launch-readiness repair in health-ai 1fe41c2: validation.config was re-synced to
      os-engineering-contract.v9, the training checker rejects the old ACTIVE/DAY_LOOP
      sample-launch state, and Health AI now blocks at PROGRAM awaiting Deep Research.
      The lane remains recurring/on-demand, not a second active bet. Authority, safety,
      provider-portability or owner-gate defects escalate to a bounded repair/executor
      CALL; cosmetic papercuts are batched, deferred or dropped.

decisions: []

next: |
  CALL c-health-map-evidence-001
  to: research
  direction: health
  play: research
  node: g-health-root
  goal: |
    Produce fresh map_evidence for routing the owner's new health wants into the next planning target, parked item, or explicit defer.
  context: |
    Use the context and boundaries from NOW.md open_calls[c-health-map-evidence-001].
  boundaries: |
    Strategy evidence only; no bet activation; no raw health/training/nutrition/body data; no routine Health AI execution tracking.
  done_when: |
    Evidence brief is ready for parent map session to build the step-3 skeleton.
  return: |
    RESULT returning to c-health-owner-wants-planning-001.
  budget: one research session
  parent: c-health-owner-wants-planning-001

END_OF_FILE: live/health/NOW.md
