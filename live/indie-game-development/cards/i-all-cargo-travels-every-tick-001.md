---
id: i-all-cargo-travels-every-tick-001
_kind: issue
level: objective
route: work
evidence: history/2026-08-20-s-research-g-5a7c-interactive-density-part1-recheck-001.md
_pos: 114
---

## issue
Весь pose/hold груза едет reliable каждому клиенту каждый tick; current static estimate
для 50/200/500 предметов — около 70.7/277/691 KB/s до headers/retransmits. После B1
покой pose/hold может стоить ноль, initial/catch-up остаётся O(cargo), массовый каскад —
O(simultaneous pose/hold dirty); глобальный gameplay-state идёт отдельным lifecycle только
на semantic start/change/end/catch-up и не входит в room-interest scope.
## review_when
B0 runtime + B1 доказывают exact pose/hold bytes, 60-second idle и cascade dirty;
`t-cargo-state-lifecycle-1` отдельно доказывает global state traffic/order/catch-up без
timer-dirty; runtime-часть `c-research-g-5a7c-interactive-density-001` записывает итоговые
wire/queue/latency числа. До всех трёх issue остаётся open.
## журнал
2026-08-20 · B1 отделена от глобального gameplay-state — pose/hold остаётся sparse, lifecycle вынесен в отдельную blocked-задачу перед B1, мёртвые wire-поля не резервируются · history/2026-08-20-s-repair-g-5a7c-cargo-state-lane-001.md
2026-08-20 · CURRENT MAIN ПЕРЕСЧИТАН: snapshot 45 байт для малых id, RPC reliable всегда, 50/200/500 дают статически ≈70.7/277/691 KB/s на удалённого клиента и 2/8/19 fragments каждый такт. Это не wire capture; runtime обязателен. Простое omission незаконно — клиент уничтожает пропущенный view, значит B требует registry/add-update-remove/catch-up. Exact-delta вероятно хватает обычной плотности, но не доказан для массового каскада · history/2026-08-20-s-research-g-5a7c-interactive-density-part1-recheck-001.md
2026-08-17 · ЕГО ВОПРОС ПРО ПЛОТНОСТЬ ПОЛУЧИЛ ПОЛОВИНУ ОТВЕТА ЗАМЕРОМ, А НЕ НАРЯДОМ: потолок сегодня — СЕТЬ, а не физика, и это потолок неоптимизированного кода. PublishSnapshots строит массив по всему ростеру груза и шлёт его КАЖДЫЙ ТАКТ КАЖДОМУ наблюдателю без всякого фильтра — лежащий на полу камень стоит ровно столько же, сколько летящий, хотя поле Moved в снимке есть и заполняется; снимок 15 полей около 57-60 байт, массив выделяется заново каждый такт. И ЕГО СОБСТВЕННАЯ ДОГАДКА ПРО ФОН ОКАЗАЛАСЬ НЕ ТОЛЬКО ПРО ПОНЯТНОСТЬ: обстановка не едет по сети вовсе, значит «стеллаж один объект, а не сто книг» и «шкаф прибит, открывается только дверца» — единственный способ вообще получить его числа, а не приём подачи. Сегодня в доме 12 предметов груза и 23 обстановки, поэтому цена ещё не видна. Вторая половина ушла нарядом на ресёрч из восьми вопросов, каждый с требованием ЧИСЛА и источника числа, и первым стоит самый дешёвый рычаг — сколько даёт исключение осевших из снимка. Ресёрчу прямо запрещено решать дизайн: две породы вещей, дорогие хозяину против продаваемых, и сознательная скупость на мелкий лут — его содержание, оно записано отдельной карточкой его же словами · history/2026-08-17-s-work-g-5a7c-density-research-dispatch-001.md
END_OF_FILE: live/indie-game-development/cards/i-all-cargo-travels-every-tick-001.md
