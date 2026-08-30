---
id: c-exec-g-5a7c-cargo-tuning-safety-1-001
_kind: call
_bet: bet-g-5a7c-wave-5
status: dropped
to: executor
for: t-cargo-tuning-safety-1
play: work
issued: 2026-08-20
call: work/2026-08-20-call-cargo-tuning-safety-1.md
repo: C:\projects\Unity\GasCoopGame_dev
engineering_contract: 36
description: Единая нормализация engine-facing cargo tuning и bounded physics-step
  loop
unblock_when: Repair A принят после native Unity + binding review и интегрирован в
  fresh product main; слот не резервирован
_pos: 111
---

## note
Fresh post-Repair-A basis и свободный Unity slot выбираются только при dispatch; running Repair A не расширяется и не считается закрытым этой ногой.

Acceptance требует один production-used actual-loop/throw seam: без reflection/string/private/test-only hook, fault flag или raw-knob обхода.
## журнал
2026-08-30 · ЗАКРЫТ ЗАКРЫТИЕМ ВОСЬМОЙ ВОЛНЫ по той же причине: parked вне схемы, paused без слова владельца невозможен, ставка закрыта. Содержание держат живые улики i-cargo-physics-knobs-unbounded-001 и i-unclamped-knobs-can-freeze-the-world-001; текст наряда цел в work/2026-08-20-call-cargo-tuning-safety-1.md · history/2026-08-30-s-review-g-5a7c-wave-8-close-001.md
2026-08-20 · cargo physics tuning оформлен отдельной blocked-задачей после Repair A — одна граница, bounded substeps и production-used rollback seam · history/2026-08-20-s-work-g-5a7c-cargo-tuning-safety-001.md
END_OF_FILE: live/indie-game-development/cards/closed/c-exec-g-5a7c-cargo-tuning-safety-1-001.md
