RESULT s-canon-floor-board-kernel-001 (call: c-canon-floor-board-kernel-001)
direction: indie-game-development
play: local/canon-forge
node/task: g-d3a8/q-floor-board-kernel
parent: s-canon-floor-loop-001

outcome: |
  `q-floor-board-kernel` is frozen.

  Canon answer:
  floor/cluster uses the Simple Floor Read kernel:
  "where are we → what local environment is here → what active conditions are visible/suspected → what can we try → what is confirmed only in the field."

  The card freezes:
  - floor/cluster as a simple readable situation, not a room list or numeric affix sheet;
  - place = physical function and affordances;
  - environment = local cluster regime, not a strict cold→warm→hot depth staircase;
  - active conditions = readable world-causes, not stat modifiers;
  - multiple active conditions allowed if the one-sentence read remains simple;
  - pre-entry/read/scanning information helps prepare but must not solve the floor before entry;
  - field confirmation teaches the meaning of conditions through consequences;
  - cold remains valuable as preservation/read/stabilize/quench/control, including deeper local cold pockets;
  - hot remains tempting but not always better because it worsens custody/route/return/risk;
  - base cannot cheaply replace field-value creation;
  - exact tools, scanner UI, loadout, gear loss, room verbs, balance, and implementation remain deferred.

evidence: |
  Done_when match:
  - invariants define place/environment/active-conditions/intel/actionable-read;
  - owner direction is reflected:
    - owner corrected environment: "не обязательно делать, что наверху всегда какой-то холод... могут попасться и холодные";
    - owner required simplicity: "у нас должна еще стать во главу угла вообще во всем... простота";
    - owner accepted the Simple Floor Read direction: "я согласен с твоим вариантом";
    - owner requested not to freeze exact tools/scanner/loadout yet: "мы ещё не определились с инструментами, будут они или нет";
    - owner requested a future question for intel/detail level: "уровень разведки, это как будто отдельный вопрос";
    - owner signed freeze: "Морозим".
  - anti-affix check passed: active conditions are world-causes, not numeric tags.
  - anti-wiki check passed: baseline learns through field consequences; expert mastery/min-max remains allowed.
  - anti-chaos check passed: multiple active conditions allowed only if one-sentence read remains simple.
  - anti-hotter-always-better check passed: cold has positive systemic jobs; hot has yield but also custody/route/return cost.
  - anti-base-crafting-collapse check passed: base prepares/processes; field creates the living stake through local state-window + conditions + risk + return.
  - relationship to `q-floor-loop` is explicit: this card provides substrate; `q-floor-loop` can now define moment-to-moment play.
  - rejected alternatives are listed in the frozen card.
  - owner signed freeze in-session: "Морозим".

state_changes: |
  Apply mechanically. This session did not edit either repo.

  1. Direction OS repo `github.com/ainazemtsau/my_global_workflow`:
     append to `live/indie-game-development/LOG.md`:

     2026-07-01 — canon-forge freeze (g-d3a8/q-floor-board-kernel, s-canon-floor-board-kernel-001): q-floor-board-kernel frozen as Simple Floor Read. Floor/cluster = place + local environment + known/suspected active conditions + pre-entry read/field confirmation + simple actionable read. Environment is local and non-monotonic, not strict cold→warm→hot depth staircase. Active conditions are world-causes, not numeric affixes; multiple conditions allowed if one-sentence read remains simple. Baseline avoids wiki/spreadsheet; mastery/min-max allowed. Cold remains valuable; hot not always better; base cannot cheaply replace field-value creation. q-floor-loop is now unblocked for canon-forge. → history/s-canon-floor-board-kernel-001.md

  2. Direction OS repo:
     create `live/indie-game-development/history/s-canon-floor-board-kernel-001.md`
     containing this full RESULT.

  3. Direction OS repo:
     `NOW.md` untouched.
     Canon track remains parallel; no active bet/task change.

  4. Direction OS repo:
     `TREE.md` untouched.

  5. Direction OS repo:
     `CHARTER.md` untouched.

  6. Direction OS repo:
     `knowledge/` untouched.
     Candidate process/craft rule captured below, not applied directly.

  7. Canon repo `github.com/ainazemtsau/gas_coop_game_canon`:
     replace `questions/q-floor-board-kernel.md` with exact content:

     ---
     id: q-floor-board-kernel
     area: mechanic
     status: frozen
     depends_on: [q-expedition-macrocycle, q-depth-grammar, q-coop-shape, q-gas-value-forms, q-field-capture-principles, q-cargo-containment-principles]
     images: []
     gate:
       consistency_with_parents: true
       simple_not_primitive: true
       anti_affix: true
       anti_wiki_baseline: true
       anti_chaos: true
       anti_hotter_always_better: true
       anti_base_crafting_collapse: true
       q_floor_loop_substrate: true
       scope_boundary: true
       paper_only_fun_unverified: true
     created_on: 2026-06-29
     frozen_on: 2026-07-01
     signed_by: owner    # "Морозим"
     ---

     # Floor-board kernel: простое чтение одного floor/cluster

     ## Ответ (канон)

     **Инварианты — на это сверяется будущий floor loop, floor intel, loadout/prep, field legibility, opportunity grammar, cargo/return pressure and implementation:**

     1. **Floor/cluster — это простая читаемая ситуация, а не список комнат или affixes.**
        Один floor/cluster должен читаться игроками как:

        `где мы → какая тут локальная среда → какие условия видны или подозреваются → что можно попробовать → что подтвердится только в поле`.

        Это не numeric-affix карточка вроде:
        `Morgue / Cold / Toxic +2 / Rare +3 / Volatile +1`.

        Правильная форма:
        "Это морг. Тут холодная среда. Известна органика, подозревается утечка давления. Значит, здесь может быть
        стабильная проба, но есть риск загрязнения или leak-срыва. В поле надо подтвердить источник."

        "Карточка" здесь означает модель информации, а не frozen UI. Exact screen/UI belongs to `q-floor-intel-levels`.

     2. **Базовые элементы floor read: место / среда / активные условия / разведданные / actionable read.**
        - **Место** — physical function and affordances.
        - **Среда** — local regime of the cluster.
        - **Активные условия** — readable world-causes that change gas, route, cargo, tools, players, salvage or return decisions.
        - **Разведданные** — what is known, suspected, hidden, or field-confirmed.
        - **Actionable read** — simple enough-to-act understanding, not full solution.

        This is internal canon language. The player-facing feel should remain simple: read the floor, prepare lightly, enter,
        confirm, learn, take/push/leave.

     3. **Место отвечает за физические affordances.**
        Место is the physical/function layer: morgue, storage, compressor room, laboratory, shaft/lift node, service bypass,
        medical bay, processing cell, logistics corridor.

        It answers:
        - what doors, vents, pipes, chambers, containers, machines, bodies, records, passages and control points exist here;
        - where value/sample/opportunity might be;
        - where route/cargo/return problems can emerge;
        - where a player can make a simple mistake or a smarter play.

        Место is not a tier by itself. The same place type can play differently under different local environments and active
        conditions.

     4. **Среда — локальный режим cluster, не жёсткая лестница глубины.**
        Environment is not locked to "upper = cold, lower = warm, deeper = always hot."

        Depth affects probability and baseline, but local environment can vary:
        - early floors are often colder and simpler;
        - deeper floors are often warmer/hotter/more active;
        - a warm or hot zone can contain a cold room, cold sink, quench corridor or preserved cold pocket;
        - a cold zone can contain a hot leak or pressure anomaly;
        - a cold pocket deeper down can be a valuable tool, complication, or route/cargo problem, not an easy-mode patch.

        This preserves the parent rule: depth is qualitative regime, not a numeric difficulty ladder; place/function and regime
        are separate axes.

     5. **Среда должна быть грубо читаема до входа.**
        Before entry, players should have at least a coarse read of local environment.

        Examples of later possible signal words:
        cold / warm / hot / unstable / quiet-near-inert / pressure-heavy / drafty / contaminated-looking.

        Exact vocabulary, UI, scanner categories, and reveal rules are deferred. The invariant is narrower:
        players should not enter completely blind about the local environment.

     6. **Active conditions are world-causes, not numeric modifiers.**
        An active condition is a concrete thing or state in the world:
        pressure leak, broken cold chamber, organic material/blood/biomaterial, hot leak, cold sink, contaminated bypass,
        emergency draft, broken containment site, working compressor, catalyst dust, sealed clean chamber.

        It is not:
        `+15% volatility`, `-10% purity`, `rare affix`, `fire modifier`.

        It should be visible, audible, scannable, field-confirmable, or legible through consequence. If the player cannot connect
        the condition to a world cause or consequence, it is a hidden table, not a good condition.

     7. **Multiple active conditions are allowed if the read stays simple.**
        A cluster does not need exactly one dominant condition.

        But it must pass the one-sentence read test:
        - "cold morgue with organics and suspected leak";
        - "hot compressor room with pressure leak and cold service pocket";
        - "warm lab with catalyst dust, broken scrubber and contaminated bypass."

        If baseline play requires a spreadsheet or five hidden interactions before the floor can be understood, the board failed.
        Expert min-max over combinations is allowed; mandatory wiki for ordinary play is not.

     8. **Разведданные are a layer, but exact intel model is deferred.**
        Players may receive floor information before entry and clarify it in the field.

        Information can be:
        known, suspected, partially revealed, misunderstood, hidden, or field-confirmed.

        This card does not freeze:
        - how much information appears pre-entry;
        - whether scanner exists as an item;
        - whether scanners upgrade;
        - what UI categories exist;
        - exact accuracy, probabilities, signal wording, or reveal mechanics.

        Spawned downstream question: `q-floor-intel-levels`.

     9. **Intel helps prepare; it does not solve the floor before entry.**
        Pre-entry read should support lightweight decisions:
        go / avoid / prepare more carefully / expect contamination / expect pressure risk / do not greed-push before confirmation.

        Forbidden form:
        "scan says do recipe A+B+C to get value X."

        Correct form:
        "we know enough not to go blind; real understanding appears inside."

     10. **Actionable read is a working understanding, not a heavy planning phase.**
         Actionable read means players can roughly answer:
         - what is here;
         - why it may be useful;
         - what may go wrong;
         - what must be checked inside;
         - when not to greed.

         It is not a requirement that players spend minutes planning a route before entry.

         Good baseline form:
         "This is cold storage with suspected leak. We enter, check the leak, take the sample if it is stable, and leave or
         stabilize worse if the route is compromised."

     11. **Field confirmation is the main teacher.**
         Players can learn what a condition means by meeting it in play.

         Example:
         First run shows "pressure anomaly suspected." Players open a bypass, pressure changes route, sample starts leaking,
         shared air worsens. After that run, "pressure anomaly" becomes meaningful.

         Baseline learning:
         read environment → see/suspect condition → act → observe consequence.

         Mastery learning:
         infer combinations earlier and optimize preparation, route, greed/push, stabilization and return.

     12. **Cold remains valuable, not only tutorial/easy mode.**
         Cold can provide:
         - better reading;
         - preservation;
         - stabilization;
         - quench/control;
         - safe samples;
         - route confidence;
         - containment help;
         - preserved state-window;
         - near-inert/deep value later.

         A deeper cold pocket can be a valuable systemic tool or complication, not a safe room by default.

     13. **Hot is tempting, but hotter is not always better.**
         Hot / pressure / active environment can raise yield, enable regime push, strengthen reaction output, or create rare active value.

         It must also worsen or complicate at least one meaningful axis:
         containment, stability, route, shared air, return, player safety, purity, time under pressure, rescue margin.

         Correct feel:
         "hotter can be richer, but not always smarter."

     14. **Base cannot cheaply replace field-value creation.**
         Base can prepare the team, improve readiness, process returned value, stabilize returned output, store procedures, and help future runs.

         But it must not cheaply create the same value as the field.

         Field value comes from:
         place + local environment + active conditions + found state-window + capture/push risk + containment + return.

         If the same thing can be made cheaply at base without the field, expedition value collapses.

     15. **Preparation can be lightweight, but exact tools/loadout are not frozen here.**
         Floor read should be useful enough that some preparation can matter.

         This card does not decide:
         scanners as items, containers, tools, slots, gear loss, insurance, prices, extraction-shooter economy, exact loadout screen,
         or whether any specific instrument exists.

         Spawned downstream question: `q-lightweight-expedition-loadout`.

     16. **This kernel is the required substrate for q-floor-loop.**
         This card does not solve moment-to-moment floor play.

         It defines the board that `q-floor-loop` will use:
         place + local environment + active conditions + known/suspected/field-confirmed information + simple actionable read.

         After this card, `q-floor-loop` may define:
         entry, field reading, capture/push/stabilize/return decisions, temporary co-op roles, and handoff to expedition macrocycle.

     ### Проза — простыми словами

     Игроки не должны входить на floor как в абстрактную комнату со скрытыми числами.

     Перед входом они примерно понимают:
     "куда мы идём, какая там среда, какие условия уже видны или подозреваются, что там может быть полезного, что может нас
     наказать."

     Например:
     "Это холодный medical storage. Видна органика, подозревается pressure leak. Значит, там может быть стабильная проба,
     но можно загрязнить её или испортить route. Внутри надо найти источник leak."

     Или:
     "Это горячая компрессорная. Там pressure-heavy среда и неизвестный холодный сигнал. Можно попробовать дорогой push,
     но возвращать результат будет опасно. Холодный pocket может помочь, если мы найдём его."

     Игроки не обязаны знать формулы. Они учатся через заходы. Первый раз condition — это непонятный риск. После столкновения
     оно становится игровым словом:
     "pressure anomaly — это та штука, из-за которой у нас проба потекла и route стал хуже";
     "cold chamber можно использовать, чтобы сохранить state";
     "organics могут дать contamination, а не просто generic danger."

     Базовый игрок понимает:
     "смотри среду, смотри условия, не жадничай вслепую, подтверждай в поле."

     Опытный игрок понимает глубже:
     "эта комбинация place + cold pocket + pressure leak + contaminated bypass даёт шанс на дорогой state, если правильно
     выбрать момент и путь назад."

     ## Образы

     Нет. Узел структурный / mechanic-kernel canon; изображение не требуется. StyleBible and exact UI language are not changed.

     ## Открытые под-вопросы

     - [[q-floor-loop]] (mechanic) — now unblocked: what the team does moment-to-moment inside one floor after this board language
       exists; how it reads, confirms, captures/pushes/stabilizes/returns, creates temporary co-op roles, and hands off to
       expedition macrocycle. depends_on: q-floor-board-kernel + q-expedition-macrocycle + q-depth-grammar + q-coop-shape +
       q-gas-value-forms + q-field-capture-principles + q-cargo-containment-principles.
     - [[q-floor-intel-levels]] (mechanic/UI) — what exactly players see before entry; how detailed environment/conditions are;
       what is known/suspected/hidden; whether scanner/upgrades exist; what field confirmation means; how intel helps prepare
       without solving the floor. depends_on: q-floor-board-kernel.
     - [[q-lightweight-expedition-loadout]] (mechanic/economy) — how pre-entry read affects preparation, equipment, possible
       gear loss and run commitment without heavy buildcraft and without freezing exact tools in board-kernel. depends_on:
       q-floor-board-kernel + q-expedition-macrocycle + q-coop-shape.
     - [[q-floor-opportunity-grammar]] (mechanic) — broad opportunity types a board can produce: capture, push, stabilize,
       route, return pressure, rescue, field confirmation; not exact room verbs or balance. depends_on: q-floor-board-kernel +
       q-gas-value-forms + q-field-capture-principles + q-cargo-containment-principles.
     - [[q-field-legibility]] (mechanic/visual) — how local environment, active conditions and gas/cargo state are read through
       world signs, sound, instruments and behavior without mandatory wiki/spreadsheet. depends_on: q-floor-board-kernel +
       q-gas-value-forms + q-gas-role + q-visual-style + q-field-capture-principles + q-cargo-containment-principles.

     ## rejected_alternatives

     - **Strict cold→warm→hot depth staircase** — rejected by owner. Environment is local; depth affects probability/baseline,
       not a hard monotone ladder.
     - **Cold as only tutorial/easy mode** — rejected. Cold can preserve, stabilize, quench, reveal, enable safe samples,
       support containment, and carry late/deep value.
     - **Hotter always better** — rejected. Hot can raise yield, but must worsen custody/route/return/risk on some axis.
     - **Numeric affix soup** — rejected. Active conditions are world-causes, not stat tags.
     - **Mandatory wiki/spreadsheet for baseline play** — rejected. Baseline players learn through readable field consequences.
     - **No mastery/min-max** — rejected. Expert inference over combinations is allowed and desirable.
     - **Scanner/base intel solves the floor before entry** — rejected. Pre-entry read helps prepare; field confirmation remains
       necessary.
     - **Entering fully blind every time** — rejected. Coarse local environment and some condition signals should be readable
       before entry.
     - **Exactly one dominant condition per cluster** — rejected. Multiple active conditions are allowed if the one-sentence
       read remains simple.
     - **Base crafting replaces expedition value** — rejected. Base prepares/processes; field creates the living stake under
       local conditions and return risk.
     - **Exact tools, scanner UI, loadout, gear loss, prices, balance or implementation in this card** — rejected by scope.
       These are downstream questions.

     END_OF_FILE: questions/q-floor-board-kernel.md

  8. Canon repo:
     replace `questions/q-floor-loop.md` with exact content:

     ---
     id: q-floor-loop
     area: mechanic
     status: open
     depends_on: [q-floor-board-kernel, q-expedition-macrocycle, q-depth-grammar, q-coop-shape, q-gas-value-forms, q-field-capture-principles, q-cargo-containment-principles]
     images: []
     gate: {}
     created_on: 2026-06-26
     last_redirect_on: 2026-06-29
     blocker_resolved_on: 2026-07-01
     unblocked_by: s-canon-floor-board-kernel-001
     ---

     # Петля этажа/слоя: что команда делает после входа на один floor?

     ## Вопрос

     После входа на один floor/layer, что команда делает moment-to-moment до того, как может продолжить глубже, вынести
     результат, отступить или провалиться?

     Нужно найти local gameplay loop, который:
     - достаточно казуальный и понятный, без большого набора сложных действий;
     - стратегический: если команда придумала простой план в голове, его не должно быть сложно реализовать;
     - создаёт глубину через field read, route, cargo, gas state, push/bank decisions, return liability and temporary co-op roles;
     - outputs cleanly into `q-expedition-macrocycle`: deeper / return / retreat / partial disaster / failure.

     ## Blocker resolved

     `s-canon-floor-loop-001` attempted to freeze a loop direction around:
     `read → opportunity → plan → capture/push → custody/return debt → handoff`.

     The owner blocked freeze because this remained too vague and did not yet define the local playable rule substrate:
     - "точных базовых правил ... не хватает"
     - "сам core правил"
     - "всё вот это идет размыто"
     - "не могу четко представить именно игру с этим"
     - "не хватает какой-то именно структуры"

     The blocker is now resolved by frozen `q-floor-board-kernel`.

     The substrate for this question is **Simple Floor Read**:
     a floor/cluster is read as:
     `where are we → what local environment is here → what active conditions are visible/suspected → what can we try → what is confirmed only in the field`.

     Therefore this question should now solve the moment-to-moment loop on top of:
     place + local environment + active conditions + known/suspected/field-confirmed information + simple actionable read.

     ## Наследует

     - [[q-floor-board-kernel]]: required substrate. Floor/cluster = Simple Floor Read; local environment is non-monotonic;
       active conditions are world-causes, not affixes; multiple conditions allowed if one-sentence read stays simple; intel
       helps prepare but field confirms; cold remains valuable and hot is not always better.
     - [[q-expedition-macrocycle]]: expedition boundaries, safe-return banking, no default global hard timer, return liability,
       retreat/failure framing, and handoff requirements.
     - [[q-depth-grammar]]: this floor belongs to qualitative depth regimes, not just a difficulty tier; place/function and
       regime are separate axes.
     - [[q-coop-shape]]: meaningful/progression value requires temporary team coverage, not solo-with-friends.
     - [[q-gas-value-forms]]: visible gas can be collected; value comes from captured/pushed/stabilized/read state, not raw volume.
     - [[q-field-capture-principles]]: field capture starts with reading a bounded state-window, not vacuuming rooms.
     - [[q-cargo-containment-principles]]: captured value can preserve, pressure, leak, spoil, stabilize, release, break or be lost
       before safe return.

     ## Нужно решить

     1. The smallest understandable floor phases after Simple Floor Read.
     2. How the team moves from pre-entry read to field confirmation to simple action.
     3. How strategic planning stays lightweight: players should not need a spreadsheet or long planning phase.
     4. What a floor contributes to macrocycle: value opportunity, route change, cargo pressure, recovery cost, readiness signal,
        retreat reason, or deeper handoff.
     5. How players read gas/value/route danger in the field quickly enough to decide.
     6. How temporary co-op roles appear locally: carrier/custody, field conditioning, route/anchor, reader, rescue/release.
     7. How a floor creates local return liability without relying on a universal expedition timer.
     8. Which exact downstream mechanic questions are forced next.

     ## Boundaries

     - Do not re-open `q-floor-board-kernel`.
     - Do not decide final gas roster, exact reaction tables, exact room taxonomy, exact object inputs, UI, prices, balance,
       inventory/carry stats, equipment stats, save/recovery implementation, production task breakdown, or architecture.
     - Do not certify fun until later two-player grey-box evidence.
     - Do not import `s-canon-015` inside-floor placeholders as accepted mechanics.
     - Do not solve full failure/death/recovery model here; only produce local outputs into later failure/recovery questions.
     - Do not turn floor loop into heavy pre-planning, wiki/spreadsheet calculation, or numeric affix management.
     - Do not assume exact scanner/tool/loadout mechanics; those belong to `q-floor-intel-levels` and `q-lightweight-expedition-loadout`.

     ## rejected_alternatives

     - **Freeze the vague read/opportunity/capture/return-debt draft** — rejected by owner. It was directionally useful but too
       abstract to make the playable game clear.
     - **Define floor loop before floor-board kernel** — rejected. The loop needed a substrate.
     - **One mandatory dominant condition per cluster** — rejected as too rigid. Floors/clusters may have multiple active
       conditions; the requirement is simple actionable read, not a single dominant condition.
     - **Numeric affix soup** — rejected. Active conditions are world causes, not stat tags.
     - **Mandatory wiki/spreadsheet calculation** — rejected. Base play should be readable; deeper mastery/min-max calculation
       is allowed.
     - **Scanner solves the floor before entry** — rejected. Pre-entry intel helps preparation; field confirmation remains.
     - **Unlimited vague conditions** — rejected. New active conditions must be authored systemic ingredients with readable
       causes/effects and checked combinations, not cheap tags.
     - **Exact floor verbs, room loop, tools, controls, UI, carry stats, balance or implementation here** — rejected by scope.

     END_OF_FILE: questions/q-floor-loop.md

  9. Canon repo:
     create `questions/q-floor-intel-levels.md` with exact content:

     ---
     id: q-floor-intel-levels
     area: mechanic
     status: open
     depends_on: [q-floor-board-kernel]
     images: []
     gate: {}
     created_on: 2026-07-01
     spawned_by: s-canon-floor-board-kernel-001
     ---

     # Уровни разведки floor: что игроки знают до входа?

     ## Вопрос

     Что именно игроки видят перед входом на floor/cluster, насколько детально, чем это раскрывается, что считается known /
     suspected / hidden / field-confirmed, и как это помогает подготовиться, не решая floor заранее?

     ## Почему вопрос появился

     `q-floor-board-kernel` заморозил Simple Floor Read и оставил разведку как принцип, но не exact model.

     Owner explicitly requested preserving this as a future question:
     "уровень разведки, это как будто отдельный вопрос, который вообще надо прояснить."

     ## Наследует

     - [[q-floor-board-kernel]]: pre-entry read should expose coarse local environment and some known/suspected active conditions;
       field confirmation remains necessary; exact scanner/tool/UI/upgrades are not frozen.
     - [[q-floor-loop]]: later loop must use intel without becoming heavy planning.
     - [[q-field-legibility]]: field confirmation must be readable in-world, not only through HUD numbers.

     ## Нужно решить

     1. What is always known before entry: place? environment? danger class? value hint?
     2. What can be suspected but not confirmed?
     3. What stays hidden until field confirmation?
     4. Whether there is a scanner, scan action, scanner upgrade, base scan, map screen, or other intel source.
     5. How much detail is healthy before the floor becomes solved.
     6. How players learn condition meanings across runs without mandatory wiki.
     7. How intel supports lightweight preparation/loadout without turning into spreadsheet planning.

     ## Boundaries

     - Do not solve exact tools/loadout/gear loss here unless required by intel.
     - Do not make scanner solve the floor before entry.
     - Do not require mandatory wiki/spreadsheet.
     - Do not decide full UI implementation, exact signal names, balance numbers, percentages, scanner art, or equipment stats.
     - Do not re-open `q-floor-board-kernel`.

     ## rejected_alternatives

     - **Full perfect scan before entry** — rejected by parent. It solves the floor too early.
     - **No pre-entry information at all** — rejected by parent. Simple Floor Read needs coarse environment/condition signals.
     - **Hidden spreadsheet intel** — rejected. Baseline play must learn from readable consequences.
     - **Exact scanner UI/equipment stats in this child seed** — rejected by scope until this question is forged.

     END_OF_FILE: questions/q-floor-intel-levels.md

  10. Canon repo:
      create `questions/q-lightweight-expedition-loadout.md` with exact content:

      ---
      id: q-lightweight-expedition-loadout
      area: mechanic
      status: open
      depends_on: [q-floor-board-kernel, q-expedition-macrocycle, q-coop-shape]
      images: []
      gate: {}
      created_on: 2026-07-01
      spawned_by: s-canon-floor-board-kernel-001
      ---

      # Lightweight expedition loadout: как подготовка перед входом остаётся простой?

      ## Вопрос

      Как pre-entry floor read влияет на подготовку, снаряжение, возможную потерю gear и run commitment, не превращая игру
      в тяжёлый билдкрафтинг и не замораживая exact tools слишком рано?

      ## Почему вопрос появился

      `q-floor-board-kernel` needs pre-entry read to matter, but owner corrected that exact tools are not yet decided:
      "мы ещё не определились с инструментами, будут они или нет."

      Therefore this question is deferred instead of freezing scanners/containers/tools in board-kernel.

      ## Наследует

      - [[q-floor-board-kernel]]: floor read should be enough to prepare lightly, but exact tools/loadout are deferred.
      - [[q-expedition-macrocycle]]: value and gear are at risk until safe return; return liability matters.
      - [[q-coop-shape]]: meaningful/progression value should create temporary team coverage, not solo-with-friends.

      ## Нужно решить

      1. Does the game have explicit pre-run gear choice?
      2. If gear exists, what broad categories matter without exact stats: reading, containment, stabilization, route, rescue, protection?
      3. What can be lost on failure or bad retreat?
      4. How much gear loss is acceptable before it becomes punishing busywork?
      5. How loadout supports co-op roles without permanent classes.
      6. How to stay close to extraction/lightweight prep feel without copying extraction-shooter economy complexity.
      7. How preparation interacts with base readiness, insurance and recovery later.

      ## Boundaries

      - Do not decide exact tool list, slot counts, prices, equipment stats, UI, insurance, repair economy or balance here until this question is forged.
      - Do not make prep phase heavier than the floor.
      - Do not make the right loadout a wiki recipe.
      - Do not require gear for every simple floor interaction.
      - Do not re-open `q-floor-board-kernel`.

      ## rejected_alternatives

      - **Freeze scanner/container/tool list inside q-floor-board-kernel** — rejected by owner correction.
      - **No preparation can ever matter** — rejected because pre-entry read would become decorative.
      - **Heavy buildcraft spreadsheet before every run** — rejected. Prep must be lightweight.
      - **Gear loss as pure punishment with no readable cause** — rejected by parent containment/return-pressure principles.
      - **Permanent classes as the default answer** — rejected by q-coop-shape; roles should be temporary/instrumental.

      END_OF_FILE: questions/q-lightweight-expedition-loadout.md

  11. Canon repo:
      create `questions/q-floor-opportunity-grammar.md` with exact content:

      ---
      id: q-floor-opportunity-grammar
      area: mechanic
      status: open
      depends_on: [q-floor-board-kernel, q-gas-value-forms, q-field-capture-principles, q-cargo-containment-principles]
      images: []
      gate: {}
      created_on: 2026-07-01
      spawned_by: s-canon-floor-board-kernel-001
      ---

      # Floor opportunity grammar: какие возможности создаёт читаемая доска?

      ## Вопрос

      Какие broad opportunity types может создавать floor/cluster после Simple Floor Read — capture, push, stabilize, route,
      return pressure, rescue, field confirmation — без exact room verbs, spawn tables, UI or balance?

      ## Почему вопрос появился

      `q-floor-board-kernel` froze the readable board substrate. `q-floor-loop` now needs to know what kinds of opportunities
      the board can produce, but this should be solved separately from the board kernel if it grows too detailed.

      ## Наследует

      - [[q-floor-board-kernel]]: place + local environment + active conditions + intel/actionable read create the board.
      - [[q-gas-value-forms]]: value comes from state/regime/stability/purity/push risk/containment/safe return, not raw volume.
      - [[q-field-capture-principles]]: capture starts with reading a bounded state-window.
      - [[q-cargo-containment-principles]]: captured value remains under custody and return pressure.

      ## Нужно решить

      1. What broad opportunity families exist at board level.
      2. How an active condition becomes a gameplay opportunity rather than decoration.
      3. How opportunity stays readable without exact recipe tables.
      4. How local environment and condition combinations produce push/stabilize/route/return decisions.
      5. How opportunity grammar feeds q-floor-loop without solving exact room verbs.

      ## Boundaries

      - Do not decide exact room verbs, equipment stats, spawn rates, recipes, UI, prices or balance.
      - Do not create numeric affix categories.
      - Do not require wiki/spreadsheet for baseline play.
      - Do not re-open `q-floor-board-kernel`.

      ## rejected_alternatives

      - **Opportunity-free board taxonomy** — rejected. Board elements must eventually create playable choices, not just labels.
      - **Exact recipe/opportunity table in the board kernel** — rejected by scope.
      - **Affix-based opportunity grammar** — rejected. Opportunities derive from world-causes and state-windows.

      END_OF_FILE: questions/q-floor-opportunity-grammar.md

  12. Canon repo:
      update `maps/World.md`.

      In section `## Связанные узлы (вне world)`, replace the existing two lines for `q-floor-board-kernel` and `q-floor-loop`
      with this block:

      - ✅ [[q-floor-board-kernel]] (mechanic, frozen 2026-07-01) — Simple Floor Read: one floor/cluster reads as
        `where are we → what local environment is here → what active conditions are visible/suspected → what can we try →
        what is confirmed only in the field`. Environment is local and non-monotonic, not a strict cold→warm→hot staircase;
        cold remains useful for reading/preservation/stabilization/quench/control, hot is tempting but not always better.
        Active conditions are world-causes, not numeric affixes; multiple conditions allowed if the one-sentence read remains
        simple. Intel helps prepare but does not solve the floor. Base prepares/processes; field creates the living stake.
        signed_by owner "Морозим". depends_on: q-expedition-macrocycle + q-depth-grammar + q-coop-shape +
        q-gas-value-forms + q-field-capture-principles + q-cargo-containment-principles.
      - ▶️ [[q-floor-loop]] — UNBLOCKED by q-floor-board-kernel. Next: define what team does moment-to-moment on top of
        Simple Floor Read: enter, field-confirm, capture/push/stabilize/return, temporary co-op roles, return liability,
        and handoff to expedition macrocycle. depends_on: q-floor-board-kernel + q-expedition-macrocycle +
        q-depth-grammar + q-coop-shape + q-gas-value-forms + q-field-capture-principles + q-cargo-containment-principles.
      - 🆕 [[q-floor-intel-levels]] — what players see before entry, how detailed local environment/conditions are, what is
        known/suspected/hidden/field-confirmed, and whether scanner/upgrades exist without solving the floor. depends_on:
        q-floor-board-kernel.
      - 🆕 [[q-lightweight-expedition-loadout]] — how pre-entry read affects preparation/equipment/possible gear loss without
        heavy buildcraft or freezing exact tools in board-kernel. depends_on: q-floor-board-kernel +
        q-expedition-macrocycle + q-coop-shape.
      - 🆕 [[q-floor-opportunity-grammar]] — broad opportunity families produced by the board: capture, push, stabilize, route,
        return pressure, rescue, field confirmation; no exact room verbs or balance yet. depends_on: q-floor-board-kernel +
        q-gas-value-forms + q-field-capture-principles + q-cargo-containment-principles.

captures:
  - Process/craft note: add or promote a Simple-not-primitive check for mechanic canon sessions. The desired standard is not "first obvious idea" and not primitive minimalism; it is a mechanic that is hard to find but simple to feel/play/explain. Candidate checklist: one ordinary player sentence; understandable after one run; depth remains after baseline comprehension; no mandatory wiki; expert min-max allowed; cause visible in world, not only HUD/table.
  - Design seed: `q-floor-intel-levels` should preserve owner concern that the amount/detail of floor information before entry may be a major independent design question.
  - Design seed: `q-lightweight-expedition-loadout` should preserve owner interest in lightweight extraction/Lethal-Company-like gear commitment/loss, without assuming exact instruments yet.
  - Design seed: environment is local and non-monotonic. Depth shifts probabilities/baseline, but local cold/hot pockets can appear as meaningful active board elements.
  - Watchpoint: future scanner/intel design must not accidentally create a solved pre-entry puzzle or hidden spreadsheet.
  - Watchpoint: future floor-loop design must keep prep lightweight; "we saw the floor read, chose approach, entered, learned, won/lost" should remain the feel.

decisions_needed: []

play_check:
  - 1 Frame: done. Restated exact question `q-floor-board-kernel`, area = mechanic, and parent canon constraints from `q-expedition-macrocycle`, `q-depth-grammar`, `q-coop-shape`, `q-gas-value-forms`, `q-field-capture-principles`, `q-cargo-containment-principles`, plus redirect findings from `s-canon-floor-loop-001`.
  - 2 Diverge (owner): done. Three directions were proposed: A readable board kernel, B field-opportunity kernel, C intel-first kernel. Owner read A and corrected it toward simplicity and local environment: "я вот вроде как с тобой согласен"; "у нас должна еще стать во главу угла вообще во всем... простота"; "не обязательно делать, что наверху всегда какой-то холод"; "среда будет... могут попасться и холодные."
  - 3 Draft: done. Drafted Simple Floor Read: place + local environment + visible/suspected active conditions + field confirmation + simple actionable read, with exact tools/scanner/loadout deferred.
  - 4 Gate: done. Ran consistency and skeptical checks: anti-affix, anti-wiki, anti-chaos, anti-hotter-always-better, anti-base-crafting-collapse, simple-not-primitive, q-floor-loop substrate, paper-only fun limit.
  - 5 Illustrate: skipped. Structural mechanic kernel; no image needed. StyleBible not relevant and no visual artifact requested.
  - 6 Freeze & grow (owner): done. Owner accepted direction and signed freeze: "Морозим." Child questions spawned: `q-floor-intel-levels`, `q-lightweight-expedition-loadout`, `q-floor-opportunity-grammar`; `q-floor-loop` marked unblocked.

log: |
  2026-07-01 — canon-forge freeze (g-d3a8/q-floor-board-kernel, s-canon-floor-board-kernel-001): q-floor-board-kernel frozen as Simple Floor Read. Floor/cluster = place + local environment + known/suspected active conditions + pre-entry read/field confirmation + simple actionable read. Environment is local and non-monotonic, not strict cold→warm→hot depth staircase. Active conditions are world-causes, not numeric affixes; multiple conditions allowed if one-sentence read remains simple. Baseline avoids wiki/spreadsheet; mastery/min-max allowed. Cold remains valuable; hot not always better; base cannot cheaply replace field-value creation. q-floor-loop is now unblocked for canon-forge.

next: |
  CALL c-canon-floor-loop-002
  to: session
  direction: indie-game-development
  play: local/canon-forge
  node: g-d3a8
  question: q-floor-loop
  parent: s-canon-floor-board-kernel-001
  surface: any / repo root `C:\my_global_workflow_worktrees\indie-game-development`

  goal: |
    A frozen canon answer exists for `q-floor-loop`: what the team does moment-to-moment inside one floor/cluster after
    Simple Floor Read is known; how players enter, field-confirm local environment/active conditions, decide capture/push/
    stabilize/route/return, create temporary co-op roles, generate return liability, and hand off cleanly to the expedition
    macrocycle.

  context: |
    Read:
    - `questions/q-floor-loop.md`
    - `questions/q-floor-board-kernel.md`
    - frozen parents:
      `q-expedition-macrocycle`
      `q-depth-grammar`
      `q-coop-shape`
      `q-gas-value-forms`
      `q-field-capture-principles`
      `q-cargo-containment-principles`
    - Direction OS history:
      `live/indie-game-development/history/s-canon-floor-loop-001.md`
      `live/indie-game-development/history/s-canon-floor-board-kernel-001.md`

    Owner-approved direction from `q-floor-board-kernel`:
    - Use Simple Floor Read as substrate:
      `where are we → what local environment is here → what active conditions are visible/suspected → what can we try →
      what is confirmed only in the field`.
    - Keep simplicity as a core test: simple to feel/play/explain, not primitive.
    - Environment is local and non-monotonic. Do not force strict cold→warm→hot staircase.
    - Active conditions are world-causes, not numeric affixes.
    - Multiple active conditions are allowed if one-sentence read remains simple.
    - Pre-entry read helps prepare; field confirmation remains necessary.
    - Do not freeze exact tools/scanner/loadout unless this loop cannot be stated without a child blocker.
    - Cold remains valuable; hot not always better.
    - Base prepares/processes; field creates the living stake.
    - Maintain skeptical counter-pass.

  boundaries: |
    Do not re-open `q-floor-board-kernel`.
    Do not decide exact full roster of places/environments/conditions/gases/reactions/recipes/scanner UI/room spawn tables/
    equipment stats/balance/implementation.
    Do not turn floor-loop into numeric-affix soup, mandatory wiki/spreadsheet, or heavy pre-planning.
    Do not require exact tools/loadout/scanner model unless a blocker must be spawned.
    Do not certify fun until later two-player grey-box evidence.

  done_when: |
    One frozen canon card for `q-floor-loop` is ready for writer:
    - loop phases are simple and playable on top of Simple Floor Read;
    - field confirmation, capture/push/stabilize/route/return and temporary co-op roles are defined at the right altitude;
    - handoff to expedition macrocycle is explicit;
    - anti-wiki, anti-affix, anti-heavy-planning, anti-solo-with-friends and anti-base-crafting-collapse checks pass;
    - rejected alternatives are listed;
    - owner signs freeze in his words.

  return: RESULT packet with exact canon repo changes and OS log/history changes.
  budget: one session

END_OF_FILE: live/indie-game-development/history/s-canon-floor-board-kernel-001.md
