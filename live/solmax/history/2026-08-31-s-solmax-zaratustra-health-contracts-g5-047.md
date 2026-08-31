RESULT s-solmax-zaratustra-health-contracts-g5-047
direction: solmax
play: review
node: g-zara-health-vertical
bet: bet-g-zara-health-vertical
task: t-health-contracts
call: c-solmax-zaratustra-health-contracts-g5-047

outcome: |
  verdict: accepted

  Исправленный перевод девяти свойств `context_item` на продуктовом коммите
  `c559d72b3fffd0180bd4e6b900e38ad1841f0754` устоял. `owner`,
  `boundary_read` и `boundary_write` независимы и обязательны; конкретные
  operation/process-specific значения сохраняются без огрубления.
  `freshness` является свободным carried `LABEL` и без закрытого неполного
  словаря несёт все структурные разновидности подписанного источника.

  Граница автомата устояла в точной узкой формулировке: валидируемые записи
  `workflow`, `step`, `transition`, `effect` образуют конечный декларативный
  автомат; данные сценария не могут добавить поле-инструкцию или новое значение
  закрытого instruction enum. Произвольный текст в `LABEL`/`OPAQUE` допустим,
  но остаётся carried-текстом, а не инструкцией. `no-dynamic-python` доказывает
  только отсутствие названных механизмов динамического Python и ничего не
  заявляет о будущем runner.

  Устоявшие свойства также перевыведены: ровно 14 исходных versioned identities,
  14 entity-файлов с одним literal `CONTRACT = Contract(...)`, оба вида образцов
  у каждого, все четыре обязательных класса нарушений, нулевые domain/transport
  findings. `--deliver` и `selfcheck` зелёные, все подсадки восстановлены.

  По дословному условию владельца в CALL:
  «При `accepted`: закрыть `t-health-contracts` и открыть законный следующий
  work-CALL для `t-health-registry`». Задача контрактов закрывается; существующая
  задача реестра становится active и получает один готовый engineering-CALL.

evidence: |
  ПРОДУКТОВЫЙ СНИМОК

  Репозиторий `C:\projects\zaratusta-product`, ветка
  `feat/health-contracts`, проверенный HEAD
  `c559d72b3fffd0180bd4e6b900e38ad1841f0754`, родитель
  `5b46bd3b007932fe4a12ea6040b5823df5add4c8`.

  До проверки и после всех запусков:
  `git status --short --branch` вывел только
  `## feat/health-contracts`;
  `git diff --exit-code` и `git diff --cached --exit-code` завершились
  с кодом 0.

  ПОСТРОЧНАЯ СВЕРКА ДЕВЯТИ СВОЙСТВ

  | подписанное свойство | место в `context_item` | фактическая форма | verdict |
  |---|---|---|---|
  | `id` | `id` | обязательный `IDENT`; note фиксирует неизменность при смене значения | Устояло как форма устойчивой идентичности; межвременная неизменность сама по себе этим одиночным record-validator не доказывается. |
  | `владелец` | `owner` | обязательный enum `owner|system|observation` | Устояло; отдельно от read/write. |
  | `тип` | `kind` | обязательный enum `fact|version|rule|observation|policy` | Устояло. |
  | `происхождение` | `origin` | обязательный carried `LABEL` | Устояло без толкования свободного текста. |
  | `версия/наблюдение` | `version` | обязательный carried `LABEL` | Устояло: несёт версию или момент наблюдения; источник не требовал машинно различать разновидности. |
  | `чувствительность` | `sensitivity` | обязательный enum `ordinary|bodily|opaque` | Устояло для всех трёх подписанных значений. |
  | `актуальность` | `freshness` | обязательный carried `LABEL`, `choices=()` | Устояло; закрытого словаря нет, семь структурных атак приняты. |
  | `применения` | `uses` | обязательный повторяемый carried `LABEL` | Устояло; непустая свободная форма сохраняется и не толкуется. |
  | `граница` | `boundary_read`, `boundary_write` | два независимых обязательных carried `LABEL` | Устояло; reader и writer оба сохранены, `owner` ни один не подменяет. |

  `context_class` проверен отдельно сверх девяти: обязательный enum
  `owner_shared|area_scoped|opaque`. Четвёртый класс дал
  `unknown_enum_value@context_class`.

  ФАКТИЧЕСКИЙ ВЫВОД СОБСТВЕННЫХ ADVERSARIAL RECORDS

      IDENTITIES
      count=14
      area-v1
      capability-v1
      operation-v1
      workflow-v1
      step-v1
      run-v1
      transition-v1
      effect-v1
      artifact-v1
      owner-projection-v1
      trace-event-v1
      context-item-v1
      context-ref-v1
      permission-v1
      valid_world_findings=0
      samples=area:1/2,capability:1/2,operation:1/2,workflow:1/2,step:1/3,run:1/2,transition:1/2,effect:1/2,artifact:1/2,owner_projection:1/2,trace_event:1/2,context_item:1/3,context_ref:1/2,permission:1/2
      rejected_violation_classes=broken_ref,effect_out_of_bounds,empty_required,malformed_ident,malformed_instant,missing_required,unexpected_field,unknown_enum_value,wrong_type
      CONTEXT
      fields=id,context_class,owner,kind,origin,version,sensitivity,freshness,uses,boundary_read,boundary_write
      context_class=enum:owner_shared,area_scoped,opaque
      freshness=kind:label,required:True,choices:0,carried:True
      boundary_read=kind:label,required:True,choices:0,carried:True
      boundary_write=kind:label,required:True,choices:0,carried:True
      missing-owner: missing_required@owner
      missing-boundary_read: missing_required@boundary_read
      missing-boundary_write: missing_required@boundary_write
      independent-owner-read-write: ACCEPTED
      fourth-context-class: unknown_enum_value@context_class
      freshness-interval: ACCEPTED
      freshness-phase: ACCEPTED
      freshness-days: ACCEPTED
      freshness-years: ACCEPTED
      freshness-revocation: ACCEPTED
      freshness-version: ACCEPTED
      freshness-next-event: ACCEPTED
      AUTOMATON
      unknown-opcode: unexpected_field@opcode
      new-executor: unknown_enum_value@executor
      new-outcome: unknown_enum_value@on
      new-effect-kind: unknown_enum_value@kind; effect_out_of_bounds@kind
      user-condition: unexpected_field@condition
      user-expression: unexpected_field@expression
      user-action: unexpected_field@action
      execution-mechanism: unexpected_field@execution_mechanism
      instruction-shaped-opaque-text: ACCEPTED
      answer_note=kind:opaque,carried:True

  Последняя принятая строка не является дырой: `answer_note` имеет
  `FieldKind.OPAQUE`, входит в `CARRIED_ONLY`, и текущая валидация его содержание
  не читает. Сделать такой текст исполняемым потребовало бы нового Python-кода;
  поведение будущего runner этой задачей не заявляется.

  СТРУКТУРНЫЙ АУДИТ ОФИЦИАЛЬНЫМИ ФУНКЦИЯМИ ГЕЙТА

      entity_files=14
      src/vocabulary/area.py: contract_calls=1, named_CONTRACT=True
      src/vocabulary/artifact.py: contract_calls=1, named_CONTRACT=True
      src/vocabulary/capability.py: contract_calls=1, named_CONTRACT=True
      src/vocabulary/context_item.py: contract_calls=1, named_CONTRACT=True
      src/vocabulary/context_ref.py: contract_calls=1, named_CONTRACT=True
      src/vocabulary/effect.py: contract_calls=1, named_CONTRACT=True
      src/vocabulary/operation.py: contract_calls=1, named_CONTRACT=True
      src/vocabulary/owner_projection.py: contract_calls=1, named_CONTRACT=True
      src/vocabulary/permission.py: contract_calls=1, named_CONTRACT=True
      src/vocabulary/run.py: contract_calls=1, named_CONTRACT=True
      src/vocabulary/step.py: contract_calls=1, named_CONTRACT=True
      src/vocabulary/trace_event.py: contract_calls=1, named_CONTRACT=True
      src/vocabulary/transition.py: contract_calls=1, named_CONTRACT=True
      src/vocabulary/workflow.py: contract_calls=1, named_CONTRACT=True
      one_per_file_findings=0
      negative_control_findings=0
      domain_free_findings=0
      transport_free_findings=0
      no_dynamic_python_findings=0

  Четыре обязательных класса присутствуют среди реально отвергаемых образцов:
  `missing_required`, `unknown_enum_value`, `broken_ref`,
  `effect_out_of_bounds`.

  ТОЧНАЯ ПРОВЕРЕННАЯ ФОРМУЛИРОВКА ГРАНИЦЫ

  На границе валидируемых контрактных записей `workflow`, `step`,
  `transition`, `effect` задают конечный декларативный автомат, а не
  расширяемый язык процедур. Валидные данные могут только составлять записи
  из объявленных полей и закрытых значений executor, answer shape,
  missing-input response, transition outcome и effect kind. Неизвестные
  opcode/condition/expression/action/execution mechanism и новые значения
  instruction enums отвергаются. Свободные `LABEL`/`OPAQUE` остаются carried
  данными без instruction semantics. Изменить набор инструкций можно только
  ревьюируемым изменением Python-кода. Это не доказательство поведения
  будущего registry/runner — они явно вне этой ноги.

  `vocabulary/no-dynamic-python` заявляет только узкий факт: в tracked Python
  под `src/` AST-гейт не нашёл bare calls `eval`, `exec`, `compile`,
  `__import__` и imports `importlib`, `runpy`. Он не заявляет отсутствие
  конечного интерпретатора на обычном Python control flow.

  ОБЯЗАТЕЛЬНАЯ КОМАНДА 1 — ПОЛНЫЙ ДОСЛОВНЫЙ ВЫВОД

      $ uv run --locked python tools/check.py --deliver
      zaratusta check | contract 36 | python 3.13.7
      --- static (config, hygiene, deliver): ok
      --- format
      35 files already formatted
      --- lint
      All checks passed!
      --- boundary

      ╔══╗─────────▶╔╗ ╔╗      ╔╗◀───┐
      ╚╣╠╝◀─────┐  ╔╝╚╗║║────▶╔╝╚╗   │
       ║║   ╔══╦══╦╩╗╔╝║║  ╔╦═╩╗╔╝╔═╦══╗
       ║║╔══╣╔╗║╔╗║╔╣║ ║║ ╔╬╣╔╗║║ ║│║╔═╝
      ╔╣╠╣║║║╚╝║╚╝║║║╚╗║╚═╝║║║║║╚╗║═╣║
      ╚══╩╩╩╣╔═╩══╩╝╚═╝╚═══╩╩╝╚╩═╩╩═╩╝
        └──▶║║                    ▲
            ╚╝────────────────────┘


      ---------
      Contracts
      ---------

      Analyzed 29 files, 67 dependencies.
      -----------------------------------

      Layers: runtime over vocabulary over foundation, never upwards KEPT
      foundation is independent of every other module KEPT
      vocabulary is a dictionary: it knows nothing of the layer above it KEPT

      Contracts: 3 kept, 0 broken.
      --- types
      Success: no issues found in 32 source files
      --- tests
      ........................................................................ [ 43%]
      ........................................................................ [ 87%]
      ....................                                                     [100%]
      164 passed in 0.15s

      GREEN: static, format, lint, boundary, types, tests

  Код возврата 0.

  ОБЯЗАТЕЛЬНАЯ КОМАНДА 2 — ПОЛНЫЙ ДОСЛОВНЫЙ ВЫВОД

      $ uv run --locked python tools/selfcheck.py
      ok   test-layout red
      ok   test-layout green
      ok   orphan-tests red
      ok   orphan-tests green
      ok   skipped-test red
      ok   skipped-test green
      ok   empty-test red
      ok   empty-test green
      ok   scratch red
      ok   scratch keeper red
      ok   scratch green
      ok   shell-script red
      ok   backslash red
      ok   drive-path red
      ok   config-backslash red
      ok   allow-hatch green
      ok   launch-lines green
      ok   launch-drift red
      ok   launch-missing red
      ok   launch-no-readme red
      ok   config missing red
      ok   config key missing red
      ok   config green
      ok   report missing red
      ok   report field red
      ok   cited-artifact red
      ok   report green
      ok   domain-word red
      ok   domain-stem red
      ok   domain green
      ok   transport-word red
      ok   transport-stem red
      ok   transport green
      ok   transport outside src green
      ok   eval red
      ok   importlib red
      ok   re.compile green
      ok   one-per-file green
      ok   two-in-a-file red
      ok   empty-entity-file red
      ok   unnamed-contract red
      ok   entity-in-machinery red
      ok   negative-controls green
      ok   no-rejected-sample red
      ok   no-conforming-sample red
      ok   uncovered-violation red
      ok   boundary green
      ok   boundary red (runtime)
      ok   boundary red (vocabulary)
      ok   boundary cleanup
      ok   conformance green
      ok   conformance red
      ok   conformance cleanup
      ok   context-translation green
      ok   boundary-write red
      ok   boundary-write red cleanup
      ok   freshness-windows red
      ok   freshness-windows red cleanup
      ok   automaton-instructions green
      ok   unknown-opcode red
      ok   unknown-opcode red cleanup
      ok   undeclared-condition red
      ok   undeclared-condition red cleanup
      ok   undeclared-action red
      ok   undeclared-action red cleanup

      SELFCHECK GREEN: 65 controls, every gate provably fails on a seeded miss

  Код возврата 0.

  После команд и собственного аудита оба репозитория снова чисты:
  продукт — `## feat/health-contracts`;
  Direction — `## wt/solmax...origin/wt/solmax [ahead 12]`;
  worktree/index diff в обоих случаях пусты.

  В продуктовой сессии не создано ни одного коммита и не выполнялся `git push`.
  Product HEAD остался `c559d72b3fffd0180bd4e6b900e38ad1841f0754`.

state_changes: |
  1. Закрыть returning call
     `c-solmax-zaratustra-health-contracts-g5-047` со статусом `done`.

  2. Закрыть `t-health-contracts` со статусом `done`. Основание — verdict
     `accepted` выше и дословное условное распоряжение владельца в CALL:
     «При `accepted`: закрыть `t-health-contracts` и открыть законный следующий
     work-CALL для `t-health-registry`».

  3. Установить существующей карточке `t-health-registry` статус `active`;
     её goal/done_when и остальное содержание сохранить без изменений.

  4. Создать карточку `c-solmax-zaratustra-health-registry-048`,
     kind `call`, `to: executor`, `play: work`, `for: t-health-registry`,
     `status: ready`, `issued: 2026-08-31`,
     `_bet: g-zara-health-vertical`, `_pos: 13`,
     `kind: engineering`,
     `repo: C:\projects\zaratusta-product`,
     `engineering_contract: 36`,
     `call: work/calls/c-solmax-zaratustra-health-registry-048.md`,
     description: «Реестр обработчиков и двусторонняя build-проверка
     объявленных мест вызова».

  5. Создать полный пакет
     `live/solmax/work/calls/c-solmax-zaratustra-health-registry-048.md`
     из `RESULT.next` ниже.

  6. NOW, bet, узлы, остальные задачи, решения, вопросы и knowledge сохранить
     без изменений. Задача реестра уже существовала в подписанной ставке;
     новая задача или lane не создаётся.

captures: |
  Ничего. Принятый инертный instruction-shaped `OPAQUE` не является новой
  работой: это ожидаемая carried-only граница, а runner явно вне задачи.

decisions_needed: |
  Ничего. Владелец заранее и дословно задал ветку состояния при `accepted`;
  reviewer verdict — `accepted`.

play_check: |
  1. Verify by refutation — done: девять строк перевыведены из подписанного
     источника и атакованы собственными records; freshness и каждая instruction
     boundary атакованы отдельно; verdict `accepted`.
  2. Harvest per lens — done:
     - Extensibility: закрытая instruction surface допускает новые композиции
       без новых opcodes.
     - Real depth: эта словарная задача не доказывает глубину будущего runner.
     - Agent-buildability: единая команда, semantic tests и 65 seeded controls
       воспроизводимы.
     - Daily use/dogfood: изменений нет; живой прогон остаётся дальнейшей задачей.
     - Privacy/trust/safety: owner/read/write больше не смешаны; свободный
       freshness не теряет подписанные окна.
     - Cost discipline: зависимостей, внешних расходов и новой поверхности нет.
  3. Tree diff (owner) — done по дословному условию текущего CALL:
     «При `accepted`: закрыть `t-health-contracts` и открыть законный следующий
     work-CALL для `t-health-registry`». Других tree-изменений нет.
  4. Add-back check — done: registry, call sites, runner и Health-content не
     возвращались в проверенную задачу; следующий registry-task уже был отдельной
     строкой подписанной ставки.
  5. Knowledge — skipped: нового durable fact с отдельным `read_by` нет;
     доказательство принадлежит history/task journal.
  6. Forecast & next — done: числовой forecast по-прежнему `no_basis`;
     открывается только существующая следующая задача `t-health-registry`,
     current engineering contract/stamp = 36.
  7. Close — done: returning call и задача закрываются, registry-task становится
     active, один current-pinned engineering CALL регистрируется.

log: |
  binding G5 приняла исправленный `context_item` и закрытую границу конечного
  автомата на c559d72: все девять строк, семь видов freshness и независимые
  owner/read/write устояли; unknown opcode, новые executor/outcome/effect-kind,
  condition/expression/action и execution mechanism отвергнуты; точная граница
  ограничена валидируемыми records, carried-текст остаётся инертным, а
  no-dynamic-python заявляет только узкий AST-факт; 14 identities и entity-файлов,
  оба вида samples, четыре обязательных violations и domain/transport-free
  перевыведены; --deliver дал 164 passed, selfcheck — 65 controls, оба дерева
  чисты, product commit/push не создавались; t-health-contracts закрыта,
  t-health-registry активирована и получила current-pinned CALL 048

next: |
  CALL c-solmax-zaratustra-health-registry-048
  to: executor
  direction: solmax
  play: work
  node: g-zara-health-vertical
  bet: bet-g-zara-health-vertical
  task: t-health-registry
  status: ready
  kind: engineering
  repo: C:\projects\zaratusta-product
  engineering_contract: 36

  goal: |
    Создать явный реестр обработчиков и сделать объявленные места вызова
    двусторонним build-инвариантом: у каждого зарегистрированного обработчика
    есть объявленное место вызова, и каждый вызываемый шагом обработчик
    зарегистрирован.

  context: |
    АБСОЛЮТНЫЕ ПУТИ. Искать исходную задачу не надо.

    ПРОДУКТОВЫЙ РЕПОЗИТОРИЙ — вся работа здесь:
    `C:\projects\zaratusta-product`.
    Ветка `feat/health-contracts`, базовый HEAD
    `c559d72b3fffd0180bd4e6b900e38ad1841f0754`.
    Перед работой прочитать корневой `AGENTS.md` и
    `src/vocabulary/AGENTS.md`; они определяют HOW и штатные команды.
    Репозиторий синхронизирован с engineering contract 36 и работает в
    default `PROBA`, пока владелец явно не скажет перейти в OPORA.

    РЕПОЗИТОРИЙ НАПРАВЛЕНИЯ — только читать:
    `C:\my_global_workflow_worktrees\solmax`.

    Источники:
    - `live/solmax/cards/t-health-registry.md` — точные строки задачи;
    - `live/solmax/history/2026-08-31-s-solmax-zaratustra-health-contracts-g5-047.md`
      — принятый predecessor и граница, которую нельзя размыть;
    - продуктовые `docs/adr/0003-the-fourteen-contracts.md`,
      `src/vocabulary/`, `tools/check.py`, `tools/selfcheck.py`,
      `validation.config`.

    Уже истинно на базе: четырнадцать versioned contracts, закрытая
    декларативная automaton boundary, единая команда `tools/check.py`,
    selfcheck и ноль предметного Health-словаря в общем `src/`.

  boundaries: |
    - Это отдельная задача реестра и двусторонней проверки call sites.
      Не строить runner, сценарий, Health-content, UI, MCP или domain module.
    - Не угадывать обработчики поиском по именам, импортам, именованию файлов
      или динамическим discovery. Handler и его call sites объявляются данными
      реестра, а нарушение роняет штатную проверку.
    - Сохранить принятые 14 identities, lossless `context_item` и закрытую
      instruction surface. Не превращать carried `LABEL`/`OPAQUE` в команды.
    - Проверка встраивается в существующую одну команду; отдельной второй
      команды не создавать. Каждый новый/изменённый gate получает seeded miss
      в `tools/selfcheck.py` и восстанавливает байты.
    - В общем коде реестра и проверки не должно появиться Health, питания или
      тренировок; использовать официальный domain-free gate.
    - Инструмент недоступен — СТОП и вопрос владельцу, без обходного пути.
    - Коммит локальный. `git push` не выполнять: пушит владелец.
    - Если задача требует третьего дробления или расширения за указанные
      границы, СТОП и вопрос владельцу.

  done_when: |
    1. Явный реестр существует: каждый handler — типизированная запись с
       объявленными call sites; ни поиск по имени, ни dynamic discovery не
       участвуют. Принятые contracts/automaton boundaries и domain-free общий
       слой сохранены.
    2. Та же `uv run --locked python tools/check.py` реально падает в обе
       стороны: (a) зарегистрированный handler имеет ноль объявленных call
       sites; (b) step ссылается на handler, которого нет в реестре. Чистое
       дерево проходит.
    3. `tools/selfcheck.py` содержит отдельные автоматически восстанавливаемые
       seeded misses для обеих сторон; `--deliver` и весь selfcheck зелёные на
       локальном коммите, а RESULT фиксирует точный commit/parent, вывод
       красных подсадок, полные штатные проверки, чистое дерево и отсутствие
       push.

  return: |
    Один RESULT плея `work`, HOME в Direction OS. В evidence:
    - точный local commit и parent;
    - manifest изменённых файлов;
    - примеры registry record и обеих незаконных конфигураций;
    - фактический вывод обеих focused red-подсадок и их cleanup;
    - полный дословный вывод `tools/check.py --deliver` и `tools/selfcheck.py`;
    - нулевые findings официальных domain/transport gates;
    - чистое дерево и подтверждение, что push не выполнялся.

    Не выдавать следующий Direction-CALL из продукта. Если каждая строка
    done_when перевыведена первыми руками из committed bytes и command output,
    вернуть доказательства для light-close; любой остаток суждения явно назвать
    для свежего G5.

  budget: |
    Одна сосредоточенная сессия, не больше полудня. Задача уже отделена от
    контрактов; третьего дробления без слова владельца нет.

END_OF_FILE: live/solmax/history/2026-08-31-s-solmax-zaratustra-health-contracts-g5-047.md
