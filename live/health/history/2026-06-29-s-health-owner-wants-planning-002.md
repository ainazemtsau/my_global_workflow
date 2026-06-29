RESULT s-health-owner-wants-planning-002 (call: c-health-owner-wants-planning-001)
direction: health   play: map   node/task: g-health-root
outcome: |
  Owner candidates for the next health planning target were received and normalized for evidence routing.
  No next bet was selected or activated yet.
  The session checkpointed because play map step 2 requires fresh map_evidence unless the owner explicitly waives it; no waiver was given.
evidence: |
  Owner provided new wants in-session:
  - "нужно создать условно какую-то область в health ai, которая будет собирать данные со всех остальных health ai... агрегировать информацию... смотреть за выполнением целей, за метриками... предлагать какие-то улучшения"
  - "возможность... чтобы она могла кастомизировать какие-то процессы... домейны уже кастомизировать... ревью, чтобы она делала как бы общее"
  - "Strava есть приложение, и там есть всякие челленджи... более игровой тематики сделать... тренировки"
  - "вынести отдельно domain готовка"
  - "посмотреть в сторону автоматизации... Strava, Heavy... оттуда данные подтягивать или туда их сохранять"
  Current state context remains: no active_bet, no tasks, no open_calls; Direction OS must not create routine Health AI tracking/execution cycles unless explicitly requested.
state_changes: |
  TREE.md: no changes.
  NOW.md:
  - active_bet remains:
      status: none
  - tasks remains: []
  - open_calls add:
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
  - next becomes:
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
captures: []
decisions_needed: []
play_check:
  - "1 Recite: done — current health mission/tree/NOW boundary was recited before owner intake; no state change has occurred since."
  - "2 Candidates & evidence (owner): done for candidates — owner supplied candidates with: 'Вот это первое. Второе... Ну и третье... следующий... автоматизации'; evidence part checkpointed because fresh map_evidence is missing and owner did not waive it."
  - "3 Skeleton (owner): skipped — blocked until c-health-map-evidence-001 returns."
  - "4 Cards: skipped — pending skeleton."
  - "5 Per-node verdict (owner): skipped — pending cards."
  - "6 Order (owner): skipped — pending node verdicts."
  - "7 Depth check: skipped — pending accepted top-level candidates."
  - "8 Lens sweep on the map: skipped — pending draft map."
  - "9 Close (owner): skipped — no owner-approved whole tree or routing verdict yet."
log: |
  map health/root: owner supplied four next-health candidates; spawned c-health-map-evidence-001 for evidence before skeleton; no bet activated.
next: |
  CALL c-health-map-evidence-001
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

    Owner candidates:
    1. Cross-domain Health AI aggregation/review/customization service.
    2. Gameful activity/training, Strava-like challenges.
    3. Separate cooking domain.
    4. Automation/integrations with apps such as Strava and Hevy.

    Use the full open_calls[c-health-map-evidence-001] context from state_changes above.
  boundaries: |
    Do not select or activate a bet.
    Do not design full architecture.
    Do not create routine execution/tracking cycles.
    Do not poll nutrition/training research status.
    Do not include raw health/training/nutrition/body-execution data.
  done_when: |
    A compact evidence brief exists for the parent map session: candidate-to-lens mapping, leverage/risk/sequence evaluation, TREE-worthy vs parked/child/lane verdicts, one non-obvious path, and recommended skeleton input.
  return: |
    RESULT returning to parent c-health-owner-wants-planning-001.
  budget: one research session
  parent: c-health-owner-wants-planning-001

END_OF_FILE: live/health/history/2026-06-29-s-health-owner-wants-planning-002.md
