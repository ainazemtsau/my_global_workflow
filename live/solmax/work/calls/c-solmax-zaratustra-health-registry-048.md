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

END_OF_FILE: live/solmax/work/calls/c-solmax-zaratustra-health-registry-048.md
