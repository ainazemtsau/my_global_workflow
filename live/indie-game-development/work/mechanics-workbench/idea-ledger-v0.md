# Mechanics Workbench — Idea Ledger v0

Status: idea ledger / parking lot, не canon.
Purpose: сохранить идеи и показать, какой blocker они ждут.

## Статусы

- **NOW** — обсуждаем в ближайшем ревью.
- **NEXT** — зависит от текущего blocker, но скоро понадобится.
- **PARKED** — сохраняем, не спорим сейчас.
- **SALVAGE** — старый материал; может вернуться только если нужен новой минимальной игре.
- **REJECTED-FOR-NOW** — не выброшено навсегда, но вредно как текущий путь.

## 1. Пузырь / visible gas custody

Status: NOW candidate for minimal floor proof.

Claim:
игроки переводят часть газа в большой видимый хрупкий пузырь и несут его наружу; если пузырь рвется, газ возвращается в мир.

Почему сильная идея:

- понятная картинка: "вынеси шарик, не лопни";
- газ остается видимым, не прячется в железный stat-container;
- failure world-changing: газ выходит рядом с игроками;
- co-op может быть телесным: route, двери, узкие места, внешние газы, реакции;
- тип/состояние газа может менять характер переноски без отдельного monster AI.

Что не решено:

- откуда именно берется газ для пузыря;
- как игроки понимают область газа;
- как переводят газ в bubble;
- кто и как несет;
- как bubble повреждается / течет / рвется;
- как внешние газы и reactions влияют на bubble;
- можно ли восстановиться после rupture.

Первый вопрос:

> Принимаем ли мы `Пузырь` как текущий предмет обсуждения минимального proof, если capture-action честно помечен TBD?

## 2. ЛЁГКИЕ / base air meta

Status: PARKED, preserved.

Source:
attachment `pasted-text.txt` and `concept-pitch-2026-07-07.md` v1.4.

Claim:
ценность и дыхание — одна субстанция. На базе один бак воздуха и один refinery choice: `ДЫШАТЬ` или `ПРОДАТЬ`.

Почему сильная идея:

- сохраняет одну субстанцию от floor до meta;
- убирает абстрактную квоту;
- дает видимый one-more-run pressure через колбу воздуха;
- корпоративный долг/воздух в кредит попадает в тон;
- переносима: может питаться captured gas или оплатой за mission-value, если ядро не capture-first.

Почему не сейчас:

- зависит от доказанного floor value;
- зависит от replay pull без меты;
- преждевременная экономика начнет диктовать mechanics;
- числа/маржа легко съедят обсуждение.

Blocker:
A7 replay/value proof.

First later session:

> Если голый floor proof вызывает "еще один заход", как `ЛЁГКИЕ` усиливают это без превращения игры в таблицу?

## 3. Quiet / sleep floor

Status: NEXT.

Claim:
этаж начинается тихим: газ не обязательно очевиден и не обязательно активен; игроки читают следы и выбирают момент disturbance.

Что полезно:

- дает phase structure: read -> act -> escalation -> greed;
- позволяет detection-first;
- делает route planning meaningful.

Опасность:

- "сон" может стать магическим aggro;
- "спящий" может стать слишком безопасным;
- если признаки слишком явные, разведка превращается в чеклист;
- если признаки слишком скрытые, смерть кажется нечестной.

Blocker:
A2 floor read / detection.

## 4. Detection / field legibility

Status: NOW/NEXT.

Claim:
игроки должны видеть/слышать/мерить достаточно, чтобы действие было честным.

Candidate tells:

- пыль движется к щели;
- иней/конденсат;
- слой у пола/потолка;
- muffled sound / pressure hum;
- corrosion/residue;
- door pressure behavior;
- simple instrument spike;
- visible front after disturbance.

Не решаем:
final scanner UI, full diagnosis game, gas names, tutorial.

Blocker:
A2.

## 5. Release / reactions / external gas

Status: NOW.

Claim:
ошибка с bubble должна возвращать газ в sim and create a world state, not just lose value.

Must discuss:

- bubble ruptures in clean air;
- bubble ruptures inside another gas;
- external gas damages membrane / heats / cools / pressurizes;
- released gas reacts with room gas;
- partial leak creates trail;
- release can sometimes be correct play;
- after release, recovery may be possible.

Почему важно:
в прошлой версии это было забыто, хотя reactions уже core engine/design material.

Blocker:
A5.

## 6. Carry / body co-op

Status: NEXT.

Claim:
перенос должен требовать живой кооперации, а не быть "один несет, второй смотрит".

Open questions:

- bubble size;
- handles/tethers/contact points;
- one vs two carriers;
- does carrier lose vision/hands/speed;
- can teammate read signals on bubble;
- what happens in narrow door/stairs/elevator;
- how route operator matters.

Blocker:
A4/A6.

## 7. Flagship gas examples

Status: PARKED.

Examples from pitch/share:
`Тихоня`, `Сквозняк`, `Вспышка`, `Разлив`, `Руки`, `Хор`.

Use:
only as examples of possible behavior jobs.

Do not do now:
freeze roster, names, exact gas types, exact prices, exact reactions.

Blocker:
after A1-A6, then gas jobs/roster session.

## 8. Building as gas tool

Status: NEXT/SALVAGE.

Claim:
doors, vents, height, holes, pressure and route are player tools, not backdrop.

Why useful:
keeps gas interactive even before full toolset.

Candidate first proof uses:

- open/close route;
- one vent/shaft;
- one hot/cold/pressure hazard;
- one destructible or route-change beat only if needed.

Blocker:
A2/A5.

## 9. Tools / instruments

Status: PARKED.

Claim:
tools will be needed, but exact list is not current blocker.

Allowed now:
"some way to read" / "some way to transfer gas" as unresolved sockets.

Not allowed now:
scanner UI, membrane ring as final, canister taxonomy, store/loadout, upgrades.

## 10. Mission-value-first

Status: REJECTED-FOR-NOW as playable parallel branch; kept as paper fallback.

Why not build now:
owner rejected wasting time on two mechanics. We should not create Bubble-vs-mission comparison as playable work.

What remains useful:
paper sanity question:

> Does Bubble make gas itself feel valuable enough? If not, fallback to mission-value-through-gas-danger.

## 11. Old canon / gas-interaction map

Status: SALVAGE.

Useful terms:
field read, source/flow, reaction front, active condition, release, custody, return liability, no creature AI.

Danger:
old canon language can sound authoritative and hide unclear current mechanics.

Rule:
old material enters only when it helps answer a current blocker.

## 12. Title / `ОНО ДЫШИТ`

Status: PARKED.

Allowed:
working title / pitch label.

Forbidden:
living city ontology, gas subjectivity, creature AI, magical sleep/wake, title-driven mechanics.

Rule:
title follows proof.

END_OF_FILE: live/indie-game-development/work/mechanics-workbench/idea-ledger-v0.md
