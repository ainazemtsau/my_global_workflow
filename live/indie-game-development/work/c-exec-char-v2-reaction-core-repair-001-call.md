CALL c-exec-char-v2-reaction-core-repair-001

* id: c-exec-char-v2-reaction-core-repair-001
* to: executor (fresh CONTINUATION session — НЕ plan-лег; fix-a-finding discipline)
* for: g-6d4e «Игровые персонажи» / В2 Leg 1 — закрыть единственное опровержение связывающего G5
* issued: 2026-07-14 by s-review-char-v2-reaction-core-g5-001 (binding G5)
* play: execute

goal (outcome, not method)

Leg 1 закрыт: класс «обёртка отдаёт baseline, который не заполняла» убит целиком (не по сайту), G4-запись
перестала утверждать ложное, RESULT цитирует воспроизводимую цифру. После этого Leg 1 = done и Leg 2 разблокирован.

**Это БАГ-ФИКС, а не новая нога и НЕ ре-план** (AGENTS.md `## Contract v19` scope-bullet, владельческое правило
2026-07-11: review-находки — БАГИ, чинятся ПРЯМО, максимум свежей continuation-сессией; предписание «перепланировать»
не связывает). Объём: **~2 строки продукт-кода + RED-тест + 2 строки в ревью + 1 строка в RESULT.** Не расширять.

context

* Worktree `C:\projects\Unity\GasCoopGame_p2a0_002`, ветка `c-exec-char-v2-reaction-core-build-001`, тип `e64f070f`.
  **Продолжать эту же ветку** (не плодить новую, не ребейзить — ребейз на `86e7927f` принадлежит мерж-слоту).
* Спек (AUTHORITY):
  `C:\my_global_workflow_worktrees\indie-game-development\live\indie-game-development\work\c-plan-characters-002-plan.md`
  §0 F1 / §4 Leg 1 / §6.
* Полный G5-разбор с пробами: `knowledge/g6d4e-char-v2-leg1-reaction-core.md`. Прочти его — там доказательства.
* Что G5 подтвердил и чего НЕ надо трогать: F1-гейт герметичен (ноль утечки за весь Knockdown/GettingUp);
  тесты не таутологичны (7/7 мутантов убиты); сейм байт-идентичен; 1721/1721; base-drift ортогонален; v21-SKIP
  законен. **Ничего из этого не переделывать.**

## R1 (P2, главное) — класс «`_held` отдан незаполненным»

**Инвариант к закрытию:** `IsReady == true` ⟹ `Current` — поза, реально полученная от inner, а НЕ незаполненный
плейсхолдер `BodyPose.Origin`. Это дословный контракт `IAuthoritativeBodyState` («Current... Only meaningful when
IsReady is true») и обещание `PlayerBodySocket.Bind` («a not-yet-ready source does not snap the body»).

**Воспроизведение (сделай САМ до фикса — fix-a-finding требует verify-at-site):** обёртка построена, пока
`inner.IsReady == false` (ctor:43-44 → `_everReady=false`, `_held=Origin`) → inner становится ready в реальной позе
(например 100,0,250) → `Knockdown(valid)` ДО первого Normal-чтения → `wrapper.IsReady` == **true**
(`KnockdownAwareBodyState.cs:74` латчится от опроса inner, НЕ заполняя `_held`) → `wrapper.Current` == **Origin** →
`PlayerBodySocket.Current:48` доверяет `IsReady` и затирает корректный last-known → **тело в мировом нуле весь
knockdown+get-up**.

**Сайты класса (свести все, не только сайт 2):**
1. `KnockdownAwareBodyState.cs:43-44` — ctor сеет `_held=Origin`, когда inner не ready. *(G4-находка F1 запинила
   БЕЗОПАСНУЮ ветку этого сайта — inner ready на ctor — тестом `Knockdown_WithoutPriorRead_FreezesAtConstruction
   Snapshot` (`1ebc3af5`); сломанная ветка того же класса осталась незапиненной. Это и есть промах class-sweep.)*
2. `KnockdownAwareBodyState.cs:70-77` — `IsReady` латчит `_everReady=true` от опроса inner, НЕ заполняя `_held`. ← разрыв
3. `KnockdownAwareBodyState.cs:85-90` — `GetUp(BodyPose)` пишет `_held` + `_everReady=true` даже когда драйвер
   отказал (`BodyReactionDriver.cs:83` возвращает рано, если `State != Knockdown`) — это G4-F3.

**Порядок (обязателен):** RED-тест(ы) на инвариант ПЕРЕД фиксом (независимо авторские — билдер их не редактирует,
только делает зелёными) → фикс → sweep всех трёх сайтов → полные гейты. Форма фикса — твоё ADR-решение
(например: заполнять `_held` из inner в момент, когда латч переворачивается; и гейтить запись `_held` в
`GetUp(BodyPose)` фактом перехода драйвера). **Сейм НЕ трогать** — `IAuthoritativeBodyState` / `PlayerBodySocket` /
`BodyPose` / `BodyReactions` остаются байт-идентичны (это проверяемое done_when).

## R2 (P3) — исправить ложные диспозиции в G4-ревью

`docs/reviews/review-c-exec-char-v2-reaction-core-build-001.md`:
* **F2** сейчас пишет «`Current` stays well-defined (frozen/Origin) — self-healing, **no observable corruption**».
  Ложь: коррупция наблюдаема через реальный `PlayerBodySocket` (см. R1). Переписать по факту + disposition
  `fixed <sha>`.
* **F3** сейчас пишет «the next Normal read overwrites `_held` ... **self-correcting**». Ложь в реальном порядке:
  самокоррекция происходит только на NORMAL-чтении, а Knockdown может прийти раньше → тело замирает в
  инъецированной позе. Переписать по факту.
* Соблюсти contract v10/v14/v15 форму (disposition ∈ `fixed <sha>` | `refuted`+маркер | `owner-ack`; sweep-строка
  на класс; scope/site колонки). Раунды ≤3.

## R3 (P3) — исправить протухшую цифру в RESULT

`docs/results/c-exec-char-v2-reaction-core-build-001.md:58` фиксирует «**1720** passed (baseline 1662 + **58** new)».
На доставленном кончике прогон даёт **1721** (G5 прогнал first-hand; 1662 + 59 = 1721 — 46 driver + 13 wrapper
`[Test]`). Цифра снята на `192855f3`, до `1ebc3af5`; тот же документ себе противоречит на стр. 33-34 и 97-99.
Привести evidence к тому, что реально выдаёт `check.ps1` на типе.

boundaries (out of scope / do not touch)

* **НЕ расширять объём.** Не трогать F1-гейт, state machine, валидацию импульса, leftover-carry, `>=`-границу,
  Tick-атомарность — G5 их подтвердил (7/7 мутантов убиты).
* **НЕ чинить resume-snap / re-seed inner-источника** — это раскрытая, спеком маршрутизированная граница **Leg 2**
  (спек §4 Leg 2 «вставание БЕЗ рывка» = owner-eye Leg 2; раскрыто 4× в доках лега). Идёт carry-forward'ом в CALL
  Leg 2, НЕ сюда.
* Сейм остаётся байт-идентичным. Ветка НЕ на main. Не мержить, не пушить, не ребейзить.
* Не трогать `GasCoopGame_dev` / `GasCoopGame_core`. Грязь p2a0_002 (`.vscode/`, `Assets/Plugins/NuGet/*`,
  `Packages/*`, `ProjectSettings/PackageManagerSettings.asset`) и untracked `Characters.meta` — пре-существующее,
  не коммитить, не чинить.
* Unity/MCP не нужен (headless). Требуемый инструмент недоступен → STOP + владелец (contract v16), без костылей и
  без source-скан-суррогатов (v17).
* v21-re-sync не делать — база уже v21 (проверено).

done_when (verifiable)

1. Воспроизведение R1 показано ДО фикса (проба/тест), не по словам.
2. RED-тест(ы) на инвариант «`IsReady==true` ⟹ `Current` получена от inner, не `Origin`-плейсхолдер» написаны
   НЕЗАВИСИМО и краснели до фикса; билдер их не редактировал.
3. Все три сайта класса сведены; фикс структурный (закрывает класс), не по-сайтовый патч.
4. `pwsh -File tools/check.ps1` → `OK: all gates green`; headless ≥1721 + новые, 0 failed; Characters зелёные.
5. Сейм байт-идентичен: `git diff origin/main..HEAD` по четырём сейм-файлам ПУСТ.
6. G4-ревью: F2/F3 переписаны по факту, каждая строка диспозирована; contract v10/v14/v15 форма соблюдена.
7. RESULT: цифра гейта воспроизводится на типе; ADR обновлён, если форма фикса — архитектурное решение.
8. Один cross-family G4 read-only на ремонт. **Codex PREFERRED** — на этом коде до сих пор НЕ было ни одного
   независимого семейства (и билдер, и его G4, и этот G5 — все Claude).

return

RESULT (execute) в `docs/results/c-exec-char-v2-reaction-core-build-001.md` (тот же per-leg файл — это тот же лег,
не новый) + маршрут домой направлению на связывающий G5 ремонта. Билдер НЕ авторит следующий CALL, НЕ мержит,
НЕ открывает Leg 2.

budget

Одна свежая continuation-сессия. Ремонт маленький — если он раздувается, это сигнал: STOP + владелец.

END_OF_FILE: live/indie-game-development/work/c-exec-char-v2-reaction-core-repair-001-call.md
