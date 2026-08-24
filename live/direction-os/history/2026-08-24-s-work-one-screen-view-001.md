RESULT s-work-one-screen-view-001 (call: c-work-one-screen-view-001)
direction: direction-os   play: work   node/task: g-one-screen/t-one-screen-3

outcome: |
  Ещё выключенный вид сводки собран на точном carrier `ae72e7dc` поверх
  `b786ac92`: один read-only экран одного направления показывает четыре стороны,
  держит на входе не больше пяти строк блока, раскрывает глубину на месте и даёт
  переходы внутрь. Ровно одна графическая форма — 30-дневная полоса активности;
  библиотек, инлайн-стилей и записывающих действий не добавлено.

  Задача `t-one-screen-3` НЕ закрывается этой ногой. Внешний вид и поведение требуют
  суждения, которое та же сессия не может превратить в light close. Выпускается
  отдельная fresh binding G5 на exact `ae72e7dc`; соседние `t-one-screen-4…6`
  сохранены своими задачами, а `dashboard` остаётся выключен.

evidence: |
  **Carrier.** Commit `ae72e7dc023b6ad14c4dfe1fa4f66bb3b655b1a5`, parent
  `b786ac922de2b12ccc7f44dd49038348ba53cde9`. Манифест ровно пяти файлов:
  `M panel/app/app.js` (`143/15`), `M panel/app/style.css` (`95/0`),
  `A panel/focused_dashboard_view.cjs` (`144/0`),
  `A panel/focused_dashboard_view.py` (`165/0`), `M panel/serve.py` (`25/8`).
  `git diff b786ac92 ae72e7dc --check` — exit 0.

  **Восемь строк задачи — поимённая улика, без close-вердикта.**
  1. `panel/focused_dashboard_view.py` исполняет production `renderDashboard` над
     реальными HTTP-ответами: у всех трёх направлений ровно четыре блока; у каждого
     видимы одно число и серверный `view_how`; максимум входных строк — 5.
  2. Тот же focused-check вызывает настоящий обработчик каждой кнопки: глубина
     сначала скрыта, после клика видна, hash не меняется. В in-app Browser на
     реальном `direction-os` раскрытие подтвердилось отдельно.
  3. Production DOM дал переходы цели в `#/direction-os/goals/g-one-screen`,
     отчёта ноги — в `#/direction-os/history`; браузер пришёл на страницу цели
     «Сводка каждого направления» и в ИСТОРИЮ с 21 строкой. У семи записей проблем
     клик открыл их собственный текст на месте. Focused DOM насчитал ссылки/записи:
     direction-os `26/7`, indie-game-development `244/44`, solmax `0/0`.
  4. В содержимом сводки машинные id не печатаются: focused-check ищет direction,
     block, row и commit ids и в компактном, и в раскрытом тексте; браузер на
     реальном экране дал `visibleCodes=0`. Общая верхняя навигация не менялась:
     имена направлений и два общих правила про коды остаются `t-one-screen-4`;
     внутри сводки до той задачи показано `без имени`.
  5. У каждого реального ответа ровно один `.dash-activity` и 30 `.dash-day`;
     границы окна приходят из того же серверного расчёта, который отобрал отчёты.
     SVG/canvas/chart-библиотек и dependency-файлов в manifest нет.
  6. Все новые правила вида находятся в `panel/app/style.css`; app.js создаёт только
     классы. `panel/test_readers.py` — ПРИНЯТО; отдельный поиск цвета/inline-style в
     JS не нашёл совпадений. Цвет употреблён только как сигнал идёт/стоит/проблема/
     активный день, что записано рядом с CSS-правилами.
  7. Focused DOM не содержит form/input/select/textarea; все HTTP-запросы — GET,
     обработчики только раскрывают локальный текст или меняют hash. Negative control
     с POST ловится как `read-only`; все штатные проверки повторно подтвердили, что
     `live/` не изменился за прогоны.
  8. Четыре стороны представлены одновременно, но вход остаётся мал: заголовок,
     число+способ счёта, максимум пять строк и `подробнее`. Browser 1280×720 показал
     четыре блока, одну полосу, `maxPreviewRows=5`; первый экран носит `без имени`.

  **Три настоящих HTTP/UI показа.** Focused carrier и production renderer совпали:
  direction-os `идёт/стоит/сделано/проблемы = 6/0/20/7`,
  indie-game-development `10/0/234/44`, solmax `0/0/0/0`. У каждого UI — четыре
  блока, одна полоса на 30 ячеек; source-gap по-прежнему пуст у всех трёх.

  **Negative controls.** Тот же проверяющий код намеренно портил по одному свойству
  и каждый раз падал именно на нём: compactness, links, chart-count, code-leak,
  inline-style, read-only — все шесть `true`.

  **Девять штатных приёмок на exact `ae72e7dc`.** Exit 0 / ПРИНЯТО:
  `panel/test_osctl.py`; `panel/test_cards_cmd.py`; `panel/test_carrier.py`;
  `panel/test_wave2.py`; `panel/test_readers.py`; `panel/test_docs.py`;
  `panel/test_context.py`; `panel/verify.py` (шаги `00`, `01b`, `01c`);
  `node panel/test_md.cjs`. Дополнительно зелёны
  `panel/focused_dashboard_source_gap.py` и `panel/focused_dashboard_view.py`.

  **Границы.** `READY_SECTIONS` и `panel/PLAN.md` не менялись; verify `00` по-прежнему
  перечисляет готовыми только прежние восемь разделов. Старые поля ручки
  `ready/other/cards_total/cards_closed`, freshness/build/worktree tally и stale-bar
  не заменены. Человеческие имена не заведены, сводка не включена, другой тип
  state-файла и библиотека не появились. In-session code-review pre-pass не оставил
  critical/important findings; это не binding G5 и не выдаётся за него.

state_changes: |
  1. Закрыть возвращённый CALL `c-work-one-screen-view-001` как отработавший,
     сохранив его исторический `status: ready`; причина и history-pointer — строка
     `log` этой ноги.
  2. Оставить `t-one-screen-3` со `status: open`; done_when не переписывать. Добавить
     этой задаче строку `log`: carrier собран, но close ждёт fresh binding G5.
  3. Создать ready CALL `c-work-one-screen-view-g5-001`: `_bet: g-one-screen`,
     `to: session`, `play: work`, `for: t-one-screen-3`, `issued: 2026-08-24`,
     `call: work/c-work-one-screen-view-g5-001-call.md`; `_pos` назначает `osctl`.
  4. Создать полный наряд
     `live/direction-os/work/c-work-one-screen-view-g5-001-call.md`: отдельная свежая
     сессия пытается опровергнуть восемь строк задачи на exact `ae72e7dc`, ничего не
     исправляет внутри проверки и не забирает `t-one-screen-4…6`.
  5. Сохранить этот полный RESULT один раз как
     `live/direction-os/history/2026-08-24-s-work-one-screen-view-001.md`; одной
     транзакцией добавить `log` в журналы возвращённого CALL, `t-one-screen-3` и
     нового G5 CALL. NOW, bet/node, knowledge, другие задачи/CALL и прочие `live/**`
     сохранить без изменений.

captures: []

decisions_needed: []

play_check:
  - step 1 recite: done — восемь done_when t-one-screen-3, границы ставки и returning CALL перечитаны дословно.
  - step 2 owner inputs: skipped — все продуктовые значения уже подписаны в карточке задачи и каноне; новых слов владельца экран не требует.
  - step 3 do the work: done — exact ae72e7dc собирает ещё выключенный read-only вид и два focused-check на реальном HTTP/production DOM.
  - step 4 self-check: done — восемь строк сопоставлены поимённо; три HTTP/UI ответа, шесть negative controls, browser clicks, diff и девять штатных приёмок зелёные.
  - step 5 close: done checkpoint — задача остаётся open и returning CALL заменяется отдельной fresh binding G5 на тот же exact carrier.
  - G1-G4: done — NOW, активная ставка, appetite и kill_by не меняются; successor служит той же задаче.
  - G5: pending binding fresh-session — in-session browser/code-review являются только pre-pass; look/behavior не закрываются light.
  - G7: done — соседние продуктовые решения не принимались, слова владельца не изобретены.
  - G10: done — полный RESULT сформирован до writer apply; меняется только объявленный checkpoint state.

log: ещё выключенный вид сводки собран на ae72e7dc — четыре блока, максимум пять строк, одна 30-дневная полоса и переходы прошли HTTP/UI negative checks и девять приёмок; задача остаётся open до fresh binding G5

next: |
  CALL c-work-one-screen-view-g5-001
  to: session
  direction: direction-os
  play: work
  node: g-one-screen   task: t-one-screen-3
  goal: |
    Для восьми строк вида сводки на exact `ae72e7dc` существует binding
    fresh-session PASS/FAIL с уликой на компактность, переходы, единственную
    графику, отсутствие кодов/инлайн-стилей/записи и границы соседних задач.
  context: |
    `live/direction-os/cards/t-one-screen-3.md`;
    `live/direction-os/history/2026-08-24-s-work-one-screen-view-001.md`;
    carrier `ae72e7dc`, parent `b786ac92`; production вид — `panel/app/app.js` и
    `panel/app/style.css`; HTTP — `panel/serve.py`; focused проверки —
    `panel/focused_dashboard_view.py` и `panel/focused_dashboard_source_gap.py`.
  boundaries: |
    Свежая физическая сессия, отдельная от реализации и её in-session pre-pass.
    До verdict не менять carrier и `live/**`. Не включать dashboard, не заводить
    имена, не менять freshness и не заменять старые поля ручки: это t-one-screen-4…6.
    FAIL возвращает узкую починку этой же задачи, а не исправляется внутри проверки.
  done_when: |
    1. Каждая из восьми исходных строк t-one-screen-3 получила отдельную попытку
       опровержения на точном commit/parent/manifest и поимённый PASS либо FAIL.
    2. Для трёх направлений заново воспроизведены реальные HTTP/production-DOM
       ответы, шесть negative controls и девять штатных приёмок; поведение кликов
       проверено отдельно от утверждений реализации.
    3. Дифф подтверждён в границах вида: dashboard всё ещё выключен, а имена,
       freshness и замена старого содержимого ручки не выполнены досрочно.
    4. Только полный PASS закрывает t-one-screen-3; любой FAIL оставляет её open и
       выпускает один узкий work-CALL на доказанный дефект exact carrier.
  return: |
    RESULT с binding PASS/FAIL; exact commit/parent/manifest; уликой по каждой из
    восьми строк; тремя HTTP/UI ответами; negative controls; девятью приёмками;
    boundary diff и state_changes закрытия либо узкой починки.
  budget: one fresh session

END_OF_FILE: live/direction-os/history/2026-08-24-s-work-one-screen-view-001.md
