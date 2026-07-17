# Track-mode: как владельцу управлять треками

updated: 2026-07-17 by s-work-characters-resume-a1
readers: владелец направления и любая Direction-OS session, которая меняет lifecycle трека.

## Текущий снимок

* WIP-лимит: **6**; occupancy: **5/6**.
* Занимают слот: `core`, `level`, `canon`, `visual`, `characters`.
* Не занимают слот: `marketing`, `damage` и `dotnet-gates`, потому что их root CALL сейчас `paused`.
* Primary: `core` — там живёт текущая ставка NearGas L1B.
* Default: `core / NearGas L1B surface-freeze` — это только ответ на «продолжаем»; ready Characters идёт параллельно и default не меняет.

## Четыре статуса CALL

| Статус | Что значит | Занимает WIP |
|---|---|---:|
| `ready` | CALL можно запускать | да |
| `waiting` | root ждёт child/event из `waiting_on` | да |
| `blocked` | есть явный внешний `unblock_when`; это не ручная пауза | да |
| `paused` | владелец явно остановил работу; есть `paused_by` receipt | нет |

WIP считает **трек**, а не количество CALL. Child не добавляет второй слот. Pending owner decision занимает слот даже
при paused root, поэтому одной паузы CALL недостаточно, чтобы освободить трек с нерешённым decision.

## Что можно говорить обычными словами

ID помнить не нужно. Достаточно человеческого названия и намерения:

* «Поставь marketing на паузу. Default не меняй».
* «Возобнови characters».
* «Поставь marketing на паузу и возобнови characters; default оставь extraction».
* «Добавь параллельный трек Audio Polish, но WIP оставь 6 — освободи для него marketing».
* «Подними WIP-лимит с 6 до 7 и добавь Audio Polish».
* «Убери visual из текущих треков совсем» — здесь система уточнит: временная пауза или retirement.

Явная фраза вроде «поставь X на паузу» уже является owner verdict. Неясное «выключи X» требует одного выбора:
`pause` (временно) или `retire` (убрать из current frontier).

## Pause: временно остановить

Pause сохраняет трек, CALL, зависимости и всю историю; меняется только dispatch-состояние. TREE-узел остаётся
`parallel`. Все текущие CALL трека получают `paused` и один receipt с точными словами владельца. Default меняется
только если он указывал на остановленный CALL и где-то остаётся другой `ready` CALL.

Пример из выполненного 17.07 swap — поставить marketing на паузу:

| | До | После |
|---|---|---|
| marketing root | `ready` | `paused` + `paused_by` |
| occupancy | `6/6` | `5/6` |
| default core/NearGas | `ready`, выбран | без изменения |

Важно: pausing `core` сейчас само по себе не освободит слот — там остаётся pending min-spec decision.

## Resume: возобновить

Resume не означает автоматически `ready`: система заново выводит состояние из сохранённых зависимостей и свежих
свидетельств. Для `characters` переход выполнен 2026-07-17 так:

| CALL | На паузе | После resume |
|---|---|---|
| body-rig root | `paused` | `waiting` на repair-002 + binding G5 |
| reaction repair child | `paused` | `ready` после full-packet refresh под product-owned protocol v2 |

Characters снова занял один WIP-слот. В том же атомарном RESULT владелец поставил на паузу marketing и damage,
поэтому occupancy перешёл `6/6 → 5/6` без промежуточного превышения.

## Swap при полном лимите — выполненный вариант

Владелец выбрал вариант A и дополнительно поставил damage на паузу; default оставлен core/NearGas.

| Трек | До | После |
|---|---|---|
| marketing | root `ready`, WIP 1 | root `paused`, WIP 0 |
| characters | root+child `paused`, WIP 0 | root `waiting`, child `ready`, WIP 1 |
| damage | root `blocked`, WIP 1 | root `paused`, WIP 0 |
| occupancy | `6/6` | `5/6` |
| default | core/NearGas | core/NearGas |

Это атомарный lifecycle RESULT: сначала считается весь before/after, поэтому промежуточного превышения `7/6` нет.

Если позже поставить на паузу трек, на который указывает current default, default обязан переехать на другой ready CALL.

## Добавить новый трек

Новый current track требует одновременно:

1. уникальные короткий id и человеческое название;
2. `primary` или `parallel` — primary всегда ровно один;
3. approved scope с проверяемым `done_when`;
4. один self-contained root CALL либо pending decision;
5. явные слова владельца об открытии трека;
6. свободный WIP-слот или явно одобренное изменение лимита.

Если scope уже является TREE-узлом, добавление идёт через `map`: владелец подтверждает карточку, TREE меняется
`parked → parallel` по G9, затем появляется track + root CALL. Если это bounded local process без TREE-узла,
достаточен `work`: TREE не раздувается, но scope/done_when и root CALL всё равно обязательны. Новый primary — не
«ещё один трек»: это handoff текущей ставки через `review`, потому что второй active bet запрещён.

При `6/6` есть два честных варианта:

* **Swap (рекомендуется):** pause/retire один занятый трек, добавить новый; лимит остаётся 6.
* **Raise:** владелец явно говорит «поднять WIP до 7»; затем новый root занимает седьмой слот. Это не выводится из
  желания добавить трек автоматически.

## «Выключить» навсегда: retirement

Retirement — не pause. Он проходит через `review`: каждый открытый CALL получает явную disposition, root не удаляется
как будто его не было, receipt остаётся в history, track исчезает из current NOW, а TREE-backed узел с отдельным G9
вердиктом становится `parked` или `dropped`. Ни `blocked`, ни merge/push, ни устная фраза «кажется, закончили» не
являются доказательством close.

## Что система показывает перед записью

Для lifecycle-изменения owner brief должен показать: затронутые треки и CALL, before/after статусы, occupancy до и
после, судьбу default, изменение WIP-лимита и любой TREE diff. При неоднозначности он останавливается за одним
коротким verdict; при уже точной команде владельца применяет именно её, не расширяя полномочия.

END_OF_FILE: live/indie-game-development/work/track-mode-owner-operations-guide.md
