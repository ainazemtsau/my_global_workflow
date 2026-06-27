RESULT s-canon-gas-value-forms-001 (call: c-canon-gas-value-forms-001)
direction: indie-game-development   play: local/canon-forge   node/task: g-d3a8/q-gas-value-forms
outcome: |
  Owner-frozen canon answer produced for `q-gas-value-forms`.

  Frozen direction:
  `field capture` is the first step of gas value. Players can collect visible gas from the world, but collected gas is not
  automatically valuable loot. Value depends on the gas state, whether the relevant regime is preserved or changed, whether
  the team pushes it into a better state, whether it is stabilized or spoiled, and whether it safely returns to the bank
  boundary. The central chain is:

  field capture → read state → carry as-is or regime-push → stabilize/spoil/surge → return or lose → banked readiness.

  This answer:
  - allows visible gas to be collected from the world;
  - rejects "vacuum up all gas = money";
  - treats raw gas as possible material/sample/charge/stake, not the main product by itself;
  - makes the player's core dilemma legible: take the current result home or risk changing it into something more valuable;
  - keeps randomness only as a readable, influenceable risk, not a slot-machine click;
  - keeps four broad payoff forms: sample, regime output, charge/preparation, knowledge/procedure;
  - explicitly defers exact field-capture rules, containers, rooms, attempts, percentages, UI, recipes, balance, co-op roles,
    floor loop, expedition macrocycle, recovery implementation, and save system.

  `q-coop-shape` remains deferred. This card gives substrate for co-op, but does not solve hard anti-solo pressure.

  `q-expedition-loop` remains PAUSED / superseded-as-label until `q-depth-grammar`, `q-coop-shape`, and
  `q-expedition-macrocycle` are complete. `q-depth-grammar` is already complete; `q-coop-shape` and
  `q-expedition-macrocycle` remain incomplete.

evidence: |
  Owner first pushed that `q-coop-shape` was premature because base mechanics were unclear:
  - "Сначала вот условно вообще общие правила хотя бы к ним прописать ... без привязки к кооперативу"
  - "а потом уже, наверное, кооператив обсуждать"
  - "много незакрытых дыр, чтобы принять решение тут"

  Owner accepted `q-gas-value-forms` as the next question:
  - "В принципе, да, это этот вопрос"
  - "я с тобой согласен, давай следующим вопросом делать"

  Owner corrected the abstract draft toward a gameplay situation:
  - "много условных терминов, которым не дано определения"
  - "нам главное не превратиться в техно-демку"
  - "люди зашли, им сразу должно быть очевидно, что делать"
  - "сложность должна быть не быть в понимании"
  - "мы не можем просто сделать, что ты спускаешься ... и засасываешь все газы"

  Owner proposed the regime-push / casino-like risk idea:
  - "нашли газ"
  - "перевести в другое состояние"
  - "можно сделать, что он либо превращается в более лучшее, либо в более худшее, либо вообще взрывается"
  - "такой прям элемент казино ... хорошо ложится"
  - "элемент случайности нужен, но главное не переборщить"
  - "быть категоричным, скептичным ко мне ... мы сейчас именно ищем лучшую идею"

  Owner chose the regime-stake direction:
  - "Выбор A"

  Owner corrected that gas from visible clouds should be collectible:
  - "складывается впечатление, что ... не могут собрать газ"
  - "почему бы и не, чтобы они могли бы собрать"
  - "вот они идут в коридоре, увидели облако газа"
  - "если газ есть огненный ... почему бы они не могли бы его и собрать"
  - "хорошо, что вот они могут так вот увидеть, и его там собрать"

  Owner approved adding field capture as first step:
  - "Да, добавляй field capture как первый шаг"

  Final owner freeze:
  - "Морозь"

  Inherited frozen parents respected:
  - `q-between-expeditions-progression`: gas value banks only after safe return; before return it can be lost, spoiled,
    released, broken, mixed wrongly, or not delivered.
  - `q-gas-role`: gas is one substrate with regimes following current conditions; collecting an active state does not
    guarantee the same regime persists after conditions change.
  - `q-base-logistics-labs-factories`: raw gas is not the main corporate product; value comes from controlled regime +
    stabilized output; canisters/cassettes exist for samples, calibration, emergency isolation, and delivery to cells.
  - `q-depth-grammar`: value changes by depth regime; readiness is real fit to depth, not key/quota.
  - `s-canon-coop-shape-001`: `q-coop-shape` remains deferred until non-coop gas-value/cargo/readiness substrate is clearer.
  - `s-canon-015`: inside-floor mechanics remain placeholders, not accepted canon.

canon_answer: |
  # `q-gas-value-forms` — Формы газовой ценности: за чем команда реально спускается?

  ## Ответ (канон)

  **Инварианты — на это сверяется вся будущая экономика газа, field capture, cargo/containment, readiness, co-op shape,
  expedition macrocycle and floor loop:**

  1. **Газ в мире собираем.**
     Видимое облако, карман, утечка, холодный остаток, активный горячий режим или загрязнённая смесь могут быть объектом
     сбора. Это базовая связь игрока с системой: "вижу газ → могу попытаться что-то с ним сделать". Иначе газ рискует
     остаться красивой симуляцией, а не игровым материалом.

  2. **Собрать газ ≠ сразу получить ценный лут.**
     Сбор даёт не "деньги из воздуха", а состояние в руках команды: пробу, сырьё, опасный груз, заряд, материал для
     дальнейшего режима, низкоценный результат или начало более дорогой ставки. Полноценная ценность зависит от того,
     какой газ собран, в каком состоянии, насколько он стабилен, чистый ли он, сохранился ли режим, можно ли его довезти
     и есть ли смысл его дальше усиливать.

  3. **Сырой газ может быть полезен, но не является главным товаром.**
     Игроки могут собирать сырой/обычный газ, но игра не должна превращаться в "пылесосим всё подряд и продаём объём".
     Сырой газ может быть материалом, пробой, зарядом, входом в процесс, способом убрать опасность или частью находки.
     Но главная ценность рождается из полезно удержанного, переведённого, стабилизированного или понятого состояния, а не
     из продажи любого объёма.

  4. **Режим может потеряться при сборе.**
     Если игрок собирает "огненное" или активное облако, он не обязательно сохраняет его как "огненный предмет". Газ — один
     субстрат, а его лицо/режим следует текущим условиям: плотность, температура, соседи, катализаторы. Поэтому перенос в
     колбу, контейнер, холодную зону или другую среду может ослабить, изменить, стабилизировать или испортить режим.
     Это не запрет на сбор; это источник gameplay.

  5. **Центральная дилемма: вынести как есть или рискнуть режимом.**
     После сбора команда решает:
     - вынести безопаснее — сохранить текущий результат, стабилизировать и возвращаться;
     - рискнуть жаднее — перевести результат в более ценное состояние через условия места: жар, холод, давление,
       плотность, соседний материал, катализатор, производственную ячейку, quench/clean/control context.

     Чем сильнее команда разгоняет результат, тем выше потенциальная ценность и тем опаснее ошибка.

  6. **Плохой исход — событие в экспедиции, не абстрактный минус.**
     Неудачный сбор или regime push может дать понятное последствие: результат испортился, вытек, сорвался, стал
     нестабильным, загрязнился, взорвался, разбудил газовый карман, ухудшил маршрут, испортил контейнер или сделал возврат
     опаснее. Это должно происходить в мире, а не только в меню как "качество -10%".

  7. **Случайность допустима только как управляемая ставка.**
     Элемент "казино" допустим: команда не обязана заранее знать точный результат попытки усилить газ. Но это не чистая
     слот-машина. Игрок должен понимать, почему риск вырос и как он мог его снизить: выбором условий, глубины, контейнера,
     стабилизации, расходника, времени, маршрута или отказом от жадности.

     Запрещённая форма: нажал кнопку → игра кинула кубик → случайно плюс/минус/взрыв без читаемой причины.

  8. **Ценность должна быть понятна без wiki.**
     Базовое чтение должно идти через мир: холод/жар, давление, звук, цвет, плотность, стрелочные приборы, пломбы, иней,
     конденсат, трещины, нестабильное поведение. Сложность — в решении и исполнении под давлением, а не в изучении скрытой
     таблицы свойств.

  9. **Малый словарь payoff, не экономика из десятков валют.**
     На этой высоте достаточно четырёх форм результата:
     - **Проба** — собранное состояние газа/материала, которое надо сохранить и вынести.
     - **Выход режима** — результат после перевода через условия: обработанный материал, реакционный результат,
       стабилизированный output, полезный остаток.
     - **Заряд/подготовка** — результат, который помогает следующему заходу: инструментальный заряд, защитный слой,
       limited insurance material, подготовка к другому режиму.
     - **Знание/процедура** — доказанный способ повторить режим, безопаснее гасить, читать опасность, пройти глубже или
       готовиться к следующему слою.

     Это не список предметов, не UI и не economy table. Точные товары, рецепты, названия, цены и баланс — later nodes.

  10. **Depth changes what is worth collecting.**
      В cold upper regime ценнее безопасные пробы, калибровка, route confidence, понятные ошибки. В hot working depth ценнее
      active controlled outcomes и результаты режима. В pre-terminus active peak ценнее volatile high-yield results,
      которые тяжело вынести. В cold near-inert terminus ценность меняет тип: deep/frozen yield, особый late-game result /
      answer-bearing value, но не новая grind-currency.

  11. **После safe return ставка становится readiness.**
      Пока команда внутри, собранный/усиленный результат остаётся незакреплённой ставкой: его можно потерять, испортить,
      выпустить, разбить, смешать не с тем или не довезти. После safe return он превращается в прогресс: деньги, материал,
      инструмент, заряд, страховку, route confidence, процедуру, подготовку к следующему режиму или другой слой readiness.

  12. **Кооп пока не решается.**
      Эта карточка даёт материал для `q-coop-shape`, но не решает hard co-op pressure. Идеи вроде "кооперация повышает шанс
      хорошего исхода", "один держит режим, другой собирает", "двое стабилизируют контейнер" остаются seeds, not canon.
      Конкретная anti-solo форма будет отдельным вопросом.

  ### Проза — простыми словами

  Игроки могут собирать газ из мира. Если они идут по коридору и видят облако, утечку, горячий карман или холодный
  остаток, игра не должна отвечать "нет, это просто декорация". Базовая фантазия должна быть прямой: газ существует в мире,
  и команда может попытаться взять его себе.

  Но собранный газ — ещё не гарантированный куш. Важно, что именно игроки взяли. Обычный холодный газ может быть слабой
  пробой. Горячий активный газ может быть ценнее, но в простой колбе быстро потеряет режим или станет опасным.
  Загрязнённая смесь может быть почти мусором без обработки. Редкий глубокий карман может быть очень ценным, но страшным
  для возврата. Сбор — это начало решения, а не конец.

  Дальше команда выбирает: вынести как есть или рискнуть. Можно стабилизировать результат и идти домой. А можно попробовать
  сделать его дороже: перевести через условия комнаты, агрегата, ячейки, горячего места, холодного буфера, давления,
  смешивания или гашения. Это ставка режима. Если получилось — результат ценнее. Если сорвалось — плохой исход происходит
  прямо в экспедиции: газ вытек, стал нестабильным, испортил маршрут, разбудил опасность, взорвался или сделал обратную
  дорогу тяжелее.

  Игроку не нужна wiki, чтобы понять базовое правило: увидел газ → можно взять; понял состояние → реши, стоит ли пушить;
  чем жаднее, тем дороже ошибка; пока не вернулся, это ещё не прогресс.

gate: |
  - Consistency with parents: PASS.
    Field capture does not contradict `q-base-logistics-labs-factories`; canisters/cassettes already exist for samples,
    calibration, emergency isolation, and delivery to cells. Raw gas is not the main product, but it can be collected as
    sample/material/stake.

  - Regime logic: PASS.
    The draft respects `q-gas-role`: active/fiery/cold behavior is a regime following conditions, so capture may preserve,
    weaken, alter, stabilize, or spoil the regime.

  - No vacuum-cleaner loop: PASS.
    The draft explicitly rejects "any gas volume = money". Collected gas has context-dependent value through state,
    stability, purity, regime, containment, risk, and return.

  - Not a tech demo: PASS at paper-canon altitude.
    The chain creates decisions: collect, read state, carry as-is, push regime, stabilize/spoil, return/lose. Paper cannot
    certify fun; grey-box/playtests later must test whether the loop is actually fun.

  - No PoE-lite spreadsheet: PASS.
    The owner seed "like corrupting a thing" is preserved only as "risky state change"; affix economy, currencies, reroll
    mats, wiki crafting and large taxonomy are rejected.

  - Legibility: PASS as requirement.
    The card demands that value/risk be readable through world state, instruments, sound, and gas behavior. It does not
    solve exact VFX/UI/audio language.

  - Mechanic altitude: PASS.
    Not frozen: exact rooms, devices, one/two attempts, percentages, consumables, UI, inventory, container stats, co-op
    roles, floor loop, expedition macrocycle, save/recovery implementation.

  - Co-op deferral: PASS.
    The card gives substrate for `q-coop-shape`, but does not declare hard co-op solved.

rejected_alternatives: |
  - **Сырой газ как основной товар / прямой money per volume** — rejected. Leads to vacuum-cleaner play, tech-demo feel,
    and loss of regime/value depth.
  - **Gas cannot be collected from visible field** — rejected by owner correction. If players see a cloud, pocket, leak, or
    active state, attempting to collect it should be a natural baseline interaction.
  - **Pure slot-machine corrupt** — rejected. Randomness without readable cause/control becomes pasted-on gambling.
  - **PoE-lite economy** — rejected. No large set of currencies, affixes, reroll mats, or wiki-crafting as the value core.
  - **Guaranteed improvement consumable / cheap risk removal** — rejected. Consumables may alter or reduce risk later, but
    cannot erase the greed/fear stake cheaply.
  - **Exact attempts/percentages/rooms/recipes in this card** — rejected by altitude. These belong to later mechanic and
    balance questions.
  - **Solve co-op here** — rejected. Co-op use of field capture/regime push is a later `q-coop-shape` / mechanic-family
    question.

proposed_child_question_graph: |
  Children / follow-up questions forced by this answer:

  1. `q-field-capture-principles` (mechanic)
     Question: how field capture works in principle: what can be collected from visible gas, what state is preserved or
     lost, what makes capture low/high value, and why it does not become a vacuum-cleaner loop.
     Depends_on: `q-gas-value-forms`, `q-gas-role`, `q-cargo-containment-principles` if that exists first or in parallel.
     Boundary: no exact tool stats, inventory UI, capacity numbers, controls, or balance.

  2. `q-regime-push-rules` (mechanic)
     Question: what broad outcomes can happen when a team tries to push a collected result into a more valuable state:
     improve, degrade, destabilize, spoil, surge, side-grade, contaminate route, create dangerous return pressure.
     Depends_on: `q-gas-value-forms`, `q-gas-role`, `q-base-logistics-labs-factories`.
     Boundary: no exact percentages, recipes, rooms, interaction timings, or UI.

  3. `q-cargo-containment-principles` (mechanic)
     Question: how collected gas results are held, leaked, stabilized, damaged, spoiled, carried, released, and lost before
     safe return.
     Depends_on: `q-gas-value-forms`, `q-between-expeditions-progression`, later `q-expedition-macrocycle`.
     Boundary: no inventory UI, container stats, exact carry verbs, or co-op solution.

  4. `q-field-legibility` (mechanic/visual)
     Question: how players read gas state/value/risk without wiki: world signs, sound, density, color, diegetic gauges,
     pressure/temperature signs, instability tells.
     Depends_on: `q-gas-value-forms`, `q-gas-role`, `q-visual-style`.
     Boundary: no production implementation or accessibility pass here.

  5. `q-frontier-readiness` (mechanic/campaign)
     Question: which banked gas-value results actually make the team fit for a deeper regime without keyhunt/quota.
     Depends_on: `q-gas-value-forms`, `q-depth-grammar`, `q-between-expeditions-progression`.

  6. `q-recovery-insurance` (mechanic/campaign)
     Question: which banked gas-value results can become limited recovery/insurance without cheap universal fear removal.
     Depends_on: `q-gas-value-forms`, `q-between-expeditions-progression`.

  7. `q-coop-shape` (mechanic) — later resumed.
     Question: which parts of field capture / regime push / containment / stabilization / return become hard co-op and
     anti-solo.
     Depends_on should inherit this card's substrate conceptually; exact frontmatter update optional for graph hygiene.

  8. `q-expedition-macrocycle` (mechanic) — later.
     Question: where one expedition exposes field capture, push-or-bank decisions, return stake, and safe/banked boundary.
     Depends_on: `q-full-game-descent-arc`, `q-between-expeditions-progression`, `q-depth-grammar`, `q-coop-shape`,
     and now `q-gas-value-forms` as value substrate.

  Guard:
  - `q-expedition-loop` remains PAUSED / superseded-as-label until `q-depth-grammar`, `q-coop-shape`, and
    `q-expedition-macrocycle` are complete.
  - `s-canon-015` inside-floor ideas remain placeholders, not accepted mechanics.

state_changes: |
  Apply the following changes mechanically. The session did not directly edit either repo.

  1. Direction OS repo: append to `live/indie-game-development/LOG.md`:

     2026-06-27 — canon-forge frozen (g-d3a8/q-gas-value-forms, s-canon-gas-value-forms-001): owner froze A with field capture added as first step. Gas value = field capture → read state → carry as-is or regime-push → stabilize/spoil/surge → return or lose → banked readiness. Visible gas can be collected, but collected gas is not automatic loot; value depends on state, preserved/lost regime, stability, purity, push risk, containment, and safe return. Rejects vacuum-cleaner loop, raw-gas-as-main-product, pure slot-machine corrupt, PoE-lite economy, cheap guaranteed improvement, and exact percentages/rooms/UI/balance. Child graph spawned: q-field-capture-principles, q-regime-push-rules, q-cargo-containment-principles, q-field-legibility; existing q-frontier-readiness, q-recovery-insurance, q-coop-shape, q-expedition-macrocycle inherit new substrate. q-coop-shape remains deferred; q-expedition-loop remains paused until q-depth-grammar + q-coop-shape + q-expedition-macrocycle are complete. → history/s-canon-gas-value-forms-001.md

  2. Direction OS repo: create `live/indie-game-development/history/s-canon-gas-value-forms-001.md`
     containing this full RESULT.

  3. Direction OS repo: `NOW.md` untouched.

  4. Direction OS repo: `TREE.md` untouched.

  5. Direction OS repo: `CHARTER.md` untouched.

  6. Direction OS repo: `knowledge/` untouched.
     No cross-cutting knowledge promotion proposed yet; the frozen canon card is sufficient source for the next canon
     questions.

  7. Canon repo `C:\projects\gas_coop_game_canon`: replace `questions/q-gas-value-forms.md` with exact content:

     ---
     id: q-gas-value-forms
     area: mechanic
     status: frozen
     depends_on: [q-between-expeditions-progression, q-gas-role, q-base-logistics-labs-factories, q-depth-grammar]
     images: []
     gate:
       consistency_with_parents: true
       regime_logic: true
       no_vacuum_cleaner_loop: true
       no_tech_demo_at_paper_altitude: true
       no_poe_lite_spreadsheet: true
       legibility_requirement: true
       mechanic_altitude: true
       coop_deferred: true
       paper_only_fun_unverified: true
     created_on: 2026-06-26
     frozen_on: 2026-06-27
     signed_by: owner    # "Морозь" — after adding field capture as first step
     ---

     # Формы газовой ценности: за чем команда реально спускается?

     ## Ответ (канон)

     **Инварианты — на это сверяется вся будущая экономика газа, field capture, cargo/containment, readiness, co-op shape,
     expedition macrocycle and floor loop:**

     1. **Газ в мире собираем.**
        Видимое облако, карман, утечка, холодный остаток, активный горячий режим или загрязнённая смесь могут быть объектом
        сбора. Это базовая связь игрока с системой: "вижу газ → могу попытаться что-то с ним сделать". Иначе газ рискует
        остаться красивой симуляцией, а не игровым материалом.

     2. **Собрать газ ≠ сразу получить ценный лут.**
        Сбор даёт не "деньги из воздуха", а состояние в руках команды: пробу, сырьё, опасный груз, заряд, материал для
        дальнейшего режима, низкоценный результат или начало более дорогой ставки. Полноценная ценность зависит от того,
        какой газ собран, в каком состоянии, насколько он стабилен, чистый ли он, сохранился ли режим, можно ли его довезти
        и есть ли смысл его дальше усиливать.

     3. **Сырой газ может быть полезен, но не является главным товаром.**
        Игроки могут собирать сырой/обычный газ, но игра не должна превращаться в "пылесосим всё подряд и продаём объём".
        Сырой газ может быть материалом, пробой, зарядом, входом в процесс, способом убрать опасность или частью находки.
        Но главная ценность рождается из полезно удержанного, переведённого, стабилизированного или понятого состояния, а не
        из продажи любого объёма.

     4. **Режим может потеряться при сборе.**
        Если игрок собирает "огненное" или активное облако, он не обязательно сохраняет его как "огненный предмет". Газ — один
        субстрат, а его лицо/режим следует текущим условиям: плотность, температура, соседи, катализаторы. Поэтому перенос в
        колбу, контейнер, холодную зону или другую среду может ослабить, изменить, стабилизировать или испортить режим.
        Это не запрет на сбор; это источник gameplay.

     5. **Центральная дилемма: вынести как есть или рискнуть режимом.**
        После сбора команда решает:
        - вынести безопаснее — сохранить текущий результат, стабилизировать и возвращаться;
        - рискнуть жаднее — перевести результат в более ценное состояние через условия места: жар, холод, давление,
          плотность, соседний материал, катализатор, производственную ячейку, quench/clean/control context.

        Чем сильнее команда разгоняет результат, тем выше потенциальная ценность и тем опаснее ошибка.

     6. **Плохой исход — событие в экспедиции, не абстрактный минус.**
        Неудачный сбор или regime push может дать понятное последствие: результат испортился, вытек, сорвался, стал
        нестабильным, загрязнился, взорвался, разбудил газовый карман, ухудшил маршрут, испортил контейнер или сделал возврат
        опаснее. Это должно происходить в мире, а не только в меню как "качество -10%".

     7. **Случайность допустима только как управляемая ставка.**
        Элемент "казино" допустим: команда не обязана заранее знать точный результат попытки усилить газ. Но это не чистая
        слот-машина. Игрок должен понимать, почему риск вырос и как он мог его снизить: выбором условий, глубины, контейнера,
        стабилизации, расходника, времени, маршрута или отказом от жадности.

        Запрещённая форма: нажал кнопку → игра кинула кубик → случайно плюс/минус/взрыв без читаемой причины.

     8. **Ценность должна быть понятна без wiki.**
        Базовое чтение должно идти через мир: холод/жар, давление, звук, цвет, плотность, стрелочные приборы, пломбы, иней,
        конденсат, трещины, нестабильное поведение. Сложность — в решении и исполнении под давлением, а не в изучении скрытой
        таблицы свойств.

     9. **Малый словарь payoff, не экономика из десятков валют.**
        На этой высоте достаточно четырёх форм результата:
        - **Проба** — собранное состояние газа/материала, которое надо сохранить и вынести.
        - **Выход режима** — результат после перевода через условия: обработанный материал, реакционный результат,
          стабилизированный output, полезный остаток.
        - **Заряд/подготовка** — результат, который помогает следующему заходу: инструментальный заряд, защитный слой,
          limited insurance material, подготовка к другому режиму.
        - **Знание/процедура** — доказанный способ повторить режим, безопаснее гасить, читать опасность, пройти глубже или
          готовиться к следующему слою.

        Это не список предметов, не UI и не economy table. Точные товары, рецепты, названия, цены и баланс — later nodes.

     10. **Depth changes what is worth collecting.**
         В cold upper regime ценнее безопасные пробы, калибровка, route confidence, понятные ошибки. В hot working depth
         ценнее active controlled outcomes и результаты режима. В pre-terminus active peak ценнее volatile high-yield results,
         которые тяжело вынести. В cold near-inert terminus ценность меняет тип: deep/frozen yield, особый late-game result /
         answer-bearing value, но не новая grind-currency.

     11. **После safe return ставка становится readiness.**
         Пока команда внутри, собранный/усиленный результат остаётся незакреплённой ставкой: его можно потерять, испортить,
         выпустить, разбить, смешать не с тем или не довезти. После safe return он превращается в прогресс: деньги, материал,
         инструмент, заряд, страховку, route confidence, процедуру, подготовку к следующему режиму или другой слой readiness.

     12. **Кооп пока не решается.**
         Эта карточка даёт материал для `q-coop-shape`, но не решает hard co-op pressure. Идеи вроде "кооперация повышает шанс
         хорошего исхода", "один держит режим, другой собирает", "двое стабилизируют контейнер" остаются seeds, not canon.
         Конкретная anti-solo форма будет отдельным вопросом.

     ### Проза — простыми словами

     Игроки могут собирать газ из мира. Если они идут по коридору и видят облако, утечку, горячий карман или холодный
     остаток, игра не должна отвечать "нет, это просто декорация". Базовая фантазия должна быть прямой: газ существует в мире,
     и команда может попытаться взять его себе.

     Но собранный газ — ещё не гарантированный куш. Важно, что именно игроки взяли. Обычный холодный газ может быть слабой
     пробой. Горячий активный газ может быть ценнее, но в простой колбе быстро потеряет режим или станет опасным.
     Загрязнённая смесь может быть почти мусором без обработки. Редкий глубокий карман может быть очень ценным, но страшным
     для возврата. Сбор — это начало решения, а не конец.

     Дальше команда выбирает: вынести как есть или рискнуть. Можно стабилизировать результат и идти домой. А можно попробовать
     сделать его дороже: перевести через условия комнаты, агрегата, ячейки, горячего места, холодного буфера, давления,
     смешивания или гашения. Это ставка режима. Если получилось — результат ценнее. Если сорвалось — плохой исход происходит
     прямо в экспедиции: газ вытек, стал нестабильным, испортил маршрут, разбудил опасность, взорвался или сделал обратную
     дорогу тяжелее.

     Игроку не нужна wiki, чтобы понять базовое правило: увидел газ → можно взять; понял состояние → реши, стоит ли пушить;
     чем жаднее, тем дороже ошибка; пока не вернулся, это ещё не прогресс.

     ## Образы

     Нет. Узел структурный / mechanic-progression canon; изображение не требуется. StyleBible и визуальный язык не меняются.

     ## Открытые под-вопросы

     - [[q-field-capture-principles]] (mechanic) — как в принципе работает сбор газа из поля: что можно собрать, что теряется
       при сборе, что значит "сохранить режим", почему это не vacuum-cleaner loop. depends_on: q-gas-value-forms + q-gas-role.
     - [[q-regime-push-rules]] (mechanic) — какие общие исходы у попытки усилить собранный результат: улучшился, ухудшился,
       стал нестабильным, сорвался, дал side-grade, загрязнил маршрут. depends_on: q-gas-value-forms + q-gas-role +
       q-base-logistics-labs-factories.
     - [[q-cargo-containment-principles]] (mechanic) — как собранный результат удерживается, течёт, портится,
       стабилизируется, переносится и теряется до safe return. depends_on: q-gas-value-forms +
       q-between-expeditions-progression.
     - [[q-field-legibility]] (mechanic/visual) — как игрок без wiki читает состояние газа/результата через мир, звук,
       приборы и поведение. depends_on: q-gas-value-forms + q-gas-role + q-visual-style.
     - [[q-frontier-readiness]] (mechanic/campaign) — какие banked gas-value results реально делают команду готовой к
       следующему depth regime без keyhunt/quota. depends_on: q-gas-value-forms + q-depth-grammar +
       q-between-expeditions-progression.
     - [[q-recovery-insurance]] (mechanic/campaign) — какие gas-value results могут стать limited recovery/insurance, не
       превращаясь в cheap universal failure removal. depends_on: q-gas-value-forms + q-between-expeditions-progression.
     - [[q-coop-shape]] (mechanic) — later resumed: какие части field capture / regime push / containment / stabilization /
       return становятся hard co-op and anti-solo.
     - [[q-expedition-macrocycle]] (mechanic) — где в одном заходе команда собирает газ, решает push-or-bank, несёт stake
       назад, и где value becomes banked. depends_on: q-full-game-descent-arc + q-between-expeditions-progression +
       q-depth-grammar + q-coop-shape + q-gas-value-forms.

     `q-expedition-loop` остаётся PAUSED / superseded-as-label, пока не заморожены `q-depth-grammar`, `q-coop-shape` и
     `q-expedition-macrocycle`. После этой карточки `q-depth-grammar` и `q-gas-value-forms` выполнены; `q-coop-shape` и
     `q-expedition-macrocycle` ещё нет. s-canon-015 inside-floor ideas остаются placeholders, not canon.

     ## rejected_alternatives

     - **Сырой газ как основной товар / прямой money per volume** — отвергнуто. Ведёт к vacuum-cleaner play, tech-demo feel
       and loss of regime/value depth.
     - **Газ из видимого поля нельзя собирать** — отвергнуто owner-правкой. Если игрок видит облако, карман, утечку или
       активное состояние, попытка собрать должна быть естественным baseline interaction.
     - **Чистый slot-machine corrupt** — отвергнуто. Случайность без читаемой причины/контроля становится приклеенным
       gambling mechanic.
     - **PoE-lite экономика** — отвергнуто. Никаких больших наборов валют, affixes, reroll mats или wiki-crafting как центра
       gas value.
     - **Гарантированное улучшение расходником / дешёвое снятие риска** — отвергнуто. Расходники позже могут менять или
       снижать риск, но не бесплатно отменять greed/fear stake.
     - **Точные попытки/проценты/комнаты/рецепты в этой карточке** — отвергнуто по высоте. Это later mechanic and balance
       work.
     - **Решить кооп здесь** — отвергнуто. Кооп-использование field capture/regime push — later `q-coop-shape` /
       mechanic-family question.

     END_OF_FILE: questions/q-gas-value-forms.md

  8. Canon repo `C:\projects\gas_coop_game_canon`: create `questions/q-field-capture-principles.md` with:
     ---
     id: q-field-capture-principles
     area: mechanic
     status: open
     depends_on: [q-gas-value-forms, q-gas-role]
     images: []
     gate: {}
     created_on: 2026-06-27
     ---

     # Сбор газа из поля: что значит "увидел газ → могу взять"?

     ## Вопрос

     Как в принципе работает field capture: что можно собрать из видимого облака/кармана/утечки/остатка, что теряется при
     сборе, что значит сохранить или потерять режим, и почему сбор не превращается в vacuum-cleaner loop?

     ## Наследует

     - [[q-gas-value-forms]]: газ в мире собираем, но сбор ≠ автоматический лут; ценность зависит от состояния, режима,
       стабилизации и safe return.
     - [[q-gas-role]]: газ — один субстрат; лицо/режим следует условиям.

     ## Нужно решить

     1. Что считается collectible gas state.
     2. Что именно переносится при сборе: вещество, состояние, режим, загрязнение, заряд, след, риск.
     3. Когда режим сохраняется, ослабевает, меняется или портится.
     4. Какие принципиальные ограничения мешают "собрать весь газ".
     5. Как игрок читает, что стоит собирать.

     ## Boundaries

     - Не решать точные инструменты, UI, capacity numbers, container stats, controls, balance.
     - Не решать co-op pressure.
     - Не решать expedition macrocycle или floor loop.

     ## rejected_alternatives

     <->

     END_OF_FILE: questions/q-field-capture-principles.md

  9. Canon repo `C:\projects\gas_coop_game_canon`: create `questions/q-regime-push-rules.md` with:
     ---
     id: q-regime-push-rules
     area: mechanic
     status: open
     depends_on: [q-gas-value-forms, q-gas-role, q-base-logistics-labs-factories]
     images: []
     gate: {}
     created_on: 2026-06-27
     ---

     # Ставка режима: что может случиться при усилении газового результата?

     ## Вопрос

     Какие общие исходы бывают, когда команда пытается перевести собранный газовый результат в более ценное состояние:
     улучшение, ухудшение, нестабильность, срыв, side-grade, загрязнение маршрута, авария — и как это остаётся читаемой
     управляемой ставкой, а не слот-машиной?

     ## Наследует

     - [[q-gas-value-forms]]: central dilemma = carry as-is or risk regime push.
     - [[q-gas-role]]: режим следует условиям; реакции finite/simulable.
     - [[q-base-logistics-labs-factories]]: база = фабрика режимов; regime cells/quench/clean/certify are natural context.

     ## Нужно решить

     1. Broad outcome families for regime push.
     2. How players understand risk before acting.
     3. What makes a bad outcome an in-world event, not menu penalty.
     4. How randomness remains influenceable.
     5. What must remain deferred to balance/prototype.

     ## Boundaries

     - Не решать exact percentages, recipes, room verbs, device list, UI, balance, co-op roles, or floor loop.
     - Не делать PoE-lite crafting system.

     ## rejected_alternatives

     <->

     END_OF_FILE: questions/q-regime-push-rules.md

  10. Canon repo `C:\projects\gas_coop_game_canon`: create or replace `questions/q-cargo-containment-principles.md` with:
      ---
      id: q-cargo-containment-principles
      area: mechanic
      status: open
      depends_on: [q-gas-value-forms, q-between-expeditions-progression]
      images: []
      gate: {}
      created_on: 2026-06-27
      ---

      # Удержание газовой ценности: как результат течёт, портится, стабилизируется и доезжает?

      ## Вопрос

      Как собранный газовый результат удерживается, переносится, протекает, портится, стабилизируется, выпускается или
      теряется до safe return — на уровне принципов, без inventory UI, container stats, exact carry verbs or co-op solution?

      ## Наследует

      - [[q-gas-value-forms]]: collected result is an unbanked stake until safe return.
      - [[q-between-expeditions-progression]]: value banks only after return; before return it can be lost/spoiled/released.

      ## Нужно решить

      1. Broad states of containment: safe, unstable, leaking, spoiled, stabilized, released, broken.
      2. How containment interacts with value and return pressure.
      3. Why carrying value is a decision, not busywork.
      4. What kinds of loss are interesting vs annoying.
      5. What remains for `q-coop-shape` and `q-expedition-macrocycle`.

      ## Boundaries

      - Не решать exact UI, capacity numbers, equipment stats, prices, balance, save/recovery implementation.
      - Не решать co-op pressure.
      - Не define floor loop.

      ## rejected_alternatives

      <->

      END_OF_FILE: questions/q-cargo-containment-principles.md

  11. Canon repo `C:\projects\gas_coop_game_canon`: create `questions/q-field-legibility.md` with:
      ---
      id: q-field-legibility
      area: mechanic
      status: open
      depends_on: [q-gas-value-forms, q-gas-role, q-visual-style]
      images: []
      gate: {}
      created_on: 2026-06-27
      ---

      # Читаемость газовой ценности: как игрок понимает состояние без wiki?

      ## Вопрос

      Как игрок читает состояние, ценность и риск газа/результата через мир: цвет, плотность, звук, давление, температуру,
      стрелочные приборы, пломбы, иней, конденсат, трещины, нестабильное поведение — без hidden spreadsheet and wiki?

      ## Наследует

      - [[q-gas-value-forms]]: value must be legible without wiki.
      - [[q-gas-role]]: gas is a structured field, not uniform fog.
      - [[q-visual-style]]: visual language must stay within accepted style.

      ## Нужно решить

      1. Which state changes must be readable.
      2. Which signals are diegetic/world-first.
      3. How players distinguish valuable, dangerous, unstable, spoiled, and safe-enough states.
      4. What is learned through action rather than tutorial text.

      ## Boundaries

      - Не решать final VFX implementation, accessibility pass, UI polish, or full tutorial.
      - Не solve exact gas roster.

      ## rejected_alternatives

      <->

      END_OF_FILE: questions/q-field-legibility.md

  12. Canon repo `C:\projects\gas_coop_game_canon`: update `maps/World.md` related nodes section:
      - Mark `q-gas-value-forms` as frozen with summary:
        `✅ [[q-gas-value-forms]] (mechanic/economy, frozen 2026-06-27) — gas value starts with field capture: visible gas can be collected, but collected gas is not automatic loot. Value depends on state/regime/stability/purity/push risk/containment/safe return. Core chain = collect → read state → carry as-is or regime-push → stabilize/spoil/surge → return or lose → banked readiness. Rejects vacuum-cleaner loop, raw-gas-as-main-product, pure slot-machine corrupt, and PoE-lite economy. depends_on: q-between-expeditions-progression + q-gas-role + q-base-logistics-labs-factories + q-depth-grammar. signed_by owner "Морозь".`
      - Add open child nodes:
        `▶️ [[q-field-capture-principles]] — what can be collected from visible gas, what state/regime is preserved or lost, and why field capture does not become vacuum-cleaner play. depends_on: q-gas-value-forms + q-gas-role.`
        `▶️ [[q-regime-push-rules]] — broad outcomes and readable risk of trying to improve a collected gas result without slot-machine randomness or exact percentages. depends_on: q-gas-value-forms + q-gas-role + q-base-logistics-labs-factories.`
        `▶️ [[q-cargo-containment-principles]] — how collected gas results leak, spoil, stabilize, carry, release, or get lost before safe return. depends_on: q-gas-value-forms + q-between-expeditions-progression.`
        `▶️ [[q-field-legibility]] — how players read gas state/value/risk through world signs, sound, instruments, and gas behavior without wiki. depends_on: q-gas-value-forms + q-gas-role + q-visual-style.`
      - Keep the guard:
        `q-expedition-loop remains PAUSED / superseded-as-label until q-depth-grammar, q-coop-shape and q-expedition-macrocycle are complete. After q-gas-value-forms is applied, q-depth-grammar and q-gas-value-forms are complete; q-coop-shape and q-expedition-macrocycle remain incomplete. s-canon-015 inside-floor ideas remain placeholders, not canon.`

captures:
  - Owner's correction "visible gas should be collectible" is a major design unlock: the game needs a first obvious action
    against gas before abstract value/cargo/co-op layers can be understood.
  - The value loop should be expressed player-first as "видишь газ → можешь взять → понял состояние → вынести или пушить →
    донести или потерять", not as classification-first terminology.
  - Regime push keeps the useful part of the owner's PoE-corrupt analogy, but should be protected from becoming
    slot-machine / affix-economy / wiki-crafting.
  - Field capture needs its own follow-up because preserving/losing regime during capture is likely a deep design seam.
  - "Syrio/raw gas not main product" must never be read as "gas cannot be collected"; it only means volume alone should not
    be the primary value metric.
  - Paper canon still does not prove fun. Later grey-box must test whether players actually understand and enjoy collect →
    push/bank → return pressure.

decisions_needed: []

play_check: |
  1. Frame — DONE.
     `q-gas-value-forms` framed as: what forms of gas value exist, how field-collected gas can become a valuable expedition
     stake, how value can be found/created/raised/spoiled/banked, and how to avoid tech-demo/vacuum-cleaner/PoE-lite failure.
     Frozen parents named: `q-between-expeditions-progression`, `q-gas-role`, `q-base-logistics-labs-factories`,
     `q-depth-grammar`, plus checkpoint parent `s-canon-coop-shape-001`.

  2. Diverge (owner) — DONE.
     Initial options were too abstract; owner pushed toward a playable situation and regime-risk idea. Owner then selected
     the refined direction: "Выбор A". Owner later corrected the draft to add field capture: "почему бы и не, чтобы они
     могли бы собрать", then approved: "Да, добавляй field capture как первый шаг".

  3. Draft — DONE.
     Draft v2 produced: gas in field is collectible; collected gas is not automatic loot; value depends on state/regime/risk;
     central dilemma = carry as-is or regime-push; bad outcomes are in-world events; randomness must be readable/manageable;
     payoff vocabulary remains small; safe return turns stake into readiness; co-op deferred.

  4. Gate — DONE.
     Gate passed: consistency with parents, regime logic, no vacuum-cleaner loop, no tech-demo at paper altitude,
     no PoE-lite spreadsheet, legibility requirement, mechanic altitude, co-op deferral. Explicit note: paper only, fun
     unverified until grey-box/playtest.

  5. Illustrate — SKIPPED.
     Structural mechanic/progression canon; image not required. StyleBible and visual language unchanged.

  6. Freeze & grow (owner) — DONE.
     Owner signed freeze with: "Морозь". Child graph proposed/spawned: `q-field-capture-principles`,
     `q-regime-push-rules`, `q-cargo-containment-principles`, `q-field-legibility`; existing `q-frontier-readiness`,
     `q-recovery-insurance`, `q-coop-shape`, `q-expedition-macrocycle` inherit the substrate. Canon repo edits are proposed
     only via `state_changes`.

log: |
  2026-06-27 — canon-forge frozen (g-d3a8/q-gas-value-forms, s-canon-gas-value-forms-001): owner froze A with field capture
  added as first step. Gas value = field capture → read state → carry as-is or regime-push → stabilize/spoil/surge → return
  or lose → banked readiness. Visible gas can be collected, but collected gas is not automatic loot; value depends on
  state, preserved/lost regime, stability, purity, push risk, containment, and safe return. Rejects vacuum-cleaner loop,
  raw-gas-as-main-product, pure slot-machine corrupt, PoE-lite economy, cheap guaranteed improvement, and exact
  percentages/rooms/UI/balance. Child graph spawned; q-coop-shape remains deferred; q-expedition-loop remains paused.

next: |
  CALL c-canon-field-capture-principles-001
  to: session
  direction: indie-game-development
  play: local/canon-forge
  node: g-d3a8
  question: q-field-capture-principles
  parent: s-canon-gas-value-forms-001
  surface: any / repo root `C:\my_global_workflow_worktrees\indie-game-development`

  goal: |
    The canon track has an owner-forged answer for `q-field-capture-principles`: what it means to collect visible gas from
    the field, what state/regime is preserved or lost, what makes a collected sample valuable or low-value, and what
    principle prevents "vacuum up all gas" from becoming the dominant loop — without defining exact tools, UI, capacity,
    percentages, room verbs, co-op pressure, floor loop, or implementation.

  context: |
    Direction OS repo:
    - `live/indie-game-development/TREE.md`
    - `live/indie-game-development/history/s-canon-gas-value-forms-001.md`
    - `live/indie-game-development/history/s-canon-coop-shape-001.md`
    - `live/indie-game-development/history/s-canon-depth-grammar-003.md`
    - `live/indie-game-development/plays/canon-forge.md`
    - `live/indie-game-development/knowledge/mechanic-lenses.md`

    Canon repo:
    - `C:\projects\gas_coop_game_canon`
    - `questions/q-north-star.md`
    - `questions/q-gas-role.md`
    - `questions/q-the-city.md`
    - `questions/q-base-logistics-labs-factories.md`
    - `questions/q-between-expeditions-progression.md`
    - `questions/q-depth-grammar.md`
    - `questions/q-gas-value-forms.md`
    - `questions/q-field-capture-principles.md`
    - `maps/World.md`

    Required inherited facts:
    - `q-gas-value-forms`: visible gas can be collected; collection is baseline interaction; collected gas is not automatic
      loot; value depends on state/regime/stability/purity/push risk/containment/safe return. Core chain: collect → read
      state → carry as-is or regime-push → stabilize/spoil/surge → return/lose → banked readiness.
    - `q-gas-role`: gas is one substrate; face/regime follows current conditions (density, temperature, neighbors,
      catalysts); collecting an active state may preserve, weaken, change, stabilize, or spoil the regime.
    - `q-base-logistics-labs-factories`: canisters/cassettes exist for samples/calibration/emergency isolation/delivery;
      raw gas is not the main product; value comes from controlled regime + stabilized output.
    - `q-between-expeditions-progression`: value banks only after safe return.
    - `s-canon-coop-shape-001`: do not solve hard co-op before substrate mechanics are clearer.

  boundaries: |
    Do not define exact capture tools, container stats, capacity numbers, UI, controls, percentages, room verbs, equipment
    stats, balance, co-op roles, floor loop, expedition macrocycle, save/recovery implementation, or implementation
    architecture.
    Do not make "collect all gas" optimal.
    Do not make visible gas uncollectible by default.
    Do not solve `q-coop-shape`.
    Do not treat s-canon-015 inside-floor ideas as accepted mechanics.

  done_when: |
    A local/canon-forge RESULT or checkpoint contains:
    1. a framed `q-field-capture-principles` question with inherited frozen parents named;
    2. owner-chosen direction or checkpointed owner pushback;
    3. a compact canon answer or explicit split if too broad;
    4. child questions forced by the answer, especially exact capture tools, containment/cargo, field legibility,
       regime-preservation, and co-op coupling if deferred;
    5. explicit statement that `q-coop-shape` remains deferred until non-coop gas-value/cargo/readiness substrate is clearer;
    6. explicit statement that `q-expedition-loop` remains paused until `q-depth-grammar`, `q-coop-shape`, and
       `q-expedition-macrocycle` are complete;
    7. exact state_changes only through RESULT.

  return: |
    RESULT with owner evidence, canon answer/checkpoint, proposed child question graph, captures/decisions_needed, exact
    state_changes, and next CALL.

  budget: one session

END_OF_FILE: live/indie-game-development/history/s-canon-gas-value-forms-001.md
