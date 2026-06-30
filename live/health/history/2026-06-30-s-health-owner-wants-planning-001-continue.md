RESULT s-health-owner-wants-planning-001-continue (call: c-health-owner-wants-planning-001-continue)
direction: health   play: map   node/task: g-health-root

outcome: |
  Health root map routing is owner-approved.
  One new top-level TREE node is approved: g-health-hq-goal-coordinator.
  The node frames Health HQ v0 as an owner-facing goal-management and orchestration layer for Health AI:
  it manages health goals, runs owner-triggered reviews, coordinates domains, defines domain integration contracts,
  and routes correction requests without replacing domains or silently editing their artifacts.
  No bet is activated and no tasks are created.

evidence: |
  State read:
  - live/health/CHARTER.md: mission includes weight loss from 125 kg toward ~90 kg, strength/athletic outcome,
    maintenance, and Health AI as an operational support layer that does not pollute Direction OS with daily data.
  - live/health/TREE.md: existing root children include starter-kit done, old ai-core dropped, core done,
    nutrition-system parked/current partial progress, first-nutrition-cycle dropped, and training-activity-system done
    as product/process boundary with real training program still awaiting suitable research/owner approval.
  - live/health/NOW.md: active_bet none, tasks empty, open_calls empty, next was return-to-parent
    c-health-owner-wants-planning-001.
  - live/health/history/2026-06-29-s-health-owner-wants-planning-002.md: owner supplied four planning candidates:
    cross-domain Health AI layer, gameful activity/training, separate cooking domain, and automation/integrations.
  - live/health/history/2026-06-29-c-health-map-evidence-001.md: research bottom line said only the cross-domain
    Health AI layer may be TREE-worthy now, while gameful belongs under training/activity later, cooking stays
    nutrition capsule unless concrete bottleneck appears, and integrations are deferred.

  Owner words / decisions in this session:
  - Owner rejected the too-small "reviewer only" framing and clarified the desired layer as a higher-level Health AI
    coordinator / dashboard-like front door that leads toward goals, syncs domains, and can initiate processes.
  - Owner clarified the priority of goal management:
    "важный функционал... это управление целями, чтобы... вести к ним"
  - Owner clarified that Health HQ should review progress, find weak points, and route issues into domains without
    changing domain artifacts directly:
    "он как бы... должен заниматься... посмотреть, что где слабо, что где можно подстроить...
     он не менял ничего в domain... он инициализировал процедуру"
  - Owner clarified that the system should remain owner-triggered, not self-checking:
    "в этом направлении оно ничего само не проверяет. Все проверки только через меня"
  - Owner added that current and future domains need their own structure for HQ integration:
    "domains... если новые будут добавляться и текущие, имели вообще вот свою структуру...
     что должно интегрироваться в Health HQ... репорты делать"
  - Per-card verdict: owner accepted the Health HQ v0 + domain integration contract card with:
    "Accept"
  - Order verdict: owner accepted the proposed order with:
    "Accept order"
  - Whole-tree close verdict: owner approved the whole tree with:
    "Approve whole tree"

state_changes: |
  TREE.md:
  - Keep existing root and existing root children unchanged.
  - Append the following new child under root.children, after g-health-training-activity-system:

      - id: g-health-hq-goal-coordinator
        goal: >
          Health AI имеет верхний Health HQ v0: owner-facing goal-management и orchestration слой.
          Owner может обращаться к нему как к главному входу в Health AI: "что сегодня?",
          "разбери неделю", "проверь прогресс", "где bottleneck?", "добавить новый процесс?".
          Health HQ ведёт явную структуру целей, текущую фазу, phase metrics, domain responsibilities,
          review/decision log; проводит on-demand daily/weekly-style reviews; синхронизирует
          nutrition/training/activity/recovery; готовит routed correction requests в домены;
          задаёт минимальный domain integration contract для текущих и будущих доменов.
        why: >
          Root health goal требует не только отдельных nutrition/training процессов, а согласованного
          движения к весу, силе, атлетичному виду, энергии и maintenance. Health HQ нужен, чтобы домены
          не оптимизировали локально и не конфликтовали между собой.
        done_when:
          - Есть явная верхняя goal structure: root health goals, current phase, phase metrics,
            domain responsibilities, review/decision log.
          - Health HQ принимает owner-запросы типа "что сегодня?", "разбери неделю",
            "проверь прогресс", "где bottleneck?".
          - Есть минимальный domain integration contract для current/future domains:
            responsibility; supported goals; summary/report format для HQ; metrics/signals exposed
            to HQ; accepted correction/request types; boundaries: что HQ не меняет напрямую.
          - Nutrition и training/activity имеют хотя бы thin summary/report adapter для HQ;
            если real data ещё мало, proof использует clearly marked sample/test fixtures.
          - Health HQ проводит один dry-run или partial-real goal review across nutrition +
            training/activity + goal state.
          - Review выдаёт progress verdict, bottleneck/uncertainty, routed requests в домены,
            owner decisions если нужны, и какие метрики нужны сейчас/позже.
          - Health HQ не меняет domain artifacts silently: только маршрутизирует correction через
            domain procedures и owner/governance gates.
          - Direction OS получает только summary, decisions, problems, next CALL; raw body/nutrition/
            training data остаются вне Direction OS.
        status: parked
        children: []

  - Update TREE.md owner_approved / approval_evidence to include:
      Owner approved adding g-health-hq-goal-coordinator on 2026-06-30 in map close with:
      "Approve whole tree". The node is parked and creates no active bet or tasks.

  NOW.md:
  - active_bet remains:
      status: none
  - tasks remains: []
  - open_calls remains: []
  - decisions remains: []
  - next becomes the following ready CALL:

      CALL c-health-shape-hq-goal-coordinator-001
      to: session
      direction: health
      play: shape
      node: g-health-hq-goal-coordinator
      goal: |
        Shape the owner-approved g-health-hq-goal-coordinator node into the next possible health bet without activating it.
        The shaped bet should test the smallest useful Health HQ v0: goal structure, owner-triggered review, domain
        integration contract, and routed correction requests.
      context: |
        Read:
        - live/health/CHARTER.md
        - live/health/TREE.md
        - live/health/NOW.md
        - live/health/history/2026-06-29-c-health-map-evidence-001.md
        - this map RESULT

        Owner-approved node:
        g-health-hq-goal-coordinator = Health HQ v0 as owner-facing goal-management/orchestration layer.
        It is not just a reviewer and not a visual dashboard. It should manage goals, current phase, phase metrics,
        domain responsibilities, review/decision log, on-demand reviews, domain coordination, and domain integration
        contracts.

        Owner constraints captured during map:
        - All checks/reviews are owner-triggered; Health AI does not self-check or poll by default.
        - Health HQ may diagnose and route but must not silently edit nutrition/training/activity artifacts.
        - Current and future domains need a structure for integration with Health HQ: summaries/reports, supported goals,
          exposed signals/metrics, accepted correction request types, and boundaries.
        - Training starts only now and nutrition has only partial recent real use, so proof may use clearly marked
          sample/test fixtures where real weekly data is not yet available.
      boundaries: |
        Do not activate a bet until shape is complete and owner approves.
        Do not create tasks before bet shaping gates are satisfied.
        Do not design a full future architecture.
        Do not build a visual dashboard, API/integration layer, automatic polling, gameful engine, cooking domain,
        habit system, sleep domain, or medical domain in this shape.
        Do not store raw body/nutrition/training data in Direction OS.
        Keep Health HQ as coordinator/front door/goal manager, not a god-agent replacing domains.
      done_when: |
        Shape output is ready for owner decision and includes:
        - appetite and kill_by;
        - cut list with at least one real cut;
        - lens sweep verdict per charter lens;
        - riskiest assumption and first task proposal testing it;
        - explicit proof target for smallest useful Health HQ v0;
        - clear boundary for domain integration contracts and owner-triggered reviews.
      return: |
        RESULT with shaped bet proposal, cut list, lens sweep, recommended first task, state_changes only if owner approves,
        and next.
      budget: one shape session

  LOG.md:
  - Append:
      2026-06-30 map health/root: owner approved adding parked g-health-hq-goal-coordinator as Health HQ v0
      goal-management/orchestration node; next is shape on that node; no bet activated.

  history/:
  - Add this RESULT as:
      live/health/history/2026-06-30-s-health-owner-wants-planning-001-continue.md

captures:
  - parked: gameful activity/training challenge layer belongs under g-health-training-activity-system after safe training/activity program boundary and HQ reporting contract are stable.
  - parked: cooking should remain a nutrition capsule unless cooking workflow friction becomes a concrete bottleneck not covered by nutrition.
  - deferred: Strava/Hevy/API integrations should wait until manual/export/import contracts and source-of-truth value are stable.
  - risk: Health HQ can become a god-agent/dashboard/product yak-shave unless v0 is cut to goal structure, owner-triggered review, domain integration contract, and routed correction requests.
  - future-shape-input: Health HQ should support phased metric governance so early focus can stay on weight/adherence/energy/training completion, while later phases add strength/body-composition/visual-form indicators.

decisions_needed: []

play_check:
  - 1 Recite: done — mission, success criteria, current TREE/NOW state, and Direction OS raw-data boundary were summarized before skeleton work.
  - 2 Candidates & evidence (owner): done — owner candidates came from prior parent session; fresh map_evidence existed in live/health/history/2026-06-29-c-health-map-evidence-001.md.
  - 3 Skeleton (owner): done — one-screen skeleton was shown; owner rejected the too-small reviewer framing and clarified the desired Health HQ/coordinator direction.
  - 4 Cards: done — card was elaborated for g-health-hq-goal-coordinator with goal, done_when, why, edge, risk, cuts, and domain integration contract.
  - 5 Per-node verdict (owner): done — owner accepted the card with "Accept".
  - 6 Order (owner): done — owner accepted the order with "Accept order".
  - 7 Depth check: done — only one top-level node is approved; deeper elements stay in done_when/cuts or parked/deferred.
  - 8 Lens sweep on the map: done — weight/nutrition, strength/body composition, activity/conditioning, adherence/relapse, medical safety, and AI/data architecture were checked; no extra TREE node was needed.
  - 9 Close (owner): done — owner approved the compact whole-tree change with "Approve whole tree".

log: |
  map health/root: owner approved parked g-health-hq-goal-coordinator as Health HQ v0 goal-management/orchestration node with domain integration contract; next is shape; no bet activated.

next: |
  CALL c-health-shape-hq-goal-coordinator-001
  to: session
  direction: health
  play: shape
  node: g-health-hq-goal-coordinator
  goal: |
    Shape the owner-approved g-health-hq-goal-coordinator node into the next possible health bet without activating it.
    The shaped bet should test the smallest useful Health HQ v0: goal structure, owner-triggered review, domain
    integration contract, and routed correction requests.
  context: |
    Read:
    - live/health/CHARTER.md
    - live/health/TREE.md
    - live/health/NOW.md
    - live/health/history/2026-06-29-c-health-map-evidence-001.md
    - live/health/history/2026-06-30-s-health-owner-wants-planning-001-continue.md

    Owner-approved node:
    g-health-hq-goal-coordinator = Health HQ v0 as owner-facing goal-management/orchestration layer.
    It is not just a reviewer and not a visual dashboard. It should manage goals, current phase, phase metrics,
    domain responsibilities, review/decision log, on-demand reviews, domain coordination, and domain integration
    contracts.

    Owner constraints captured during map:
    - All checks/reviews are owner-triggered; Health AI does not self-check or poll by default.
    - Health HQ may diagnose and route but must not silently edit nutrition/training/activity artifacts.
    - Current and future domains need a structure for integration with Health HQ: summaries/reports, supported goals,
      exposed signals/metrics, accepted correction request types, and boundaries.
    - Training starts only now and nutrition has only partial recent real use, so proof may use clearly marked
      sample/test fixtures where real weekly data is not yet available.
  boundaries: |
    Do not activate a bet until shape is complete and owner approves.
    Do not create tasks before bet shaping gates are satisfied.
    Do not design a full future architecture.
    Do not build a visual dashboard, API/integration layer, automatic polling, gameful engine, cooking domain,
    habit system, sleep domain, or medical domain in this shape.
    Do not store raw body/nutrition/training data in Direction OS.
    Keep Health HQ as coordinator/front door/goal manager, not a god-agent replacing domains.
  done_when: |
    Shape output is ready for owner decision and includes:
    - appetite and kill_by;
    - cut list with at least one real cut;
    - lens sweep verdict per charter lens;
    - riskiest assumption and first task proposal testing it;
    - explicit proof target for smallest useful Health HQ v0;
    - clear boundary for domain integration contracts and owner-triggered reviews.
  return: |
    RESULT with shaped bet proposal, cut list, lens sweep, recommended first task, state_changes only if owner approves,
    and next.
  budget: one shape session

END_OF_FILE: live/health/history/2026-06-30-s-health-owner-wants-planning-001-continue.md
