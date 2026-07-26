RESULT s-canon-expedition-macrocycle-001 (call: c-canon-expedition-macrocycle-001)
direction: indie-game-development   play: local/canon-forge   node/task: g-d3a8/q-expedition-macrocycle

outcome: |
  `q-expedition-macrocycle` is owner-approved and ready to freeze in the canon repo through the writer.

  Owner direction and sign:
  - Owner accepted the Safe-return spine direction after simplification: "мне в принципе нравиться".
  - Owner identified the missing question: "как заканчиваеться экспедиция", including whether players can "сколько угодно ходить" or whether a timer/hard wipe is needed.
  - Owner rejected a universal timer as default unless it is truly needed: "таймер используетсья много в каких играх и мне не всегда мне нравится, НО если нужно мы сможем и их использовать".
  - Owner accepted the no-universal-timer / return-liability correction: "я с тобой согдасен".
  - Owner explicitly chose not to over-define exact expedition end before floor gameplay exists: "точно сейчас не определишь конец так как нет гемплея внутри экспедиции".
  - Owner signed the freeze direction and next step: "нужно фиксирваоть что мы обсудили и переходить именно к гемпелю на уровне".
  - Owner added floor-loop design steer: gameplay should be "достаточно казуальное понятное не требующее прям много сложных действий НО с глубиной"; it should be strategic, where "если в голове придумал план его было бы не сложно реализвоать".
  - Owner invited critique: "это опять же мои мысли которые ты можешь критиковать я этого ожидаю".

  Canon answer:
  An expedition is one closed risk arc:
  safe zone / staging → unsecured descent → field work / capture / push → commit windows →
  return, retreat, partial disaster, or failure. Value is not banked inside the expedition. Captured gas value
  remains an unbanked state-window/sample/cargo stake until the team crosses a safe-return boundary with
  preserved value.

  The macrocycle has no default global "timer to wipe." Infinite wandering is constrained by escalating,
  readable return liability: cargo pressure, route degradation, shared-air contamination, spent tools/recovery,
  player condition, depth-regime danger, and the fact that the team still owes the return path. Local physical
  timers are allowed only as properties of specific cargo, route windows, emergency systems, or recovery windows.

  Retreat is a valid extraction decision, not automatic failure. Failure means no safe return at the macrocycle
  level; exact death, recovery, insurance, save, rollback, and campaign-collapse rules remain downstream.

  `q-floor-loop` is now the next major gameplay question. It must decide what players actually do inside one
  floor/layer, with the owner steer that local gameplay should be simple to understand and execute, but
  strategically deep through planning, readable field state, cargo pressure, route decisions, and temporary
  co-op roles.

evidence: |
  Owner evidence:
  - Direction acceptance: "мне в принципе нравиться".
  - Missing-end concern: "как заканчиваеться экспедиция"; "они могут сколько угодно ходить?"; "или будет таймер".
  - Timer preference: "таймер используетсья много в каких играх и мне не всегда мне нравится".
  - Agreement to correction: "я с тобой согдасен".
  - Scope boundary: "точно сейчас не определишь конец так как нет гемплея внутри экспедиции".
  - Freeze sign: "нужно фиксирваоть что мы обсудили".
  - Next gameplay direction: "переходить именно к гемпелю на уровне".
  - Floor-loop craft steer: "достаточно казуальное понятное не требующее прям много сложных действий НО с глубиной";
    "нечто стратегическое"; "если в голове придумал план его было бы не сложно реализвоать".
  - Critique expectation: "это опять же мои мысли которые ты можешь критиковать я этого ожидаю".

  Source evidence read:
  - Canon repo `questions/q-expedition-macrocycle.md`: open macrocycle question; asks entry/descent/work/value/deeper-or-out/return/failure and whether lift/shaft is commit/extract/save spine.
  - Frozen parents: `q-full-game-descent-arc`, `q-between-expeditions-progression`, `q-depth-grammar`,
    `q-cargo-containment-principles`, `q-coop-shape`.
  - Supporting substrate: `q-gas-value-forms`, `q-field-capture-principles`, `q-gas-role`, `q-the-city`.
  - Direction OS `knowledge/mechanic-lenses.md`: mechanic gate requires paper checks first and forbids fun certification before a two-player grey-box.
  - Parent result `live/indie-game-development/history/s-canon-coop-shape-001.md`: q-coop-shape frozen, q-expedition-macrocycle next.
  - Existing `questions/q-floor-loop.md`: open child question waiting on q-expedition-macrocycle.

  Done_when evidence:
  1. owner-chosen macrocycle direction exists and cites owner words;
  2. compact canon answer for `q-expedition-macrocycle` exists;
  3. mechanic craft gate result exists below;
  4. child question graph exists below;
  5. explicit statement of what remains for `q-floor-loop` exists below;
  6. exact state_changes are included below and no repo files were edited by this session.

state_changes: |
  Apply mechanically. This session did not edit either repo.

  1. Direction OS repo: append to `live/indie-game-development/LOG.md`:

     2026-06-28 — canon-forge frozen-ready (g-d3a8/q-expedition-macrocycle, s-canon-expedition-macrocycle-001): owner signed safe-return spine with no default global hard timer. Expedition = safe zone/staging → unsecured descent → field work/capture/push → commit windows → return/retreat/partial disaster/failure. Value banks only after safe return; captured gas value remains unbanked state-window/cargo until returned. Infinite wandering is constrained by readable return liability (cargo pressure, route degradation, shared-air contamination, spent tools/recovery, player condition, depth-regime danger), not a universal wipe clock. Local physical timers allowed only as cargo/route/emergency/recovery properties. Retreat with return is valid, not automatic failure; exact death/recovery/save/failure model deferred. q-floor-loop next: owner steer = casual-readable, not many complex actions, but strategically deep and easy to execute once planned. Paper mechanic gate clean / UNVERIFIED; fun not certified. → history/s-canon-expedition-macrocycle-001.md

  2. Direction OS repo: create `live/indie-game-development/history/s-canon-expedition-macrocycle-001.md`
     containing this full RESULT.

  3. Direction OS repo: `NOW.md` untouched.

  4. Direction OS repo: `TREE.md` untouched.

  5. Direction OS repo: `CHARTER.md` untouched.

  6. Direction OS repo: `knowledge/` untouched.
     No cross-cutting knowledge promotion proposed; the canon card and child question update carry the facts.

  7. Canon repo `C:\projects\gas_coop_game_canon`: replace `questions/q-expedition-macrocycle.md` with exact content:

     ---
     id: q-expedition-macrocycle
     area: mechanic
     status: frozen
     depends_on: [q-full-game-descent-arc, q-between-expeditions-progression, q-depth-grammar, q-cargo-containment-principles, q-coop-shape]
     images: []
     gate:
       consistency_with_parents: true
       safe_return_banking: true
       return_liability_no_global_timer: true
       mechanic_altitude: true
       grows_from_core: true
       interesting_decision: true
       anti_solo_refutation_paper: true
       pillar_pull: true
       field_read_requirement: true
       floor_loop_deferred: true
       paper_only_fun_unverified: true
     created_on: 2026-06-26
     frozen_on: 2026-06-28
     signed_by: owner    # "я с тобой согдасен"; "нужно фиксирваоть что мы обсудили"; no exact end before floor gameplay
     ---

     # Макроцикл экспедиции: один заход от входа до safe return или failure

     ## Ответ (канон)

     **Инварианты — на это сверяется future floor loop, cargo/carry, pressure model, failure/recovery, readiness and final exam:**

     1. **Экспедиция начинается при выходе из safe zone в unsecured descent.**
        Старт экспедиции — не первый pickup и не первый этаж сам по себе. Экспедиция начинается, когда команда покидает
        безопасную границу: поверхность / базу / верхний staging / другой future safe-return node, и входит в пространство,
        где люди, маршрут и газовая ценность снова находятся под риском. Точное название safe zone, spawn flow, lobby,
        save/load implementation and base UI не решаются здесь.

     2. **Одна экспедиция — это закрытая risk-arc, а не набор независимых комнат.**
        Базовая форма:
        `safe zone → descent → floor/layer work → capture/push value → commit windows → return/retreat/partial disaster/failure`.
        Экспедиция может пересекать несколько floors/layers/depth regimes, но этот узел не решает exact floor count, floor
        verbs, rooms, objectives, procedural structure, or encounter tables.

     3. **Safe return — единственная граница banking.**
        Внутри экспедиции value остаётся unbanked stake. Пойманный газ, sample, reaction result, data, route proof, cargo or
        pushed state becomes real progress only after safe return. После safe return он может стать readiness: resource,
        material, tool charge, insurance layer, procedure, money, route confidence, controlled output, or preparation for
        another depth regime.

     4. **Captured value creates return pressure immediately after capture/push.**
        Команда не выиграла, когда "засосала газ в сосуд". Она получила stake. Valuable captured state-window can leak,
        spoil, lose regime, contaminate shared air, demand cooling/isolation, occupy a player/tool role, damage the route,
        force release, or make "one more room" a bad idea. Return is the second half of extraction.

     5. **Push-deeper-or-bank decisions happen at readable commit windows.**
        Commit window — это момент, где команда понимает, что меняет ставку. Typical windows:
        - после удачного capture или regime push: стабилизировать/нести домой или сделать дороже;
        - перед переходом в deeper or harsher depth regime;
        - когда cargo pressure, route state, shared air, player condition, or recovery margin worsens;
        - когда team role coverage is strained: one player carries/holds value, another conditions route/air, another must rescue/anchor;
        - когда safe return is still reachable but another greedy move may make it doubtful.

        Это не меню "bank/push" and not a required pause after every room. Floor loop later decides how these windows are
        surfaced in play.

     6. **No universal expedition hard timer by default.**
        The macrocycle does not freeze a global "20 minutes until wipe" rule. A universal clock easily turns greed/fear into
        schedule racing and can feel like external punishment. The stronger default is readable return liability: the longer
        and deeper the team pushes, especially with valuable cargo, the more it owes the return path.

     7. **Return liability replaces infinite wandering without becoming a hidden timer.**
        Players may try to stay longer, but the expedition should become less rational as liability accumulates:
        - cargo pressure / leak / spoil / instability;
        - route degradation, contamination, blocked bypasses, bad thermal path, or worse return air;
        - spent tools, charges, stabilizers, rescue options, and recovery margins;
        - player condition, downed teammates, carried bodies, occupied hands/body/attention;
        - deeper regime danger and harder re-crossing of already-entered space.

        The point is not "the timer killed us." The point is: "we created a debt to the return route and stayed too long."

     8. **Local physical timers are allowed, but only as properties of concrete states.**
        A cargo sample may hold a hot state for a short window. A vented route may stay passable briefly. An emergency node
        may be unstable. A recovery beacon may keep a rescue window open. These are valid if readable, attributable, and
        tied to cargo/route/system/recovery behavior. They are not the default law of every expedition, and expiry does not
        automatically imply full wipe unless later failure/recovery canon earns it.

     9. **Retreat is a valid expedition end, not automatic failure.**
        A team can return early and bank preserved value. It can also retreat with little or no value, after releasing cargo,
        stabilizing it down, abandoning a push, rescuing a player, or saving future readiness. This can be smart play.
        Greed/fear works only if "go home now" is sometimes correct.

     10. **Failure means no safe return at this altitude; exact consequences are later.**
         If the team does not return, unbanked value is not banked. Ordinary failure may lose cargo, prepared run resources,
         current opportunity, route confidence, or part of the expedition prep without erasing player knowledge. Full-team
         wipe without prepared recovery may be severe, but exact death model, bodies, rescue, insurance, rollback, save/load,
         campaign collapse, or reset boundary belong to `q-recovery-insurance`, `q-failure-stakes`, and later implementation
         questions.

     11. **The shaft/lift is a physical spine, not a solved save/checkpoint system.**
         `q-the-city` already freezes vertical descent through a shaft/lift spine. Here that spine becomes the default physical
         grammar of going down and owing the way back. But this card does not freeze elevator controls, checkpoint rules,
         exact extraction UI, save implementation, powered-lift behavior, or whether an anchor player is required. Lift/shaft
         anchor roles remain future questions.

     12. **Macrocycle hands off to floor loop, not around it.**
         This card defines what a floor/layer must output into the expedition:
         - readable gas/value opportunity;
         - an unbanked captured or pushed state;
         - a reason to return, stabilize, release, rescue, or push deeper;
         - route/air/cargo/player state that can create return liability;
         - temporary co-op role pressure;
         - a clean handoff back to the macrocycle: deeper, bank, retreat, partial disaster, or failure.

         The exact inside-floor verbs, rooms, tools, controls, UI, objectives, encounter timing, carry implementation, and
         fun proof belong to `q-floor-loop` and downstream mechanic questions.

     13. **Owner floor-loop steer carried forward.**
         Future floor gameplay should be understandable and relatively casual in execution: not a large set of fiddly complex
         actions. The intended depth is strategic: players should be able to form a plan in their heads and execute it without
         the controls/mechanics fighting them. This is a design constraint for `q-floor-loop`, not a solved mechanic here.

     ### Проза — простыми словами

     Экспедиция — это не "зачистили комнату и получили награду". Команда выходит из безопасного места, спускается, находит
     или создаёт газовую ценность, а потом должна решить: тащить домой сейчас или рискнуть ещё.

     Пока команда не вернулась, добыча ещё не настоящая награда. Это ставка в руках. Она может течь, портиться, мешать
     маршруту, занимать игрока, ухудшать общий воздух или заставить бросить дальнейшую жадность. Игроки выигрывают не в
     момент capture, а когда люди и ценное состояние дошли до safe return.

     У экспедиции нет базового правила "через 20 минут wipe". Лучше, если давление рождается из самой ситуации. Мы уже
     глубоко. Груз дорогой, но нестабильный. Обратный путь хуже. Один игрок занят сосудом. Один инструмент потрачен. Воздух
     уходит. Ещё одна комната может быть очень плохой идеей. Не таймер убивает экспедицию — экспедицию убивает долг перед
     обратной дорогой.

     Таймеры не запрещены. Но они должны быть физическими и локальными: эта проба держится недолго, этот маршрут открыт
     временно, этот emergency node скоро сорвётся, recovery window закрывается. Это свойства конкретной ставки, а не закон
     всей экспедиции.

     Retreat — нормальный конец. Иногда лучший ход — выйти сейчас и bank. Иногда правильный ход — бросить пробу и спасти
     людей. Иногда команда возвращается почти пустой, но живой и с новым пониманием. Full failure — это когда safe return
     не случился; точные death/recovery/save rules решаются позже.

     ## Образы

     Нет. Узел структурный / mechanic-macrocycle canon; изображение не требуется. StyleBible и визуальный язык не меняются.

     ## Открытые под-вопросы

     - [[q-floor-loop]] (mechanic) — следующий крупный узел: что команда делает внутри одного floor/layer, чтобы gameplay
       был простым для понимания и исполнения, но стратегически глубоким; как floor produces readable opportunities,
       unbanked value, co-op role pressure, local return liability, and handoff back to macrocycle. depends_on:
       q-expedition-macrocycle + q-depth-grammar + q-coop-shape + q-gas-value-forms + q-field-capture-principles +
       q-cargo-containment-principles.
     - [[q-return-liability-pressure-model]] (mechanic) — exact model after floor loop: how cargo pressure, route degradation,
       shared-air contamination, spent recovery/tools, local physical timers and player condition accumulate without a
       universal global hard timer. depends_on: q-expedition-macrocycle + q-floor-loop + q-cargo-containment-principles +
       q-failure-stakes + q-recovery-insurance.
     - [[q-anchor-coordination-role]] (mechanic) — when shaft/lift/control-node support is an optional active role versus a
       spectator/operator anti-pattern. depends_on already includes q-expedition-macrocycle.
     - [[q-cargo-containment]] (mechanic) — concrete carry/container/co-op handling must inherit return liability and safe
       return banking, without turning into busywork.
     - [[q-rescue-release-failure-coupling]] (mechanic/campaign) — how rescue, release, partial retreat, bodies, full wipe and
       recovery stay cooperative and non-betrayal.
     - [[q-failure-stakes]] / [[q-recovery-insurance]] — later exact consequences of no safe return, prepared recovery, campaign
       collapse/reset, and what insurance protects.

     `q-expedition-loop` remains superseded-as-label, not a live mechanic source. After this card, the parent chain for
     `q-floor-loop` is complete enough to forge it. s-canon-015 inside-floor placeholders remain placeholders, not canon.

     ## rejected_alternatives

     - **Universal global hard timer as default** — rejected. It can collapse expedition pressure into schedule racing and
       feels external unless earned by a concrete physical state. Local physical timers remain allowed.
     - **Infinite wandering with no accumulating pressure** — rejected. It kills greed/fear and safe-return stakes. The
       replacement is readable return liability.
     - **Every floor/layer as a local bank checkpoint** — rejected. It contradicts the parent rule that value banks only on
       safe return.
     - **Lift/elevator as solved save/checkpoint/extraction UI here** — rejected by altitude. Shaft/lift is physical spine and
       possible future anchor-role substrate, not a solved implementation.
     - **Retreat equals failure** — rejected. Retreat can be the correct extraction decision.
     - **Full wipe exact death/save/recovery model here** — rejected by altitude; belongs to recovery/failure nodes.
     - **Exact floor verbs, room loop, tools, controls, UI, carry stats, balance or implementation here** — rejected by scope;
       next stop is `q-floor-loop`.
     - **Import s-canon-015 inside-floor placeholders as accepted mechanics** — rejected. They remain placeholders.

     END_OF_FILE: questions/q-expedition-macrocycle.md

  8. Canon repo `C:\projects\gas_coop_game_canon`: replace `questions/q-floor-loop.md` with exact content:

     ---
     id: q-floor-loop
     area: mechanic
     status: open
     depends_on: [q-expedition-macrocycle, q-depth-grammar, q-coop-shape, q-gas-value-forms, q-field-capture-principles, q-cargo-containment-principles]
     images: []
     gate: {}
     created_on: 2026-06-26
     ---
     
     # Петля этажа/слоя: что команда делает после входа на один floor?
     
     ## Вопрос
     
     После входа на один floor/layer, что команда делает moment-to-moment до того, как может продолжить глубже, вынести
     результат, отступить или провалиться?
     
     Нужно найти local gameplay loop, который:
     - достаточно казуальный и понятный, без большого набора сложных действий;
     - стратегический: если команда придумала план в голове, его не должно быть сложно реализовать;
     - создаёт глубину через reading, route, cargo, gas state, push/bank decisions, return liability and temporary co-op roles;
     - outputs cleanly into `q-expedition-macrocycle`: deeper / return / retreat / partial disaster / failure.
     
     ## Наследует
     
     - [[q-expedition-macrocycle]]: expedition boundaries, safe-return banking, no default global hard timer, return liability,
       retreat/failure framing, and handoff requirements.
     - [[q-depth-grammar]]: this floor belongs to a qualitative depth regime, not just a difficulty tier.
     - [[q-coop-shape]]: meaningful/progression value requires temporary team coverage, not solo-with-friends.
     - [[q-gas-value-forms]]: visible gas can be collected; value comes from captured/pushed/stabilized/read state, not raw volume.
     - [[q-field-capture-principles]]: field capture starts with reading a bounded state-window, not vacuuming rooms.
     - [[q-cargo-containment-principles]]: captured value can preserve, pressure, leak, spoil, stabilize, release, break or be lost
       before safe return.
     
     ## Нужно решить
     
     1. The smallest understandable floor phases: enter/read → choose opportunity/plan → split/together roles → capture/work/push →
        stabilize/release/return/deeper.
     2. The minimal verb/tool surface: what players actually do without turning the game into fiddly procedure or UI work.
     3. How strategic planning maps to simple execution: "we have a plan" should not require excessive mechanical complexity to perform.
     4. What a floor contributes to the macrocycle: value opportunity, route change, cargo pressure, recovery cost, readiness signal,
        or reason to retreat.
     5. How players read gas/value/route danger in the field quickly enough to decide.
     6. How temporary co-op roles appear locally: carrier/custody, field conditioning, route/anchor, reader, rescue/release.
     7. How a floor creates local return liability without relying on a universal expedition timer.
     8. Which concrete child mechanic questions are forced next.
     
     ## Boundaries
     
     - Do not decide final gas roster, exact reaction tables, exact room taxonomy, exact object inputs, UI, prices, balance,
       inventory/carry stats, equipment stats, save/recovery implementation, production task breakdown, or architecture.
     - Do not certify fun until later two-player grey-box evidence.
     - Do not import `s-canon-015` inside-floor placeholders as accepted mechanics.
     - Do not solve full failure/death/recovery model here; only produce local outputs into later failure/recovery questions.
     
     ## rejected_alternatives
     
     <->
     
     END_OF_FILE: questions/q-floor-loop.md

  9. Canon repo `C:\projects\gas_coop_game_canon`: add file `questions/q-return-liability-pressure-model.md` with exact content:

     ---
     id: q-return-liability-pressure-model
     area: mechanic
     status: open
     depends_on: [q-expedition-macrocycle, q-floor-loop, q-cargo-containment-principles, q-failure-stakes, q-recovery-insurance]
     images: []
     gate: {}
     created_on: 2026-06-28
     ---
     
     # Return liability pressure model: что заменяет универсальный таймер?
     
     ## Вопрос
     
     После того как known `q-floor-loop`: какая exact pressure model заставляет экспедицию заканчиваться или становиться
     всё опаснее без default global hard timer?
     
     Как cargo pressure, route degradation, shared-air contamination, spent tools/recovery, player condition, local physical
     timers and depth-regime danger combine into readable return liability, and where this hands off to failure/recovery rules?
     
     ## Наследует
     
     - [[q-expedition-macrocycle]]: no universal expedition hard timer by default; pressure comes from return liability.
     - [[q-floor-loop]]: defines actual floor actions and local outputs that can create return liability.
     - [[q-cargo-containment-principles]]: captured value can leak/spoil/stabilize/release/break before safe return.
     - [[q-failure-stakes]]: exact loss scale and failure boundary.
     - [[q-recovery-insurance]]: prepared recovery can protect limited catastrophes but cannot erase fear.
     
     ## Нужно решить
     
     1. Which pressure sources exist mechanically: cargo, route, shared air, player state, tool/recovery spend, depth regime, local events.
     2. Which are visible/diegetic and how players read them without hidden timers or spreadsheet UI.
     3. When local physical timers are allowed: cargo state window, route window, emergency system, recovery window.
     4. What happens when a local window expires: spoil, leak, route loss, forced release, rescue cost, partial failure, or other consequence.
     5. Whether any exceptional global countdown can exist later, and what owner sign/evidence would be required to override the default.
     6. How return liability interacts with safe return, retreat, partial disaster, full failure and recovery insurance.
     
     ## Boundaries
     
     - Do not introduce a universal "timer to wipe" as the default.
     - Do not decide exact death/save/load/rollback implementation.
     - Do not tune numbers, prices, durations, UI, or balance.
     - Do not solve before `q-floor-loop`; pressure needs real local gameplay outputs.
     
     ## rejected_alternatives
     
     <->
     
     END_OF_FILE: questions/q-return-liability-pressure-model.md

  10. Canon repo `C:\projects\gas_coop_game_canon`: update `maps/World.md` mechanically:

      10.1. Replace the existing line:

        - ▶️ [[q-expedition-macrocycle]] — one expedition from entry to saved return/failure; replaces the too-broad historical `q-expedition-loop` label; must place containment return-pressure and safe-return banking boundary. depends_on: q-full-game-descent-arc + q-between-expeditions-progression + q-depth-grammar + q-cargo-containment-principles + q-coop-shape.

      with:

        - ✅ [[q-expedition-macrocycle]] (mechanic/game-structure, frozen 2026-06-28) — one expedition = safe zone/staging → unsecured descent → floor/layer work → capture/push value → commit windows → return/retreat/partial disaster/failure. Value banks only after safe return; captured value is unbanked state-window/cargo until returned. No default universal hard timer: infinite wandering is constrained by readable return liability (cargo pressure, route degradation, shared-air contamination, spent tools/recovery, player condition, depth-regime danger). Local physical timers are allowed only as cargo/route/emergency/recovery properties. Retreat with return is valid, not automatic failure. Shaft/lift = physical spine and future anchor-role substrate, not solved save/checkpoint/elevator UI. Exact floor verbs, death/recovery/save and pressure model deferred. signed_by owner "я с тобой согдасен"; "нужно фиксирваоть что мы обсудили". depends_on: q-full-game-descent-arc + q-between-expeditions-progression + q-depth-grammar + q-cargo-containment-principles + q-coop-shape.

      10.2. Replace the existing line:

        - ▶️ [[q-floor-loop]] — one floor/layer loop after macrocycle. depends_on: q-expedition-macrocycle + q-depth-grammar + q-coop-shape.

      with:

        - ▶️ [[q-floor-loop]] — NEXT: one floor/layer gameplay loop after macrocycle. Must be casual-readable and not require many complex actions, but strategically deep: players can form a plan and execute it without fiddly procedure. Must output readable opportunities, unbanked value, temporary co-op role pressure, local return liability, and handoff to macrocycle: deeper / return / retreat / partial disaster / failure. depends_on: q-expedition-macrocycle + q-depth-grammar + q-coop-shape + q-gas-value-forms + q-field-capture-principles + q-cargo-containment-principles.

      10.3. Under related open questions, after `q-floor-loop`, add:

        - 🆕 [[q-return-liability-pressure-model]] — exact post-floor-loop pressure model that replaces a default global hard timer: cargo pressure, route degradation, shared-air contamination, spent tools/recovery, player condition, local physical timers and failure/recovery handoff. depends_on: q-expedition-macrocycle + q-floor-loop + q-cargo-containment-principles + q-failure-stakes + q-recovery-insurance.

      10.4. Replace the existing pause note:

        `q-expedition-loop` remains PAUSED / superseded-as-label until `q-expedition-macrocycle` is complete. After `q-coop-shape` is applied, `q-depth-grammar`, `q-gas-value-forms`, `q-field-capture-principles`, `q-cargo-containment-principles`, and `q-coop-shape` are complete; `q-expedition-macrocycle` remains incomplete. s-canon-015 inside-floor ideas remain placeholders, not canon.

      with:

        `q-expedition-loop` is now superseded-as-label and remains non-source. After `q-expedition-macrocycle` is applied, the parent chain is complete enough to forge `q-floor-loop` next. s-canon-015 inside-floor ideas remain placeholders, not canon.

captures:
  - Critique guardrail for `q-floor-loop`: "casual/simple" must not become shallow; depth should come from state, route, cargo and team plan, not from many buttons or hidden accounting.
  - Future pressure design risk: too many return-liability axes can become an invisible spreadsheet. `q-return-liability-pressure-model` must make pressure readable and attributable.
  - Local physical timers remain allowed, but every timer must answer: what physical state is changing, how players read it, and why expiry is not arbitrary punishment.
  - Future playtests must specifically watch whether players say "we stayed too long / cargo made return worse" rather than "the game killed us by timer."

decisions_needed: []

play_check:
  - 1 Frame: done — framed `q-expedition-macrocycle` as the mechanic/game-structure question for entry, descent, commit windows, unbanked value, safe-return banking, retreat/failure and floor-loop handoff. Direct frozen parents named: `q-full-game-descent-arc`, `q-between-expeditions-progression`, `q-depth-grammar`, `q-cargo-containment-principles`, `q-coop-shape`. Area = mechanic.
  - 2 Diverge (owner): done — proposed A/B/C; owner accepted A after simplification ("мне в принципе нравиться"), then steered it with the missing ending/timer question: "как заканчиваеться экспедиция", "они могут сколько угодно ходить?", "таймер ... не всегда мне нравится".
  - 3 Draft: done — drafted Safe-return spine with the owner correction: no default global hard timer; expedition pressure comes from readable return liability; exact end/failure implementation deferred until floor gameplay exists.
  - 4 Gate: done — mechanic paper gate clean at macrocycle altitude. Grows-from-core: safe-return/return-liability derives from shared gas field + not-solo extraction + unbanked captured value. Interesting-decision: push/deeper/bank/retreat choices have live tradeoffs and no universal clock dominance. Anti-solo: inherits temporary team coverage from q-coop-shape; exact local proof deferred to q-floor-loop. Pillar-pull: greed↔fear together, no betrayal. Field-read: pressure must be readable through cargo/route/air/player/recovery state. Grey-box not run; fun UNVERIFIED.
  - 5 Illustrate: skipped — structural mechanic/game-structure node; no image required and visual language unchanged.
  - 6 Freeze & grow (owner): done — owner agreed and signed: "я с тобой согдасен"; "нужно фиксирваоть что мы обсудили"; "точно сейчас не определишь конец так как нет гемплея внутри экспедиции"; "переходить именно к гемпелю на уровне". Child graph grown and `q-floor-loop` marked next.

log: |
  2026-06-28 — canon-forge frozen-ready q-expedition-macrocycle: safe-return spine; no default global hard timer; pressure = readable return liability; retreat valid; exact floor gameplay/failure/recovery deferred; q-floor-loop next with owner steer simple/casual-readable but strategically deep.

next: |
  CALL c-canon-floor-loop-001
  to: session
  direction: indie-game-development
  play: local/canon-forge
  node: g-d3a8
  question: q-floor-loop
  parent: s-canon-expedition-macrocycle-001
  surface: any / repo root `C:\my_global_workflow_worktrees\indie-game-development`

  goal: |
    A frozen canon answer exists for the one-floor/layer gameplay loop: what the team actually does after entering a floor,
    how players read opportunities and danger, how they plan and execute with simple understandable actions, how local play
    creates captured value / return liability / co-op role pressure, and how the floor hands off to expedition macrocycle
    states: deeper, return, retreat, partial disaster, or failure.

  context: |
    Read:
    - canon repo `questions/q-floor-loop.md`
    - frozen parents: `q-expedition-macrocycle`, `q-depth-grammar`, `q-coop-shape`, `q-gas-value-forms`,
      `q-field-capture-principles`, `q-cargo-containment-principles`
    - supporting substrate: `q-gas-role`, `q-the-city`, `q-base-logistics-labs-factories`
    - `live/indie-game-development/knowledge/mechanic-lenses.md`
    - parent result `live/indie-game-development/history/s-canon-expedition-macrocycle-001.md`

    Required inherited facts:
    - Value banks only on safe return; captured value remains unbanked until returned.
    - No default global expedition hard timer; pressure should come from readable return liability.
    - Local physical timers are allowed only as properties of concrete cargo/route/emergency/recovery states.
    - Floor gameplay must be casual-readable and not require many complex actions, but strategically deep.
    - If players form a plan in their heads, execution should not be mechanically fiddly.
    - Meaningful/progression-relevant value requires temporary team coverage, not solo-with-friends.
    - Retreat can be correct play; exact failure/recovery implementation remains deferred.
    - `s-canon-015` inside-floor placeholders remain placeholders, not canon.

  boundaries: |
    Do not solve final gas roster, exact reaction tables, full room taxonomy, exact UI, carry controls, container stats,
    equipment stats, prices, balance, save/recovery implementation, implementation architecture, production task breakdown,
    or full death model.
    Do not certify fun without a later two-player grey-box.
    Do not import `s-canon-015` inside-floor placeholders as accepted mechanics.
    Do not make the floor loop a fiddly simulator procedure; owner wants simple readable execution with strategic depth.

  done_when: |
    A local/canon-forge RESULT contains:
    1. owner-chosen floor-loop direction with owner words cited;
    2. compact canon answer for `q-floor-loop`;
    3. mechanic craft gate result, including anti-solo and field-read checks;
    4. child questions forced by the answer;
    5. explicit statement of what remains for downstream concrete verbs/tools/UI/recovery/balance;
    6. exact state_changes only through RESULT.

  return: |
    RESULT with owner evidence, canon answer/checkpoint, proposed child question graph, captures/decisions_needed,
    exact state_changes, and next CALL.

  budget: one session

END_OF_FILE: live/indie-game-development/history/s-canon-expedition-macrocycle-001.md
