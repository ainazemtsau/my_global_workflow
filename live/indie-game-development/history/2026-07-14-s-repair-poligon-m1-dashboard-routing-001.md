RESULT s-repair-poligon-m1-dashboard-routing-001 (call: owner-message-poligon-m1-dashboard-routing-001)
direction: indie-game-development   play: repair   node/task: g-9c41/Poligon-M1-dashboard-routing
outcome: |
  Главная владельческая панель теперь показывает путь к сильной интеграционной сцене Полигона М1,
  а NearGas dashboard явно остаётся дочерним техническим зеркалом gas-engineering. Шесть трасс — gas,
  Level/DA/PGG, character, integration lab, visual, network/min-spec/final evidence — имеют текущий статус,
  зависимости, площадки, границы merge и явную параллельность.
  Ратифицированный DA/PGG-маршрут восстановлен без возобновления Phase 0: старый невозможный Level PLAN
  помечен SUPERSEDED / NEVER ISSUE. Основной следующий вход уже продвинут отдельным подтверждённым repair до
  NearGas PLAN-AMEND/Re-sync v20→v21; параллельно готовы Direction-only анализ общего M1-маршрута и owner-present
  Frame v2. Product BUILD не запускался, скрытого 14-го product leg не появилось.
evidence: |
  - Владелец после полного brief исправленного состояния выбрал дословно: «A1».
  - `live/indie-game-development/NOW.md` хранит две active tasks, неизменные предел 13 product legs и stop-line
    2026-07-24; M1-Integration-ROUTE прямо помечен Direction-only/non-product-leg. `NOW.next` указывает на
    `work/c-exec-near-gas-core-authority-001-plan-amend-resync-002-call.md`; gas/runner/character BUILD не runnable.
  - Создан self-contained `work/c-work-poligon-m1-integration-route-001-call.md` со всеми шестью трассами,
    точным appetite accounting, матрицей параллельности и owner-verdict gate; он READY PARALLEL и не мутирует product.
  - `work/c-exec-level-platform-phase1-plan-001-call.md` сохраняет историческое тело, но имеет явный статус
    SUPERSEDED / NEVER ISSUE и указывает на свежий M1 successor route. Сохранён доказанный маршрут:
    project-owned full-3D Level/Module Contract + validators → DA runtime + PGG editor-time bake/import → content.
  - `work/board/dashboard.html` имеет M1 title/hero и finish line, шесть полноширинных track-карточек,
    явную таблицу последовательности/параллельности, актуальные Board/Journal и gas PROGRAM как дочернюю линию.
  - Static HTML QA: 8/8 section, 3/3 details и 2/2 table open/close; current routing не содержит старого
    engineering-repair PRIMARY, а execute-002 везде остаётся только CHECKPOINT / NOT DELIVERED.
  - Automated visual render не выполнен: in-app Browser отклонил локальный `file:///` URL и прямо запретил
    browser/CDP/local-server обход. Ограничение не обходилось; панель остаётся обычным локальным HTML для owner-eye.
  - Semantic rebase сохранил concurrent Canon checkpoint `83568c7`, binding engineering repair `5946277` и
    независимый `.gitattributes` commit `45af36c`; engineering repair уже потребил старый repair CALL, закрепил
    execute-002 как CHECKPOINT / NOT DELIVERED и открыл текущий PLAN-AMEND/Re-sync, поэтому stale CALL не воскресал.
  - TREE.md, CHARTER.md, product repos и gas child-dashboard не менялись. Чужая dirty-правка
    `work/marketing/handle-reservation-inomand.md` сохранена и исключена из session commit.
state_changes: |
  - SET `NOW.md.updated` = `2026-07-14 by s-repair-poligon-m1-dashboard-routing-001`; compact hot-state narrative
    without changing the 13-leg/2026-07-24 limits or the binding engineering-repair outcome.
  - UPDATE `NOW.md.bet.forecast`, `against` and `technical_feasibility`: Direction board is the M1 owner view;
    gas PROGRAM is a child lane; the ratified Level Contract → DA runtime + PGG editor-time → content route survives;
    the old Phase-0-gated call is invalid; exact appetite reconciliation remains pending.
  - UPSERT active task `M1-Integration-ROUTE` as Direction-only/non-product-leg and UPSERT open_call
    `c-work-poligon-m1-integration-route-001` as READY PARALLEL. Preserve concurrent Frame v2 READY PARALLEL,
    NearGas PLAN-AMEND/Re-sync PRIMARY, HELD runner/character, and SET `NOW.next` to the existing Re-sync CALL.
  - CREATE `work/c-work-poligon-m1-integration-route-001-call.md`. PATCH the old Level PLAN status to
    SUPERSEDED / NEVER ISSUE while preserving its historical body and ratified phasing evidence. Do not create or
    restore the consumed engineering-v21 repair CALL.
  - REGENERATE `work/board/dashboard.html` per `knowledge/g9c41-lanes-venues.md`: primary M1 framing,
    six tracks, explicit parallelism, live open-call cards, current journal/problems, gas as child, unified finish.
  - APPEND the declared LOG line once; ADD this full RESULT once to
    `history/2026-07-14-s-repair-poligon-m1-dashboard-routing-001.md`.
  - Preserve TREE.md, CHARTER.md, all product repositories, product NearGas dashboard, concurrent routing/canon
    outcomes and unrelated dirty files.
captures: []
decisions_needed: []
play_check:
  - 1 Name the contradiction: done — M1 outcome required a unified DA/PGG+gas+character+network scene, while the visible engineering roadmap was gas-only; the ratified level route waited on Phase 0 that is NEVER RESUME.
  - 2 Reconstruct: done — newest-first NOW/LOG/history/findings, gas PROGRAM, PGG spike/analysis, level phasing, character frozen PLAN and lane rules showed that PGG evidence survived; the concurrent engineering repair later made NearGas Re-sync the only primary product route.
  - 3 Propose corrected state: done — owner received the exact A1 diff: main M1 board, gas child, six tracks, parallel Direction plan, superseded old Level CALL, no silent 14th leg or BUILD.
  - 4 Confirm: done — owner actual words: «A1».
  - 5 Friction: skipped — this was one direction-level routing/render drift; existing owner-panel regeneration rules and the repaired engineering finding already cover the mechanisms, so no new OS-rule claim was invented.
log: 2026-07-14 — repair/route (g-9c41/Poligon-M1-dashboard-routing, s-repair-poligon-m1-dashboard-routing-001): owner «A1» made the Direction board the M1 integration-scene roadmap, kept gas as a child lane, preserved Level/DA/PGG through a fresh successor route, and registered whole-M1 planning READY PARALLEL alongside the current NearGas PLAN-AMEND/Re-sync PRIMARY; no product BUILD. → history/2026-07-14-s-repair-poligon-m1-dashboard-routing-001.md
next: |
  # CALL c-exec-near-gas-core-authority-001-plan-amend-resync-002

  to: executor
  direction: indie-game-development
  kind: engineering
  repo: C:\projects\Unity\GasCoopGame_core
  project: GasCoopGame
  node: g-9c41
  task: NearGas-L1-BUILD
  phase: PLAN-AMEND / RE-SYNC
  issued: 2026-07-14 (s-repair-daily-engineering-v21-routing-20260714-001)
  parent: s-repair-daily-engineering-v21-routing-20260714-001

  goal: |
    NearGas L1 has a product-contract-v21, owner-approved frozen planning authority from which a fresh independent
    RED author can instantiate every required acceptance, NegativeControl and Property witness without guessing,
    while L1 remains NOT DELIVERED and implementation has not started.

  context: |
    Direction engineering-contract authority is exact commit 8aa4d02750bc77d504e8badb01eee9d989d60dcb in
    C:\my_global_workflow_worktrees\indie-game-development; live state was semantically rebased through concurrent
    writer HEAD 83568c73880a7de09e76b097cffbcd7803887ac4. Current contract v21 is only the semantic full-packet
    handoff in os/engineering/CONTRACT_VERSION, CONTOUR.md, VALIDATION.md, PROJECT_SETUP.md and
    os/adapters/coding-agent.md. Deleted transaction/schema/TESTABILITY/receipt/conformance requirements from earlier
    failed v21 drafts are not authority and must not be restored.

    Product authority remains origin/main@32107343d75240d6b3bc850d7010bd3f17dc4ca8. Its frozen L1 packet contains
    owner-approved PLAN@1e4e78c and PLAN-AMEND@a58ee3567f08ba8e2c16e88c851e3de89f0678c6. The original BUILD
    checkpoint is b94806deaaa3cbb56a8b6cda9baa75ac52f028c3. Product contract is v20.

    Returned execute evidence is commit 5c783e07b5378dece1e0664b203c4e147edacd68, 0 behind / 1 ahead of that main.
    Its committed docs/results/c-exec-near-gas-core-authority-001.md says PRODUCT EXECUTE-002 CHECKPOINT /
    SPEC-ONLY RED BLOCKED / NOT DELIVERED. The fresh author stopped before a test file or commit. Production BUILD,
    tests, tools/check, review, mutation, binding G5, Deliver, Unity, merge and push did not run.

    The full known gap set is: VoxelImpulse/FaceRef construction; open and sealed two-room topology/aperture fixtures;
    NoSourceGolden and SourceChecksumIsolation inputs; ReactionRuleSet/custom-kind construction; audit-counter
    observation; hidden-state observation; handler-instance ownership; GasScenario/LockstepLoopback construction,
    return observation and delegation plant; injectable same-assertion shapes for several NegativeControls.

    Frozen authority to reconcile as one packet:
    - openspec/changes/c-exec-near-gas-core-authority-001/PLAN.md
    - openspec/changes/c-exec-near-gas-core-authority-001/proposal.md
    - openspec/changes/c-exec-near-gas-core-authority-001/specs/sim-core/spec.md
    - openspec/changes/c-exec-near-gas-core-authority-001/tasks.md
    - docs/adr/ADR-E-0011-c-exec-near-gas-core-authority-001-atomic-core-owner.md

    The existing owner-approved construction A / fault A choices remain binding, but their local blocker GREEN was
    never whole-suite readiness. Option A remains serial concurrency-ready; real workers stay deferred until delivered
    L1/L2/C1 plus fresh profiling.

  boundaries: |
    This is an owner-present planning amendment and contract-only v20→v21 Re-sync. Product source, tests, gate scripts,
    scenes and assets are out of scope. Do not author RED tests, commission the later independent test-author, implement,
    build, run tests/tools/check/review/mutation/Deliver, launch Unity/MCP, merge or push.

    The fresh semantic reviewer may fact-check existing public signatures and harness facts read-only, but every fact it
    uses must be copied into the final spec. Do not create a parser, regex scanner, schema compiler, conformance program
    or other self-written completeness checker; plan/spec completeness is semantic AI judgment under current v21.

    Do not use the lagging C:\projects\Unity\GasCoopGame checkout as authority. Do not assign, switch, clean, stage,
    overwrite or otherwise touch C:\projects\Unity\GasCoopGame_dev; it contains foreign uncommitted changes. Preserve
    all existing L1 meaning, option A, legacy-audit obligations and deferred-worker boundary unless the owner explicitly
    revises them in this PLAN session.

    A blocker-only GREEN cannot open execution. Even a full-packet GREEN returns home to Direction for a separate fresh
    binding review. Do not author an EXECUTE/BUILD CALL or the next Direction CALL.

  done_when: |
    1. Product §Re-sync moves the repo-local contract stamp exactly v20→v21 and mirrors current v21 only in the root run
       contract and OpenSpec planning guidance, with the product maintenance record updated. Re-sync changes no product
       source, tests or gate scripts and introduces no mechanical semantic-completeness checker.
    2. The full PLAN/proposal/spec/tasks/ADR packet is mutually consistent, owner-readable and still explicitly
       NOT DELIVERED. It contains none of the deleted transaction/schema/TESTABILITY/receipt/conformance machinery.
    3. Every acceptance criterion, NegativeControl token and Property row owns one exact five-field recipe:
       `fixture | call | observe | source | negative`. Constructors/signatures/literals, assertion/evidence seams,
       golden/input authorities and deliberately-wrong injectable shapes are concrete rather than inferred.
    4. The complete known nine-group gap set is resolved in the frozen text, and a whole-packet inventory proves that
       no additional acceptance, NegativeControl or Property obligation was omitted.
    5. A fresh read-only semantic AI reviewer independently derives the complete obligation set from the entire final
       candidate, writes one concise test skeleton for every row and returns the complete gap list for each RED pass.
       Any packet edit invalidates the verdict and triggers another full run. Final GREEN is against the exact final
       packet and has zero unresolved, inferred, hidden, `n/a` or merely-future-test cells.
    6. Only after that final full-packet GREEN, the owner reads the detailed plain-language amendment and gives actual
       approval words. The frozen final packet and evidence commit record those words and the exact reviewed revision.
    7. Product RESULT/dashboard truthfully report PLAN-AMEND / RE-SYNC only, L1 NOT DELIVERED, no actual RED-test or
       implementation activity, and no build/test/check/review/mutation/G5/Deliver/Unity/merge/push claim.
    8. The return explicitly routes to a separate fresh Direction binding review. It contains no EXECUTE/BUILD CALL and
       no statement that a local blocker close, product commit or full-packet GREEN alone authorized execution.

  return: |
    Product PLAN-AMEND / RE-SYNC RESULT HOME with base/branch/commit and exact changed paths; v20→v21 contract diff and
    stamp; the complete obligation inventory with every five-field recipe and test skeleton; every full-pass gap list,
    amendment/rerun sequence and final exact-packet GREEN evidence; owner approval words; proof that product source,
    tests, gate scripts, Unity and delivery gates were untouched; L1 status NOT DELIVERED; and an explicit return to
    Direction for the separate fresh binding review. If full GREEN plus owner approval cannot be completed, return a
    CHECKPOINT / NOT DELIVERED with the complete remaining gap list and no downstream CALL.

  budget: one owner-present PLAN-AMEND / Re-sync session; checkpoint rather than shortcut
  surface: any

END_OF_FILE: live/indie-game-development/history/2026-07-14-s-repair-poligon-m1-dashboard-routing-001.md
