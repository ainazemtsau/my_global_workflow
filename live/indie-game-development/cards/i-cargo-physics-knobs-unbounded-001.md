---
id: i-cargo-physics-knobs-unbounded-001
_kind: issue
level: execution
route: work
evidence: work/2026-08-20-call-cargo-tuning-safety-1.md
_pos: 122
---

## issue
`GameRulesSettings` нормализует engine-facing cargo knobs несогласованно: nonfinite/отрицательные значения некоторых полей могут попасть в Unity, а min-only `PhysicsStepsPerTick` позволяет одному tick выполнить до `int.MaxValue` симуляций. Sleep/contact уже имеют repaired fallback; dimensions/mass принадлежат отдельному loud invalid-authoring path и сюда не входят.
## review_when
После возврата `t-cargo-tuning-safety-1` на fresh post-Repair-A main с native Unity evidence и binding fresh review; закрыть только если valid tuning осталось live, actual Unity/world path и bounded loop доказаны через production-used seam, а rollback bare-rethrow proof сохранён.
## журнал
2026-08-20 · cargo physics tuning оформлен отдельной blocked-задачей после Repair A — одна граница, bounded substeps и production-used rollback seam · history/2026-08-20-s-work-g-5a7c-cargo-tuning-safety-001.md
END_OF_FILE: live/indie-game-development/cards/i-cargo-physics-knobs-unbounded-001.md
