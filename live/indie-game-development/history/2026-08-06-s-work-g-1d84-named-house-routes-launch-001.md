# RESULT — s-work-g-1d84-named-house-routes-launch-001

direction: indie-game-development
track: дом
play: work
node/task: g-1d84/t-host-2
date: 2026-08-06
base_read: Direction `2797d197`; product `main = origin/main = origin/dev = d647a58b`; selector —
`WIN-U1..WIN-U4 AVAILABLE`, `lease: none`.

## outcome

Выпущен один новый инженерный корень на единственную ещё не построенную содержательную часть
срезанной волны: хозяин ходит между названными местами через названные проходы дома и после реакции
возвращается к прежнему намерению по свежему пути. Корень pinned на engineering contract v36,
содержит три строки `done_when` и ждёт фактического запуска владельцем в `WIN-U2`.

Продуктовые ноги точки доставки (`WIN-U2`, product `d647a58b`) и шума (`WIN-U4`, уже в ancestry
`main`) не перезапускались: их RESULT существуют и должны быть приняты отдельными Direction work-
ногами. Вырезанные карточкой второй профиль, пять реакций, proof-only способность и погоня/поиск не
получили ни наряда, ни запуска.

## evidence

- `C:\projects\Unity\GasCoopGame`: `main = origin/main = origin/dev = d647a58b`; три новых коммита
  после `15ee4151` доставляют `c-exec-g-1d84-delivery-point-001`.
- `d647a58b:docs/results/c-exec-g-1d84-delivery-point-001.md` — статус `DELIVERED on dev`, кандидат
  `6b1622fc`, интеграция `29e8505d`, четыре строки результата и слова владельца о видимом успехе.
- `d647a58b:docs/results/c-exec-g-1d84-world-noise-contact-001.md` — статус `DELIVERED on dev`,
  опубликованный шум от контакта груза с домом и точное удаление контакта с игроком по слову владельца.
- Selector `gascoop-slot-state.v1.json`: все четыре слота `AVAILABLE`, lease `none`. Физическая сверка:
  `WIN-U2 = d647a58b` и чист; `WIN-U1` и `WIN-U4` чисты и являются предками main; `WIN-U3` имеет
  divergence `main...HEAD = 25/3`, поэтому не рекомендован.
- `NOW.md/t-host-2`: задача разблокирована закрытием данных дома; названные места совпадают с
  нынешними точками распорядка, а текущий дефект — прямые отрезки сквозь перегородки.
- Product contract stamp и OS current совпадают: v36.

## state_changes

1. Создать полный `work/c-exec-g-1d84-named-house-routes-001-call.md`: новый root, track `дом`,
   task `t-host-2`, contract v36, stage PLAN, три business-level `done_when`, base `d647a58b` как ground.
2. `NOW.md`: upsert `open_calls/c-exec-g-1d84-named-house-routes-001` со статусом `blocked`, указателем
   на CALL и условием запуска точным сообщением владельца с `WIN-U2`; обновить только header `updated`.
3. `LOG.md`: добавить одну строку; `history/`: сохранить этот полный RESULT.

Не менять: статусы задач, существующие open_calls, TREE/CHARTER, lanes/WIP, decisions/issues/forecast,
продуктовый репозиторий. Особенно не присваивать Direction-закрытие `t-house-6` или `t-host-7`.

## captures

- Post-cut hot state всё ещё требует отдельного `repair`: убрать из dispatch-фронтира снятые карточкой
  `t-host-4`, `t-host-5`, `t-host-6`, `t-host-8` и свести формулировку уже доставленного `t-host-7`.

## decisions_needed

Нет. Слот остаётся blocked до фактического owner launch message; рекомендация — WIN-U2.

## play_check

- **1 recite** — done: цель и три строки `t-host-2` сверены с активной bet и срезанной карточкой.
- **2 owner inputs (owner)** — done: владелец попросил «какие вообще остались» и «сразу дай сообщение,
  в каких слотах их запустить»; новых gameplay-ответов для уже подписанной задачи не требовалось.
- **3 do the work** — done: self-contained engineering CALL выпущен; технический HOW оставлен PLAN.
- **4 self-check** — done: contract v36 совпадает, `done_when` ровно три, track существует, свободный
  root в полосе `дом` есть, WIP после регистрации — три корня из четырёх.
- **5 close** — done: CALL зарегистрирован blocked до owner launch; другие lanes/calls сохранены.
- **G2/G3/G7** — pass: только задача активной ставки, без расширения appetite и без нового gameplay.
- **G10** — pass: TREE не меняется; CALL/RESULT полные; owner launch не выдуман и status не `running`.

## log

g-1d84/t-host-2: после фактического завершения продуктовых ног точки доставки и шума выпущен
единственный новый продуктовый корень — маршруты хозяина по названным местам и проходам; рекомендован
WIN-U2 на свежем main `d647a58b`. Два готовых product RESULT остаются отдельными HOME-закрытиями;
устаревший объём после среза здесь не запускался.

## next

return-to-owner. Владелец запускает `c-exec-g-1d84-named-house-routes-001` в `WIN-U2`; параллельно
два отдельных свежих Direction-чата принимают product RESULT `t-house-6` и `t-host-7`. `WIN-U4`
остаётся свободным до финальной exe-задачи после закрытия маршрутов и двух вернувшихся результатов.

END_OF_FILE: live/indie-game-development/history/2026-08-06-s-work-g-1d84-named-house-routes-launch-001.md
