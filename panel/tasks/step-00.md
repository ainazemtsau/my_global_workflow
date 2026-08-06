# Этап 0 — каркас панели

## 1. GOAL

Локальный сервер и одностраничное приложение: экран выбора направления, страница направления
с меню из семи разделов, шапка состояния сборки. Данных состояния ещё нет — раздел «Сейчас»
открывается пустым, остальные шесть приглушены и не кликаются.

## 2. СОЗДАТЬ (только новые файлы, ничего не править)

- `panel/serve.py` — не более 140 строк
- `panel/app/index.html` — не более 40 строк
- `panel/app/app.js` — не более 160 строк
- `panel/start.cmd` — не более 10 строк

`panel/app/style.css` и `panel/verify.py` УЖЕ СУЩЕСТВУЮТ и написаны не тобой.
Не открывай их на запись, не меняй ни байта, не создавай своих стилей.

## 3. ВХОД

Только стандартная библиотека Python 3.13 и `git`. Никаких зависимостей, никакого npm,
никакого фреймворка.

## 4. КОНТРАКТ

`panel/serve.py` принимает `--port <N>` (по умолчанию 8787) и `--no-open`
(не открывать браузер). Без `--no-open` открывает браузер на `http://127.0.0.1:<port>/`.

Отдаёт:
- `GET /` → `panel/app/index.html`
- `GET /app.js`, `GET /style.css` → файлы из `panel/app/` с правильным Content-Type
- `GET /api/state` → JSON строго такой формы:

```json
{
  "build": {
    "commit": "f619b8d4",
    "commit_date": "2026-08-06",
    "unpushed": 7,
    "unread": 0
  },
  "directions": [
    {
      "id": "indie-game-development",
      "sections": [
        {"id": "now",       "label": "СЕЙЧАС",      "ready": true},
        {"id": "waiting",   "label": "ЖДЁТ ТЕБЯ",   "ready": false},
        {"id": "wave",      "label": "ВОЛНА",       "ready": false},
        {"id": "goals",     "label": "ЦЕЛИ",        "ready": false},
        {"id": "history",   "label": "ИСТОРИЯ",     "ready": false},
        {"id": "knowledge", "label": "ЗНАНИЯ",      "ready": false},
        {"id": "direction", "label": "НАПРАВЛЕНИЕ", "ready": false}
      ]
    },
    { "id": "solmax", "sections": [ ...тот же список... ] }
  ]
}
```

Как считается `build`:
- `commit` = вывод `git rev-parse --short HEAD`
- `commit_date` = `git log -1 --format=%ad --date=short`
- `unpushed` = целое из `git rev-list --count origin/main..HEAD`; если команда не прошла — `0`
- `unread` = `0` (разбора состояния на этом этапе нет)

Направления = имена папок первого уровня в `live/`, отсортированные по алфавиту.
Список разделов одинаков для всех направлений и задан в `serve.py` одной константой.

`panel/app/app.js` — приложение с адресами без перезагрузки страницы:
- `#/` — экран выбора: по строке на направление, каждая ведёт на `#/<id>/now`
- `#/<direction>/<section>` — страница направления
- переключение раздела и направления НЕ перезагружает страницу
- раздел с `"ready": false` не кликается и имеет класс `off`
- пустой раздел рисует `<div class="empty">РАЗДЕЛ ПУСТ</div>`
- неготовый раздел — `<div class="empty">РАЗДЕЛ ЕЩЁ НЕ СДЕЛАН</div>`

Разметка использует ТОЛЬКО классы из `style.css`: `topbar brand dirs build warn bad shell
nav count active off content row status wait title dim desc id empty problem`.
Своих классов не изобретать, инлайн-стилей не писать, цвета в JS не задавать.

Шапка: слева `PANEL` классом `brand`, затем ссылки направлений в `.dirs`; справа `.build`
с текстом `<commit> · не отправлено <N> · не прочиталось <M>`, где число «не отправлено»
обёрнуто в `<span class="warn">`, а «не прочиталось» — в `<span class="bad">`.
Если число ноль — обёртку в цвет не ставить.

`panel/start.cmd` — двойным кликом из корня репозитория запускает
`python panel/serve.py` и оставляет окно открытым.

## 5. ЧТО РАЗРЕШЕНО

Только `http.server`, `socketserver`, `json`, `subprocess`, `os`, `argparse`, `webbrowser`,
`threading` из стандартной библиотеки. Больше ничего.

Если что-то не получается — верни ошибку явным текстом и остановись.
НЕ пиши обходной путь, НЕ добавляй зависимость, НЕ трогай `style.css` и `verify.py`.
Любое из этого — проваленная задача.

## 6. САМОПРОВЕРКА

```
python panel/verify.py 00
```

Должно закончиться словом `ПРИНЯТО` и кодом возврата 0. Проверка сама поднимает сервер
и опрашивает его; она же следит, что `style.css` не перекрашен.

## 7. НЕ ТРОГАТЬ

`C:\my_global_workflow_worktrees\indie-game-development\live`
`C:\my_global_workflow_worktrees\indie-game-development\os`
`C:\my_global_workflow_worktrees\indie-game-development\archive`
`C:\my_global_workflow_worktrees\indie-game-development\.git`
`panel/app/style.css`
`panel/verify.py`
`panel/PLAN.md`

## 8. ЕСЛИ ЗАСТРЯЛ

После двух неудачных прогонов `verify.py` остановись и напиши
`panel/tasks/step-00-BLOCKED.md` с описанием, что именно упало.
Не пробуй другой подход, не переписывай проверку, не меняй контракт.

END_OF_FILE: panel/tasks/step-00.md
