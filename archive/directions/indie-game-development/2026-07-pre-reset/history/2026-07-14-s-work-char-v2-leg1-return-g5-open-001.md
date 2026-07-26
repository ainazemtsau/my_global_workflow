RESULT s-work-char-v2-leg1-return-g5-open-001 (input: builder handback for c-exec-char-v2-reaction-core-build-001)
direction: indie-game-development   play: work (executor return; g-6d4e — параллельный трек, идёт через open_calls, не через tasks активной ставки)   node/task: g-6d4e / В2 Leg 1

outcome: |
  Пришёл продуктовый BUILD-хендбэк В2 Leg 1 (headless-ядро реакции + knockdown-aware источник) из worktree
  C:\projects\Unity\GasCoopGame_p2a0_002. Зачтён как evidence-checkpoint: все структурно проверяемые заявки
  подтверждены first-hand в гите, ни одна не опровергнута. Leg 1 НЕ закрыт (связывающий свежий G5 — обязателен),
  НЕ смёржен; Leg 2 остаётся HELD. Returned BUILD CALL consumed; открыт связывающий fresh cross-family G5
  (c-review-char-v2-reaction-core-g5-001, READY PARALLEL), несущий ДВЕ поправки к картине билдера: (1) база уехала
  на origin/main@86e7927f «Fix Git artifact identity false-green guard» через 8 минут после форка — его gate-green
  и счёт 1721 померены на дереве без этой починки; (2) В1 УЖЕ смёржен в main (продукт на v21), вопреки knowledge/,
  который правится по first-hand git-доказательству. Глобальный NOW.next (route-reset review) сохранён.

evidence: |
  Класс входа:
  - Вход — продуктовый BUILD-хендбэк (evidence input, не Direction-OS RESULT: нет state_changes/play_check/next).
    По KERNEL §4 + adapter Role 1 «builder-return is not close» сам по себе не очищает open_call и не метит done.
  - Сам хендбэк это признаёт: «СТАТУС: BUILT, gate-green, NOT MERGED. Закрытия не заявляю» + «ЗАПРОС К НАПРАВЛЕНИЮ:
    выпустить связывающий свежий cross-family (Codex) G5 в ОТДЕЛЬНОЙ сессии».

  First-hand проверка (read-only, продуктовый репо C:\projects\Unity\GasCoopGame_p2a0_002):
  - Ветка c-exec-char-v2-reaction-core-build-001, HEAD = e64f070f3eda4e270a683f4380035a00962d63ed. Все 5 заявленных
    коммитов присутствуют в заявленном порядке.
  - ПОРЯДОК RED→GREEN подтверждён коммитами: 5e38d058 (surface, только 2 .cs + 2 .meta) → b1e800fb (только 2 тест-файла)
    → 192855f3 (только 2 .cs impl) → 1ebc3af5 (только тест) → e64f070f (только 4 дока). Тесты РАНЬШЕ импла.
  - ИСТИННАЯ ДЕЛЬТА ЛЕГА (git diff --name-status 1674e3ef..HEAD) = 10 файлов, ВСЕ со статусом A (добавление),
    ноль M/D: Characters/{BodyReactionDriver,KnockdownAwareBodyState}.cs(+.meta), tests/Characters/{BodyReactionDriverV2Tests,
    KnockdownAwareBodyStateTests}.cs, docs/{adr/ADR-E-0013-…, results/…, reviews/prefreeze-red-…, reviews/review-…}.md.
    ⇒ boundary держится механически: ноль рига/рэгдолла/материала/физики/ядра/грида/сети/газа, ноль правок gate-scripts,
    ноль конформанс-скриптов. Заявка «Product source/tests/gate-scripts не тронуты» — ПОДТВЕРЖДЕНА.
  - СЕЙМ БАЙТ-ИДЕНТИЧЕН — подтверждено ДВАЖДЫ: (а) git diff origin/main..HEAD по IAuthoritativeBodyState.cs /
    PlayerBodySocket.cs / BodyPose.cs / BodyReactions.cs = ПУСТ; (б) ни один из четырёх не появляется в дельте лега.
  - v21 НА БАЗЕ ПОДТВЕРЖДЁН (⇒ идемпотентный SKIP законен, а не пропущенная работа): git show HEAD:validation.config →
    "synced_contract_version": 21 + synced_contract_version_v21_note (semantic full-packet Plan-to-RED); HEAD:AGENTS.md →
    строка 127 «Full-packet Plan-to-RED readiness (contract v21)» + секция 369 «## Contract v21». Дельта лега контракт-файлы
    НЕ трогает — согласовано со SKIP.
  - Доки на HEAD (git ls-tree): docs/adr/ADR-E-0013-…-knockdown-reaction-core.md, docs/results/c-exec-char-v2-reaction-core-build-001.md,
    docs/reviews/prefreeze-red-…md, docs/reviews/review-…md — все 4 существуют.
  - G4-ревью прочитан first-hand: reviewed-commit 192855f3, builder claude-opus-4-8, reviewer claude-sonnet-5, ревьюер сам
    прогнал сьют (97/97) и проверил сейм через git diff. P0/P1 нет; F1(P2) fixed 1ebc3af5; F2/F3(P3) acknowledged-intentional
    (S3/S8); F4 n/a by absence. Заявка «после reviewed-commit источник не менялся» ПОДТВЕРЖДЕНА по коммитам (1ebc3af5 = тест,
    e64f070f = доки) ⇒ неревьюенного источника нет.

  НАХОДКА 1 — БАЗА УЕХАЛА (билдер не мог знать; поправка к его пакету):
  - Заявка «база origin/main@1674e3ef» была ИСТИННОЙ на форке и УСТАРЕЛА к хендбэку. Факты: git merge-base HEAD origin/main
    = 1674e3ef; origin/main = 86e7927f82c1e48a9d5ab7255ac8004dc12c10eb; 86e7927f — ПРЯМОЙ ребёнок 1674e3ef
    (parents:1674e3ef), committed 2026-07-14 11:40:15 +0300, тогда как первый коммит лега 5e38d058 — 11:32:53 +0300.
    Дрейф ~8 минут, ВНУТРИ лега. origin/main НЕ предок HEAD (проверено).
  - Что несёт 86e7927f («Fix Git artifact identity false-green guard»), чего у лега нет: M docs/results/c-exec-cross-platform-git-identity-001.md,
    M tests/…/Field/Coarse/CoarseArtifactTests.cs, M tests/…/Tooling/GitBlobIdentityTests.cs, A tests/…/Tooling/GitCommittedArtifactGuard.cs.
  - ПОСЛЕДСТВИЕ для G5: «OK: all gates green» и «headless 1721/0/0 (baseline 1662 + 58)» померены на дереве БЕЗ этой
    починки ложно-зелёного гварда. Базлайн 1662 привязан к 1674e3ef, НЕ к актуальному main — на перебазированном дереве
    счёт будет другим, и это не расхождение. Структурно 86e7927f ортогонален Characters (Tooling + coarse gas-field),
    поэтому это НЕ дефект Leg 1 и НЕ повод блокировать G5.
  - Маршрутизация по правилам самого направления (knowledge/g9c41-lanes-venues.md): правило 4 («база уехала → пересогласовать»)
    — предполётное, билдер его на старте выполнил; правило 5 («следующий лег перебазируется» на мерж-слоте) — значит ребейз
    принадлежит МЕРЖ-СЛОТУ, не G5 и не этой сессии. G5 гоняется по замороженному кончику e64f070f.

  НАХОДКА 2 — ДРЕЙФ СОСТОЯНИЯ: В1 УЖЕ СМЁРЖЕН (first-hand):
  - git merge-base --is-ancestor db69aba6 origin/main → YES (В1-tip НА main); база В1 32107343 → тоже предок origin/main;
    git ls-tree origin/main Assets/GasCoopGame/Characters/ → BodyPose.cs, BodyReactions.cs, IAuthoritativeBodyState.cs,
    PlayerBodySocket.cs, ScriptedPathBodyState.cs, GasCoopGame.Characters.asmdef (+metas) — все В1-исходники на main.
    Продукт на v21 (validation.config), не v20.
  - А knowledge/g6d4e-char-v1-socket-delivered.md утверждает «**НЕ СМЁРЖЕН в main**» + «база origin/main@32107343
    (contract v20)». Владельческое «Вариант 1» (merge запущен отдельно) ДОЕХАЛО, запись — нет. Ложный факт в knowledge/
    отравил бы и G5-сессию, и будущее merge-решение ⇒ правится по first-hand доказательству (узко, только два факта).

  Точность формулировки (не дефект): билдер называет G4 «CROSS-FAMILY», но claude-opus-4-8 ↔ claude-sonnet-5 —
  кросс-МОДЕЛЬНО внутри ОДНОГО семейства. Язык направления это разделяет: В1-G5 Opus↔Opus записан как «SAME-FAMILY»
  с каветом, а routing (gascoopgame-engineering-model-routing) держит cross-family = Codex/GPT. ⇒ запрошенная Codex-G5
  будет ПЕРВЫМ независимым семейством на этом коде; просьба билдера обоснована.

  Дополнительно (в CALL, не блокер):
  - Assets/GasCoopGame/Characters.meta untracked — подтверждено, и ШИРЕ заявленного: git cat-file -e origin/main:…/Characters.meta
    → ОТСУТСТВУЕТ и на origin/main тоже. Т.к. В1 смёржен, папка без folder-meta уже НА MAIN ⇒ Unity генерит folder-meta
    с новым guid на каждой машине; будущий -Deliver споткнётся через DF-5. Пре-существующее, вне scope Leg 1.
  - Рабочее дерево p2a0_002 грязное локальным Unity/MCP-шумом (.vscode/settings.json, Assets/Plugins/NuGet/*,
    Packages/manifest.json, packages-lock.json, ProjectSettings/PackageManagerSettings.asset) — не часть лега, не коммичено.

  OS-репо / конкурентность:
  - Ветка wt/indie-game-development @3c45efc; дерево чисто кроме давнего dirty work/marketing/handle-reservation-inomand.md
    (сохранён, не стейжен). NOW.md перечитан свежим; NearGas/route-reset/runner состояния не тронуты.

state_changes: |
  - SET NOW.md.updated = «2026-07-14 by s-work-char-v2-leg1-return-g5-open-001».
  - NOW.md.open_calls: REMOVE c-exec-char-v2-reaction-core-build-001 (returned/consumed); ADD
    c-review-char-v2-reaction-core-g5-001 (to: session, for: g-6d4e/В2 Leg 1 binding G5, READY PARALLEL; note несёт
    истину чекпоинта: замороженный кончик @e64f070f, форк-база 1674e3ef, origin/main УЕХАЛ на 86e7927f (false-green
    guard fix, ортогонален Characters, ребейз = мерж-слот по правилу линий 5), сейм байт-идентичен, G4 без P0/P1
    (кросс-модельно, НЕ кросс-семейно), Leg 1 НЕ закрыт до G5, НЕ смёржен).
  - NOW.md.open_calls: UPDATE c-exec-char-v2-body-rig-ragdoll-build-001 (Leg 2) note — HELD теперь висит на
    c-review-char-v2-reaction-core-g5-001 (прежний id — build-CALL — consumed); runnable Leg 2 CALL выпускает G5-сессия
    при CONFIRMED. Статус HELD не меняется.
  - NOW.md.next: UNCHANGED = c-review-poligon-m1-route-reset-001 (хребет g-9c41 сохранён).
  - CREATE work/c-review-char-v2-reaction-core-g5-001-call.md (self-contained binding G5 CALL: заявки к опровержению
    (a)–(j) из done_when BUILD-CALL'а + spec §0 F1/§4/§6; обязателен first-hand прогон; обязателен разбор base-drift;
    read-only, никакого ребейза/мержа/пуша). END_OF_FILE trailer.
  - UPDATE knowledge/g6d4e-char-v1-socket-delivered.md — УЗКАЯ фактическая правка по first-hand git-доказательству:
    заголовок «(unmerged)» → «(MERGED в main 2026-07-14)»; §Где «НЕ СМЁРЖЕН в main / база v20» → «СМЁРЖЕН: db69aba6 —
    предок origin/main, В1-исходники на main, продукт на v21»; §Дальше — Leg 1 вернулся, ждёт G5. Ничего другого в файле
    не трогается (каветы/находки/В2/В3 сохранены как есть).
  - REGENERATE work/board/dashboard.html (declared owner panel; правила: knowledge/g9c41-lanes-venues.md §Панель +
    play local/lanes-board): stamp-строка, матричная строка Character V2 BUILD (🟢 READY PARALLEL → 🟢 СОБРАН · ждёт G5),
    трек-карточка Character, карточка открытых работ (build → G5 READY PARALLEL, с base-drift ⚠), журнал 14.07 (новая
    запись; окно ≤3 дней), строка «Контроллер игрока + камера» (В1 смёржен).
  - APPEND LOG.md line once; ADD this full RESULT to history/2026-07-14-s-work-char-v2-leg1-return-g5-open-001.md.
  - PRESERVE: TREE.md, CHARTER.md (g-6d4e остаётся outcome-level; В2/Leg 1 — волна, не TREE-нода → без G9-мутации);
    все g-9c41/NearGas/route-reset/runner/marketing open_calls и decisions; продуктовые репо (ничего не собрано, не
    перебазировано, не смёржено, не запушено); dirty work/marketing/handle-reservation-inomand.md — без стейджа.

captures:
  - Assets/GasCoopGame/Characters.meta отсутствует и на origin/main (не только на ветке) — папка без folder-meta уже в main
    после мержа В1 ⇒ per-machine guid-генерация + будущий -Deliver DF-5. Пре-существующее с В1; чинить отдельной мелкой ногой.
  - Ребейз Leg 1 на origin/main@86e7927f + полный check — работа мерж-слота (правило линий 5), не G5; всплывёт при
    merge-решении вместе с пре-существующим газовым L19-красным.
  - Терминология гейтов размывается: «cross-family» в продуктовом ревью означало кросс-МОДЕЛЬНО (Opus↔Sonnet). Стоит
    один раз зафиксировать словарь family vs model, чтобы G4/G5-каветы читались одинаково всеми сессиями.
  - G4 F2/F3 (P3, S3/S8: IsReady латчится при гейте; GetUp из Normal транзиентно ставит _held) — намеренные, но Leg 2
    обязан их знать: потребитель не должен читать IsReady==true как «поза синхронна с вводом».

decisions_needed: []

play_check:
  - 1 Recite: done — В2 Leg 1 (g-6d4e), done_when из work/c-exec-char-v2-reaction-core-build-001-call.md, spec
    work/c-plan-characters-002-plan.md §0 F1/§4/§6; трек параллельный, хребет g-9c41 остаётся №1.
  - 2 Owner inputs (owner): skipped — не owner-content: инженерный headless-лег, ничем не «живёт» владелец лично.
    Owner-eye для В2 приходит только в Leg 2 (engine + LOOK), здесь его нет по дизайну приёмки.
  - 3 Do the work: done — возврат проверен first-hand в продуктовом гите (ветка/коммиты/порядок/дельта/сейм/v21/доки/
    G4), найдены base-drift и knowledge-дрейф; связывающий G5-CALL выпущен (call:session).
  - 4 Self-check против done_when BUILD-CALL'а: done — #1 v21-SKIP ПОДТВЕРЖДЁН (стамп на базе, контракт-файлы не в дельте);
    #2/#3/#4 заявлены и подкреплены доками+коммит-порядком, но их СУТЬ (краснота, качество тестов, полнота obligation-set)
    — предмет G5, не моя сессия; #5 гейты — заявлены билдером, first-hand прогон = done_when G5 (+ поправка base-drift);
    #6 сейм байт-идентичен — ПОДТВЕРЖДЁН МНОЙ. Ни одна заявка не опровергнута; лег НЕ закрыт (G5 обязателен).
  - 5 Close: done — BUILD CALL consumed, G5 CALL открыт READY PARALLEL, Leg 2 остаётся HELD, merge не запускается,
    NOW.next не тронут.

log: 2026-07-14 — work/product-return (g-6d4e/В2 Leg 1, s-work-char-v2-leg1-return-g5-open-001): хендбэк Leg 1 (headless-ядро реакции + knockdown-aware источник, @e64f070f) зачтён evidence-чекпоинтом — first-hand подтверждены дельта из 10 файлов (все добавления), порядок RED→impl по коммитам, байт-идентичный сейм, v21 на базе (SKIP законен), 4 дока, G4 без P0/P1 и без неревьюенного источника. Две поправки к пакету билдера: (1) база уехала — origin/main@86e7927f «Fix Git artifact identity false-green guard», прямой ребёнок форка +8 мин, ⇒ gate-green и baseline 1662 померены без этой починки (ортогонален Characters; ребейз = мерж-слот, правило линий 5); (2) В1 УЖЕ смёржен в main и продукт на v21 — knowledge/ утверждал обратное, поправлено по git. Leg 1 НЕ закрыт, НЕ смёржен; BUILD CALL consumed; открыт связывающий fresh G5 c-review-char-v2-reaction-core-g5-001 (READY PARALLEL, Codex = первое независимое семейство: G4 был кросс-модельным Opus↔Sonnet); Leg 2 остаётся HELD; NOW.next не менялся. → history/2026-07-14-s-work-char-v2-leg1-return-g5-open-001.md

next: |
  READY PARALLEL (character track): work/c-review-char-v2-reaction-core-g5-001-call.md — связывающий свежий G5 на
  замороженный Leg 1 @e64f070f (отдельная сессия, cross-family Codex предпочтительно — это первое независимое семейство
  на этом коде; read-only; попытка ОПРОВЕРЖЕНИЯ + обязательный first-hand прогон + обязательный разбор base-drift).
  Только CONFIRMED закрывает Leg 1 и разблокирует Leg 2 — тогда G5-сессия выпускает runnable
  c-exec-char-v2-body-rig-ragdoll-build-001. При опровержении — repair-CALL, Leg 2 остаётся HELD.

  Глобальный NOW.next UNCHANGED (хребет): work/c-review-poligon-m1-route-reset-001-call.md (g-9c41).

END_OF_FILE: live/indie-game-development/history/2026-07-14-s-work-char-v2-leg1-return-g5-open-001.md
