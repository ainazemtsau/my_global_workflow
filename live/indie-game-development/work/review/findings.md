# Леджер находок дневного ревью — indie-game-development

updated: 2026-07-11 (s-daily-review-20260711-001 — первое ревью: 4 новые находки)
rules: plays/daily-review.md (находит — не чинит; дедуп обязателен; rejected не переоткрывать без новой причины)
format: | id | дата | класс night/repair/day/maintenance | P1-3 | факт (с file:line) | статус new/known/in-fix/fixed/rejected:<причина> |

## Открытые находки

| id | дата | класс | P | факт | статус |
|---|---|---|---|---|---|
| dr-20260711-001 | 2026-07-11 | repair | P1 | Product-routing врёт о committed-состоянии: `NOW.md:68` всё ещё фиксирует `dev@8fc25d90` и незакоммиченную запись round 8, тогда как после fetch `dev@5030696b` = 48 commits ahead `origin/main@a644e5db`, запись round 8 уже закоммичена, а `evidence/c-exec-lv-round9-stop@39021141` содержит движение round 9; `NOW.md:83` и `work/board/dashboard.html:198` называют P2a0 READY, но `lab@1a878226` уже на 1 commit впереди main с committed frozen PLAN. Дополнительно базы `work/c-exec-lv-ingest-phase0-call.md:4` и `work/c-shape-sc-damage-call.md:32` остаются `defade72`, хотя текущий product `origin/main` = `a644e5db`. Готовый repair-CALL: `c-repair-daily-product-routing-20260711-001` ниже. | new |
| dr-20260711-004 | 2026-07-11 | night | P1 | Канон-борд `C:\projects\gas_coop_game_canon\board\dashboard.html:110,206,301` всё ещё показывает бумажный research / открытый Gate Q, хотя сам же на `:154` помечает Gate Q пройденным, а `NOW.md:84-88` и `LOG.md:167,171` фиксируют уже выбранный paper-answer «Цель стоит запуска», ACCEPTED пилот процесса и открытый отдельный canon-admission CALL. Требуется только перегенерировать канон-борд из committed канона + frame-слоя OS; канон не менять. | new |
| dr-20260711-002 | 2026-07-11 | repair | P2 | Нарушена целостность state-history: `LOG.md:20-26` содержит 7 ссылок на отсутствующие history-paths (для 6 есть committed файлы под другими именами, для `s-work-047-df-backlog-sequencing` совпадение не найдено); 7 history-файлов не проходят точный EOF-трейлер — `history/2026-06-17-c-exec-005-t1-result.md`, `2026-06-18-c-exec-006-t2-result.md`, `2026-07-11-s-repair-minimum-game-frame-001.md`, `s-canon-between-expeditions-progression-001.md`, `s-canon-floor-gas-work-verbs-001.md`, `s-frame-005.md`, `s-repair-consolidate.md` (последний имеет укороченный путь в трейлере). Готовый repair-CALL: `c-repair-daily-history-integrity-20260711-001` ниже. | new |
| dr-20260711-003 | 2026-07-11 | night | P2 | 21 ссылка на 15 файлов висит в актуальных TREE/knowledge: `TREE.md:140-141,157,159`; `knowledge/g9c41-architecture-locked-slices.md:8,14`; `knowledge/g9c41-drift-guard.md:9`; `knowledge/g9c41-gas-engine-SPEC.md:213-223`; `knowledge/g9c41-wave2-aplus-over-b-code-grounded.md:7`. Четырнадцать целей фактически лежат в `work/archive/`, а `g9c41-drift-guard.md` — в `knowledge/`, но ссылки оставлены на несуществующие `work/...` пути. | new |

## Готовые repair-CALL

### dr-20260711-001 — committed product-routing

```markdown
CALL c-repair-daily-product-routing-20260711-001
to: session
direction: indie-game-development
play: repair
node: g-9c41  task: product-routing
goal: |
  NOW, действующие CALL-артефакты и панель образуют один точный committed-state маршрут
  для Phase 0 и P2a0, не закрывая ни одного недоказанного lifecycle-состояния.
context: |
  live/indie-game-development/NOW.md; work/board/dashboard.html;
  work/c-exec-lv-ingest-phase0-call.md; work/c-shape-sc-damage-call.md;
  finding dr-20260711-001. Product facts after fetch: origin/main@a644e5db;
  dev@5030696b (48 ahead); evidence/c-exec-lv-round9-stop@39021141;
  lab@1a878226 (1 ahead); old recorded bases/tips: defade72 and 8fc25d90.
boundaries: |
  Product repo is read-only. No merge, rebase, BUILD, review verdict, delivery claim,
  owner verdict or open_call closure. Preserve concurrent product work and every unrelated state field.
done_when: |
  Phase 0 remains explicitly NOT MERGED and P2a0 remains open; their exact committed tips and
  movement are represented without calling either delivered. Both defade72 base drifts have an
  explicit current disposition; no running CALL is silently restarted or erased. The owner panel
  matches the repaired NOW + committed git facts.
return: |
  RESULT with exact state/artifact diff, before/after refs and proof that product files were not changed.
budget: one session
surface: any
```

### dr-20260711-002 — LOG/history integrity

```markdown
CALL c-repair-daily-history-integrity-20260711-001
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
  а для s-work-047-df-backlog-sequencing совпадение не найдено. Семь history-файлов перечислены
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
  RESULT с таблицей 7 ссылок, 7 trailer-проверок, точной дельтой и отдельной строкой о нерешимом остатке.
budget: one session
surface: any
```

## Закрытые / отклонённые

(пусто)

END_OF_FILE: live/indie-game-development/work/review/findings.md
