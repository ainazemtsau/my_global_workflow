CALL c-solmax-zaratustra-health-contracts-g5-047
to: session
direction: solmax
play: review
node: g-zara-health-vertical
bet: bet-g-zara-health-vertical
task: t-health-contracts
status: ready

goal: |
  В новой отдельной физической сессии попытаться опровергнуть исправленный
  перевод девяти свойств `context_item` и доказательство закрытой границы
  конечного декларативного автомата на продуктовом коммите
  `c559d72b3fffd0180bd4e6b900e38ad1841f0754`.

context: |
  АБСОЛЮТНЫЕ ПУТИ. Искать ничего не надо.

  ПРОДУКТОВЫЙ РЕПОЗИТОРИЙ — только читать и запускать объявленные проверки:
  `C:\projects\zaratusta-product`.
  Ветка `feat/health-contracts`, проверяемый коммит
  `c559d72b3fffd0180bd4e6b900e38ad1841f0754`, родитель
  `5b46bd3b007932fe4a12ea6040b5823df5add4c8`.
  Перед проверкой прочитать корневой `AGENTS.md` и
  `src/vocabulary/AGENTS.md`. Не редактировать, не коммитить, не пушить.

  РЕПОЗИТОРИЙ НАПРАВЛЕНИЯ — только читать:
  `C:\my_global_workflow_worktrees\solmax`.

  Источники:
  - `live/solmax/work/health-context-model-v1.md`;
  - `live/solmax/cards/t-health-contracts.md`;
  - `live/solmax/history/2026-08-30-s-solmax-zaratustra-health-contracts-g5-045.md`;
  - продуктовые `RESULT.md`,
    `docs/adr/0003-the-fourteen-contracts.md`,
    `src/vocabulary/context_item.py`, `_spec.py`, `_validate.py`,
    `workflow.py`, `step.py`, `transition.py`, `effect.py`,
    `tests/vocabulary/test_context_translation.py`,
    `tests/vocabulary/test_automaton_boundary.py`,
    `tools/check.py`, `tools/selfcheck.py`.

  Утверждённая владельцем граница:
  конечный декларативный автомат допустим; расширяемый язык процедур,
  пользовательские условия/выражения и новые инструкции из данных запрещены.
  Его дословный ответ: «согласен с твоей рекомендацией».

  Нога 046 сообщает:
  - `boundary_read` и `boundary_write` стали независимыми carried `LABEL`;
  - `freshness` стал свободным carried `LABEL`;
  - отдельные тесты фиксируют девять отображений и закрытые инструкции;
  - selfcheck имеет подсадки boundary-write, freshness-windows,
    unknown-opcode, undeclared-condition и undeclared-action;
  - лексический гейт переименован в `no-dynamic-python`.

boundaries: |
  - Это binding G5: сессия физически отдельна от автора 046.
  - Оба репозитория только читать; объявленные проверки и их автоматически
    восстанавливаемые подсадки запускать можно.
  - Не расширять проверку до registry, declared call sites, runner,
    предметного Health-содержимого или будущих задач.
  - Не принимать RESULT 046 на веру: перевывести свойства из подписанного
    источника и атаковать каждую границу собственными adversarial records.
  - Не доказывать поведение поиском исходного текста. Лексический поиск может
    оценивать только узкий запрет динамического Python.
  - Инструмент недоступен — СТОП и вопрос владельцу, без обходного пути.
  - Никаких изменений, коммитов или push.

done_when: |
  1. Девять свойств подписанного источника сверены построчно с
     `context_item`; отдельно атакованы независимость owner/read/write,
     обязательность writer и сохранение operation/process-specific формы.
     `context_class` проверен как отдельный дискриминатор сверх девяти.
  2. `freshness` атакован всеми уже подписанными структурными разновидностями:
     конкретным интервалом, фазой, днями, годами, до отмены/версии и до
     следующего события. Проверено, что форма несёт их без закрытого
     неполного словаря и без предметного содержимого в общем коде.
  3. Граница автомата атакована неизвестным opcode, новым executor/outcome/
     effect-kind, пользовательскими condition/expression/action и попыткой
     расширить способ исполнения из данных. Отдельно установлено, что
     `no-dynamic-python` заявляет только узкий доказанный факт.
  4. Перевыведены устоявшие свойства: 14 versioned identities, один literal
     contract на entity-файл, оба вида образцов, четыре обязательных класса
     нарушений, transport/domain-free. `--deliver` и `selfcheck` зелёные,
     оба дерева после проверки чистые. Дан единый verdict
     `accepted|partial|rejected`.

return: |
  Один RESULT плея `review`.

  В evidence:
  - точный commit и parent;
  - построчная таблица девяти свойств с verdict каждой строки;
  - все adversarial records и фактические findings;
  - полный дословный вывод `--deliver` и `selfcheck`;
  - точная проверенная формулировка границы автомата;
  - подтверждение чистых деревьев, отсутствия коммита и push.

  При `accepted`: закрыть `t-health-contracts` и открыть законный следующий
  work-CALL для `t-health-registry`.
  При `partial|rejected`: оставить задачу active и открыть узкую переработку
  только по опровергнутым строкам.

budget: |
  Одна свежая сосредоточенная read-only сессия. Это попытка опровержения, а
  не повтор реализации и не обзор по впечатлению.

END_OF_FILE: live/solmax/work/calls/c-solmax-zaratustra-health-contracts-g5-047.md
