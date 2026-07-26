# g-6d4e В1 — socket + drop-in capsule: DELIVERED + G5-CONFIRMED + MERGED в main

updated: 2026-07-14 (s-review-char-v1-g5-close-001); 2026-07-14 (s-work-char-v2-leg1-return-g5-open-001 — узкая
фактическая правка merge-статуса по first-hand git-доказательству: В1 СМЁРЖЕН, продукт на v21)
readers: любая сессия character-трека (В2/В3), merge-сессия, direction review/pulse.

## Статус
В1 (socket + drop-in управляемая капсула) СОБРАН и прошёл ОБЕ половины ворот:
- **owner-eye** (owner-run PlayMode, 3 сцены) GREEN — владелец «Вариант 1» (подтвердил, что направлял билд).
- **связывающий fresh G5** (s-review-char-v1-g5-close-001; same-family Opus; read-only; 5 независимых рефутаторов
  + first-hand прогон 39/39 headless first-hand мной): **CONFIRMED** — ни одна заявка (a–f) не опровергнута, P1 нет.

## Где
- Продукт GasCoopGame: ветка c-exec-char-v1-socket-dropin-build-001 @db69aba6847a47ce2544ad1314f3567b327805d7,
  база origin/main@32107343 (на момент билда — contract v20). Worktree C:\projects\Unity\GasCoopGame_p2a0_002.
- **СМЁРЖЕН в main** (владельческое «Вариант 1» доехало). Проверено first-hand 2026-07-14
  (s-work-char-v2-leg1-return-g5-open-001): `git merge-base --is-ancestor db69aba6 origin/main` → YES; база 32107343 —
  тоже предок origin/main; `git ls-tree origin/main Assets/GasCoopGame/Characters/` показывает BodyPose.cs,
  BodyReactions.cs, IAuthoritativeBodyState.cs, PlayerBodySocket.cs, ScriptedPathBodyState.cs, asmdef (+metas).
  Продукт с тех пор ушёл на **contract v21** (validation.config `synced_contract_version: 21`).
  ⚠ Прежняя редакция этого файла утверждала «НЕ СМЁРЖЕН / продукт остаётся v20» — устаревший факт, снят по git.
- ⚠ `Assets/GasCoopGame/Characters.meta` (мета ПАПКИ) отсутствует и на origin/main тоже ⇒ Unity генерит folder-meta с
  новым guid на каждой машине; будущий `-Deliver` споткнётся через DF-5. Пре-существующее с В1, отдельной мелкой ногой.
- Доки: docs/results/c-exec-char-v1-socket-dropin-build-001.md; docs/adr/ADR-E-0012-...-authoritative-body-pose-socket.md;
  docs/character-v1-b1-owner-eye.md.

## Что доказано / чем
- Engine-free seam (IAuthoritativeBodyState pull-модель + PlayerBodySocket rebindable + BodyPose + ScriptedPathBodyState
  + NullBodyReactions no-op) — headless 39/39; тесты неташтологичны (проверено рефутацией: pull/swap/not-ready/null/NaN
  экспонированы assert'ами, которые падают, если поведение убрать).
- «Controllable» + drop-in во 2-ю сцену + follow-camera + scene-decouple — доказаны **OWNER-EYE**, не headless
  (это дизайн приёмки: InputBodyStateSource — MonoBehaviour, headless не гоняется).
- Boundary держится: нет rig/ragdoll/physics/core/grid/network/gas (PuppetMaster только в комментарии; RootMotion
  gitignored). Ветка НЕ на main (проверено git merge-base).
- Внешний красный L19_T2AndT3Artifacts_RemainByteUntouched — предсуществующий coarse gas-field TDD-red
  (SHA-digest газовой телеметрии), структурно не связан с В1. Чинится в gas-track.

## Открытые находки (НЕ блокеры В1; в В2 / cleanup)
- **P2 magenta:** префаб + Ground + Markers ссылаются на material guid 31321ba15b8f8eb4c954353edc038b1d, которого нет
  в проекте → рендер как missing-material magenta. Косметика; фикс в В2/визуал (owner-eye был зелёным как grey-box).
- **P2 test-robustness:** no-op reaction тест таутологичен (State — константа); ScriptedPath.Advance/interp не покрыты
  (out of scope по docstring). Усилить при В2.
- Awake-ordering (ScriptedPathSource.Awake до PlayerBodyView.Start) — load-bearing для drop-in override; Unity
  гарантирует Awake-before-Start, но headless не покрывает.

## Каветы гейта
- G5 был **SAME-FAMILY** (Opus валидировал Opus-билд), тогда как routing направления
  ([[gascoopgame-engineering-model-routing]]) предпочитает Codex (cross-family) для VALIDATE. По правилам OS свежий
  same-family G5 — валидный binding G5; cross-family опционален. Доп-Codex-проход можно запросить перед merge для
  доп-строгости (особенно на Unity-adapter/input, которые headless не покрывает).

## Дальше
- **d-char-v1-post-g5-001 РЕШЁН (Вариант 1):** продуктовый merge В1 запущен отдельно и **ДОЕХАЛ** (В1 на main, см. §Где);
  Codex cross-family проход НЕ делаем; В2 открыт. (s-plan-characters-v2-freeze-001, 2026-07-14.)
- **В2 Leg 1 СОБРАН и ВЕРНУЛСЯ 2026-07-14** (s-work-char-v2-leg1-return-g5-open-001): замороженный кончик
  c-exec-char-v2-reaction-core-build-001@e64f070f, форк-база 1674e3ef. First-hand подтверждено: дельта = 10 файлов, все
  добавления; сейм байт-идентичен; v21 уже на базе (re-sync законно пропущен); RED-коммит раньше импла; G4 без P0/P1.
  **НЕ закрыт, НЕ смёржен** — ждёт связывающий свежий G5 (`c-review-char-v2-reaction-core-g5-001`, READY PARALLEL); у
  этого лега нет owner-eye половины (headless по дизайну), поэтому G5 — единственные ворота. ⚠ База уехала внутри лега:
  origin/main = 86e7927f «Fix Git artifact identity false-green guard» ⇒ gate-green и baseline 1662 померены без этой
  починки; ребейз = мерж-слот (правило линий 5), не G5.
- **В2 FROZEN:** тело через ТОТ ЖЕ сейм. Spec: work/c-plan-characters-002-plan.md (owner «1 да / 2 да / 3 как
  рекомендуешь»). Две BUILD-ноги: Leg 1 = headless reaction state machine + **knockdown-aware
  IAuthoritativeBodyState-обёртка** (RUNNABLE, c-exec-char-v2-reaction-core-build-001); Leg 2 = риг + процедурная
  локомоция + **изолированный** косметический PuppetMaster рэгдолл + свой материал (HELD до Leg 1 G5). Два вывода
  разбора кода, вшитые в спек: **F1** — реакция ОБЯЗАНА гейтить источник в нокдауне и на GetUp reconcile-ить
  авторитет←rest (иначе «тело лежит но идёт на вводе»); сейм-ТИПЫ при этом байт-идентичны. **F2** — magenta guid
  31321ba1… = дефолтный URP Lit.mat (referenced project-wide вкл. 2 газовые сцены), guid-pin ЗАПРЕЩЁН, фикс = свой
  материал персонажа. Гейтинг v20→v21 = идемпотентный контракт-текст re-sync на входе Leg 1, НЕ за NearGas.
  PuppetMaster установлен локально но **gitignored** (per-machine) → рэгдолл изолирован, базовый префаб работает без RootMotion.
- **В3:** grid-ballistics CORE (g-9c41) кормит сейм; 2-machine FishNet proof.

END_OF_FILE: live/indie-game-development/knowledge/g6d4e-char-v1-socket-delivered.md
