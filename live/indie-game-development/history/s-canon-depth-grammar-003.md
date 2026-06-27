RESULT s-canon-depth-grammar-003 (call: c-canon-depth-grammar-001)
direction: indie-game-development   play: local/canon-forge   node/task: g-d3a8/q-depth-grammar
outcome: |
  Owner-frozen canon answer produced for `q-depth-grammar`.

  Frozen direction:
  "Четыре режима — это глубинная грамматика, не четыре точные зоны. Биомы/кампусы/горизонты могут повторяться и
  чередоваться внутри режимов; глубина меняет условия, readiness and gas value. Терминус — heavy cold capstone exam,
  но не абсолютный стоп игры: после первого дна возможен late-game continuation through deep/frozen yield, without
  infinite deeper treadmill, keyhunt, quota, grind, exact floor loop, or implementation."

  The answer defines depth grammar at the correct altitude:
  - depth bands are qualitative regime beats, not exact floor count, exact biome list, exact campuses, or progression numbers;
  - depth-regime and place-function are separate axes: lab/logistics/housing/industrial/old-bypass/etc. can be interpreted
    differently under cold, hot, peak, or near-inert conditions;
  - deeper means different gas behavior and different readiness, not "same rooms with higher damage";
  - readiness means real fit to the regime: field-reading, thermal geography, return discipline, containment, recovery,
    routes, protocols, banked gas results, and team competence;
  - gas value changes by regime: calibration/knowledge/safe samples → active controlled outcomes → high-risk peak value →
    deep/frozen/near-inert terminus yield;
  - final cold exam tests the whole arc and can unlock late-game continuation, but does not create an endless deeper ladder;
  - exact expedition macrocycle, floor loop, room verbs, gas roster, reaction table, co-op actions, equipment stats, UI,
    prices, balance, save/recovery implementation, and q-the-deep lore content remain deferred.

  `q-expedition-loop` remains PAUSED / superseded-as-label until `q-depth-grammar`, `q-coop-shape`, and
  `q-expedition-macrocycle` are complete. After this RESULT is applied, `q-depth-grammar` is complete, but
  `q-coop-shape` and `q-expedition-macrocycle` remain incomplete.

evidence: |
  Owner supplied the correction that shaped the final answer:
  - "как дефолтное значение, наверное, вот четыре таких этапа – это нормально"
  - "хочу сделать, чтобы в игру можно было относительно долго интересно играть"
  - "реиграбельность хорошая была" [owner said "неиграбельность"; context indicates replayability]
  - "когда до конца доходит ... газа с глубины, может даже замороженный ... это большой плюс, и ... игра дальше может продолжаться"
  - "стоит ли вообще насчет деления на четыре зоны"
  - "у нас наверняка будет несколько биомов условно, да, там лаборатории, жилые комплексы, еще что-то, но они как бы чередуются"
  - "не четыре, то есть может быть там 110, первый кампус, второй, третий"
  - "чем жарче, тем больше агрессивность включается, тем опаснее становится"

  Final owner freeze choice:
  - "Вариант А."

  Inherited frozen parents respected:
  - `q-full-game-descent-arc`: full game = repeated team descent through qualitatively different depth regimes; progress =
    readiness to enter, take value, and return together; final layer = heavy cold exam of the whole arc; exact q-the-deep
    content deferred.
  - `q-between-expeditions-progression`: gas value becomes real progression only after safe return; value may be found or
    created; return turns value into readiness; full-team wipe without prepared recovery can collapse campaign; no keyhunt,
    quota, cheap insurance, or flat currency center.
  - `q-gas-role`: one substance / many regimes; depth flips regime by conditions, not damage slider; cold top → hot working
    depth → cold near-inert origin; reactions finite/simulable; risk/reward flows through shared field.
  - `q-the-city`: cold passive upper zone → active hot human working depth → cold near-inert terminus; environment gates
    depth, not locks; return passes back through dangerous depth.
  - `s-canon-015`: inside-floor ideas remain placeholders, not accepted mechanics.

  Craft gate:
  - Consistency: PASS. Keeps cold top → hot working depth → pre-terminus active peak → cold near-inert terminus, while
    allowing many campuses/horizons/biomes inside the regime grammar.
  - Parent-lock correction: PASS. "Жилые комплексы" are not frozen as full habitation at every depth; `q-the-city` still
    keeps proper living in the cold upper zone. Deeper repeats of "living-like" material, if later used, must be shift,
    service, medical-control, ruined/cut-through, or other parent-consistent traces.
  - Mechanic altitude: PASS. Defines depth grammar, not macrocycle, floor loop, verbs, gas roster, reaction table, stats,
    UI, prices, save system, recovery implementation, or q-the-deep content.
  - No damage-scaling: PASS. Lower depth changes operating conditions, gas activation, value type, and readiness mismatch.
  - No keyhunt/quota/grind: PASS. Readiness is real survivability/return competence, not "collect X to open deeper."
  - Replayability boundary: PASS-WITH-BOUNDARY. Post-terminus continuation is allowed only as late-game continuation inside
    the established vertical and through deep/frozen yield; rejected as an infinite depth treadmill or seasonal grind.
  - Co-op interdependence: PASS-AS-PARENT. This answer gives material to `q-coop-shape` but does not solve anti-solo.
  - Mechanic-lenses status: PAPER-PASS ONLY. This is valid as canon direction; fun/replayability must still be proven later
    by grey-box/playtest evidence.
  - Tone: PASS. Keeps thriller/greed/fear/grounded sci-fi; rejects boss, magic, gas will, and final chase intent.
  - Scope: PASS. Explicitly defers exact expedition macrocycle, floor loop, q-the-deep content, and implementation.

state_changes: |
  Apply the following changes mechanically. The session did not directly edit either repo.

  1. Direction OS repo: append to `live/indie-game-development/LOG.md`:

     2026-06-26 — canon-forge frozen (g-d3a8/q-depth-grammar, s-canon-depth-grammar-003): owner froze A — depth grammar = four qualitative regimes, not exact four zones: cold upper regime → hot working depth → pre-terminus active peak → cold near-inert terminus. Many campuses/horizons/biomes can repeat/interleave inside this grammar; depth-regime × place-function creates replayability. Readiness = real fit to the next regime (field-reading, thermal geography, return discipline, containment, recovery, route/protocol/team competence, banked gas results), not key/quota. Gas value shifts by regime: calibration/knowledge/safe samples → active controlled outcomes → high-risk peak value → deep/frozen/near-inert terminus yield. Final cold exam is capstone of the whole arc but may allow late-game continuation after first terminus; no infinite deeper treadmill, damage scaling, keyhunt, grind, exact floor loop, or implementation. Child graph spawned: q-post-terminus-continuation, q-depth-biome-overlay, q-final-cold-exam-readiness; existing q-frontier-readiness and q-gas-value-forms inherit new depth-regime pressure. q-expedition-loop remains paused until q-depth-grammar + q-coop-shape + q-expedition-macrocycle are complete; after this apply, q-depth-grammar is complete, q-coop-shape and q-expedition-macrocycle remain. Canon repo changes proposed for writer application. → history/s-canon-depth-grammar-003.md

  2. Direction OS repo: create `live/indie-game-development/history/s-canon-depth-grammar-003.md`
     containing this full RESULT.

  3. Direction OS repo: `NOW.md` untouched.

  4. Direction OS repo: `TREE.md` untouched.

  5. Direction OS repo: `CHARTER.md` untouched.

  6. Direction OS repo: `knowledge/` untouched. No cross-cutting knowledge promotion proposed yet; the frozen canon card
     is sufficient source for the next canon questions.

  7. Canon repo `C:\projects\gas_coop_game_canon`: replace `questions/q-depth-grammar.md` with exact content:

     ---
     id: q-depth-grammar
     area: mechanic
     status: frozen
     depends_on: [q-full-game-descent-arc, q-between-expeditions-progression, q-gas-role, q-the-city]
     images: []
     gate:
       consistency: true
       parent_lock: true
       mechanic_altitude: true
       no_damage_scaling: true
       no_keyhunt_quota_grind: true
       replayability_boundary: true
       coop_interdependence_parent: true
       tone: true
       scope_boundary: true
       paper_only_fun_unverified: true
     frozen_on: 2026-06-26
     signed_by: owner    # "Вариант А" — four regimes as depth grammar, not exact zones; post-terminus continuation allowed without infinite treadmill
     ---

     # Грамматика глубины: почему ниже качественно иначе?

     ## Ответ (канон)

     **Инварианты — на это сверяется вся будущая структура depth, readiness, gas value, expedition macrocycle, floor loop
     и endgame continuation:**

     1. **Четыре режима — это грамматика, не точное число зон.**
        `cold upper regime / hot working depth / pre-terminus active peak / cold near-inert terminus` — это крупные
        qualitative beats спуска. Они не означают “в игре ровно четыре зоны”, “ровно четыре биома”, “ровно четыре кампуса”
        или “ровно четыре floor tiers”. Внутри них может быть много этажей, кампусов, производственных горизонтов,
        лабораторий, логистических узлов, старых обходов, жилых следов и procedural/hand-authored вариаций.

     2. **Биом / функция места ≠ режим глубины.**
        Биом или функция базы отвечает на вопрос: “что это за место?” — лаборатория, логистика, производство, верхнее жильё,
        measurement horizon, old bypass, склад, сервисный узел, hot experimental depth. Режим глубины отвечает на вопрос:
        “как здесь ведёт себя газ и что от команды требуется?” Один и тот же тип места может играть иначе в холоде, жаре,
        пике активности или near-inert тишине. Но parent-lock держится: полноценное жильё принадлежит холодному верхнему
        поясу; глубже возможны сменные/служебные/медконтрольные/руинные следы, а не противоречащие `q-the-city` жилые
        комплексы на любой глубине.

     3. **Глубже нужно идти не потому, что там больше числа, а потому что там другой режим ценности.**
        Холодный верх даёт безопасное чтение, калибровку, первые образцы, маршруты и понятные ошибки. Рабочая глубь даёт
        активный газ, controlled outcomes, реакционные результаты, редкие состояния и возможность рискованно создать
        ценность. Предтерминальный пик даёт самый высокий ожидаемый куш горячей зоны и самую тяжёлую дорогу назад.
        Терминус даёт не “ещё более горячий тир”, а холодную near-inert ценность / ответ / особый deep yield; точную
        природу этого yield и самого записанного ответа решает `q-the-deep`.

     4. **Readiness — это соответствие режиму, не ключ.**
        Команда готова идти ниже не потому, что собрала X штук для двери, а потому что реально способна войти в другой
        режим, прочитать его, взять ценность и вернуться. Readiness может включать field-reading, тепловую географию,
        маршрут, return discipline, containment, recovery, страховку, процедуры, banked gas results, командный протокол и
        понимание, когда push deeper хуже, чем bank now. Точные предметы, цены, UI, upgrade tree и баланс не решаются здесь.

     5. **Газовая ценность меняется по глубине.**
        В верхнем режиме ценнее знание, калибровка, безопасные образцы, route confidence и базовая подготовка. В горячей
        рабочей глуби ценнее активные controlled outcomes, рецепты условий, tool charges, стабилизированные результаты и
        рискованно усиленный газ. У предтерминального пика ценнее высокодоходные, опасные, трудно-выносимые результаты,
        которые сильнее всего давят на greed↔fear. В терминусе ценность меняет тип: deep/frozen/near-inert yield может быть
        большим late-game плюсом, но не становится новой валютой для гринда.

     6. **Cold upper regime — режим чтения и калибровки.**
        Верх не является “нулевой зоной без игры”. Он учит, что газ структурный, что холод усмиряет, что маршруты и
        безопасное возвращение важны, что ценность становится progress только после bank. Ошибки здесь должны быть читаемыми
        и обучающими, но не обязаны решать весь loop.

     7. **Hot working depth — режим активной эксплуатации.**
        В рабочей глуби та же субстанция легче переходит пороги: жар, плотность, источники, катализаторы, старые фабричные
        узлы и замкнутые пространства делают газ активным. Здесь команда не просто выживает, а находит или создаёт газовую
        ценность, добровольно поднимает ставку и должна вынести результат через общую опасную среду.

     8. **Pre-terminus active peak — пик ожидаемого ада.**
        Это не отдельная магия и не boss-tier. Это максимальное напряжение логики горячей рабочей зоны: ценность выше,
        условия жёстче, возврат дороже, unbanked stake страшнее. Если команда умеет только “терпеть урон” или “фармить
        безопасный паттерн”, этот слой должен ломать её. Если команда понимает режимы, маршруты, банк, recovery, containment
        и кооп-связку, она может рискнуть.

     9. **Cold near-inert terminus — смена правил, а не следующий damage tier.**
        Терминус резко холодный / near-inert / тихий. Он проверяет всю дугу тем, что привычная логика “глубже = горячее,
        активнее, агрессивнее” перестаёт быть прямой. Команда должна применить всё, чему научилась, в ином режиме: не
        разбудить лишнее, сохранить/прочитать deep value, понять, что здесь важно, и вернуться. Он не является волей газа,
        монстром, chase, arbitrary puzzle или q-the-deep lore dump.

     10. **Первый успешный терминус — capstone, но не обязательный конец всей игры.**
         Дно реально и достижимо: первый успешный выход к терминусу доказывает, что команда прошла главный экзамен дуги.
         Но это не обязано навсегда закрывать игру. После первого достижения дна игра может продолжаться: команда может
         использовать deep/frozen/near-inert yield, брать более рискованные заходы, собирать недобранную ценность, улучшать
         late-game readiness, проверять другие маршруты и играть дальше внутри уже понятной вертикали. Продолжение не
         означает бесконечную новую лестницу “ещё глубже”: терминус остаётся нижним пределом.

     11. **Реиграбельность рождается из комбинации, не из 110 ручных тиров.**
         Долгая игра держится на пересечении: функция места × режим глубины × состояние маршрута × газовая ценность ×
         подготовка команды × риск возврата × кооп-связка. Поэтому можно иметь много кампусов, горизонтов, биомов и вариаций,
         не превращая depth grammar в spreadsheet, checklist, grind ladder или biome taxonomy dump.

     12. **Этот узел не решает expedition macrocycle / floor loop.**
         Здесь не решаются: точный floor loop, expedition macrocycle, room verbs, gas roster, reaction table, co-op actions,
         equipment stats, UI, prices, balance, save system, recovery implementation, exact cargo/containment rules или
         содержимое `q-the-deep`. `q-expedition-loop` остаётся PAUSED / superseded-as-label, пока не заморожены
         `q-depth-grammar`, `q-coop-shape` и `q-expedition-macrocycle`.

     ### Проза — простыми словами

     Глубина в игре — не лестница “урон выше, лут жирнее”. Это смена режима. Сверху холодно и относительно спокойно:
     команда учится читать газ, понимать маршруты, возвращаться и bank результат. Ниже начинается рабочая глубь, где люди
     когда-то сгустили и разогрели газ, и та же субстанция становится активной: вспыхивает легче, реагирует опаснее,
     создаёт более дорогие controlled outcomes и сильнее давит на решение “вынести сейчас или рискнуть ещё”.

     Ещё ниже рабочая логика доходит до пика. Это ожидаемый ад: не магия и не босс, а максимальное напряжение известных
     правил. Там самый сильный горячий куш, но и самая тяжёлая дорога назад. Лучший результат ещё не progress, пока команда
     не вернулась; он всё ещё unbanked stake.

     А потом — резкий обрыв ожидания. Терминус не “самый горячий этаж”. Он холодный, near-inert, тихий. Его тяжесть в том,
     что привычная рабочая логика больше не переносится напрямую. Команда должна доказать, что поняла режимы, а не просто
     натерпела броню или нафармила ключи: прочитать холодный deep state, не разбудить лишнее, сохранить особую ценность,
     понять, что можно взять, и вернуться.

     При этом четыре режима — не четыре комнаты и не четыре биома. В игре может быть много кампусов, горизонтов, лабораторий,
     логистических блоков, старых обходов и повторяющихся функций базы. Они меняются не потому, что мы навесили на них tier
     number, а потому что попали в другой режим глубины. Лаборатория в холодном верхе, горячей рабочей зоне и рядом с
     терминусом — это разные игровые ситуации, даже если функция места родственная.

     Дойти до дна — большой capstone, но не обязательно “удалить сейв и показать титры”. Команда может вынести deep/frozen
     yield, получить сильный late-game плюс и продолжить играть: возвращаться за более рискованной ценностью, собирать
     недобранное, улучшать readiness, пробовать другие маршруты. Но это continuation внутри достигнутой вертикали, не
     бесконечный treadmill “теперь ещё сто глубин ниже”.

     ## Образы

     Нет. Узел структурный / mechanic-progression canon; изображение не требуется. StyleBible и визуальный язык не меняются.

     ## Открытые под-вопросы

     - [[q-coop-shape]] (mechanic) — какая hard co-op pressure делает depth readiness, dangerous gas value, return, wipe risk
       and final exam structurally not solo-with-friends.
     - [[q-expedition-macrocycle]] (mechanic) — где exactly команда делает deeper-or-bank decision, где результат становится
       safe/banked, как one expedition crosses regimes or hands off between them.
     - [[q-frontier-readiness]] (mechanic/campaign) — какие readiness layers persistent/spendable/fragile; как команда
       реально становится готовой к next regime без keyhunt/quota.
     - [[q-gas-value-forms]] (mechanic/economy) — какие формы gas value существуют по depth regime: calibration/safe sample,
       controlled outcome, peak volatile value, deep/frozen/near-inert yield.
     - [[q-post-terminus-continuation]] (mechanic/campaign) — как игра продолжается после первого успешного терминуса без
       infinite deeper treadmill, grind, seasonality, or invalidating the capstone.
     - [[q-depth-biome-overlay]] (mechanic/world) — как functional biomes/campuses/horizons repeat or interleave across depth
       regimes without becoming exact floor loop.
     - [[q-final-cold-exam-readiness]] (mechanic/endgame) — что именно final cold exam checks after macrocycle/co-op are known,
       without boss, magic, arbitrary puzzle, q-the-deep lore dump, or damage-scaling.
     - [[q-the-deep]] (world) — exact recorded answer / deep content; this card only reserves cold near-inert terminus and deep
       yield, not its lore.

     `q-expedition-loop` остаётся PAUSED / superseded-as-label, пока не заморожены `q-depth-grammar`, `q-coop-shape` и
     `q-expedition-macrocycle`. После этой карточки `q-depth-grammar` выполнен; `q-coop-shape` и `q-expedition-macrocycle`
     ещё нет. s-canon-015 inside-floor ideas остаются placeholders, not canon.

     ## rejected_alternatives

     - **Ровно четыре зоны / четыре биома / четыре кампуса** — отвергнуто owner-правкой: четыре этапа годятся как дефолтная
       грамматика, но игра может иметь много кампусов, горизонтов и повторяющихся функций.
     - **Depth = bigger numbers / higher damage** — отвергнуто родителями: depth flips regime by conditions, not slider.
     - **Биом как progression tier** — отвергнуто: функция места и режим глубины разные оси; иначе получится theme-park tiering.
     - **Скрытый keyhunt / quota gate** — отвергнуто: готовность идти глубже должна быть реальной survivability/readiness,
       не “собрал X, дверь открылась”.
     - **End = абсолютный стоп игры** — отвергнуто owner-правкой: после дна игра может продолжаться through deep/frozen yield
       and late-game readiness.
     - **Endgame = бесконечный treadmill глубже** — отвергнуто: дно реально и достижимо; continuation не отменяет нижний предел.
     - **Терминус как босс / воля газа / chase / магия** — отвергнуто: финал = cold near-inert exam, gas has no will.
     - **Решить здесь exact post-terminus loop / rewards / economy** — отвергнуто по высоте; это [[q-post-terminus-continuation]].
     - **Решить здесь exact floor loop, rooms, verbs, gas roster, reaction table, co-op actions, balance or UI** — отвергнуто по
       высоте; это later macrocycle/floor/mechanic questions.

     END_OF_FILE: questions/q-depth-grammar.md

  8. Canon repo: add file `questions/q-post-terminus-continuation.md` with exact content:

     ---
     id: q-post-terminus-continuation
     area: mechanic
     status: open
     depends_on: [q-depth-grammar, q-between-expeditions-progression, q-frontier-readiness]
     images: []
     gate: {}
     created_on: 2026-06-26
     ---

     # Продолжение после терминуса: как играть дальше после первого дна?

     ## Вопрос

     Как игра может продолжаться после первого успешного выхода к cold near-inert terminus: что даёт deep/frozen/near-inert
     yield, какие late-game цели остаются, как команда использует новое readiness, и как не превратить это в infinite deeper
     treadmill, grind, seasonality, keyhunt, or invalidation of the capstone?

     ## Наследует

     - [[q-depth-grammar]]: терминус — capstone всей дуги, но не обязательный абсолютный стоп игры; continuation allowed only
       inside established vertical, not as endless deeper ladder.
     - [[q-between-expeditions-progression]]: gas value becomes progression only after safe return.
     - [[q-frontier-readiness]]: exact readiness layers are defined separately; this node consumes them when known.

     ## Нужно решить

     1. Что означает first terminus clear для кампании.
     2. Какие формы deep/frozen/near-inert yield могут стать late-game плюсами без новой валютной духоты.
     3. Какие meaningful goals remain after first bottom: safer repeats, harder extraction, unfinished value, alternate routes,
        recovery prep, mastery, or other non-treadmill forms.
     4. Что нельзя делать после терминуса: no infinite depth, no season ladder, no arbitrary prestige grind, no invalidating
        "bottom is real and reached."
     5. Какие части continuation are persistent, spendable, risky, or optional.

     ## Boundaries

     - Не решать q-the-deep lore content.
     - Не решать exact rewards, prices, UI, balance, save system, or recovery implementation.
     - Не создавать бесконечную новую глубину ниже терминуса.
     - Не превращать continuation в MMO/seasonal grind.
     - Не отменять `q-depth-grammar`: first terminus remains the capstone exam.

     ## rejected_alternatives

     <->

     END_OF_FILE: questions/q-post-terminus-continuation.md

  9. Canon repo: add file `questions/q-depth-biome-overlay.md` with exact content:

     ---
     id: q-depth-biome-overlay
     area: mechanic/world
     status: open
     depends_on: [q-depth-grammar, q-base-logistics-labs-factories, q-base-biome-room-families]
     images: []
     gate: {}
     created_on: 2026-06-26
     ---

     # Depth × biome overlay: как кампусы и функции меняются от режима глубины?

     ## Вопрос

     Как functional biomes / campuses / production horizons / labs / logistics / old bypasses / upper living traces repeat,
     interleave, or mutate across depth regimes, so the game can have long replayable variety without becoming exact floor loop,
     biome taxonomy dump, or "110 manual tiers"?

     ## Наследует

     - [[q-depth-grammar]]: four regimes are qualitative grammar, not exact zone count.
     - [[q-base-logistics-labs-factories]]: base function comes from raw flow, regime cells, logistics, labs, factories,
       quench/clean/certify, and historical growth.
     - [[q-base-biome-room-families]]: exact biome/room family work belongs there; this node only overlays depth-regime logic.

     ## Нужно решить

     1. How place-function and depth-regime combine.
     2. Which functions can repeat across regimes and which are parent-locked to upper/lower layers.
     3. How to keep "many campuses/horizons" readable without spreadsheet tiering.
     4. How depth changes affordances, risk, props, route value, and gas value without defining exact room verbs.
     5. How to avoid contradiction with `q-the-city`: full living is upper; deeper variants must be shift/service/medical/control/ruin traces unless later canon explicitly permits more.

     ## Boundaries

     - Не решать exact floor loop, procedural algorithm, room verbs, content count, map size, UI, or balance.
     - Не turn biomes into progression keys.
     - Не contradict `q-the-city` habitation bands.
     - Не replace `q-base-biome-room-families`; this is an overlay question, not the room-family catalog.

     ## rejected_alternatives

     <->

     END_OF_FILE: questions/q-depth-biome-overlay.md

  10. Canon repo: add file `questions/q-final-cold-exam-readiness.md` with exact content:

      ---
      id: q-final-cold-exam-readiness
      area: mechanic/endgame
      status: open
      depends_on: [q-depth-grammar, q-frontier-readiness, q-coop-shape, q-expedition-macrocycle]
      images: []
      gate: {}
      created_on: 2026-06-26
      ---

      # Final cold exam readiness: что именно проверяет терминус?

      ## Вопрос

      После того как известны readiness layers, co-op shape, and expedition macrocycle: что именно cold near-inert terminus
      проверяет как heavy exam всей дуги, чтобы это было gameplay, not boss, magic, chase, arbitrary puzzle, q-the-deep lore
      dump, damage-scaling, or keyhunt?

      ## Наследует

      - [[q-depth-grammar]]: terminus is cold near-inert rule-shift and capstone; continuation after first clear is possible.
      - [[q-frontier-readiness]]: defines what readiness exists.
      - [[q-coop-shape]]: final exam must remain structurally co-op, not solo-with-friends.
      - [[q-expedition-macrocycle]]: defines expedition boundaries, banking, return, and failure.

      ## Нужно решить

      1. Which learned skills/readiness layers the terminus tests.
      2. How a cold near-inert regime creates pressure without "more damage."
      3. What players must read in the field vs know strategically.
      4. How the final exam creates greed↔fear and return pressure.
      5. What counts as success, partial success, retreat, or failure at the final exam altitude.
      6. How it supports post-terminus continuation without invalidating the capstone.

      ## Boundaries

      - Не решать exact q-the-deep lore content.
      - Не write boss/chase/magic/intent.
      - Не design exact room verbs before macrocycle/floor loop.
      - Не define rewards, prices, UI, equipment stats, save/recovery implementation, or balance.
      - Не turn exam into arbitrary puzzle/keyhunt.

      ## rejected_alternatives

      <->

      END_OF_FILE: questions/q-final-cold-exam-readiness.md

  11. Canon repo: update `questions/q-frontier-readiness.md` mechanically:
      - keep frontmatter as-is;
      - under `## Наследует`, add:

        - [[q-depth-grammar]] (frozen 2026-06-26): readiness means real fit to a qualitative depth regime, not key/quota.
          Four regimes are grammar, not exact zones; readiness must support cold upper reading, hot working depth,
          pre-terminus peak, cold near-inert terminus, and possible post-terminus late-game continuation.

      - under `## Нужно решить`, ensure these bullets exist or append them:

        - Which readiness layers correspond to each depth regime.
        - Which readiness layers are persistent, spendable, fragile, recoverable, or post-terminus.
        - How readiness supports replayability without becoming grind or hidden keyhunt.

      - ensure file ends with:
        END_OF_FILE: questions/q-frontier-readiness.md

  12. Canon repo: update `questions/q-gas-value-forms.md` mechanically:
      - keep frontmatter as-is;
      - under `## Наследует`, add:

        - [[q-depth-grammar]] (frozen 2026-06-26): gas value changes by depth regime — calibration/knowledge/safe sample
          in the cold upper regime; active controlled outcomes in hot working depth; high-risk volatile peak value near
          the pre-terminus active peak; deep/frozen/near-inert yield at the terminus.

      - under `## Нужно решить`, ensure these bullets exist or append them:

        - Which gas-value forms belong naturally to each depth regime.
        - How deep/frozen/near-inert yield is valuable without becoming a new grind currency.
        - How value-by-depth stays readable without PoE-lite taxonomy.

      - ensure file ends with:
        END_OF_FILE: questions/q-gas-value-forms.md

  13. Canon repo: update `questions/q-coop-shape.md`:
      - under the existing inherited seeds, add:

        **Семена от [[q-depth-grammar]] (заморожен 2026-06-26):**
        - Четыре режима — это qualitative depth grammar, not exact zone count: cold upper regime → hot working depth →
          pre-terminus active peak → cold near-inert terminus.
        - Depth readiness must be structural and team-facing: field-reading, return discipline, containment, recovery,
          route/protocol/team competence, banked gas results.
        - Final cold exam must test co-op interdependence too; it cannot be optimally solo-with-friends or sequential-one-body.
        - Post-terminus continuation may exist, but must not become solo grind, infinite deeper treadmill, or keyhunt.

      - ensure file ends with:
        END_OF_FILE: questions/q-coop-shape.md

  14. Canon repo: update `maps/World.md` or the relevant mechanic/design MOC if present:
      - replace the existing line for `q-depth-grammar` under related mechanic/game-structure nodes with:

        - ✅ [[q-depth-grammar]] (mechanic/game-structure, frozen 2026-06-26) — depth grammar = four qualitative regimes, not exact four zones: cold upper regime → hot working depth → pre-terminus active peak → cold near-inert terminus. Many campuses/horizons/biomes can repeat/interleave inside this grammar; depth-regime × place-function creates replayability. Readiness = real fit to next regime (field-reading, thermal geography, return discipline, containment, recovery, route/protocol/team competence, banked gas results), not key/quota. Gas value shifts by regime: calibration/knowledge/safe samples → active controlled outcomes → high-risk peak value → deep/frozen/near-inert terminus yield. Final cold exam is capstone but game may continue after first terminus through late-game deep/frozen yield; no infinite deeper treadmill, damage scaling, keyhunt, grind, exact floor loop, or implementation. depends_on: q-full-game-descent-arc + q-between-expeditions-progression + q-gas-role + q-the-city. signed_by owner "Вариант А".

      - add under related open questions:

        - ▶️ [[q-post-terminus-continuation]] — how play continues after first terminus via deep/frozen/near-inert yield without infinite depth treadmill, grind, seasonality, or invalidating the capstone. depends_on: q-depth-grammar + q-between-expeditions-progression + q-frontier-readiness.
        - ▶️ [[q-depth-biome-overlay]] — how functional biomes/campuses/horizons repeat or interleave across depth regimes without exact floor loop or "110 manual tiers". depends_on: q-depth-grammar + q-base-logistics-labs-factories + q-base-biome-room-families.
        - ▶️ [[q-final-cold-exam-readiness]] — after readiness/co-op/macrocycle are known, what final cold exam actually tests without boss/magic/chase/arbitrary puzzle/damage scaling. depends_on: q-depth-grammar + q-frontier-readiness + q-coop-shape + q-expedition-macrocycle.

      - update the pause note to:

        `q-expedition-loop` remains PAUSED / superseded-as-label until `q-depth-grammar`, `q-coop-shape` and `q-expedition-macrocycle` are complete. After `q-depth-grammar` is applied, the remaining blockers are `q-coop-shape` and `q-expedition-macrocycle`. s-canon-015 inside-floor ideas remain placeholders, not canon.

captures:
  - Owner's "трахандаза" should remain an un-frozen placeholder word for a valuable deep/endgame thing; do not canonize the term or object without a later owner clarification.
  - Strong design guardrail: four regimes are a readability spine, not a content cap. Production can create many campuses/horizons/biome variants under this grammar.
  - Strong replayability guardrail: continuation after the first terminus is allowed, but the bottom remains real; do not make "endgame" into infinite depth, prestige reset, seasonal ladder, or grind currency.
  - Parent-lock for future biome work: full habitation belongs to the cold upper zone; deeper "living" material needs to be framed as shift/service/medical-control/ruin traces unless explicitly re-opened.
  - Future grey-box/playtest must prove actual replayability and co-op fun; this canon card only removes structural contradictions on paper.
  - `q-expedition-macrocycle` is still blocked by `q-coop-shape`; after `q-coop-shape` freezes, macrocycle can be forged without reviving the old overloaded `q-expedition-loop`.

decisions_needed: []

play_check:
  - "1. Frame: DONE. Framed `q-depth-grammar` as the mechanic question for qualitative depth regimes, readiness demands, gas value by depth, and final cold exam. Direct frozen parents named: `q-full-game-descent-arc`, `q-between-expeditions-progression`, `q-gas-role`, `q-the-city`. Area = mechanic."
  - "2. Diverge (owner): DONE. Proposed A/B/C; owner steered toward A with replayability/endgame correction: 'четыре таких этапа – это нормально', 'относительно долго интересно играть', 'игра дальше может продолжаться', 'не четыре, то есть может быть там 110, первый кампус, второй, третий'. Final owner choice: 'Вариант А.'"
  - "3. Draft: DONE. Drafted compact canon entry: four regimes = grammar not exact zones; biomes/campuses can repeat/interleave; readiness = regime-fit; gas value changes by regime; final cold exam is capstone but may allow post-terminus continuation."
  - "4. Gate: DONE. Ran consistency / parent-lock / mechanic-altitude / no-damage-scaling / no-keyhunt-quota-grind / replayability boundary / co-op-parent / tone / scope checks. Passed as paper canon direction; fun/replayability not certified."
  - "5. Illustrate — where it fits: SKIPPED. Structural mechanic/progression node; no image required and visual language unchanged."
  - "6. Freeze & grow (owner): DONE. Owner signed: 'Вариант А.' Frozen card content, rejected alternatives, child graph, MOC update, and next CALL specified. `q-expedition-loop` remains paused until `q-depth-grammar`, `q-coop-shape`, and `q-expedition-macrocycle` are complete."

log: |
  2026-06-26 — canon-forge frozen (g-d3a8/q-depth-grammar, s-canon-depth-grammar-003): owner froze A. Depth grammar = four qualitative regimes, not exact four zones; many campuses/biomes inside regimes; gas value and readiness shift by depth; final cold exam is capstone, but game can continue after first terminus via late-game deep/frozen yield without infinite depth treadmill. q-expedition-loop remains paused until q-depth-grammar + q-coop-shape + q-expedition-macrocycle complete. Canon repo changes proposed for writer application.

next: |
  CALL c-canon-coop-shape-001
  to: session
  direction: indie-game-development
  play: local/canon-forge
  node: g-d3a8
  question: q-coop-shape
  parent: s-canon-depth-grammar-003
  surface: any / repo root `C:\my_global_workflow_worktrees\indie-game-development`

  goal: |
    The canon track has an owner-forged answer for `q-coop-shape`: the hard co-op pressure that makes full descent, gas value,
    return, recovery stakes, depth readiness, and final cold exam structurally not solo-with-friends, without defining exact
    floor loop, room verbs, equipment stats, UI, balance, or implementation.

  context: |
    Direction OS repo:
    - `live/indie-game-development/TREE.md`
    - `live/indie-game-development/history/s-canon-015.md`
    - `live/indie-game-development/history/s-research-018.md`
    - `live/indie-game-development/history/s-canon-full-game-descent-arc-001.md`
    - `live/indie-game-development/history/s-canon-between-expeditions-progression-001.md`
    - `live/indie-game-development/history/s-canon-depth-grammar-003.md`
    - `live/indie-game-development/plays/canon-forge.md`
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

    Required inherited facts:
    - `q-north-star`: "Мы рискнули — и вытащили это вместе"; no solo-with-friends; gas is sim-derived danger/loot/spectacle;
      greed-vs-fear = take payoff out vs risk deeper.
    - `q-gas-role`: gas is shared structured field; non-local effects are a seam for co-op but do not themselves solve
      anti-solo; risk/reward is shared through common air.
    - `q-the-city`: vertical base; return passes back through dangerous depth; depth gate = environment/readiness, not locks.
    - `q-full-game-descent-arc`: full progress = readiness to enter qualitatively different depth regimes, take value, and
      return together; final layer = heavy cold exam of the whole arc.
    - `q-between-expeditions-progression`: gas value banks only after safe return; full-team wipe without prepared recovery can
      collapse campaign; recovery/insurance cannot be cheap universal fear removal.
    - `q-depth-grammar`: four regimes are grammar, not exact zones; readiness is regime-fit, not key/quota; gas value changes
      by depth; final cold exam is capstone; post-terminus continuation allowed without infinite deeper treadmill.
    - `s-canon-015`: inside-floor mechanics remain placeholders, not accepted canon.

  boundaries: |
    Do not define exact expedition macrocycle, floor loop, room verbs, gas roster, reaction table, equipment stats, UI, prices,
    balance, save system, recovery implementation, or q-the-deep lore content.
    Do not solve co-op by simple two-switches, parallel-solo tasks, escort busywork, bot/AFK-compatible roles, or sequential
    one-body bypass.
    Do not make co-op a declared vibe; it must be structurally anti-solo and must later survive mechanic-lens scrutiny.
    Do not treat s-canon-015 inside-floor ideas as accepted mechanics.
    Do not edit canon repo unless owner signs through local/canon-forge's owner steps.

  done_when: |
    A local/canon-forge RESULT or checkpoint contains:
    1. a framed `q-coop-shape` question with inherited frozen parents named;
    2. owner-chosen direction or checkpointed owner pushback;
    3. a compact canon answer or explicit split if the question is still too broad;
    4. child questions forced by the answer, especially exact co-op mechanic families / cargo-return coupling / recovery
       rescue coupling / final exam co-op pressure if deferred;
    5. explicit statement that `q-expedition-loop` remains paused until `q-depth-grammar`, `q-coop-shape`, and
       `q-expedition-macrocycle` are complete;
    6. exact state_changes only through RESULT.

  return: |
    RESULT with owner evidence, canon answer/checkpoint, proposed child question graph, captures/decisions_needed,
    exact state_changes, and next CALL.

  budget: one session

END_OF_FILE: live/indie-game-development/history/s-canon-depth-grammar-003.md
