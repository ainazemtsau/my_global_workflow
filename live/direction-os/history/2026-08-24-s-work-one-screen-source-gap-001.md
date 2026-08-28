RESULT s-work-one-screen-source-gap-001 (call: c-work-one-screen-source-gap-001)
direction: direction-os   play: work   bet: g-one-screen   task: t-one-screen-2

outcome: |
  Противоречие `gap` / честного нуля устранено кодовым коммитом `96ff902b`.
  `gap` снова означает только отсутствие источника; отсутствие активной ставки у solmax
  остаётся объяснённым честным нулём в существующем поле `note`. Поэтому сама HTTP-ручка
  теперь даёт `blocks_without_source: []` для каждого из трёх направлений, и число под
  порог смерти 2 прямо воспроизводится как **0 из 4** без отдельной трактовки.

  `t-one-screen-2` НЕ ЗАКРЫТА, вердикт о судьбе ставки не вынесен. Эта нога — исправление и
  self-check, не binding G5. Выпущен один новый CALL в отдельную свежую физическую сессию,
  которая снова пытается опровергнуть все пять исходных `done_when` задачи.

evidence: |
  **Код и дифф.** `96ff902b` (`panel: честный ноль отделён от отсутствующего источника`),
  parent `5ab780d6`. `git diff --numstat 96ff902b^..96ff902b`:
  `184 0 panel/focused_dashboard_source_gap.py`; `6 6 panel/serve.py`. Других файлов в
  коммите нет. В `serve.py` объяснение отсутствующей ставки перенесено из `gap` в уже
  существующий `note`; `dash_block` уточняет, что `note` объясняет честный ноль или рез.

  **Focused acceptance — исходный RED и итоговый GREEN одной финальной проверкой.** На
  отдельном detached-дереве `4b026c0c` команда
  `C:\wf-direction-os\.venv\Scripts\python.exe panel/focused_dashboard_source_gap.py`
  завершилась exit 1 ровно строкой:
  `FAILED dashboard source-gap semantics: solmax: blocks_without_source == ['running'], expected []`.
  На `96ff902b` та же команда завершилась exit 0:
  `ACCEPTED dashboard source-gap semantics`; `blocks_without_source` =
  `{"direction-os": [], "indie-game-development": [], "solmax": []}`;
  `death-threshold-2: 0 of 4 blocks without source`.

  **Повторный ручной HTTP-замер на `96ff902b`.** Три настоящих запроса к
  `/api/section/<direction>/dashboard` дали HTTP 200, `build.commit=96ff902b`,
  `build.commit_date=2026-08-24`, поле `stale` в шапке, ровно четыре блока и непустой `how`
  у каждого. Row-count прямо из ответов:
  - direction-os — `running=7/stalled=0/done_in_window=18/problems=7`,
    `blocks_without_source=[]`;
  - indie-game-development — `10/0/234/44`, `blocks_without_source=[]`;
  - solmax — `0/0/0/0`, `blocks_without_source=[]`.
  У каждого ответа длина `blocks_without_source` равна 0, поэтому число задачи и ручки одно:
  **0 из 4**, ниже порога «2 и более»; дальнейшая судьба ставки здесь не решалась.

  **Честный ноль отделён от настоящего source-gap.** Прямой ответ блока solmax:
  `count=0`, `gap=null`, `note="активной ставки нет: NOW.md направления прочитан и не
  называет bet, поэтому ноль строк — честный ноль данных"`. Негативный контроль focused
  acceptance временно направил читатель на отдельный temp-source без `history/` и получил:
  `{"id":"done_in_window","count":0,"gap":"папки live/missing-source-probe/history/ нет — отчётов ног взяться неоткуда"}`.
  Значит отсутствие строк в прочитанном источнике и отсутствие самого источника не смешаны.

  **Девять штатных приёмок после коммита — каждая exit 0 / ПРИНЯТО:**
  `panel/test_osctl.py`; `panel/test_cards_cmd.py`; `panel/test_carrier.py`;
  `panel/test_wave2.py`; `panel/test_readers.py`; `panel/test_docs.py`;
  `panel/test_context.py`; `panel/verify.py` (все три шага `00`, `01b`, `01c`);
  `node panel/test_md.cjs`. Focused acceptance прогнана отдельно и не превращена в десятую
  штатную: `test_docs.py` по-прежнему подтверждает ровно девять.

  **Границы.** Кодовый коммит меняет только два файла `panel/**`; `panel/app/**`, `live/**`,
  `work/converge-g-one-screen-v3.md`, имена/коды, свежесть, включение dashboard и соседние
  задачи не затронуты. `ready/other/cards_total/cards_closed` остались в ответе; все прежние
  проверки `verify.py` зелёные. Новых источников, типов state-файлов и записывающих HTTP-
  маршрутов нет. Предположений и резов сверх объявленных границ не сделано.

state_changes: |
  1. Закрыть возвращённый CALL `c-work-one-screen-source-gap-001` как отработавший, сохранив
     его исторический `status: ready`; в журнале назвать коммит `96ff902b`, согласованный
     ответ `0 из 4` и этот history-pointer.
  2. `t-one-screen-2` оставить `status: open`; исходные пять `done_when` не переписывать.
     Добавить только журнал этой ноги с кодовым коммитом, focused RED→GREEN и указателем на
     новую binding G5.
  3. Создать ready CALL `c-work-one-screen-source-gap-g5-001`: `_bet: g-one-screen`,
     `to: session`, `play: work`, `for: t-one-screen-2`, `issued: 2026-08-24`,
     `call: work/c-work-one-screen-source-gap-g5-001-call.md`; `_pos` назначает `osctl`.
  4. Создать полный наряд
     `live/direction-os/work/c-work-one-screen-source-gap-g5-001-call.md`: отдельная свежая
     физическая binding G5 проверяет коммит `96ff902b`, пять исходных строк задачи, focused
     RED→GREEN, ручной source tally и девять штатных приёмок; она ничего не чинит и не
     переходит к соседним задачам.
  5. Сохранить этот полный RESULT один раз как
     `live/direction-os/history/2026-08-24-s-work-one-screen-source-gap-001.md`; той же
     транзакцией добавить `log` в журналы `t-one-screen-2` и нового CALL. NOW, bet/node,
     knowledge, остальные карточки и все прочие `live/**` сохранить без изменений.

captures: []

decisions_needed: []

play_check:
  - step 1 recite: done — устранён только source-gap дефект активной ставки g-one-screen/t-one-screen-2; шесть done_when CALL сверены поимённо.
  - step 2 owner inputs: skipped — владелец не управляет этим read-only артефактом; код, HTTP-ответы, дисковые источники и команды дают все нужные факты.
  - step 3 do the work: done — `gap` оставлен только отсутствию источника, честный ноль объяснён существующим `note`, добавлена focused acceptance.
  - step 4 self-check: done — одна финальная acceptance дала точный RED на 4b026c0c и GREEN на 96ff902b; три HTTP-ответа, настоящий missing-source и девять штатных проверок перемерены первой рукой.
  - step 5 close: done — это checkpoint до binding G5: возвращённый CALL закрывается, задача остаётся open, выпускается одна свежая проверка той же задачи.
  - G1-G4: done — NOW, активная ставка, appetite и kill_by не меняются; продолжение служит только t-one-screen-2.
  - G5: pending binding fresh-session refutation — focused acceptance и self-check этой ноги не объявлены binding G5 и задачу не закрывают.
  - G7: done — решений владельца и вердикта о судьбе ставки не изобретено.
  - G10: done — полный RESULT выпущен до writer apply; `live/**` меняется только перечисленными state_changes.

log: source-gap t-one-screen-2 исправлен коммитом 96ff902b — честный ноль solmax больше не считается отсутствием источника, три ответа дают 0 из 4; задача остаётся open, выпущена новая свежая G5

next: |
  `c-work-one-screen-source-gap-g5-001` — отдельная свежая binding G5 той же задачи:
  попытаться опровергнуть пять исходных `done_when` на коммите `96ff902b`; только её PASS
  может закрыть `t-one-screen-2`.

END_OF_FILE: live/direction-os/history/2026-08-24-s-work-one-screen-source-gap-001.md
