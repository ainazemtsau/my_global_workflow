# TREE — health

owner_approved: true
approval_evidence: >
  Owner accepted training/activity v0 launch in t-3 with "Запускаем"; this review verifies
  the bet as met and closes the node without adding a new TREE node.
  Owner approved a text-only cleanup for g-health-training-activity-system on 2026-06-28:
  "давай отправим запрос на очистку TREE". The cleanup replaces stale 8aa14f8/ACTIVE wording
  with the current 1fe41c2/PROGRAM-awaiting-research boundary; it does not restructure the node,
  reopen the bet, or claim body execution.
  Owner approved adding g-health-hq-goal-coordinator on 2026-06-30 in map close with:
  "Approve whole tree". The node is parked and creates no active bet or tasks.
  Owner approved activating the shaped Health HQ v0 bet on 2026-07-01 with:
  "approve recommended bet". This activates g-health-hq-goal-coordinator with a 5-calendar-day
  appetite, kill/review on 2026-07-06 end-of-day Europe/Amsterdam, and t-1 executor first.

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
  children:
    - id: g-health-starter-kit
      goal: >
        Стартовый комплект питания и тренировок выдан и пригоден к немедленному началу:
        owner может начать есть и тренироваться по первому рабочему варианту до завершения
        Health AI System.
      why: >
        Быстрый старт нужен, чтобы тело начало меняться сейчас, а питание и тренировки
        не ждали завершения AI/tracking-инфраструктуры.
      done_when:
        - Создан один стартовый артефакт, который можно выполнить без полной AI/tracking-системы:
          первый nutrition starter и первый training/activity starter.
        - Артефакт остаётся практическим, но не превращается в долгий "идеальный план":
          он покрывает ближайший стартовый период и даёт понятный способ сообщить, что не подошло.
        - В комплекте есть safety boundaries: боль, симптомы, перегруз, резкое падение сна/энергии
          или другие красные флаги не игнорируются.
        - В Direction OS не заносятся daily raw data: только итоговый summary, проблемы, решения
          и следующий CALL.
        - Starter kit спроектирован так, чтобы позже стать первым seed для nutrition system
          и training/activity system, а не одноразовой случайной выдачей.
      status: done
      appetite: 7 calendar days
      kill_by: >
        2026-06-19: if corrected starter kit v0 and compressed feedback path are not usable by then,
        stop and review instead of extending the bet.
      children: []

    - id: g-health-ai-core
      goal: >
        (DROPPED 2026-06-14 — superseded by g-health-core.) Первое ядро Health AI System, помечено
        done 2026-06-13, но оказалось недостаточно сильным/структурным для core-first видения владельца.
        Его артефакты (репозиторий health-ai, contract/skeleton v0) — грязный вход для converge
        g-health-core, не авторитет.
      why: >
        Заменено сильным провайдеро-независимым ядром (core-first re-frame); детали —
        history/2026-06-14-s-health-reframe-map-001.md.
      status: dropped
      children: []

    - id: g-health-core
      goal: >
        (DONE 2026-06-24 — current-head WA-K10 evidence repaired in health-ai
        8246cec19672bdd7eaadb2fec070a247088b6749; check_kernel_spine reports
        WA-K10 GREEN; WA-K6/WA-K8 breadth remains a named follow-on, not this
        closed kernel-spine bet.)
        (RE-OPENED 2026-06-20 — owner chose Variant 1. The delivered core nailed the DATA/CONTRACT
        layer but missed the RUNTIME layer the architecture needs: per-domain memory/working-state,
        a state-machine object, a single procedure-interpreter/router (each "term" = one bounded
        procedure the kernel runs), and a governance lifecycle (artifact SEED→PROPOSED→ACTIVE→
        SUPERSEDED + owner-approval gate + confirm-before-save + readable-for-owner + writer/
        evidence barrier + one-chat-one-job). Because the core shipped no runtime, the nutrition
        module reinvented its own workflow engine without a governance gate and was rejected;
        training would reinvent it again. The core is being EXTENDED into a kernel — the data/
        contract layer stays; nutrition/training become thin one-responsibility-per-procedure
        layers; the governance design from the nutrition converge moves into the kernel
        (work/core-kernel-governance-lifecycle-spec.md). Re-shaped into a bet at the kernel converge.)
        Сильное ядро Health AI System создано как провайдеро-независимая файловая система
        (Markdown/YAML в git): держит здоровье-состояние, программы-как-план, ежедневный трекинг и
        общий слой метрик/фаз/ревью; принимает ввод обычным текстом/голосом/фото; управляется любым
        LLM (ChatGPT, Claude, Claude Code, Codex) без проприетарной памяти.
      why: >
        Без сильного структурного ядра модули питания/тренировок повторяют v1-ошибку и расходятся;
        ядро задаёт типизированную структуру и механику, на которую модули просто навешиваются, и
        ведёт к root через надёжный рабочий слой для всего процесса.
      done_when:
        - Состояние хранится в человекочитаемых Markdown/YAML файлах в git; нет runtime/БД/сервера;
          владелец не редактирует файлы вручную — это делает LLM.
        - Провайдеро-независимость: одни и те же файлы и конвенции работают идентично в ChatGPT, Claude,
          Claude Code и Codex; конвенции живут в AGENTS.md, в CLAUDE.md (ссылается на AGENTS.md) и в
          переносимом system-prompt для вставки в project instructions; без зависимости от памяти/инструментов
          конкретного провайдера; числа в файлах, арифметика в задокументированных формулах.
        - Типизированная граница «факты владельца vs системно-решаемые переменные» (якорный профиль) и
          принцип research-and-decide: система решает экспертное, спрашивает только неустранимые личные факты.
        - Программа-как-план: можно определить программу и фазы и идти по ней день за днём; дневные
          предписания — производные от якорей, не захардкоженные.
        - Ядро владеет общими концептами (модули потребляют, не дублируют): метрики (вес+тренд,
          самочувствие, adherence), фаза, раздельные PLAN vs LOG, ревью-механизм (каденцию задаёт программа).
        - Ежедневный трекинг через текст/голос/фото: ввод парсится в структурированную запись со сверкой
          по активной программе/библиотеке; уточняющий вопрос только при существенной двусмысленности;
          числа берутся из файлов, не выдумываются.
        - Само-расширяемость: определён механизм добавления новых глобальных процедур/функций через
          workflow (не только новых доменов); новый домен = 1 папка + 1 строка реестра.
        - Модули (питание, тренировки) навешиваются на ядро без его переписывания и обмениваются данными
          (общие метрики, фаза) по определённому контракту.
        - Граница Direction OS сохранена: вверх идут только summary/decision/problem/CALL; сырые
          ежедневные данные живут в Health AI System.
      status: done
      appetite: >
        14 calendar days (kill 2026-07-04), servant-boxed. The OUTCOME worth this box is the kernel's BINDING
        PRECONDITION green — the runtime primitives + the lifecycle/gate/writer-barrier/cold-start spine + ONE
        real artifact walked SEED→PROPOSED→ACTIVE through the gate, proven by a fresh session (WA-K10 +
        KC5/KC6/KC7/KC14) — NOT the full breadth. The kernel is built by LIFTING the proven hand-rolled
        nutrition trio (router/graph/cursor) up into core/ + building the net-new governance spine
        (EXTRACT-AND-CANONIZE). Honest sizing is MULTI-LEG (one desk pre-proof + ≥2 executor legs), not half a
        day — the weaker predecessor data layer took ~6 days. Breadth (WA-K6 render-pair + WA-K8 anti-fragility
        strongest form) is a named follow-on bet, not this box. No extend (G3): over-box → re-shape.
      kill_by: >
        2026-07-04. Dies if ANY: (a) the Wave-0 zero-engine subtraction-proof surfaces a real non-empty engine
        residual a thin domain cannot shed (WA-K9 unmeetable as architected → do NOT build, re-open the arch
        claim); (b) the WA-K10 journey-proof + KC5/KC6/KC7/KC14 cannot be walked cold (KQ2 bootstrap recursion
        fails) under a fresh-session refutation; (c) PROCRASTINATION GUARD — by 2026-07-04 kernel commits exist
        but ZERO measurable body-execution (none of: ≥1 committed weight log, ≥1 owner-confirmed real
        menu/grocery used, ≥1 logged training/activity session) → per CHARTER pre_mortem risk #4, CUT the
        product part, force a near-path to real питание/активность before resuming.
        next_if_true (precondition green by date): the HARD precondition is cleared — nutrition (already live,
        re-homed thin) re-enters TRIAGE toward ACTIVE to earn the engine's keep; the breadth follow-on bet
        (WA-K6/WA-K8) opens. next_if_false: bounce/cut per the failing branch; no breadth leg proceeds on an
        unproven spine.
      children: []

    - id: g-health-nutrition-system
      goal: >
        (PARTIAL CURRENT PROGRESS 2026-06-24 — nutrition is now a thin Health AI
        domain on the closed g-health-core kernel with an ACTIVE program, ACTIVE
        cycle, ACTIVE week plan, ACTIVE fixed menu, ACTIVE recipe book, and
        cursor DAY_LOOP / selected family x_nutrition_day_log. The node remains
        parked because the next large bet is training/activity; minor nutrition
        papercuts ride r-health-ai-minor-fix-lane.) Питание внедрено в Health AI
        System КАК МОДУЛЬ НА ЯДРЕ g-health-core: меню, рецепты, grocery/meal-prep решения,
        fallback-еда, nutrition reviews и регулярные research-процессы работают на ядровых
        программах/трекинге/метриках/фазах (не дублируя их) из единого source-of-truth, но
        могут переноситься в удобные специализированные приложения.
      why: >
        Nutrition system нужна, чтобы питание стало производящей системой меню, рецептов
        и корректировок, а не разовой диетой или дневником в Direction OS.
      done_when:
        - Есть nutrition source-of-truth: где хранятся базовые правила питания, меню, рецепты,
          списки продуктов, meal-prep шаблоны, fallback варианты и ограничения.
        - Система умеет выдавать практические outputs: меню на неделю, варианты замены,
          список покупок, рецепты, "ленивую еду", план заготовок, корректировки после feedback.
        - Есть процедура nutrition review: owner может сообщить, что не подошло — вкус, голод,
          сложность готовки, цена, время, срывы, скука, социальные ситуации — и система превращает
          это в изменение артефактов.
        - Есть extension points для регулярных процессов: например, "каждый вторник найти новое блюдо",
          "обновить fallback meals", "подобрать рецепты под продукты дома", "адаптировать меню
          под неделю с низким временем".
        - Специализированные recipe/meal-planning приложения допустимы как интерфейс, но Direction OS
          не хранит daily food logs; в Direction OS возвращаются только summary, решения, проблемы
          и следующие CALL.
        - Питание встроено в body outcome: оно должно поддерживать снижение веса, достаточную сытость,
          белок, повторяемость и плохие недели, но не превращаться в crash diet или бесконечный research.
      status: parked
      children: []

    - id: g-health-first-nutrition-cycle
      goal: >
        (DROPPED 2026-06-20 — first-cycle execution bet rejected with the underlying Health AI
        nutrition slice.) Первые 8 дней питания реально выполнены через Health AI nutrition:
        owner стартовал по tomorrow-start packet, вёл Health AI-only nutrition LOG, прошёл
        day-3 safety/friction check и day-8 review, а Direction OS получил только
        summary/decision/problem без raw food diary.
      why: >
        Реальная body-value начинается не от внедрённого модуля, а от первого выдержанного цикла;
        этот узел тестирует adherence, logging, fallback и review loop до следующей системной стройки.
      done_when:
        - Owner начал питание по Health AI nutrition first cycle.
        - Day-3 safety/friction check выполнен и не выявил blocker red flags, либо включил conservative branch.
        - Day-8 first-cycle review выполнен в Health AI по LOG summaries, owner feedback and core metrics.
        - Direction OS не содержит raw daily food logs/photos/check-ins; только summary, decisions, problems, and next CALL.
      status: dropped
      children: []

    - id: g-health-training-activity-system
      goal: >
        (DONE 2026-06-27 at product/process review, with 2026-06-28 repair superseding launch-readiness semantics.
        Current authority is health-ai @1fe41c2: x_training_activity is PROGRAM awaiting Deep Research; no ACTIVE
        real training program, current week, today brief, or first real session is claimed until suitable returned
        research conclusion plus owner approval exist. Raw training/body execution data stay outside Direction OS.)
        Тренировки и активность внедрены в Health AI System КАК МОДУЛЬ НА ЯДРЕ g-health-core
        (с кросс-модульным обменом с питанием: белок/калории под объём, фаза/deload): силовая
        работа, conditioning, VR-активности, велосипед, gameful/competitive loops, safety gates и
        training reviews живут на ядровых программах/трекинге/метриках, а не в Direction OS-дневнике.
      why: >
        Training/activity system нужна, чтобы сила, атлетичность, conditioning и регулярная активность
        развивались через удобный рабочий контур, а не через ручное ведение тренировок в Direction OS.
      done_when:
        - Есть training/activity source-of-truth: где хранятся базовые правила, starter-программы,
          прогрессии, activity options, safety boundaries, review notes и решения по инструментам.
        - Система умеет выдавать практические outputs: первый тренировочный процесс, варианты для дома/зала,
          VR/велосипед/conditioning активности, корректировки под усталость, плохую неделю, боль,
          нехватку времени или мотивации.
        - Есть процедура training review: owner может сообщить, что не подошло — боль, скука,
          слишком легко/тяжело, неудобный формат, слабая мотивация, проблемы с техникой,
          VR/велосипед не зашёл — и система превращает это в изменение артефактов.
        - Силовая часть защищает body-composition outcome: baseline движений, прогрессия,
          восстановление и связка с питанием учитываются как отдельный контур, а не как случайное
          приложение к похудению.
        - Activity часть использует низкофрикционные и интересные источники: VR-игры,
          VR-boxing/fitness, велосипед, прогулки, gym conditioning, Strava-like/self-hosted механики,
          но без превращения соревнования в риск.
        - Специализированные приложения допустимы как интерфейсы: Hevy-like для силовых,
          Strava-like для велосипеда, VR/wearable summaries для активности. Direction OS получает
          только summary, проблемы, решения и следующие CALL, не raw logs.
      status: done
      appetite: 7 calendar days
      kill_by: >
        2026-07-03. Kill/review if by this date Health AI does not have an owner-approved
        thin-but-functional training/activity domain v0 that can produce an evidence-backed
        training program, current-week slice, today's session brief, normalized logging/import
        route, basic guided route, status/advice/substitution handling, basic review/handoff
        contour, and owner-operated acceptance without violating W1-W20, TA-CA1..TA-CA12,
        Direction OS raw-data boundary, D-kernel-1, or the setup/body evidence split.
      children: []

    - id: g-health-hq-goal-coordinator
      goal: >
        Health AI имеет верхний Health HQ v0: owner-facing goal-management и orchestration слой.
        Owner может обращаться к нему как к главному входу в Health AI: "что сегодня?",
        "разбери неделю", "проверь прогресс", "где bottleneck?", "добавить новый процесс?".
        Health HQ ведёт явную структуру целей, текущую фазу, phase metrics, domain responsibilities,
        review/decision log; проводит on-demand daily/weekly-style reviews; синхронизирует
        nutrition/training/activity/recovery; готовит routed correction requests в домены;
        задаёт минимальный domain integration contract для текущих и будущих доменов.
      why: >
        Root health goal требует не только отдельных nutrition/training процессов, а согласованного
        движения к весу, силе, атлетичному виду, энергии и maintenance. Health HQ нужен, чтобы домены
        не оптимизировали локально и не конфликтовали между собой.
      done_when:
        - Есть явная верхняя goal structure: root health goals, current phase, phase metrics,
          domain responsibilities, review/decision log.
        - Health HQ принимает owner-запросы типа "что сегодня?", "разбери неделю",
          "проверь прогресс", "где bottleneck?".
        - Есть минимальный domain integration contract для current/future domains:
          responsibility; supported goals; summary/report format для HQ; metrics/signals exposed
          to HQ; accepted correction/request types; boundaries: что HQ не меняет напрямую.
        - Nutrition и training/activity имеют хотя бы thin summary/report adapter для HQ;
          если real data ещё мало, proof использует clearly marked sample/test fixtures.
        - Health HQ проводит один dry-run или partial-real goal review across nutrition +
          training/activity + goal state.
        - Review выдаёт progress verdict, bottleneck/uncertainty, routed requests в домены,
          owner decisions если нужны, и какие метрики нужны сейчас/позже.
        - Health HQ не меняет domain artifacts silently: только маршрутизирует correction через
          domain procedures и owner/governance gates.
        - Direction OS получает только summary, decisions, problems, next CALL; raw body/nutrition/
          training data остаются вне Direction OS.
      status: active
      appetite: 5 calendar days
      kill_by: >
        2026-07-06 end-of-day Europe/Amsterdam. Kill/review if by this date Health AI cannot show
        evidence that Health HQ v0 holds explicit top-level goal structure, accepts one owner-triggered
        request, consumes nutrition and training/activity summary/report adapters or clearly marked
        fixtures, produces a progress verdict/bottleneck/routed correction requests/needed metrics,
        preserves the Direction OS raw-data boundary, does not silently edit domain artifacts, and does
        not add dashboard/API/polling/full architecture or out-of-scope domains.
      children: []

END_OF_FILE: live/health/TREE.md
