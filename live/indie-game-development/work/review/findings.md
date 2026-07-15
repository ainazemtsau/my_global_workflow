# Леджер находок дневного ревью — indie-game-development

updated: 2026-07-15 (s-work-near-gas-l1-experimental-close-001 — 6 открытых: 1 new, 5 known; dr-20260712-002 fixed)
rules: plays/daily-review.md (находит — не чинит; дедуп обязателен; rejected не переоткрывать без новой причины)
format: | id | дата | класс night/repair/day/maintenance | P1-3 | факт (с file:line) | статус new/known/in-fix/fixed/rejected:<причина> |

## Открытые находки

| id | дата | класс | P | факт | статус |
|---|---|---|---|---|---|
| dr-20260711-001 | 2026-07-11 | repair | P1 | **Новая причина 13.07, тот же P2a0/launch drift:** `NOW.md:85-99` теперь ставит M1-P2a0 `done`, хотя неизменённый done_when требует bounded-C и fresh G5, а note и `history/2026-07-13-s-map-characters-track-p2a0-close-001.md` прямо фиксируют, что оба не доставлены и owner-eye использован вместо fresh G5; это противоречит `KERNEL.md` G5 и `knowledge/g9c41-lanes-venues.md:24` («ворота не срезаются никогда»). Та же карта всё ещё держит старый P2a0 call 001 и «Phase 0 in flight» (`:12-13`), а панель оставляет старый merge-gate источников; `work/c-shape-sc-damage-call.md:32` всё ещё запускается от `defade72`. Phase 0 повторно не открывать; нужен узкий lifecycle/lanes repair. | known |
| dr-20260711-004 | 2026-07-11 | night | P1 | **Player-count half disposed 15.07; admission/render drift remains:** current canon-board now presents Minimum Game Frame v2, the exact current pillar-1 player-count norm and explicit SUPERSEDED labels on the retained Frame-v1 map/matrix. The remaining P1 under this ID is separate: INDEX/QUEUE/card c-001 and several board statements still disagree about the completed `ADMIT TO CANON` state. A future bounded canon-board regeneration owns that remainder; canon content itself is not changed by this finding. | known |
| dr-20260712-001 | 2026-07-12 | repair | P1 | Маршрут `c-marketing-wake-001` отстал от собственного committed checkpoint: `NOW.md:127-131` всё ещё говорит `READY` и отправляет запускаться от брифа 11.07, но `history/2026-07-12-s-marketing-wake-claude-handoff-001.md` и `work/marketing/claude-code-handoff-c-marketing-wake-001-2026-07-12.md` уже фиксируют INOMAND / `@inomandgames`, купленный домен и входящую accounts@, B1 strategy checkpoint и точное продолжение в Claude; Chinvat отменён, game title/Steam App/public accounts остаются открыты, исходный open_call не закрыт. Старый note может повторно запустить уже пройденный старт и вернуть отменённую идентичность. Готовый repair-CALL: `c-repair-daily-marketing-routing-20260712-001` ниже. | known |
| dr-20260714-001 | 2026-07-14 | repair | P1 | Первичный `NOW.next` указывает на `work/c-review-poligon-m1-route-reset-001-call.md`, но его committed context `:26-27` всё ещё называет живым старый `PLAN-AMEND/Re-sync v20→v21` маршрут. Текущая truth уже иная: NearGas L1a DELIVERED исключительно по owner-authorized experimental skeleton→independent RED→BUILD→fresh-refutation carrier; product remote `dev`/`main` = `400ef8eca1e747378493c97530770286c7e26ff1`, binding fresh G5 PASS, старый v22 packet/carrier retired и forbidden, B1 является отдельной maintenance, L1b — отдельной product leg. Пакет просит owner выбрать следующую ставку и не должен переоткрывать L1a или предъявлять старый blocker. Готовый repair-CALL: `c-repair-daily-primary-review-packet-20260714-001` ниже. | new |
| dr-20260711-002 | 2026-07-11 | repair | P2 | Нарушена целостность state-history: `LOG.md` содержит те же 7 ссылок на отсутствующие history-paths (для 6 есть committed файлы под другими именами, для `s-work-047-df-backlog-sequencing` совпадение не найдено). Точный committed trailer-check теперь даёт 7, а не 8 misses среди 336 state markdown files: `history/2026-07-11-s-board-walkthrough-decisions-001.md` уже заканчивается корректным трейлером; остальные семь перечислены в repair-CALL ниже. Готовый repair-CALL: `c-repair-daily-history-integrity-20260712-001`. | known |
| dr-20260711-003 | 2026-07-11 | night | P2 | Повторная committed-сверка подтверждает те же 21 ссылки на 15 отсутствующих target-paths в актуальных TREE/knowledge: `TREE.md:147-148,164,166`; `knowledge/g9c41-architecture-locked-slices.md:8,14`; `knowledge/g9c41-drift-guard.md:9`; `knowledge/g9c41-gas-engine-SPEC.md:213-223`; `knowledge/g9c41-wave2-aplus-over-b-code-grounded.md:7`. Четырнадцать целей фактически лежат в `work/archive/`, а `g9c41-drift-guard.md` — в `knowledge/`, но ссылки оставлены на несуществующие `work/...` пути. | known |

## Готовые repair-CALL

### dr-20260711-001 — P2a0 lifecycle + lanes routing

```markdown
CALL c-repair-daily-p2a0-lanes-routing-20260713-001
to: session
direction: indie-game-development
play: repair
node: g-9c41  task: p2a0-lanes-routing
goal: |
  Lifecycle P2a0 и карта площадок имеют одно непротиворечивое состояние, которое
  не подменяет обязательный fresh G5 owner-eye вердиктом и не возвращает Phase 0.
context: |
  live/indie-game-development/NOW.md:81-99; knowledge/g9c41-lanes-venues.md:10-24;
  history/2026-07-13-s-map-characters-track-p2a0-close-001.md;
  work/c-shape-sc-damage-call.md; work/board/dashboard.html; finding dr-20260711-001.
  Current state marks M1-P2a0 done while its unchanged done_when still requires bounded-C
  and fresh G5; the close RESULT says both were not delivered. Lanes still name P2a0 call 001
  and Phase 0 in flight; the panel still carries the old sources merge-gate.
boundaries: |
  Product repo is read-only. Не изобретать новый owner verdict, G5, delivery evidence или
  waiver; owner-eye не называть fresh G5. Не возобновлять Phase 0, не запускать BUILD,
  не менять канон и не трогать unrelated state.
done_when: |
  P2a0 status/evidence satisfy the written done_when and KERNEL G5 or stay pending with the
  exact missing gate named; no owner-eye substitution remains. Lanes C/D and the panel no longer
  claim old P2a0/Phase-0 work is live; `defade72` has an explicit current disposition. Phase 0
  remains NOT DELIVERED / NEVER RESUME, and the owner panel matches the repaired state.
return: |
  RESULT with exact lifecycle/lanes/panel delta and proof that product and canon files were not changed.
budget: one session
surface: any
```

### dr-20260712-001 — marketing checkpoint routing

```markdown
CALL c-repair-daily-marketing-routing-20260712-001
to: session
direction: indie-game-development
play: repair
node: g-2f8c  task: marketing-routing
goal: |
  Живой маршрут c-marketing-wake-001 начинается от committed INOMAND checkpoint и
  сохраняет точный открытый остаток без повторения уже завершённого старта.
context: |
  live/indie-game-development/NOW.md; work/marketing/claude-code-handoff-c-marketing-wake-001-2026-07-12.md;
  history/2026-07-12-s-marketing-wake-claude-handoff-001.md; work/board/dashboard.html;
  finding dr-20260712-001.
boundaries: |
  Не закрывать c-marketing-wake-001, не замораживать q-channels, не выбирать название игры,
  не создавать Steam App/аккаунты, не публиковать, не тратить деньги и не выполнять сам маркетинг.
done_when: |
  NOW note и панель называют INOMAND/@inomandgames, готовый substrate+B1 checkpoint,
  authoritative handoff и точный открытый остаток; Chinvat и старт-с-нуля не выглядят живым маршрутом;
  open_call остаётся pending и указывает на self-contained продолжение из checkpoint.
return: |
  RESULT с before/after маршрутом, точными сохранёнными границами и подтверждением отсутствия публичных действий.
budget: one session
surface: any
```

### dr-20260712-002 — owner requirement «до 8»

CLOSED / FIXED by
`s-repair-eight-player-live-consistency-sweep-001`.
The obsolete proposed
`c-repair-daily-player-count-routing-20260712-001`
remains non-runnable and must not be launched.

### dr-20260714-001 — stale primary M1 review packet

```markdown
CALL c-repair-daily-primary-review-packet-20260714-001
to: session
direction: indie-game-development
play: repair
node: g-9c41  task: primary-review-packet
goal: |
  Первичный M1 review-пакет снова самодостаточен и сообщает текущую committed planning truth,
  не меняя уже принятую цель review или требуя от владельца повторять прежние решения.
context: |
  live/indie-game-development/NOW.md;
  work/c-review-poligon-m1-route-reset-001-call.md:26-27;
  work/c-exec-near-gas-core-authority-001-plan-amend-v22-003-call.md (SUPERSEDED / NEVER ISSUE);
  history/2026-07-15-s-work-near-gas-l1-experimental-close-001.md;
  finding dr-20260714-001.
  NearGas L1a is DELIVERED through the owner-authorized experimental carrier. Product remote
  dev/main are exact 400ef8eca1e747378493c97530770286c7e26ff1; binding fresh G5 is PASS.
  The old v22 packet/carrier is retired and forbidden. B1 is separate maintenance; L1b is separate.
boundaries: |
  Не запускать сам review, не выносить verdict за владельца, не закрывать/продлевать ставку и не
  открывать executor/RED/BUILD CALL. Не переоткрывать L1a, не восстанавливать старый v22 packet/carrier
  и не выполнять B1/L1b внутри repair. Не менять принятый no-cap route, 24.07 control-review,
  product/canon/TREE/CHARTER или unrelated open_calls. Product и canon read-only.
done_when: |
  `work/c-review-poligon-m1-route-reset-001-call.md` сохраняет исходные goal/done_when/owner-verdict
  guards, но его context называет L1a DELIVERED @400ef8ec, experimental carrier, retired/forbidden old
  route, separate B1 maintenance и separate L1b alongside current Level/DA/PGG, character and frame
  blockers. `NOW.next` остаётся тем же pointer; панель совпадает с repaired packet. Никакой review
  verdict или downstream CALL не создан.
return: |
  RESULT с before/after packet truth, сохранёнными review guards и proof отсутствия product/canon mutation.
budget: one session
surface: any
```

### dr-20260711-002 — LOG/history integrity

```markdown
CALL c-repair-daily-history-integrity-20260712-001
to: session
direction: indie-game-development
play: repair
node: g-9c41  task: history-integrity
goal: |
  LOG и history снова образуют полностью разрешимый журнал, а каждый history-файл имеет точный
  END_OF_FILE-трейлер без изменения исторического смысла.
context: |
  live/indie-game-development/LOG.md:20-26; history/; finding dr-20260711-002.
  Семь LOG-paths отсутствуют; шесть похожих committed history-файлов имеют более длинные имена,
  а для s-work-047-df-backlog-sequencing совпадение не найдено. Семь history-файлов не проходят
  точный trailer-check: 2026-06-17-c-exec-005-t1-result, 2026-06-18-c-exec-006-t2-result,
  2026-07-11-s-repair-minimum-game-frame-001, s-canon-between-expeditions-progression-001,
  s-canon-floor-gas-work-verbs-001, s-frame-005 и s-repair-consolidate.
boundaries: |
  Не изобретать RESULT, evidence, owner words или потерянный history-контент. Не менять NOW/TREE/
  CHARTER/knowledge и не переписывать смысл LOG-строк; использовать только committed evidence.
done_when: |
  Каждая LOG-ссылка разрешается в существующий committed history-файл; каждый history-файл
  заканчивается точным `END_OF_FILE: live/indie-game-development/history/<name>.md`.
  Если единственный отсутствующий RESULT нельзя восстановить из committed evidence, возвратить
  точный BLOCKED checkpoint вместо fabricated history.
return: |
  RESULT с таблицей 7 ссылок, 7 trailer-проверок, точной дельтой и отдельной строкой о нерешимом остатке.
budget: one session
surface: any
```

## Закрытые / отклонённые

| id | дата | класс | P | факт | статус |
|---|---|---|---|---|---|
| dr-20260713-001 | 2026-07-14 | repair | P1 | Repair `s-repair-daily-engineering-v21-routing-20260714-001` представил `execute-002@5c783e07` ровно один раз как returned checkpoint / NOT DELIVERED в canonical task note, убрал его из `open_calls` и `NOW.next`, оставил runner/character HELD для их собственной full-packet проверки и открыл единственный NearGas-маршрут `c-exec-near-gas-core-authority-001-plan-amend-resync-002` на contract-only v20→v21 Re-sync, полный semantic whole-packet dry-run и отдельную fresh Direction binding review; удалённые mechanical draft requirements не перенесены. | fixed |
| dr-20260712-002 | 2026-07-12 | repair | P1 | 15.07 Frame v2, g-d3a8, canon law, active g-9c41 player-count and owner-facing player-count renders received one explicit disposition: primary range 4–8, full eight mandatory, lower bound below four OPEN, solo not current target. Clean 1-player, 2+ client, two-machine and two-human grey-box checks remain engineering/test hygiene. g-5b07 remains parked with an explicit wake condition and owner. Historical evidence was not rewritten. | fixed |

END_OF_FILE: live/indie-game-development/work/review/findings.md
