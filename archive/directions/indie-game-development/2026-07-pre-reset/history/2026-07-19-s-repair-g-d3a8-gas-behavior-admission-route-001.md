RESULT s-repair-g-d3a8-gas-behavior-admission-route-001 (call: c-forge-g-d3a8-gas-behavior-jobs-canon-admission-001)
direction: indie-game-development
track: canon
play: repair
node/task: g-d3a8 / gas-behavior canon-admission close and route repair

outcome: |
  Owner canon-admission verdict remains recorded verbatim:

  «ADMIT TO CANON»

  The exact existing OWNER-SELECTED PAPER ANSWER:

  live/indie-game-development/work/
  q-gas-behavior-jobs-paper-decision-v1.md

  is admitted into canon as the separate preliminary mechanic card:

  canon/c-002-gas-behavior-jobs.md

  The prior unapplied RESULT contained a track-mode routing defect:
  it removed the completed canon-track root without creating a replacement
  root or a real pending owner decision.

  The corrected route keeps the existing «Геймдизайн и канон» track active.

  The completed canon-admission root is replaced by one ready cartography
  root whose only job is to:

  - reconcile the current design-question map after c-002 admission;
  - remove the now-resolved gas-behavior question from the live front;
  - recalculate downstream dependencies;
  - explicitly account for preserved historical floor-loop and
    floor-board findings;
  - present the owner with 2–3 plain-language next-question options and a
    recommendation;
  - stop for the owner's choice before opening another design answer.

  No second canon/design track is created.

  The canon track is not paused, removed or parked.

  No next gameplay-design question is automatically selected or answered.

  No greybox, prototype, implementation or product route is opened.

evidence: |
  1. Owner canon-admission verdict, verbatim:

     «ADMIT TO CANON»

  2. Owner approval of this routing repair, verbatim:

     «Теперь стало понятнее. То есть да, ты совершил ошибку.
     Ну, всё, исправляй тогда запрос.»

  3. Current unapplied hot state still contains:

     - the track «Геймдизайн и канон»;
     - the root
       c-forge-g-d3a8-gas-behavior-jobs-canon-admission-001.

     Therefore no rollback is required. The old root can be replaced
     atomically by the corrected successor root.

  4. The current owner-approved question map exists at:

     live/indie-game-development/work/canon-maps/
     g-d3a8-current-question-front-v2.md

     It contains a full dependency graph and multiple unresolved questions,
     but still names Gas behavior job grammar as its one current next
     question.

  5. That gas-behavior question has now completed its full route:

     - Gate F: «FRAME READY»
     - Gate Q: «QUESTION READY»
     - paper selection:
       «Мне нравится вариант А.»
       «В принципе, можем фиксировать. Я согласен с рекомендацией.»
     - canon admission:
       «ADMIT TO CANON»

     Therefore the v2 map's live-next recommendation is stale after this
     RESULT is applied.

  6. Preserved historical floor-loop evidence exists, including:

     - history/s-canon-floor-loop-001.md
     - history/s-canon-floor-loop-002.md
     - related floor-board and core-recovery history

     These materials contain substantive findings about:

     - real but incomplete floor read;
     - progressive field understanding;
     - active conditions as world causes rather than numeric affixes;
     - repeated gas/value work;
     - changing stake and return liability;
     - greed / return / deeper decisions;
     - temporary co-op roles;
     - the Simple Gas Work Loop.

     They are historical evidence under the current authority model, but the
     current v2 map does not explicitly reconcile their surviving findings.

  7. The correct next procedure is therefore cartography, not another
     automatic Canon Forge question:

     - inventory current questions;
     - update dependencies;
     - reconcile historical findings;
     - present next-route options;
     - obtain owner sign;
     - only then issue another design-question CALL.

state_changes: |
  Apply atomically against fresh current state using stable ids, exact paths
  and semantic rebase.

  This session did not edit either repository directly.

  Observed merge bases are aids, not freshness locks:

  - ainazemtsau/my_global_workflow:
    live/indie-game-development/NOW.md
    observed blob:
    81bfbdb120e142024f4361f4ee8b6fb91f2d27f4

  - ainazemtsau/my_global_workflow:
    live/indie-game-development/work/canon-maps/
    g-d3a8-current-question-front-v2.md
    observed blob:
    b014796924ca7336f85d757c089aed5095f9a72f

  - ainazemtsau/gas_coop_game_canon:
    INDEX.md
    observed blob:
    f1e793c8a9ef94e47f8dd65f211c21a6cbcba47b

  - ainazemtsau/gas_coop_game_canon:
    QUEUE.md
    observed blob:
    004f8ff59f87e2c4bd6e25aeb99db3186dad22f2

  ----------------------------------------------------------------------
  1. CREATE THE ADMITTED CANON CARD
  ----------------------------------------------------------------------

  Add exactly once to repository:

  ainazemtsau/gas_coop_game_canon

  Path:

  canon/c-002-gas-behavior-jobs.md

  Add only if absent.

  If byte-identical, no-op.

  If another file already occupies this path, or id c-002 already exists
  with different semantics, stop as a semantic collision. Do not silently
  renumber, merge or overwrite.

  FILE_CONTENT_BEGIN
  ---
  id: c-002
  вопрос: Какое минимальное физическое различие между газами должно заставлять команду по-разному добывать, останавливать и вести Шар, а не только видеть другое название или цвет?
  статус: предварительная
  дата: 2026-07-19
  кластер: []
  трогает: []
  режим: механика
  проверка: нужен-грейбокс
  вердикт_владельца: «ADMIT TO CANON»
  ---

  # Минимальная грамматика физического поведения газов

  ## Ответ — канон

  Движение и контроль являются текущим минимальным общим слоем поведения
  gameplay-газов.

  Каждый gameplay-газ обязан иметь хотя бы одну основную читаемую
  физическую тенденцию движения, которая создаёт для игроков
  **Control Obligation** внутри общей системы добычи и физического
  владения Шаром.

  **Control Obligation** — физическая работа, которую игрок должен
  выполнить, предвидеть или использовать из-за поведения газа в движении.

  ## Текущая минимальная грамматика

  ### Counter

  Противодействовать направленной физической тенденции либо использовать
  её.

  Эта задача меняет:

  - где располагаются игроки;
  - с какой стороны прикладывают силу;
  - какой просвет или маршрут выбирают;
  - стоит ли сопротивляться тенденции или использовать её.

  ### Brake

  Управлять сохранённым движением, ускорением, остановкой и
  перенаправлением.

  Эта задача меняет:

  - необходимое место для торможения;
  - скорость подхода;
  - выбор маршрута;
  - момент начала остановки или изменения направления.

  ### Time

  Действовать относительно видимого повторяющегося физического импульса
  или ослабления силы.

  Эта задача меняет момент:

  - закрытия Шара;
  - тяги;
  - толчка;
  - прохождения физического ограничения.

  Она не требует timing-meter или скрытого случайного цикла.

  Counter, Brake и Time являются семьями gameplay-jobs.

  Они не являются:

  - названиями газов;
  - финальным roster;
  - точным количеством газов;
  - окончательной гарантией того, что после playable evidence других
    movement-job families не потребуется.

  ## Проверка нового movement-job

  Предлагаемое поведение проходит эту карточку только тогда, когда
  одновременно верно всё следующее.

  1. Поведение объясняется одним читаемым физическим правилом.

  2. Оно работает через ту же стандартную систему добычи и физического
     владения Шаром.

  3. Замена поведения в той же физической ситуации меняет хотя бы одно
     содержательное решение о:

     - позиции добычи;
     - затронутой части газового поля;
     - выбранном объёме;
     - моменте закрытия;
     - точке остановки;
     - положении тела или строп;
     - времени действия;
     - торможении;
     - перенаправлении;
     - маршруте возврата.

  4. Различие не сводится только к:

     - другому имени;
     - другому цвету;
     - другому численному значению силы;
     - тому же directed-job, повёрнутому в другую сторону;
     - gas-specific требованию к оболочке;
     - повреждению оболочки типом газа;
     - реакции;
     - damage outcome;
     - специальному инструменту, который подменяет movement-job.

  5. Последствие остаётся атрибутируемым:

     - физической тенденции газа;
     - геометрии пространства;
     - действию игрока.

  ## Газ, объём и оболочка

  **Объём задаёт силу.**

  Более сильное проявление той же Control Obligation не становится
  автоматически новой job-family.

  **Оболочка задаёт общую физическую выдержку.**

  Ни одна Control Obligation не создаёт gas-specific eligibility
  оболочки или матрицу `gas × shell`.

  Действует universal capture:

  - каждый стандартный Шар захватывает и удерживает каждый gameplay-газ;
  - тип газа сам по себе не повреждает Шар;
  - тип газа сам по себе не ослабляет Шар;
  - тип газа сам по себе не дестабилизирует Шар;
  - тип газа сам по себе не разрывает Шар;
  - обязательной gas-specific категории Шара нет;
  - совместимости `gas × shell` нет.

  Возможные последствия нескольких газов не определяются этой карточкой.

  Они остаются будущими общими правилами `gas × gas`.

  ## Один игрок и помощь

  Эта грамматика не вводит обязательный порог вида
  «для этого Шара необходимо N игроков».

  - Один игрок может контролировать малый Шар.
  - Один игрок может попытаться провести несколько больший Шар, если это
    допускают маршрут, скорость, позиция и запас контроля.
  - Цена более крупной работы в одиночку может выражаться в:
    - более медленном ведении;
    - более раннем торможении;
    - более длинном маршруте;
    - меньшем запасе коррекции;
    - невозможности выполнить продвинутый манёвр.
  - Дополнительные игроки добавляют:
    - ограниченную силу с других направлений;
    - более ранние позиции торможения;
    - живую координацию времени.
  - Дополнительные игроки улучшают управляемость.
  - Они не создают бинарное правило допуска к газу или Шару.

  В пределах текущих трёх jobs:

  - Counter доступен одному игроку при малой силе через выгодную сторону
    и маршрут;
  - Brake доступен одному игроку через меньшую скорость и больший путь
    торможения;
  - Time доступен одному игроку через ожидание или использование
    благоприятной физической фазы.

  Остаются OPEN:

  - точный максимальный размер для одного игрока;
  - helper count;
  - player-count scaling;
  - carry tuning;
  - balance.

  Это положение не изменяет design-цель меняющейся группы 4–8 игроков,
  обязательную поддержку восьми, открытый нижний предел ниже четырёх и
  отсутствие текущей solo design-цели.

  ## Movement-first, не movement-only

  Эта карточка решает только минимальную грамматику движения и контроля.

  Она не утверждает, что все будущие содержательные различия между газами
  обязаны быть movement-эффектами.

  Будущие газы или наполненные Шары могут иметь дополнительные эффекты
  или modifiers, только если отдельная ограниченная design-работа позднее
  выберет их.

  Такие будущие эффекты:

  - не получают authority из этой карточки;
  - не заменяют обязательный movement-job;
  - не создают молча совместимость `gas × shell`;
  - не определяют здесь damage;
  - не определяют здесь reactions;
  - не определяют здесь status effects;
  - не определяют здесь implementation.

  Упоминание чего-либо вроде радиоактивного Шара является только примером
  возможного будущего не-movement измерения.

  Эта карточка не выбирает:

  - radiation rule;
  - radiation consequence;
  - damage law;
  - modifier taxonomy.

  ## Граница authority

  Эта карточка допускает только точный ограниченный ответ о минимальной
  грамматике поведения газов.

  Она не допускает в канон целиком:

  - Minimum Game Frame v2;
  - Gas Sphere extraction/custody Frame.

  Из рамочных источников authority получают только положения, прямо
  записанные в этой карточке:

  - movement/control grammar;
  - Counter / Brake / Time;
  - критерий содержательного movement-job;
  - volume as strength;
  - shell as general endurance;
  - universal capture;
  - отсутствие `gas × shell`;
  - отсутствие обязательного N-player eligibility gate;
  - movement-first, not movement-only.

  Остальные правила наполнения, управления, строп, телесных импульсов,
  вместимости, разрыва, доставки, лифта и реализации не получают canon
  authority по умолчанию.

  Эта карточка не изменяет и не расширяет:

  canon/c-001-investigation-readiness.md

  ## Открытое и непроверенное

  Эта карточка не определяет и не доказывает:

  - точные названия газов;
  - финальный roster;
  - число газов;
  - точное назначение газов в Counter, Brake или Time;
  - останутся ли три семьи исчерпывающими после playable evidence;
  - точные физические тенденции;
  - силы;
  - циклы;
  - концентрации;
  - thresholds;
  - точные read channels поля или Шара;
  - controls;
  - UI;
  - VFX;
  - onboarding;
  - capacity;
  - точный one-player maximum;
  - helper count;
  - player-count scaling;
  - carry tuning;
  - balance;
  - taxonomy дополнительных effects/modifiers;
  - radiation;
  - reactions;
  - mixed-gas outcomes;
  - rupture;
  - damage;
  - health;
  - death;
  - rescue;
  - recovery;
  - economy;
  - prices;
  - progression;
  - tools;
  - artifact rules;
  - networking;
  - physics architecture;
  - implementation;
  - production scope;
  - fun;
  - runtime legibility;
  - реальную дополнительную ценность 4–8 игроков;
  - commercial response;
  - market response.

  Все перечисленные измерения сохраняются OPEN или UNVERIFIED.

  Они не могут выводиться из этой карточки по аналогии.

  ## Провенанс

  Точный paper-источник:

  `live/indie-game-development/work/
  q-gas-behavior-jobs-paper-decision-v1.md`

  Gate F, слова владельца:

  «FRAME READY»

  Gate Q, слова владельца:

  «QUESTION READY»

  Paper selection, слова владельца:

  «Мне нравится вариант А.»

  «В принципе, можем фиксировать. Я согласен с рекомендацией.»

  «...мы сейчас фокусируемся на движении...»

  «...это не значит, что шары не могут какими-то дополнительными
  модификаторами обладать.»

  Отдельный canon-admission verdict владельца 2026-07-19:

  «ADMIT TO CANON»

  END_OF_FILE: canon/c-002-gas-behavior-jobs.md
  FILE_CONTENT_END

  ----------------------------------------------------------------------
  2. UPDATE THE CANON INDEX
  ----------------------------------------------------------------------

  Edit:

  ainazemtsau/gas_coop_game_canon/INDEX.md

  Upsert exactly one entry immediately after the current c-001 entry and
  before the `## Historical evidence` heading.

  Exact entry:

  - **c-002** · q-gas-behavior-jobs · «Control Obligation: Counter / Brake / Time» — статус **предварительная** (нужен-грейбокс), режим механика · допущена owner-вердиктом «ADMIT TO CANON» 19.07 · `canon/c-002-gas-behavior-jobs.md`

  If the exact entry already exists, no-op.

  If c-002 exists with another path or semantics, stop as a semantic
  collision.

  Preserve every other fresh-current INDEX entry and the Historical
  evidence section unchanged.

  ----------------------------------------------------------------------
  3. RECORD THE ADMISSION IN THE CANON QUEUE WITHOUT OPENING A QUESTION
  ----------------------------------------------------------------------

  Edit:

  ainazemtsau/gas_coop_game_canon/QUEUE.md

  Preserve:

  - `status: NO ACTIVE DESIGN QUESTION`;
  - the complete c-001 admission receipt;
  - the Removed live route section;
  - the rule that a future design question requires a new explicit
    Direction OS CALL.

  Insert exactly once after the current c-001 admission block and before
  the next paragraph beginning:

  `A future design question may be opened only by a new explicit Direction OS`

  Insert:

  QUEUE_INSERT_BEGIN
  q-gas-behavior-jobs reached a separate owner-present canon-admission
  verdict on 2026-07-19:

  «ADMIT TO CANON»

  The exact existing OWNER-SELECTED PAPER ANSWER
  «Control Obligation Grammar» is now a preliminary canon card:

  canon/c-002-gas-behavior-jobs.md
  (status предварительная · режим механика · проверка нужен-грейбокс)

  The admission route
  c-forge-g-d3a8-gas-behavior-jobs-canon-admission-001 is completed.

  What admission established:

  - movement/control is the current minimum common gas-behavior layer;
  - every gameplay gas requires at least one primary readable movement
    Control Obligation in the shared Sphere system;
  - the current grammar is Counter / Brake / Time;
  - volume supplies strength;
  - shell supplies general endurance;
  - universal capture remains intact;
  - gas × shell compatibility remains absent;
  - no mandatory N-player eligibility gate exists;
  - movement-first does not mean movement-only.

  What remains OPEN or UNVERIFIED:

  - gas names, roster, count and job assignments;
  - whether the three families remain exhaustive;
  - additional effects or modifier taxonomy;
  - radiation;
  - reactions and mixed-gas outcomes;
  - forces, cycles, concentrations and thresholds;
  - read channels, controls, UI and VFX;
  - capacity, one-player limits, helper count and player-count scaling;
  - carry tuning;
  - rupture, damage, health, death, rescue and recovery;
  - economy, prices and progression;
  - tools and artifacts;
  - networking, physics architecture and implementation;
  - production scope and balance;
  - fun, runtime legibility, actual 4–8-player value and market response.

  This admission does not admit Minimum Game Frame v2 or the Sphere Frame
  as whole documents.

  No next gameplay-design question is active.

  The Direction OS canon track now routes to a separate cartography session
  that will reconcile the current question map and return to the owner with
  plain-language next-question options.
  QUEUE_INSERT_END

  If a semantically identical c-002 receipt already exists, no-op.

  If a conflicting c-002 receipt exists, stop as a semantic collision.

  Do not change QUEUE.status.

  Do not register an active gameplay-design question in QUEUE.

  ----------------------------------------------------------------------
  4. MARK THE CURRENT QUESTION MAP AS ROUTE-STALE
  ----------------------------------------------------------------------

  Edit:

  ainazemtsau/my_global_workflow/
  live/indie-game-development/work/canon-maps/
  g-d3a8-current-question-front-v2.md

  Insert exactly once immediately after:

  owner_verdict: «A»

  Insert:

  MAP_CURRENTNESS_NOTICE_BEGIN
  post_admission_currentness:
    status: ROUTE_STALE_AFTER_GAS_BEHAVIOR_ADMISSION
    changed_on: 2026-07-19
    reason: |
      The map's §7 current route still names Gas behavior job grammar as
      the one next question. That question has now completed paper
      selection and received the separate owner verdict
      «ADMIT TO CANON».
    live_route: |
      Do not use the old §7 Q3-R recommendation as the current next
      route. The only live canon-track root is:
      c-cartography-g-d3a8-post-gas-behavior-admission-front-001.
    preservation: |
      Existing node descriptions and dependencies remain evidence until
      an owner-approved superseding map is produced. This notice answers
      no design question and promotes no historical answer.
  MAP_CURRENTNESS_NOTICE_END

  If the exact notice exists, no-op.

  If another post-admission currentness notice gives conflicting routing,
  stop as a semantic collision.

  Do not rewrite the graph, node text or historical evidence in this
  RESULT.

  ----------------------------------------------------------------------
  5. CREATE THE SUCCESSOR CARTOGRAPHY CALL
  ----------------------------------------------------------------------

  Add exactly once to repository:

  ainazemtsau/my_global_workflow

  Path:

  live/indie-game-development/work/
  c-cartography-g-d3a8-post-gas-behavior-admission-front-001-call.md

  Add only if absent.

  If byte-identical, no-op.

  A different file under the same path is a semantic collision.

  FILE_CONTENT_BEGIN
  CALL c-cartography-g-d3a8-post-gas-behavior-admission-front-001
  to: session
  direction: indie-game-development
  track: canon
  play: local/canon-cartography
  node: g-d3a8

  goal: |
    The current design-question map is reconciled after the gas-behavior
    answer enters canon, so the owner sees which unresolved design
    questions are genuinely ready next, which remain blocked, and how
    preserved historical floor-loop findings relate to the current route.

  context: |
    Current owner direction:

    - keep the existing «Геймдизайн и канон» track active;
    - do not pause, remove or duplicate it;
    - the previous admission RESULT was not applied because it removed the
      completed root without a replacement root or real pending decision;
    - no repository change or commit was made from that invalid RESULT.

    Exact owner repair approval:

    «Теперь стало понятнее. То есть да, ты совершил ошибку.
    Ну, всё, исправляй тогда запрос.»

    The parent admission RESULT establishes:

    - q-gas-behavior-jobs is admitted as
      gas_coop_game_canon/canon/c-002-gas-behavior-jobs.md;
    - movement-first Control Obligation grammar is now canon;
    - the current minimal grammar is Counter / Brake / Time;
    - all named open and unverified dimensions remain open;
    - no next gameplay-design question was selected.

    Read:

    - live/indie-game-development/NOW.md
    - live/indie-game-development/TREE.md
    - live/indie-game-development/CHARTER.md
    - live/indie-game-development/plays/canon-cartography.md
    - live/indie-game-development/plays/canon-forge.md
    - live/indie-game-development/work/minimum-game-frame-v2.md
    - live/indie-game-development/work/
      gas-sphere-extraction-custody-frame-v1.md
    - live/indie-game-development/work/
      q-gas-behavior-jobs-paper-decision-v1.md
    - live/indie-game-development/work/canon-maps/
      g-d3a8-current-question-front-v2.md
    - live/indie-game-development/history/
      2026-07-18-s-cartography-g-d3a8-post-sphere-frame-front-001.md
    - live/indie-game-development/history/
      2026-07-18-s-forge-g-d3a8-gas-behavior-jobs-001.md
    - live/indie-game-development/history/
      2026-07-19-s-repair-g-d3a8-gas-behavior-admission-route-001.md
    - live/indie-game-development/history/
      s-canon-floor-loop-001.md
    - live/indie-game-development/history/
      s-canon-floor-loop-002.md
    - live/indie-game-development/history/
      2026-07-09-s-repair-canon-core-recovery-001.md
    - live/indie-game-development/work/canon-maps/
      core-concept-rebuild-question-map-v0.1.md
      as REVOKED historical evidence only
    - current gas_coop_game_canon:
      CONSTITUTION.md, CORE.md, INDEX.md, QUEUE.md,
      canon/c-001-investigation-readiness.md and
      canon/c-002-gas-behavior-jobs.md.

    Current routing defect to resolve:

    - the v2 map still names Gas behavior job grammar as the one current
      next question;
    - that question is now resolved and admitted;
    - several downstream questions may have changed readiness;
    - historical floor-loop and floor-board findings remain preserved but
      are not explicitly reconciled with the current map;
    - TREE detail contains older route prose, but TREE may not be changed
      without a separate exact owner-approved G9 diff.

    Owner communication requirement:

    - speak to the owner in simple Russian;
    - explain each question as normal game-design language;
    - do not require the owner to understand or type internal ids;
    - internal codes may appear only in the technical RESULT/CALL block.

  boundaries: |
    Text only.

    Do not answer a new gameplay-design question.

    Do not automatically select the next question.

    Do not redesign or revise c-002.

    Do not reopen the admitted Counter / Brake / Time answer.

    Do not silently restore historical floor-loop or old canon authority.

    Historical material may be classified only as:

    - still-compatible parent/background;
    - current open question material;
    - superseded;
    - conflicting;
    - requiring a new bounded admission route;
    - requiring playable evidence.

    Do not:

    - create gas names, roster or exact count;
    - define additional-effect taxonomy;
    - define radiation mechanics;
    - define reactions or mixed-gas outcomes;
    - define damage, health, death, recovery or rupture;
    - define controls, UI or VFX;
    - define capacity, helper count or scaling;
    - define economy, prices or progression;
    - define artifact mechanics;
    - define networking, physics architecture or implementation;
    - run a greybox, prototype, playtest or visual probe;
    - mutate canon;
    - edit Minimum Game Frame v2;
    - edit the Sphere Frame;
    - edit TREE or CHARTER;
    - open product or Sc-damage work.

    If a current question requires one of those topics, classify it honestly
    as blocked or downstream.

  done_when: |
    1. Current authority is verified, including the applied c-002 card and
       the END_OF_FILE markers of all load-bearing current artifacts.

    2. The current question inventory is reconstructed in simple language:

       - resolved;
       - ready;
       - blocked;
       - downstream;
       - proof later;
       - implementation later;
       - superseded or parked.

    3. The old Gas behavior job grammar node is marked resolved/admitted,
       and every dependency that formerly waited on it is recalculated.

    4. Historical floor-loop, floor-board and related core findings are
       explicitly reconciled.

       Every significant surviving finding is assigned one disposition:

       - already preserved by current Frame/canon;
       - belongs to a current open question;
       - superseded;
       - conflicts with current authority;
       - requires a new bounded paper/admission route;
       - requires playable evidence.

       Nothing is silently imported and nothing is silently discarded.

    5. Any stale route prose outside the map, including TREE detail, is
       identified.

       TREE changes are not applied in this session unless a separate exact
       G9 artifact is shown to and approved by the owner.

    6. The owner receives 2–3 next-question options in plain Russian.

       Each option states:

       - the actual player-facing question;
       - why it matters now;
       - what it unlocks;
       - what remains blocked;
       - one clear downside.

       Include one recommendation.

       Do not make the owner read or choose by internal codes.

    7. The owner approves, revises or rejects the proposed updated map and
       next route with exact words.

    8. On approval, return:

       - one superseding current map:
         live/indie-game-development/work/canon-maps/
         g-d3a8-current-question-front-v3.md;
       - one ready successor Canon Forge CALL for the owner-selected next
         question;
       - no gameplay answer;
       - no canon mutation;
       - no implementation route.

  return: |
    A plain-Russian owner-readable current question map:

    - what has been resolved;
    - what remains;
    - how old floor-loop findings are treated;
    - 2–3 next-question options;
    - recommendation;
    - exact owner verdict.

    Then one writer-safe RESULT containing the superseding map and only the
    owner-approved next route.

  budget: one owner-present text-only session

  END_OF_FILE:
  live/indie-game-development/work/
  c-cartography-g-d3a8-post-gas-behavior-admission-front-001-call.md
  FILE_CONTENT_END

  ----------------------------------------------------------------------
  6. REPLACE THE COMPLETED CANON-TRACK ROOT IN NOW
  ----------------------------------------------------------------------

  Edit:

  ainazemtsau/my_global_workflow/
  live/indie-game-development/NOW.md

  6.1 Set the last-applier-wins header to:

      updated: 2026-07-19 by s-repair-g-d3a8-gas-behavior-admission-route-001

  6.2 Remove exactly the complete open_calls entity whose stable id is:

      c-forge-g-d3a8-gas-behavior-jobs-canon-admission-001

  Do not match or remove by list position.

  6.3 Add exactly once as the replacement root of the existing canon track:

      - id: c-cartography-g-d3a8-post-gas-behavior-admission-front-001
        track: canon
        status: ready
        to: session
        for: "g-d3a8 / reconcile current design-question map after gas-behavior canon admission"
        issued: 2026-07-19
        call: work/c-cartography-g-d3a8-post-gas-behavior-admission-front-001-call.md
        receipts:
          - history/2026-07-19-s-repair-g-d3a8-gas-behavior-admission-route-001.md
        note: "READY / CARTOGRAPHY ONLY / SAME CANON TRACK. c-002 is admitted; v2 still names the resolved gas-behavior question as NEXT. Reconcile the map, explicitly account for preserved floor-loop findings, and show the owner 2–3 plain-language next-question options. No automatic design answer, canon mutation, greybox or implementation."

  6.4 Preserve the existing track exactly as an active parallel track:

      - id: canon
        label: "Геймдизайн и канон"
        mode: parallel
        for: g-d3a8

  Do not pause, remove, duplicate or rename this track.

  6.5 Preserve every other fresh-current field and entity unchanged,
      including:

      - the current primary bet;
      - every task and task status;
      - track_wip_limit;
      - all unrelated tracks;
      - all unrelated open_calls;
      - all unrelated decisions;
      - recurring entries.

  6.6 Preserve global NOW.next after semantic rebase.

      Observed value:

      next:
        call: c-exec-near-gas-l1b-surface-cap-reconcile-001

      This admission CALL was not the global default.

      Do not retarget the direction-wide default to the canon track.

  ----------------------------------------------------------------------
  7. REGENERATE THE OWNER PANEL
  ----------------------------------------------------------------------

  Regenerate only the generated live sections in:

  ainazemtsau/my_global_workflow/
  live/indie-game-development/work/board/dashboard.html

  Regenerate from fresh post-merge NOW, LOG, git and current findings:

  - «📋 Борд»
  - «Журнал»
  - «Проблемы»

  The panel must:

  - keep «Геймдизайн и канон» visible;
  - remove the completed gas-behavior admission root;
  - show the new READY map-reconciliation root;
  - not show the canon track as paused or empty;
  - not claim that a next gameplay-design question has already been chosen.

  This dashboard update is render-only.

  It creates no design or canon authority.

  ----------------------------------------------------------------------
  8. APPEND THE DIRECTION LOG
  ----------------------------------------------------------------------

  Append exactly once before END_OF_FILE in:

  ainazemtsau/my_global_workflow/
  live/indie-game-development/LOG.md

  Exact line:

  2026-07-19 — repair/canon-route (g-d3a8, s-repair-g-d3a8-gas-behavior-admission-route-001): owner verdict «ADMIT TO CANON» admits the exact movement-first Control Obligation answer as preliminary canon card c-002. The prior unapplied close was rejected because it orphaned the active «Геймдизайн и канон» track. Corrected routing keeps the same track active and replaces the completed admission root with READY cartography to update the stale question map, reconcile preserved floor-loop findings and return 2–3 plain-language next-question options; no next design answer, greybox or implementation opened. → history/2026-07-19-s-repair-g-d3a8-gas-behavior-admission-route-001.md

  ----------------------------------------------------------------------
  9. SAVE THIS RESULT TO HISTORY
  ----------------------------------------------------------------------

  Add exactly once:

  ainazemtsau/my_global_workflow/
  live/indie-game-development/history/
  2026-07-19-s-repair-g-d3a8-gas-behavior-admission-route-001.md

  Content:

  - this full RESULT verbatim;
  - followed by:

    END_OF_FILE: live/indie-game-development/history/2026-07-19-s-repair-g-d3a8-gas-behavior-admission-route-001.md

  Add only if absent.

  If byte-identical, no-op.

  A different file under the same path is a semantic collision.

  ----------------------------------------------------------------------
  10. LEAVE UNCHANGED
  ----------------------------------------------------------------------

  In ainazemtsau/my_global_workflow leave unchanged:

  - live/indie-game-development/TREE.md
  - live/indie-game-development/CHARTER.md
  - live/indie-game-development/work/minimum-game-frame-v2.md
  - live/indie-game-development/work/
    gas-sphere-extraction-custody-frame-v1.md
  - live/indie-game-development/work/
    q-gas-behavior-jobs-paper-decision-v1.md
  - live/indie-game-development/plays/canon-forge.md
  - live/indie-game-development/plays/canon-cartography.md
  - live/indie-game-development/knowledge/**
  - product repositories
  - Sc-damage routing
  - os/**

  In ainazemtsau/gas_coop_game_canon leave unchanged:

  - CONSTITUTION.md
  - CORE.md
  - AMENDMENTS.md
  - canon/c-001-investigation-readiness.md
  - every other existing canon card
  - historical evidence

  Preserve every unrelated working-tree modification byte-for-byte.

  ----------------------------------------------------------------------
  REQUIRED POSTCONDITIONS
  ----------------------------------------------------------------------

  - exactly one c-002 card exists at:
    canon/c-002-gas-behavior-jobs.md;

  - INDEX contains exactly one c-002 entry;

  - QUEUE still states:
    NO ACTIVE DESIGN QUESTION;

  - QUEUE records c-002 admission and the map-reconciliation route without
    selecting another gameplay-design question;

  - the v2 map contains exactly one post-admission currentness notice;

  - the v2 map's old Gas behavior NEXT recommendation is explicitly marked
    non-live;

  - NOW still contains exactly one track with id canon;

  - the canon track remains mode parallel;

  - NOW contains no open_call with id:
    c-forge-g-d3a8-gas-behavior-jobs-canon-admission-001;

  - NOW contains exactly one root open_call on the canon track:

    c-cartography-g-d3a8-post-gas-behavior-admission-front-001;

  - that root has status ready;

  - no pending decision is invented;

  - global NOW.next remains unchanged after rebase;

  - no gameplay-design question is automatically selected;

  - no greybox, product or implementation work is opened;

  - the original paper artifact remains unchanged;

  - TREE and CHARTER remain unchanged.

captures: []

decisions_needed: []

play_check:
  - 1 Name the contradiction: done — the prior unapplied RESULT removed the completed canon-track root while retaining the track, but created neither a replacement root nor a real pending owner decision.
  - 2 Reconstruct: done — current NOW still contains the canon track and old admission root; the v2 map exists with many downstream questions but still names the now-resolved gas-behavior question as NEXT; historical floor-loop findings remain preserved but unreconciled.
  - 3 Propose corrected state: done — keep the same canon track active, admit c-002, mark the v2 route stale, and replace the completed admission root with one READY cartography root that updates the map before any new design question begins.
  - 4 Confirm (owner): done — exact owner approval: «Теперь стало понятнее. То есть да, ты совершил ошибку. Ну, всё, исправляй тогда запрос.»
  - 5 Friction: skipped — this was a one-off assistant RESULT-packaging error, not a demonstrated recurring hole in the Direction OS rules; no os/FRICTION.md or os/** change is justified.

log: 2026-07-19 — repair/canon-route g-d3a8: c-002 admission preserved; orphan-track close corrected by keeping the same active canon track and routing next to question-map reconciliation with historical floor-loop accounting and owner choice.

next: |
  call: c-cartography-g-d3a8-post-gas-behavior-admission-front-001
  track: canon
  status: ready
  route: reconcile the current question map after c-002 admission, account
    explicitly for preserved floor-loop findings, and present 2–3
    plain-language next-question options to the owner before opening another
    Canon Forge answer.
  preserve_global_now_next: true

END_OF_FILE: live/indie-game-development/history/2026-07-19-s-repair-g-d3a8-gas-behavior-admission-route-001.md
