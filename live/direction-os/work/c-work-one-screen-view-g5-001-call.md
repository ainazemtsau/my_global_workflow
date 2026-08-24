CALL → session · play: work · direction: direction-os · ставка: g-one-screen · задача: t-one-screen-3

рабочая копия: `C:\wf-direction-os`, ветка `wt/direction-os`
карточка наряда: c-work-one-screen-view-g5-001
carrier: `ae72e7dc`, parent `b786ac92`
checkpoint: `history/2026-08-24-s-work-one-screen-view-001.md`

goal
Для восьми строк вида сводки на exact `ae72e7dc` существует binding
fresh-session PASS/FAIL с уликой на компактность, переходы, единственную
графику, отсутствие кодов/инлайн-стилей/записи и границы соседних задач.

context

- Авторитетные строки — `cards/t-one-screen-3.md`; резы и линзы —
  `cards/bet-g-one-screen.md`; значения слов —
  `knowledge/five-words-that-judge-the-summary.md`.
- Полный checkpoint — `history/2026-08-24-s-work-one-screen-view-001.md`.
- Production вид — `panel/app/app.js` и `panel/app/style.css`; HTTP —
  `panel/serve.py`; focused проверки — `panel/focused_dashboard_view.py` и
  `panel/focused_dashboard_source_gap.py`.

boundaries

- Свежая физическая сессия, отдельная от реализации и её in-session pre-pass.
- До verdict не менять carrier и `live/**`.
- Не включать dashboard, не заводить имена, не менять freshness и не заменять
  старые поля ручки: это `t-one-screen-4…6`.
- FAIL возвращает узкую починку этой же задачи, а не исправляется внутри проверки.

done_when

1. Каждая из восьми исходных строк `t-one-screen-3` получила отдельную попытку
   опровержения на точном commit/parent/manifest и поимённый PASS либо FAIL.
2. Для трёх направлений заново воспроизведены реальные HTTP/production-DOM
   ответы, шесть negative controls и девять штатных приёмок; поведение кликов
   проверено отдельно от утверждений реализации.
3. Дифф подтверждён в границах вида: dashboard всё ещё выключен, а имена,
   freshness и замена старого содержимого ручки не выполнены досрочно.
4. Только полный PASS закрывает `t-one-screen-3`; любой FAIL оставляет её open и
   выпускает один узкий work-CALL на доказанный дефект exact carrier.

return

RESULT с binding PASS/FAIL; exact commit/parent/manifest; уликой по каждой из
восьми строк; тремя HTTP/UI ответами; negative controls; девятью приёмками;
boundary diff и state_changes закрытия либо узкой починки.

budget

Одна свежая сессия.

END_OF_FILE: live/direction-os/work/c-work-one-screen-view-g5-001-call.md
