# CALL — c-exec-g-1d84-world-noise-contact-001

to: executor
kind: engineering
repo: ainazemtsau/GasCoopGame
engineering_contract: 36
stage: PLAN
direction: indie-game-development
node: g-1d84
task: t-host-7
track: внешний-вид
issued: 2026-08-06 by s-shape-g-1d84-core-recut-001
status: blocked
slot: **UNASSIGNED** — владелец обязан назвать WIN-U2 или WIN-U4 в сообщении с запуском; агент не выбирает слот
base: `8ffe5a5d89398b1dd7bcf450157446f7952f3855` — перебита 2026-08-06 с `d60c2f04` по `s-work-g-1d84-house-as-data-close-001`; это ground, не freshness-lock, перемерить при запуске

## goal

Контакт несомого груза с домом или другим игроком одним швом становится замеченным фактом хозяина;
инспектор редактора перестаёт быть источником факта.

## context

- Подписанная карточка: `live/indie-game-development/TREE.md`, g-1d84, критерий 7.
- Точная задача и принятая owner-facing полоса «внимание»: `live/indie-game-development/NOW.md`,
  t-host-7; внутренний стабильный route id `внешний-вид` сохранён до review ставки.
- Перемер на `d60c2f04`: только три вызова `EmitBoardCreak`, `EmitQuietRustle`,
  `EmitRepeatedHeavyNoise` из `Assets/TunnelCrew/Editor/HouseholderRouteControllerEditor.cs` производят
  реакции; `Core/Cargo/AuthoritativeCargoRoster.cs` каждый тик кладёт `ReadContact` в `cargo.Contact`;
  у `AuthoritativeCargoRoster.GetContact` нет потребителя. Это улика для PLAN, не предписанный HOW.
- **Улика ПЕРЕПРОВЕРЕНА 2026-08-06 на новой базе и держится буквально, потому что оба файла не
  менялись вовсе:** `HouseholderRouteControllerEditor.cs` = блоб `832c6aa8` и
  `AuthoritativeCargoRoster.cs` = блоб `9711121b` — на `8ffe5a5d` те же самые, что на `d60c2f04`.
  Доставка `t-house-4` их не касалась (26 файлов, из них два изменения: заготовка дома и настройки
  облака). То есть перемерять эти два пути заново незачем — но selector, аренду и HEAD слота перемерить
  всё равно обязательно.
- **Слоты на момент правки:** `WIN-U2` (HEAD `d60c2f04`, предок `main`, 9 позади, чисто) и `WIN-U4`
  (HEAD `0fd8ea96`, предок `main`, 2 позади, чисто) — оба чистый fast-forward. `WIN-U3` НЕ предлагается:
  разошёлся на 3 коммита вперёд `main`. `WIN-U1` занят арендой профилей хозяина.

## boundaries

- Не строить обстановку, отдельную механику удара по игроку, бой, поимку или проверку понятности шума игроку.
- Не переписывать хозяина и не трогать текущие корни данных дома или текстового профиля.
- Не выбирать слот и не запускаться без его точного имени в сообщении владельца.

## done_when

1. Контакт груза о дом и контакт того же груза о другого игрока проходят одним названным швом «контакт производит шум» в замеченный факт хозяина; отдельной механики удара по игроку нет.
2. Кнопки инспектора не нужны для возникновения факта; хозяин идёт смотреть, а увидев игрока реагирует на него.
3. Проверка различает отсутствие контакта, контакт с домом и контакт с игроком.

## return

Терминальный HOME по pinned v36: product RESULT, commits/manifest, проверки и честная диспозиция всех
трёх строк done_when. Продуктовый handback сам задачу Direction не закрывает.

## budget

Один engineering root; feature-нога — не больше сосредоточенного полудня. Это соединение двух
существующих концов; если PLAN требует новую систему внимания или второй сетевой канал, STOP и HOME.

END_OF_FILE: live/indie-game-development/work/c-exec-g-1d84-world-noise-contact-001-call.md
