# Этап 1c — раздел «Сейчас» становится читаемым

## 1. GOAL

Убрать со страницы стену технического текста. Наверх — описание обычным языком
и четыре числа; всё техническое — под сворачивающимся «подробности», дословно и без потерь.

## 2. ПЕРЕПИСАТЬ ЦЕЛИКОМ (не редактировать построчно)

- `panel/serve.py` — не более 240 строк
- `panel/app/app.js` — не более 300 строк
- `panel/app/md.js` — новый файл, не более 90 строк

Всё поведение этапов 0 и 1b обязано сохраниться:
`python panel/verify.py 00` и `python panel/verify.py 01b` проверяются первыми.

`panel/app/index.html` подключает `md.js` — это ЕДИНСТВЕННОЕ, что в нём меняется,
и правку в него внесёт человек, не ты. Считай, что `md.js` уже подключён перед `app.js`.

## 3. ВХОД

То же, что на 1b: `panel/cards.py`, карточки в `panel/.cards/<direction>/`.
Про `read_card` помни: возвращает `(head, blocks)`, блок — СПИСОК СТРОК,
ошибки летят через `SystemExit`, даты ломают `json.dumps` без `default=str`.

## 4. КОНТРАКТ

### 4.1 Что добавляется в ответ ручки

`GET /api/section/<direction>/now` — та же форма, что на 1b, плюс:

у каждого наряда два новых поля:
```json
"description": "<текст поля description дословно, или null>",
"description_by": "<значение поля description_by, или null>"
```
Берутся из шапки или из блока тела карточки, как и всё остальное. Не выдумывать.

и на верхнем уровне ответа:
```json
"numbers": {
  "tasks_done": 8,
  "tasks_total": 16,
  "tracks_busy": 2,
  "tracks_limit": 4,
  "waiting_for_you": 1,
  "bet_days": 2
}
```

Как считается, буквально:
- `tasks_total` — число карточек `kind: task`; `tasks_done` — из них со `status: done`.
- `tracks_limit` — `track_wip_limit` из `NOW.md` направления (нет — `null`).
  `tracks_busy` — число РАЗНЫХ непустых `track` среди карточек `kind: call`,
  у которых `status` НЕ `done` и НЕ `paused`.
- `waiting_for_you` — число карточек `kind: decision` плюс карточек `kind: question`
  с `who: владелец`. Карточек `question` сегодня нет — это нормально, считается ноль.
- `bet_days` — целое число суток от `opened` карточки `kind: bet` до сегодняшней даты.
  Нет ставки или нет `opened` — `null`.

Направление без карточек отдаёт `numbers` со всеми нулями и `null` там, где нечего считать.

### 4.2 Что показывает страница

**Сверху раздела — строка чисел**, одним `<div class="numbers">`, внутри по одному
`<span class="num">` на число, текстом:
`задачи 8 из 16` · `полосы 2 из 4` · `ждёт тебя 1` · `ставка идёт 2 дня`.
Число `null` пропускается целиком. Разделитель между ними — точка `·` внутри того же span.

**Наряд стал таким:**

```
<div class="row">
  <div class="status">BLOCKED · сцена</div>
  <div class="title">Цель захода: выход из дома…</div>
  <div class="human">…description, отрисованный из markdown…</div>
  <div class="draft">описание составлено при разработке панели, может быть неточным</div>
  <div class="waitline">ждёт: …why…</div>
  <button class="act">скопировать запуск</button>
  <button class="act">подробности</button>
  <div class="details" hidden>…все fields дословно…</div>
  <div class="id">c-exec-…</div>
</div>
```

Правила:
- `.human` — `description`, отрисованный как markdown (см. §4.3). Нет описания —
  вместо блока `<div class="human dim">описания нет</div>`.
- `.draft` — показывается ТОЛЬКО когда `description_by` равно `dev`. Иначе блока нет.
- `.waitline` — только когда `why` не `null`. Текст: `ждёт: ` плюс `why`.
  **`unblock_when` при этом НЕ повторяется в подробностях** — оно уже здесь.
- `.details` — все `fields`, КРОМЕ `unblock_when` и `description`, каждое
  как `<div class="desc">` с именем поля и текстом, отрисованным markdown.
  Скрыт по умолчанию, кнопка «подробности» переключает атрибут `hidden`.
- Кнопка «скопировать запуск» кладёт в буфер значение `launch`.
  После клика её текст на две секунды становится `скопировано`.
- Раздел `other` — то же самое, но `status` с классом `wait`, а `title` с классом `dim`.

Новые классы `numbers num human draft waitline act details` в `style.css` УЖЕ добавлены
человеком. Своих классов не заводить, инлайн-стилей и цветов в JS не писать.

### 4.3 `panel/app/md.js` — маленький отрисовщик markdown

Экспортирует в `window` одну функцию `mdToHtml(text)`. Поддерживает ровно это
и ничего больше:

- `**жирный**` → `<strong>`
- `` `код` `` → `<code>`
- строки, начинающиеся с `- ` → элементы одного `<ul><li>`
- пустая строка разделяет абзацы `<p>`
- перевод строки внутри абзаца → `<br>`

Всё прочее выводится как текст. **Любой `<`, `>` и `&` во входном тексте
экранируется ДО разметки** — в описаниях встречаются угловые скобки,
и вставлять их как HTML нельзя. Ссылки, картинки и заголовки не поддерживаются
и не должны появляться в выводе.

### 4.4 Что не меняется

Экран выбора, шапка, меню, роутинг, неготовые разделы, `/api/state`,
маршруты `/`, `/app.js`, `/style.css`, флаги `--port` и `--no-open`,
404 на неизвестное направление. Плюс `/md.js` отдаётся так же, как `/app.js`.

## 5. ЧТО РАЗРЕШЕНО

Стандартная библиотека Python 3.13, `yaml`, `panel/cards.py`. В JS — только браузерный API,
никаких библиотек и никакого `innerHTML` от неэкранированного текста.

Не получается — падай с явной ошибкой. Не обходить, не догадываться.
НЕ писать в `live/`, `os/`, `archive/`.

## 6. САМОПРОВЕРКА

```
python panel/verify.py 00
python panel/verify.py 01b
python panel/verify.py 01c
```
Все три обязаны закончиться `ПРИНЯТО` и кодом 0.

## 7. НЕ ТРОГАТЬ

`C:\my_global_workflow_worktrees\indie-game-development\live`
`C:\my_global_workflow_worktrees\indie-game-development\os`
`C:\my_global_workflow_worktrees\indie-game-development\archive`
`C:\my_global_workflow_worktrees\indie-game-development\.git`
`panel/verify.py` · `panel/app/style.css` · `panel/app/index.html` · `panel/cards.py` · `panel/PLAN.md`

## 8. ЕСЛИ ЗАСТРЯЛ

После двух неудачных прогонов остановись и напиши `panel/tasks/step-01c-BLOCKED.md`
с описанием, что именно упало. Не меняй проверку, не меняй контракт.

END_OF_FILE: panel/tasks/step-01c.md
