# CALL c-review-char-v2-reaction-core-g5-001

- id: c-review-char-v2-reaction-core-g5-001
- to: session (fresh, separate — binding G5; cross-family Codex PREFERRED — см. §Почему именно Codex; read-only)
- for: g-6d4e «Игровые персонажи» / В2 Leg 1 — связывающий G5 на собранное headless-ядро реакции
- issued: 2026-07-14 by s-work-char-v2-leg1-return-g5-open-001
- play: review

## goal (outcome, not method)

У В2 Leg 1 есть связывающий G5-вердикт: свежая ОТДЕЛЬНАЯ сессия попыталась ОПРОВЕРГНУТЬ заявки собранного лега и не
смогла (или вернула, что именно опровергла и чем). Только CONFIRMED закрывает Leg 1 и разблокирует Leg 2. У этого лега
НЕТ owner-eye половины — он headless по дизайну приёмки (owner-eye приходит только в Leg 2), поэтому **G5 — единственные
ворота Leg 1**. Merge в main остаётся решением направления, НЕ этой сессии.

## context

### Что проверять (единственный источник истины — читать в продукте, НЕ изобретать)

- Worktree `C:\projects\Unity\GasCoopGame_p2a0_002`, ветка `c-exec-char-v2-reaction-core-build-001`,
  **замороженный кончик @e64f070f3eda4e270a683f4380035a00962d63ed**.
- Коммиты лега (порядок проверен писарем first-hand): `5e38d058` frozen surface (RED-ready) → `b1e800fb` independent
  RED (58 тестов) → `192855f3` impl (green) → `1ebc3af5` regression guard (G4-находка F1) → `e64f070f` ADR + G4-review +
  pre-freeze RED record + RESULT.
- Новый код лега: `Assets/GasCoopGame/Characters/{BodyReactionDriver,KnockdownAwareBodyState}.cs`.
  Новые тесты: `tests/GasCoopGame.Core.Tests/Characters/{BodyReactionDriverV2Tests,KnockdownAwareBodyStateTests}.cs`.
- Доки лега: `docs/adr/ADR-E-0013-c-exec-char-v2-reaction-core-build-001-knockdown-reaction-core.md`;
  `docs/results/c-exec-char-v2-reaction-core-build-001.md`;
  `docs/reviews/review-c-exec-char-v2-reaction-core-build-001.md` (G4);
  `docs/reviews/prefreeze-red-c-exec-char-v2-reaction-core-build-001.md` (obligation-set O1–O36 + скелеты + gap-list).

### Замороженный spec (AUTHORITY — ПРОЧТИ; абсолютный путь на этой машине)

`C:\my_global_workflow_worktrees\indie-game-development\live\indie-game-development\work\c-plan-characters-002-plan.md`
— особенно **§0 F1** (knockdown-контракт: реакция ГЕЙТИТ источник пока State≠Normal + на GetUp reconcile авторитет←rest),
**§4 Leg 1** (что именно строится и evidence-class = headless), **§6 riskiest assumption** (утечка даже в ОДИН кадр в
авторитетный трансформ = коррупция детерминированного ядра и разрыв В1-контракта — это убивающая сила лега).
Исходный BUILD-CALL с done_when: `work/c-exec-char-v2-reaction-core-build-001-call.md`.

### Что писарь УЖЕ подтвердил first-hand (НЕ переделывай — атакуй остальное)

Проверено в гите read-only сессией s-work-char-v2-leg1-return-g5-open-001; перепроверять эти пункты можно, но они не
должны съесть бюджет:

- **Дельта лега (`git diff --name-status 1674e3ef..HEAD`) = 10 файлов, ВСЕ статуса A (добавление), ноль M/D.**
  ⇒ boundary держится механически: ноль рига/рэгдолла/материала/физики/ядра/грида/сети/газа, ноль правок gate-scripts,
  ноль новых конформанс-скриптов.
- **Сейм байт-идентичен** — двумя способами: `git diff origin/main..HEAD` по `IAuthoritativeBodyState.cs` /
  `PlayerBodySocket.cs` / `BodyPose.cs` / `BodyReactions.cs` = ПУСТ; и ни один из четырёх не появляется в дельте лега.
- **v21 на базе** (⇒ идемпотентный SKIP re-sync'а законен, а не пропущенная работа): `HEAD:validation.config` →
  `"synced_contract_version": 21` + `synced_contract_version_v21_note`; `HEAD:AGENTS.md` → run-contract
  «Full-packet Plan-to-RED readiness (contract v21)» + секция `## Contract v21`. Контракт-файлов в дельте лега нет.
- **Порядок RED→impl по коммитам**: `b1e800fb` (только тест-файлы) РАНЬШЕ `192855f3` (только impl).
- **Неревьюенного источника нет**: после reviewed-commit `192855f3` идут только `1ebc3af5` (тест) и `e64f070f` (доки).
- Все 4 дока существуют на HEAD.

### ⚠ ПОПРАВКА К ПАКЕТУ БИЛДЕРА №1 — БАЗА УЕХАЛА (билдер не мог знать)

Хендбэк называет базу «origin/main@1674e3ef». Это было ИСТИНОЙ на форке и УСТАРЕЛО к возврату:

- `git merge-base HEAD origin/main` = `1674e3ef`; **`origin/main` = `86e7927f82c1e48a9d5ab7255ac8004dc12c10eb`**;
  `86e7927f` — **прямой ребёнок** `1674e3ef` (`parents:1674e3ef`). origin/main НЕ предок HEAD.
- Тайминг: первый коммит лега `5e38d058` — `2026-07-14 11:32:53 +0300`; `86e7927f` — `2026-07-14 11:40:15 +0300`.
  Дрейф ~8 минут, ВНУТРИ лега.
- Что несёт `86e7927f` («**Fix Git artifact identity false-green guard**»), чего у лега нет:
  `M docs/results/c-exec-cross-platform-git-identity-001.md` · `M tests/…/Field/Coarse/CoarseArtifactTests.cs` ·
  `M tests/…/Tooling/GitBlobIdentityTests.cs` · `A tests/…/Tooling/GitCommittedArtifactGuard.cs`.
- **Почему это важно именно тебе:** заявленные «OK: all gates green» и «headless 1721/0/0 (baseline 1662 + 58)»
  померены на дереве БЕЗ этой починки **ложно-зелёного** гварда. Базлайн 1662 привязан к `1674e3ef`, НЕ к актуальному
  main: на перебазированном дереве счёт будет ДРУГИМ, и это НЕ расхождение и НЕ ложь билдера.
- Предварительная оценка писаря (проверь, не принимай на веру): `86e7927f` ортогонален Characters (трогает Tooling +
  газовые coarse-тесты), поэтому это НЕ дефект Leg 1 и НЕ повод блокировать G5.
- **Ребейз — не твоя работа.** По правилам линий направления (`knowledge/g9c41-lanes-venues.md`): правило 4 «база уехала»
  — предполётное, билдер его на старте выполнил; правило 5 «следующий лег перебазируется» — ребейз принадлежит
  МЕРЖ-СЛОТУ. Ты гоняешь G5 по замороженному кончику `e64f070f`.

### ⚠ ПОПРАВКА №2 — В1 УЖЕ СМЁРЖЕН (в отличие от того, что говорили старые записи)

Проверено first-hand: `git merge-base --is-ancestor db69aba6 origin/main` → YES; база В1 `32107343` — тоже предок
origin/main; `git ls-tree origin/main Assets/GasCoopGame/Characters/` показывает все В1-исходники на main; продукт на
**v21**, не v20. Владельческое «Вариант 1» (merge запущен отдельно) доехало. `knowledge/g6d4e-char-v1-socket-delivered.md`
поправлен этой же сессией. **Не строй картину на «В1 unmerged / продукт v20»** — это устаревший факт.

### Почему именно Codex (cross-family)

Билдер называет свой G4 «cross-family», но это `claude-opus-4-8` ↔ `claude-sonnet-5` — кросс-**модельно** внутри ОДНОГО
семейства. Язык направления это разделяет: В1-G5 (Opus↔Opus) записан как «SAME-FAMILY» с каветом, а routing
(`gascoopgame-engineering-model-routing`) держит cross-family = Codex/GPT. ⇒ **Codex будет ПЕРВЫМ независимым семейством
на этом коде.** По правилам OS жёсткое требование — СВЕЖЕСТЬ сессии (≠ билдер), а не семейство; свежая same-family сессия
остаётся валидным binding G5. Но здесь cross-family реально добавляет, а не ритуал: запиши в RESULT, каким семейством
прогнан.

### Прочий контекст

- Проектные правила: локальная валидация = headless .NET гейты, CI нет (`gascoopgame-local-validation-no-ci`);
  контур `os/engineering/CONTOUR.md` + `VALIDATION.md` (v21 Plan-to-RED).
- G4 нашёл 0×P0/P1. Открытые намеренные P3 (знай их, Leg 2 обязан их учитывать): **F2/S3** — `IsReady` латчится в true
  «once ever-ready» и опрашивает inner при гейте; **F3/S8** — `GetUp(BodyPose)` из Normal транзиентно ставит `_held`.
  Оба задокументированы как self-healing. Твоё дело — проверить, что «намеренно» ≠ «замаскированный дефект».
- Reconcile-поза висит на СОБСТВЕННОМ `GetUp(BodyPose)` обёртки; `IBodyReactions.GetUp()` остался без параметров;
  `NullBodyReactions` — по-прежнему дефолт. Это заявка (f), проверь её.

## boundaries (out of scope / do not touch)

- **ТОЛЬКО ЧТЕНИЕ продукта**: ничего не собирать, не править source/tests, **не ребейзить**, не мержить, не пушить.
  Прогон тестов read-only — разрешён и ОБЯЗАН (см. done_when #2).
- Unity/MCP этой ноге не нужен (всё headless). Если для проверки заявки понадобился недоступный инструмент →
  **STOP + сказать владельцу**, никаких костылей и никаких source-скан-суррогатов (contract v16/v17).
- G5 обязана быть ОТДЕЛЬНОЙ свежей сессией (KERNEL G5), НЕ той, что писала билд, и НЕ сессией-писарем
  s-work-char-v2-leg1-return-g5-open-001.
- Не закрывать Leg 1 и не открывать Leg 2 без реального G5-вердикта. Merge в main — решение направления, НЕ этой сессии.
- Не трогать `GasCoopGame_dev` / `GasCoopGame_core` (foreign uncommitted работа). Дерево `p2a0_002` грязное локальным
  Unity/MCP-шумом (`.vscode/settings.json`, `Assets/Plugins/NuGet/*`, `Packages/manifest.json`, `packages-lock.json`,
  `ProjectSettings/PackageManagerSettings.asset`) — это НЕ часть лега, не коммитить и не чинить.
- `Assets/GasCoopGame/Characters.meta` untracked (и отсутствует на origin/main тоже) — пре-существующее с В1, вне scope
  Leg 1, уже captured направлением. НЕ дефект этого лега.
- Пре-существующий газовый красный (`L19_T2AndT3Artifacts_RemainByteUntouched` класс, golden-digest на main) — газовый
  трек, не дефект Leg 1.

## Заявки к ОПРОВЕРЖЕНИЮ (из done_when BUILD-CALL'а + spec §0 F1/§4/§6)

По каждой верни: **опровергнуто / не опровергнуто**, с доказательством (тест / код / наблюдение). По умолчанию —
refuted-if-uncertain: твоя работа опровергать, а не подтверждать.

- **(a) v21-SKIP законен**: база несёт v21, поэтому открывающий re-sync корректно пропущен; product source/tests/
  gate-scripts не тронуты; новых конформанс-скриптов нет. *(писарь подтвердил структурно — атакуй, если видишь дыру)*
- **(b) Independent RED был настоящим и краснел ДО импла**: заявлено 55/58 падали против скелетов, 3 зелёных = структурные
  seam-identity guard'ы. Тесты писал независимый автор (claude-sonnet-5) из spec+сейм+surface, импл не читал; builder их
  не редактировал. **Ключевой вопрос: не таутологичны ли они** — падают ли assert'ы, если поведение убрать? (В1-G5 гонял
  ровно эту проверку.)
- **(c) State machine**: Normal→Knockdown→GettingUp→Normal по абстрактному `BodyImpulse`-токену; инвариант «одно активное
  состояние»; детерминизм при (event, time) — ноль wall-clock/RNG/static mutable; неизвестный/нулевой токен = no-op
  (negative-control).
- **(d) F1 GATE — главная заявка лега**: пока State≠Normal вход НЕ двигает авторитетную позу. Заявлена **нулевая утечка
  за ВЕСЬ Knockdown/GettingUp** (гейт-ветка `Current` возвращает `_held` и не читает `_inner`). Утечка даже в один кадр =
  провал лега (spec §6). **Атакуй это в первую очередь.**
- **(e) F1 RECONCILE**: `GetUp(restPose)` ⇒ авторитетная поза == restPose (авторитет ← rest, а не картинка ← авторитет).
- **(f) Сейм и дефолт целы**: обёртка реализует СУЩЕСТВУЮЩИЙ `IAuthoritativeBodyState`; reconcile-поза висит на
  собственном `GetUp(BodyPose)` обёртки; `IBodyReactions.GetUp()` без параметров; `NullBodyReactions` остаётся дефолтом;
  старые Characters-тесты зелёные без правок.
- **(g) Гейты зелёные**: `pwsh -File tools/check.ps1` → «OK: all gates green»; headless 1721/0/0; hygiene / zero-float /
  int-overflow / type-hardcode OK. **Сверяй с поправкой №1** (см. done_when #4).
- **(h) Pre-freeze RED-ревьюер (v21 Plan-to-RED)** вывел ПОЛНЫЙ obligation-set O1–O36 + скелет на строку + полный
  gap-list; раунд 2 закрыл gap'ы (Tick-throw atomicity, same-step conflict determinism, wrapper-over-NullBodyReactions,
  extreme/terminate, per-field non-finite). **Вопрос: полон ли O1–O36 против spec — или обязательство потеряно?**
- **(i) G4-ревью честен**: 0×P0/P1; единственный P2 — пробел покрытия, закрыт `1ebc3af5`; F2/F3 (P3) действительно
  намеренные и self-healing, а не замаскированные дефекты; F4 negative-control N/A by absence законно.
- **(j) Boundary + не на main**: ноль рига/рэгдолла/материала/физики/ядра/грида/сети/газа; ветка НЕ на main.

## done_when (verifiable)

1. Свежая отдельная сессия прочитала лег first-hand (@e64f070f) и попыталась опровергнуть КАЖДУЮ заявку (a)–(j);
   вернула по каждой: опровергнуто / не опровергнуто, с доказательством. Заявка (d) — приоритет №1.
2. **Прогон тестов подтверждён зелёным ТВОИМИ руками** (headless .NET, read-only), а не по словам билдера. Минимум:
   `dotnet test tests/GasCoopGame.Core.Tests/GasCoopGame.Core.Tests.csproj --filter FullyQualifiedName~Characters`
   на HEAD `e64f070f` (билдер заявляет 98/98 Characters). Полный `tools/check.ps1` — по желанию/бюджету.
3. **Base-drift разобран явно** (это НЕ опция): подтверди или опровергни, что `86e7927f` («Fix Git artifact identity
   false-green guard») структурно ортогонален Characters и что заявленный gate-green Leg 1 НЕ зависит от отсутствия
   этой починки. Если найдёшь связь — это находка, и Leg 1 не закрывается до ребейз-прогона.
4. Числовые расхождения счёта тестов интерпретируются через поправку №1 (базлайн 1662 привязан к `1674e3ef`), а НЕ
   записываются в дефекты автоматически.
5. Явный связывающий вердикт: **Leg 1 CONFIRMED** (заявки не опровергнуты) — либо список реальных опровержений →
   repair-CALL, и Leg 2 остаётся HELD.
6. В RESULT зафиксировано, каким СЕМЕЙСТВОМ прогнан G5 (Codex/GPT = cross-family; Claude = same-family + кавет), и что
   evidence пришёл из свежей сессии, а не из in-session пре-пасса.

## return

RESULT (review): связывающий G5-вердикт по Leg 1 + first-hand доказательства по каждой заявке (a)–(j) + разбор
base-drift.

- **При CONFIRMED**: Leg 1 = done; выпустить **runnable** `c-exec-char-v2-body-rig-ragdoll-build-001` (Leg 2; spec
  `work/c-plan-characters-002-plan.md` §4 Leg 2; сейчас HELD в NOW.open_calls) — CALL самодостаточен, с абсолютным путём
  к spec'у и переиспользованием worktree `GasCoopGame_p2a0_002` (без плодения новых); передать в него открытые P3
  (F2 `IsReady`-латч / F3 транзиентный `_held`) как обязательные к учёту потребителем. Merge и ребейз на `86e7927f` —
  оставить решением направления (мерж-слот, правило линий 5), НЕ авто-запускать.
- **При опровержении**: repair-CALL с конкретными опровержениями; Leg 2 остаётся HELD; Leg 1 не закрывается.
- Знание: обновить/создать запись character-трека (G5-вердикт + каветы) — это review-play, knowledge/ твой.

## budget

Одна свежая review-сессия (можно MacBook; конвейерится параллельно другим трекам направления — правило линий 6).

END_OF_FILE: live/indie-game-development/work/c-review-char-v2-reaction-core-g5-001-call.md
