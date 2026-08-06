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
slot: **UNASSIGNED** — владелец обязан назвать WIN-U2 или WIN-U3 в сообщении с запуском; агент не выбирает слот
base: `d60c2f04228bdfa161d6e122c56a2c5ccfec89f3` — перемерить при запуске, это ground, не freshness-lock

## goal

Контакт несомого груза с домом или другим игроком одним швом становится замеченным фактом хозяина;
инспектор редактора перестаёт быть источником факта.

## context

- Подписанная карточка: `live/indie-game-development/TREE.md`, g-1d84, критерий 7.
- Точная задача и принятая owner-facing полоса «внимание»: `live/indie-game-development/NOW.md`,
  t-host-7; внутренний стабильный route id `внешний-вид` сохранён до review ставки.
- Перемер на `d60c2f04`, повторённый 2026-08-06 на файлах без diff относительно базы: только три
  вызова `EmitBoardCreak`, `EmitQuietRustle`, `EmitRepeatedHeavyNoise` из
  `Assets/TunnelCrew/Editor/HouseholderRouteControllerEditor.cs` производят реакции;
  `Core/Cargo/AuthoritativeCargoRoster.cs` каждый тик кладёт `ReadContact` в `cargo.Contact`;
  у `AuthoritativeCargoRoster.GetContact` нет потребителя. Это улика для PLAN, не предписанный HOW.

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
