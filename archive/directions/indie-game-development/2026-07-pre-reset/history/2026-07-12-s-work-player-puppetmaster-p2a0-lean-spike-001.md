# RESULT s-work-player-puppetmaster-p2a0-lean-spike-001

call: none — owner-present re-scope of M1-P2a0 (owner drove the decision in chat)
direction: indie-game-development
play: work (owner-present re-scope + BUILD issue)
node/task: g-9c41 / M1-P2a0
date: 2026-07-12

## outcome

Владелец пересмотрел scope доказательства M1-P2a0 и выбрал **лёгкий спайк** вместо тяжёлого
live-source proof. Owner-present бриф показал: доказываем ровно две вещи (толчок→реакция→подъём на
нашей капсуле; чистое владение позицией тела в момент удара — это и есть весь мультиплеерный риск),
всё остальное — обвязка. Владелец дал дословный вердикт «Лёгкий спайк» → «го» на конкретную лёгкую
спеку. Тяжёлый подход (тест-owned observer/publisher/attempt-tree/collision-atomicity + A/B-сразу +
immutable-RED-как-гейт + видео/openspec/ревью-машинерия) **сознательно свёрнут**; гейт лёгкого спайка =
**глаз владельца + живой runtime-прибор** в открытом редакторе, владелец сам жмёт Play и выносит
PASS/FAIL. Открытый PLAN-amend open_call заменён единственным лёгким BUILD-CALL
`c-exec-player-puppetmaster-p2a0-lean-spike-build-001`; задача M1-P2a0 остаётся `active`.

## owner decision (verbatim, this chat 2026-07-12)

- «Лёгкий спайк» — выбор лёгкой версии из двух предложенных (лёгкий спайк vs строгий машинный proof).
- «го» — одобрение конкретной лёгкой спеки (кнопки камень/импульс/сброс; прибор 3 строки
  Контроллер/Рэгдолл · Норма/Сбит/Встаёт · коллизия цела/сломана; Кандидат A первым; критерий «чисто»
  = удар→Сбит→Встаёт→Норма, управление чисто вернулось контроллеру, коллизия цела, стабильно на
  нескольких ударах; мутно → пробуем B; MP inventory-only; гейт = owner-eye + прибор).

Владелец также предупредил про переусложнение (chat: «мне что-то начинает казаться, что ты строишь
какую-то прям сложную вещь… реально ли это самое минимальное?») — это учтено: половина сложности
прошлого захода была борьбой с headless-обвязкой, не с самим вопросом; лёгкий спайк уходит от неё.

## the lean spike (что заказано на стройку)

1. Стенд: **существующий** p2a0 (переиспользуя готовый PuppetMaster import + подтверждённый маппер
   BehaviourPuppet.state{Puppet|Unpinned|GetUp}, base b9aea60c). Не с нуля.
2. Кнопки: «Кинуть камень» / «Импульс» / «Сброс» (владелец в Play сам бьёт).
3. Прибор (реальный runtime-считыватель, не подделка): Управление телом Контроллер/Рэгдолл ·
   Состояние Норма/Сбит/Встаёт · Коллизия капсулы цела/сломана.
4. Проводка «Кандидат A» первым (контроллер = владелец позиции; рэгдолл реагирует поверх). B — только
   если A мутный.
5. Смоук через PlayMode test runner (не headless-loop): кнопки/прибор живые. Это НЕ вердикт про
   PuppetMaster — вердикт выносит владелец, играя.
6. MP inventory-only (записать модель владельца строкой); двух-машинный тест — обязательная будущая нога.

## evidence

- Owner-present бриф + дословные вердикты в этом чате (см. «owner decision»).
- Переиспользуемое product-состояние (проверено первыми руками в предыдущей сессии
  s-work-player-puppetmaster-p2a0-checkpoint-route-001): branch codex/c-exec-player-puppetmaster-p2a0-002-build
  @ b9aea60c, NOT MERGED vs origin/main@a644e5db; чистый import + маппер готовы.
- Заказ на стройку: work/c-exec-player-puppetmaster-p2a0-lean-spike-build-001-call.md (self-contained).

## state_changes

**NOW.md:**
- `updated:` → `s-work-player-puppetmaster-p2a0-lean-spike-001`.
- task `M1-P2a0`: без изменений (`status: active`; done_when не трогается — доказательство того же исхода
  более лёгким способом).
- `open_calls`: УДАЛИТЬ `c-exec-player-puppetmaster-p2a0-002-plan-amend-001` (свёрнут в лёгкий BUILD —
  тяжёлый PLAN-amend больше не нужен, владелец выбрал лёгкую версию напрямую); ДОБАВИТЬ
  `c-exec-player-puppetmaster-p2a0-lean-spike-build-001` (to: executor, kind: engineering, lean spike,
  gate = owner-eye + live readout).
- `next:` → `work/c-exec-player-puppetmaster-p2a0-lean-spike-build-001-call.md`.

**work/:** + `c-exec-player-puppetmaster-p2a0-lean-spike-build-001-call.md`;
− `c-exec-player-puppetmaster-p2a0-002-plan-amend-001-call.md` (superseded same-day, никогда не исполнялся;
содержимое сохранено в git @ d1e38ce).

**LOG.md:** + одна строка lean-spike re-scope + BUILD issue.

**history/:** + этот файл.

**work/board/dashboard.html:** перегенерированы hero-eyebrow + tag «Борд» + карточка P2a0
(статус «СТРОЙКА ЗАКАЗАНА · лёгкий спайк») + строка журнала за 12.07. «Проблемы» не менялись.

## captures

- immutable RED c73b0195 тестировал СУПЕРСЕДНУТЫЙ тяжёлый подход — оставлен read-only, НЕ гейт лёгкого
  спайка (записано в BUILD-CALL); будущая уборка/маркировка heavy-подхода — не эта нога.
- (перенесены из checkpoint-route) immutable-001 full_runtime_cycle_green=false RED (честный, не трогать);
  CoarseArtifactTests.L19 digest drift — g9c41/coarse-нога.

## decisions_needed

(нет — владелец дал дословный вердикт; следующий вердикт P2a0 берётся после того, как владелец сыграет)

## play_check

- 1 orient/recite: done — свежая сверка состояния (HEAD d1e38ce, NOW open_calls/next), продолжение
  owner-present разговора о scope.
- 2 present brief (owner): done — plain-language бриф «что доказываем / это минимально?»; two-option
  выбор (лёгкий спайк vs строгий) с рекомендацией лёгкого.
- 3 owner verdict (owner): done — «Лёгкий спайк» + дословное «го» на конкретную спеку (цитаты выше).
- 4 freeze + issue: done — лёгкая спека заморожена как self-contained BUILD-CALL; тяжёлый PLAN-amend
  свёрнут; M1-P2a0 остаётся active; NOW.next → lean BUILD; панель перегенерирована.

## log

2026-07-12 — work/lean-spike-rescope (g-9c41/M1-P2a0, s-work-player-puppetmaster-p2a0-lean-spike-001):
владелец пересмотрел scope доказательства и выбрал ЛЁГКИЙ спайк («Лёгкий спайк» → «го») — тяжёлый
observer/attempt-tree/A-B-C/RED-gate/видео сознательно свёрнут; гейт = owner-eye + живой runtime-прибор
(кнопки камень/импульс/сброс; прибор Контроллер/Рэгдолл · Норма/Сбит/Встаёт · коллизия; Кандидат A первым;
владелец сам жмёт Play и выносит PASS/FAIL; MP inventory-only). PLAN-amend open_call заменён единственным
lean BUILD-CALL c-exec-player-puppetmaster-p2a0-lean-spike-build-001 (переиспользует import+mapper @
b9aea60c, immutable RED c73b0195 read-only и не гейт); M1-P2a0 active, next = lean BUILD.

## next

```
CALL c-exec-player-puppetmaster-p2a0-lean-spike-build-001
to: executor   kind: engineering   phase: BUILD (lean spike)
direction: indie-game-development   node: g-9c41   task: M1-P2a0
repo: C:\projects\Unity\GasCoopGame_p2a0_002   base: b9aea60c
gate: owner-eye + live runtime readout (owner plays)
→ work/c-exec-player-puppetmaster-p2a0-lean-spike-build-001-call.md
```

END_OF_FILE: live/indie-game-development/history/2026-07-12-s-work-player-puppetmaster-p2a0-lean-spike-001.md
