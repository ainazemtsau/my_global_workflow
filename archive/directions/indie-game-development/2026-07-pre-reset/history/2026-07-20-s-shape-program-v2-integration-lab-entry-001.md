RESULT s-shape-program-v2-integration-lab-entry-001 (call: c-shape-program-v2-integration-lab-entry-001)
direction: indie-game-development
track: program
play: shape
node/task: g-9c41/integration-lab-entry

outcome: |
  Владелец утвердил один постоянный product-proof entry: `Integration Lab`. Это не маленькая статичная
  газовая демка и не общий debug framework, а будущий playable skeleton игры. Она должна принимать
  сформированные Level-треком профили Dungeon Architect от малого до большого generated level и
  проверять модули через настоящие gameplay objects, commands/events и production consumers.

  Отдельные track scenes не являются обязательной постоянной архитектурой. Bounded fixture/harness
  допустим только пока он является доказанно нужным validator; после утраты этой роли он становится
  кандидатом на удаление. Планируемая `NearGasSimulationLab` не получает отдельное постоянное место
  автоматически и не дублирует Integration Lab.

  Debug-функции добавляются только по фактической необходимости. Например, inspector action на
  gameplay gas cylinder может отправить тот же production event, что и реальное разрушение игроком;
  он не мутирует симуляцию отдельным обходным путём. Generic spatial picker, fill-room command,
  record/replay, benchmark UI и module controls сейчас не заказаны. Каждый Gas, Grid, Level, Character,
  loot или иной capability сначала получает отдельную shape/PLAN границу.

  Ни одна существующая scene не принята как основа. Старые lab/demo scenes и их scene-only support
  surface должны быть удалены, если они не нужны текущей authority/validator, без переноса legacy ради
  сохранения. Первый и единственный следующий шаг — строго read-only purge-аудит с verdict
  `DELETE / KEEP / BLOCKED`; удаление, PLAN и продуктовая работа в этой сессии не начинались.

evidence: |
  | Проверка | First-hand evidence | Вывод |
  | --- | --- | --- |
  | Существующая общая сцена | clean product `C:\projects\Unity\GasCoopGame`, branch `main`, HEAD `45b15623120f395b4295e43ac6cc5ed0c3aa108c`; inventory `Assets/**/*.unity` | Найдены 12 scenes, но ни `IntegrationLab`, ни `NearGasSimulationLab` не существуют. Подходящей уже принятой общей сцены нет. |
  | Фактические scene families | `SampleScene`; `GasSourcePhase0Demo`; `GasVoxelSandboxScene`; `GasBuoyancyDemoScene`; `GasBenchmarkScene`; `GasVisualScene`; `GasRoomScene`; `GasLabScene`; `ReactionSandboxScene`; три `Player*` proof scenes | Surface разнесён по demo/sandbox/visual/character families; его consumers и validators ещё не классифицированы, поэтому удалять сейчас нельзя. |
  | Связь с NearGas | `docs/gas-simulation/PROGRAM.md` L3 планирует создать engine-owned `NearGasSimulationLab` с нуля и временно удерживать старые gas/demo scenes до green replacements/visual dependencies | Это не готовая сцена, а прежний план. Owner verdict заменяет постоянную топологию на одну Integration Lab и требует audit/reconciliation retention clauses до purge. |
  | Дублирование компонентов | `VoxelSandboxDirector.cs` — 1722 строки; `GasDemoPlumeControls.cs` — 1798; `ReactionSandbox.cs` — 421; custom inspector — 173; `GasScenario.cs` — gas-specific legacy/concept surface | Существующая sandbox/control поверхность подтверждает риск второй монолитной Lab, но line count сам по себе не доказывает DELETE. Это вход в dependency audit. |
  | Общий seam | current sim-core SPEC описывает `LayerRegistry + RevisionFeed`, но не ownership общей scene | Технический seam не решает scene ownership и не превращает NearGas plan в постоянную Lab. |
  | Owner verdict | «Принимаю: одна постоянная Integration Lab, реальные gameplay paths, минимум debug-функций и сначала read-only purge-аудит» | Выбран вариант одной общей сцены; отдельная постоянная Gas lab и blocker отклонены. |

  В shape-сессии product branch, files, scenes, dependencies и versions не менялись; Unity и tests не
  запускались. Inspection была read-only. Direction-only state применяется этим RESULT отдельно.

recommendation: |
  Сначала провести узкий read-only dependency audit всех game-owned scene/support families. Для каждого
  семейства нужен только один исход: `DELETE` при first-hand отсутствии current consumer, `KEEP` при
  доказанной текущей authority/validator или `BLOCKED` с точной зависимостью и одним reconciliation need.
  После audit owner-present сессия решит purge PLAN; новая Lab, её код и module functionality до этого
  не начинаются.

alternatives: |
  1. Сделать `NearGasSimulationLab` постоянной общей сценой — отклонено: Gas ownership начал бы задавать
     общую product-proof topology и создавал бы риск специального обходного пути для других модулей.
  2. Создать постоянную Integration Lab плюс постоянные labs каждого трека и общий Lab framework —
     отклонено: это сразу создаёт maintenance и компоненты без доказанного consumer.
  3. Остановиться с blocker — не требуется: сцены ещё не созданы, а точную границу безопасного purge
     можно получить read-only аудитом.

owner_verdict: |
  Владелец утвердил рекомендацию дословно: «Принимаю: одна постоянная Integration Lab, реальные gameplay
  paths, минимум debug-функций и сначала read-only purge-аудит».

state_changes: |
  live/indie-game-development/NOW.md:
    - CLEAR returned program root `c-shape-program-v2-integration-lab-entry-001`.
    - ADD ready/default root `c-audit-program-v2-legacy-lab-surface-001` in track `program`, pinned
      `engineering_contract: 31`, for a read-only `DELETE / KEEP / BLOCKED` dependency audit.
    - SET `next.call` to `c-audit-program-v2-legacy-lab-surface-001`.
    - Preserve all concurrent tracks, unrelated calls and `d-m1-min-spec-hardware-001`; in particular,
      preserve the concurrently parked Build & Tooling route without restoring its retired live track id.
  live/indie-game-development/work/c-audit-program-v2-legacy-lab-surface-001-call.md:
    - CREATE the complete V31 read-only executor CALL with exact no-mutation boundary, pre/post hygiene
      gate and audit HOME contract.
  live/indie-game-development/work/program-v2-integration-lab-plan.md:
    - REPLACE the small static-shell assumption and unresolved ownership with the approved single
      permanent playable Integration Lab boundary, generated Level profiles, real gameplay paths,
      minimum on-demand debug and temporary-only track validators.
    - MAKE read-only purge audit the first step before any purge PLAN or M2 product work; keep milestone
      count at 2/10 because no scene or capability drop was built or accepted.
  live/indie-game-development/work/board/dashboard.html:
    - REGENERATE Board, Journal, Problems and relevant M2/track sections from fresh NOW/LOG/plan state;
      show the audit as default and the product PROGRAM retention conflict without changing unrelated routes.
  live/indie-game-development/LOG.md:
    - APPEND the declared one-line entry once.
  live/indie-game-development/history/2026-07-20-s-shape-program-v2-integration-lab-entry-001.md:
    - SAVE this complete RESULT.
  live/indie-game-development/TREE.md, CHARTER.md, decision ledger, product/canon repositories, product
  docs/code/scenes/assets, frozen calls, dependencies, versions, branches, worktrees, Unity and tests: unchanged.

captures:
  - Future Gas shape decides the smallest real gameplay source/event proof, including whether a cylinder inspector action is actually needed.
  - Generic picker, fill-room, record/replay and benchmark UI remain cut until a named experiment cannot be run cleanly without one.
  - Sleeping gas remains a lore-only future candidate and creates no current Lab requirement.

decisions_needed: []

play_check:
  - "1 Recite: done — Integration Lab is the eventual playable product skeleton that accepts verified track drops; the parent outcome remains a released Steam game, not a collection of demos."
  - "2 Appetite: done — this was one owner-present shape; the only continuation is a <=0.5 focused day read-only audit."
  - "3 Approaches: done — compared separate permanent common/Gas labs, a universal Lab framework with permanent track labs, and one permanent Integration Lab with temporary proof fixtures; selected the third."
  - "4 Scope hammer: done — cut product changes, permanent per-track scenes, generic framework, spatial picker, room-fill, record/replay, benchmark implementation, module feature work and legacy migration."
  - "5 Lens sweep: done — Gameplay is protected by real gameplay paths; Technical by first-hand dependency audit; Scope/Production by one permanent scene and minimum debug. Commercial, Co-op and Audience need no claim in this shape because nothing is published or accepted as multiplayer/product proof."
  - "6 Riskiest assumption: done — purge could delete a current authority/validator and debug could bypass gameplay; audit-first plus separate module shapes are the guardrails."
  - "7 Tasks: done — no scene/product task was launched; exactly one read-only audit root is the continuation."
  - "8 Kill criteria: done — any family without proof of no current consumer is KEEP or BLOCKED; the auditor may not guess DELETE or create a migration/shim."
  - "9 Close: done — owner verdict words are «Принимаю: одна постоянная Integration Lab, реальные gameplay paths, минимум debug-функций и сначала read-only purge-аудит»."

handoff: |
  status: not-ready
  result: One permanent playable Integration Lab is approved; real gameplay paths, generated Level profiles and minimum on-demand debug define its current boundary.
  proof: Clean product main 45b15623 has 12 scattered scenes but no IntegrationLab/NearGasSimulationLab, and the owner supplied the exact approving verdict.
  scene_drop: none
  blocker: none — the read-only audit must resolve current consumers and conflicting Gas PROGRAM retention clauses before purge PLAN.
  next: CALL c-audit-program-v2-legacy-lab-surface-001

log: 2026-07-20 · s-shape-program-v2-integration-lab-entry-001 · shape · program · g-9c41/integration-lab-entry: owner approved one permanent playable Integration Lab with generated Level profiles, real gameplay paths and minimum debug; no existing scene was accepted, no product work began, and one V31 read-only DELETE/KEEP/BLOCKED purge audit is the sole next step. → history/2026-07-20-s-shape-program-v2-integration-lab-entry-001.md

next: |
  # CALL c-audit-program-v2-legacy-lab-surface-001

  to: executor
  direction: indie-game-development
  track: program
  kind: engineering
  repo: ainazemtsau/GasCoopGame
  node: g-9c41
  task: legacy-lab-surface-audit
  issued: 2026-07-20 (s-shape-program-v2-integration-lab-entry-001)

  goal: |
    Установить точную first-hand границу удаления старых lab/demo scenes и scene-only support surface,
    чтобы новая постоянная Integration Lab начиналась без лишнего legacy и без потери действующей
    продуктовой authority или validator.

  context: |
    Владелец утвердил дословно: «Принимаю: одна постоянная Integration Lab, реальные gameplay paths,
    минимум debug-функций и сначала read-only purge-аудит».

    Постоянный product-proof entry один: Integration Lab. Она со временем принимает разные размеры и
    профили Dungeon Architect level generation и проверяет модули через настоящие gameplay objects,
    commands/events и production consumers. Debug-действие допустимо только как тонкий вызов того же
    production path, если без него проверка действительно неудобна. Track-specific fixture может жить
    лишь пока он является доказанно нужным validator; отдельная постоянная NearGasSimulationLab заранее
    не принята. Конкретные Gas, Grid, Level, Character, loot, benchmark и другие возможности формируются
    отдельными shape/PLAN по мере необходимости; универсальный Lab framework сейчас не заказан.

    First-hand shape evidence на clean product `main`
    `45b15623120f395b4295e43ac6cc5ed0c3aa108c` нашло 12 `.unity` scenes, но не нашло существующей
    `IntegrationLab` или `NearGasSimulationLab`. `docs/gas-simulation/PROGRAM.md` пока планирует новую
    engine-owned NearGasSimulationLab и временное сохранение старых gas/demo scenes; это нужно назвать
    как конфликт с новым owner verdict, а не молча перенести в cleanup. Current product authority и
    ссылки надо перечитать заново; указанный SHA — evidence shape-сессии, не freshness lock.

    Launch block: lane `program / Integration audit`; venue — текущий product `main` строго read-only,
    без отдельного worktree и без Unity Editor; machine `PC`; depends_on `[]`; merge_queue `none`;
    conflict_surface `none`, потому что продуктовые файлы не меняются. Gate — точные branch/HEAD/status
    до и после совпадают.

  boundaries: |
    Только read-only аудит. Не менять code, scenes, prefabs, assets, docs, specs, ADR, dependencies,
    packages, versions, branches или worktrees. Не запускать PLAN, PAIR, RED, BUILD, Unity, tests,
    import, merge, Deliver или publication. Ничего не удалять и не создавать. Не проектировать новую
    Lab architecture, module API или debug tool; не предлагать MIGRATE/SHIM как автоматическую судьбу
    legacy. Не считать archive authority. Vendor/sample assets не включать, если на них не ссылается
    game-owned surface. Если действующая authority или validator зависит от семейства, это KEEP либо
    BLOCKED, но не предположительный DELETE.

  done_when: |
    1. Собран полный game-owned inventory `.unity` scenes и их Build Settings/loading/addressable refs,
       setup/editor scripts, scene-only components, prefabs, tests, docs/spec/ADR и GUID/code refs.
    2. Каждое scene/support family имеет ровно один verdict `DELETE | KEEP | BLOCKED` с точными путями,
       прямыми ссылками, владельцем/consumer и коротким first-hand обоснованием.
    3. `DELETE` доказан отсутствием текущего consumer; `KEEP` называет действующую authority/validator;
       `BLOCKED` называет точную зависимость и один вопрос reconciliation. `MIGRATE/SHIM` не используется.
    4. Явно перечислены clauses текущих product PROGRAM/ADR/SPEC, конфликтующие с owner-approved purge
       и одной постоянной Integration Lab.
    5. Branch, HEAD и status до/после идентичны; Unity и tests не запускались; HOME сообщает команды,
       количества и точные blind spots.
    6. Возвращён six-line handoff с eligibility для owner-present purge PLAN либо одним точным blocker;
       successor CALL не создаётся executor-сессией.

  return: |
    Один self-contained audit HOME: inventory matrix, dependency evidence, DELETE/KEEP/BLOCKED boundary,
    authority conflicts, blind spots и six-line handoff. `review: n/a — read-only audit`.

  budget: <=0.5 focused day
  surface: any
  engineering_contract: 31

  END_OF_FILE: live/indie-game-development/work/c-audit-program-v2-legacy-lab-surface-001-call.md

END_OF_FILE: live/indie-game-development/history/2026-07-20-s-shape-program-v2-integration-lab-entry-001.md
