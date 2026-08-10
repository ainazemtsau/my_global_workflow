---
id: i-world-situations-need-extensible-reaction-architecture-001
_kind: issue
level: objective
route: review
evidence: GasCoopGame@d9518538:docs/results/c-exec-g-5a7c-loot-inactive-until-held-001.md
_pos: 36
---

## issue
Текущий `CargoSituation → HouseholderStimulus` — cargo-specific мост ПРОБЫ, а не выбранная общая архитектура: orchestration знает производителя и потребителя, а priority/supersession значимых ситуаций остаётся внутри хозяина. При расширении обработчики могут начать знать реализацию источника, а новые ситуации — молча теряться на pending/active наблюдении.
## review_when
До первой задачи со вторым типом world-situation или вторым независимым consumer, либо на review текущей ставки: сравнить простые доменные мосты с host-owned tick-scoped typed situation stream/buffer и явно решить ordering, one-shot, merge и supersession.
## журнал
2026-08-10 · первая волна закрыта вердиктом met — пропорция 0.16, вертикаль у игрока и у груза, луч и ступень по рукам доказаны байтами и прогнанными этой ногой 151/151, ни одна клауза не сломалась, а всё неснятое снял сам владелец; ревью нашло три вещи, которых не назвала ни одна нога волны — доставка видит один кусок лута из четырёх, мир стал впятеро длиннее по времени, и вырез «хозяин работает как сегодня» сломан пятой реакцией; следующая волна выбрана им: две дорожки, дом следующей · history/2026-08-10-s-review-g-5a7c-first-wave-met-001.md
2026-08-09 · лут живёт только в луче или падении, после посадки структурно молчит и остаётся низким препятствием — задача закрыта повторным прогоном владельца; общий situation-layer вынесен отдельным вопросом архитектуры · history/2026-08-09-s-work-g-5a7c-scale-4-close-001.md
END_OF_FILE: live/indie-game-development/cards/i-world-situations-need-extensible-reaction-architecture-001.md
