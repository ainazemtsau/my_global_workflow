# g-6d4e В1 — socket + drop-in capsule: DELIVERED + G5-CONFIRMED (unmerged)

updated: 2026-07-14 (s-review-char-v1-g5-close-001)
readers: любая сессия character-трека (В2/В3), merge-сессия, direction review/pulse.

## Статус
В1 (socket + drop-in управляемая капсула) СОБРАН и прошёл ОБЕ половины ворот:
- **owner-eye** (owner-run PlayMode, 3 сцены) GREEN — владелец «Вариант 1» (подтвердил, что направлял билд).
- **связывающий fresh G5** (s-review-char-v1-g5-close-001; same-family Opus; read-only; 5 независимых рефутаторов
  + first-hand прогон 39/39 headless first-hand мной): **CONFIRMED** — ни одна заявка (a–f) не опровергнута, P1 нет.

## Где
- Продукт GasCoopGame: ветка c-exec-char-v1-socket-dropin-build-001 @db69aba6847a47ce2544ad1314f3567b327805d7,
  база origin/main@32107343 (contract v20). Worktree C:\projects\Unity\GasCoopGame_p2a0_002.
- **НЕ СМЁРЖЕН в main.** Merge — решение направления (владельца).
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
- **d-char-v1-post-g5-001 РЕШЁН (Вариант 1):** продуктовый merge В1 запущен отдельно; Codex cross-family проход НЕ
  делаем; В2 открыт. (s-plan-characters-v2-freeze-001, 2026-07-14.)
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
