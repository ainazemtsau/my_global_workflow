RESULT s-canon-between-expeditions-progression-001 (call: c-canon-between-expeditions-progression-001)
direction: indie-game-development   play: local/canon-forge   node/task: g-d3a8/q-between-expeditions-progression

outcome: |
  Owner-frozen canon answer produced for `q-between-expeditions-progression`.

  Frozen direction:
  "Газовая ценность становится прогрессом только после возврата; full-team wipe без заранее подготовленного recovery
  может обрушить кампанию вплоть до нового начала."

  The answer defines between-expedition progression at the correct altitude:
  - players descend for gas value, not abstract coins;
  - gas value may be found already valuable OR made more valuable through risky expedition manipulation;
  - before safe return, captured gas / samples / reaction results / data / cargo are unbanked stakes;
  - after return, gas value becomes readiness: preparation, tools, insurance, recipes, resources, money, route/frontier support,
    or ability to handle deeper regimes;
  - ordinary failure loses unbanked value/prep but does not erase player knowledge;
  - full-team wipe without prepared recovery can be campaign collapse, up to starting over;
  - recovery/insurance must be prepared/banked/charged in advance and cannot become cheap universal fear removal;
  - exact economy, UI, balance, containers, gas roster, recipes, expedition macrocycle, floor loop, co-op verbs, and implementation
    remain deferred.

evidence: |
  Owner supplied the core gas-value direction and asked for skeptical synthesis:
  - "так как у нас газ центральная механика ... чтобы всё крутилось вокруг него"
  - "хорошо, чтобы как раз-таки за газом и спускались"
  - "газ сам и есть ценность"
  - "может быть дешевый газ, который они захотят сделать более дорогим. Может быть дорогой газ сразу"
  - "они могут превратиться в третий, например, более дорогой ... взорваться ... chain reaction"
  - "ты к моим идеям, к мыслям должен относиться критически, скептически"

  Owner accepted the refined direction:
  - "ну я в принципе с тобой согласен сейчас"
  - "я с большим с тобой согласен, как минимум по направлению"

  Owner corrected the failure-stakes altitude:
  - "не сдал квоту за четыре дня ... мне это, конечно, не нравится"
  - "если все погибли и ... нет страховки ... тогда сначала ... все, все, все сначала начинать"
  - "чтобы условно такой хардкорный режим, и он по умолчанию стоит"
  - "но чтобы мы к этому привязывались"

  Final owner freeze choice:
  - "A"

  Inherited frozen parents respected:
  - `q-full-game-descent-arc`: full-game progress = readiness to enter qualitatively different depth regimes, take value,
    and return together; exact loss/save/insurance/economy belonged to this node.
  - `q-north-star`: "Мы рискнули — и вытащили это вместе"; greed-vs-fear = take payoff out vs risk deeper.
  - `q-gas-role`: one substrate/many regimes; gas is danger + loot + spectacle; gas reacts by conditions, not magic will.
  - `q-the-city`: depth gate = environment/readiness, not arbitrary locks/quotas; return path through dangerous depth.
  - `q-base-logistics-labs-factories`: raw gas is not automatically the product; value comes from controlled gas results,
    stabilized outputs, procedures, and readable industrial affordances.

  Craft gate:
  - Consistency: PASS. Keeps full-game progress as readiness to go deeper and return, and does not contradict gas/city canon.
  - Mechanic altitude: PASS. Defines persistence and failure-stake invariants without freezing floor loop, containers, recipes,
    economy numbers, UI, save implementation, or balance.
  - Not contrived: PASS. Progression grows from gas as danger/loot/spectacle and return pressure, not from external quota/keyhunt.
  - Greed↔fear: PASS. The best value is unbanked until return; players can choose to bank, push deeper, or risk making value bigger.
  - Co-op interdependence: PASS-AS-PARENT. Dangerous gas value, shared loss, unstable cargo, reactions, and recovery stakes give
    material to `q-coop-shape`, but the exact anti-solo mechanism is deferred.
  - Tone: PASS. Keeps thriller/greed/fear; rejects arbitrary quota punishment and cheap failure erasure.
  - Scope: PASS. Avoids PoE-lite currency sprawl, Factorio-style base crafting, exact permadeath rules, and premature implementation.

state_changes: |
  Apply the following changes mechanically. The session did not directly edit either repo.

  1. Direction OS repo: append to `live/indie-game-development/LOG.md`:

     2026-06-26 — canon-forge frozen (g-d3a8/q-between-expeditions-progression, s-canon-between-expeditions-progression-001): owner froze A — between-expedition progression = gas value becomes real progress only after safe return. Players descend for gas value: already-valuable gas/state OR cheap/ordinary gas made more valuable through risky expedition manipulation. Before return, captured gas / sample / reaction result / data / cargo = unbanked stake; after return it becomes readiness (prep/tools/insurance/recipes/resources/money/frontier support/depth capability). Ordinary failure loses unbanked value/prep but not player knowledge. Full-team wipe without prepared recovery can be campaign collapse up to new beginning; recovery/insurance must be banked/charged in advance and cannot be cheap universal fear removal. Exact economy/UI/balance/containers/recipes/macrocycle/floor/co-op/save implementation deferred. q-expedition-loop remains paused until q-depth-grammar + q-coop-shape + q-expedition-macrocycle chain is complete. Canon repo changes proposed for writer application. → history/s-canon-between-expeditions-progression-001.md

  2. Direction OS repo: create `live/indie-game-development/history/s-canon-between-expeditions-progression-001.md`
     containing this full RESULT.

  3. Direction OS repo: `NOW.md` / `TREE.md` / `CHARTER.md` untouched.

  4. Direction OS repo: `knowledge/` untouched. No cross-cutting knowledge promotion proposed yet; the frozen canon card is
     sufficient source for the next canon questions.

  5. Canon repo `C:\projects\gas_coop_game_canon`: replace `questions/q-between-expeditions-progression.md` with exact content:

     ---
     id: q-between-expeditions-progression
     area: mechanic
     status: frozen
     depends_on: [q-full-game-descent-arc]
     images: []
     gate:
       consistency: true
       mechanic_altitude: true
       not_contrived: true
       greed_fear: true
       coop_interdependence_parent: true
       tone: true
       scope_boundary: true
     frozen_on: 2026-06-26
     signed_by: owner    # "A" — hard full-wipe risk: gas value banks only on return; wipe without prepared recovery can collapse campaign
     ---

     # Прогресс между экспедициями: что сохраняется, теряется и страхуется?

     ## Ответ (канон)

     **Инварианты — на это сверяется вся будущая экономика, failure model, insurance, экспедиционный макроцикл и floor loop:**

     1. **Главная ценность между экспедициями — газовая ценность, а не абстрактные монеты.**
        Команда спускается за тем, что связано с газом: редким состоянием газа, опасным образцом, результатом реакции,
        рецептом условий, доказанной процедурой, стабилизированным выходом, данными или подготовкой к следующей глубине.
        Деньги могут существовать, но они не являются центром progression.

     2. **Газовая ценность бывает найденной или созданной.**
        Иногда команда находит уже дорогой / редкий / опасный газовый результат, и главная задача — собрать и вынести его.
        Иногда команда находит дешёвое / обычное / неполное состояние и может добровольно сделать его ценнее: изменить
        условия, смешать, нагреть, охладить, провести через рискованную зону или иначе поднять ставку. Этот узел фиксирует
        принцип, но не решает конкретные комнаты, реакции, рецепты и floor loop.

     3. **До безопасного возврата ценность не banked.**
        Пока команда внутри экспедиции, пойманный газ, образец, результат реакции, данные и груз остаются ставкой. Их можно
        потерять, испортить, выпустить, разбить, смешать не с тем или не довезти. Полноценным прогрессом они становятся
        только после возврата в безопасную точку / на поверхность / в базу — точную границу решает
        [[q-expedition-macrocycle]].

     4. **Возврат превращает риск в readiness.**
        Banked результат может стать подготовкой к следующему режиму глубины: ресурсом, инструментом, зарядом, страховкой,
        доказанным рецептом, знанием, доступом к новой подготовке, восстановлением базы/маршрута или деньгами. Точные
        категории экономики, UI, upgrade tree и баланс не решаются здесь.

     5. **Обычный провал теряет незакреплённое, но не стирает всё.**
        Обычная неудача, частичный retreat или смерть без полного кампанийного краха могут потерять unbanked value, груз,
        подготовку захода, расходники и текущий шанс превратить находку в readiness. Player knowledge не стирается: игроки
        могут помнить, что увидели, и часть фактов может сохраниться через аварийные данные или косвенное знание.

     6. **Страх провала держится на возврате.**
        Самая сильная ставка: команда уже получила или создала ценный газовый результат, но ещё не вернулась. Чем ценнее
        результат, тем страшнее дорога назад: можно выйти сейчас и bank, можно рискнуть глубже или усилить результат, но
        провал может забрать всё незакреплённое.

     7. **Full-team wipe без prepared recovery может быть кампанийным крахом.**
        Если вся команда погибает / пропадает в глубине и заранее не была подготовлена recovery-страховка, игра может
        откатить команду очень жёстко — вплоть до нового начала. Это не quota punishment, не таймер долга и не “не успел
        нафармить X за N дней”; это цена полного провала экспедиции в опасной среде. Точная форма reset / отката / rescue
        — отдельный child-вопрос, не этот узел.

     8. **Recovery и insurance должны быть подготовлены заранее и не отменяют страх.**
        Страховка не может быть дешёвым универсальным “провал не считается”. Recovery надо заранее banked / зарядить /
        подготовить через газовую ценность, ресурс базы, установку, протокол или иной ограниченный слой. Она защищает
        конкретную катастрофу или категорию потери, сгорает / тратится / оставляет другую цену и не делает глубокий wipe
        безопасным.

     9. **Прогресс не является keyhunt / quota gate.**
        Глубина не открывается потому, что игроки “собрали X газа для двери” или “выполнили квоту за срок”. Команда идёт
        глубже потому, что стала реально готовее: лучше понимает режимы газа, имеет подготовку, инструменты, страховки,
        маршруты, процедуры и опыт, чтобы войти в другой режим и вернуться.

     10. **Этот узел даёт материал для кооперации, но не решает точные кооп-механики.**
         Опасный газовый груз, shared loss, нестабильные образцы, реакции, переноска, изоляция, давление, охлаждение,
         возврат и recovery stakes создают естественную почву для коопа. Но конкретный механизм “почему это нельзя
         оптимально сделать solo-with-friends” решает [[q-coop-shape]].

     ### Проза — простыми словами

     Между экспедициями прогресс строится вокруг газа. Игроки не просто собирают “деньги в подземелье”. Они находят или
     создают газовую ценность: редкий газ, опасный образец, результат реакции, полезное состояние, данные или способ
     подготовиться к следующей глубине.

     Иногда ценный газ уже есть в глубине, и главная задача — забрать его. Иногда команда может взять более обычный газ и
     сделать его дороже: изменить условия, смешать, провести через опасную зону, поднять ставку. Но пока команда не
     вернулась, это не награда, а риск. Газ может вырваться, испортиться, смешаться, взорваться, разбить маршрут или просто
     не доехать.

     Возврат — момент превращения риска в прогресс. То, что вынесли, становится подготовкой: ресурсом, инструментом,
     страховкой, рецептом, знанием, деньгами или шагом к следующему режиму глубины. Поэтому “выйти сейчас или рискнуть
     ещё” — центральное решение. Не потому, что игра отнимает всё при любой смерти, а потому что лучший результат экспедиции
     ещё надо вытащить.

     Провал не должен стирать всю кампанию при каждой ошибке. Игроки сохраняют опыт и понимание. Но если они не донесли
     ценность, она не считается banked. А если вся команда ушла в мясорубку, погибла в глубине и заранее не подготовила
     recovery, это может быть настоящим кампанийным крахом — вплоть до начала заново. Это не штраф за квоту, а цена того,
     что команда не вернулась и не застраховала полный провал.

     ## Образы

     Нет. Узел структурный / progression-canon; изображение не требуется. StyleBible и визуальный язык не меняются.

     ## Открытые под-вопросы

     - [[q-depth-grammar]] (mechanic) — какие режимы глубины требуют разной readiness; как газовая ценность связана с
       подготовкой к hot working depth, pre-terminus peak и cold near-inert final exam.
     - [[q-coop-shape]] (mechanic) — какая hard co-op pressure делает газовый груз, возврат, recovery и endgame readiness
       структурно не solo-with-friends.
     - [[q-expedition-macrocycle]] (mechanic) — где именно результат становится safe/banked: поверхность, база, лифт,
       checkpoint или другая граница; как one expedition hands off into this progression.
     - [[q-gas-value-forms]] (mechanic/economy) — какие формы газовой ценности существуют: найденный дорогой газ, усиленный
       дешёвый газ, образец, reaction result, recipe, tool charge, insurance, money, preparation.
     - [[q-cargo-containment]] (mechanic) — как работают ёмкости/кассеты/контейнеры/переноска/утечки на уровне принципов,
       без premature tuning.
     - [[q-recovery-insurance]] (mechanic/campaign) — какие recovery-страховки спасают от full-team wipe, как они
       заряжаются/тратятся, что именно защищают и что оставляют под риском.
     - [[q-failure-stakes]] (mechanic/campaign) — точная шкала потерь: обычный провал, частичный retreat, потеря груза,
       тяжёлый wipe, campaign collapse / reset boundary.
     - [[q-frontier-readiness]] (mechanic/campaign) — что значит “готовее идти глубже” без arbitrary key gate или quota.

     `q-expedition-loop` остаётся PAUSED / superseded-as-label, пока не заморожены `q-depth-grammar`, `q-coop-shape` и
     `q-expedition-macrocycle`. s-canon-015 inside-floor ideas остаются placeholders, not canon.

     ## rejected_alternatives

     - **Абстрактные деньги как центр progression** — отвергнуто: газ — центральная механика; если ценность отрывается от
       газа, игра теряет свою ось.
     - **Сырой газ всегда бесполезен** — отвергнуто owner-правкой: ценный газовый результат может быть найден уже готовым;
       не всё надо улучшать/крафтить.
     - **Только “дешёвый газ → дорогой газ” как loop** — слишком узко; команда может и находить готовую ценность, и
       добровольно усиливать более дешёвую.
     - **PoE-lite валюта / экономика из многих газовых currency** — отвергнуто как риск второй игры и wiki-духоты; берём
       конвергентность ценности, не spreadsheet.
     - **Base crafting game как центр между экспедициями** — отвергнуто по высоте: база может закреплять/готовить/страховать,
       но exact crafting/recipes/UI не этот узел.
     - **Flat cheap insurance** — отвергнуто: убивает fear of failure и greed↔fear; recovery должен быть заранее
       подготовленным ограниченным ресурсом.
     - **Quota punishment / “не сдал норму за N дней → reset”** — отвергнуто owner-правкой: reset/risk должен вытекать из
       полного провала экспедиции, не из внешней бухгалтерии.
     - **Безопасная смерть с потерей только лута** — отвергнуто как слишком мягко для intended descent fear; full-team wipe
       without recovery can be campaign collapse.
     - **Перманентный reset от любой ошибки** — отвергнуто как мясорубка; обычный провал теряет незакреплённое, но не обязан
       стирать кампанию.
     - **Решить здесь exact permadeath/save/recovery implementation** — отвергнуто по высоте; это child-вопросы
       `q-recovery-insurance` / `q-failure-stakes`.

     END_OF_FILE: questions/q-between-expeditions-progression.md

  6. Canon repo: add file `questions/q-gas-value-forms.md` with exact content:

     ---
     id: q-gas-value-forms
     area: mechanic
     status: open
     depends_on: [q-between-expeditions-progression, q-gas-role, q-base-logistics-labs-factories]
     images: []
     gate: {}
     created_on: 2026-06-26
     ---

     # Формы газовой ценности: за чем команда реально спускается?

     ## Вопрос

     Какие формы газовой ценности существуют в игре: уже ценный газ, дешёвый газ, который можно усилить, образец,
     reaction result, recipe, tool charge, insurance, money, preparation, route/frontier support — и как они остаются
     простыми, не превращаясь в PoE-lite экономику или crafting spreadsheet?

     ## Наследует

     - [[q-between-expeditions-progression]]: газовая ценность становится прогрессом только после возврата.
     - [[q-gas-role]]: газ = один субстрат / много режимов; реакции и эффекты следуют из условий.
     - [[q-base-logistics-labs-factories]]: сырой газ не обязательно товар; ценность = controlled/stabilized result.

     ## Нужно решить

     1. Минимальный список форм газовой ценности.
     2. Какие формы можно найти готовыми, а какие создаются/усиливаются в экспедиции.
     3. Какие формы становятся readiness, какие деньгами, какие insurance, какие tool/prep.
     4. Как держать конвергентность ценности без множества валют и таблиц.
     5. Что игрок должен понять без wiki.

     ## Boundaries

     - Не решать exact prices, UI, upgrade tree, balance, full recipe list.
     - Не решать concrete room verbs or floor loop.
     - Не делать gas-value taxonomy большой экономической игрой.
     - Не отменять `q-between-expeditions-progression`: value banks only after return.

     ## rejected_alternatives

     <->

     END_OF_FILE: questions/q-gas-value-forms.md

  7. Canon repo: add file `questions/q-cargo-containment.md` with exact content:

     ---
     id: q-cargo-containment
     area: mechanic
     status: open
     depends_on: [q-between-expeditions-progression, q-coop-shape, q-expedition-macrocycle]
     images: []
     gate: {}
     created_on: 2026-06-26
     ---

     # Удержание газовой ценности: как пойманное можно потерять?

     ## Вопрос

     Как работают ёмкости / кассеты / контейнеры / переноска / утечки / повреждение пойманной газовой ценности так,
     чтобы это создавало greed↔fear и кооп, но не превращалось в раздражающий escort/carry minigame?

     ## Наследует

     - [[q-between-expeditions-progression]]: до safe return gas value remains unbanked stake.
     - [[q-coop-shape]]: exact anti-solo pressure must be structural, not declared.
     - [[q-expedition-macrocycle]]: defines where carried value becomes banked.

     ## Нужно решить

     1. Какие состояния есть у пойманной газовой ценности: safe/unstable/leaking/spoiled/lost.
     2. Как игроки читают риск контейнера без spreadsheet/UI overload.
     3. Какие потери возможны без точных balance numbers.
     4. Как containment supports co-op handling.
     5. Как не сделать игру “тасканием хрупких банок”.

     ## Boundaries

     - Не решать exact item stats, durability numbers, UI widgets, inventory implementation.
     - Не решать gas roster or reaction table.
     - Не решать all expedition phases; read `q-expedition-macrocycle`.

     ## rejected_alternatives

     <->

     END_OF_FILE: questions/q-cargo-containment.md

  8. Canon repo: add file `questions/q-recovery-insurance.md` with exact content:

     ---
     id: q-recovery-insurance
     area: mechanic
     status: open
     depends_on: [q-between-expeditions-progression]
     images: []
     gate: {}
     created_on: 2026-06-26
     ---

     # Recovery и страховка: что спасает от полного wipe?

     ## Вопрос

     Какие заранее подготовленные recovery / insurance слои могут спасти кампанию от full-team wipe, как они заряжаются
     через gas value / readiness, что именно защищают, что оставляют под риском, и почему они не становятся дешёвой
     универсальной отменой страха?

     ## Наследует

     - [[q-between-expeditions-progression]]: full-team wipe без prepared recovery can collapse campaign up to new beginning.
     - Insurance must protect a limited category and cost real banked value/readiness.
     - No quota punishment; failure stakes come from expedition failure.

     ## Нужно решить

     1. Какие виды recovery возможны на уровне дизайна: rescue, revival, retrieval, reserve, anchor, blackbox, route fallback.
     2. Как recovery заряжается / готовится / тратится без exact economy numbers.
     3. Что recovery сохраняет: campaign, players, cargo, data, route, base state, or only part.
     4. Что recovery принципиально не сохраняет.
     5. Как игрок заранее понимает risk: “идём без recovery — wipe может быть крахом”.
     6. Где граница между tense hardcore и unfair meat grinder.

     ## Boundaries

     - Не решать save-file implementation.
     - Не решать exact costs, charges, UI, resurrection fiction, timers, or balance.
     - Не превращать recovery в cheap flat insurance.
     - Не вводить quota/debt timer punishment.

     ## rejected_alternatives

     <->

     END_OF_FILE: questions/q-recovery-insurance.md

  9. Canon repo: add file `questions/q-failure-stakes.md` with exact content:

     ---
     id: q-failure-stakes
     area: mechanic
     status: open
     depends_on: [q-between-expeditions-progression, q-recovery-insurance]
     images: []
     gate: {}
     created_on: 2026-06-26
     ---

     # Ставки провала: что происходит при обычной ошибке, retreat, wipe и reset?

     ## Вопрос

     Какая шкала последствий существует для провала: обычная потеря unbanked value, испорченный результат, частичный retreat,
     потеря подготовки, повреждение frontier/readiness, full-team wipe, campaign collapse / reset — и где проходит честная,
     заранее читаемая граница?

     ## Наследует

     - [[q-between-expeditions-progression]]: ordinary failure hurts but does not erase everything; full wipe without recovery
       can collapse campaign up to new beginning.
     - [[q-recovery-insurance]]: prepared recovery modifies wipe consequences.

     ## Нужно решить

     1. Категории провала.
     2. Какие потери соответствуют каждой категории.
     3. Что всегда сохраняется: player knowledge, maybe discovered facts.
     4. Что может потеряться: unbanked cargo, prep, reserves, frontier/readiness.
     5. Когда reset / near-reset is allowed.
     6. Как сделать hard default without quota punishment or unfair surprise.

     ## Boundaries

     - Не решать exact save/load implementation.
     - Не решать balance values, campaign length, UI copy, death screens.
     - Не превращать провал в external quota/debt timer.

     ## rejected_alternatives

     <->

     END_OF_FILE: questions/q-failure-stakes.md

  10. Canon repo: add file `questions/q-frontier-readiness.md` with exact content:

      ---
      id: q-frontier-readiness
      area: mechanic
      status: open
      depends_on: [q-between-expeditions-progression, q-depth-grammar]
      images: []
      gate: {}
      created_on: 2026-06-26
      ---

      # Frontier readiness: что значит “мы готовы идти глубже”?

      ## Вопрос

      Что значит readiness to go deeper без arbitrary key gate / quota: какие знания, газовые результаты, recovery,
      tools, routes, procedures, team protocols or frontier states make the next depth regime survivable and worth attempting?

      ## Наследует

      - [[q-between-expeditions-progression]]: banked gas value becomes readiness after return.
      - [[q-depth-grammar]]: deeper regimes are qualitatively different, not just higher numbers.

      ## Нужно решить

      1. Какие формы readiness существуют.
      2. Какие readiness layers persistent vs spendable vs fragile.
      3. Как readiness supports final cold exam without grind.
      4. Как readiness gates by survivability and confidence, not doors/quotas.
      5. How failure can damage readiness without turning every death into reset.

      ## Boundaries

      - Не решать exact upgrade tree, UI, prices, item stats, balance.
      - Не решать floor loop or room verbs.
      - Не превращать readiness в key collection.

      ## rejected_alternatives

      <->

      END_OF_FILE: questions/q-frontier-readiness.md

  11. Canon repo: update `questions/q-depth-grammar.md`:
      - keep frontmatter as-is;
      - under `## Наследует`, add:

        - [[q-between-expeditions-progression]] (frozen 2026-06-26): gas value becomes progression only after safe return;
          readiness to go deeper may come from banked gas results, recipes, tools, recovery, routes/frontier support, and
          prepared insurance. Depth must demand qualitatively different readiness, not arbitrary quotas.

      - under `## Нужно решить`, append:

        7. How each depth regime changes what gas value is worth finding, making, carrying, banking, or risking.
        8. How final cold exam consumes/tests readiness without turning progression into grind or keyhunt.

      - ensure file ends with:
        END_OF_FILE: questions/q-depth-grammar.md

  12. Canon repo: update `questions/q-coop-shape.md`:
      - under `**Семена от [[q-full-game-descent-arc]]` block or after it, add:

        **Семена от [[q-between-expeditions-progression]] (заморожен 2026-06-26):**
        - Между экспедициями прогресс строится вокруг газовой ценности, которая banked only on safe return.
        - До возврата gas value = опасный shared stake: груз, образец, reaction result, data, recovery/prep.
        - Full-team wipe без prepared recovery can collapse campaign up to new beginning.
        - Точный anti-solo механизм должен использовать это как материал: shared cargo, return pressure, recovery stakes,
          containment, isolation, pressure/cooling, reaction risk, rescue/failure coupling, or another hard interdependence.

      - ensure file ends with:
        END_OF_FILE: questions/q-coop-shape.md

  13. Canon repo: update `maps/World.md` or the relevant mechanic/design MOC if present:
      - replace the existing line for `q-between-expeditions-progression` under related mechanic/game-structure nodes with:

        - ✅ [[q-between-expeditions-progression]] (mechanic/game-structure, frozen 2026-06-26) — progression between expeditions = gas value becomes real progress only after safe return. Players descend for gas value: already-valuable gas/state OR cheap/ordinary gas made more valuable through risky expedition manipulation. Before return, captured gas/sample/reaction result/data/cargo = unbanked stake; after return it becomes readiness (prep/tools/insurance/recipes/resources/money/frontier support/depth capability). Ordinary failure loses unbanked value/prep but not player knowledge. Full-team wipe without prepared recovery can collapse campaign up to new beginning; recovery/insurance must be banked/charged in advance and cannot be cheap universal fear removal. depends_on: q-full-game-descent-arc. signed_by owner "A".

      - add under related open questions:
        - ▶️ [[q-gas-value-forms]] — forms of gas value without PoE-lite currency/crafting sprawl. depends_on: q-between-expeditions-progression + q-gas-role + q-base-logistics-labs-factories.
        - ▶️ [[q-cargo-containment]] — how captured gas value can be carried, damaged, leaked, spoiled, or lost without becoming annoying carry busywork. depends_on: q-between-expeditions-progression + q-coop-shape + q-expedition-macrocycle.
        - ▶️ [[q-recovery-insurance]] — prepared recovery layers that can save campaign from full-team wipe without becoming cheap fear removal. depends_on: q-between-expeditions-progression.
        - ▶️ [[q-failure-stakes]] — ordinary failure vs retreat vs full wipe vs campaign collapse/reset boundaries. depends_on: q-between-expeditions-progression + q-recovery-insurance.
        - ▶️ [[q-frontier-readiness]] — what "ready to go deeper" means without arbitrary key/quotas. depends_on: q-between-expeditions-progression + q-depth-grammar.

      - keep existing note:
        `q-expedition-loop` remains PAUSED / superseded-as-label until the parent chain above is complete; s-canon-015 inside-floor ideas remain placeholders, not canon.

captures:
  - Owner wants gas to be the convergent progression object: gas is danger, loot, preparation, insurance, and future-risk material, not merely hazard or abstract money.
  - Strong correction: gas value can be found already valuable OR made more valuable through expedition manipulation; do not imply raw/cheap gas must always be upgraded before it matters.
  - Full-team wipe without prepared recovery should be a real default-hardcore threat, potentially up to starting over; the owner dislikes quota/debt timer punishment but wants expedition failure itself to create dread.
  - Recovery should likely be charged through some gas-value/resource installation, but exact fiction/mechanics are deferred.
  - Future mechanic work should test cargo/containment/pressure/cooling/chain-reaction co-op ideas, but none of those examples are frozen as exact mechanics here.

decisions_needed: []

play_check:
  - 1. Frame: DONE. Framed `q-between-expeditions-progression` as the parent question for what changes after completed/failed expeditions; inherited `q-full-game-descent-arc` and its parent canon; area = mechanic/game-structure.
  - 2. Diverge (owner): DONE. Proposed 3 directions: readiness ledger, living frontier, debt spiral; then refined through owner brainstorming into "gas value becomes progress only after return" and hard full-wipe risk. Owner accepted direction: "ну я в принципе с тобой согласен сейчас"; final freeze choice: "A".
  - 3. Draft: DONE. Drafted compact canon entry with invariants + prose: gas value found/created, unbanked until return, return converts risk into readiness, ordinary failure loses unbanked, full wipe without prepared recovery can collapse campaign, exact systems deferred.
  - 4. Gate: DONE. Ran consistency / mechanic-altitude / not-contrived / greed-fear / co-op-parent / tone / scope checks. Passed; exact co-op, floor loop, gas roster, recipes, containers, economy, UI, save/recovery implementation deferred.
  - 5. Illustrate — where it fits: SKIPPED. This is a structural progression/failure-stakes canon node; no image required and no visual language changes.
  - 6. Freeze & grow (owner): DONE. Owner signed the hard-full-wipe direction with exact word: "A". Child graph specified: `q-depth-grammar`, `q-coop-shape`, `q-expedition-macrocycle`, `q-gas-value-forms`, `q-cargo-containment`, `q-recovery-insurance`, `q-failure-stakes`, `q-frontier-readiness`. `q-expedition-loop` remains paused.

log: |
  2026-06-26 — canon-forge frozen (g-d3a8/q-between-expeditions-progression, s-canon-between-expeditions-progression-001): owner froze A — between-expedition progression = gas value becomes real progress only after safe return. Players descend for gas value: already-valuable gas/state OR cheap/ordinary gas made more valuable through risky expedition manipulation. Before return, captured gas / sample / reaction result / data / cargo = unbanked stake; after return it becomes readiness (prep/tools/insurance/recipes/resources/money/frontier support/depth capability). Ordinary failure loses unbanked value/prep but not player knowledge. Full-team wipe without prepared recovery can be campaign collapse up to new beginning; recovery/insurance must be banked/charged in advance and cannot be cheap universal fear removal. Exact economy/UI/balance/containers/recipes/macrocycle/floor/co-op/save implementation deferred. q-expedition-loop remains paused until q-depth-grammar + q-coop-shape + q-expedition-macrocycle chain is complete. Canon repo changes proposed for writer application. → history/s-canon-between-expeditions-progression-001.md

next: |
  CALL c-canon-depth-grammar-001
  to: session
  direction: indie-game-development
  play: local/canon-forge
  node: g-d3a8
  question: q-depth-grammar
  parent: s-canon-between-expeditions-progression-001
  surface: any / repo root `C:\my_global_workflow_worktrees\indie-game-development`

  goal: |
    The canon track has an owner-forged answer for depth grammar: why lower depth regimes are qualitatively different and
    necessary, what readiness each regime demands, how gas value changes by depth, and how the final cold exam tests the
    whole arc without becoming damage-scaling, keyhunt, grind, exact floor loop, or implementation.

  context: |
    Direction OS repo:
    - `live/indie-game-development/TREE.md`
    - `live/indie-game-development/history/s-canon-014.md`
    - `live/indie-game-development/history/s-canon-015.md`
    - `live/indie-game-development/history/s-research-018.md`
    - `live/indie-game-development/history/s-canon-full-game-descent-arc-001.md`
    - `live/indie-game-development/history/s-canon-between-expeditions-progression-001.md`
    - `live/indie-game-development/plays/canon-forge.md`
    - `live/indie-game-development/plays/mechanic-forge.md`
    - `live/indie-game-development/knowledge/mechanic-lenses.md`

    Canon repo:
    - `C:\projects\gas_coop_game_canon`
    - `questions/q-north-star.md`
    - `questions/q-gas-role.md`
    - `questions/q-the-city.md`
    - `questions/q-full-game-descent-arc.md`
    - `questions/q-between-expeditions-progression.md`
    - `questions/q-depth-grammar.md`
    - `questions/q-coop-shape.md`
    - `maps/World.md`
    - relevant mechanic/design MOCs if present.

    Required inherited facts:
    - `q-full-game-descent-arc`: full game = repeated team descent through the vertical eye of storm; progress = readiness
      to enter qualitatively different depth regimes, take value, and return together; final layer = heavy cold near-inert
      exam of the whole arc.
    - `q-between-expeditions-progression`: gas value becomes real progress only after safe return; players may find already
      valuable gas states or make cheap/ordinary gas more valuable through risky expedition manipulation; full-team wipe
      without prepared recovery can collapse campaign up to new beginning; exact economy/UI/balance/containers/recipes/save
      implementation deferred.
    - `q-gas-role`: depth flips gas regime by conditions, not damage slider; one substance/many regimes; reactions are
      finite/simulable; risk/reward through shared gas field.
    - `q-the-city`: cold top → hot active working depth → cold near-inert terminus; depth gate = environment/readiness, not
      arbitrary locks/quotas.
    - `q-expedition-loop` remains paused; s-canon-015 inside-floor details remain placeholders, not canon.

  boundaries: |
    Do not define exact floor loop, expedition macrocycle, room verbs, gas roster, reaction table, co-op actions, equipment
    stats, UI, prices, balance, save system, recovery implementation, or q-the-deep lore content.
    Do not turn depth into bigger numbers, keyhunt, quota, or grind.
    Do not treat s-canon-015 inside-floor ideas as accepted mechanics.
    Do not edit canon repo unless owner signs through local/canon-forge's owner steps.

  done_when: |
    A local/canon-forge RESULT or checkpoint contains:
    1. a framed `q-depth-grammar` question with inherited frozen parents named;
    2. owner-chosen direction or checkpointed owner pushback;
    3. a compact canon answer or explicit split if the question is still too broad;
    4. child questions forced by the answer, especially depth readiness, gas-value-by-depth, final cold exam preparation,
       and any follow-up needed before q-expedition-macrocycle;
    5. explicit statement that `q-expedition-loop` remains paused until `q-depth-grammar`, `q-coop-shape`, and
       `q-expedition-macrocycle` are complete;
    6. exact state_changes only through RESULT.

  return: |
    RESULT with owner evidence, canon answer/checkpoint, proposed child question graph, captures/decisions_needed,
    exact state_changes, and next CALL.

  budget: one session
