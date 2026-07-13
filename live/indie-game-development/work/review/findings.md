# Леджер находок дневного ревью — indie-game-development

updated: 2026-07-13 (s-daily-review-20260713-001 — 1 new, 6 known; всего 7 открытых)
rules: plays/daily-review.md (находит — не чинит; дедуп обязателен; rejected не переоткрывать без новой причины)
format: | id | дата | класс night/repair/day/maintenance | P1-3 | факт (с file:line) | статус new/known/in-fix/fixed/rejected:<причина> |

## Открытые находки

| id | дата | класс | P | факт | статус |
|---|---|---|---|---|---|
| dr-20260711-001 | 2026-07-11 | repair | P1 | **Новая причина 13.07, тот же P2a0/launch drift:** `NOW.md:85-99` теперь ставит M1-P2a0 `done`, хотя неизменённый done_when требует bounded-C и fresh G5, а note и `history/2026-07-13-s-map-characters-track-p2a0-close-001.md` прямо фиксируют, что оба не доставлены и owner-eye использован вместо fresh G5; это противоречит `KERNEL.md` G5 и `knowledge/g9c41-lanes-venues.md:24` («ворота не срезаются никогда»). Та же карта всё ещё держит старый P2a0 call 001 и «Phase 0 in flight» (`:12-13`), а панель оставляет старый merge-gate источников; `work/c-shape-sc-damage-call.md:32` всё ещё запускается от `defade72`. Phase 0 повторно не открывать; нужен узкий lifecycle/lanes repair. | known |
| dr-20260711-004 | 2026-07-11 | night | P1 | Канон-борд частично перегенерирован, но всё ещё противоречит committed канону `HEAD@324a30ed`: `INDEX.md:4`, `QUEUE.md` и `canon/c-001-investigation-readiness.md` фиксируют owner-вердикт `ADMIT TO CANON` и preliminary c-001, тогда как `board/dashboard.html:206,270` всё ещё называют ответ неканоническим, а `:302` говорит, что admission только открыт, рядом с корректной строкой `:303` о состоявшемся допуске. Требуется только перегенерировать канон-борд из CONSTITUTION/CORE/INDEX/QUEUE + frame-слоя OS; канон не менять. | known |
| dr-20260712-001 | 2026-07-12 | repair | P1 | Маршрут `c-marketing-wake-001` отстал от собственного committed checkpoint: `NOW.md:127-131` всё ещё говорит `READY` и отправляет запускаться от брифа 11.07, но `history/2026-07-12-s-marketing-wake-claude-handoff-001.md` и `work/marketing/claude-code-handoff-c-marketing-wake-001-2026-07-12.md` уже фиксируют INOMAND / `@inomandgames`, купленный домен и входящую accounts@, B1 strategy checkpoint и точное продолжение в Claude; Chinvat отменён, game title/Steam App/public accounts остаются открыты, исходный open_call не закрыт. Старый note может повторно запустить уже пройденный старт и вернуть отменённую идентичность. Готовый repair-CALL: `c-repair-daily-marketing-routing-20260712-001` ниже. | known |
| dr-20260712-002 | 2026-07-12 | repair | P1 | Принятое дословное требование владельца «до 8 игроков; дизайн-оптимум — 8; соло вне компетенции» живёт в `knowledge/g9c41-players-8-owner-requirement.md`, но активные `TREE.md:70,180` всё ещё говорят 2–4 / 1–4 и solo-startable, канон `CONSTITUTION.md:6` — 1–4 и solo-startable, а `NOW.md:134-137` содержит только решение d-m1 и не регистрирует поданные owner-gated формулировки. Панель показывает карточку, но панель не является state-authority; без явного pending route следующие shape/PLAN могут прочитать взаимоисключающие пределы. Готовый repair-CALL: `c-repair-daily-player-count-routing-20260712-001` ниже; TREE/канон без новых слов владельца не менять. | known |
| dr-20260713-001 | 2026-07-13 | repair | P1 | `NOW.md:19-25,44,75-80,107-111,138-139` и панель называют `c-exec-near-gas-core-authority-001-execute-002` готовым новым EXECUTE, но fetched product-ветка уже имеет committed checkpoint `5c783e07` (0 behind / 1 ahead от `origin/main@32107343`): `docs/results/c-exec-near-gas-core-authority-001.md` фиксирует второй `SPEC-ONLY RED BLOCKED / NOT DELIVERED`, девять групп недостающих executable bindings и отсутствие test commit/implementation/gates. Одновременно OS current contract = v21, product `validation.config` = v20, а NearGas CALL `:3-10,35,92` не содержит обязательных v21 transaction identity/receipt полей (worktree/branch/base-authority/acceptance/run/TESTABILITY). Runner CALL остаётся v19, его `7a3e747` не разрешается fetched refs. После concurrent committed rebase `93d3f44` новый `c-exec-char-v1-socket-dropin-build-001` также помечен READY (`NOW.md:122-126`), но его artifact оформлен pseudo-полями, предлагает выбрать clean worktree/branch позже и не содержит обязательной v21 identity/receipts. Текущий `NOW.next` указывает на returned CALL; все три engineering route mechanically non-dispatchable. Готовый repair-CALL: `c-repair-daily-engineering-v21-routing-20260713-001` ниже. | new |
| dr-20260711-002 | 2026-07-11 | repair | P2 | Нарушена целостность state-history: `LOG.md:20-26` содержит 7 ссылок на отсутствующие history-paths (для 6 есть committed файлы под другими именами, для `s-work-047-df-backlog-sequencing` совпадение не найдено); уже 8 history-файлов не проходят точный EOF-трейлер — прежние семь плюс `history/2026-07-11-s-board-walkthrough-decisions-001.md`, у которого addenda стоят после трейлера. Готовый repair-CALL: `c-repair-daily-history-integrity-20260712-001` ниже. | known |
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

### dr-20260713-001 — engineering v21 routing

```markdown
CALL c-repair-daily-engineering-v21-routing-20260713-001
to: session
direction: indie-game-development
play: repair
node: g-9c41  task: engineering-v21-routing
goal: |
  NearGas, runner и character BUILD имеют правдивые pending-маршруты, а ни один returned
  или несовместимый с v21 EXECUTE/BUILD не обозначен как готовый к запуску.
context: |
  live/indie-game-development/NOW.md; os/engineering/CONTRACT_VERSION;
  os/adapters/coding-agent.md Role 1 v21; work/c-exec-near-gas-core-authority-001-execute-002-call.md;
  work/c-exec-unity65-mac-revision-002-build-001-call.md;
  work/c-exec-char-v1-socket-dropin-build-001-call.md; work/board/dashboard.html;
  finding dr-20260713-001. Product after fetch: origin/main@32107343; execute-002@5c783e07
  (0 behind / 1 ahead), committed RESULT = SPEC-ONLY RED BLOCKED / NOT DELIVERED with nine
  missing binding groups; product synced contract 20, OS current 21. Runner commits 7a3e747/8a344e9
  do not resolve from fetched refs. Concurrent committed state @93d3f44 adds character BUILD as READY,
  but that CALL also lacks the complete v21 identity/handoff.
boundaries: |
  Product repo is read-only. Не менять frozen PLAN/spec/tasks/ADR/TESTABILITY, не запускать RED,
  implementation, gates, Unity, merge или push; не закрывать NearGas-L1-BUILD и не изобретать v21 hashes,
  worktree/ref availability или delivery evidence.
done_when: |
  execute-002 checkpoint @5c783e07 represented once and its returning open_call is not runnable;
  NearGas task remains open with all nine binding groups and v21 re-sync/full-sweep prerequisite named.
  Every registered engineering continuation is either a schema-valid current-contract CALL that passes
  its applicable dispatch precondition, or explicitly non-runnable with the exact missing committed fact;
  runner uncertainty and the character BUILD are not labeled READY without that proof. NOW.next and the
  owner panel match that routing.
return: |
  RESULT with exact before/after routing, valid CALL artifacts if any, and read-only product proof.
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
  knowledge/g9c41-players-8-owner-requirement.md; TREE.md:70,180;
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
