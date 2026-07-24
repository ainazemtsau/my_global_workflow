RESULT s-repair-demo-working-hypothesis-checkpoint-g10-001 (call: owner-plain-message-2026-07-24-demo-working-hypothesis-checkpoint)
direction: indie-game-development
track: canon
play: repair
node/task: g-d3a8/demo-working-hypothesis-checkpoint-g10-repair

outcome: |
  Восстановлен применимый и полностью самодостаточный checkpoint текущей
  owner-present работы над первой Steam-demo.

  Предыдущий пакет
  `s-research-demo-working-hypothesis-checkpoint-001`
  был отклонён writer'ом до любых изменений, поскольку его заголовок не
  содержал обязательную связь `(call: <call-id>)`.

  Никакой history-файл не был добавлен, LOG.md не менялся, commit не создавался.
  Настоящий RESULT полностью заменяет отклонённый пакет.

  Его input identity:

  `owner-plain-message-2026-07-24-demo-working-hypothesis-checkpoint`

  Это идентификатор leg, начатого обычным сообщением владельца по KERNEL §2
  OPEN. Это не зарегистрированный `NOW.open_calls` Canon-root, не новый
  design CALL и не разрешение на следующую работу. Настоящий RESULT не пытается
  очистить, заменить или переиспользовать какой-либо существующий call id.

  ======================================================================
  1. ЧТО ИМЕННО ЗАКРЫВАЕТ ЭТОТ CHECKPOINT
  ======================================================================

  Закрывается одна длинная исследовательская ветка, начавшаяся с поиска
  player-facing hook будущей demo и затем уточнившая:

  - incident-level моменты не являются взаимоисключающими hooks;
  - конкретные реакции, аварии Шаров, изменение маршрута и pressure events
    должны по возможности рождаться из симуляции, а не ставиться режиссёром;
  - прежде чем строить широкую demo-meta, необходимо доказать, что сама
    экспедиция является игрой, а не технической демонстрацией газа;
  - база, ремонт, progression, procedural breadth и послеглавная песочница
    могут обрамлять сильную экспедицию, но не способны спасти слабую;
  - при дефиците времени первая public demo потенциально может состоять
    преимущественно из одной сильной, воспроизводимой экспедиционной loop.

  Этот checkpoint сохраняет:

  1. текущую рабочую форму demo;
  2. её точный non-canon статус;
  3. сильные части, которые не следует потерять;
  4. элементы, которые остаются OPEN и могут быть полностью вырезаны;
  5. важные design separations;
  6. отдельную сохранённую гипотезу собранной формы газа;
  7. точный следующий bounded design question;
  8. достаточный контекст для продолжения в новой сессии без этого чата.

  ======================================================================
  2. OWNER VERDICT И ТЕКУЩИЙ СТАТУС
  ======================================================================

  Владелец согласился сохранить предложенную demo-форму только как рабочий
  вариант, требующий дальнейшей проработки.

  Точные owner statements, определяющие disposition:

  - «я согласен с твоей рекомендацией»;
  - «это мы еще будем прорабатывать»;
  - «сейчас уже важно начать прорабатывать, что будет самой экспедицией»;
  - «время поджимает»;
  - «в первую очередь надо определиться, что всё-таки в экспедиции,
    что мы принимаем, что нет»;
  - «теоретически мы на demo даже сможем выставить просто экспедицию,
    если там будет весело играть»;
  - «она не становится каноном»;
  - «Давай сохраним нашу работу»;
  - «дальше мы договорились более детально погружаться в саму экспедицию»;
  - «чтобы мы потом могли продолжить в новой сессии».

  Classification сохранённой demo-формы:

  - OWNER-SELECTED WORKING HYPOTHESIS;
  - PAPER-ONLY;
  - PROVISIONAL;
  - NON-CANON;
  - REVISABLE;
  - CUTTABLE;
  - NOT A DEMO CONTRACT;
  - NOT A DEMO EXPERIENCE TREE NODE;
  - NOT A PRODUCT REQUIREMENT;
  - NOT PLAN OR BUILD AUTHORITY.

  Никакое утверждение этого checkpoint не доказывает:

  - fun;
  - replay pull;
  - настоящую причинную кооперацию;
  - runtime legibility;
  - procedural quality;
  - техническую осуществимость;
  - networking или performance;
  - solo-production cost;
  - коммерческую привлекательность.

  ======================================================================
  3. PRODUCT И AUDIENCE НАПРАВЛЕНИЕ, КОТОРОЕ НЕЛЬЗЯ ПОТЕРЯТЬ
  ======================================================================

  Игра остаётся co-op-first экспедиционной игрой вокруг настоящей симуляции
  газа, Grid и изменяемого пространства.

  Владелец уточнил целевую домашнюю социальную группу:

  - примерно четыре пары, потенциально до восьми игроков;
  - сильно различающийся игровой опыт;
  - часть игроков любит сложные системные игры;
  - часть предпочитает более казуальные и спокойные игры.

  Поэтому базовая экспедиция не должна постоянно требовать высокой
  напряжённости, сложной процедуры или полного понимания системы.

  Рабочий social-play vector:

  `смотреть → сделать простое полезное действие → добровольно разогнать`

  Это означает:

  - событие должно быть интересно и понятно даже наблюдающему игроку;
  - менее опытный игрок должен иметь возможность повлиять одним простым
    действием;
  - опытные игроки могут сознательно усложнить, усилить или использовать ту
    же ситуацию;
  - высокий риск и mastery являются добровольным продолжением базового пути,
    а не обязательным onboarding;
  - роли возникают из занятых рук, позиции, инструмента, знания и ситуации,
    а не из меню постоянных классов.

  Этот audience vector является критерием будущей expedition work, но не
  отдельной принятой механикой.

  ======================================================================
  4. ТЕКУЩАЯ РАБОЧАЯ MACRO-ФОРМА DEMO
  ======================================================================

  Сохраняется следующий provisional envelope:

  `маленькая база / staging area
   → один ограниченный тип вариативного комплекса
   → одна или несколько экспедиций через настоящий gas gameplay
   → безопасно возвращённые meaningful outcomes потенциально двигают
      одну видимую цель
   → потенциально восстанавливается один базовый механизм
   → основная demo-глава может завершиться
   → потенциально открывается добровольный Experimental Mode
   → более глубокая часть игры остаётся будущим продолжением`.

  Это envelope, а не обязательный production scope.

  Вся обёртка может быть сокращена до одной сильной экспедиции, если:

  - экспедиционная loop сама вызывает желание немедленно повторить;
  - meta не добавляет достаточно player-facing value;
  - repair/profile systems начинают задерживать proof основной игры;
  - сроки или solo-production cost делают wrapper опасным;
  - один representative run уже честно показывает identity игры.

  Обёртка может быть расширена позднее, если playable evidence покажет, что
  сильной экспедиции не хватает:

  - понятной chapter goal;
  - payoff безопасного возврата;
  - послеглавного replay tail;
  - демонстрации того, что продукт глубже одной системной комнаты.

  ======================================================================
  5. ОДНА ENVIRONMENT / PLACE FAMILY
  ======================================================================

  Для первой demo не требуются:

  - три полноценных биома;
  - три разных procedural generator;
  - несколько map families;
  - широкая progression;
  - большой roguelike route graph.

  Рабочий минимальный envelope:

  - одна environment/place family;
  - один room kit;
  - небольшое число проверенных пространственных модулей;
  - меняющаяся компоновка;
  - меняющиеся пути входа и возврата;
  - меняющиеся позиции газовых карманов;
  - меняющиеся позиции active conditions;
  - конфигурации, в которых изменение расположения меняет решение игроков.

  Procedural generation не получает ценность автоматически.

  Она заслуживает scope только тогда, когда следующий заход заставляет иначе:

  - читать поле;
  - выбирать маршрут;
  - работать с газом;
  - использовать либо обходить active condition;
  - распределять временные роли;
  - решать, продолжать добычу или возвращаться.

  Переставленные коридоры без изменившихся решений не считаются replay value.

  Для первого proof допустим любой из трёх carriers:

  - ограниченный настоящий generator;
  - небольшой curated pool authored seeds;
  - модульная сборка из проверенных комнат.

  Игроку важна вариативность решений, а не архитектурная сложность генератора.

  ======================================================================
  6. ACTIVE CONDITIONS
  ======================================================================

  Active condition — физическая причина в пространстве, а не numeric affix,
  случайная карточка сложности или автоматически переносимый loot.

  Source examples, не выбранный roster:

  - radiation leak;
  - cold sink;
  - hot leak;
  - pressure source;
  - contaminated route;
  - draft shaft;
  - broken machine;
  - organics или другой физический материал;
  - иной world-cause, реально меняющий поведение газа или пространства.

  Active condition потенциально может влиять на:

  - газовое состояние;
  - ценность результата;
  - стабильность;
  - маршрут;
  - перенос;
  - безопасность игроков;
  - условия возврата.

  Если pre-entry read сообщает active condition, оно существует.

  Неизвестность допустима в деталях:

  - точный источник;
  - местоположение;
  - масштаб;
  - сила;
  - связь с газом;
  - можно ли использовать;
  - можно ли обойти;
  - какие дополнительные условия скрыты.

  Не принято:

  - exact condition roster;
  - exact effects;
  - exact detection method;
  - exact scanner/UI;
  - exact generation rules;
  - exact gas interactions.

  ======================================================================
  7. ИСТОРИЧЕСКИЙ SIMPLE GAS WORK LOOP — SOURCE, НЕ CURRENT LEDGER LAW
  ======================================================================

  Историческая owner-frozen design work описывала один floor через:

  `enter with floor read
   → progressive field contact
   → gas/value/condition/route work
   → stake/liability changes
   → greed/return/deeper decision
   → repeat or handoff`.

  Полезные положения source material:

  - команда входит с грубым, но реальным floor read;
  - понимание развивается во время движения, наблюдения, bounded actions и
    последствий;
  - active conditions являются world-causes, не numeric modifiers;
  - центр floor play — повторяемая работа с газом и ценностью, а не один pickup;
  - meaningful action меняет gas, cargo, route, condition, player coverage,
    readiness или return liability;
  - базовая жадность повторяется внутри floor;
  - решение «ещё или домой» рождается из состояния мира, не из popup/menu;
  - база готовит и обрабатывает, а живую ставку создаёт field;
  - paper не доказывает реальный fun.

  Однако старые question cards и maps не являются current Canon Decision
  Ledger или routing authority после Demo-Driven amendment.

  Поэтому будущая expedition session может использовать этот материал как
  source evidence, но обязана заново сверить каждое решение с:

  - current CONSTITUTION;
  - CORE;
  - INDEX;
  - c-001;
  - c-002;
  - c-003;
  - accepted Frames;
  - Demo Skeleton;
  - fresh owner words.

  Нельзя молча назвать весь historical floor-loop текущим canon.

  ======================================================================
  8. ВИДИМАЯ ЦЕЛЬ НА БАЗЕ
  ======================================================================

  Рабочая macro-форма допускает один заметный сломанный механизм на базе.

  Возможные функции:

  - дать demo-главе понятную конечную цель;
  - показать, что безопасный возврат имеет дальнейшее значение;
  - визуально отражать продвижение;
  - потенциально открыть послеглавный экспериментальный режим.

  Возможные образы, только placeholders:

  - broken experimental contour;
  - level-conditioning mechanism;
  - access installation;
  - calibration machine;
  - иной physically connected base system.

  Не принято:

  - что база или механизм обязательны;
  - что механизм обязательно чинится газом;
  - что ремонт является progression core;
  - сколько экспедиций требуется;
  - что является repair component;
  - нужен ли магазин;
  - нужна ли валюта;
  - нужен ли отдельный финальный уровень;
  - завершает ли ремонт demo-главу;
  - существует ли этот механизм в полной игре.

  ======================================================================
  9. REPAIR ECONOMY ОСТАЁТСЯ OPEN
  ======================================================================

  Рассматривались:

  - прямое заполнение механизма газовой массой;
  - продажа добычи и покупка деталей;
  - переработка результата на базе;
  - calibration milestones;
  - несколько meaningful returned outcomes.

  Ни один вариант не выбран.

  Рабочая граница:

  - не вводить широкую экономику только ради объяснения ремонта;
  - не добавлять магазин и цены раньше необходимости;
  - не превращать газ в generic money без player-facing причины;
  - не делать ремонт raw-volume progress bar;
  - не заставлять игроков повторять один безопасный farm route;
  - не решать repair economy раньше самой экспедиции.

  ======================================================================
  10. ТРИ DESIGN LAYERS ЯВНО РАЗДЕЛЕНЫ
  ======================================================================

  Зафиксировано важное разделение:

  1. physical extraction carrier —
     что игрок буквально выносит из field;

  2. banked expedition value —
     что сохраняется после безопасного возврата;

  3. future-floor conditioning input —
     чем потенциально изменяется следующая экспедиция.

  Эти слои не обязаны быть одним объектом.

  Поэтому снята обязательная цепочка:

  `вынести газ или сгусток
   → сохранить его
   → буквально вылить тот же объект обратно в следующий уровень`.

  Она была признана искусственной и сразу вызывала вопрос:

  «Зачем мы вообще его выносили, если теперь возвращаем обратно?»

  Не принято, что extraction carrier является:

  - газом в Шаре;
  - фазовым сгустком;
  - sample;
  - state-window;
  - иным cargo.

  Не принято, что banked value является:

  - деньгами;
  - запасом газа;
  - обработанным материалом;
  - исследованным состоянием;
  - технологическим доступом;
  - repair component.

  ======================================================================
  11. РАБОЧИЙ EXPERIMENTAL MODE
  ======================================================================

  Владелец согласился сохранить только как provisional working option:

  после завершения основной demo-главы игрокам потенциально открывается
  добровольный Experimental Mode, использующий тот же вариативный комплекс и
  уже реализованные systems.

  Текущий рабочий мост:

  `безопасно вернуть или доказать интересное состояние
   → база потенциально открывает reusable condition profile
   → после завершения главы игрок выбирает один profile
   → следующий run получает одно настоящее active condition`.

  Possible diegetic representations:

  - plate;
  - cassette;
  - module;
  - protocol;
  - иной интерфейс.

  Ничего из этого не выбрано.

  Profile не должен быть числовым affix.

  Он должен создавать реальную причину в пространстве:

  - физический источник;
  - область;
  - environmental state;
  - machine condition;
  - другой world-cause.

  Любой profile должен потенциально давать:

  - новую возможность;
  - liability или trade-off;
  - изменившееся решение игроков.

  Не принято:

  - что Experimental Mode входит в demo MUST;
  - что profiles вообще переживут expedition evidence;
  - как profiles открываются;
  - расходуются ли они;
  - бесплатны ли они;
  - постоянны ли они;
  - exact profile roster;
  - exact UI;
  - exact relation to repair;
  - exact full-game equivalent.

  Profiles могут быть полностью вырезаны.

  ======================================================================
  12. LITERAL GAS REINJECTION НЕ ЯВЛЯЕТСЯ ТЕКУЩЕЙ РЕКОМЕНДАЦИЕЙ
  ======================================================================

  Возможность вливать сохранённый газ обратно в будущий floor сохраняется
  только как отдельная future hypothesis.

  Она не используется сейчас как обязательное объяснение Experimental Mode.

  Причины:

  - extraction carrier ещё не выбран;
  - возможный сгусток плохо сочетается с буквальным глаголом «залить»;
  - возврат той же массы обратно требует отдельной цели;
  - иначе возникает лишняя conversion/economy layer;
  - gas infusion ради возможного артефакта является отдельным открытым вопросом;
  - тематическая симметрия не является достаточной причиной механики.

  ======================================================================
  13. СОБРАННАЯ ФИЗИЧЕСКАЯ ФОРМА ГАЗА
  ======================================================================

  Отдельная owner-preserved hypothesis сохранена в:

  `live/indie-game-development/history/
   2026-07-23-s-repair-gas-phase-condensate-preservation-packet-001.md`

  Её статус:

  - owner-preserved research hypothesis;
  - non-canon;
  - unparented;
  - not required for demo;
  - direct Sphere capture remains baseline;
  - all formation, movement, trail, decay, value, Sphere and implementation
    rules remain OPEN.

  Содержательное ядро:

  газ потенциально может иметь временную собранную физическую форму — отдельное
  видимое подвижное тело из той же газовой массы, способное выражать характер
  газа и создавать автономные события симуляции.

  Не принято:

  - как оно возникает;
  - движется ли самостоятельно;
  - оставляет ли газ;
  - распадается ли;
  - появляется ли в Шаре;
  - является ли добычей;
  - имеет ли ценность;
  - входит ли в demo;
  - нужно ли оно вообще.

  Следующая expedition work не должна автоматически включать сгусток.

  Он возвращается только если конкретная expedition problem требует:

  - autonomous gas activity;
  - concentration-as-opportunity;
  - consequence transfer между пространствами;
  - low-pressure `watch → touch → escalate`;
  - либо другого exact outcome, который cloud/Sphere/space дают хуже.

  ======================================================================
  14. ГЛАВНЫЙ ПРИОРИТЕТ СЛЕДУЮЩЕЙ СЕССИИ
  ======================================================================

  Следующая bounded-задача:

  `Определить одну конкретную экспедицию от pre-entry до safe return,
  partial disaster или wipe, которая без repair, profiles, progression и
  teaser показывает настоящую игру и создаёт желание сыграть ещё раз.`

  Нужно создать одну owner-readable playable sequence, а не:

  - набор абстрактных hooks;
  - каталог возможностей;
  - несколько взаимоисключающих incident cards;
  - технический roadmap;
  - full-game meta.

  Обязательные части будущей expedition work:

  1. PRE-ENTRY
     - что игроки знают;
     - чего хотят;
     - почему выбирают этот спуск;
     - какой грубый floor read получают.

  2. ENTRY
     - что видно сразу;
     - что понятно без объяснения архитектуры;
     - какое маленькое полезное действие доступно менее опытному игроку.

  3. FIRST GAME-STARTING ACTION
     - какое простое физическое действие запускает настоящую игру;
     - почему это не процедура, сканерный checklist или hold-to-progress.

  4. GAS / CONDITION / SPACE
     - один main gas/value opportunity;
     - одно active condition;
     - одно изменение маршрута или пространства;
     - видимая причинная связь.

  5. REPEATED WORK
     - что игроки повторяют;
     - как состояние после действия меняет следующую работу;
     - почему нет одной всегда правильной линии.

  6. CAUSAL CO-OP
     - как действие одного игрока меняет живую ситуацию другого;
     - почему второй игрок не декоративен;
     - почему это не two-key gate;
     - как casual-player полезен одним понятным действием.

  7. OPTIONAL ESCALATION
     - как базовый путь остаётся относительно ненапряжённым;
     - как игроки сами выбирают жадность, риск, эксперимент или chaos.

  8. GREED / RETURN
     - почему хочется взять ещё;
     - почему уже разумно уйти;
     - как выбор рождается из мира, не popup/menu.

  9. OUTCOMES
     - safe return;
     - partial success;
     - abandon/release;
     - rescue;
     - wipe или полный провал.

  10. REPLAY PULL
      - что в следующем запуске требует другой мысли;
      - почему это не только перестановка коридоров;
      - какое наблюдение опровергает replay pull.

  ======================================================================
  15. МИНИМАЛЬНЫЙ ENVELOPE СЛЕДУЮЩЕЙ EXPEDITION WORK
  ======================================================================

  Использовать:

  - one place/environment family;
  - one active condition;
  - one main gas/value opportunity;
  - one primary extraction/custody hypothesis;
  - one route that can materially change;
  - one causal co-op dependency;
  - one optional escalation;
  - one greed-versus-return moment;
  - one safe-return result;
  - one explicit falsification test.

  Не проектировать в этом bounded вопросе:

  - ремонтируемую машину;
  - repair economy;
  - condition profiles;
  - Experimental Mode;
  - progression;
  - магазин;
  - валюту;
  - артефактную систему;
  - несколько environment families;
  - broad generator architecture;
  - final gas roster;
  - reaction matrix;
  - full tool catalogue;
  - full damage/death/recovery model;
  - фазовый сгусток без exact need;
  - technical PLAN;
  - BUILD.

  ======================================================================
  16. INHERITED DESIGN BOUNDARIES
  ======================================================================

  Следующая expedition work обязана сохранять:

  - co-op-first направление;
  - full-game цель для меняющейся группы 4–8;
  - mixed-skill social group;
  - simple entry;
  - optional player-chosen escalation;
  - real gas simulation;
  - gas, Grid and spatial change as gameplay causes;
  - attributable consequences;
  - связь ценности и опасности;
  - failure changing the world where possible;
  - roles from hands/position/situation, not classes;
  - paper does not prove fun;
  - no silent creature-AI;
  - no mandatory engineering procedure;
  - no generic fragile-object extraction with gas as decoration;
  - one strong loop before several weak systems.

  ======================================================================
  17. CURRENT AUTHORITY И ROUTING
  ======================================================================

  Accepted Demo Contract по-прежнему отсутствует.

  Существующий Canon root:

  `c-cartography-g-d3a8-demo-experience-tree-pilot-001`

  остаётся:

  `WAITING on owner-approved-launch-control-demo-contract`.

  Настоящий checkpoint:

  - не очищает этот root;
  - не меняет его status;
  - не ретаргетит его;
  - не создаёт новый Canon root;
  - не регистрирует successor;
  - не создаёт Demo Contract;
  - не создаёт Demo Experience Tree;
  - не запускает prototype, PLAN или BUILD;
  - не выводит NEXT из capture или истории.

  Для будущей детальной expedition design потребуется:

  - новый exact owner override; либо
  - полный принятый Demo parent trace.

  В новой сессии владелец может написать обычными словами:

  `Продолжаем: одна экспедиция`.

  Новая сессия должна сначала прочитать:

  - fresh `NOW.md`;
  - этот checkpoint;
  - current Canon authority;
  - Demo Skeleton;
  - applicable Frames;
  - preserved condensate receipt только при реальной необходимости.

  ======================================================================
  18. КОРОТКОЕ OWNER-READABLE СОСТОЯНИЕ
  ======================================================================

  Рабочая demo потенциально выглядит так:

  Игроки начинают на небольшой базе и ходят в один ограниченный, вариативный
  комплекс. Там настоящие газ, пространство и active conditions создают
  решения, совместные действия, жадность и последствия возврата.

  Если одна экспедиция уже сильная, этого может хватить для первой demo.

  Если понадобится законченная маленькая глава, несколько результатов могут
  потенциально двигать один видимый механизм на базе.

  После прохождения главы может открыться добровольное экспериментирование с
  ранее обнаруженными физическими условиями в том же комплексе.

  Всё это рабочая и вырезаемая обёртка.

  Главная следующая работа — доказать саму экспедицию.

evidence: |
  PROTOCOL RECONSTRUCTION:

  - KERNEL §2 permits OPEN from either a CALL or a plain owner message.
  - Packet schema requires every RESULT header to include `(call: <call-id>)`.
  - Existing repository precedent uses synthetic input identities such as
    `owner-plain-message-2026-07-17` for owner-initiated legs that were not
    pre-registered in NOW.open_calls.
  - The previous packet omitted the call field completely.
  - Writer therefore rejected it before all writes.
  - Writer explicitly reported:
    history and LOG were unchanged and no commit was created.

  CURRENT PLAIN-MESSAGE IDENTITY:

  `owner-plain-message-2026-07-24-demo-working-hypothesis-checkpoint`

  This identity:
  - identifies the initiating owner conversation;
  - is not an ordinary Canon root;
  - does not claim registration in NOW.open_calls;
  - is not cleared from NOW by this RESULT;
  - creates no successor.

  OWNER EVIDENCE:

  - «я согласен с твоей рекомендацией»;
  - «это мы еще будем прорабатывать»;
  - «сейчас уже важно начать прорабатывать, что будет самой экспедицией»;
  - «время поджимает»;
  - «в первую очередь надо определиться, что всё-таки в экспедиции,
    что мы принимаем, что нет»;
  - «теоретически мы на demo даже сможем выставить просто экспедицию,
    если там будет весело играть»;
  - «она не становится каноном»;
  - «Давай сохраним нашу работу»;
  - «дальше мы договорились более детально погружаться в саму экспедицию»;
  - «чтобы мы потом могли продолжить в новой сессии».

  AUTHORITY POINTERS FOR FUTURE SESSION:

  Direction OS:
  - `os/KERNEL.md`
  - `os/schema/packets.md`
  - `live/indie-game-development/NOW.md`
  - `live/indie-game-development/plays/canon-forge.md`
  - `live/indie-game-development/work/demo-workflow/
    demo-driven-design-canon-workflow-v1.md`
  - `live/indie-game-development/work/launch-control/demo-control-room.md`

  Current Canon:
  - `CONSTITUTION.md`
  - `CORE.md`
  - `INDEX.md`
  - `QUEUE.md`
  - `SESSION.md`
  - `canon/c-001-investigation-readiness.md`
  - `canon/c-002-gas-behavior-jobs.md`
  - `canon/c-003-visual-development-contract.md`

  Accepted non-canon Frames:
  - `live/indie-game-development/work/minimum-game-frame-v2.md`
  - `live/indie-game-development/work/
    gas-sphere-extraction-custody-frame-v1.md`

  Preserved coherent-gas-phase hypothesis:
  - `live/indie-game-development/history/
    2026-07-23-s-repair-gas-phase-condensate-preservation-packet-001.md`

  Historical floor-loop source:
  - `live/indie-game-development/history/s-canon-floor-loop-002.md`
    — source evidence only under current Demo-Driven routing; not automatic
      current work or NEXT.

  CONFIDENCE:

  HIGH:
  - the demo wrapper is only a provisional non-canon working hypothesis;
  - the condition-profile route remains optional and open;
  - literal gas reinjection is not required;
  - physical carrier, banked value and conditioning input are independent;
  - expedition design is now the priority;
  - meta cannot certify or rescue weak expedition play;
  - the current Canon root remains WAITING;
  - no previous state change from the rejected packet exists.

  MEDIUM:
  - a small base, one visible repair goal and voluntary experiments may be a
    useful wrapper around a strong expedition;
  - discovered condition profiles may provide cheap replay after the chapter;
  - one environment family may be enough if variation changes decisions.

  OPEN / UNVERIFIED:
  - exact expedition sequence;
  - exact extraction form;
  - exact player verbs;
  - actual causal co-op;
  - replay pull;
  - procedural variation;
  - active-condition gameplay;
  - base necessity;
  - repair economy;
  - condition profiles;
  - Experimental Mode;
  - runtime legibility;
  - fun;
  - implementation feasibility;
  - production cost;
  - market response.

  EVIDENCE LIMIT:

  This RESULT repairs preservation and packet validity only.
  It admits no gameplay truth to canon and proves no experiential claim.

state_changes: |
  REJECTED PACKET DISPOSITION:

  - Do not apply the rejected packet
    `s-research-demo-working-hypothesis-checkpoint-001`.
  - It produced no history file, LOG entry or commit.
  - This repair RESULT is the sole transaction to apply for the checkpoint.

  `live/indie-game-development/history/`:

  - add only if absent:
    `2026-07-24-s-repair-demo-working-hypothesis-checkpoint-g10-001.md`
    containing this complete RESULT verbatim.

  `live/indie-game-development/LOG.md`:

  - before `END_OF_FILE`, append only if an equivalent session-id entry is
    absent:

    `2026-07-24 — repair (canon/g-d3a8,
    s-repair-demo-working-hypothesis-checkpoint-g10-001):
    repaired the rejected demo checkpoint by supplying its lawful
    plain-owner-message input identity and preserving a self-contained
    non-canon handoff: one strong expedition is the next priority; base repair,
    discovered condition profiles and Experimental Mode remain optional
    provisional wrappers; no Canon root, Contract, Tree, PLAN or BUILD changed.
    → history/2026-07-24-s-repair-demo-working-hypothesis-checkpoint-g10-001.md`

  `live/indie-game-development/NOW.md`:

  - no change;
  - preserve every fresh track, call, status, receipt and decision;
  - preserve
    `c-cartography-g-d3a8-demo-experience-tree-pilot-001`
    as WAITING;
  - do not clear the synthetic plain-message input identity because it is not
    an open_calls row;
  - do not register a successor, decision, root or child.

  `live/indie-game-development/TREE.md`:
    - no change.

  `live/indie-game-development/CHARTER.md`:
    - no change.

  `live/indie-game-development/knowledge/`:
    - no change;
    - working demo hypotheses are not durable accepted facts.

  `live/indie-game-development/work/`:
    - no change.

  Canon repository:
    - no change.

  Product repository and all foreign tracks:
    - no change.

  `os/FRICTION.md`:
    - no change; this was an authored packet omission, not yet a repeated OS
      defect.

captures:
  - >
    OWNER-SELECTED WORKING DEMO / NON-CANON:
    one strong expedition is the primary proof. A small base, one visible repair
    goal and a post-completion Experimental Mode using reusable discovered
    condition profiles remain optional provisional wrappers and may be cut after
    expedition evidence.

  - >
    NEXT BOUNDED DESIGN QUESTION:
    define one concrete expedition from pre-entry read to safe return, partial
    disaster or wipe, using one environment family, one active condition, one
    gas/value opportunity, one extraction/custody hypothesis, one changing
    route, one causal co-op dependency, one optional escalation and one
    greed-versus-return decision.

  - >
    HARD PRIORITY RULE:
    repair, profiles, progression, procedural breadth and cliffhanger may frame
    or extend a strong expedition, but may not be used to rescue weak
    minute-to-minute expedition play.

  - >
    SUBSTRATE SEPARATION:
    physical extraction carrier, banked expedition value and future-floor
    conditioning input remain independent design layers. Do not restore literal
    extract-and-reinject without a separate player-facing reason and evidence.

  - >
    CONDENSATE POINTER:
    the coherent gas-phase hypothesis is preserved separately and must not enter
    the first expedition automatically. Read
    `history/2026-07-23-s-repair-gas-phase-condensate-preservation-packet-001.md`
    only if the expedition needs autonomous gas activity,
    concentration-as-opportunity or cross-space consequence movement.

decisions_needed: []

play_check:
  - >
    1 Name the contradiction: done —
    the rejected checkpoint had complete content but no `(call: <call-id>)`
    header, while the writer correctly refused to invent an existing Canon call
    from NOW.

  - >
    2 Reconstruct: done —
    current KERNEL, packets schema, writer adapter, fresh NOW, historical
    owner-plain-message precedent, the rejected checkpoint content and the
    owner's preservation verdict were reconciled. No prior mutation existed.

  - >
    3 Propose corrected state: done —
    one repair history receipt plus one LOG pointer preserve the complete
    checkpoint; NOW, TREE, CHARTER, knowledge, Canon and product state remain
    unchanged.

  - >
    4 Confirm: done —
    the owner already explicitly approved this semantic transaction with
    «Давай сохраним нашу работу» and
    «чтобы мы потом могли продолжить в новой сессии».
    The repair changes no design substance; it only supplies the missing
    protocol identity and makes the approved preservation transaction valid.

  - >
    5 Friction: skipped —
    packet schema already required the missing call field and repository history
    already demonstrates the plain-message identity convention. This was the
    assistant's one-off omission. A repeated failure of this class should be
    recorded as OS friction.

log: >
  Repaired the rejected demo checkpoint with a lawful plain-owner-message input
  identity and preserved the full non-canon handoff; no active state or design
  authority changed.

next: |
  return-to-owner

END_OF_FILE: live/indie-game-development/history/2026-07-24-s-repair-demo-working-hypothesis-checkpoint-g10-001.md
