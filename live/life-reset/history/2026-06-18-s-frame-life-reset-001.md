RESULT s-frame-life-reset-001 (call: c-frame-life-reset-001)
direction: life-reset
play: frame
node/task: root

outcome: |
  Сформирована и явно утверждена основа нового направления life-reset:

  - утверждён CHARTER с миссией, критериями успеха, границами scope,
    operating model, lenses, owner edges, risk posture и pre-mortem;
  - утверждён единственный корневой TREE node без children и tasks;
  - root outcome установлен на создание и проверку Life-Reset Operating
    System к 20 июля 2026 года;
  - определено, что ядром являются Weekly Contract, Daily Execution,
    Weekly Review, управляемый backlog и lifecycle небольших процессов;
  - health остаётся source of truth по питанию, тренировкам, телу и
    health-метрикам;
  - game development остаётся source of truth по игре, production и
    соответствующим outcome/tasks;
  - life-reset координирует направления, но не дублирует их;
  - GitHub и другие repo-файлы в этой сессии не изменялись.

evidence: |
  Owner approvals in this session:

  - Charter framing / skeptical co-creation:
    owner verdict: "A".
  - Pre-mortem skeptical co-creation revision:
    owner verdict: "A".
  - Operating model v6 with Weekly Contract, standalone activities and backlog:
    owner verdict: "утвердить".
  - Pre-mortem v4:
    owner verdict: "A".
  - Final root:
    owner verdict: "A, утверждаю Root v5".

  Root deadline was explicitly corrected by the owner from a shorter horizon
  to: "давай возьмем с запасом 20 июля".

state_changes: |
  CREATE live/life-reset/CHARTER.md with exact content:

  ---
  # CHARTER — life-reset

  owner_approved:
    status: true
    evidence:
      - 'Owner approved charter direction: "A".'
      - 'Owner approved operating model v6: "утвердить".'
      - 'Owner approved pre-mortem v4: "A".'

  mission: |
    Создать и эксплуатировать личную операционную систему, через которую
    владелец раскрывает свой потенциал: эффективно проводит дни и недели,
    удерживает совместимость game development, health, семьи и самостоятельных
    активностей, замечает уход в хаос и постепенно улучшает способ жизни через
    небольшие критически проверенные процессы.

    Направление не ищет покой ради покоя. Оно должно поддерживать сильную жизнь
    с вызовом, дисциплиной, стоическим взглядом, живостью, внутренней честностью
    и трансцендентным смыслом — без превращения интенсивности в самоненависть,
    обжорство, курение, залипание, суету или многодневный откат.

    Life-reset принимает свободные сообщения владельца, но не исполняет их
    слепо. Система различает ценность, импульс, гипотезу, ограничение и принятое
    решение; критикует по существу и превращает идеи в ограниченные эксперименты,
    backlog-кандидаты, маршруты в другие directions либо осознанные отказы.

  outside_view: |
    Попытки построить личную систему обычно проваливаются одним из двух способов:
    либо возникает жёсткий краткосрочный режим с последующим откатом, либо
    создаётся сложная система рефлексии, трекинга и советов, которая сама
    становится прокрастинацией.

    Более устойчивый путь начинается не со списка привычек, а с операционного
    цикла: ограниченный недельный контракт, перевод его в реалистичные дневные
    действия, evidence-based review, обнаружение слабого звена и изменение
    только одного существенного элемента за раз.

    Внутренний референс — направление health: наличие отдельных артефактов без
    явного workflow graph для состояний, переходов, review и mutation оказалось
    недостаточным для owner-facing execution. Поэтому life-reset должен сначала
    получить целостный operating graph, а не набор отдельных prompts, практик,
    чатов или файлов.

    Внешние reference classes для следующего map_evidence:
    - behavior-change design: анализ поведения и механизма до назначения практики;
    - N-of-1 / small experiments: ограниченные проверки с baseline и stop rules;
    - adaptive interventions: интенсивность поддержки меняется по состоянию;
    - AI risk management: authority, context, measurement, review и routing;
    - personal informatics: собирать только данные, которые меняют решение.

    Sequencing implication:
    сначала исследуется и проектируется минимальный operating graph; затем map
    создаёт outcome nodes; после converge/shape запускается первый ограниченный
    pilot. Отдельный repo, постоянные чаты и автоматизация не выбираются заранее.

  success_criteria:
    - id: sc-weekly-operation
      criterion: |
        К 20 июля 2026 года проведено не менее трёх полных циклов:
        weekly planning → daily execution → weekly review.
        Для каждого цикла сохранены обязательства, фактический результат,
        drift-сигналы и принятое системное решение.
      calibration: |
        Проверяется работой в реальной жизни, а не наличием инструкции.

    - id: sc-protected-week
      criterion: |
        Weekly Contract отличает главные outcomes, самостоятельные activities,
        maintenance floors, максимум один новый improvement experiment и
        explicit cuts. Новые несрочные идеи не расширяют неделю автоматически.
      calibration: |
        Защищает от известного паттерна: сильная фиксация на одном направлении,
        выпадение опор и последующий общий спад.

    - id: sc-managed-extensions
      criterion: |
        Работает backlog небольших желаний, проектов, практик и process
        candidates. Элемент может быть selected, parked, promoted, dropped
        или done, не создавая автоматического морального долга.
      calibration: |
        Сохраняет небольшие идеи без отдельного direction для каждой из них.

    - id: sc-process-incubation
      criterion: |
        Система умеет провести подходящую идею через lifecycle:
        capture → clarify → challenge → research if needed → shape → pilot
        → review → adopt / mutate / kill.
      calibration: |
        Проверяет способность выращивать отдельные процессы, не предрешая,
        нужен ли им чат, workspace, приложение, repo или tree node.

    - id: sc-provider-portability
      criterion: |
        Новый чат или другой AI-провайдер может продолжить текущую работу из
        durable state без ручного пересказа всей истории.
      calibration: |
        Чат является интерфейсом, но не единственной памятью системы.

    - id: sc-owner-acceptance
      criterion: |
        После реального использования владелец явно подтверждает, что система
        помогает проводить недели и дни, сохраняет новые идеи без разрушения
        текущих обязательств, не захватывает scope соседних directions и не
        производит лишнюю бюрократию.
      calibration: |
        Owner acceptance после эксплуатации важнее полноты архитектуры на бумаге.

  operating_model:
    weekly_direction_cycle: |
      Управляющее ядро. В начале недели система собирает актуальные outcomes
      directions, доступную мощность, календарные ограничения, maintenance
      floors, standalone activities, backlog и evidence прошлой недели.

      Результат — Weekly Contract с:
      - главными progress outcomes;
      - выбранными standalone activities;
      - защищёнными maintenance floors;
      - максимум одним новым improvement experiment, если он обоснован;
      - explicit cuts.

      Добавление нового обязательства посреди недели требует назвать новый
      существенный факт, показать его приоритет и явно снять конкурирующий объём.

    daily_execution_loop: |
      Каждый день переводит Weekly Contract в реалистичный результат дня.
      Система помогает выбрать главное, защитить необходимые floors, заметить
      drift и перестроиться при существенном изменении.

      Интенсивность поддержки адаптивна:
      - стабильное состояние → короткое открытие/закрытие;
      - drift → более жёсткая структура;
      - срыв → recovery mode;
      - восстановление → снижение внешнего контроля.

      Daily loop не дублирует nutrition/training logs и game production state.

    weekly_review: |
      Review сверяет обязательства с evidence, разбирает причины расхождения,
      определяет текущее слабое звено и заканчивается решениями из множества:
      hold | mutate | kill | route | research | simplify.

      На review также разбираются captures, чистится backlog, выбираются либо
      откладываются standalone activities и решается, заслуживает ли candidate
      отдельного process, tree node или direction.

      Невыполненная цель не переносится автоматически.

    improvement_lab: |
      Вторичный механизм развития системы. Он исследует и проверяет не более
      одного нового improvement experiment одновременно.

      Кандидат должен быть связан с конкретной проблемой либо осознанной
      возможностью. Его minimal version, observable signal, cost, risk и stop
      condition определяются до постоянного внедрения.

    backlog: |
      Backlog хранит небольшие желания, activities, проекты, практики и process
      candidates, которые не требуют немедленного отдельного direction.

      Capture означает "не потерять", а не "обязательно выполнить".

      Минимальный lifecycle:
      inbox → candidate / parked / blocked → selected → done / dropped,
      с возможностью promoted в TREE или отдельный direction.

    process_extension: |
      Если candidate требует повторяемой работы, система сначала определяет
      outcome, scope, интерфейс владельца, durable state, cadence, связь с
      Weekly Contract, benefit signal, stop condition и promotion threshold.

      Отдельный чат, provider project, Markdown workspace, external tool или
      repo являются вариантами поверхности, а не обязательным решением.

  scope:
    in:
      - weekly planning, execution и review;
      - реалистичный план дня и восстановление после drift;
      - координация конфликтов между directions;
      - backlog небольших activities и желаний;
      - разработка ограниченных личных процессов и экспериментов;
      - обучение и перевод книг/идей в решения или практики;
      - spiritual artifacts: личная молитва, текст, песня, аудиоритуал;
      - inner-work и self-disclosure как аккуратно ограниченные процессы;
      - fatherhood/example как критерий качества жизни;
      - выбор подходящей operating surface для повторяемого процесса.

    out:
      - конкретные nutrition, weight, training и medical protocols;
      - game production roadmap и feature tasks;
      - клиническая диагностика или лечение;
      - Solmax/W0;
      - raw health diary внутри Direction OS;
      - отдельный direction, чат, repo или автоматизация без доказанной нужды;
      - grand abstract manifesto вместо проверяемого operating cycle.

  authority_and_boundaries:
    - |
      health является source of truth по питанию, тренировкам, весу, телу,
      health-метрикам и соответствующим протоколам.
    - |
      game development является source of truth по игре, production,
      game-specific outcomes и tasks.
    - |
      life-reset может читать согласованные summaries соседних directions,
      замечать конфликты и маршрутизировать вопросы, но не переписывает их scope.
    - |
      Owner input — высокоценный signal, но не final truth и не автоматическая
      команда к реализации.
    - |
      Research предоставляет evidence и варианты, но не принимает решение
      вместо владельца.
    - |
      При признаках клинического риска life-reset не усиливает дисциплину и не
      назначает лечение, а маршрутизирует к профессиональной поддержке.

  interaction_principles:
    - id: skeptical-co-creation
      principle: |
        Значимые идеи разделяются на underlying value, impulse, hypothesis,
        constraints и approved decision.
    - id: useful-criticism
      principle: |
        Критика используется только если обнаруживает противоречие, риск,
        вытесняемый приоритет, неподтверждённую гипотезу, более дешёвую проверку
        либо меняет решение.
    - id: guarded-intensity
      principle: |
        Система жёсткая к принятым обязательствам, скептичная к новым планам и
        нейтральная к сбоям. Сбой рассматривается как данные, а не identity.
    - id: one-change-at-a-time
      principle: |
        Новые процессы и практики не накапливаются одновременно; система
        предпочитает ограниченный test большому пакету улучшений.
    - id: no-silent-week-expansion
      principle: |
        Интересная несрочная идея по умолчанию сохраняется в backlog до review.
        Текущая неделя меняется только через явную замену обязательств.
    - id: chat-is-interface
      principle: |
        История одного чата не является долговременным state.

  lenses:
    - id: weekly-execution
      name: Weekly execution
      checks: |
        Реалистичность Weekly Contract, evidence результата, explicit cuts,
        перенос обязательств только после review.

    - id: daily-discipline
      name: Daily discipline
      checks: |
        Ясность главного действия, drift detection, recovery, отсутствие
        зависимости от постоянного разрешения AI.

    - id: cross-direction-integration
      name: Cross-direction integration
      checks: |
        Совместимость health, game development, семьи и standalone activities
        без дублирования state и захвата scope.

    - id: improvement-and-learning
      name: Improvement & learning
      checks: |
        Идеи, книги и практики переводятся в bounded experiments, решения,
        rejected ideas или backlog candidates.

    - id: spirit-and-transcendence
      name: Spirit & transcendence
      checks: |
        Личная молитва, текст, музыка, символы и ритуалы увеличивают живость и
        следующий реальный поступок, а не создают spiritual bypass.

    - id: inner-work-and-disclosure
      name: Inner work & disclosure
      checks: |
        Работа с саботажем, стыдом, insecurity, закрытыми эмоциями и
        самораскрытием имеет контейнер, ступенчатость и stop conditions.

    - id: fatherhood-and-example
      name: Fatherhood & example
      checks: |
        Система помогает становиться сильным, честным, присутствующим и живым
        примером для сына, а не только оптимизировать индивидуальную мощность.

    - id: system-quality
      name: System quality
      checks: |
        Workflow экономит внимание, переносим между провайдерами и не становится
        бюрократией или архитектурой ради архитектуры.

    - id: safety
      name: Safety
      checks: |
        Различает интенсивность и самоповреждение, inner work и
        дестабилизацию, self-reflection и clinical risk.

  owner_edges:
    - edge: Ресурсное окно для перестройки жизни.
      proving_fact: |
        Владелец сообщил, что сейчас располагает временем и ресурсами,
        направленными прежде всего на себя.

    - edge: Вызов является источником энергии.
      proving_fact: |
        Владелец прямо сказал, что не ищет покоя и хочет ежедневно преодолевать
        вызовы.

    - edge: Существующий Direction OS.
      proving_fact: |
        Владелец уже использует workflow с durable state, CALL/RESULT и
        owner-approved planning gates.

    - edge: Существующие health и game development directions.
      proving_fact: |
        Владелец обозначил их как отдельные важные направления и потребовал не
        дублировать питание, тренировки и game-production работу.

    - edge: Готовность к прямой критике.
      proving_fact: |
        Владелец явно потребовал рассматривать его идеи скептически, критиковать
        их по существу и не принимать текущую формулировку как истину.

    - edge: Символический и духовный запрос.
      proving_fact: |
        Владелец хочет создать собственные тексты, молитву, музыку и практики,
        которые дают сильный внутренний подъём.

    - edge: Fatherhood как моральный якорь.
      proving_fact: |
        Владелец назвал желание быть лучшим примером для сына.

  risk_posture:
    posture: guarded-intensity
    rationale: |
      Интенсивность и вызов являются центральными ценностями владельца, однако
      уже описан повторяющийся цикл: сильная фиксация → выпадение опор →
      обжорство/курение/залипание/хаос → снижение общей продуктивности.

      Guarded intensity означает не мягкость, а высокую требовательность с
      явными scope boundaries, evidence, stop conditions и review.

  pre_mortem:
    - risk: Weekly Contract становится списком пожеланий.
      mitigation: |
        Главные outcomes, floors, максимум один experiment и explicit cuts;
        новое обязательство требует снять другое.
      kill_by_candidate: |
        Две подряд перегруженные недели → обязательное уменьшение формата недели.

    - risk: Game development пожирает поддерживающие опоры.
      mitigation: |
        Life-reset защищает imported health floors, не назначая конкретные
        nutrition/training меры.
      kill_by_candidate: |
        План, систематически требующий нарушения floors, пересматривается.

    - risk: Daily operator становится внешней волей.
      mitigation: |
        Адаптивная интенсивность поддержки; при стабильности контроль уменьшается.
      kill_by_candidate: |
        Если процесс требует больше внимания, чем экономит, он упрощается.

    - risk: Weekly Review становится ритуалом без mutation.
      mitigation: |
        Review заканчивается hold, mutate, kill, route, research или simplify.
      kill_by_candidate: |
        Третье повторение одного failure pattern требует изменения системы.

    - risk: Backlog становится кладбищем желаний и источником вины.
      mitigation: |
        Capture не является обещанием; candidates выбираются, паркуются,
        повышаются или удаляются.
      kill_by_candidate: |
        Если backlog перестал помогать выбору, проводится жёсткая очистка.

    - risk: Improvement Lab конкурирует с основной жизнью.
      mitigation: |
        Одновременно не более одного нового experiment.
      kill_by_candidate: |
        Experiment без конкретной проблемы и observable signal не запускается.

    - risk: AI становится послушным зеркалом или спорщиком ради спора.
      mitigation: |
        Skeptical co-creation и критерий practically useful criticism.
      kill_by_candidate: |
        Значимое решение без challenge возвращается на пересмотр; критика,
        которая ничего не меняет, удаляется.

    - risk: State распадается между чатами, GitHub и провайдерами.
      mitigation: |
        Разделить strategic state, runtime state, specialized direction state
        и chat interface.
      kill_by_candidate: |
        Если новый provider не может продолжить из durable state, operating
        structure не считается завершённой.

    - risk: Духовные и inner-work практики становятся уходом от реальности.
      mitigation: |
        Проверять живость и следующий реальный поступок; использовать контейнер,
        минимальную форму и safety boundary.
      kill_by_candidate: |
        Уход от обязательств или признаки дестабилизации останавливают practice.

    - risk: Построена архитектура, но не проведена нормальная неделя.
      mitigation: |
        Архитектура создаётся только до уровня следующего реального pilot.
      kill_by_candidate: |
        Дальнейшая архитектура блокируется, если v0 не позволяет провести
        полноценный недельный цикл.

  product_repos: []

  END_OF_FILE: live/life-reset/CHARTER.md
  ---

  CREATE live/life-reset/TREE.md with exact content:

  ---
  # TREE — life-reset

  owner_approved:
    status: true
    evidence: 'Owner: "A, утверждаю Root v5"'

  root:
    id: g-life-reset-root
    status: shaped
    goal: |
      К 20 июля 2026 года life-reset работает как проверенная личная
      операционная система владельца: формирует реалистичные обязательства на
      неделю, переводит их в планы на день, удерживает совместимость game
      development, health и самостоятельных активностей, принимает возникающие
      идеи без разрушения текущей недели и умеет выращивать подходящие идеи в
      отдельные управляемые процессы.

    done_when: |
      1. Проведено не менее трёх полных циклов:
         weekly planning → daily execution → weekly review.

      2. Weekly Contract различает:
         - главные outcomes существующих directions;
         - выбранные standalone activities;
         - imported maintenance floors;
         - максимум один новый improvement experiment;
         - explicit cuts.

      3. Новая несрочная идея посреди недели по умолчанию попадает в backlog.
         Изменение недели требует назвать существенный новый факт, показать
         приоритет и явно снять конкурирующий объём.

      4. Работает backlog с исходами:
         selected | parked | promoted | dropped | done.
         Capture не создаёт обязательство выполнить идею.

      5. Система умеет провести подходящую идею через:
         capture → clarify → challenge → research if needed → shape → pilot
         → review → adopt / mutate / kill.

      6. Daily interaction служит Weekly Contract, помогает заметить drift и
         восстановиться, но не дублирует raw health logs и game-production state.

      7. Weekly Review использует evidence, определяет слабое звено и
         заканчивается решением:
         hold | mutate | kill | route | research | simplify.

      8. Значимые идеи владельца проходят содержательную критику, разделение
         value / impulse / hypothesis / constraints / decision и не исполняются
         автоматически.

      9. Durable state позволяет продолжить работу в новом чате или у другого
         AI-провайдера без ручного восстановления всей истории.

      10. Владелец после реального использования явно подтверждает, что система:
          - помогает проводить недели и дни;
          - сохраняет новые идеи без разрушения текущих обязательств;
          - умеет выращивать подходящие идеи в ограниченные процессы;
          - не создаёт отдельный direction или инфраструктуру для каждой мелочи;
          - не захватывает scope health и game development;
          - достаточно полезна и целостна для дальнейшего развития.

    children: []

  END_OF_FILE: live/life-reset/TREE.md
  ---

  CREATE live/life-reset/NOW.md with exact content:

  ---
  # NOW — life-reset

  active_bet:
    status: none
    note: |
      Direction framed. No active bet exists.
      Do not invent a daily loop, repo, permanent chat, practice or task before
      map_evidence, map and shape.

  tasks: []

  recurring: []

  open_calls: []

  decisions: []

  next: |
    CALL c-life-reset-map-evidence-001
    to: research
    direction: life-reset
    play: research
    node: g-life-reset-root
    goal: |
      Produce evidence for the first owner-co-created map of life-reset by
      identifying a minimal coherent operating architecture for weekly planning,
      daily execution, weekly review, managed backlog, small-process incubation
      and cross-direction coordination.
    context: |
      Read:
      - live/life-reset/CHARTER.md
      - live/life-reset/TREE.md
      - live/life-reset/NOW.md
      - os/KERNEL.md
      - os/plays/frame.md
      - os/plays/map.md
      - os/plays/converge.md
      - os/plays/converge-arch.md
      - os/plays/converge-verify.md
      - os/plays/shape.md
      - os/plays/research.md
      - live/health/CHARTER.md
      - live/health/NOW.md
      - live/health/work/converge-g-health-nutrition-workflow-graph.md
      - live/health/work/converge-g-health-nutrition-workflow-graph-arch.md
      - current CHARTER/TREE/NOW for the game-development direction after its
        canonical direction id is located.

      Owner intent:
      - Weekly Contract is the governing layer.
      - Daily planning and end-of-day review are required capabilities.
      - New non-critical ideas should normally enter a managed backlog rather
        than expand the active week.
      - Small activities such as English learning, reading, a personal prayer,
        music or another bounded process may be incubated without automatically
        becoming separate directions.
      - health owns nutrition/training/body data and protocols.
      - game development owns game production state.
      - life-reset coordinates and challenges; it does not duplicate.
      - Owner input is signal, not final truth.
      - The system must be direct and skeptical without criticizing for show.
      - Chat is an interface, not the sole durable memory.

      Investigate:
      1. Current best practices and failure modes for weekly planning,
         daily execution, weekly review and relapse/drift recovery.
      2. Behavior-change diagnosis before practice selection.
      3. Personal informatics: minimum useful data and burden control.
      4. N-of-1 and small-experiment design for personal practices.
      5. Adaptive-support models: when the AI should intervene more or less.
      6. Backlog and WIP mechanisms that preserve ideas without moral debt.
      7. Architectures for portable AI-assisted personal workflows:
         Direction OS only, provider chat/project, Markdown workspace,
         separate repo, external tools, or hybrids.
      8. Safe boundaries for inner work, self-disclosure and spiritual practice.
      9. Internal health workflow-graph lessons that transfer to life-reset.
      10. The strongest argument against building a separate runtime/repo now.

      Do not assume that the owner's examples are requirements.
      Critique the proposed framing and identify contradictions or missing
      components.
    boundaries: |
      Do not continue Solmax/W0.
      Do not prescribe nutrition, training, medical or psychiatric treatment.
      Do not create repo files or modify state.
      Do not select a permanent chat/provider/repo architecture prematurely.
      Do not design detailed morning/evening questionnaires yet.
      Do not choose the first active bet.
      Do not create TREE children; research informs the later map session.
    done_when: |
      Return a dated, source-cited research report containing:

      - 2–3 coherent alternative operating architectures;
      - for each: states, transitions, authority model, durable state,
        owner interface, health/game-development boundaries, advantages,
        failure modes, operational burden and what would falsify it;
      - a recommended minimum architecture with confidence and unresolved risks;
      - a candidate operating graph with explicit states and routing;
      - minimum information required for Weekly Contract, Daily Execution,
        Weekly Review and backlog without specifying unnecessary fields;
      - decision rules for chat vs Direction OS vs external tool vs separate repo;
      - process-incubation lifecycle for small activities;
      - strongest case against the recommendation;
      - 3–6 candidate top-level outcome nodes for the map session, clearly
        marked as research candidates rather than accepted TREE nodes;
      - recommendation for the riskiest node to examine first.

      Separate established evidence from inference and state what would change
      the recommendation.
    return: |
      RESULT with findings, dated sources, confidence/limits, map candidates,
      captures and next = a ready map CALL carrying the research result.
    budget: one deep-research-capable session

  END_OF_FILE: live/life-reset/NOW.md
  ---

  CREATE live/life-reset/LOG.md with exact content:

  ---
  # LOG — life-reset

  - 2026-06-18 — frame: owner approved CHARTER and root; direction framed around
    Weekly Contract, Daily Execution, Weekly Review, managed backlog and
    incubated small processes; next is map_evidence research.

  END_OF_FILE: live/life-reset/LOG.md
  ---

captures:
  - Candidate map path: Weekly Contract and capacity-aware commitment selection.
  - Candidate map path: Daily Execution with adaptive support and recovery mode.
  - Candidate map path: Weekly Review, weakest-link diagnosis and mutation.
  - Candidate map path: Managed backlog without moral debt or silent week expansion.
  - Candidate map path: Small-process incubation and extension registry.
  - Candidate map path: Durable portable runtime state independent of one chat/provider.
  - Candidate map path: Summary adapters for health and game development.
  - Candidate process: personal prayer, heavy-music artifact or audio ritual.
  - Candidate process: reading-to-practice integration.
  - Candidate process: English learning through games or another bounded format.
  - Candidate process: inner-parts / Jung / active-imagination research.
  - Candidate process: staged self-disclosure.
  - Candidate process: anti-chaos and drift-recovery mechanism.
  - Candidate architecture: separate workspace/repo only after a repeated stateful process proves the need.
  - Locate and confirm the canonical direction id and state paths for game development before map research consumes them.

decisions_needed: []

play_check:
  - '1 Interview: done — owner described the desired outcome as "Полностью раскрыть свой потенциал", requested challenge rather than comfort, named health and game development as adjacent directions, described chaos/overeating/smoking/gaming drift, spiritual/transcendent interests and fatherhood.'
  - '2 Homework: done — outside-view and internal workflow analogies were developed; the owner then required a deeper dedicated map_evidence research before architecture or practices are selected.'
  - '3 Charter draft: done — owner approved the direction framing with "A" and later approved operating model v6 with "утвердить".'
  - '4 Pre-mortem: done — owner approved the final operational pre-mortem with "A".'
  - '5 Root node: done — root contains no children or tasks; owner explicitly approved: "A, утверждаю Root v5".'
  - '6 Close: done — owner explicitly instructed: "Нужно прислать исправленный RESULT, где шаг 6 содержит фактическую фразу владельца или явный waiver." Approved CHARTER/root state changes, captures, log and ready map_evidence CALL are included; no repo writes were performed.'

log: |
  2026-06-18 frame c-frame-life-reset-001: life-reset charter and root approved;
  next is deep map_evidence research for the operating graph.

next: |
  CALL c-life-reset-map-evidence-001
  to: research
  direction: life-reset
  play: research
  node: g-life-reset-root
  goal: |
    Produce evidence for the first owner-co-created map of life-reset by
    identifying a minimal coherent operating architecture for weekly planning,
    daily execution, weekly review, managed backlog, small-process incubation
    and cross-direction coordination.
  context: |
    Read the approved life-reset CHARTER/TREE/NOW, Direction OS kernel and plays,
    the health workflow-graph evidence, and the canonical game-development
    direction state.

    Compare 2–3 coherent architectures for:
    - Weekly Contract;
    - Daily Execution;
    - Weekly Review;
    - drift/recovery;
    - backlog and WIP;
    - incubation of small personal processes;
    - portable durable state;
    - health/game-development adapters;
    - chat/workspace/repo/tool surface decisions.

    Critique the owner's examples rather than treating them as requirements.
  boundaries: |
    No Solmax/W0 work.
    No medical, psychiatric, nutrition or training prescription.
    No repo changes.
    No permanent provider/chat/repo decision.
    No first bet or TREE children.
  done_when: |
    A dated, source-cited report provides alternative architectures, a
    recommendation, explicit operating states/transitions, burden and risk
    analysis, falsification conditions, surface decision rules and 3–6
    candidate top-level outcomes for the later map session.
  return: |
    RESULT with findings, confidence, sources, candidates, captures and a ready
    map CALL.
  budget: one deep-research-capable session

END_OF_FILE: live/life-reset/history/2026-06-18-s-frame-life-reset-001.md
