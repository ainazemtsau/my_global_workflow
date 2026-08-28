CALL → session · play: work · direction: direction-os · ставка: g-one-screen · задача: t-one-screen-3

рабочая копия: `C:\wf-direction-os`, ветка `wt/direction-os`
карточка наряда: c-work-one-screen-view-001
основа данных: `96ff902b`, binding G5
`history/2026-08-24-s-work-one-screen-source-gap-g5-001.md`

goal
Собрать ещё не включённый вид сводки: один экран одного направления, где на входе
мало и просто, а четыре блока отдают глубину по требованию и ведут внутрь.

context

- Восемь авторитетных строк — `cards/t-one-screen-3.md`; резы и линзы —
  `cards/bet-g-one-screen.md`; значения слов — `knowledge/five-words-that-judge-the-summary.md`.
- HTTP-carrier уже даёт четыре блока, `how`, `gap/note` и честный source tally; его
  binding PASS — `history/2026-08-24-s-work-one-screen-source-gap-g5-001.md`.
- Текущий UI живёт в `panel/app/index.html`, `panel/app/app.js`, `panel/app/style.css`,
  markdown-renderer — `panel/app/md.js`. Прежние поля `ready/other/cards_total/cards_closed`
  остаются до задачи `t-one-screen-6`.

boundaries

- Не включать `dashboard` в `READY_SECTIONS`, не заменять старое содержимое ручки и не
  править план/список разделов — это целиком `t-one-screen-6`.
- Не заводить человеческие имена направлений и не снимать два правила про коды —
  это `t-one-screen-4`. В этом виде машинный id не показывать: до имени законна
  строка `без имени`.
- Не менять определение свежести, git/worktree tally и полосу отставания — это
  `t-one-screen-5`.
- Не добавлять библиотеки, новый источник/тип state-файла, письмо в `live/**` или
  HTTP-действие, меняющее состояние.

done_when

1. Все восемь строк `t-one-screen-3` имеют поимённую улику на точном коммите:
   четыре компактных блока и `how`; раскрытие без ухода; переходы внутрь; ноль
   кодов; ровно одна полоса 30 дней без библиотек; цвета/вид только в CSS; ноль записи.
2. Для трёх направлений показаны реальные HTTP/UI ответы, negative checks ловят
   нарушение компактности, ссылок, числа графиков, code leak, inline-style и read-only; все
   девять штатных приёмок зелёные.
3. Дифф остаётся в границах вида; `t-one-screen-4…6` не выполнены досрочно. Если хоть
   одна строка ещё требует суждения о поведении/виде, задача остаётся open и выпускает
   отдельную fresh binding G5 на exact carrier.

return

RESULT с commit/parent/diff; уликой по каждой из восьми строк; тремя HTTP/UI показами;
negative checks; девятью штатными приёмками; границами `t-one-screen-4…6`; явным
решением, закрывается ли задача light или остаётся open до fresh binding G5. Никакого
перехода к соседней реализации внутри этой ноги.

budget

Половина сфокусированного дня. Если границы требуют `t-one-screen-4…6`, STOP и узкий
чекпоинт той же задачи, а не расширение.

END_OF_FILE: live/direction-os/work/c-work-one-screen-view-001-call.md
