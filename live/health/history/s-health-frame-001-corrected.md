RESULT s-health-frame-001-corrected (call: owner-message-2026-06-12-health-create)
direction: health   play: frame   node/task: g-health-root/root-create

outcome: |
  Создан и утверждён фундамент нового направления health:
  CHARTER.md v0.2, TREE.md с единственным root node g-health-root,
  NOW.md с указанием на следующую research-сессию c-health-map-evidence-001.
  Направление сфокусировано на снижении веса с 125 кг до атлетичного диапазона около 90 кг,
  росте силовых, удержании результата без отката и создании Health AI System как отдельного
  рабочего слоя для AI-assisted трекинга, питания, тренировок, рецептов и продолжения в новых чатах.

evidence: |
  Fresh instruction check:
  - os/plays/frame.md current step 6 requires close.next = map_evidence research CALL
    unless the owner explicitly waives evidence. Owner did not waive evidence.
  Owner interview:
  - id/name: владелец согласился с рекомендацией health: "Хелпс, ну, в принципе, согласен с рекомендацией."
  - baseline: "35 лет, мужской пол, 182 см, 125 кг, похудеть до 90, травм нету, диагнозов нету, лекарств нету, ограничений нету."
  - why: "Особенно дисциплина, энергия, здоровье."
  - constraints: "Ограничений нету."
  - quality bar: "Вес ушёл без отката и силовые выросли. Выгляжу атлетично."
  - failure: "Снова набрал вес, мало активности."
  - edges: "есть ещё весы... пульсометр могу купить... Есть опыт спорта, есть опыт диет... если надо, то можно купить. С рекомендацией согласен."
  Charter approval:
  - owner approved charter v0.2 with exact response: "A"
  Pre-mortem approval:
  - owner approved pre-mortem v0.1 with exact response: "A"
  Root approval:
  - owner approved root v0.1 with exact response: "A"
  Correction instruction:
  - owner instructed: "да делай все строго по свежим и актуальным инструкциям"

state_changes: |
  Create file: live/health/CHARTER.md

  ---
  # CHARTER — health

  mission: |
    Создать устойчивую систему здоровья, веса, силы и энергии, в которой владелец
    снижает вес с 125 кг до атлетичного диапазона около 90 кг, повышает силовые
    показатели и удерживает результат без отката.

    Отдельный продукт направления — Health AI System: AI-ассистированная
    операционная система здоровья, которая помогает трекать процесс, давать
    апдейты, вести питание/тренировки/рецепты, использовать фото еды и сохранять
    рабочее состояние так, чтобы новые чаты могли продолжать процесс без потери
    контекста.

  outside_view: |
    Reference cases:
    1. DPP / клиническая lifestyle-программа: рабочий минимум — цель снижения
       веса около 7%, снижение калорийности/жиров и 150 минут активности в неделю.
       Для health это калибрует первый рубеж как доказательство системы на
       -8–12 кг, а не попытку сразу решить всю цель.
    2. NIDDK / безопасная программа похудения: реалистичный начальный ориентир —
       -5–10% стартового веса за 6 месяцев. Для 125 кг это примерно 112.5–118.75 кг.
    3. National Weight Control Registry / долгосрочное удержание: успешные maintainers
       часто сочетают высокую активность, самоконтроль веса и стабильные пищевые
       паттерны. Масштаб цели владельца близок к сильным outlier-cases, поэтому
       sequencing должен включать не только похудение, но и maintenance.
    4. CDC / устойчивый темп: постепенная потеря веса обычно лучше удерживается;
       для -35 кг практический горизонт следует считать 18–30 месяцев плюс минимум
       12 месяцев maintenance.
    5. WHO / активность как здоровье: физическая активность, силовая работа и
       снижение сидячего поведения важны не только для веса, но и для сердечно-
       сосудистого, метаболического и ментального здоровья.

    Implication:
    Направление нельзя строить как короткий жёсткий челлендж. Первый этап должен
    доказать повторяемую систему на 5–10% снижения веса, затем масштабировать её
    до -30–35 кг, одновременно защищая силовые, восстановление и maintenance.
    AI-система должна обслуживать эти исходы, а не становиться отдельной
    прокрастинационной стройкой.

  success_criteria:
    - id: sc-weight-maintenance
      criterion: |
        Средний вес находится в диапазоне 90–95 кг и удерживается 12 месяцев
        после выхода на него.
      calibration: |
        Calibrated against NWCR-style long-term maintainers: large weight loss
        is only successful when maintenance is proven, not when target weight is
        briefly touched.

    - id: sc-first-clinical-milestone
      criterion: |
        За первые 6 месяцев вес снижен минимум на 5–10% от стартового веса:
        с 125 кг до примерно 112.5–118.75 кг, без травм и без срыва активности.
      calibration: |
        Calibrated against NIDDK-style safe initial weight-loss targets.

    - id: sc-strength-and-athletic-look
      criterion: |
        К моменту выхода в диапазон 90–95 кг основные силовые показатели по
        согласованным движениям выше стартового baseline, а внешний вид субъективно
        соответствует "атлетично".
      calibration: |
        Calibrated against owner's quality bar: "силовые выросли" and
        "выгляжу атлетично".

    - id: sc-maintenance-system
      criterion: |
        В течение 12 месяцев maintenance есть повторяемые метрики и ритмы:
        вес минимум 1 раз в неделю, активность минимум 150–300 минут в неделю,
        силовая работа минимум 2 раза в неделю, питание готовится или планируется
        заранее в большинстве недель.
      calibration: |
        Calibrated against evidence-based maintenance patterns: activity,
        monitoring, strength work, and repeatable food structure.

    - id: sc-health-ai-system
      criterion: |
        Health AI System работает как операционная прослойка: отдельная система,
        вдохновлённая текущим workflow, но не засоряющая Direction OS ежедневными
        данными. Она хранит рабочее состояние, поддерживает продолжение в новых
        чатах, принимает апдейты по весу/еде/тренировкам, помогает с рецептами
        и планированием, а для специализированных задач использует лучшие
        инструменты, например Hevy для ведения силовых тренировок.
      calibration: |
        Calibrated against owner intent to use AI throughout the process while
        keeping Direction OS strategic rather than turning it into a raw diary.

  constraints:
    - |
      Медицинская безопасность выше темпа. При стартовой точке 35 лет, мужчина,
      182 см, 125 кг, BMI примерно 37.7. Давление, пульс, базовые анализы и
      врачебная проверка становятся hard constraint при симптомах, болях или
      необходимости эскалации нагрузок.
    - |
      "Жёсткие тренировки" не являются самоцелью. Самоцель — прогрессия, которую
      можно держать годами.
    - |
      Нельзя считать успехом быстрое снижение веса, если оно ломает сон, энергию,
      силовые, либидо, настроение, работу или приводит к травме.
    - |
      Оборудование — актив, не обязательство: VR, велосипед, гантели 24 кг, зал
      и техника для готовки должны снижать friction, а не создавать хаос выбора.
    - |
      Direction OS не становится дневником веса, калорий и сетов. Он хранит
      стратегическое состояние: решения, ставки, критерии, review, следующие CALL.
    - |
      Health AI System может иметь собственное состояние, файлы, репозиторий или
      формат данных; это будет спроектировано в отдельной ветке работы внутри
      направления.
    - |
      Специализированные приложения допустимы, если они снижают friction.
      Принцип: AI координирует систему, но не обязан быть интерфейсом для каждого
      микродействия.
    - |
      Быстрый старт по тренировкам и питанию нужен раньше полной архитектуры
      системы; полноценная система не должна блокировать начало движения.
    - |
      product_repos: []

  lenses:
    - id: weight-nutrition
      name: Weight & nutrition lens
      checks: |
        Энергетический дефицит, белок, насыщаемость, простота еды, заготовки.

    - id: strength-body-composition
      name: Strength & body composition lens
      checks: |
        Силовая прогрессия, сохранение/рост мышц, техника, восстановление.

    - id: activity-conditioning
      name: Activity & conditioning lens
      checks: |
        Велосипед, ходьба, VR, кардио-зона, NEAT, выносливость.

    - id: adherence-relapse
      name: Adherence & relapse lens
      checks: |
        Дисциплина, трекинг, срывы, отпуск/болезнь/стресс, возврат после пропусков.

    - id: medical-safety
      name: Medical safety lens
      checks: |
        Давление, пульс, сон, анализы, симптомы, травмопрофилактика.

    - id: ai-system-data-architecture
      name: AI system & data architecture lens
      checks: |
        Какие данные трекать, где они живут, как новые чаты получают контекст,
        какие задачи делает AI, какие задачи отдаём специализированным приложениям,
        как не превратить трекинг в бюрократию.

  owner_edges:
    - edge: Оборудование дома и доступ к залу.
      proving_fact: |
        У владельца есть VR, велосипед, гантели 24 кг, возможность ходить в зал.
    - edge: Пищевая инфраструктура.
      proving_fact: |
        У владельца есть техника для приготовления еды.
    - edge: Опыт спорта и диет.
      proving_fact: |
        Владелец прямо сообщил: "Есть опыт спорта, есть опыт диет."
    - edge: Готовность к измерениям.
      proving_fact: |
        Есть весы; владелец готов купить пульсометр/трекер, если надо.
    - edge: Низкие заявленные внешние ограничения.
      proving_fact: |
        Владелец сообщил: "Ограничений нету."
    - edge: Опыт работы с Direction OS и GitHub-state подходом.
      proving_fact: |
        Владелец хочет вдохновляться текущим workflow и хранить состояние так,
        чтобы новые AI-сессии могли продолжать работу.
    - edge: Готовность использовать AI как ежедневного оператора.
      proving_fact: |
        Владелец хочет давать апдейты, фото еды, трекать тренировки, придумывать
        рецепты и запускать research через AI.
    - edge: Готовность комбинировать AI со специализированными приложениями.
      proving_fact: |
        Владелец назвал Hevy как более удобный интерфейс для ведения тренировок,
        чем ручное ведение каждого подхода в ChatGPT.

  risk_posture:
    posture: guarded
    rationale: |
      Цель крупная, текущий BMI высокий, а запрос на жёсткие тренировки повышает
      риск перегруза. Guarded означает не мягкость, а дисциплинированную эскалацию
      через метрики, восстановление и удержание.

  pre_mortem:
    - risk: Вес ушёл, но вернулся.
      cause: |
        Система была построена на фазе "худею", но не на фазе "живу так всегда".
      mitigation: |
        Считать успехом не 90 кг на весах, а 90–95 кг плюс 12 месяцев удержания.
      kill_by_candidate: |
        Если после достижения промежуточного рубежа вес растёт 8 недель подряд
        без corrective action — ставка на текущий подход мертва, нужен review.

    - risk: Активность снова стала низкой.
      cause: |
        Тренировки воспринимались как проект, а не как базовая инфраструктура жизни.
      mitigation: |
        Минимальный протокол плохой недели: 2 силовые + 2 лёгкие активности или
        эквивалент, даже если питание/сон неидеальны.
      kill_by_candidate: |
        Если 3 недели подряд нет минимального протокола активности — система не
        удерживается, надо снижать friction.

    - risk: Жёсткие тренировки привели к перегрузу или травме.
      cause: |
        Нагрузка росла быстрее, чем восстановление, техника и суставы адаптировались.
      mitigation: |
        Guarded-подход: прогрессия через baseline, пульс/самочувствие, сон, боли,
        технику; "жёстко" = дисциплинированно, не хаотично.
      kill_by_candidate: |
        Любая боль, которая меняет движение или держится больше 7–10 дней,
        останавливает эскалацию нагрузки.

    - risk: Health AI System стала прокрастинацией вместо похудения.
      cause: |
        Система, GitHub-state, чаты, рецепты и автоматизации стали интереснее
        ежедневных действий.
      mitigation: |
        Быстрый старт не блокируется архитектурой; AI-система строится как servant
        layer, не как главный проект.
      kill_by_candidate: |
        Если 2 недели подряд есть работа над системой, но нет измеримого выполнения
        питания/активности — продуктовая часть урезается.

    - risk: Трекинг стал слишком тяжёлым, и владелец перестал им пользоваться.
      cause: |
        Слишком много метрик, ручного ввода и "надо отчитаться".
      mitigation: |
        Минимальный набор данных: вес, тренировки, базовая активность, питание в
        грубой форме; Hevy — для силовых, AI — для анализа и коррекции, не для
        ручного ввода каждого сета.
      kill_by_candidate: |
        Если трекинг пропущен 14 дней подряд — формат трекинга считается непригодным.

    - risk: Диета стала слишком жёсткой или скучной.
      cause: |
        Дефицит был технически эффективным, но психологически нежизнеспособным.
      mitigation: |
        Meal prep + рецепты + варианты "ленивой еды"; не запрещать всё, а строить
        повторяемые шаблоны.
      kill_by_candidate: |
        Если 2 крупных срыва за месяц повторяются 2 месяца подряд — пересобрать
        питание, а не "давить дисциплиной".

    - risk: Силовые выросли недостаточно или тело стало легче, но не атлетичнее.
      cause: |
        Похудение велось как потеря веса, а не как recomposition: мало силовой
        прогрессии, белка, восстановления.
      mitigation: |
        Baseline силовых, 2–4 силовые в неделю, прогрессия движений, контроль
        восстановления.
      kill_by_candidate: |
        Если вес падает, но силовые и самочувствие системно падают 6–8 недель —
        пересмотр дефицита/нагрузки.

    - risk: Отсутствие регулярного review.
      cause: |
        После первых недель система стала ехать на автопилоте и не замечала плато,
        откатов, усталости.
      mitigation: |
        Weekly check-in в Health AI System и стратегический review в Direction OS
        только по значимым рубежам.
      kill_by_candidate: |
        Если 4 недели нет review при стагнации веса/активности — направление
        считается без управления.

  END_OF_FILE: live/health/CHARTER.md

  ---

  Create file: live/health/TREE.md

  ---
  # TREE — health

  root:
    id: g-health-root
    goal: >
      Устойчивая система здоровья, веса, силы и энергии создана и работает:
      вес снижен с 125 кг до атлетичного диапазона около 90 кг, силовые показатели
      выросли, результат удерживается без отката, а Health AI System помогает вести
      процесс без засорения Direction OS ежедневными данными.
    why: >
      Это направление должно дать долгосрочную дисциплину, энергию, здоровье,
      атлетичный внешний вид и управляемую AI-поддержку всего процесса.
    done_when:
      - Средний вес находится в диапазоне 90–95 кг и удерживается 12 месяцев.
      - Основные силовые показатели по согласованным движениям выше стартового baseline.
      - Есть повторяемая система питания, активности, тренировок и review, выдерживающая плохие недели.
      - Health AI System работает как отдельный рабочий слой для апдейтов, трекинга, рецептов, еды, тренировок и продолжения в новых AI-сессиях.
    status: shaped
    children: []

  END_OF_FILE: live/health/TREE.md

  ---

  Create file: live/health/NOW.md

  ---
  # NOW — health

  active_bet: null

  tasks: []

  recurring: []

  open_calls:
    - id: c-health-map-evidence-001
      to: research
      direction: health
      play: research
      node: g-health-root
      goal: |
        Собрать evidence pack для будущей map-сессии направления health:
        какие дочерние outcome-узлы нужны под root, чтобы карта была grounded
        в доказательствах по крупному снижению веса, удержанию, силовым на дефиците,
        активности, relapse prevention и AI-assisted health system.
      context: |
        Read live/health/CHARTER.md and live/health/TREE.md after they are created.
        Owner baseline: 35 лет, мужчина, 182 см, 125 кг; цель — около 90 кг,
        без заявленных травм, диагнозов, лекарств и ограничений.
        Owner priorities: дисциплина, энергия, здоровье; качество — вес ушёл без
        отката, силовые выросли, внешний вид атлетичный.
        Owner failure fears: снова набрал вес, мало активности.
        Assets: VR, велосипед, гантели 24 кг, доступ к залу, техника для еды,
        весы, готовность купить пульсометр/трекер, опыт спорта и диет.
        Important architecture decision: Health AI System belongs inside health
        as a working layer, while Direction OS remains strategic and must not
        store daily raw weight/food/set data.
        Candidate outcomes captured by frame:
        - быстрый вводный план тренировок и питания, чтобы начать движение до полной архитектуры;
        - baseline здоровья, веса, силовых, активности и питания;
        - система снижения веса на первые 5–10% за 6 месяцев;
        - силовая система для сохранения/роста мышц и атлетичного вида;
        - система активности/кардио с использованием велосипеда, VR, ходьбы и зала;
        - repeatable meal-prep система и набор простых рецептов;
        - Health AI System architecture: state, data model, session protocol, фото еды, рецепты, апдейты, research;
        - Hevy или аналог как специализированный слой для силовых тренировок;
        - maintenance system на 12 месяцев после выхода в 90–95 кг;
        - medical safety / baseline checks / review gates.
      boundaries: |
        Не создавать TREE children и не выбирать первую ставку.
        Не делать детальный тренировочный или диетический план.
        Не записывать daily tracking data в Direction OS.
        Не отделять Health AI System в новое направление.
        Не заменять будущую map-сессию: результат research должен только подготовить evidence.
      done_when: |
        Evidence pack готов и покрывает:
        1. evidence-based sequencing for losing ~30–35 kg and maintaining it;
        2. strength training and muscle retention during caloric deficit;
        3. activity/cardio/NEAT requirements and relapse prevention;
        4. nutrition/meal-prep adherence patterns;
        5. safety checks for obese beginner/intermediate training escalation;
        6. practical AI-assisted tracking architecture patterns and tool-boundary principles;
        7. implications for child outcome nodes under g-health-root.
      return: |
        RESULT with concise evidence pack, source citations, recommended map implications,
        captures, and next = ready CALL c-health-map-001 for play: map carrying the evidence
        and candidate outcomes.
      budget: one deep-research-capable session
      surface: chatgpt

  decisions: []

  next: |
    CALL c-health-map-evidence-001
    to: research
    direction: health
    play: research
    node: g-health-root
    goal: |
      Собрать evidence pack для будущей map-сессии направления health.
    context: |
      live/health/CHARTER.md; live/health/TREE.md; candidate outcomes from frame
      are in open_calls.c-health-map-evidence-001.
    boundaries: |
      No TREE children, no tasks, no detailed plan, no daily tracking data in Direction OS.
    done_when: |
      Evidence pack ready for map and its RESULT chains to c-health-map-001.
    return: |
      RESULT with evidence pack and next CALL for map.
    budget: one deep-research-capable session
    surface: chatgpt

  END_OF_FILE: live/health/NOW.md

  ---

  Create file: live/health/LOG.md

  ---
  # LOG — health

  - 2026-06-12 — frame s-health-frame-001-corrected: создан и утверждён фундамент направления health; next = c-health-map-evidence-001.

  END_OF_FILE: live/health/LOG.md

  ---

  Create file: live/health/history/s-health-frame-001-corrected.md
  Content: this RESULT block verbatim.

captures:
  - "candidate outcome: быстрый вводный план тренировок и питания, чтобы владелец начал движение до полной архитектуры Health AI System."
  - "candidate outcome: baseline здоровья, веса, силовых, активности и питания."
  - "candidate outcome: система снижения веса на первые 5–10% за 6 месяцев."
  - "candidate outcome: силовая система для сохранения/роста мышц и атлетичного внешнего вида."
  - "candidate outcome: система активности и кардио с использованием велосипеда, VR, ходьбы и зала."
  - "candidate outcome: repeatable meal-prep система и набор простых рецептов."
  - "candidate outcome: Health AI System architecture — state, data model, session protocol, фото еды, рецепты, апдейты, research."
  - "candidate outcome: интеграция Hevy или аналога как специализированного слоя для силовых тренировок."
  - "candidate outcome: maintenance system на 12 месяцев после выхода в 90–95 кг."
  - "candidate outcome: medical safety / baseline checks / review gates."

decisions_needed: []

play_check:
  - "1 Interview (owner): done — owner provided baseline and intent: '35 лет, мужской пол, 182 см, 125 кг, похудеть до 90...'; priorities: 'Особенно дисциплина, энергия, здоровье'; quality: 'Вес ушёл без отката и силовые выросли. Выгляжу атлетично'; failure: 'Снова набрал вес, мало активности'; edges: equipment, scales, optional pульсометр/трекер, sport/diet experience."
  - "2 Homework (outside view): done — reference cases considered: DPP, NIDDK safe weight-loss guidance, NWCR long-term maintenance, CDC gradual loss, WHO physical activity; derived lenses, success criteria, owner edges, and guarded risk posture."
  - "3 Charter draft (owner): done — charter v0.2 shown and owner approved with exact response: 'A'."
  - "4 Pre-mortem (owner): done — pre-mortem v0.1 shown and owner approved with exact response: 'A'."
  - "5 Root node: done — root node g-health-root shown and owner approved with exact response: 'A'."
  - "6 Close (owner): done — RESULT includes owner_approved evidence for charter and root, exact state_changes, log line, and next = map_evidence research CALL; no owner evidence waiver was claimed."

log: |
  2026-06-12 — frame s-health-frame-001-corrected: создан и утверждён фундамент направления health; next = c-health-map-evidence-001.

next: |
  CALL c-health-map-evidence-001
  to: research
  direction: health
  play: research
  node: g-health-root
  goal: |
    Собрать evidence pack для будущей map-сессии направления health:
    какие дочерние outcome-узлы нужны под root, чтобы карта была grounded
    в доказательствах по крупному снижению веса, удержанию, силовым на дефиците,
    активности, relapse prevention и AI-assisted health system.
  context: |
    Read live/health/CHARTER.md and live/health/TREE.md after they are created.
    Owner baseline: 35 лет, мужчина, 182 см, 125 кг; цель — около 90 кг,
    без заявленных травм, диагнозов, лекарств и ограничений.
    Owner priorities: дисциплина, энергия, здоровье; качество — вес ушёл без
    отката, силовые выросли, внешний вид атлетичный.
    Owner failure fears: снова набрал вес, мало активности.
    Assets: VR, велосипед, гантели 24 кг, доступ к залу, техника для еды,
    весы, готовность купить пульсометр/трекер, опыт спорта и диет.
    Important architecture decision: Health AI System belongs inside health
    as a working layer, while Direction OS remains strategic and must not
    store daily raw weight/food/set data.
    Candidate outcomes captured by frame:
    - быстрый вводный план тренировок и питания, чтобы начать движение до полной архитектуры;
    - baseline здоровья, веса, силовых, активности и питания;
    - система снижения веса на первые 5–10% за 6 месяцев;
    - силовая система для сохранения/роста мышц и атлетичного вида;
    - система активности/кардио с использованием велосипеда, VR, ходьбы и зала;
    - repeatable meal-prep система и набор простых рецептов;
    - Health AI System architecture: state, data model, session protocol, фото еды, рецепты, апдейты, research;
    - Hevy или аналог как специализированный слой для силовых тренировок;
    - maintenance system на 12 месяцев после выхода в 90–95 кг;
    - medical safety / baseline checks / review gates.
  boundaries: |
    Не создавать TREE children и не выбирать первую ставку.
    Не делать детальный тренировочный или диетический план.
    Не записывать daily tracking data в Direction OS.
    Не отделять Health AI System в новое направление.
    Не заменять будущую map-сессию: результат research должен только подготовить evidence.
  done_when: |
    Evidence pack готов и покрывает:
    1. evidence-based sequencing for losing ~30–35 kg and maintaining it;
    2. strength training and muscle retention during caloric deficit;
    3. activity/cardio/NEAT requirements and relapse prevention;
    4. nutrition/meal-prep adherence patterns;
    5. safety checks for obese beginner/intermediate training escalation;
    6. practical AI-assisted tracking architecture patterns and tool-boundary principles;
    7. implications for child outcome nodes under g-health-root.
  return: |
    RESULT with concise evidence pack, source citations, recommended map implications,
    captures, and next = ready CALL c-health-map-001 for play: map carrying the evidence
    and candidate outcomes.
  budget: one deep-research-capable session
  surface: chatgpt