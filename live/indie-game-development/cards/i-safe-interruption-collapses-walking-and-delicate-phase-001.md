---
id: i-safe-interruption-collapses-walking-and-delicate-phase-001
_kind: issue
level: execution
route: work
status: open
_pos: 84
---

## issue
**«ЗАНЯТ» — ОДИН БУЛЕВ ФЛАГ НА ДВА РАЗНЫХ СМЫСЛА, И ГОРЯЩАЯ ПЛИТА ПРОИГРЫВАЕТ ГРОМКИМ РЕАКЦИЯМ.**
Перемерено чтением байтов `origin/main` = `c485b30e` этой ногой.

**МЕХАНИКА, ТРИ СТРОКИ.**

- `Core/Householder/Householder.cs:2817-2818` — стоя на занятии: `isSafeToInterrupt` берётся из фазы.
- `Core/Householder/Householder.cs:2831` — ПОКА ИДЁТ: `isSafeToInterrupt = false` на всю дорогу.
- `Core/Householder/Householder.cs:1321-1322` — политика решения: реакция пропускается тогда и только
  тогда, когда `RequiresSafeInterruption && !IsSafeToInterrupt`.

То есть «занят ходьбой» и «занят опасным делом» сведены в ОДИН флаг, и различить их нечем.

**КАТАЛОГ РЕАКЦИЙ НА ОПУБЛИКОВАННОЙ ГОЛОВЕ** (`Core/Householder/HouseholderReaction.cs`):
`daily-route` false, `suspicious-noise` **true**, `quiet-rustle` **true**, `repeated-heavy-noise`
false, `landing` false, `seen-rat` false. Профиль: `secure-hot-stove` — `safeToInterrupt: false`,
единственная непрерываемая из пяти фаз.

**СЛЕДСТВИЕ: три реакции из шести, включая ДВЕ САМЫЕ ГРОМКИЕ** (`Landing` 4 и `RepeatedHeavyNoise` 3
по `Core/Situations/WorldSituationNoise.cs`), **проходят мимо гейта фазы и срывают хозяина с горящей
плиты.** Правило его документа дословно: «Если на плите что-то горит, он не должен ПО ПЕРВОМУ ШУМУ
мгновенно бросить всё и побежать за крысами: сначала он физически обезопасит плиту». Первый шум — это
и есть посадка груза и повторный тяжёлый шум.

**ЭТО БЫЛО ВЕРНО ДО ЗРЕНИЯ. Перемерено на `4fc04b4c`** — голове, на которой владелец принял
`t-occupations-1`: `landing` и `repeated-heavy-noise` уже несли `RequiresSafeInterruption = false`.
Зрение добавило ТРЕТЬЮ такую реакцию, а не создало дыру.

**МОЯ ОШИБКА, ЗАПИСАННАЯ, А НЕ СПРЯТАННАЯ.** Закрывая `t-occupations-1`, я написала в журнал и в
сообщение коммита `f9ed5d70`: «фаза secure-hot-stove единственная из пяти помечена непрерываемой,
ТО ЕСТЬ горящую плиту он сначала обезопасит и только потом побежит». Байтовая половина верна — фаза
действительно помечена. Вывод после «то есть» НЕВЕРЕН: для двух самых громких реакций он побежит
сразу. Я вывела поведение из разметки данных, не проверив политику решения, которая эту разметку
читает.

**СТРОКА 3 `t-occupations-1` ПРИ ЭТОМ НЕ НАРУШЕНА, и это надо разделять честно.** Она требует ровно:
«реакция, требующая безопасного прерывания, ждёт конца опасной фазы; реакция, которой это не нужно,
прерывает сразу». Механизм именно такой. Не выполнено НАМЕРЕНИЕ его документа, а не буква критерия,
и поэтому задача не переоткрывается, а вопрос уходит ему решением.

**ЧТО СТОИТ РАЗДЕЛЕНИЕ.** Расщепить флаг на «занят ходьбой» и «занят деликатным» нельзя молча: тот же
флаг читают `suspicious-noise` и `quiet-rustle`, обе с `true`, и обе изменят поведение. Это отдельная
нога, а не правка попутно.
## review_when
Закрывается СЛОВОМ ВЛАДЕЛЬЦА по решению `d-sight-overrides-the-hot-stove-001`, а не ногой: чем занят
хозяин и от чего его можно оторвать — геймплей, и его выбирает только он. Если он говорит «плиту
защищаем» — улика становится содержанием отдельной ноги, которая расщепляет флаг и пересматривает
`suspicious-noise` и `quiet-rustle` вместе с ним. Если он говорит «пусть бежит» — улика закрывается
как принятое поведение, и вместе с ней снимается моя запись в журнале `t-occupations-1`.
## evidence
Перемерено этой ногой на `origin/main` = `origin/dev` = `c485b30e704b1706675dd92d15c5223b0d166b92`:
`Assets/TunnelCrew/Core/Householder/Householder.cs:1321-1322,2817-2818,2831`;
`Assets/TunnelCrew/Core/Householder/HouseholderReaction.cs` — шесть определений с их флагами;
`Assets/StreamingAssets/TunnelCrew/Householder/default.householder.json` — фаза `secure-hot-stove`
c `safeToInterrupt: false`; `Assets/TunnelCrew/Core/Situations/WorldSituationNoise.cs:186-194` —
порядок громкости. Сравнение с `4fc04b4c:Assets/TunnelCrew/Core/Householder/HouseholderReaction.cs`
показывает те же флаги у `landing` и `repeated-heavy-noise` ДО зрения.
`origin/main:docs/results/c-exec-g-5a7c-sight-1-001.md` §«Named cost, owner-visible» — исполнитель
назвал размен сам и отказался чинить его в своей ноге.
END_OF_FILE: live/indie-game-development/cards/i-safe-interruption-collapses-walking-and-delicate-phase-001.md
