# RESULT s-work-g-37a1-venue-packaged-player-plan-reset-001

call: owner verdict replacing `c-exec-g-37a1-venue-packaged-player-001`
direction: indie-game-development · track: t-venue · play: work · node/task: g-37a1/t-3
date: 2026-07-30

## outcome

Текущая audit-grade линия packaged player остановлена после binding PAIR-FREEZE rejection и больше не является
dispatchable Direction-root. Существующий PAIR-CANDIDATE не ремонтируется и не получает BUILD authority; все его
PLAN/pair/review/receipt/commit artifacts сохраняются без удаления как историческое evidence.

Вместо неё выпущен отдельный ready CALL `c-exec-g-37a1-venue-packaged-player-minimal-002` с новым product change id,
явным pin `engineering_contract: 31`, слотом WIN-U3 и Target Local. Его первая сессия — строго PLAN-only: она пишет
только новый план, не меняет production code/tests/tools, предъявляет план владельцу и останавливается для owner
approval.

Новый scope требует одну Windows-сборку, минимально полный bundle, ровно один запуск `.exe` без аргументов, видимое
рабочее окно, отсутствие немедленного падения, нормальное закрытие и успешный exit code. Старый audit-grade слой
срезан до обычных отказов; stale-success-marker закрывается удалением временного результата перед сборкой и созданием
успешного маркера только после полностью успешной сборки.

t-3 остаётся active. Этот узкий root намеренно не доказывает сохранённое task-требование повторного запуска/M7 и сам
по себе не может закрыть t-3. CHARTER, TREE, bet, tasks, tracks и WIP limit не меняются.

## evidence

- Owner verdict этого leg: “Текущую audit-grade задачу после PAIR-FREEZE rejection на commit
  2a66cd10756ae17dff709a85d2e6f499f31e3dd4 не продолжать и существующий PAIR-CANDIDATE не ремонтировать. Сохранить
  историю без удаления и остановить/заменить текущую линию.”
- Owner routing: “Выпустить новый отдельный PLAN-only CALL, engineering contract 31, в WIN-U3, Target Local, с новым
  change id.”
- Owner execution boundary: один build и один `.exe` launch без аргументов; видимое рабочее окно; no immediate crash;
  normal close; successful process exit; перечисленные обычные fail outcomes остаются.
- Owner cuts: “Исключить: два запуска, сравнение кадров, независимые builder/validator evidence sets, защиту от
  намеренной подделки доказательств, actor/capture provenance, полный environment fingerprint, PlayerPrefs provenance,
  47-path authority binding, before/between/after bundle byte snapshots и сложный rollback.”
- Owner stale-marker rule: “очищать временный результат перед сборкой и создавать признак успеха только после
  полностью успешной сборки.”
- Owner planning boundary: “Планировочная сессия не пишет production code, tests или tools и останавливается для owner
  approval.”
- Fresh Direction state before apply: g-37a1 active; t-3 active; t-venue exists; old root
  `c-exec-g-37a1-venue-packaged-player-001` was the sole ready call in that lane.
- Read-only product evidence at WIN-U3: rejection commit `2a66cd10756ae17dff709a85d2e6f499f31e3dd4` adds
  `docs/measurements/c-exec-g-37a1-venue-packaged-player-001-pair-freeze-r1-refutation.json` and
  `docs/reviews/pair-freeze-c-exec-g-37a1-venue-packaged-player-001-r1.md`; the refutation records
  `PAIR_FREEZE_RETRY_1_REFUTATION_BLOCKED`, `NOT_ELIGIBLE_FOR_BUILD`, and no PAIR-FREEZE receipt.
- The rejected package remains tied to change id `c-exec-g-37a1-venue-packaged-player-001`; the new self-contained CALL
  uses distinct change id `c-exec-g-37a1-venue-packaged-player-minimal-002`.
- Current Direction default is contract 34, but KERNEL authority order gives the owner's live exact pin-31 ruling
  precedence for this bounded same-lane replacement. The CALL records the explicit owner override rather than silently
  upgrading the requested pin.
- New CALL artifact:
  `live/indie-game-development/work/c-exec-g-37a1-venue-packaged-player-minimal-002-call.md`.

No Unity process, Editor, MCP action, product write, test, build, executable launch, network action or old-candidate
repair was performed in this Direction leg.

## state_changes

1. `NOW.md` — set `updated` to 2026-07-30 by this session.
2. `NOW.md.open_calls` — remove `c-exec-g-37a1-venue-packaged-player-001`; register
   `c-exec-g-37a1-venue-packaged-player-minimal-002` as the sole `ready` root in `t-venue`, serving t-3, with the
   rejection/no-repair/PLAN-only note. Preserve all unrelated calls, lanes, tasks, issues, decisions and forecast.
3. Add the complete CALL
   `work/c-exec-g-37a1-venue-packaged-player-minimal-002-call.md`; do not modify or delete the old CALL or any product
   artifact.
4. Prepend the declared LOG line and save this full RESULT once in history.

t-3 remains `active`. No CHARTER, TREE, bet, task, track or WIP-limit field changes.

## captures

None.

## decisions_needed

None in Direction. The new product PLAN session must present its exact artifact and obtain the owner's actual
approve/revise/reject words before any downstream stage.

## play_check

1. **Recite** — done: fresh state confirms active bet g-37a1, active task t-3 and its t-venue lane; this leg only
   replaces that lane's root.
2. **Owner inputs (owner)** — done: exact words supplied `engineering contract 31`, `WIN-U3`, `Target Local`, new change
   id, one launch, ordinary failure modes, ten exclusion groups, the simple stale-marker rule and PLAN-only STOP.
3. **Do the work** — done: one self-contained same-lane engineering CALL with a distinct change id was authored; the
   old candidate is history rather than new authority.
4. **Self-check** — done: build error, missing required bundle files, no window, immediate crash, close hang and nonzero
   exit remain fail outcomes; every owner exclusion is explicit; PLAN cannot write code/tests/tools or proceed without
   owner approval.
5. **Close** — done: old root id is removed from dispatch, exactly one successor root is registered in t-venue, t-3
   stays active and unrelated state is preserved.

G1: one root remains in t-venue and WIP is unchanged. G3: appetite unchanged. G5: neither t-3 nor either product root
is marked done/PASS. G7: no unresolved Direction decision. G9: CHARTER/TREE untouched. G10: owner words are cited.

## log

После PAIR-FREEZE rejection старый audit-grade packaged-player root остановлен без ремонта PAIR-CANDIDATE; выпущен
новый contract-31 PLAN-only root на WIN-U3 / Target Local с одним запуском, обычными failure modes и простым post-build
success marker.

## next

`c-exec-g-37a1-venue-packaged-player-minimal-002` — `ready`, track `t-venue`, task t-3, slot WIN-U3, Target Local.
Полный self-contained payload:
`live/indie-game-development/work/c-exec-g-37a1-venue-packaged-player-minimal-002-call.md`.

END_OF_FILE: live/indie-game-development/history/2026-07-30-s-work-g-37a1-venue-packaged-player-plan-reset-001.md
