# RESULT — s-work-g-5a7c-scale-7-dispatch-001

play: work · close: light — because эта нога делает ровно три механические вещи и каждая
перемеряется первой рукой: селектор прочитан, база и пин прочитаны `git` и `validation.config`,
слот назван его словом. Ни одного суждения здесь не выносится
direction: indie-game-development · node: g-5a7c · task: t-scale-7 · call: c-exec-g-5a7c-cargo-class-seam-001
date: 2026-08-10

base_read: OS — `wt/indie-game-development` = `aa7b1259`, рабочее дерево чисто. Продукт перемерен
`git ls-remote origin`: `origin/dev` = `origin/main` = `origin/slot/win-u1` =
`918600ba355c693068035894ef86d258b46ccb0f`, дерево `84701a5d0e78fb70ddbd2215bc6910c7c3c7544b`.
Продуктовые байты, ветки, слоты и slot-state этой ногой НЕ изменялись: только чтение и read-only
селектор.

## outcome

Наряд `c-exec-g-5a7c-cargo-class-seam-001` разблокирован и выдан к отправке. Владелец назвал слот
одним словом: **«u1»**.

Наряд был написан закрытым (`blocked`) именно потому, что трогает файлы, которые `WIN-CTRL` в тот
момент публиковал. Оба условия его `unblock_when` теперь выполнены и перемерены здесь: `t-scale-6`
опубликован, WIN-U1 свободен, слот назван. `basis` и `slot` вписаны в файл наряда настоящими
значениями, `unblock_when` снят, статус — `ready`.

**Статус остаётся `ready`, а не `running`.** Расписки о запуске у Direction-ноги нет и быть не
может: наряд исполняет отдельная продуктовая сессия. Повторно как новый его не предлагать.

## evidence — перемерено первой рукой

**Слово владельца о слоте, дословно:** «u1».

**Селектор WIN-U1** (`tools/select-slot.ps1 -Slot WIN-U1`, только чтение), прогнан непосредственно
перед выдачей: `state: CLEAN`, `lifecycle: AVAILABLE`, `lease: none`, `branch: slot/win-u1`,
`head: 918600ba355c693068035894ef86d258b46ccb0f`, `mcp-endpoint: unrecorded`,
`state-authority: C:\projects\Unity\GasCoopGame_slot-state\gascoop-slot-state.v1.json`. HEAD слота
совпадает с базисом наряда знак в знак.

**База.** `git ls-remote origin` даёт одно и то же `918600ba` для `dev`, `main` и `slot/win-u1`;
дерево `84701a5d0e78fb70ddbd2215bc6910c7c3c7544b`. Это состояние уже несёт интегрированный
`t-scale-6` (`9f4eb6cf` → merge `3d24731a` → `918600ba`).

**Расхождение, названное в наряде прямо:** локальная `main` = `11f8ddbf1f11722c5bfa25e3104c3847e45d7b04`,
`main...origin/main` = `0 15` — отстала на пятнадцать коммитов и этой работой не двигается.
`origin/main` при этом догнал `origin/dev`, то есть условие улики
`i-deliver-gate-red-when-main-catches-dev-001` взведено; наряд велит назвать красный `-Deliver` на
чужой истории, а не чинить чужие отчёты.

**Пин.** `os/engineering/CONTRACT_VERSION` `current: 36` против продуктового `validation.config`
`synced_contract_version: 36`. Re-sync не нужен.

**Содержание наряда не переписывалось.** Изменены ровно два раздела — `basis` и `slot` — плюс точка
возврата в разделе отката, которая была той же строкой «вписывается при отправке». Границы, `goal`,
`done_when`, `return` и `budget` те же, что были написаны и закоммичены ногой
`s-work-g-5a7c-scale-7-call-001`.

## state_changes

1. `c-exec-g-5a7c-cargo-class-seam-001`: `status: blocked -> ready`; `unblock_when` снят; добавлены
   `slot: WIN-U1` и `basis: 918600ba355c693068035894ef86d258b46ccb0f`. `for`, `call`, `repo`,
   `engineering_contract`, `issued` и `description` не тронуты.
2. `work/c-exec-g-5a7c-cargo-class-seam-001-call.md`: заполнены `basis` и `slot`, вписана точка
   возврата. Остальной текст без изменений.
3. `t-scale-7`, `g-5a7c`, `NOW.bet` и любые другие карточки НЕ трогать.
4. Одним `osctl leg close` сохранить этот RESULT в
   `history/2026-08-10-s-work-g-5a7c-scale-7-dispatch-001.md` и добавить log ровно один раз в
   журналы `g-5a7c`, `t-scale-7` и выданного наряда.

## captures

Нет.

## decisions_needed

Нет.

## play_check

- 1 recite: done — наряд и `t-scale-7` сведены; задача последняя в активной ставке `g-5a7c`
- 2 owner inputs (owner): done — он назвал слот дословно: «u1»
- 3 do the work: done — селектор, база, дерево и пин перемерены; наряд разблокирован и заполнен
- 4 self-check: done — оба условия `unblock_when` имеют свои evidence-строки; статус `ready`, а не
  `running`, и причина названа
- 5 close: done — наряд выдан, задача остаётся открытой до его слова после прогона

## Гейты

- **G5.** `close: light`: селектор, `ls-remote`, дерево, отставание локальной `main` и его слово о
  слоте — всё перемерено или процитировано здесь. Суждений нет.
- **G3.** Аппетит не тронут: содержание наряда не переписывалось, добавлены только измеренные
  значения.
- **G9.** Карточка узла не редактировалась — только строка в её журнал.
- **Панель.** Направление панели не объявляет — регенерация пропущена.

## log

наряд на класс груза разблокирован и выдан в WIN-U1 его словом «u1»: слот CLEAN/AVAILABLE, база 918600ba совпала с головой слота, отставание локальной main на 15 коммитов названо в наряде вместе со взведённой уликой про красный Deliver

## next

`CALL c-exec-g-5a7c-cargo-class-seam-001` — отправить наряд исполнителю в продуктовый репозиторий,
слот `WIN-U1`, база `918600ba`. После HOME отдельная нога Направления читает возврат первой рукой;
`t-scale-7` закрывает его слово о том, что игра не изменилась. Это последняя задача волны: следом
`review` закрывает ставку `g-5a7c` и разбирает накопленные улики.

END_OF_FILE: live/indie-game-development/history/2026-08-10-s-work-g-5a7c-scale-7-dispatch-001.md
