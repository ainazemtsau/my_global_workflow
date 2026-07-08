# Mechanics Workbench — Review Guide v0

Status: owner review guide, не canon.

## 1. Что читать первым

Не читать весь пакет подряд.

Начать здесь:

1. `core-proof-skeleton-v0.1.md`
2. Раздел 2: минимальная promise.
3. Раздел 3: one-room-to-exit loop.
4. Раздел 7: blockers B1-B8.

Остальное — справочник.

## 2. Как ревьюить

На каждый кусок лучше отвечать одним из четырех типов:

- **ок как skeleton** — можно временно использовать как предмет обсуждения;
- **непонятно** — слово/действие не представляется;
- **не согласен** — идея неверная или тянет не туда;
- **потом** — идея хорошая, но не текущий blocker.

Не надо сразу решать финальную механику.

## 3. Первый реальный вопрос

Первый вопрос, который я бы поставил на обсуждение:

> Что значит "газ есть здесь" в первом proof?

Без этого нельзя честно обсуждать bubble transfer.

Возможные ответы не надо выбирать прямо сейчас, но их надо разложить:

- gas layer along floor/ceiling;
- diffuse room volume;
- visible low pool;
- moving source/flow;
- hidden concentration with traces;
- local bounded volume;
- mixture of source + layer.

После этого второй вопрос:

> Что игроки читают, чтобы понять это без wiki and without unfair invisibility?

И только потом:

> Каким действием часть газа переходит в bubble?

## 4. Где лежит `ЛЁГКИЕ`

`ЛЁГКИЕ` не потеряны.

Они лежат в `idea-ledger-v0.md` как parked meta и ждут:

1. floor proof;
2. value/custody proof;
3. replay pull proof.

Когда эти три вещи хотя бы paper-clean, можно отдельной сессией разбирать:

- бак воздуха;
- `ДЫШАТЬ / ПРОДАТЬ`;
- долг;
- смену;
- кредиты/аренду;
- базу как маленький floor;
- whether it feeds captured gas or mission-value payouts.

## 5. Что я буду делать во время обсуждения

Я не должен:

- записывать canon без твоего review;
- прятать сомнительные слова;
- делать вид, что TBD уже решен;
- выбирать два playable branches;
- тащить economy/title/roster в текущий blocker.

Я должен:

- переводить каждую идею в player action;
- критиковать свои варианты;
- критиковать твои варианты, если они ломают core;
- парковать сильные идеи с dependency;
- явно писать, что именно еще не определено;
- после owner approval обновлять draft/canon через понятный результат.

## 6. Когда можно будет писать canon

Только когда по конкретному вопросу есть:

- понятная owner-facing формулировка;
- player action;
- read;
- risk;
- consequence;
- boundary list;
- явное "можно записывать".

До этого mechanics-workbench = черновая доска.

END_OF_FILE: live/indie-game-development/work/mechanics-workbench/review-guide-v0.md
