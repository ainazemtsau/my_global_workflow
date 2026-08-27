---
id: t-cargo-tuning-safety-1
_kind: task
_bet: bet-g-5a7c-wave-5
status: parked
goal: Cargo physics tuning безопасно доезжает до Unity, а число substeps структурно
  ограничено
unblock_when: Repair A принят после native Unity + binding review и интегрирован в
  fresh product main; слот не резервирован
_pos: 93
---

## done_when
1. **ОДНА OWNER-BOUNDARY И FIELD-SPECIFIC DOMAINS.** `GameRulesSettings` остаётся единственным serialized authoring owner и один раз создаёт typed immutable engine-facing carrier. Gravity, linear/angular damping, max angular speed, solver iterations/velocity iterations, sleep threshold, contact offset и physics steps имеют собственные finite/sign/range/fallback правила в этой границе; `CargoBody` не повторяет policy per tick. Где нужен structural ceiling, инженерия выбирает, именует и обосновывает его через engine/work safety; universal clamp и произвольные feel maxima запрещены.
2. **VALID TUNING ОСТАЁТСЯ LIVE, ACTUAL UNITY PATH И BOUNDED LOOP ДОКАЗАНЫ ЧЕРЕЗ PRODUCTION-USED SEAM.** In-domain values проходят identity-mapping; serialized asset не получает guessed tuning edits, а каждый knob остаётся наблюдаемо живым через synthetic valid probes, не фиксирующие сегодняшние числа. Native tests проверяют фактические `Physics.gravity`, `Rigidbody` damping/maxAngularVelocity/solver properties, `Collider.contactOffset` и world progression. Nonfinite/out-of-domain probes не достигают Unity. Один production-grade engine-driver boundary или другой production-used честный seam проходит тем же runtime path, что игра; один runnable test подаёт raw `PhysicsStepsPerTick = int.MaxValue`, считает фактические simulate calls, доказывает не больше выбранного structural ceiling и ровно один tick суммарного world progression. Seeded bypass/removal mutants падают без запуска unbounded loop.
3. **ТОТ ЖЕ SEAM СОХРАНЯЕТ BARE-RETHROW/ROLLBACK CLAIM И ЗАКРЫВАЕТСЯ NATIVE + BINDING REVIEW.** Тот же runnable test заставляет engine call детерминированно бросить и доказывает, что исходное исключение выходит через bare rethrow, `SimulationMode`/gravity возвращены, а последующая операция работает. Нынешний Repair A seed через `+Infinity` gravity удаляется только вместе с этой честной заменой; молчаливое удаление/ослабление, reflection/string invocation, private/test-only hook, fault flag или иной raw knob, который normalization обязана обезвредить, запрещены. Возврат несёт native Unity test/build evidence, per-field/actual-loop negative controls и binding fresh review.
## note
**ФОНОВАЯ ИНЖЕНЕРИЯ, НЕ SCREENSHOT TASK И НЕ GATE ВОЛНЫ.** Основание и автономный режим: `work/2026-08-20-background-cargo-engineering-mandate.md`.

**DEPENDENCY:** `c-exec-g-5a7c-cargo-sleep-repair-1-002` должен пройти native Unity + binding fresh review, быть принят Direction и интегрирован в fresh product main. Unity slot и execution basis заранее не резервируются; их выбирает отдельный будущий dispatch.

**BOUNDARY:** serialized tuning остаётся live; normalization владеет одна `GameRulesSettings → typed immutable carrier` граница, а доказательный actual-loop/throw seam используется production path, не test-only обходом. Dimensions/mass, network/lifecycle, scenes/art/screenshots и running Repair A не входят.
## журнал
2026-08-20 · cargo physics tuning оформлен отдельной blocked-задачей после Repair A — одна граница, bounded substeps и production-used rollback seam · history/2026-08-20-s-work-g-5a7c-cargo-tuning-safety-001.md
END_OF_FILE: live/indie-game-development/cards/t-cargo-tuning-safety-1.md
