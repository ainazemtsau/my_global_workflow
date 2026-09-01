RESULT s-solmax-zaratustra-health-run-050
direction: solmax
play: work
node: g-zara-health-vertical
bet: bet-g-zara-health-vertical
task: t-health-run

outcome: |
  Следующая задача активной ставки подготовлена к исполнению: восемь строк
  `t-health-run` сохранены в трёх проверяемых группах одного bounded
  engineering-CALL. Зарегистрирован ровно один готовый корневой CALL
  `c-solmax-zaratustra-health-run-050`; продуктовый репозиторий этой ногой не
  изменялся.

evidence: |
  Свежий `osctl context --direction solmax --for t-health-run` показал активную
  ставку `g-zara-health-vertical`, отсутствие owner-owed inputs и карточку
  `t-health-run` в статусе `open`, `_pos: 4`.

  `live/solmax/history/2026-09-01-s-solmax-zaratustra-health-registry-049.md`
  фиксирует закрытый predecessor на продуктовом commit
  `6e8b3fcea623d0e0247c1b2a748e34508985286e`.

  Продуктовый репозиторий `C:\projects\zaratusta-product` прочитан первыми
  руками: ветка `feat/health-contracts`, HEAD `6e8b3fc`, рабочее дерево чистое;
  `validation.config: synced_contract_version = 36`, текущий Direction
  engineering contract также `36`.

  В живых карточках нет конкурирующего CALL или pending decision. Полный новый
  пакет записывается в
  `live/solmax/work/calls/c-solmax-zaratustra-health-run-050.md`.

state_changes: |
  1. Установить существующей карточке `t-health-run` статус `active`; goal,
     done_when, placement и журнал сохранить.

  2. Создать карточку `c-solmax-zaratustra-health-run-050`, kind `call`,
     `to: executor`, `play: work`, `for: t-health-run`, `status: ready`,
     `issued: 2026-09-01`, `_bet: g-zara-health-vertical`, `_pos: 14`,
     `repo: C:\projects\zaratusta-product`, `engineering_contract: 36`,
     `call: work/calls/c-solmax-zaratustra-health-run-050.md`, description:
     «Runtime прогона, fail-closed входы и доказуемая правда о сохранении».

  3. Создать полный CALL-пакет
     `live/solmax/work/calls/c-solmax-zaratustra-health-run-050.md` из `next`
     ниже.

  4. NOW, ставку, остальные task/node/call/decision/knowledge cards сохранить
     без изменений. Продуктовый репозиторий не менять.

captures: |
  Ничего.

decisions_needed: |
  Ничего. Эта нога не определяет Health-содержание и не просит владельца
  эксплуатировать артефакт; его прогон остаётся в последней UI-задаче.

play_check: |
  1. Recite — done: задача служит активной ставке и берёт generic runtime,
     typed trace, fail-closed boundaries и правду о сохранении.
  2. Owner inputs — skipped lawfully: владелец не работает с артефактом этой
     ноги; owner-content и его будущий полезный прогон сюда не входят.
  3. Do the work — done: сформирован один current-pinned executor-CALL без
     технического HOW; восемь acceptance lines сведены без потери в три
     проверяемые группы.
  4. Self-check — done: CALL сохраняет четыре terminal outcomes, шесть write
     outcomes, receipt-only saved, deny-by-default/context isolation,
     adversarial no-handler/no-effect и запрет записи в Direction OS.
  5. Close — done: task становится active, ровно один ready CALL
     регистрируется; unrelated state и продуктовый репозиторий не меняются.

log: |
  После light-close реестра следующая задача ставки `t-health-run` активирована:
  выдан current-pinned CALL 050 на generic runtime с append-only typed trace,
  четырьмя честными terminal outcomes, fail-closed входами, deny-by-default и
  шестью исходами записи с receipt-only saved; Health-содержание, handlers,
  UI, MCP и Direction repo вырезаны, product HEAD остаётся чистым `6e8b3fc`.

next: |
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

END_OF_FILE: live/solmax/history/2026-09-01-s-solmax-zaratustra-health-run-050.md
