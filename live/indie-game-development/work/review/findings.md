# Леджер находок дневного ревью — indie-game-development

updated: 2026-07-12 (s-daily-review-20260712-001 — 2 новые, 4 known; всего 6 открытых)
rules: plays/daily-review.md (находит — не чинит; дедуп обязателен; rejected не переоткрывать без новой причины)
format: | id | дата | класс night/repair/day/maintenance | P1-3 | факт (с file:line) | статус new/known/in-fix/fixed/rejected:<причина> |

## Открытые находки

| id | дата | класс | P | факт | статус |
|---|---|---|---|---|---|
| dr-20260711-001 | 2026-07-11 | repair | P1 | Product-routing по-прежнему не совпадает с committed-состоянием. `NOW.md:73` всё ещё фиксирует `dev@8fc25d90` и незакоммиченную запись round 8; после fetch `origin/main@a644e5db`, `dev@5f459a85` = 0 behind / 50 ahead, причём два коммита после общего с Phase-0 review-base `5030696b` добавляют незарегистрированный в NOW change `c-exec-near-gas-authority-stabilization-001`, а `evidence/c-exec-lv-round9-stop@39021141` расходится с dev от того же `5030696b`; Phase 0 не является ancestor main. `NOW.md:88,93` оставляет P2a0 на pre-builder checkpoint/READY от `a2d50c2a`, но product-ветка `codex/c-exec-player-puppetmaster-p2a0-002-build@b9aea60c` = 0 behind / 14 ahead и на два коммита дальше: committed RESULT остаётся `CHECKPOINT / NOT DELIVERED`, фиксирует import/readback и venue-blocker без G5/verdict/merge и просит route home. `knowledge/g9c41-lanes-venues.md:12` всё ещё называет старый `c-exec-player-puppetmaster-p2a0-001` в lab. Базы `work/c-exec-lv-ingest-phase0-call.md:4` и `work/c-shape-sc-damage-call.md:32` остаются `defade72`. Готовый repair-CALL: `c-repair-daily-product-routing-20260712-001` ниже. | known |
| dr-20260711-004 | 2026-07-11 | night | P1 | Канон-борд частично перегенерирован, но всё ещё противоречит committed канону `HEAD@324a30ed`: `INDEX.md:4`, `QUEUE.md` и `canon/c-001-investigation-readiness.md` фиксируют owner-вердикт `ADMIT TO CANON` и preliminary c-001, тогда как `board/dashboard.html:206,270` всё ещё называют ответ неканоническим, а `:302` говорит, что admission только открыт, рядом с корректной строкой `:303` о состоявшемся допуске. Требуется только перегенерировать канон-борд из CONSTITUTION/CORE/INDEX/QUEUE + frame-слоя OS; канон не менять. | known |
| dr-20260712-001 | 2026-07-12 | repair | P1 | Маршрут `c-marketing-wake-001` отстал от собственного committed checkpoint: `NOW.md:94-98` всё ещё говорит `READY` и отправляет запускаться от брифа 11.07, но `history/2026-07-12-s-marketing-wake-claude-handoff-001.md` и `work/marketing/claude-code-handoff-c-marketing-wake-001-2026-07-12.md` уже фиксируют INOMAND / `@inomandgames`, купленный домен и входящую accounts@, B1 strategy checkpoint и точное продолжение в Claude; Chinvat отменён, game title/Steam App/public accounts остаются открыты, исходный open_call не закрыт. Старый note может повторно запустить уже пройденный старт и вернуть отменённую идентичность. Готовый repair-CALL: `c-repair-daily-marketing-routing-20260712-001` ниже. | new |
| dr-20260712-002 | 2026-07-12 | repair | P1 | Принятое дословное требование владельца «до 8 игроков; дизайн-оптимум — 8; соло вне компетенции» живёт в `knowledge/g9c41-players-8-owner-requirement.md`, но активные `TREE.md:63,173` всё ещё говорят 2–4 / 1–4 и solo-startable, канон `CONSTITUTION.md:6` — 1–4 и solo-startable, а `NOW.md:101-104` содержит только решение d-m1 и не регистрирует поданные owner-gated формулировки. Панель показывает карточку, но панель не является state-authority; без явного pending route следующие shape/PLAN могут прочитать взаимоисключающие пределы. Готовый repair-CALL: `c-repair-daily-player-count-routing-20260712-001` ниже; TREE/канон без новых слов владельца не менять. | new |
| dr-20260711-002 | 2026-07-11 | repair | P2 | Нарушена целостность state-history: `LOG.md:20-26` содержит 7 ссылок на отсутствующие history-paths (для 6 есть committed файлы под другими именами, для `s-work-047-df-backlog-sequencing` совпадение не найдено); уже 8 history-файлов не проходят точный EOF-трейлер — прежние семь плюс `history/2026-07-11-s-board-walkthrough-decisions-001.md`, у которого addenda стоят после трейлера. Готовый repair-CALL: `c-repair-daily-history-integrity-20260712-001` ниже. | known |
| dr-20260711-003 | 2026-07-11 | night | P2 | Повторная committed-сверка подтверждает те же 21 ссылки на 15 отсутствующих target-paths в актуальных TREE/knowledge: `TREE.md:140-141,157,159`; `knowledge/g9c41-architecture-locked-slices.md:8,14`; `knowledge/g9c41-drift-guard.md:9`; `knowledge/g9c41-gas-engine-SPEC.md:213-223`; `knowledge/g9c41-wave2-aplus-over-b-code-grounded.md:7`. Четырнадцать целей фактически лежат в `work/archive/`, а `g9c41-drift-guard.md` — в `knowledge/`, но ссылки оставлены на несуществующие `work/...` пути. | known |

## Готовые repair-CALL

### dr-20260711-001 — committed product-routing

```markdown
CALL c-repair-daily-product-routing-20260712-001
to: session
direction: indie-game-development
play: repair
node: g-9c41  task: product-routing
goal: |
  Phase 0 и P2a0 имеют один точный committed-state маршрут без повторного запуска
  возвращённого checkpoint и без закрытия недоказанного lifecycle.
context: |
  live/indie-game-development/NOW.md; knowledge/g9c41-lanes-venues.md;
  work/board/dashboard.html; finding dr-20260711-001. Product facts after fetch:
  origin/main@a644e5db; dev@5f459a85 (0 behind / 50 ahead); Phase-0 evidence branch
  @39021141 diverges from dev after common @5030696b; P2a0 build branch @b9aea60c
  (0 behind / 14 ahead), cumulative RESULT remains CHECKPOINT / NOT DELIVERED and
  routes home after a venue blocker. Old recorded refs: dev@8fc25d90, checkpoint
  @a2d50c2a, old P2a0 call id 001, bases defade72.
boundaries: |
  Product repo is read-only. No merge, rebase, BUILD, review verdict, delivery claim,
  owner verdict or open_call closure. Product RESULT is evidence input, not Direction-OS close.
  Preserve concurrent product work and every unrelated state field.
done_when: |
  Phase 0 remains explicitly NOT MERGED/NOT DELIVERED and its divergent committed refs are
  represented without attributing the unrelated near-gas PLAN to it. P2a0 remains open without
  G5/verdict/merge claims, but the returned checkpoint, blocker and required Direction route are
  represented once; old 001/lab routing and both defade72 bases have explicit current dispositions.
  The owner panel matches repaired state + committed git facts.
return: |
  RESULT with exact state/artifact diff, before/after refs and proof that product files were not changed.
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

```markdown
CALL c-repair-daily-player-count-routing-20260712-001
to: session
direction: indie-game-development
play: repair
node: g-9c41  task: player-count-routing
goal: |
  Требование владельца «до 8 игроков, дизайн-оптимум 8, соло вне компетенции» имеет
  единый явный pending-owner маршрут, а старые пределы 1–4/2–4 не читаются как новый вердикт.
context: |
  knowledge/g9c41-players-8-owner-requirement.md; TREE.md:63,173;
  C:\projects\gas_coop_game_canon\CONSTITUTION.md:6; NOW.md; work/board/dashboard.html;
  history/2026-07-11-s-work-players8-knowledge-pin-001.md; finding dr-20260712-002.
boundaries: |
  Не менять TREE/CHARTER без фактических owner words и owner_approved (G9). Не менять канон
  без отдельного owner-verdict и его amendment-механизма. Не изобретать минимальный состав,
  сетевую архитектуру, дизайн коопа или M1 evidence; канон-репо до вердикта read-only.
done_when: |
  Все три конфликтующие живые формулировки перечислены; pending решение зарегистрировано в
  NOW.decisions с 2–3 вариантами и рекомендацией и имеет self-contained owner-present route.
  До реального verdict knowledge явно выигрывает как новое owner requirement, а TREE/канон
  остаются помеченными ожидающими согласования; панель совпадает с этим маршрутом.
return: |
  RESULT с точным решением/маршрутом, G9/canon guards и proof, что owner-gated тексты не менялись.
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
  а для s-work-047-df-backlog-sequencing совпадение не найдено. Восемь history-файлов перечислены
  в finding и не проходят точный trailer-check.
boundaries: |
  Не изобретать RESULT, evidence, owner words или потерянный history-контент. Не менять NOW/TREE/
  CHARTER/knowledge и не переписывать смысл LOG-строк; использовать только committed evidence.
done_when: |
  Каждая LOG-ссылка разрешается в существующий committed history-файл; каждый history-файл
  заканчивается точным `END_OF_FILE: live/indie-game-development/history/<name>.md`.
  Если единственный отсутствующий RESULT нельзя восстановить из committed evidence, возвратить
  точный BLOCKED checkpoint вместо fabricated history.
return: |
  RESULT с таблицей 7 ссылок, 8 trailer-проверок, точной дельтой и отдельной строкой о нерешимом остатке.
budget: one session
surface: any
```

## Закрытые / отклонённые

(пусто)

END_OF_FILE: live/indie-game-development/work/review/findings.md
