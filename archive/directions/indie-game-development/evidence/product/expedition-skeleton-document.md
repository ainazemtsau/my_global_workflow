# Expedition Skeleton Document

## 0. Статус документа

Это direction-level game documentation note.

Документ фиксирует минимальный доказуемый игровой скелет **Expedition**: какую игру нужно проверять, какие systems образуют её core loop, какие commitments уже являются foundation, какие формы допустимы как placeholders, а какие вопросы остаются deferred или требуют отдельного решения.

Документ не является:

- полным дизайном игры;
- экономикой;
- деревом улучшений;
- технической архитектурой;
- планом реализации;
- build order;
- task list;
- proof design;
- gas simulation plan;
- tool catalog;
- cargo / carrying / death mechanics spec.

Документ нужен для того, чтобы следующие Goals, proof/build planning and implementation work проверяли именно **Expedition skeleton**, а не isolated gas demo, случайный prototype, набор disconnected features or premature full game design.

## 1. Selected skeleton hypothesis

Выбранная skeleton hypothesis:

**Нарастающая экспедиционная ставка.**

Коротко:

Команда готовит рискованный капитал, спускается через физический лифт на этаж / фронтир, добывает опасную ценность в сосуде с газом и решает: возвращаться сейчас или рискнуть ради большего продвижения.

Чем дальше команда продвигается и чем больше ценности несёт обратно, тем выше цена ошибки.

Ошибка может стоить:

- части ценности;
- всего сосуда;
- инструментов;
- состояния лифта или доступа;
- знания / маршрута;
- возможности следующего забега;
- игрока или командного состояния внутри забега.

Смысл игры не в “больше этажей” и не в “больше лута”.

Смысл игры в том, что каждый следующий шаг делает ставку понятнее и опаснее.

## 2. Why this hypothesis is selected

Expedition рассматривалась через несколько возможных skeleton centers:

- depth / going deeper;
- unstable value;
- risky preparation.

Чистая **depth hypothesis** опасна тем, что может стать просто ростом номеров этажей, difficulty curve or reward curve. В текущем skeleton depth остаётся supporting pressure: команда может открыть следующий front / deeper access, но exact unlock model не фиксируется.

Чистая **unstable value hypothesis** опасна тем, что может стать скучным тасканием cargo. В текущем skeleton value сохраняется как dangerous gas-vessel value: награда и угроза связаны в одном объекте.

Чистая **risky preparation hypothesis** опасна тем, что может стать item catalog, shop, loadout manager or upgrade tree. В текущем skeleton tools остаются risky capital roles: они создают возможности, риск, расход, потерю и кооперативные решения, но не превращаются в catalog.

**Нарастающая экспедиционная ставка** сильнее, потому что связывает эти centers в одну причинную цепочку:

preparation / tools / lift
→ run
→ gas / map / dangerous vessel / retreat / co-op
→ value or loss
→ changed between-run state
→ reason for next descent.

## 3. One-line skeleton

**Expedition** — это 4-player-first expedition game, где команда через физический лифт спускается в одноразовый опасный этаж / фронтир, сталкивается с газом, неизвестной картой, опасной vessel-value, расходом инструментов и кооперативной ответственностью, а затем выходит с частичным успехом, потерями или изменённым доступом.

После выхода результат фиксируется.

**Post-exit recovery run запрещён.**

## 4. Main causal chain

Минимальный skeleton работает только если systems связаны так:

 

```
подготовка / инструменты / выбранный риск
→ спуск через лифт
→ маршрут на этаже / фронтире
→ газ, карта, vessel-value, переноска, ошибки, спасение, отступление
→ вынесенная ценность или потеря
→ изменённое состояние между забегами
→ причина следующего спуска
```

 

Если эта цепочка распадается, Expedition превращается в список механик.

Если gas отделяется от route / vessel / tools / retreat / lift / co-op, игра превращается в gas demo.

Если vessel становится обычным loot box, ставка исчезает.

Если between-run layer становится полной экономикой, skeleton выходит за нужную границу.

## 5. Local expedition loop

Один забег выглядит так на skeleton-level.

Команда готовится.

Она выбирает рискованный капитал:

- tools;
- roles;
- protection;
- scouting;
- stabilization;
- carrying support;
- rescue capability;
- communication.

Команда входит через лифт.

Лифт — физическая точка входа, выхода, передачи риска и возврата последствий.

Команда исследует этаж / фронтир.

Карта не полностью ясна. Маршрут туда может быть проще, чем маршрут назад.

Команда сталкивается с газом.

Газ влияет на:

- route;
- time pressure;
- tool spend;
- vessel danger;
- visibility of threat;
- retreat;
- co-op decisions.

Команда получает или обнаруживает опасную ценность.

Ценность — это **vessel / container / gas carrier**, а не generic cargo.

Сосуд создаёт ставку.

Его можно повредить. Повреждение может выпустить газ. Повреждение может снизить или уничтожить value.

Команда решает, что делать дальше:

- вернуться сейчас;
- рискнуть и идти глубже;
- изменить маршрут;
- потратить tool;
- спасать игрока;
- стабилизировать vessel;
- бросить часть ценности;
- принять partial loss.

Команда отступает к лифту.

Retreat должен быть игровым решением, а не формальностью.

Результат фиксируется при выходе.

Команда получает:

- value;
- loss;
- partial success;
- damaged tools;
- changed access;
- lift/access consequence;
- gained knowledge;
- reason for next descent.

## 6. Between-run value / consequence layer

Между забегами игра должна помнить последствия.

Этот слой пока не является:

- базой;
- хабом;
- магазином;
- валютой;
- upgrade tree;
- production chain.

На skeleton-level он может фиксировать:

- какая value вынесена;
- какая value потеряна;
- какой vessel повреждён или уничтожен;
- какие tools сохранены;
- какие tools потрачены, повреждены, потеряны или загрязнены;
- что команда узнала о routes / gas / frontier;
- изменился ли access к следующей глубине / фронтиру;
- изменилось ли состояние lift or access;
- почему следующий descent теперь нужен.

Главная функция этого слоя:

**последствия прошлого забега создают причину следующего забега.**

Он не должен становиться full economy до отдельного решения.

## 7. System pillars

### 7.1 Dangerous gas-vessel value

Ценность Expedition — это опасный vessel с газом / container / carrier.

Он не является обычным ящиком.

Skeleton-level commitments:

- vessel is valuable;
- vessel is dangerous;
- vessel can be damaged;
- damage can release gas;
- damage can reduce or destroy value;
- carrying / handling vessel creates responsibility;
- vessel links reward and threat.

Почему это важно:

Если vessel нельзя повредить и он не связан с газом, он превращается в обычный cargo.

Если vessel всегда полностью успешен или полностью потерян, исчезает partial success / partial loss.

Unresolved:

- found vessel vs player-filled vessel;
- exact acquisition;
- exact carrying method;
- exact ownership;
- exact damage values;
- exact leakage;
- exact value degradation.

### 7.2 Gas as decision pressure

Газ — не visual effect и не isolated simulation.

Газ должен создавать решения:

- идти через опасную область или искать обход;
- тратить tool или экономить;
- стабилизировать vessel или продолжать;
- спасать игрока или отступать;
- возвращаться сейчас или идти глубже;
- брать damaged vessel в lift или бросить;
- менять route из-за распространения газа.

Газ должен связывать:

- route choice;
- retreat urgency;
- tools;
- vessel danger;
- lift / extraction risk;
- co-op responsibility;
- between-run consequences.

Unresolved:

- exact gas recipes;
- gas type catalog;
- reaction tables;
- simulation internals;
- leakage numbers.

### 7.3 Tools as risky capital roles

Tools — это risky capital, not item catalog.

Они нужны не ради списка предметов, а ради preparation and stake.

Tool roles may include:

- access;
- protection;
- scouting;
- stabilization;
- carrying support;
- containment;
- rescue;
- communication.

Tools могут:

- открыть путь;
- снизить риск;
- дать knowledge;
- stabilize vessel;
- помочь в переноске;
- спасти игрока;
- быть потраченными;
- быть повреждёнными;
- быть потерянными;
- быть загрязнёнными;
- повлиять на всю команду, даже если использует один игрок.

Unresolved:

- exact tool list;
- exact stats;
- inventory system;
- loadout UI;
- shop;
- upgrade tree;
- crafting;
- repair economy.

### 7.4 Map / generation as route uncertainty and retreat pressure

Map / generation нужны не как “random rooms”.

Они должны создавать:

- route choice;
- uncertainty;
- retreat pressure;
- risky value placement;
- split risk;
- rescue situations;
- mistakes with consequences;
- pressure to continue or return.

Хорошая map делает обратный путь важным.

Если map не влияет на retreat, gas movement, vessel handling and co-op decisions, она не выполняет skeleton role.

Unresolved:

- exact procedural model;
- room catalog;
- generation algorithm;
- biome / content model;
- technical procgen architecture;
- exact map persistence.

### 7.5 Lift as physical bridge / extraction / risk concentration

Lift — не level menu.

Lift — не safe warehouse.

Lift — не unfair trap.

Skeleton-level role:

- entry point;
- exit point;
- extraction boundary;
- place where prepared capital enters;
- place where consequences return;
- risk concentration point;
- bridge between local run and between-run state.

Lift связывает:

- preparation;
- descent;
- retreat;
- extraction;
- vessel danger;
- tools;
- between-run consequences.

Unresolved:

- exact lift failure model;
- exact contamination model;
- access consequence model;
- repair rules;
- safe storage rules.

### 7.6 4-player co-op as gameplay interest

Основной lens: **4-player co-op**.

4-player is not just player count.

Co-op должна создавать:

- responsibility;
- rescue;
- disagreement;
- split risk;
- shared carrying;
- mistakes with consequences;
- pressure to coordinate;
- stories after run.

Примеры skeleton-level co-op interest:

- один игрок несёт или стабилизирует vessel;
- один тратит tool, который нужен всей команде;
- часть команды идёт вперёд, часть держит путь назад;
- кто-то ошибается с gas or route;
- команда спорит: возвращаться сейчас или рискнуть;
- rescue before exit может спасти часть результата;
- плохое отступление заставляет решать, что бросить.

4–8 players не является обещанием реализации.

4–8 remains:

- possible future pressure-test;
- potential scale risk;
- S3 decision if it affects identity.

### 7.7 Loss, partial success and no-return

Loss is not only binary fail.

Хорошая loss model должна давать:

- visible stake;
- understandable risk;
- partial success;
- partial loss;
- clear consequence;
- in-run decision pressure;
- no hidden unfairness.

Примеры partial result:

- vessel вынесен, но damaged;
- value reduced;
- tool lost;
- route knowledge gained but cargo lost;
- access opened but lift/access damaged;
- один игрок спасён, часть ценности брошена;
- команда вышла с меньшим результатом, но есть причина следующего забега.

Post-exit recovery run не используется для fairness.

Fairness должна появляться до выхода:

- через видимую ставку;
- через решения;
- через rescue / salvage before exit;
- через partial success / partial loss.

## 8. Hard no-return boundary

Это hard boundary.

Before exit:

- rescue may exist as in-run pressure;
- salvage may exist as in-run pressure;
- players may try to save vessel, tools, route, lift state or player state;
- team may choose what to abandon;
- partial success is possible.

After exit:

- result is fixed;
- no post-exit recovery run;
- no return to already visited floor / frontier for recovery;
- no post-exit cargo recovery;
- no post-exit tool recovery;
- no post-exit body recovery;
- no persistent recovery markers;
- no salvage economy.

Recovery-run is forbidden for current skeleton.

It is not deferred.

It is not in S3 queue.

## 9. Foundation commitments

Foundation means skeleton-level commitment.

It does not mean exact mechanics.

Current foundation:

- selected hypothesis: **Нарастающая экспедиционная ставка**;
- Expedition is 4-player-first;
- local loop uses preparation, lift, run, gas, map, vessel, retreat and extraction;
- value is dangerous gas-vessel value, not generic cargo;
- vessel can be damaged;
- damage can release gas;
- damage can reduce or destroy value;
- gas creates decisions;
- tools are risky capital roles;
- map / generation creates route uncertainty and retreat pressure;
- lift is physical bridge / extraction / risk concentration;
- between-run layer records consequences without becoming full economy;
- loss allows partial success / partial loss;
- after exit, result is fixed;
- post-exit recovery run is forbidden.

## 10. Allowed placeholders

Placeholders are temporary forms.

They are allowed only if they do not silently become final decisions.

Allowed placeholders:

**Next front / deeper access becomes available.**
This keeps depth pressure without deciding unlock math.

**Team obtains dangerous gas-vessel during run.**
This keeps vessel stake without deciding found vs filled.

**Damaged vessel leaks gas and loses some value.**
This keeps partial loss without exact numbers.

**Carrying vessel is unsafe and creates responsibility.**
This keeps co-op pressure without deciding carrying mechanics.

**Tools exist as roles.**
Access, protection, scouting, stabilization, carrying, containment, rescue, communication.

**Between-run consequence ledger.**
Tracks value, tools, knowledge, access and lift/access consequences without choosing base/economy.

**Partial success / partial loss.**
Allows meaningful loss without exact death/downing model.

**Before-exit rescue / salvage pressure.**
Rescue/salvage may exist inside the run, but not after exit.

**Map patterns.**
Route choice, gas pressure, retreat difficulty, risky value placement.

## 11. Deferred hypotheses

Deferred means unresolved but safe to postpone.

Deferred:

- exact gas recipes;
- gas type catalog;
- reaction tables;
- gas simulation internals;
- exact tool list;
- tool stats;
- inventory system;
- loadout UI;
- shop;
- upgrade tree;
- crafting;
- repair economy;
- exact economy;
- rewards;
- currency;
- reward curves;
- production chain;
- exact base / hub form;
- procedural generation algorithm;
- room catalog;
- content model;
- biome model;
- exact depth unlock granularity;
- floor numbering;
- access currency;
- contract model;
- vessel acquisition model;
- vessel damage numbers;
- leakage model;
- value degradation model;
- carrying method;
- handoff model;
- cargo ownership;
- death / downing / group failure;
- in-run rescue details;
- lift failure / contamination;
- one-use consequence tracking;
- 4–8 scale.

Important clarification:

**Post-exit recovery run is not deferred.**

**Post-exit recovery run is forbidden.**

## 12. Decision queue

These decisions must not be silently solved inside future planning or implementation.

### Found vessel vs player-filled vessel

Changes what value means: discovery, harvesting, filling, transformation or extraction.

### Cargo ownership

Shared vs personal ownership changes co-op incentives, blame, rewards and extraction logic.

### Carrying model

Hand-carrying, backpack, shared carrying, tool-assisted carrying or physics carrying would change moment-to-moment play.

### Death / downing / group failure

Affects loss fairness, rescue, frustration and team outcome.

### Lift failure / contamination

Can make lift too safe, too punishing or too central.

### Between-run base / hub form

Could pull the game into economy, management, shop or upgrade tree.

### Exact depth unlock model

Could turn the game into keyhunt, contract board, campaign gate or floor-number grind.

### 4 vs 4–8 player scale

4-player is foundation lens. 4–8 remains potential / risk only.

Not in decision queue:

- recovery-run loop;
- post-exit cargo recovery;
- post-exit tool recovery;
- post-exit body recovery.

Those are forbidden for current skeleton.

## 13. Known weak spots and current handling

### Resolved at skeleton level

**Cargo-risk / gas-vessel value**
Value is dangerous gas-vessel, not generic cargo. Exact model remains unresolved.

**Tools / preparation**
Tools are risky capital roles. No catalog, shop or upgrade tree is selected.

**Gas**
Gas creates decisions. No recipes or simulation spec selected.

**Map / generation**
Map creates route uncertainty and retreat pressure. No procgen algorithm selected.

**Lift**
Lift is physical bridge / extraction / risk concentration. Exact failure/contamination unresolved.

**4-player co-op**
Co-op creates responsibility, rescue, disagreement, split risk and mistakes with consequences. 4–8 is not committed.

**Between-run state**
Between-run layer is consequence ledger. No full base or economy selected.

**Loss / frustration**
Loss uses partial success / partial loss. No post-exit recovery.

**One-use floors / no-return**
Result is fixed after exit. Recovery is forbidden.

**First proof boundary**
First proof is WHAT-level only. No implementation plan.

### Still unresolved

- found vessel vs player-filled vessel;
- cargo ownership;
- carrying model;
- death / downing / group failure;
- lift failure / contamination;
- exact base / hub form;
- exact depth unlock model;
- 4 vs 4–8 player scale;
- exact vessel damage / leakage / value degradation;
- exact gas recipes and gas type catalog;
- exact tool catalog and stats;
- exact procedural model;
- exact one-use consequence tracking;
- first proof implementation.

These are caveats, not blockers, because the current skeleton keeps them visible as placeholders, deferred hypotheses or decision queue items.

## 14. First proof meaning boundary

The first proof should check game meaning.

It should not check whether a gas simulation looks impressive in isolation.

It should check:

### Does the repeated loop appear?

Preparation → descent → route → gas → vessel → retreat → result → next reason.

### Does gas create real decisions?

Route, retreat, tools, vessel danger, lift risk and co-op consequences.

### Does dangerous vessel-value create stake?

Value can be damaged, can leak gas, can be partly lost, and creates carrying responsibility.

### Do tools create preparation and risk?

Tools feel like risky capital, not a catalog.

### Does retreat work?

Players feel pressure to continue, change route, abandon, rescue or return.

### Does lift create physical connection and risk?

It is entry, exit, extraction point and bridge to between-run state.

### Does between-run motivation appear?

After a run, there is a clear reason for another descent.

### Does 4-player co-op create responsibility?

Rescue, disagreement, split risk, shared handling and mistakes produce stories.

### Does no-return sharpen decisions?

Fixed result after exit makes in-run decisions stronger, not just unfair.

### Do systems form Expedition skeleton?

The proof must test system synergy, not isolated gas behavior.

This is WHAT-level only.

No build steps.
No implementation tasks.
No technical architecture.
No proof design.

## 15. Forbidden directions for this skeleton

The skeleton must not become:

- full game design;
- full economy;
- reward curve;
- currency;
- shop;
- upgrade tree;
- production chain;
- technical architecture;
- implementation plan;
- task list;
- build order;
- UI flow;
- networking plan;
- balancing plan;
- content plan;
- exact gas recipes;
- gas type catalog;
- reaction tables;
- exact tool catalog;
- inventory system;
- exact vessel mechanics;
- exact carrying model;
- exact cargo ownership;
- exact death/downing model;
- exact group failure state;
- exact lift failure model;
- exact procedural generation algorithm;
- recovery-run loop;
- return-to-visited-floor recovery;
- post-exit recovery;
- broad genre / market research;
- Expedition vs Containment reopening.

## 16. Why this is not full game design

This document does not decide:

- all mechanics;
- all content;
- all items;
- exact player states;
- exact gas types;
- exact economy;
- exact progression;
- exact map algorithm;
- exact lift behavior;
- exact tool stats;
- exact reward numbers;
- exact failure model;
- exact proof implementation.

It only decides the skeleton-level truth:

**Expedition is a 4-player-first game about escalating expedition stake, where gas, map uncertainty, dangerous vessel-value, risky tools, retreat, lift extraction and between-run consequences create one causal loop.**
