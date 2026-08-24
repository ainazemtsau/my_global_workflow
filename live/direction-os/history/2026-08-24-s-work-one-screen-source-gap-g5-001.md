RESULT s-work-one-screen-source-gap-g5-001 (call: c-work-one-screen-source-gap-g5-001)
direction: direction-os   play: work   bet: g-one-screen   task: t-one-screen-2

outcome: |
  **Binding fresh-session G5: PASS.** На точном коммите `96ff902b` все пять исходных
  `done_when` задачи `t-one-screen-2` выдержали отдельную попытку опровержения. HTTP-ручка,
  физические источники и итог задачи непротиворечиво дают **0 из 4 блоков без источника**:
  честный ноль solmax объяснён, но не записан в source-gap tally; настоящий отсутствующий
  источник по-прежнему назван поимённо и с конкретной причиной.

  Задача `t-one-screen-2` закрыта как `done`. Порог смерти 2 ставки не сработал, но судьба
  ставки в этой ноге не решалась. Следующая готовая работа — отдельная реализация вида
  сводки по `t-one-screen-3`; имена, свежесть и включение остаются своим соседним задачам.

evidence: |
  **Точный carrier и границы.** Проверен `96ff902b` (`panel: честный ноль отделён от
  отсутствующего источника`), parent `5ab780d6`. `git diff --check` чист. Манифест diff:
  `A panel/focused_dashboard_source_gap.py` (`184/0`) и `M panel/serve.py` (`6/6`), других
  файлов нет. Изменение production-кода только переносит объяснение отсутствующей ставки
  из `gap` в существующий `note` и уточняет контракт этих двух полей; `panel/app/**` не
  менялся. В живом ответе сохранены прежние `ready`, `other`, `cards_total`, `cards_closed`.

  **Пять исходных done_when — PASS по каждой строке.**
  1. **PASS.** Три настоящих GET `/api/section/<direction>/dashboard` на detached
     `96ff902b` дали HTTP 200. У каждого `build.commit=96ff902b`,
     `build.commit_date=2026-08-24`, `root`, `unread=0`, `behind=141` и непустая строка
     `stale`; далее ровно четыре id в порядке `running`, `stalled`, `done_in_window`,
     `problems`.
  2. **PASS.** У всех двенадцати блоков `how` непустой и называет источник и правило:
     active/open/ready|running по живым карточкам и bet из NOW; blocked|waiting|paused;
     файлы history за включительное окно 2026-07-26…2026-08-24 по дате в имени; живые issue
     с первой фразой их текста. Независимый PowerShell-обход файлов, не вызывавший `dash_*`,
     совпал с HTTP по всем числам: direction-os `7/0/18/7`, indie-game-development
     `10/0/234/44`, solmax `0/0/0/0`.
  3. **PASS.** Отдельный temp-source вне `live/**` без `history/` вернул блок
     `done_in_window`, `count=0`, `gap="папки live/missing-source-probe/history/ нет —
     отчётов ног взяться неоткуда"`, `note=null`. Значит отсутствие источника доходит до
     ответа поимённо и с причиной.
  4. **PASS.** Рисования нет: exact diff не затрагивает `panel/app/**`; проверялась только
     наполнимость и source-gap семантика.
  5. **PASS.** Во всех трёх HTTP-ответах `blocks_without_source=[]`; прямое число задачи —
     **0 из 4**, ниже порога «двум и более». Это только замер порога, не review ставки.

  **Честный ноль solmax атакован отдельно.** В detached-дереве физически читаются
  `live/solmax/cards/` (12 файлов), `NOW.md` и `history/`; NOW не содержит `bet`. Независимый
  обход дал `running=0`, а HTTP-блок вернул `count=0`, `gap=null` и
  `note="активной ставки нет: NOW.md направления прочитан и не называет bet, поэтому ноль
  строк — честный ноль данных"`. Блок не входит в `blocks_without_source`.

  **Один финальный focused тест — точный RED и GREEN.** Байты
  `panel/focused_dashboard_source_gap.py` из `96ff902b` были запущены сначала против
  отдельного detached `4b026c0c`: exit 1 ровно на
  `AssertionError: solmax: blocks_without_source == ['running'], expected []`. На detached
  `96ff902b` та же проверка дала exit 0, `ACCEPTED dashboard source-gap semantics`, counts
  `7/0/18/7`, `10/0/234/44`, `0/0/0/0`, три пустых списка source-gap и
  `death-threshold-2: 0 of 4 blocks without source`.

  **Девять штатных приёмок повторены на exact `96ff902b`, каждая exit 0 / ПРИНЯТО:**
  `panel/test_osctl.py`; `panel/test_cards_cmd.py`; `panel/test_carrier.py`;
  `panel/test_wave2.py`; `panel/test_readers.py`; `panel/test_docs.py`;
  `panel/test_context.py`; `panel/verify.py` (шаги `00`, `01b`, `01c`);
  `node panel/test_md.cjs`.

state_changes: |
  1. Закрыть возвращённый CALL `c-work-one-screen-source-gap-g5-001` как отработавший,
     сохранив его исторический `status: ready`; в журнале назвать binding PASS, `0 из 4`,
     закрытие задачи и этот history-pointer.
  2. Закрыть `t-one-screen-2` со `status: done`. Пять исходных `done_when`, bet/NOW и другие
     задачи не переписывать; в журнале назвать exact `96ff902b`, RED→GREEN, двенадцать
     совпавших HTTP/source чисел и binding fresh-session G5 PASS.
  3. Создать ready CALL `c-work-one-screen-view-001`: `_bet: g-one-screen`, `to: session`,
     `play: work`, `for: t-one-screen-3`, `issued: 2026-08-24`,
     `call: work/c-work-one-screen-view-001-call.md`; `_pos` назначает `osctl`.
  4. Создать полный наряд `live/direction-os/work/c-work-one-screen-view-001-call.md`:
     отдельная bounded work-нога строит ещё не включённый вид по восьми строкам
     `t-one-screen-3`, не забирая имена `t-one-screen-4`, свежесть `t-one-screen-5` или
     включение/замену `t-one-screen-6`.
  5. Сохранить этот полный RESULT один раз как
     `live/direction-os/history/2026-08-24-s-work-one-screen-source-gap-g5-001.md`; той же
     транзакцией добавить `log` в журналы закрытой задачи и нового CALL. NOW, bet/node,
     knowledge, `panel/**`, остальные карточки и прочие `live/**` сохранить без изменений.

captures: []

decisions_needed: []

play_check:
  - step 1 recite: done — пять исходных done_when g-one-screen/t-one-screen-2 и шесть строк returning CALL проверены дословно.
  - step 2 owner inputs: skipped — владелец не управляет этим read-only carrier; commit, HTTP и физические источники дают все факты.
  - step 3 do the work: done — отдельная свежая физическая сессия пыталась опровергнуть exact 96ff902b; panel/** и live/** до RESULT не менялись.
  - step 4 self-check: done — все пять исходных строк PASS; шесть строк CALL закрыты exact RED→GREEN, ручным HTTP, независимым source tally, negative control, diff и девятью приёмками.
  - step 5 close: done — binding G5 закрывает t-one-screen-2 как done и регистрирует одну следующую work-ногу t-one-screen-3; это не light close и не in-session pre-pass.
  - G1-G4: done — активная ставка, appetite, kill_by и NOW не меняются; следующий CALL служит только следующей задаче той же ставки.
  - G5: PASS binding fresh-session — evidence первой руки совпадает со всеми пятью done_when; задача может стать done.
  - G7: done — судьба ставки и соседние product-решения не решались; слов владельца не изобретено.
  - G10: done — полный RESULT сформирован до writer apply; state меняется только перечисленными state_changes.

log: binding fresh-session G5 на 96ff902b дала PASS — пять строк t-one-screen-2 устояли, HTTP и независимый source tally совпали на 0 из 4 блоков без источника; задача закрыта, открыт вид сводки t-one-screen-3

next: |
  `c-work-one-screen-view-001` — одна bounded `work`-нога `t-one-screen-3`: собрать ещё не
  включённый вид сводки по восьми строкам задачи, не присваивая имена направлений, не меняя
  freshness-семантику и не включая/не заменяя раздел.

END_OF_FILE: live/direction-os/history/2026-08-24-s-work-one-screen-source-gap-g5-001.md
