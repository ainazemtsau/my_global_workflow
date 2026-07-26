# work/archive — замороженная история g-9c41 (НЕ авторитет)

Доки в этой папке = архитектура g-9c41 **до 2026-06-22**: граф-first «вода», до-lockstep
Wave-A breakdown, ранний research (12–20 июня). Они **отменены** локом 2026-06-22
(input-lockstep + одна integer-клеточная модель + грид-грань-поток) и лежат здесь ТОЛЬКО как
свидетельство, ПОЧЕМУ пришли к текущей модели.

**При планировании и реализации сюда не заходят.** Действующий канон (и единственное, что читает
свежая сессия):

- `knowledge/g9c41-architecture-locked-slices.md` — залоченные факты.
- `knowledge/g9c41-drift-guard.md` — 5 ловушек пересказа.
- `work/dev-plan-graph-2026-06-22.md` — точка входа (спайн слайсов + DECISION INDEX).
- `work/gas-model-architecture-decision-2026-06-21.md` — D1–D13.
- `work/detail-authority-cost-model-2026-06-22.md` — грубое/деталь, авторитет и цена.
- `work/grid-vs-graph-resolution-2026-06-22.md` — одна модель: грид-near + граф-как-метка-far.

Заглядывать в архив — только если ЯВНО исследуешь прошлые решения.

## Что перенесено 2026-06-22 (s-repair-canon-001) и почему отменено

| Файл | Почему в архиве |
|---|---|
| gas-model-design-full-2026-06-20.md | граф-first «вода»; нет грид-near / collapse / re-flux / checksum-спеки |
| gas-model-research-result-2026-06-20.md | граф-first research, до грид-рефайна |
| gas-model-discussion-brief-2026-06-20.md | рамит «непрерывное поле» как живого конкурента (спор закрыт) |
| aplus-replan-under-locked-arch-v1.md | пост-lockstep replan; §3 рамил детерминизм как 2-машинный гейт (отменено) |
| aplus-wave-map-v1.md | до-lockstep Wave-A карта (superseded спайном слайсов) |
| aplus-breakdown-v1.md | до-lockstep Wave-A breakdown (superseded) |
| research-g-9c41-core-architecture-2026-06-12(.|-v2).md | ранний core-research (host-broadcast эпоха) |
| research-g-9c41-analytic-representations-2026-06-12.md | ранний research представлений |
| shape-g-9c41-approaches-2026-06-12.md | ранний shape подходов |
| research-g-9c41-coarse-representation-2026-06-18.md | ранний coarse-representation research |

**Единственный кусок, ещё используемый как чек-лист:** R-* risk-register + keep-open инварианты в
`aplus-wave-map-v1.md` §4.2 / §2 — свериться ВРУЧНУЮ при PLAN слайса, если нужно (явный заход в архив).

END_OF_FILE: live/indie-game-development/work/archive/README.md
