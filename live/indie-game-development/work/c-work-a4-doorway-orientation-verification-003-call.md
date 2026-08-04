# CALL — c-work-a4-doorway-orientation-verification-003

to: session
direction: indie-game-development
track: переноска
play: work
node: g-6b13
task: a-4
issued: 2026-08-04 by s-work-g-6b13-a4-close-verification-checkpoint-002
status: waiting
waiting_on: "Владелец фактически наблюдал и назвал обе ориентации на published стенде: поперёк балка не проходит/упирается или разворачивается, вдоль проходит; либо прямо сказал, что этого не проверял."

## goal

У exact published стенда `839df47e` честно установлено последнее owner-eye различие a-4: балка
поперёк не проходит через проём, упирается/разворачивается, а вдоль проходит; без этого факта a-4
остаётся open.

## context

- Binding fresh-session refutation уже выполнена и сохранена в
  `live/indie-game-development/history/2026-08-04-s-work-g-6b13-a4-close-verification-checkpoint-002.md`.
- Exact published `origin/main` = `origin/dev` =
  `839df47e78127fe2ebfba5eabb307bf6bdd61e9b`; проверенные runtime-блобы: settings
  `f750868c2b8d423ef678b6aedc09f31c808aa952`, scene
  `4c7b224b98b0e98dff508a65eaec4fc9d721c05c`.
- Код/history/report/checks выдержали refutation. Владелец явными словами подтвердил после тюнинга
  отсутствие замеченной проблемы у второго игрока и упор мыши в стену. Про балку он назвал
  столкновение как физического объекта, но не различил две ориентации.
- Известное low-FPS ограничение и замещение Unity MCP запуском владельца уже записаны и не скрываются.

## boundaries

- Никакой записи в продуктовый репозиторий, повторной интеграции или нового инженерного теста.
- Не выводить различие ориентаций из кода, report-текста, столкновения вообще или общего «закрывать».
- Не менять a-4b, первое лицо, вертикальность груза, полосу хозяина, low-FPS ограничение или
  опубликованные продуктовые байты.
- Не открывать новых проверок сверх этого единственного остатка исходного `done_when`.

## done_when

1. Есть явные слова владельца, что он действительно видел обе стороны различия: поперёк балка не
   прошла/упёрлась или развернулась, а вдоль прошла. Если этого не наблюдалось, checkpoint называет
   только этот пробел и сохраняет a-4 open.
2. Только при этих словах прежняя exact refutation получает PASS: a-4 закрывается, этот waiting CALL
   снимается и выпускается ready same-lane engineering CALL на a-4b с уже записанными границами.

## return

Полный RESULT по play `work`: PASS либо точный checkpoint; evidence содержит фактические слова
владельца, state_changes ограничены a-4, этим CALL и законным same-lane handoff.

budget: one brief owner-present continuation after the observation exists

END_OF_FILE: live/indie-game-development/work/c-work-a4-doorway-orientation-verification-003-call.md
