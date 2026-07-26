RESULT s-canon-floor-gas-work-verbs-001
direction: indie-game-development
play: local/canon-forge
node/task: g-d3a8/q-floor-gas-work-verbs
call: c-canon-floor-gas-work-verbs-001
parent: s-canon-floor-loop-002

outcome: |
  `q-floor-gas-work-verbs` is ready to freeze.

  Canon answer:
  floor gas work is law-first, not button-list-first. The game gives players a procedural gas sandbox where gas exists in
  the world, can be extracted at practical scales, becomes custody rather than guaranteed loot, changes the floor when
  removed, and creates return liability until safe return.

  The frozen action families are:
  1. Добыть / захватить — pull gas from the field into team custody at chosen scale.
  2. Удержать / нести / держать — keep extracted gas usable while moving, waiting, pushing, stabilizing or returning.
  3. Направить / изолировать / перенаправить — change where gas, people, pressure or return routes can go.
  4. Использовать / обойти condition — work with or around world-causes that change gas.
  5. Стабилизировать / осадить — make gas more returnable for a cost.
  6. Сбросить / выпустить / погасить / бросить — sacrifice gas/value/condition to save people, route, remaining cargo or the run.
  7. Пометить / сообщить / доказать — turn field contact into usable route/source/procedure/condition knowledge.

  Key clarification:
  Anti-vacuum means anti-free-raw-volume-progression, not anti-full-extraction. Players may drain a room, zone, cheap gas,
  expensive gas or an entire valuable opportunity if they pay through world laws: capacity, equipment, time, route, custody,
  condition preservation, risk, co-op coverage and return liability. Raw volume can be useful, especially cheap/common bulk,
  but must not become the universal best progression line.

evidence: |
  Done_when match:
  - smallest action families are defined for capture/push/stabilize/route/condition use-or-avoid/release/learn:
    Добыть/захватить; Удержать/нести/держать; Направить/изолировать/перенаправить; Использовать/обойти condition;
    Стабилизировать/осадить; Сбросить/выпустить/погасить/бросить; Пометить/сообщить/доказать.
  - each action family states visible stake/liability changes in the canon card:
    field gas changes; cargo/custody appears; route/pressure/front changes; condition affects gas/route/cargo;
    stabilization trades value/ceiling/resources/time/route; release saves people/route/run at value cost; mark/prove
    changes future readiness.
  - execution stays simple:
    player plans can be spoken as ordinary operations, e.g. "изолируем комнату, вытягиваем тяжёлый слой, держим холодным,
    не даём смешаться, стабилизируем, уходим"; not a list of micro-buttons.
  - exact tools/scanner/loadout/UI/balance are deferred:
    card explicitly does not decide tools, containers, flasks, capsules, backpacks, capacity, slots, scanner, UI, extraction
    speed, prices, economy, quota/depth walls, processing or implementation.
  - owner explicitly clarified downstream scope before freeze:
    "какие-то конкретные вещи, как нести, как вот отдельные механики работают, там, сброс и так далее, вытечение...
    Сейчас это как бы просто пример, но это будет отдельно прорабатываться".
  - anti-vacuum check passed:
    full extraction is allowed; universal raw-volume-to-progress exploit is forbidden.
  - anti-wiki check passed:
    failure/success must be readable through world causes, not hidden quality numbers.
  - anti-affix check passed:
    active conditions are world-causes/context/modifiers, not numeric stat tags.
  - anti-fiddly-action-list check passed:
    seven families, no exact tool roster or micro-action list.
  - anti-solo-with-friends paper check passed:
    cheap/simple extraction can be solo-handled; meaningful/progression extraction creates team coverage through custody,
    route, condition, stabilization, release/rescue and return pressure.
  - fun not certified:
    card states later two-player grey-box evidence is required.
  - rejected alternatives are listed.
  - owner chose the direction:
    "С твоей рекомендацией согласен."
  - owner signed freeze:
    "можно фризить".

state_changes: |
  Apply mechanically. This session did not edit either repo.

  1. Direction OS repo `github.com/ainazemtsau/my_global_workflow`:
     append to `live/indie-game-development/LOG.md`:

     2026-07-03 — canon-forge freeze (g-d3a8/q-floor-gas-work-verbs, s-canon-floor-gas-work-verbs-001): q-floor-gas-work-verbs frozen as law-first Simple Gas Work verbs. Gas can be extracted from the field at practical scales, including full room/zone/full expensive extraction, if the team pays via world laws: capacity, equipment, time, custody, condition preservation, route, risk, co-op coverage and return liability. Anti-vacuum clarified: it forbids universal free raw-volume progression, not full extraction itself. Seven action families frozen: extract/capture; contain/carry/hold; route/isolate/divert; use/avoid condition; stabilize/settle; release/vent/quench/abandon; mark/call/prove. Exact tools, containers, scanner, UI, loadout, capacity, economy, balance, leakage/release/stabilization specifics and implementation deferred. Owner signed: “можно фризить”. → history/s-canon-floor-gas-work-verbs-001.md

  2. Direction OS repo:
     create `live/indie-game-development/history/s-canon-floor-gas-work-verbs-001.md`
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
     Candidate cross-cutting design note for future review/pulse, not applied directly:
     read_by: q-floor-gas-work-verbs downstream questions; q-cargo-containment; q-field-legibility; q-regime-push-rules;
       q-extraction-economy/progression; two-player grey-box proof.
     note: |
       Anti-vacuum should be read as anti-free-raw-volume-progression, not anti-full-extraction. Full extraction of cheap
       or expensive gas is allowed if world-law costs make it a meaningful operation. Future economy/progression must not
       make safe cheap bulk grind the universal path; future mechanics must price extraction through route/custody/return/
       condition/co-op state, not only flat money/equipment count.

  7. Canon repo `github.com/ainazemtsau/gas_coop_game_canon`:
     replace `questions/q-floor-gas-work-verbs.md` with exact content:

     ---
     id: q-floor-gas-work-verbs
     area: mechanic
     status: frozen
     depends_on: [q-floor-loop, q-floor-board-kernel, q-field-capture-principles, q-cargo-containment-principles]
     images: []
     gate:
       consistency_with_parents: true
       law_first_extraction: true
       full_extraction_allowed: true
       anti_vacuum_clarified: true
       custody_not_loot: true
       stake_liability_change_required: true
       small_action_families: true
       exact_tools_ui_loadout_deferred: true
       anti_affix: true
       anti_wiki_baseline: true
       anti_fiddly_action_list: true
       anti_solo_with_friends_paper: true
       paper_only_fun_unverified: true
     created_on: 2026-07-02
     spawned_by: s-canon-floor-loop-002
     frozen_on: 2026-07-03
     signed_by: owner    # "можно фризить"
     ---

     # Floor gas work verbs: как игроки реально добывают и ведут газ

     ## Ответ (канон)

     Floor gas work строится не на большом списке кнопок.

     Игроки делают простые вещи:

     1. **добывают газ из поля;**
     2. **удерживают добытый газ под ответственностью команды;**
     3. **меняют маршрут, границы и потоки;**
     4. **используют или обходят active conditions;**
     5. **стабилизируют газ за цену;**
     6. **сбрасывают / гасят / бросают газ, если надо спасать run;**
     7. **помечают и доказывают то, что поняли.**

     Глубина появляется не из сложного control set, а из законов мира:

     - газ реально существует в уровне;
     - его можно пытаться добывать в разном масштабе;
     - добыча меняет floor;
     - добытый газ становится custody, а не сразу loot;
     - большой объём создаёт больше проблем;
     - дорогой газ можно вынести весь, но это должно быть трудно не потому, что “игра запретила”, а потому что его полезное
       состояние сложно сохранить;
     - пока команда не вернулась в safe return, value ещё не banked.

     ## Инварианты

     ### 1. Газ можно добывать, если он есть в мире

     Если игроки видят газ, карман, слой, струю, утечку, фронт, residue, загрязнённую смесь или целую комнату газа, игра
     должна исходить из:

     > “Можно попытаться это добыть.”

     Не обязательно получится хорошо. Не обязательно это будет выгодно. Не обязательно команда сможет донести. Но базово газ —
     не декорация.

     Игроки могут добывать:

     - маленькое количество;
     - локальный pocket;
     - нижний/верхний слой;
     - струю из leak;
     - движущийся фронт;
     - остаток после реакции;
     - дешёвый room bulk;
     - дорогой gas deposit;
     - почти весь газ комнаты или зоны, если они реально подготовились.

     То есть **полная выкачка разрешена**.

     Запрещён не сам факт полной выкачки. Запрещён плохой design outcome:

     > “Всегда выгоднее просто пылесосить максимальный объём любого газа.”

     Anti-vacuum значит: **raw volume не должен быть универсальной лучшей progression line**.

     Anti-vacuum не значит: **нельзя выкачать всю комнату**.

     ### 2. Добыча имеет масштаб

     Добыча газа — это не только “проба в маленькой баночке”.

     Есть несколько масштабов.

     **Малый забор.**
     Один игрок может взять немного газа. Это быстро, относительно безопасно, удобно для проверки, раннего value или learning.

     Example:

     > “Берём немного cold gas, смотрим, держится ли он до return.”

     **Средняя добыча.**
     Команда или один игрок забирает pocket, layer, stream, front или другой заметный участок газа.

     Example:

     > “Вытягиваем плотный тяжёлый слой у пола, пока он не смешался с contaminated air.”

     **Большая добыча.**
     Команда может изолировать комнату или зону и выкачать много газа.

     Example:

     > “Чистим комнату от дешёвого газа, потому что нужен bulk и безопасный route.”

     **Полная дорогая добыча.**
     Команда может прийти all-in и попытаться вынести почти весь дорогой газ.

     Example:

     > “Мы закупились, взяли много custody, подготовили route, держим condition, сортируем грязные слои, стабилизируем и
     > тащим всё назад.”

     Это должно быть возможно. Если они всё сделали правильно — пусть получают большой куш.

     Но это должно быть тяжело.

     ### 3. Дорогой газ трудно добывать в большом объёме из-за законов мира

     Не потому что дизайнер сказал:

     > “Нельзя.”

     А потому что законы мира делают это сложным.

     Дорогой газ может быть дорогим из-за:

     - чистоты;
     - плотности;
     - температуры;
     - давления;
     - редкой смеси;
     - active regime;
     - нестабильности;
     - связи с source;
     - cold/hot/pressure/radiation condition;
     - reaction trace;
     - глубины;
     - трудного route;
     - сложного safe return.

     Когда команда вытаскивает маленький объём, сохранить это проще.

     Когда команда пытается забрать много, начинаются проблемы:

     - газ смешивается;
     - теряет температуру;
     - теряет pressure;
     - загрязняется;
     - остывает или перегревается;
     - выходит из active regime;
     - начинает течь;
     - портит air;
     - требует больше вместимости;
     - занимает игроков;
     - ухудшает return;
     - требует сортировки;
     - создаёт риск бросить часть cargo.

     Главный закон:

     > **Чем больше команда хочет забрать, тем сложнее сохранить то, за что этот газ дорогой.**

     Это не hard cap. Это физическая цена.

     ### 4. Добытый газ — это custody, не loot

     Когда игроки добыли газ, они ещё не выиграли.

     Они получили не “награду”, а **груз под ответственностью команды**.

     Пока команда не дошла до safe return, добытый газ может:

     - испортиться;
     - вытечь;
     - смешаться не с тем;
     - потерять regime;
     - стать дешёвым bulk;
     - загрязнить route;
     - ухудшить shared air;
     - занять carrier;
     - потратить ресурсы;
     - заставить вернуться раньше;
     - вынудить release/quench/abandon.

     Добыча — это только первая половина value.

     Вторая половина — удержать и вернуть.

     ### 5. Active condition — это не loot по умолчанию

     Active condition — это причина в мире, которая меняет газ, route, cargo или игроков.

     Это может быть:

     - radiation leak;
     - pressure source;
     - hot leak;
     - cold sink;
     - contaminated bypass;
     - draft shaft;
     - organics;
     - catalyst dust;
     - broken scrubber;
     - compressor;
     - sealed chamber;
     - damaged containment.

     Команда не обязана выносить active condition как предмет.

     Example:

     > В комнате есть radiation source. Игроки не обязательно забирают сам source. Он влияет на nearby gas: делает его
     > ценнее, но менее стабильным. Команда может работать рядом с source, обойти его, использовать для push,
     > стабилизировать результат или уйти.

     Active condition может иногда стать добываемым объектом, но это не default.

     ## Action families

     ### 1. Добыть / захватить

     Смысл для игрока:

     > “Вывести газ из поля под ответственность команды.”

     Это покрывает:

     - маленький забор;
     - pocket;
     - layer;
     - stream;
     - front;
     - residue;
     - room bulk;
     - полную дорогую extraction operation.

     Что меняется в мире:

     - газ в поле уменьшается или двигается;
     - room/zone меняется;
     - у команды появляется cargo;
     - появляется return liability;
     - часть opportunity может исчезнуть;
     - route может стать лучше или хуже.

     Не решаем здесь:

     - точный инструмент;
     - кнопку;
     - контейнер;
     - скорость добычи;
     - вместимость;
     - UI;
     - цены;
     - баланс.

     ### 2. Удержать / нести / держать

     Смысл для игрока:

     > “Сохранить добытый газ в полезном виде, пока мы двигаемся, ждём, пушим, стабилизируем или возвращаемся.”

     Это покрывает:

     - переноску;
     - containment;
     - удержание температуры/давления/чистоты;
     - защиту от смешивания;
     - удержание газа рядом с нужным condition;
     - custody большого объёма.

     Что меняется:

     - один игрок может быть занят;
     - cargo может держаться или портиться;
     - leak может испортить air/route;
     - rescue margin может стать хуже;
     - команда может решить возвращаться раньше.

     ### 3. Направить / изолировать / перенаправить

     Смысл для игрока:

     > “Поменять, куда идут газ, люди, давление или route.”

     Это покрывает:

     - открыть / закрыть путь;
     - изолировать комнату;
     - направить flow;
     - перекрыть vent;
     - пустить газ через другой route;
     - сохранить return lane;
     - пожертвовать одним путём ради другого;
     - сделать большую добычу физически возможной.

     Что меняется:

     - route открывается или закрывается;
     - gas front идёт иначе;
     - pressure меняется;
     - return становится безопаснее или хуже;
     - teammate может получить новую проблему;
     - room может стать пригодной для extraction.

     ### 4. Использовать / обойти condition

     Смысл для игрока:

     > “Работать с причиной в мире, которая меняет газ.”

     Это покрывает:

     - использовать cold pocket;
     - избегать hot leak;
     - держать газ рядом с pressure source;
     - не дать organics загрязнить cargo;
     - использовать radiation для push;
     - обойти contaminated bypass;
     - решить, что condition слишком дорогой для этого run.

     Что меняется:

     - газ становится ценнее, хуже, стабильнее, опаснее, чище, грязнее или активнее;
     - route может ухудшиться;
     - cargo может начать портиться;
     - команда может понять condition;
     - появляется co-op pressure.

     ### 5. Стабилизировать / осадить

     Смысл для игрока:

     > “Сделать газ более returnable, но потерять что-то.”

     Стабилизация не должна быть кнопкой:

     > “Сделать безопасно бесплатно.”

     Она должна быть обменом.

     Возможная цена:

     - ниже value ceiling;
     - меньше push potential;
     - потраченный ресурс;
     - время;
     - худший route;
     - занятый игрок;
     - потерянная возможность взять ещё;
     - необходимость уйти раньше.

     Что меняется:

     - cargo меньше течёт;
     - проще return;
     - ниже риск;
     - но value может стать меньше;
     - команда выбирает bank over greed.

     ### 6. Сбросить / выпустить / погасить / бросить

     Смысл для игрока:

     > “Пожертвовать газом или его ценностью, чтобы сохранить run.”

     Это покрывает:

     - выпустить cargo;
     - vent gas;
     - quench active state;
     - бросить часть добычи;
     - испортить value сознательно;
     - сбросить pressure;
     - отказаться от большого куша;
     - освободить carrier;
     - спасти route или игрока.

     Что меняется:

     - value уменьшается или теряется;
     - route может стать безопаснее;
     - shared air может улучшиться;
     - carrier освобождается;
     - rescue становится возможен;
     - команда возвращается беднее, но живой.

     Release — это не только failure. Иногда это правильный ход.

     ### 7. Пометить / сообщить / доказать

     Смысл для игрока:

     > “Мы поняли что-то полезное, даже если не вынесли много газа.”

     Это покрывает:

     - пометить source;
     - понять condition;
     - доказать procedure;
     - отметить опасный route;
     - понять, что дешёвый bulk тут не стоит риска;
     - понять, как сохранить дорогой газ;
     - подготовить future run;
     - получить route confidence.

     Что меняется:

     - следующая экспедиция становится умнее;
     - команда знает, куда вернуться;
     - становится понятнее, какое оборудование нужно;
     - retreat без cargo может всё равно быть useful.

     ## Как это должно звучать в голове игрока

     Не так:

     > “Я нажимаю кнопку capture state-window.”

     А так:

     > “Тут тяжёлый газ у пола. Если просто тянуть всё подряд, поднимем грязный слой. Давайте изолируем комнату, сначала
     > вытянем чистый нижний слой, держим его холодным, потом решим — берём ещё или уходим.”

     Или:

     > “Этот газ дешёвый. Выкачаем всю комнату, нам нужен bulk и чистый проход.”

     Или:

     > “Этот газ дорогой, но без нормального custody мы его не удержим. Берём мало, доказываем condition, возвращаемся позже
     > с подготовкой.”

     Или:

     > “Мы можем забрать всё, но тогда весь loadout уйдёт под cargo, route назад будет тяжёлый, а если leak начнётся —
     > придётся бросать половину.”

     Это правильная простота: игроки говорят обычными словами, а не управляют таблицей.

     ## Кооперация

     Не каждая добыча должна требовать всю команду.

     Дешёвый газ, маленький объём, ранняя проверка или simple sample могут быть solo-handled.

     Но meaningful extraction должна создавать team pressure:

     - один добывает;
     - один удерживает cargo;
     - один следит за route;
     - один работает с condition;
     - один готовит release/quench/rescue;
     - роли могут меняться;
     - никто не является permanent class.

     Кооп должен рождаться из ситуации:

     > “Один человек не может одновременно добывать большой дорогой газ, держать condition, защищать route, нести cargo и
     > спасать партнёра.”

     ## Scope boundary

     Эта карточка не решает:

     - точные инструменты;
     - контейнеры;
     - колбы;
     - капсулы;
     - рюкзаки;
     - вместимость;
     - цены;
     - слоты;
     - scanner;
     - UI;
     - extraction speed;
     - balance;
     - tier economy;
     - quota/depth walls;
     - processing;
     - exact carry mechanics;
     - exact leakage mechanics;
     - exact release mechanics;
     - exact stabilization mechanics;
     - exact quench mechanics;
     - implementation.

     Можно использовать примеры вроде “колба”, “капсула”, “оборудование”, но только как examples. Не как canon tool roster.

     ## Gate

     - **Consistency with parents** — pass. Inherits Simple Gas Work Loop, Simple Floor Read, field capture principles and
       cargo containment principles without reopening them.
     - **Law-first extraction** — pass. Verbs operate shared sandbox extraction laws, not bespoke button logic.
     - **Full extraction allowed** — pass. Full-room/full-zone/full-expensive extraction is allowed as costly operation.
     - **Anti-vacuum clarified** — pass. Anti-vacuum forbids universal free raw-volume progression, not physical draining.
     - **Custody not loot** — pass. Extracted gas is unbanked custody until safe return.
     - **Stake/liability change required** — pass. Every family changes cargo, route, air, condition, player occupation,
       return pressure or knowledge.
     - **Small action families** — pass. Seven families, no large fiddly action set.
     - **Exact tools/UI/loadout deferred** — pass.
     - **Anti-affix** — pass. Conditions are world-causes, not numeric tags.
     - **Anti-wiki baseline** — pass. Baseline must read causes/consequences in world; exact legibility downstream.
     - **Anti-fiddly-action-list** — pass.
     - **Anti-solo-with-friends paper** — pass. Cheap/simple extraction can be solo; meaningful/progression extraction creates
       temporary team coverage.
     - **Paper-only fun unverified** — pass. Actual fun/interdependence requires later two-player grey-box.

     ## Образы

     Нет. Узел structural mechanic canon; изображение не требуется. StyleBible and exact UI language are not changed.

     ## Открытые под-вопросы

     - [[q-extraction-economy-progression]] (mechanic/economy) — how cheap bulk, tier gaps, floor count, quotas/depth walls,
       processing bottlenecks and progression curves prevent safe bulk grind from carrying the whole game. depends_on:
       q-floor-gas-work-verbs + q-gas-value-forms + q-expedition-macrocycle.
     - [[q-cargo-containment]] (mechanic) — exact carry/container/co-op handling: how extracted gas is physically carried,
       stored, damaged, leaked, spoiled, stabilized, released, sorted, or lost without busywork. depends_on:
       q-floor-gas-work-verbs + q-cargo-containment-principles + q-coop-shape + q-expedition-macrocycle.
     - [[q-field-legibility]] (mechanic/visual) — how players read purity, instability, pressure, contamination, retained
       condition, extraction success/failure and custody state without hidden UI-number quality play. depends_on:
       q-floor-gas-work-verbs + q-floor-board-kernel + q-gas-value-forms + q-field-capture-principles +
       q-cargo-containment-principles.
     - [[q-regime-push-rules]] (mechanic) — exact outcomes when condition/push improves, degrades, destabilizes, contaminates,
       spoils, surges, side-grades, or creates route pressure. depends_on:
       q-floor-gas-work-verbs + q-gas-value-forms + q-field-capture-principles + q-cargo-containment-principles.
     - [[q-extraction-equipment-controls]] (mechanic/UI/equipment) — exact tools, interaction model, containers, rates,
       capacity and controls for extraction without busywork. depends_on:
       q-floor-gas-work-verbs + q-cargo-containment.
     - [[q-two-player-floor-greybox-proof]] (mechanic/playtest) — later evidence gate: does the law-first extraction loop
       actually create readable greed/fear, role pressure, and replay pull for two real players. depends_on:
       q-floor-loop + q-floor-gas-work-verbs + q-field-legibility.

     ## rejected_alternatives

     - **Только маленькие пробы** — отвергнуто. Слишком узко; ломает industrial extraction и sandbox.
     - **Нельзя выкачать всю комнату** — отвергнуто. Это произвольный запрет.
     - **Дорогой газ нельзя полностью добыть** — отвергнуто. Можно, если команда платит цену законами мира.
     - **Raw volume как главный progress loop** — отвергнуто. Это превращает игру в пылесос.
     - **Цена добычи только в деньгах/количестве контейнеров** — отвергнуто. Цена должна быть также в route, risk, custody,
       air, player occupation and return.
     - **Каждая добыча требует full co-op** — отвергнуто. Дешёвое/простое можно solo; meaningful/progression scale давит на
       команду.
     - **Exact tools/UI/loadout/economy здесь** — отвергнуто. Это downstream.
     - **Paper canon доказывает fun** — отвергнуто. Нужен later two-player grey-box.

     END_OF_FILE: questions/q-floor-gas-work-verbs.md

captures: |
  - Future economy/progression must decide how cheap bulk, gas tiers, floor count, quotas/depth walls, processing bottlenecks and progression curves prevent safe low-tier extraction from carrying the whole game.
  - Future containment work must keep examples like flask/capsule/backpack/equipment non-canon until exact carry/container mechanics are forged.
  - Future field-legibility must make extraction failure readable through world causes, not hidden UI-number quality play.
  - Future grey-box must test whether meaningful extraction creates real co-op pressure rather than solo-with-friends.

decisions_needed: |
  none

play_check: |
  1. Frame — done. Exact question framed as `q-floor-gas-work-verbs`; inherited frozen parent canon from `q-floor-loop`,
     `q-floor-board-kernel`, `q-field-capture-principles`, `q-cargo-containment-principles`, plus `q-coop-shape`,
     `q-gas-value-forms`, `q-expedition-macrocycle`. Area named: mechanic.
  2. Diverge (owner) — done. Three directions were presented, then revised through owner critique into law-first
     sandbox extraction. Owner chose the recommendation: "С твоей рекомендацией согласен."
  3. Draft — done. Final canon card drafted above in Russian, with invariants, action families, scope boundary, gates,
     open child questions and rejected alternatives.
  4. Gate — done. Mechanic gate passed on paper: grows from gas field + custody + return; meaningful decisions via
     extraction scale/custody/return tradeoffs; anti-solo paper refutation passes for meaningful extraction; pillar pull
     stays greed/fear/together; field-read requirement deferred to `q-field-legibility`; fun remains unverified until
     two-player grey-box.
  5. Illustrate — skipped. Structural mechanic canon; no image needed. StyleBible and exact UI/visual language unchanged.
  6. Freeze & grow (owner) — done. Owner signed: "можно фризить." Child questions listed in the canon card. Rejected
     alternatives listed.

log: |
  2026-07-03 — canon-forge freeze (g-d3a8/q-floor-gas-work-verbs, s-canon-floor-gas-work-verbs-001): q-floor-gas-work-verbs frozen as law-first Simple Gas Work verbs. Gas can be extracted from the field at practical scales, including full room/zone/full expensive extraction, if the team pays via world laws: capacity, equipment, time, custody, condition preservation, route, risk, co-op coverage and return liability. Anti-vacuum clarified: it forbids universal free raw-volume progression, not full extraction itself. Seven action families frozen: extract/capture; contain/carry/hold; route/isolate/divert; use/avoid condition; stabilize/settle; release/vent/quench/abandon; mark/call/prove. Exact tools, containers, scanner, UI, loadout, capacity, economy, balance, leakage/release/stabilization specifics and implementation deferred. Owner signed: “можно фризить”.

next: |
  await next owner CALL. Suggested next canon-status/actionable child after writer applies this result:
  choose between `q-cargo-containment`, `q-field-legibility`, `q-regime-push-rules`, `q-extraction-economy-progression`, or
  `q-extraction-equipment-controls`, depending on whether the next bottleneck is physical custody, readability, push outcomes,
  economy/progression, or controls/tools.