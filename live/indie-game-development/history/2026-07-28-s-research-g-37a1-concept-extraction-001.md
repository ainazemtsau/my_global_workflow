# RESULT s-research-g-37a1-concept-extraction-001

call: c-research-g-37a1-concept-extraction-001
direction: indie-game-development
play: research
node/task: g-37a1/concept-extraction

outcome: |
  ANSWERED, IN FULL, WITHIN BUDGET, WITH NO OWNER STEP AND NO CHECKPOINT. Every item
  of work/concept-chats-answers-g-37a1.md is classed FORM or CONTENT; there is no third
  bucket and nothing is dropped. THE ANSWER: the material DOES change the form, in eight
  places, and NOT ONE of the eight adds, removes or alters a rule of the game. All eight
  are seams — places something later plugs into — and they are the same class of thing as
  his own architectural instruction of 2026-07-28 («в ядре сразу должно быть зашито …
  ядро уже должно быть готово к кооперативу»), which he himself ruled goes to shape/PLAN
  and NOT to the card. The sixteen signed lines, the fifteen criteria and every closed
  ruling are untouched: no line was reopened, no contradiction was resolved, no owner
  decision was manufactured, and no acceptance apparatus was restored.

  ACCOUNTING, so nothing is silently dropped. TWENTY seam claims were returned (chat 1: 6,
  chat 2: 7, chat 3: 7) and they deduplicate to EIGHT distinct seams, every claim mapped.
  ONE HUNDRED AND NINE block-B items were returned (37 + 54 + 18); they are parked, MINUS
  three of chat 3's which are not content at all — see the finding below. TWENTY-THREE
  block-C items were returned; thirteen are named contradictions, two are false findings
  verified first-hand, five are frame-confirmations naming things the material never
  proposed for the first core, one is a resolution attempt the chat made inside its own
  block C and is noted rather than adopted, and two collapse into the thirteen. ONE
  CONTRADICTION WAS NOT FLAGGED BY ANY CHAT and is added. The two source texts and the
  three plugin lists are classed at the end of this outcome.

  THE FRAME THAT ORGANISES THE WHOLE ANSWER, and it is not in the material — it comes from
  his own branch-2 verdict. The engine stays and the rewrite is confined to the
  structure/topology layer. So HALF THE FORM LIST IS NOT «BUILD A NEW SEAM», IT IS «WHAT
  THE TOPOLOGY REWRITE MUST NOT FLATTEN». By the direction's own first-hand record
  (i-engine-fit-decision-ladder, product 1a6373b8) the product already carries multi-kind
  per-cell occupancy, graded conductivity over open sub-faces, and a banked
  determinism-and-replication layer. A rewrite is precisely the moment someone simplifies
  substance to two named fields and conductivity to a boolean neighbour test. F1, F7 and
  F8 are guards against that; F2, F3, F4 and F6 are genuinely new because runtime
  closed-to-open mutation does not exist today and topology therefore enters the snapshot
  for the first time.

  ---

  FORM — EIGHT SEAMS. Each carries: the seam in one sentence, why arriving late is a
  REWRITE and not an extension, the minimum that must exist in the first core for the seam
  to be real, and a confidence mark. NONE of them is a working feature and none changes
  what the player does.

  F1 — SUBSTANCE IS STORED PER CELL AS A SET KEYED BY A STABLE ID, NOT AS TWO NAMED FIELDS
  AND NOT AS A NUMBER ON A POCKET.
    · Seam: a cell holds quantities addressed by SubstanceId; exactly two ids are
      registered in the first core.
    · Why late = rewrite: a third kind — or liquid, which by his own addition may enter
      «как замену газа» rather than as an addition — otherwise changes the cell format, the
      solver loop, the configuration and the network format in one move, i.e. all four
      layers at once, and every calibrated knob value with them. The second half is
      separately load-bearing: if a pocket is «a number», M1 and M2 («total unchanged after
      a breach», «the released mass is in the cut space») are not assertable at all,
      because there is no place for the mass to be. Chat 3's own core sketch reaches the
      same conclusion independently: «Газовый карман … не "объект-источник". Это заранее
      созданная группа пустых клеток».
    · Minimum: two registered ids and per-cell mass access by id. No third behaviour, no
      third id, no reaction of any kind.
    · Confidence: HIGH as a seam; the rewrite claim is high for the two-named-fields form
      and MEDIUM for the per-cell form, because the record says the product already stores
      multiple kinds per cell — so this is preserve-under-rewrite, not new construction.
    · Sources: chat 1 A1, chat 2 A2, chat 3 A5 — independent three-way convergence.

  F2 — EVERY WORLD CHANGE GOES THROUGH ONE ORDERED, TICK-STAMPED CONTRACT WITH A SINGLE
  ATOMIC COMMIT.
    · Seam: a dig command carrying a tick number, and one commit producing a topology delta
      with a revision id.
    · Why late = rewrite: this path is being written from scratch RIGHT NOW — the
      engine-fit check established first-hand that runtime closed-to-open mutation is
      absent in the product — and ROW 16 requires two machines to agree about a world both
      of them mutate (§SEAM 5). Ordering is decided the moment the mutation path is
      written; retrofitting a canonical order onto direct cell mutation means rewriting the
      dig code, the network edge and the substance coupling together, because each of the
      three will already have its own reconstruction of what a cut did.
    · Minimum: one serializable command type with a tick; one commit producing a delta with
      an operation/revision id and the changed cells; a failed step leaves no partially
      changed geometry, mass or player state. NO rollback, NO prediction, NO reconciliation
      in the first core.
    · Confidence: HIGH.
    · Sources: chat 1 A2, chat 2 A4, chat 3 A2 — independent three-way convergence.

  F3 — THE SINGLE SOURCE OF TRUTH ABOUT DUG SPACE IS THE CORE'S OWN LOGICAL GRID; MESH,
  COLLIDER AND ANY TERRAIN PLUGIN SIT BELOW IT BEHIND A THIN REPLACEABLE BACKEND.
    · Seam: one interface — «apply this cell/chunk change» plus «rebuild finished» — with
      exactly one implementation today.
    · Why late = rewrite: if substance, network and digging each read the plugin's
      geometry, then replacing the backend becomes a migration of all three at once, and
      the backend is explicitly an OPEN shape decision under the branch-2 verdict. This
      seam is what makes the backend choice cheap; without it the choice is irreversible.
    · Minimum: the plugin/mesher is a consumer of topology changes and never an authority
      on them; nothing in substance, air, death or network reads plugin state.
    · Confidence: HIGH. It also STRENGTHENS his cubic ruling rather than competing with it:
      if the dug geometry and the gas grid are the same lattice, this interface is thinner
      still, and it is the reason a Core-owned grid and a bought plugin can be compared at
      shape without the comparison being a rewrite either way.
    · Sources: chat 3 A1 and A3; chat 2 A3's stable cell/face ids and authoritative
      passability interface.

  F4 — THE AUTHORITATIVE WORLD-STATE FORMAT IS VERSIONED AND MADE OF NAMED SECTIONS.
    · Seam: a snapshot envelope with a format version and stable section ids; adding a
      section does not change how existing sections are read.
    · Why late = rewrite: topology enters the authoritative snapshot for the FIRST time in
      this core, so the envelope is authored now whether anyone decides it or not. If it is
      serialized as one fixed struct, every later state — excitation, a third kind, a
      liquid, anything — breaks snapshot, checksum, replay, reset and the network protocol
      simultaneously, and the determinism-and-replication layer his branch-2 verdict
      explicitly PRESERVES is exactly the layer that would have to be re-derived.
    · Minimum: a version field and sections with stable ids; today the sections are
      topology, two substances and the player. A future section must register its
      serialization, its hash contribution and its reset — no such section exists now.
    · Confidence: HIGH.
    · Sources: chat 1 A4, chat 2 A5 (medium there), chat 3 A7 — independent three-way
      convergence.

  F5 — THE SUBSTANCE STEP IS A NAMED, ORDERED SEQUENCE OF PHASES WITH AN EMPTY
  REGISTERED-HANDLER STAGE, SEPARATE FROM TRANSPORT.
    · Seam: an ordered phase list with a documented canonical order and a transactional
      result type (checkable mass deltas); the handler registry is EMPTY.
    · Why late = rewrite: inserting a phase inside a monolithic transport loop later
      changes the order of computation, and order is what the co-op hash and the
      repeatability of a run rest on — the same layer his verdict banks. Changing that
      order after two machines have agreed on it is not an extension.
    · Minimum: the step expressed as a phase list; zero registered handlers; nothing
      resembling a reaction, which criterion 13 forbids outright.
    · Confidence: MEDIUM, AND THIS IS THE WEAKEST ITEM ON THE LIST — stated plainly rather
      than smoothed. «Leave an empty hook» is the textbook speculative-generality trap; a
      deterministic phase that nobody registered cannot change any result, so the rewrite
      argument only bites if a state hash exists and the order moves. IT MUST COST ALMOST
      NOTHING OR IT FAILS HIS OWN RULE «минимум с запасом, не максимум». If shape finds it
      costs more than naming the phases, it should be dropped rather than defended.
    · Sources: chat 1 A3, chat 2 A6, chat 3 A6 — independent three-way convergence.

  F6 — THE COMMITTED TICK EMITS TYPED FACTS: A READ-ONLY SNAPSHOT, PER-FACE TRANSFER, AND
  TOPOLOGY CHANGE.
    · Seam: an extensible event collection carrying tick, cell id, face id and transferred
      amount, produced by the committed tick.
    · Why late = rewrite, AND THE REASON IS NOT THE ONE THE CHATS GAVE. They argued it for
      future sound, light and warning impulses — all of which are CONTENT and are parked.
      The seam survives on a different and stronger ground: it has a consumer in the FIRST
      core. Requirements line 9 and criterion 6 require that a breach be an EVENT with an
      onset and an end, «а не изменение числа». If that event is reconstructed after the
      fact by polling state, every later consumer re-derives it differently — which is the
      exact failure the chats describe, arriving one version earlier than they thought. It
      also serves M4, whose assertion compares the field's evolution with the player
      present, elsewhere and absent.
    · Minimum: the tick's committed result carries typed facts; the only consumers in the
      first core are ROW 9's breach event and the renderer. No sound, no impulses, no
      warnings, no flux voices.
    · Confidence: HIGH.
    · Sources: chat 1 A5 (medium there), chat 2 A7.

  F7 — THE AUTHORITATIVE CORE IS ENGINE-FREE AND THE BOUNDARY TO PRESENTATION AND TRANSPORT
  IS ONE-WAY.
    · Seam: TickInput / WorldState / StepResult as plain types; Unity, renderer, audio and
      the network transport are adapters and consumers only.
    · Why late = rewrite: M1–M8 are REAL TESTS IN THE PRODUCT'S OWN GATE by the signed
      §CHECK, and the direction carries a standing owner law that a self-written scanner is
      forbidden as behaviour evidence and an unavailable tool STOPS the leg. A gate that
      needs a renderer is not a gate. If damage, air cost, mass or authority ever read GPU
      or particle state, the whole acceptance layer becomes unrunnable and two machines
      stop being able to agree at all — which is the substance of chat 1's own block-C item
      about a non-deterministic client-side substance authority.
    · Minimum: the core computes a tick with no engine present; renderer/audio/VFX receive
      snapshots and events and return nothing into the law, the air rate, death or the
      hash.
    · Confidence: HIGH — and by the direction's own record this is largely ALREADY TRUE
      (branch 2 preserves the transport, determinism-replication and render layers), so the
      binding form of this item is «the new topology and dig code lands in the engine-free
      core, not in MonoBehaviours». Not verified against the repository this leg: the CALL
      forbids a product read, so this rests on state, not on a fresh inspection.
    · Sources: chat 2 A1, chat 1 A6, chat 3 A7 in part.

  F8 — CONDUCTIVITY IS COMPUTED FROM AN OPEN-AREA QUANTITY OBTAINED BY A TOPOLOGY QUERY,
  NOT FROM A BOOLEAN «IS THE NEIGHBOUR OPEN».
    · Seam: `openFaceArea` / `openVolumeFraction` as queries whose first-core range happens
      to be {0, 1} at a one-metre cell, with aperture width expressed by the COUNT of open
      faces (chat 3's own sketch: «одна открытая грань — малая проводимость; четыре
      открытые грани — примерно вчетверо большая площадь»).
    · SPLIT FIRST, because half of what chat 3 called a seam is already a signed
      requirement and is NOT future work: «чем шире рез, тем сильнее пошло» is requirements
      line 9 and criterion 6 OF THE FIRST CORE. What is genuinely a seam is only the
      signature: the solver's input stays an area-like number obtained from topology, so
      sub-cell refinement later does not change the solver's contract or its calibration.
    · Why late = rewrite: if the transport law is written as `if (neighbour open) transfer
      = k`, then grading it later changes the core law itself and invalidates every knob
      value calibrated against it. The record says graded conductivity ALREADY SHIPS over
      open sub-faces, so — like F1 — the real risk is the topology rewrite flattening
      something that exists.
    · Minimum: the conductivity input is a number from a topology query; the query may
      return only 0 or 1 per face in the first core; microvoxels and sub-cell resolution
      are CONTENT and are parked.
    · Confidence: MEDIUM, with the honest counter stated: if F4 stands, adding an area
      field later is an extension of the FORMAT, so this item's rewrite claim rests
      entirely on the solver's law, not on the snapshot.
    · Sources: chat 3 A4 (medium there); chat 2 A3 in part.

  WHAT THE FORM LIST DOES NOT CONTAIN, stated so its silence is not read as coverage: no
  camera decision, no backend decision, no plugin purchase, no cell size, no tick rate, no
  knob value, no schema for the layout file, no estimate in days, and nothing about how a
  session is entered — late-join stays struck and the material's mentions of it are parked
  exactly as ROW 16 intends.

  ---

  CONTENT — PARKED AS INPUT TO THE NEXT VERSION, TOUCHING NOTHING. The verbatim lists stay
  where they are, in work/concept-chats-answers-g-37a1.md, which holds no authority. The
  deduplicated index of what is parked, thirteen groups covering all 109 block-B items and
  both source concept texts:

  1. «Живой газ» as a kind: rest / excitation / refractory states; a wave of excitation
     travelling at finite speed only through connected mass; splitting at forks;
     attenuation in thin or rarefied links; a full blocking threshold; spiral and scroll
     waves; annihilation of meeting fronts.
  2. Wave triggers and their honesty: breach, flow jump, volume connection, reaction; the
     impulse as an advance warning of a physical front; a guaranteed interval between
     signal and danger; protection against a free sonar, against spam, threshold chatter
     and habituation; hysteresis, cooldown and event coalescing.
  3. The mine as anatomy: chamber = lung, slit = larynx, tunnel = trachea, fork = nerve
     branch, sealed pocket = resonator, several openings = several voices of one body.
  4. The procedural voice of a real aperture: loudness from flow and pressure drop; pitch
     from jet speed and aperture width; formants and depth from the connected volume;
     chorus width from the number of exits; a bounded audio voice pool; `OnAudioFilterRead`
     and `AudioClip.Create` as the mechanism.
  5. Visual identity: dark viscous calm gas with rare inner veins; a light nerve impulse;
     filaments along density gradients and flow; a glowing trail behind a moving player;
     refractory dimming; pareidolic faces, hands and figures with the four never-rules;
     shared world-space apparition events.
  6. The ambiguity doctrine: physics / distributed organism / colony, never confirmed, no
     bestiary; and the explicit ban list — recorded human or animal screams, intelligible
     words, permanent eyes, mouth or head, reaction to the camera, movement toward the
     nearest player, instant sync of disconnected pockets, a dedicated cleanup weapon; the
     Rockpox and sculk precedents.
  7. Metabolism as the strongest reaction: the living gas absorbs the more dangerous one,
     mass converting rather than vanishing, excitation rising, an infected return route,
     one signature for all reactions; stoichiometry, overflow and a designed shortage.
  8. Co-op scenes: «what did you open», two impulses meeting at a fork, the crew
     accidentally teaching the gas to sing, the return path waking section by section.
  9. Persistent identity of connected volumes and their lineage after split and merge.
  10. Value and goal content: core extraction, value below, a destination at the bottom,
      the reason to descend, the meaning of the descent.
  11. Visual and technical backends: full-volume raymarch, a dedicated R8/RG8 excitation
      texture, a sparse GPU front buffer, dirty-chunk updates, visual LOD and area of
      interest, a regional representation of distant gas, a separate NVIDIA Flow R&D track,
      the choice of a commercial visual plugin.
  12. Simulation depth and numbers: reaction–diffusion, FitzHugh–Nagumo, Oregonator, full
      CFD, wave acoustics; concrete speeds, thresholds, delays and refractory durations;
      caps on active cells and simultaneous waves; microvoxel resolutions 2×2×2, 4×4×4,
      16×16×16; concrete kinds, names, parameters and presets; reaction rules and effects;
      colours and other channels for telling kinds apart; volumetric smoke, fire and
      particles; liquids, water, lava; collapses and weather; inventory, items, tools and
      upgrades; rock damage progress, dig durations and different tools.
  13. Rigs and studies: the two-hole and Y-shaped test stands, perceptual A/B with a yoked
      control, animacy playtests, criteria for «feels alive» — parked as CONTENT and
      flagged separately in the contradictions, because chat 1's source text states them as
      an acceptance procedure.
  Also parked and consistent with existing decisions rather than in tension with them:
  late join, host migration and client visual correction; a dedicated headless server;
  chunk checksums and corrective snapshots; procedural or infinite world generation.

  A FINDING INSIDE THE PARKING LIST, AND IT IS THE MOST DANGEROUS ITEM IN THE WHOLE DROP.
  Chat 3 parked THREE things that are not content at all but signed requirements of the
  FIRST core, and no block C flags them. Taking its block B as given would have quietly
  deleted two requirements:
    · «Читаемость положения и примерного размера кармана до вскрытия» IS requirements line
      14 and criterion 2: «Порода читается: до реза видно, что за ней карман и примерно
      насколько большой». NOT parked.
    · «Разная скорость потока через узкие и широкие отверстия» IS requirements line 9 and
      criterion 6: «чем шире рез, тем сильнее и быстрее пошло, узкий надрез даёт тонкую
      струйку». NOT parked.
    · «Рабочая градуированная проводимость частично открытых граней» IS parked as written,
      because PARTIAL faces are sub-cell resolution — but the requirement it serves (line 9)
      is signed and must be satisfied at whatever resolution the first core picks. Parked
      with that rider attached.

  ---

  CONTRADICTIONS — THIRTEEN, EACH WITH BOTH TEXTS, NONE RESOLVED. Every one is the same
  shape: parked CONTENT touching a signed line. No requirement moves.

  C1 REACTIONS AND METABOLISM. Material: «Живой газ способен поглотить второй, значительно
    более опасный газ: опасный газ исчезает как свойство, но вся его масса превращается в
    дополнительный объём живого газа». Signed: criterion 13 — «Также не появляются: реакции
    между веществами»; §SEAM 2 — «Two kinds meeting in the same space … Seam: they mix and
    nothing else». NAMED. (F5 is an EMPTY registry and is not this.)
  C2 CLEARING AN IMPASSABLE REGION. Material: «Игроки хотят соединить карманы, потому что
    живой газ очистит непроходимую область». Signed: criterion 7 — «Войти можно в любой
    карман. Разница между видами — цена воздуха, а не физическая преграда; физической
    непроходимости нет». NAMED.
  C3 CORE EXTRACTION, VALUE BELOW, A DESTINATION AT THE BOTTOM. Material: «Возвращение после
    ядра. Если изъятие ядра уже создаёт физическую волну давления или тепла…». Signed:
    criterion 13 — «ценность внизу и любая цель на дне участка, а также условие завершения —
    в ядре нет ни победы, ни прохождения, ни финального экрана»; his own words «в ядре нет
    такого, да, то есть вообще убрать ценность». NAMED.
  C4 CUTTING A DRAIN. Material: «успеть прорубить сброс». Signed: requirements line 11 —
    «Вещество никуда не исчезает: ушло из кармана — оно в выработке. Стоков нет»; §GLOSSARY
    «сток» — «In this outcome: none.» NAMED. Chat 2 additionally offered a resolution inside
    its own block C («описанный вариант с преобразованием массы этого противоречия не
    создаёт»); NOTED AND NOT ADOPTED — resolving is not a chat's work and not this leg's.
  C5 CLOSING A BRANCH BY RESTORING ROCK. Material: «закрыть выбранную ветку». Signed:
    requirements line 8 — «Выкопанное обратно не закапывается»; M3 — open volume is monotone
    non-decreasing. NAMED.
  C6 A PLAYTEST AS THE CORE'S CLOSING CONDITION — AND THIS IS THE ONE THE DIRECTION HAS A
    STANDING BAN ON. Material, from chat 1's own source text: «Проверка успешна, если
    незнакомые с идеей игроки: правильно находят источник события; начинают использовать
    импульс для решений; сами говорят "оно проснулось / вскрикнуло / почувствовало"».
    Signed: requirements line 17 and criterion 14 — «Результат достигнут, когда ядро собрано
    и владелец в него зашёл … оно НЕ оценивается по "весело / не весело"»; and his cut of
    2026-07-28 — «не надо нам формально прописывать то, что я буду тестировать … Не надо вот
    таких абстрактных линеек». NAMED, AND NOTHING FROM IT IS RESTORED anywhere in this
    RESULT: no deck, no sample size, no pass bar, no prescribed sitting.
  C7 MORE THAN TWO KINDS, AND REACTION PRODUCTS. Material: «Дополнительные вещества, продукты
    реакций и набор разных химических результатов». Signed: requirements line 13 — «два вида
    различаются на глаз»; criterion 7. NAMED — and F1's minimum registers exactly two ids and
    admits no third.
  C8 A «SIGNIFICANTLY MORE DANGEROUS» GAS, AN AUTONOMOUS DANGEROUS FRONT, AN INFECTED ROUTE.
    Material: «значительно более опасный газ … заражённый обратный маршрут … проблему,
    которую нельзя просто удалить». Signed: criterion 7 — «Разница между видами — цена
    воздуха, а не физическая преграда». NAMED. RIDER, and it belongs to us rather than to the
    chats: the request's frame said «Воздух — единственный ограничитель», which is STRICTER
    than the signed text — §GLOSSARY «счётчик» reads «Air is A counter of the player's.
    Exclusivity is gone», softened by him on 2026-07-27.
  C9 HIDING CUBICITY WITH SMOOTHING. Material: «визуальную кубичность при необходимости
    скроет Surface Nets»; «Surface Nets может визуально сглаживать поверхность, не меняя
    логические voxel-данные». Owner ruling d-core-geometry-and-view-001: «делаем максимально
    лучше визуал, который мы можем с кубическими сделать» — the best look achievable INSIDE
    cubic — and the recorded consequence of his own admitting argument is that cubic geometry
    DELETES surface smoothing and post-cut collider regeneration, because the dug geometry
    and the gas grid become one structure. HIS EXACT WORDS DO NOT BAN SMOOTHING. NAMED, NOT
    RESOLVED, and it travels to shape with the backend choice.
  C10 DIALLING POCKET VOLUME AND INITIAL FILL FROM THE RUNNING RIG. Material, chat 3's rig
    list: «объём и начальное заполнение кармана». Signed: requirements line 5 — «Разметка
    участка из запущенной игры не меняется: это авторское содержимое — габариты и карманы
    (сколько, где, каких размеров и каких видов)»; criterion 12 — «Это инструмент
    эксперимента, а не генератор уровней»; ROW 5 — «The built player may change NOTHING
    about the section». NAMED. (Chat 3 flagged this itself; confirmed first-hand.)
  C11 PER-KIND DIFFUSION COEFFICIENT AND A DANGER THRESHOLD AS THE DIFFERENCE BETWEEN KINDS.
    Material, chat 3's `GasDefinition`: «коэффициент распространения … возможный порог
    опасности». Signed: requirements line 13 — «Войти можно в любой карман; разница — цена
    воздуха, а не преграда». NAMED, NOT RESOLVED — and stated honestly: the signed line
    governs PASSABILITY, nothing signed requires the two kinds to MOVE identically, and the
    exclusivity of air as the only counter is explicitly gone in §GLOSSARY, so chat 3's own
    flag is over-strict on the diffusion half and lands on a real question only for «порог
    опасности». Same rider as C8: it was measured against the request's tightened frame.
  C12 PERSISTENCE OF AN UNFINISHED SECTION BETWEEN LAUNCHES — FLAGGED BY NOBODY, ADDED HERE.
    Material, chat 3 block B: «Сохранение и восстановление незавершённого участка между
    запусками». Signed: requirements line 4 — «умер — уровень перезапускается ПОЛНОСТЬЮ и
    сразу; между заходами ничего не копится»; §GLOSSARY «состояние захода» — «None of it
    survives a death or a relaunch.» It is parked, so it does nothing today; it is named
    because it arrived unflagged and the day someone picks it up it is a collision.
  C13 THE CO-OP ORDERING TENSION, AND BOTH TEXTS ARE HIS. Material, chat 3 block C:
    «Формулировка "кооператив сразу после первого играбельного ядра" противоречит рамке
    "кооператив заложен с первой строчки"». Text A, criterion 11: «Сетевая основа не
    откладывается — кооператив идёт сразу за первым играбельным ядром, а не после игры».
    Text B, requirements line 16: «Сетевая основа с первой строчки; старт одному и старт
    вдвоём на второй машине». NAMED AND NOT RESOLVED, per the CALL's explicit instruction.
    Recorded for shape rather than left dangling: state already holds the binding form at
    i-core-acceptance-instrument-unpriced (R7) — a shape leg may not defer the network basis
    PAST g-37a1, while distributing g-37a1's own rows across its own bets is ordinary
    sequencing. This leg adds nothing to that and decides nothing.

  TWO FALSE FINDINGS, BOTH FLAGGED AT INTAKE AND BOTH CONFIRMED FIRST-HAND HERE, so no round
  is ever spent on them:
    · Chat 3: «Переключатель бессмертия противоречит рамкам». WRONG. Requirements line 5 —
      «режим бессмертия — воздух тратится, ноль не убивает. Переключатели по умолчанию
      выключены» — and criterion 12 carries the same under his `да`. A rig knob defaulting
      OFF. The finding was produced by the request's own frame list, which omitted the
      switch and tightened air to «единственный ограничитель».
    · Chat 3: «Свежие 17 утверждённых требований» versus sixteen. A READING ARTEFACT of the
      file's own preserved numbering: work/core-requirements-g-37a1.md still carries the
      heading «Набор — семнадцать строк» with the amendment banner «Живых строк шестнадцать»
      and line 7 struck IN PLACE so the card, the rows and the technical check keep their
      references.

  FIVE FRAME-CONFIRMATIONS, listed so they are not miscounted as live collisions. Chat 1's
  block C names Dungeon Architect/PGG as a first-core generator, FluXY or another 2.5D path,
  Godot/Unreal/Luanti/Flax/O3DE/Stride/Bevy/Fyrox as the production engine, and any
  Flow/Zibra/Braze/FluidNinja loop as a non-deterministic client-side substance authority;
  chat 3 names Digger PRO on Unity Terrain. None of these is PROPOSED for the first core by
  the material — each is named as a path the frames exclude, and all five agree with his
  branch-2 verdict, his 2.5D rejection and F7. Nothing to do.

  ---

  PLUGIN AND TOOL INVENTORY — INVENTORY, NOT A DECISION, AND NO PLUGIN IS A FORM ITEM
  because F3 is precisely what makes the backend a shape choice.
    · CHAT 2 FOUND NOTHING NEW: «Новых сторонних плагинов, кроме уже известного Voxel Play 4,
      в этом чате не найдено». What it lists is the stack we already use — Unity 6, URP 17,
      RenderGraph, Texture3D, compute shaders, FishNet, `OnAudioFilterRead`,
      `AudioClip.Create`, `AsyncGPUReadback` (explicitly NOT a source of authoritative
      simulation).
    · CHAT 3 RECOMMENDS BUYING VOXEL PLAY 4 and nothing else: version 41.3 published
      2026-07-16, marketplace showing $74.99 against a normal $149.99; Digger PRO as the
      fallback bought only if Voxel Play fails a short technical check; no gas plugin needed.
      Its cited properties: direct voxel/chunk operations, spherical and block destruction,
      Surface Nets smoothing over unchanged logical voxel data, chunk-change events and RLE
      data via `GetChunkRawData`/`SetChunkRawData` including microvoxels, extension by
      events and partial classes without forking. STATED AS THE CHAT'S CLAIMS; not verified
      by this leg, which may not read the product or re-check the engine.
    · WHERE THAT SITS AGAINST OUR OWN RECORD, and the two do not agree: after his cubic
      ruling, state has the narrow Core-owned grid AHEAD of Voxel Play 4, because a
      general-purpose voxel engine solves problems this core does not have — infinite world,
      streaming, refill. THE DISAGREEMENT IS SHAPE'S TO SETTLE, NOT FORM'S, and F3 is what
      keeps the cost of settling it wrong low.
    · The rest of the inventory is CONTENT-side or already-rejected: NVIDIA Flow, Unity VFX
      Graph, Shader Graph, Six Way, EmberGen, Zibra Smoke & Fire, Zibra Liquid, BrazeFX,
      FluXY, Kronnect Volumetric Fog & Mist, Obi Fluid, FluidWorld, Digger PRO, Voxelica /
      Voxel Generator, MudBun, Voxel Play 3, Voxel Digging Master, Dungeon Architect, Voxel
      Farm, Clayxels, Ultimate Terrains, Voxeland, ProBuilder, Realtime-CSG, SabreCSG,
      Chisel, pb_CSG, LibCSG, EzySlice, Unity Terrain / Terrain Holes, OpenVDB/NanoVDB,
      NVIDIA Blast, Niagara, FluidNinja, Luanti, Godot 4 + Zylann Voxel Tools, Unreal 5 +
      Voxel Plugin 2, Flax, O3DE, Stride, Bevy, Fyrox; open-source references
      qhdwight/voxelfield (GPL-3.0), jedjoud10/VoxelTerrain (licence unstated),
      Javier-Garzo Marching-Cubes-on-Unity-3D (MIT), transvoxel-unity (MIT), Fast Unity
      Marching Cubes, Eldemarkki voxel examples; techniques Surface Nets, Marching Cubes,
      greedy meshing, Unity Jobs and Burst, microvoxels, RLE chunk buffers. ONE LICENCE FACT
      WORTH CARRYING: the strongest server-authoritative destructible-voxel reference is
      GPL-3.0 and therefore unusable as a source for a paid product, and one reference states
      no licence at all.
    · THE ONLY ITEM IN THE ENTIRE DROP THAT COSTS MONEY is the Voxel Play 4 purchase, and it
      is his if shape ever proposes it. Named, not recommended, not decided.

  ---

  ONE OBSERVATION ABOUT OUR OWN TEXT, recorded because it produced findings rather than as
  hygiene: THE REQUEST'S FRAME LIST IS TIGHTER THAN THE SIGNED SET IN AT LEAST TWO PLACES.
  It states «Воздух — единственный ограничитель» where §GLOSSARY «счётчик» records that
  exclusivity is GONE on his own softening of 2026-07-27; and it omits the immortality
  switch, which is signed requirements line 5 and criterion 12. Both of chat 3's
  false/over-strict block-C items descend from exactly those two lines. The signed text
  governs and nothing needs deciding; the lesson is that a paraphrased frame list is a
  source of manufactured contradictions, and a future request should quote the signed lines
  rather than restate them.

  WHY NO OWNER QUESTION IS BROUGHT, since done_when 5 makes checkpointing the default when
  one is forced. Every contradiction is parked content meeting a signed line, so no
  requirement moves and no verdict is needed. C13 is already held and already corrected in
  state. C9 and the backend/plugin disagreement are shape decisions by his own branch-2
  verdict. C11's «порог опасности» is future content. The request's over-tight frame is a
  defect of a work file, not of a requirement. Manufacturing a question out of any of these
  would be the thing the CALL forbids.

evidence: |
  Read first-hand this leg, in full or in the named sections:
  - work/concept-chats-answers-g-37a1.md — the entire 889-line source, all three chats'
    blocks A/B/C, both concept source texts and all three plugin lists.
  - work/concept-extraction-request-g-37a1.md — the eleven frames actually sent, which is
    how the two frame-descended false findings were diagnosed.
  - work/core-requirements-g-37a1.md — all seventeen slots with line 7 struck in place,
    both amendment banners, the settings register, the two owner questions, the three owner
    answers and «Принято к следующей итерации».
  - work/converge-g-37a1-core-rows.md — §CHECK with M1–M8 and its three non-negotiable
    rules; §GLOSSARY (вещество, карман, счётчик, смерть, база, заход, состояние захода,
    уровень, сток, настройка, спорное число); ROW 5, ROW 9, ROW 10, ROW 11, ROW 12, ROW 13,
    ROW 14, ROW 16; §KNOBS both tables; §WHAT's coverage table; §SEAM 1–5;
    §BUILD-CLOSES-BETTER; §DIED-WITH-THE-CUT.
  - TREE.md g-37a1 — all fifteen criteria verbatim.
  - CHARTER.md — mission, lens 3, premortems 2 and 3.
  - NOW.md — direction_forecast drivers, i-engine-fit-decision-ladder,
    i-card-clauses-unverifiable, i-core-acceptance-instrument-unpriced,
    d-core-geometry-and-view-001, d-core-level-authoring-001, d-post-verify-route-001,
    and the open_calls block.
  Method: the twenty seam claims were extracted individually before any merge, exactly as
  the intake required (chats 1 and 2 compared before chat 3 was folded in at all), then
  each was tested against three bars in order — is it a PLACE something plugs into rather
  than a working feature; does arriving late cost a REWRITE rather than an extension; and
  is it already held by a signed line, a row or a banked layer. Every block-B and block-C
  item was walked one by one against the requirements file and the card rather than against
  the chats' own claims about them, which is what surfaced the three mis-parked signed
  requirements and the one unflagged contradiction.
  Not done, by the CALL's boundaries: no product repository read, no engine re-check, no
  estimate in days, no answer to d-air-counter-visibility-001, no restoration of any cut
  apparatus, and no verification of chat 3's claims about Voxel Play 4's feature set.
  Concurrency note recorded by the same session acting as its own writer: while this leg
  ran, s-converge-verify-g-37a1-core-rows-cut-repair-check-001 committed 00df2e6e — step 3
  PASSED with zero findings and wrote §SIGNOFF into work/converge-g-37a1-core-rows.md. The
  state was re-read fresh before applying and this delta was rebased onto it; that leg's
  changes are preserved in full, and nothing in this analysis depended on the sections it
  touched.

state_changes: |
  Against fresh live/indie-game-development state:
  - set NOW.md `updated` to `2026-07-28 by s-research-g-37a1-concept-extraction-001`;
  - close open_call `c-research-g-37a1-concept-extraction-001`: `status: ready` -> `done`,
    add `closed: 2026-07-28` and `result:
    history/2026-07-28-s-research-g-37a1-concept-extraction-001.md`, and prepend to its
    `note` what the leg returned — eight FORM seams, thirteen named contradictions, two
    confirmed false findings, the parked content index, the plugin inventory, and that no
    owner question was forced. Preserve the original note text below it;
  - upsert issue `i-core-form-seams-from-concept-001`, level `execution`, route `shape`,
    holding the eight FORM seams with their minimums, confidences and the honest weak
    points of F5 and F8, the preserve-versus-build split under the branch-2 verdict, the
    three mis-parked signed requirements, the C9 smoothing tension and the Voxel Play 4
    versus Core-owned-grid disagreement as shape inputs. This is the only place a shape leg
    will look, and the receipt carries the reasoning;
  - append one sentence to `d-core-geometry-and-view-001` naming the smoothing tension (C9)
    as raised by the concept material and NOT resolved, routed to shape with the backend;
    do not touch the ruling itself, the open half or the evidence list beyond adding this
    receipt;
  - prepend one driver to `direction_forecast.drivers` recording the extraction's answer
    and what it releases; leave `status: no_basis`, `target`, `as_of` and `update_when`
    unchanged;
  - prepend to `d-post-verify-route-001` `progress` that the extraction is COMPLETE and
    step 6 `shape` is the sole remaining frontier of his six-step route, with the FORM list
    as its input; no step added, nothing reordered;
  - preserve everything else exactly: the bet (null), tasks (empty), every other call's
    status including the cut-repair-check closed by the concurrent leg, all other issues
    and decisions, TREE.md and CHARTER.md untouched, the sixteen requirement lines, the
    fifteen criteria, work/converge-g-37a1-core-rows.md and
    work/concept-chats-answers-g-37a1.md untouched;
  - append the `log` line below once to LOG.md and save this complete RESULT as
    history/2026-07-28-s-research-g-37a1-concept-extraction-001.md.
  Maintain every END_OF_FILE trailer and preserve unrelated current edits.

captures:
  - "A paraphrased frame list manufactures contradictions: work/concept-extraction-request-g-37a1.md restated «Воздух — единственный ограничитель» (tighter than the signed §GLOSSARY «счётчик», where exclusivity is gone) and omitted the immortality switch, and both of chat 3's bad block-C items descend from exactly those two lines. A future outbound request quotes signed lines verbatim instead of restating them."
  - "The strongest open-source server-authoritative destructible-voxel reference found in the drop (qhdwight/voxelfield) is GPL-3.0 and therefore unusable as a source for a paid product; a second (jedjoud10/VoxelTerrain) states no licence at all. Worth knowing before anyone reads either while building the topology layer."
  - "Chat 3's block B mis-parked two signed first-core requirements (line 14's readable rock, line 9's wider-cut-stronger-flow) as next-version content. Any future extraction from an outside chat must walk the parking list against the signed set rather than trusting the chat's own classification."

decisions_needed: []

play_check: |
  research, four steps, all run. (1) RECITE — one question, asked and answered as one: what
  in the material changes the FORM. It was not split; the CONTENT list, the contradictions
  and the inventory are the CALL's own required return fields, not a second question.
  (2) INVESTIGATE — by the method the CALL names: analysis of the provided material against
  the named repository documents. Budget: one session, respected. (3) CONFIDENCE — every
  FORM item carries a mark; the two medium ones carry the counter-argument that would kill
  them, and F7's product-side claim is explicitly marked as resting on state rather than on
  a fresh inspection, because the CALL forbids the read that would settle it. (4) CLOSE —
  RESULT in the requested format; next = return-to-parent.
  CALL boundaries, each checked: NOT ONE of the sixteen requirement lines, fifteen criteria
  or closed rulings is reopened, amended or reinterpreted; no contradiction is resolved,
  merged or harmonised; every FORM item is a place something plugs into and not a feature,
  and two were downgraded in confidence rather than argued up; NO owner decision is
  manufactured and none is needed, so the leg proceeds rather than checkpointing under
  done_when 5; no bet, task, track, shape, TREE or card edit; no engine re-check and no
  product repository read; no estimate in days; d-air-counter-visibility-001 untouched; and
  NO element of the cut acceptance apparatus is restored — C6 names chat 1's playtest
  procedure precisely so that it stays parked.
  KERNEL gates: G1 unaffected (no bet, no task); G2 unaffected; G7 satisfied vacuously (no
  decision raised, none manufactured); G8 satisfied (everything new is parked); G9
  satisfied (CHARTER and TREE untouched); G10 satisfied (steps exposed, RESULT final, the
  leg wrote nothing until it became its own writer after this packet).
  done_when, one by one: (1) all 20 seam claims, all 109 content items, all 23 block-C items,
  both source texts and all three plugin lists are classed, with the accounting stated;
  (2) each of the eight FORM items carries seam, rewrite argument, minimum and confidence;
  (3) thirteen contradictions named with both texts quoted, none resolved; (4) the content
  list is parked and touches nothing — with the one exception stated loudly, that three of
  chat 3's parked items are signed requirements and are NOT parked; (5) the material was in
  the repository and no requirement-level question was forced, so no checkpoint.

log: "g-37a1/concept-extraction: the concept material DOES change the form — in eight places, and NOT ONE of them adds, removes or alters a rule of the game, which is why the answer needs no owner and unsigns nothing; twenty seam claims from three chats deduplicate to eight seams — per-cell substance keyed by a stable id rather than two named fields or a number on a pocket, one ordered tick-stamped topology contract with a single atomic commit, the core's own logical grid as the sole source of truth with mesh/collider/plugin behind a thin replaceable backend, a versioned section-based world-state format, the substance step as a named phase list with an EMPTY handler registry, typed facts out of the committed tick, an engine-free authoritative core with a one-way boundary to presentation and transport, and conductivity computed from an open-area query rather than a boolean neighbour test; THE FRAME THAT ORGANISES THEM IS HIS OWN BRANCH-2 VERDICT and it is half the finding — the engine stays and only the structure/topology layer is rewritten, so four of the eight are not new construction but a guard against the rewrite flattening what the product already banked (multi-kind cells, graded conductivity, the determinism-replication layer), while the other four are genuinely new because runtime closed-to-open mutation does not exist today and topology therefore enters the authoritative snapshot for the first time; ONE SEAM SURVIVES ON A DIFFERENT REASON THAN THE CHATS GAVE — they wanted typed tick events for future sound and light, which is content, but requirements line 9 already requires the breach to be an EVENT rather than a number quietly changing, so the seam has a signed consumer in the FIRST core; TWO ITEMS ARE MARKED MEDIUM WITH THEIR OWN KILL-ARGUMENT ATTACHED rather than argued up — the empty handler registry is the textbook speculative-generality trap and fails his «минимум с запасом, не максимум» if it costs more than naming the phases, and the area-valued conductivity query is an extension rather than a rewrite the moment the versioned format exists, so its whole claim rests on the solver's law; THIRTEEN CONTRADICTIONS ARE NAMED WITH BOTH TEXTS AND NONE IS RESOLVED, all of them parked content meeting a signed line — metabolism and reactions against criterion 13, clearing an impassable region against criterion 7, core extraction and value below against the ban on a goal at the bottom, cutting a drain against «стоков нет», backfilling against line 8, more kinds against «два вида», a dangerous autonomous front against «разница — цена воздуха», dialling pocket volume from the running rig against line 5, per-kind diffusion and a danger threshold, smoothing away cubicity against the very win his cubic ruling was admitted for, the co-op ordering tension between his own criterion 11 and his own line 16, and one nobody flagged — saving an unfinished section between launches against «между заходами ничего не копится»; THE SHARPEST OF THEM IS CHAT 1's OWN SOURCE TEXT, which contains a full playtest acceptance procedure of exactly the class he cut on 2026-07-28, named here so it stays parked and with not one deck, sample size or pass bar restored anywhere; BOTH INTAKE-FLAGGED FALSE FINDINGS ARE CONFIRMED FIRST-HAND (the immortality switch IS line 5 and criterion 12; «17 требований» is the file's own preserved numbering with line 7 struck in place) AND THEIR CAUSE IS OURS — the request's frame list is tighter than the signed set in two places, stating air as the ONLY limiter when the glossary records that exclusivity gone by his own softening, and omitting the immortality switch entirely; THE MOST DANGEROUS ITEM IN THE DROP IS NOT IN ANY BLOCK C — chat 3 parked THREE things as next-version content that are signed requirements of the FIRST core, and taking its list as given would have quietly deleted the readable rock (line 14) and the wider-cut-stronger-flow (line 9); the plugin inventory returns nothing new, chat 2 found no new plugin at all, chat 3 recommends buying Voxel Play 4 at $74.99 against our own record putting a narrow Core-owned grid ahead of it after his cubic ruling — a shape disagreement rather than a form one, and the thin-backend seam is exactly what makes settling it wrong cheap; NO OWNER QUESTION IS FORCED and none is manufactured, no requirement line, criterion or ruling moves, no bet/task/track/shape and no card or TREE edit, no product read, no engine re-check and no estimate in days. -> history/2026-07-28-s-research-g-37a1-concept-extraction-001.md"

next: |
  return-to-parent g-37a1 — step 6, `shape`, is now the sole remaining frontier of his
  six-step route. Its inputs: the eight FORM seams as constraints on HOW to build
  (`i-core-form-seams-from-concept-001`), his architectural co-op instruction already
  routed there, the open camera question, the backend choice (with the Voxel Play 4 versus
  Core-owned-grid disagreement and the Surface Nets tension both routed unresolved), the
  venue and rig prices, and the anti-`g-12fd` guard that only `shape` can set — `appetite`
  and `kill_by`. Its first task is the scene he asked for: a man digs a hole and walks
  into it.

END_OF_FILE: live/indie-game-development/history/2026-07-28-s-research-g-37a1-concept-extraction-001.md
