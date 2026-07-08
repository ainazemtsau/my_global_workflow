# Core Proof Skeleton v0.1

Status: черновик для обсуждения, не canon.
Purpose: дать один понятный предмет спора для минимальной игры.

## 1. Важное исправление после критики владельца

В этом черновике я не использую как готовые решения:

- "газовый карман";
- "запузырить";
- "мембранное кольцо";
- "спящий газ" как магический sleep/aggro.

Если похожий смысл нужен, он пишется явно и честно:

- **gas area / gas state** — область или состояние газа, которое игроки могут обнаружить по следам/приборам/поведению. Точная spatial-form не решена.
- **bubble** — видимая переносимая форма custody/value. Это не тип газа и не финальный контейнер.
- **transfer to bubble** — действие, которое переводит часть газа в bubble. Способ не определен.
- **quiet state** — низкоактивное/трудночитаемое состояние газа до вмешательства. Это не creature sleep.

## 2. Минимальная promise

Рабочая формула:

> Два игрока находят опасное состояние газа, переводят часть этого газа в большой видимый хрупкий пузырь, несут его через опасный маршрут, и если ошибаются — газ выходит обратно в мир именно там, где они ошиблись.

Это не canon. Это стартовый skeleton, который можно принять, сломать или переписать.

## 3. One-room-to-exit loop

### 1. Вход

Два игрока заходят в маленький greybox cluster: 3-6 комнат, один понятный выход, один return route.

На уровне есть газ, но он не обязан быть очевидным цветным облаком.

### 2. Чтение

Игроки ищут признаки:

- где газ может быть;
- на какой высоте/в каком слое;
- опасен ли он уже сейчас;
- что может его сдвинуть/активировать;
- где route risk;
- где bubble carry route.

Признаки могут быть: dust, frost, pressure sound, residue, instrument hint, layer visibility, door behavior, local damage.

### 3. Выбор

Команда решает:

- брать ли этот газ сейчас;
- каким route выносить;
- что закрыть/открыть/обойти;
- кто читает, кто несет, кто держит route.

### 4. Transfer to bubble

Игроки выполняют короткое physical action:

> часть газа переходит в видимый пузырь.

Способ специально не решен. Это отдельный blocker.

Allowed placeholders for later discussion:

- bubble pulls gas in;
- membrane forms around gas;
- players first gather gas into a bounded area;
- tool creates a temporary spherical custody volume;
- another option.

### 5. Carry / custody

Bubble is visible, fragile, route-relevant.

It may be:

- too large for some doors unless players rotate/tilt it;
- pulled by flow/pressure;
- heavier/lighter depending on contents;
- harmed by heat/sparks/sharp surfaces/impact/external gas;
- leaking or pulsing before rupture.

Ничего из этого не финально. Это список того, что нужно обсудить.

### 6. Return pressure

The route is not passive.

Risk can come from:

- external gas;
- opened/closed doors changing flow;
- reaction front;
- hot/cold/pressure area;
- narrow route;
- damaged route;
- teammate exposure;
- bubble instability.

### 7. Failure

If bubble fails:

> gas exits back into the world.

It should not disappear, and the fail state should not be only "lost score".

Possible consequences to decide later:

- released gas spreads in room;
- reacts with external gas;
- blocks route;
- hurts/impairs player;
- forces release/retreat;
- creates a recovery attempt;
- leaves lower-value remaining gas;
- turns "we failed" into a new situation.

### 8. Exit / one more

After exit or failure, players should understand one concrete thing:

- "we chose wrong route";
- "we needed to read that flow";
- "we can carry it if one of us handles the door";
- "we can try one more bubble";
- "next time do not rupture it near that gas".

If this does not happen, meta cannot save the loop.

## 4. Player-action table

| Axis | Draft answer |
|---|---|
| Players want | get visible gas value/custody out intact |
| Players read | signs of gas, route danger, bubble stress, external gas/reaction risk |
| Players do | detect, choose route, transfer gas to bubble, carry/guide/protect, exit or recover |
| Players risk | rupture, release, reaction, route loss, teammate exposure, losing value |
| World changes | gas moves into bubble, route changes, failure releases gas back to room |
| Co-op need | one player cannot comfortably read, carry, route-control and rescue at once |

## 5. What this proof could prove

If paper-clean and later greybox-clean, this proof can show:

- gas can be desired, not only avoided;
- visible custody is stronger than hidden container stats;
- failure can be world-changing and recoverable;
- carry route can generate co-op;
- reactions/release can matter without full roster/economy;
- "one more" can come from a better plan, not only meta.

## 6. What this proof does not prove

This does not prove:

- fun;
- final gas roster;
- final bubble physics;
- exact capture tool;
- exact containers/cargo system;
- exact economy;
- `ЛЁГКИЕ`;
- final base loop;
- title;
- market hook.

Only two-player greybox can certify fun.

## 7. Blockers to discuss in order

### B1. What is the gas spatially?

Question:
is the gas in first proof a layer, diffuse volume, visible pool, source/flow, room fill, stream, or something else?

Why this matters:
without this, "take gas into bubble" is vague.

### B2. What does the player read before transfer?

Question:
what signs make the action fair before the bubble exists?

Why this matters:
if gas is too obvious, read gameplay dies; if too hidden, failure feels random.

### B3. What is the transfer action?

Question:
what does the player physically do to move gas into bubble?

Why this matters:
именно здесь раньше слово "запузырить" прятало неопределенную механику.

### B4. How do players carry?

Question:
what are hands, bodies, speed, turning, visibility, route constraints and two-player duties?

Why this matters:
if carry is just slow walking, proof fails.

### B5. How does bubble fail?

Question:
impact, pressure, heat, sharp geometry, external gas, over-stress, leak, player mistake?

Why this matters:
failure must be attributable and readable.

### B6. How do reactions enter the minimal proof?

Question:
is there one external gas/condition/reaction front, or only release into clean air first?

Why this matters:
reactions are a known important system and cannot be forgotten again, but first proof must not become full chemistry.

### B7. Why two players?

Question:
what cannot be done by one competent player with enough time?

Why this matters:
mechanic-lens anti-solo refutation.

### B8. Does it create replay pull?

Question:
after one run, do players want another because they know what to do better?

Why this matters:
`ЛЁГКИЕ` waits here.

## 8. Bad paths for the next discussion

- **Generic bottle/canister first** — bad because it hides the gas and pulls container stats.
- **Mission-value playable branch in parallel** — bad because owner already rejected spending time on two mechanics.
- **`ЛЁГКИЕ` now** — bad because it tunes meta before floor value is proven.
- **Full gas roster now** — bad because it creates names and exceptions before jobs.
- **Exact membrane ring now** — bad because it pretends transfer is solved.
- **Title discussion now** — bad because title would start pulling mechanics.

## 9. Recommended next owner discussion

Start with only this:

> Is the promise in section 2 understandable and worth using as the current skeleton, if B1-B8 are explicitly unresolved?

If "yes, as skeleton":
discuss B1 then B2 then B3.

If "no":
rewrite section 2 before touching anything else.

END_OF_FILE: live/indie-game-development/work/mechanics-workbench/core-proof-skeleton-v0.1.md
