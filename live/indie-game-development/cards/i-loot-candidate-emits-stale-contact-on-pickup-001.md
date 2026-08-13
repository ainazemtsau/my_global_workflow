---
id: i-loot-candidate-emits-stale-contact-on-pickup-001
_kind: issue
level: execution
route: work
status: open
_pos: 85
---

## issue
Preserved candidate keeps resting cargo solid but does not consume/reset its inactive contact window;
after pickup an old hit can emit false force/noise and beat a real sight/situation. The frozen ref is
custody-only and has no regression for strike → wait → pickup.
## review_when
`c-exec-g-5a7c-loot-foundation-001` builds from fresh `origin/main`, uses `e0a30194` only as evidence,
and owns inactive→active reset plus fresh-contact/one-shot/sight regressions. Close with publication;
never patch preserve, edit covering or add manual Y.
## evidence
`origin/main:docs/results/c-exec-g-5a7c-loot-1-001.md`; preserve ref
`e0a301947c28ef04a8465a411104098f54d9b9f7`;
`work/2026-08-13-loot-owner-architecture-handoff.md`.
## журнал
2026-08-13 · владелец выбрал один полный первый BUILD лута вместо split/cut; точный handoff сохранён, старый candidate оставлен PRESERVED-PAUSED, выпущен отдельный child CALL от свежего origin/main со stable IDs, physical supports, network/visual/behavior seams и stale-contact fix · history/2026-08-13-s-work-g-5a7c-loot-foundation-dispatch-001.md
END_OF_FILE: live/indie-game-development/cards/i-loot-candidate-emits-stale-contact-on-pickup-001.md
