---
id: i-standing-layer-never-ran-on-shipped-data-001
_kind: issue
level: execution
route: work
status: open
evidence: work/2026-08-29-research-householder-plan-architecture.md
_pos: 154
---

## issue
**ВЕСЬ СЛОЙ ПОЛОЖЕНИЯ ДЕЛ — ШКАЛЫ, МЕТКИ, ПЯТЬ ВИДОВ УСЛОВИЙ, ПЯТЬ ВИДОВ ЭФФЕКТОВ И ОБЁРТКА —
В СОБРАННОЙ ИГРЕ НЕ ИСПОЛНЯЕТСЯ НИ РАЗУ.**

Перемерено на `68c4e933`. `grep -in gauge` по `default.householder.json` → **0**; ни у одного из трёх
его обработчиков нет ни `when`, ни `effects`. `HouseholderStandingDecisionHandler.Wrap` возвращает
внутренний обработчик как есть, когда навешивать нечего (`:54-57`), поэтому обёртка не создаётся
вообще, и единственная боевая точка вызова `HouseholderCondition.AllHold`
(`HouseholderStandingDecisionHandler.cs:68`) не достигается.

Это расширяет `i-householder-gauges-cannot-be-authored-001` (там про недостижимость шкал со стороны
данных) на весь слой: недостижимы не только шкалы, но и метки, и условия, и эффекты — **всё, на чём
стоит любой из четырёх способов построить план хозяина.**

**ВТОРОЕ, И ОНО В ТОМ ЖЕ ФАЙЛЕ.** Единственная авторская реакция профиля, `stand-over-the-spot`,
объявляет `"cause": "landing"` — **ту же причину, что поставочная строка `landing`**.
`HouseholderReaction.FromDecision` резолвит по `HouseholderReactionCatalog.Default.TryGetByCause`,
то есть по СТАТИЧЕСКОМУ поставочному каталогу, и вернёт поставочную. Сегодня безвредно только потому,
что до `stand-over-the-spot` добираются по ИМЕНИ из обработчика.

**Загрузчик проверяет уникальность имён и НЕ проверяет ни причину, ни событие, ни факт**
(`grep -n "case \"" …Loader.cs` — 70 меток, ни одной проверки на дубль причины). А этот файл станет
образцом для каждого процедурно собранного профиля.
## fix_when
Первым шагом той ноги, которая первой захочет `when` или `effects` на строке — то есть первой ноги
по плану хозяина. Не отдельной работой: это прокур, а не предмет. Проверка на дубль причины —
одна строка в загрузчике, тем же порядком, каким он уже отказывает по дублю имени.
END_OF_FILE: live/indie-game-development/cards/i-standing-layer-never-ran-on-shipped-data-001.md
