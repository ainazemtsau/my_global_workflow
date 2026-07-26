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
