---
id: c-exec-g-5a7c-loot-1-001
_kind: call
to: executor
for: t-loot-1
status: superseded
issued: 2026-08-12
call: work/c-exec-g-5a7c-loot-1-001-call.md
repo: ainazemtsau/GasCoopGame
engineering_contract: 36
slot: WIN-U1
basis: 0618184f5e81f6f573bf88bea31782a5c85987a4
description: Набор лута по рукам в комнатах дома, библиотекой; и лут становится твёрдым
  для лута
_pos: 81
unblock_when: c-exec-g-5a7c-loot-foundation-001 публикует новый путь и stale-contact
  fix; preserve не меняется
waiting_on: c-exec-g-5a7c-loot-foundation-001
paused_by: history/2026-08-13-s-work-g-5a7c-loot-foundation-dispatch-001.md
superseded_by: c-exec-g-5a7c-loot-foundation-001
at: 2026-08-14
---

## журнал
2026-08-14 · СНЯТ КАК ПЕРЕБИТЫЙ, И УСЛОВИЕ РАЗБЛОКИРОВКИ ИСПОЛНЕНО БУКВАЛЬНО: его unblock_when требовал, чтобы дочерний наряд опубликовал новый путь и починку протухшего удара, а preserve не менялся — все три перемерены этой ногой, origin/main = origin/dev = 53afdc2d несёт LootDefinition/LootHeft/LootVisualProfile/LootSupport/ToppledCargoThing в продакшене, ветка preserve/c-exec-g-5a7c-loot-1-001-win-u1-local-20260813 стоит ровно на e0a30194 и этот коммит НЕ является предком опубликованной головы, то есть замороженный кандидат не открывали и в дерево не вливали; ready он стать не мог и не должен — его собственный текст наряда запрещает переоткрывать и патчить замороженного кандидата, а всё его содержание построено заново от свежей головы дочерним нарядом, поэтому единственная законная судьба карточки — закрытие перебитым, а не выдача на исполнение · history/2026-08-14-s-work-g-5a7c-loot-foundation-return-001.md
2026-08-13 · владелец выбрал один полный первый BUILD лута вместо split/cut; точный handoff сохранён, старый candidate оставлен PRESERVED-PAUSED, выпущен отдельный child CALL от свежего origin/main со stable IDs, physical supports, network/visual/behavior seams и stale-contact fix · history/2026-08-13-s-work-g-5a7c-loot-foundation-dispatch-001.md
2026-08-13 · наряд вернулся PRESERVED-PAUSED и переведён в paused, а не закрыт: кандидат существует целиком, сохранён на origin как preserve/c-exec-g-5a7c-loot-1-001-win-u1-local-20260813 = e0a30194 и по контракту продукта не патчится на месте — заморозка это custody; райдер владельца «лут не должен через друг друга проходить» ИСПОЛНЕН и измерен числом, как требовал замок наряда; блокер один и он записан уликой i-loot-candidate-emits-stale-contact-on-pickup-001; ре-допуск делает НОВЫЙ наряд Направления от сохранённого SHA, и он же владеет починкой · history/2026-08-13-s-work-g-5a7c-sight-1-checkpoint-001.md
2026-08-12 · наряд выдан в WIN-U1 от опубликованной головы 0618184f; несёт райдером решение владельца «лут не должен через друг друга проходить», но с замком — сначала измерить, во что обходилось выключение коллизий, и СТОП домой, если включение ломает решатель · history/2026-08-12-s-work-g-5a7c-loot-1-dispatch-001.md
END_OF_FILE: live/indie-game-development/cards/closed/c-exec-g-5a7c-loot-1-001.md
