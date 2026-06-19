# TREE — life-reset

owner_approved:
  status: true
  evidence:
    - 'Owner: "A, утверждаю Root v5"'
    - 'Owner approved top-level map: "approve whole tree"'

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

  children:
    - id: g-lr-weekly-operating-graph
      status: parked
      goal: |
        К 20 июля 2026 года life-reset умеет в активном разговоре
        строить неделю как operating graph: выбранные outcomes, slices
        длинных работ, floors, activities, backlog candidates,
        time/capacity budgets, success metrics и explicit cuts, затем
        фиксировать это как принятый Weekly Contract.
      done_when: |
        В каждом из трёх weekly cycles сохранён week graph + contract, где
        видно sources целей, success checks, time/capacity budget,
        selected slices, considered backlog candidates, reused past
        decisions/reviews, explicit cuts, owner acceptance и правило, что
        новая идея входит в текущую неделю только через critical need и
        снятие другого объёма.
      why: |
        Неделя должна строиться как честный граф целей, slices, capacity,
        metrics, backlog и cuts, а не список желаний.

    - id: g-lr-daily-runtime
      status: parked
      goal: |
        К 20 июля 2026 года life-reset умеет вести один рабочий чат дня:
        утром строить план под Weekly Contract и реальное расписание,
        в течение дня принимать сообщения о действиях, сбоях, мыслях и
        изменениях, перестраивать следующий ход и сохранять evidence для
        review.
      done_when: |
        В каждом из трёх weekly cycles есть daily runtime evidence:
        morning plan from Weekly Contract and schedule, in-day updates
        classified as action done / drift / blocker / idea intake /
        schedule change / review evidence, adaptive decisions
        continue / cut / recover / reschedule / push back, evening summary
        and a replaceable daily method reviewed after use.
      why: |
        Каждый день превращает Weekly Contract в расписание, действия,
        drift/recovery и evidence.

    - id: g-lr-direction-life-integration
      status: parked
      goal: |
        К 20 июля 2026 года life-reset умеет собирать в одну неделю
        summaries, floors, constraints и focus из других directions, семьи
        и самостоятельных activities, не забирая у них ownership.
      done_when: |
        В каждом из трёх weekly cycles видно imported game-development
        focus, imported health floors/constraints without life-reset
        prescribing nutrition/training/medical protocols, family
        commitments, standalone activities, conflicts found, and decisions
        cut / route / defer / ask / adjust without duplicating raw health
        logs, game-production tasks or long direction plans.
      why: |
        Большие цели остаются в directions, а life-reset собирает их в одну
        реальную неделю без захвата scope.

    - id: g-lr-intake-knowledge-memory
      status: parked
      goal: |
        К 20 июля 2026 года life-reset умеет принимать идеи, книги, статьи,
        наблюдения, желания, objections и process candidates; отделять
        важное от мусора; сохранять usable knowledge и decision memory в
        Markdown-first state; и возвращать это в week design, daily runtime,
        modules или reviews.
      done_when: |
        За три weekly cycles новые inputs не теряются и не попадают в работу
        автоматически; significant inputs получают решение drop /
        decision_memory / knowledge / backlog / incubate-research /
        module_candidate / current-week swap; rejected inputs carry a
        reason; knowledge notes are usable; long-running books/articles can
        be sliced across weeks; backlog enters week design as a shortlist.
      why: |
        Идеи, книги, статьи и решения сохраняются пригодно, а не становятся
        мусоркой или внезапными обязательствами.

    - id: g-lr-process-activity-modules
      status: parked
      goal: |
        К 20 июля 2026 года life-reset умеет запускать и вести ограниченные
        modules для процессов, activities и hobbies, которые ещё не являются
        отдельными directions: книга на месяц, танцы, велосипед,
        психологический разговор, духовная практика, learning workflow или
        новый life-reset protocol.
      done_when: |
        За три weekly cycles хотя бы один candidate может быть обработан как
        module или явно отложен с причиной, and the module pattern defines
        outcome, why it is not a direction yet, owner interface, durable
        state, weekly slice, daily runtime entry, progress/benefit signal,
        safety/scope boundaries, and review decisions continue / pause /
        mutate / kill / promote to direction / fold into routine.
      why: |
        Книги, танцы, велосипед, psychological/spiritual reflection и новые
        protocols можно вести как ограниченные modules без отдельного
        direction сразу.

    - id: g-lr-review-portable-evolution
      status: parked
      goal: |
        К 20 июля 2026 года life-reset умеет проводить Weekly Review,
        которое сравнивает Weekly Contract с evidence, обновляет knowledge
        and decision memory, принимает решения по directions, modules,
        backlog и daily/weekly protocols, а затем сохраняет portable
        Markdown/GitHub state так, чтобы следующий чат или AI-провайдер мог
        продолжить без старой истории.
      done_when: |
        В каждом из трёх weekly cycles review shows promised vs actual
        evidence, drift/overload/self-deception/external conflicts/failed
        protocols/useful surprises, lessons added to knowledge or decision
        memory, backlog/intake/module decisions, one weakest link, decisions
        hold / mutate / kill / route / research / simplify, next-week
        changes, portable continuation state and a clean-start reset check.
      why: |
        Review учит систему, меняет следующие недели/protocols/modules и
        сохраняет portable Markdown/GitHub state.

END_OF_FILE: live/life-reset/TREE.md
