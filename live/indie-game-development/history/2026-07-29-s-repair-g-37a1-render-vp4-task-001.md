# RESULT s-repair-g-37a1-render-vp4-task-001

call: c-repair-g-37a1-render-vp4-task-001
direction: indie-game-development · track: t-render · play: repair · node/task: g-37a1/t-4
date: 2026-07-29

## outcome

У ядра теперь зафиксирован один расширяемый контур микротопологии, а не обещание «добавить
микровоксели потом»: engine-free Core хранит авторитетные состояния Solid/Empty и разреженную
маску только у Partial. VP4 остаётся производным заменяемым представлением этой маски.

Работа разложена без плотного solver на микроклетках: t-7 строит каноническую mask-delta,
snapshot/hash/reset и детерминированное копание; t-10 строит кэшированную газовую проекцию по
связным пустотам; t-11 проверяет настоящий VP4-чанк и несёт текущую visual responsibility.
Старый кооперативный CALL на `openedCells` заблокирован до перевыпуска по новому контракту.

## evidence

- Точные слова владельца о рекомендации: «Согласен полностью с той рекомендацией».
- Точные слова владельца на запись показанного batched diff: «Записывай этот diff».
- Предоставленный владельцем ответ Kronnect: per-microvoxel delta не выдаётся; рекомендуются
  `OnChunkChanged` + повторное чтение затронутой области; `GetMicroVoxels == null` неоднозначен для
  полного solid/empty; в latest beta обещаны geometry revision и `OnChunkGeometryApplied` после
  применения collider. Это вход для t-11, не доказательство установленного пакета.
- `work/voxel-play-4-backend-evaluation-2026-07-28-v2.md`: Core-grid/F3 — единственная игровая
  правда, VP4 — заменяемый backend; покупка и импорт не выполнены.
- До применения перечитаны свежие `NOW.md`, `TREE.md`, `CHARTER.md`, LOG tail, repair play и writer
  contract. Product repository не открывался для записи и не менялся.

## state_changes

```text
live/indie-game-development/NOW.md:
  updated -> s-repair-g-37a1-render-vp4-task-001
  bet.cut_list:
    прежний cut «микровоксели потом» заменён на принятый sparse Core contour и точные срезы:
    no dense world masks, no gas mass/solver per microcell, no VP4 authority,
    no micro-aware body collision in first Core; base block 0.5/1 m is versioned config.
  bet.lens_verdicts.l2_player_clarity -> t-11
  tasks.t-5: active -> blocked; old openedCells dependency revoked
  tasks.t-7: exact Solid -> Partial -> Empty sparse-mask contract, deterministic mask-delta,
    snapshot/reset/hash and conservative Partial-is-solid body rule
  tasks: + t-10 blocked on t-7 (cached gas projection and performance evidence)
  tasks: + t-11 blocked on t-7 + local VP4 + owner-selected slot (adapter + visual evidence)
  tracks.t-render.for: t-4 -> t-11
  open_calls: clear c-repair-g-37a1-render-vp4-task-001
  open_calls: + c-work-g-37a1-render-vp4-micro-adapter-001 blocked for t-11
  open_calls.c-exec-g-37a1-coop-two-machines-001: ready -> blocked; must be reissued after t-7
  issues: remove i-render-task-missing-after-vp4-decision-001; disposition: resolved by t-11,
    t-render reroute and the blocked render root recorded in this RESULT
  issues.i-gas-core-open-questions-001: point 3 form resolved; remaining tool speed/sequence and
    0.5/1 m measurement routed to t-7/t-10/t-11; points 1,2,4 remain open
  decisions: no hot answered row added. The accepted d-core-microtopology-001 meaning is preserved
    in this RESULT, LOG, cut_list and tasks; writer hygiene forbids answered decisions in NOW.

live/indie-game-development/work/:
  + c-work-g-37a1-render-vp4-micro-adapter-001-call.md

live/indie-game-development/LOG.md:
  + one newest-first row for this session

live/indie-game-development/history/:
  + 2026-07-29-s-repair-g-37a1-render-vp4-task-001.md

NOT TOUCHED:
  CHARTER.md, TREE.md, product repositories, purchase/import, unrelated task/call/issue meanings.
```

## captures

Нет.

## decisions_needed

Нет.

## play_check

- 1 name the contradiction: done — t-render указывала на закрытую decision-only t-4, а принятая
  микротопология делала старый `openedCells` coop contract и прежний microvoxel cut ложными.
- 2 reconstruct: done — newest-first сверены state, receipts, VP4 evaluation, ответ Kronnect и
  полный owner-dialogue; покупка/импорт/продуктовая совместимость не выдуманы.
- 3 propose corrected state: done — владельцу показан один ограниченный NOW/CALL diff с
  архитектурной границей, тремя задачами и честными blockers.
- 4 confirm (owner): done — сначала «Согласен полностью с той рекомендацией», затем точная команда
  на показанный пакет: «Записывай этот diff».
- 5 friction: skipped — нового OS-hole нет; no-hot-answered-decision и status hygiene являются
  уже действующими writer-правилами и применены как механическая нормализация без смены смысла.

log: repair g-37a1/t-4: owner approved sparse Core microtopology; t-7/t-10/t-11 own Core, gas projection and VP4 adapter, old openedCells coop root blocked

next: |
  return-to-owner — t-render/t-11 законно blocked до трёх фактов: t-7 завершена, VP4 доступен
  локально, владелец выбрал свободный product slot. Никакой product CALL сейчас не dispatchится.

END_OF_FILE: live/indie-game-development/history/2026-07-29-s-repair-g-37a1-render-vp4-task-001.md
