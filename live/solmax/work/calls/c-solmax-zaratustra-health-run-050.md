CALL c-solmax-zaratustra-health-run-050
to: executor
direction: solmax
play: work
node: g-zara-health-vertical
bet: bet-g-zara-health-vertical
task: t-health-run
status: ready
kind: engineering
repo: C:\projects\zaratusta-product
engineering_contract: 36

goal: |
  Создать generic runtime прогона, который исполняет только объявленный граф,
  ведёт типизированный append-only след, останавливается до обработчика и
  эффекта при недостоверном обязательном входе и сообщает только доказуемую
  правду о завершении и сохранении.

context: |
  АБСОЛЮТНЫЕ ПУТИ. Продуктовая работа выполняется только в
  `C:\projects\zaratusta-product`, ветка `feat/health-contracts`, базовый HEAD
  `6e8b3fcea623d0e0247c1b2a748e34508985286e`. Перед PLAN прочитать корневой
  `AGENTS.md`, `src/runtime/AGENTS.md` и `src/vocabulary/AGENTS.md`; они
  определяют технический HOW и штатные команды. Репозиторий синхронизирован
  с engineering contract 36 и остаётся в repository-default PROBA, пока
  владелец явно не сменит режим.

  Репозиторий Direction OS `C:\my_global_workflow_worktrees\solmax` — только
  читать. Источники результата:
  - `live/solmax/cards/t-health-run.md` — точные восемь строк приёмки;
  - `live/solmax/history/2026-09-01-s-solmax-zaratustra-health-registry-049.md`
    — принятый predecessor и границы реестра;
  - продуктовые `docs/adr/0003-the-fourteen-contracts.md`,
    `docs/adr/0004-explicit-handler-registry.md`, `src/vocabulary/`,
    `src/runtime/handler_registry.py`, `tools/check.py`,
    `tools/selfcheck.py`, `validation.config`.

  Уже истинно: четырнадцать versioned contracts, lossless `context_item`,
  закрытая instruction surface, явный handler registry и двусторонний
  call-site invariant. Их нельзя размывать этой задачей.

boundaries: |
  - Это generic runtime и доказательства его границ. Не создавать Health,
    питание, тренировки, capability/operation content, сценарий «Свод дня»,
    предметные handlers, UI, HTTP, MCP или model executor.
  - Не менять принятые четырнадцать identities, lossless context mapping,
    закрытый набор инструкций и двусторонний registry invariant. Если
    публичный frozen contract действительно должен измениться — STOP и
    вернуть точную несовместимость, не переписывать его внутри этой ноги.
  - Не вводить dynamic discovery, разбор прозы, общий язык процессов,
    планировщик, очередь, background worker, базу данных или вторую команду
    проверки. Использовать существующую одну `tools/check.py`.
  - Направление полностью вне области эффектов. Ни runtime, ни model, ни
    writer не могут писать `C:\my_global_workflow_worktrees\solmax` или
    самоправить активные area/workflow/handler/policy definitions по следу.
  - Новые или изменённые gates получают реальные seeded misses в
    `tools/selfcheck.py`, восстанавливающие исходные bytes. Враждебные случаи
    доказывают, что handler и effect не запускались.
  - Недоступный обязательный инструмент — STOP и вопрос владельцу, без
    обходного пути. Коммит локальный; `git push` не выполнять.

done_when: |
  1. Runtime шагает только по объявленному графу и пишет append-only typed
     trace: stable event id, step, time, kind и origin. Любой путь завершения
     фиксирует ровно один из четырёх исходов — success, bounded owner question,
     diagnostic stop или recoverable failure; тест доказывает отсутствие
     выхода без terminal event.
  2. Missing, ambiguous, stale или unpermitted обязательный input останавливает
     шаг до handler и effect. Permissions deny-by-default, операция видит
     только объявленные refs, owner fact не протекает в посторонний run; hostile
     cases покрывают каждую границу и наблюдаемо подтверждают ноль handler/effect.
  3. Write truth различает applied, rejected, stale basis, known-not-done,
     partial и unknown; partial/unknown блокируют blind retry. `saved` возникает
     только по наблюдённой typed receipt: без неё состояние не меняется и
     поверхность сообщает not-saved/pending. Direction repo и активные
     definitions физически вне writable effect scope; чистое дерево проходит
     ту же одну `tools/check.py` и полный selfcheck.

return: |
  Один RESULT плея `work`, HOME в Direction OS. В evidence указать:
  - точный local commit и parent, Git manifest;
  - committed примеры trace event, четырёх terminal outcomes и шести write
    outcomes;
  - фактические focused RED для выхода без terminal event, каждой группы
    fail-closed входов, context leak, handler/effect execution и ложного saved,
    плюс byte-for-byte cleanup;
  - полный `tools/check.py --deliver` и `tools/selfcheck.py`, official
    domain/transport findings, чистое дерево и отсутствие push;
  - попунктовую сверку трёх done_when. Если всё перевыведено из committed
    bytes/ids и command output, дать короткий `close: light — because ...`;
    любой остаток behavioral/quality judgment явно отправить в свежий G5.

  Следующий Direction-CALL из продукта не выдавать.

budget: |
  Одна сосредоточенная сессия, не больше полудня. При невозможности удержать
  все три группы в одном cohesive runtime slice — STOP с точной границей и
  оценкой, без молчаливого расширения или изменения задачи.

END_OF_FILE: live/solmax/work/calls/c-solmax-zaratustra-health-run-050.md
