# CALL c-review-char-v1-socket-dropin-g5-001

- id: c-review-char-v1-socket-dropin-g5-001
- to: session (fresh, separate — binding G5; cross-family Codex preferred per this direction's VALIDATE routing; read-only)
- for: g-6d4e «Игровые персонажи» / В1 — связывающий G5 на уже собранный socket + drop-in build
- issued: 2026-07-14 by s-repair-char-v1-held-reconcile-001
- play: review

## goal (outcome, not method)

У В1 есть связывающий G5-вердикт: свежая ОТДЕЛЬНАЯ сессия попыталась ОПРОВЕРГНУТЬ заявки собранного В1-билда и
не смогла (или вернула, что именно опровергла и чем). Owner-eye уже зелёный — это его вторая половина ворот.
После зелёного G5 В1 = done и открывается В2; merge в main остаётся решением направления.

## context

- Билд (единственный источник истины — читать в продукте, НЕ изобретать): worktree
  C:\projects\Unity\GasCoopGame_p2a0_002, ветка `c-exec-char-v1-socket-dropin-build-001`
  @db69aba6847a47ce2544ad1314f3567b327805d7, база продукта origin/main@32107343 (contract v20, 9 коммитов над базой).
  RESULT-док: docs/results/c-exec-char-v1-socket-dropin-build-001.md; ADR: docs/adr/ADR-E-0012-c-exec-char-v1-socket-dropin-build-001-authoritative-body-pose-socket.md;
  owner-eye walkthrough: docs/character-v1-b1-owner-eye.md.
- Заявки В1 для опровержения (взяты из done_when исходного BUILD CALL — work/c-exec-char-v1-socket-dropin-build-001-call.md):
  (a) спавн ставит управляемого игрока; (b) префаб потребляет инъектированный источник позы (pull-модель через
  `IAuthoritativeBodyState`); (c) смена реализации источника двигает игрока БЕЗ правки префаба/сцен; (d) drop-in во
  2-ю пустую сцену композится без допнастройки; (e) reaction/knockdown/getup — объявленные no-op хуки (В2 заполнит);
  (f) стабильность сейма — позже позиция ядра g-9c41 встаёт в тот же разъём без правки префаба/сцен.
- Frozen PLAN + В1 spec (authority): C:\my_global_workflow_worktrees\indie-game-development\live\indie-game-development\work\c-plan-characters-001-plan.md.
- Owner-context: владелец сам направлял этот билд в owner-directed p2a0-worktree и прошёл owner-eye (owner-run PlayMode,
  3 сцены) — вердикт «Вариант 1». HELD с character-трека снят на этом вердикте.
- Внутренний билдерский кросс-модельный ревью (НЕ связывающий): нет P1/P2; 1 P2 (NaN в public API `ScriptedPathBodyState`)
  починен red-first (коммиты a65389b2 → d6554674); 2 P3 → В3 (ADR Deferred).

## boundaries (out of scope / do not touch)

- ТОЛЬКО ЧТЕНИЕ продукта: ничего не собирать, не править source/tests, не мержить, не пушить. Unity/MCP запускать не
  требуется (owner-eye уже сделан владельцем); если для проверки заявки нужен недоступный инструмент — STOP + сказать
  владельцу, без костылей.
- G5 обязана быть ОТДЕЛЬНОЙ свежей сессией (KERNEL G5), НЕ той, что писала билд. Cross-family (Codex) — по routing
  направления; жёсткое требование — свежесть сессии, не семейство модели.
- Не закрывать В1 и не открывать В2 без реального G5-вердикта. Merge в main — решение направления, НЕ этой сессии.
- Не трогать GasCoopGame_dev / GasCoopGame_core (foreign uncommitted работа).
- Предсуществующий газовый красный `L19_T2AndT3Artifacts_RemainByteUntouched` (golden-digest на origin/main) — НЕ дефект
  В1: доказано byte-identical к origin/main, чинится в gas-track и не блокирует срез В1.

## done_when (verifiable)

1. Свежая отдельная сессия прочитала билд first-hand (ветка @db69aba6) и попыталась опровергнуть каждую заявку (a)–(f);
   вернула по каждой: опровергнуто / не опровергнуто, с доказательством (тест / код / наблюдение).
2. Прогон независимых приёмочных тестов подтверждён зелёным first-hand (headless .NET), а не по словам билдера
   (39 Characters-тестов: 34 приёмочных + 5 hardening).
3. Явный связывающий вердикт: В1 CONFIRMED (заявки не опровергнуты) — либо список реальных опровержений → repair-CALL.
4. Возврат домой: RESULT с G5-вердиктом; при CONFIRMED — рекомендация открыть В2 и оставить merge решением направления
   (продукт всё ещё v20; при merge направление отдельно решает по предсуществующему газовому L19-красному и чистому -Deliver).

## return

RESULT (review): связывающий G5-вердикт по В1 + first-hand доказательства по каждой заявке; при зелёном — В1 done +
ready В2 CALL (тело: риг + процедурная локомоция + реакция/нокдаун/вставание в no-op хуках + косметический
PuppetMaster рэгдолл, через ТОТ ЖЕ сейм) и merge-решение направлению; при красном — repair-CALL с конкретными
опровержениями и без открытия В2.

## budget

Одна свежая review-сессия (можно MacBook; пайплайнится параллельно другим трекам направления).

END_OF_FILE: live/indie-game-development/work/c-review-char-v1-socket-dropin-g5-001-call.md
