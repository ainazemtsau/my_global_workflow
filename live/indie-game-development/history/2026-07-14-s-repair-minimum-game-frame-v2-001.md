RESULT s-repair-minimum-game-frame-v2-001 (call: c-repair-minimum-game-frame-v2-001)
direction: indie-game-development
play: repair
node/task: g-d3a8 / c-repair-minimum-game-frame-v2-001

outcome: |
  Minimum Game Frame v2 принят владельцем как текущая owner-approved
  whole-game design basis с дословным Gate F verdict:

  «FRAME READY»

  Рамка заменяет Minimum Game Frame v1 только на высоте whole-game frame.
  Она не является каноном и не изменяет существующий канон автоматически.

  Принятая рамка связывает:
  - player promise и локальную экспедицию;
  - короткий, трудный и конечный забег;
  - газ как регулярно добываемую ценность;
  - безопасное возвращение как границу силы текущего забега;
  - предсказуемые инструменты и артефакты-исключения;
  - полный вайп и быстрый meaningful restart;
  - Шар/Пузырь как principal extraction DESIGN ANCHOR;
  - меняющийся co-op состав 4–8 с обязательной поддержкой восьми;
  - эскалацию, частичный успех, retreat, failure и replay.

  Research draft не принят пакетом: его «семь законов», конкретные примеры,
  происхождение артефактов, заливка и прочие спорные формы разделены между
  OWNER DIRECTION, ARCHITECTURE HYPOTHESIS, OPEN и EXAMPLE.

  c-001 сохранён без расширения: карточка по-прежнему определяет только
  сознательный переход расследование → операция и не решает добычу,
  Пузырь, экономику, co-op composition, damage или progression.

  Никакого изменения canon, TREE.md, CHARTER.md, продукта или реализации
  в этой сессии не произошло.

evidence: |
  1. Verbatim owner Gate F verdict in this session:
     «FRAME READY»

  2. Proposed artifact accepted by that verdict:
     live/indie-game-development/work/minimum-game-frame-v2.md

     The final stored artifact is the accepted proposal with only mechanical
     post-verdict metadata changed:
     - status: FRAME READY
     - approved_on: 2026-07-14
     - owner_verdict: "FRAME READY"

  3. Required source-integrity gate:
     - parent RESULT:
       live/indie-game-development/history/
       2026-07-14-s-research-q-coop-interdependence-001.md
     - research source SHA-256:
       a831094069c59c4fccda53fe3ef788d0dd31f87f7f00c7d8531622f989d655fd
     - handoff SHA-256:
       f8384046e2aac713d71b499b0d4ae82065b8807d3fc61a19b0ea1f0dffd6c179
     - writer commit:
       4e1d7461eee10f1c163c0ca26c36e83e65594983
     - that commit installed both checksum-addressed artifacts and added
       .gitattributes entries with -text to preserve byte-for-byte checkout;
     - compare 4e1d7461eee10f1c163c0ca26c36e83e65594983...main
       does not list either required source as changed;
     - current research source ends with:
       END_OF_FILE: live/indie-game-development/work/
       ono-dyshit-gas-artifact-framework-research-draft-v1.md
     - current handoff ends with:
       END_OF_FILE: frame-v2-distillation-handoff-2026-07-14.md

  4. Done-when coverage in the accepted artifact:
     - player promise: section 1;
     - one expedition: section 2;
     - gas extraction and safe return: section 3;
     - tools versus artifacts: section 4;
     - one complete run, wipe and restart: section 5;
     - co-op form and supported group: section 6;
     - escalation, retreat, failure and replay: section 7;
     - remaining macro forks: section 8;
     - explicit non-scope: section 9;
     - classification of load-bearing statements: sections 1–10.

  5. Authority protection:
     - FOUNDATION / OWNER DIRECTION / DESIGN ANCHOR /
       ARCHITECTURE HYPOTHESIS / OPEN / EXAMPLE are explicit;
     - specific artifact, tool, node, recipe and UI examples have no design
       or canon authority;
     - c-001 is quoted only at its existing altitude and keeps its declared
       downstream non-scope.

  6. Evidence limits remain explicit:
     paper coherence does not prove fun, actual co-op, runtime legibility,
     production cost, technical feasibility of the complete product or
     market response.

state_changes: |
  1. Add exact artifact:

     path:
       live/indie-game-development/work/minimum-game-frame-v2.md

     postcondition:
       The file contains exactly the following accepted artifact and ends
       with its END_OF_FILE marker.

     artifact_content: |
       # Minimum Game Frame v2

       status: FRAME READY
       approved_on: 2026-07-14
       owner_verdict: "FRAME READY"
       authority: current owner-approved whole-game design basis; not canon
       supersedes_at_frame_altitude: minimum-game-frame-v1.md
       evidence_limit: paper-coherent only; fun, actual co-op, runtime
         legibility, production cost and market response remain UNVERIFIED

       ## Назначение

       Эта рамка коротко фиксирует, что представляет собой игра глобально
       и локально.

       Она не изменяет CHARTER, TREE или канон и не принимает
       исследовательский документ либо его «семь законов» пакетом.

       ## Статусы утверждений

       - FOUNDATION — действующее основание, не переоткрываемое этой рамкой.
       - OWNER DIRECTION — текущее решение владельца на высоте целой игры;
         оно получает authority рамки, но не становится каноном автоматически.
       - DESIGN ANCHOR — принципиальный игровой якорь, который нельзя молча
         потерять; его точное поведение остаётся изменяемым.
       - ARCHITECTURE HYPOTHESIS — связная рабочая форма, но не закон и не
         owner-selected механический ответ.
       - OPEN — реальная нерешённая развилка или измерение.
       - EXAMPLE — только иллюстрация; не получает design или canon authority.

       ## 1. Player promise

       [FOUNDATION]
       «ОНО ДЫШИТ» — co-op-first экспедиционная игра, в которой газ является
       общей физической средой: он движется, реагирует и взаимодействует с
       разрушаемым или изменяемым пространством. Игра должна давать понятные
       действия и сложные последствия, а не превращаться в демонстрацию
       симуляции или обязательную инженерную процедуру.

       [OWNER DIRECTION]
       Меняющаяся команда из 4–8 игроков входит в опасные пространства с
       неполным пониманием почти невидимого газа, расследует достаточно,
       чтобы выбрать ценную цель, добывает регулярную газовую ценность и
       пытается физически вернуть её через ситуацию, которую собственные
       действия уже могли изменить.

       Игроки постоянно сравнивают:
       - взять ещё или сохранить уже добытое;
       - идти глубже или защищать путь назад;
       - помогать людям и грузу или бросить часть ставки;
       - продолжать текущую экспедицию или сохранять весь забег.

       [DESIGN ANCHOR]
       Шар/Пузырь — главный видимый якорь добычи и физической эвакуации газа.
       Команда набирает выбранный объём; наполненный Шар ведёт себя в
       зависимости от газа внутри. Больший объём может естественно усиливать
       физическую сложность и ценность помощи других игроков.

       Точное наполнение, управление руками, вместимость, прочность, стадии,
       число помогающих и редкие альтернативы остаются OPEN. Открыта
       реализация якоря, а не его принципиальное место в игре.

       [OWNER DIRECTION]
       Газ — регулярная ценность экспедиций, подготовки и продвижения.
       Артефакты — желанные пики, редкие исключения и способы изменить
       отдельную экспедицию, текущий забег или новый старт. Экспедиция без
       артефакта должна оставаться полноценной игрой, а не обслуживающим
       фармом.

       ## 2. Одна экспедиция

       [ARCHITECTURE HYPOTHESIS]
       Текущая простая макроформа использует staging-зону и выбранную
       экспедицию или этаж. Точная география мира, устройство базы и способ
       выбора глубины не фиксируются этой рамкой.

       [OWNER DIRECTION]
       Одна экспедиция имеет размытый, перекрывающийся ход:

       `подготовка → выбор экспедиции → вход с неполной, но не ложной
       информацией → расследование → сознательный запуск операции или
       вынужденная импровизация → добыча и изменение ситуации → эвакуация,
       отступление или провал → безопасно возвращённый результат`

       Расследование, добыча и эвакуация не обязаны быть тремя изолированными
       актами. Добыча может продолжаться во время отхода; ошибка может
       изменить ситуацию до завершения расследования; маршрут назад
       уточняется и портится во время работы.

       [OWNER DIRECTION — c-001 PRESERVED]
       Сознательный переход от расследования к операции происходит, когда
       команда нашла цель, которая кажется достаточно ценной для первого
       серьёзного действия. Полная разведка, полный план уровня и
       гарантированный выход не требуются.

       Среда или ошибка могут лишить команду этого выбора раньше и заставить
       её импровизировать. Frame v2 не определяет точный источник, частоту
       или правила такого давления и не утверждает, что операция начинается
       только после нахождения цели.

       [FOUNDATION]
       Повторяемый локальный цикл:

       `понять достаточно → выбрать действие → изменить газ / пространство /
       ценность / маршрут → увидеть последствия → адаптировать план`

       Ошибка по возможности создаёт продолжающуюся ситуацию в мире, а не
       только экран наказания.

       [OPEN]
       Точные сигналы, детекторы, газовые состояния, критерии ценности цели,
       источники давления, инструменты и посекундные глаголы операции
       остаются отдельными вопросами.

       ## 3. Зачем добывать и безопасно возвращать газ

       [OWNER DIRECTION]
       Невозвращённый газ остаётся ставкой экспедиции. Только безопасное
       возвращение превращает добытый результат в устойчивую силу текущего
       забега.

       [OWNER DIRECTION]
       Регулярно возвращаемый газ должен расширять реальные возможности
       команды: давать подготовку, предсказуемые инструменты и некоторую
       форму продвижения или доступа к более серьёзному риску. Дорогой или
       трудный вывоз должен иметь заметное значение для забега.

       [FOUNDATION]
       В поле газ остаётся физической ценностью и опасностью, а не заменимым
       generic-жетоном. Его свойства должны влиять на добычу, перенос,
       маршрут или последствия.

       [OPEN]
       Не решены:
       - хранение, продажа или иная конвертация газа;
       - валюта, цены, спрос, квота или иной pressure-loop;
       - точный механизм доступа вниз;
       - почему почти пустой систематический возврат не становится оптимальным;
       - можно ли тратить сохранённый газ на изменение будущей экспедиции.

       ## 4. Предсказуемые инструменты и артефакты

       [OWNER DIRECTION]
       Инструмент — предсказуемая возможность: команда получает конкретную
       вещь ради известной функции. Обычная газовая ценность поддерживает
       подготовку такими инструментами. Точный каталог не фиксируется.

       Инструменты должны поддерживать сильные и понятные действия. Базовая
       игра не строится на восьми постоянных профессиях, длинных
       последовательностях обслуживания или обязательном микроконтроле
       параметров.

       [OWNER DIRECTION]
       Артефакт нельзя просто заказать как обычный инструмент. Это необычное,
       желанное исключение, способное сильнее изменить правила экспедиции,
       текущего забега или следующего старта.

       Артефакт не обязан присутствовать на каждой карте. Его задача — давать
       эмоциональный пик, эксперимент, общее решение и историю забега, а не
       равномерно заменять регулярную газовую игру.

       [ARCHITECTURE HYPOTHESIS]
       Происхождение через взаимодействие газа с физическим условием или
       узлом, а также добровольная заливка сохранённого газа в будущий этаж —
       сильные кандидаты на связывание газовой и артефактной игры. Ни одна из
       этих форм не является законом Frame v2.

       [OPEN]
       Остаются открыты происхождение, частота, tiers, каталог, сила,
       долговечность, потеря, ownership и возможное переживание вайпа.

       [EXAMPLE]
       Все конкретные артефакты, инструменты, узлы, рецепты, эффекты и схемы
       заливки из исследовательского источника остаются примерами без design
       или canon authority.

       ## 5. Один полный забег

       [OWNER DIRECTION]
       Забег короткий, трудный и конечный. У него есть достижимое завершение,
       а последние глубины должны быть очень сложными. Опытная группа
       потенциально проходит забег примерно за один вечер. Во время изучения
       игры серия экспедиций и поражений может растянуть один забег на
       несколько вечеров; 10–15 часов допустимы как хвост, но не являются
       целевой нормой.

       [ARCHITECTURE HYPOTHESIS]
       Рабочая макроформа:

       `быстрый старт с базовыми средствами → повторяющиеся экспедиции
       → безопасно возвращённый газ → инструменты / подготовка / доступ
       → более глубокие и опасные возможности → конечная цель или полный вайп`

       Точный порядок этажей, устройство staging-зоны и способ достижения
       финала остаются открытыми.

       [OWNER DIRECTION]
       Полный вайп завершает текущий забег и запускает новый. Обычная сила
       предыдущего забега не переносится автоматически.

       [OWNER DIRECTION]
       Новый старт должен быстро вернуть команду к настоящему решению.
       Базовые обязательные средства могут быть доступны сразу; группа не
       обязана повторять закупочный пролог или уже решённые chores.

       [OPEN]
       Не решены точная конечная цель, точный reset-state, гарантированная
       persistence, системная метапрогрессия и артефактные исключения из
       вайпа.

       ## 6. Кооперативная форма и состав группы

       [OWNER DIRECTION]
       Игра проектируется прежде всего для меняющейся группы 4–8 игроков.
       Поддержка полной группы из восьми — жёсткое требование. Если вчера
       играло восемь, а сегодня пришло пять, группа продолжает тот же забег.

       Точный нижний поддерживаемый предел ниже четырёх и правила
       масштабирования остаются OPEN. Соло не является текущей дизайн-целью.

       [ARCHITECTURE HYPOTHESIS]
       Для 4–8 игроков рабочая форма — не постоянная толпа у одного объекта,
       а несколько временных подгрупп. Игроки расходятся ради расследования,
       добычи, маршрута и других возможностей, затем собираются вокруг
       дорогой эвакуации, ухудшившегося пути, спасения или общей ставки.

       Роли возникают из текущей фазы, позиции, знания, инструмента и занятых
       рук, а не из постоянных классов. Общий газ, пространство, маршрут и
       состояние забега должны сохранять причинную связь между подгруппами.

       [OPEN]
       Не выбраны точная композиция временных ролей, обязательные формы
       взаимопомощи, anti-solo resistance, масштабирование по числу игроков,
       join/leave, ownership сохранения и техническая модель продолжения
       сессии.

       Frame v2 фиксирует источник кооперативного давления, но не утверждает,
       что реальная взаимозависимость уже доказана.

       ## 7. Эскалация, отступление, провал и replay

       [FOUNDATION]
       Действия игроков могут менять газ, реакции, пространство и маршрут.
       Ошибка должна быть по возможности атрибутируема и оставлять изменённое
       состояние мира: выпущенный газ, худший путь, потерянный груз,
       разделённую группу, необходимость спасения или вынужденное отступление.

       [OWNER DIRECTION]
       Эскалация усиливает живой вопрос:
       «берём ещё или сохраняем уже добытое?»

       Частичный успех допустим. Команда может вынести часть газа, потерять
       артефакт, бросить груз, спасти людей, отступить почти пустой или
       сохранить забег ценой отказа от большей награды.

       [OWNER DIRECTION]
       Безопасный возврат закрепляет результат экспедиции. Полный вайп
       закрывает забег. Точные последствия индивидуальной ошибки, падения
       или смерти OPEN.

       [ARCHITECTURE HYPOTHESIS]
       Replay поддерживают разные сочетания этажей, газов, физических условий,
       артефактов, состава группы и решений, а быстрый новый старт позволяет
       опытной группе раньше брать серьёзный риск.

       [OPEN]
       Точные damage, health, downed, rescue, death, recovery, procedural
       generation, difficulty scaling и replay variation не определены.

       ## 8. Реальные оставшиеся макроразвилки

       1. [OPEN] Какая экономика или система доступа превращает значимый
          вывоз газа в продвижение и не делает почти пустой возврат
          оптимальным?

       2. [OPEN] Как именно артефакты входят в игру и насколько часто
          формируют забег: находятся, создаются, возникают из газа и условий
          либо становятся результатом добровольного изменения будущего этажа?

       3. [OPEN] Как устроены глубина, staging-зона и конечная цель при
          сохранении короткого, трудного и конечного забега?

       4. [OPEN] Что именно теряется при полном вайпе, какие исключения
          допустимы и существует ли гарантированная системная метапрогрессия?

       5. [OPEN] Какая композиция временных подгрупп и ролей создаёт настоящую
          дополнительную ценность 4–8 игроков; где проходит нижний предел
          поддерживаемого состава?

       Не являются открытыми макроразвилками:
       - газ как регулярная ценность;
       - артефакты как исключения, а не обязательная награда каждого рейса;
       - полный вайп как завершение забега;
       - быстрый meaningful restart;
       - обязательная поддержка восьми игроков;
       - Шар/Пузырь как главный extraction DESIGN ANCHOR.

       ## 9. Explicit non-scope

       [OPEN]
       Frame v2 не решает:

       - конкретные артефакты, рецепты, узлы или способ происхождения;
       - конкретные инструменты;
       - валюты, цены, квоты, формулы ценности и progression numbers;
       - floor generation и точную структуру уровней;
       - детекторы, evidence, UI и onboarding;
       - Bubble filling, controls, capacity, durability, rupture и точное
         число рук;
       - gas roster, точные состояния и реакции;
       - damage, death, rescue и recovery;
       - save ownership, networking, late join, host migration и баланс
         составов;
       - balance, tuning, production scope или implementation.

       Эта рамка не доказывает fun, реальный co-op, runtime legibility,
       production cost, техническую осуществимость полного продукта или
       market response. Эти утверждения требуют отдельных бумажных гейтов
       и затем playable/external evidence.

       ## 10. Source/status matrix

       | ID | Load-bearing statement | Classification | Treatment |
       |---|---|---|---|
       | F1 | Газовая симуляция, реакции и изменяемое пространство | FOUNDATION | Сохранено без пересмотра |
       | F2 | Game-first, simple-not-primitive; провал меняет мир | FOUNDATION | Сохранено |
       | OD1 | Investigation → operation → evacuation и граница c-001 | OWNER DIRECTION | c-001 сохранён без расширения |
       | OD2 | Газ — регулярная ценность; безопасный возврат питает забег | OWNER DIRECTION | Exact economy OPEN |
       | OD3 | Инструменты предсказуемы; артефакты — желанные исключения | OWNER DIRECTION | Каталоги и частоты OPEN |
       | OD4 | Короткий трудный конечный забег; полный вайп; быстрый restart | OWNER DIRECTION | Exact endpoint/reset OPEN |
       | OD5 | Меняющийся состав 4–8; поддержка восьми обязательна | OWNER DIRECTION | TREE/canon reconciliation отдельно |
       | DA1 | Шар/Пузырь — главный extraction anchor | DESIGN ANCHOR | Exact behavior OPEN |
       | AH1 | Staging-зона + выбранные этажи + движение в глубину | ARCHITECTURE HYPOTHESIS | Не закон мира |
       | AH2 | Газ + физическое условие и заливка будущего этажа | ARCHITECTURE HYPOTHESIS | Не принято как происхождение артефактов |
       | AH3 | Временные подгруппы, ситуационные роли, общая причинность | ARCHITECTURE HYPOTHESIS | Возврат к co-op question после Frame |
       | X1 | Конкретные предметы, узлы, рецепты и эффекты | EXAMPLE | Authority отсутствует |

       END_OF_FILE: live/indie-game-development/work/minimum-game-frame-v2.md

  2. NOW.md — consume completed call:
     - if open_calls contains c-repair-minimum-game-frame-v2-001,
       remove it as completed with owner verdict FRAME READY.

  3. NOW.md — preserve current direction execution:
     - preserve the active engineering bet and all active task states;
     - preserve all unrelated open_calls and decisions;
     - preserve the current global engineering NOW.next unchanged;
     - preserve c-shape-sc-damage-001 as HELD because Frame readiness is
       not a ready canon co-op specification.

  4. NOW.md — register exact future CALL A:

     id: c-map-g-d3a8-frame-v2-reconciliation-001
     status: READY PARALLEL
     for: g-d3a8 / TREE and design-canon branch reconciliation
     note: |
       Owner-present G9 reconciliation of only g-d3a8 against accepted
       Minimum Game Frame v2 and the current eight-player requirement.
       No canon, CHARTER, product or implementation change.

     CALL c-map-g-d3a8-frame-v2-reconciliation-001
     to: session
     direction: indie-game-development
     play: map
     node: g-d3a8
     surface: any
     parent: s-repair-minimum-game-frame-v2-001

     goal: |
       The g-d3a8 design/canon branch of TREE accurately reflects accepted
       Minimum Game Frame v2, the current eight-player owner requirement and
       the actual separation between frame, paper answers and canon, without
       rewriting unrelated branches.

     context: |
       Read:
       - live/indie-game-development/NOW.md
       - live/indie-game-development/CHARTER.md
       - live/indie-game-development/TREE.md
       - live/indie-game-development/work/minimum-game-frame-v2.md
       - live/indie-game-development/knowledge/
         g9c41-players-8-owner-requirement.md
       - current gas_coop_game_canon CONSTITUTION.md, CORE.md, INDEX.md and
         canon/c-001-investigation-readiness.md
       - live/indie-game-development/history/
         2026-07-14-s-repair-minimum-game-frame-v2-001.md

       Minimum Game Frame v2 has owner verdict FRAME READY and is the current
       whole-game design basis, but is not canon.

       The current g-d3a8 TREE text still carries stale 1–4-player and
       solo-startable language. Current owner direction requires support for
       eight players and treats solo as outside the present design target.

       c-research-q-coop-interdependence-002 is issued separately but remains
       HELD until this reconciliation closes.

     boundaries: |
       Owner-present, text only.
       Touch only the g-d3a8 design/canon branch and necessary NOW routing.
       Do not change CHARTER, canon, product or implementation.
       Do not activate Gate Q, select a paper answer or generate mechanics.
       Do not rewrite unrelated TREE branches.

     done_when: |
       An exact g-d3a8 TREE/map correction exists and the owner explicitly
       approves it or blocks it.

       The corrected branch:
       - reflects Minimum Game Frame v2;
       - reflects the current eight-player requirement;
       - distinguishes frame, OWNER-SELECTED PAPER ANSWER and canon;
       - names remaining macro forks and immediate design dependencies;
       - leaves unrelated TREE content unchanged;
       - gives c-research-q-coop-interdependence-002 an unambiguous READY or
         still-HELD disposition.

     return: |
       Short Russian owner-readable contradiction brief;
       exact g-d3a8 branch diff and dependency map;
       verbatim owner verdict;
       one RESULT.

     budget: one owner-present text-only session

  5. NOW.md — register exact future CALL B:

     id: c-research-q-coop-interdependence-002
     status: HELD
     for: g-d3a8 / co-op composition question
     hold: c-map-g-d3a8-frame-v2-reconciliation-001 not yet closed
     note: |
       Return to the preserved co-op composition question under accepted
       Minimum Game Frame v2. Previous composition material remains input,
       not an OWNER-SELECTED PAPER ANSWER. No canon admission or Sc-damage
       release occurs in this CALL.

     CALL c-research-q-coop-interdependence-002
     to: session
     direction: indie-game-development
     play: local/canon-forge
     node: g-d3a8
     surface: any
     parent: s-repair-minimum-game-frame-v2-001

     goal: |
       Under accepted Minimum Game Frame v2, the existing co-op composition
       question reaches a bounded owner-selected paper answer or an explicit
       frame/question/paper block, while canon authority remains separate.

     context: |
       Run only after c-map-g-d3a8-frame-v2-reconciliation-001 closes and
       read its history RESULT.

       Also read:
       - live/indie-game-development/NOW.md
       - live/indie-game-development/CHARTER.md
       - live/indie-game-development/TREE.md
       - live/indie-game-development/plays/canon-forge.md
       - live/indie-game-development/work/
         canon-process-v3-paper-only-pilot-brief.md
       - live/indie-game-development/work/minimum-game-frame-v2.md
       - live/indie-game-development/work/
         frame-v2-distillation-handoff-2026-07-14.md
       - live/indie-game-development/knowledge/
         g9c41-players-8-owner-requirement.md
       - current gas_coop_game_canon CONSTITUTION.md, CORE.md, INDEX.md and
         canon/c-001-investigation-readiness.md
       - live/indie-game-development/history/
         2026-07-14-s-research-q-coop-interdependence-001.md
       - live/indie-game-development/history/
         2026-07-14-s-repair-minimum-game-frame-v2-001.md

       Current Gate F owner verdict is FRAME READY.

       Resume the exact preserved co-op composition question. Previous
       temporary-subgroup, situational-role and shared-causality material is
       input only and has not been selected or admitted to canon.

     boundaries: |
       Text only.
       Do not alter canon, TREE, CHARTER, product or implementation.
       Do not decide exact tools, damage, networking, balance or Bubble
       controls.
       Do not release Sc-damage automatically.
       Do not treat examples or the earlier composition draft as selected.
       Do not force mutually exclusive full-answer candidates where the
       sourced answer is genuinely compositional.

     done_when: |
       The exact current co-op composition question is sourced and
       owner-readable.

       Gate F and Gate Q statuses are explicit.

       The session returns either:
       - one OWNER-SELECTED PAPER ANSWER with all unverified dimensions and
         the owner's verbatim verdict; or
       - an honest FRAME, QUESTION or PAPER block on the same sourced issue.

       Canon remains unchanged and any later canon admission is a separate
       owner-present CALL.

     return: |
       Russian Gate F/Gate Q brief;
       composition paper artifact or exact block;
       compact source/status matrix;
       verbatim owner verdict;
       one RESULT.

     budget: one owner-present text-only session

  6. TREE.md:
     no change in this session.

  7. CHARTER.md:
     no change.

  8. gas_coop_game_canon:
     no change.

  9. Product repositories and implementation:
     no change.

  10. LOG.md:
      append the one-line log entry from this RESULT.

  11. history:
      save this full RESULT verbatim as:
      live/indie-game-development/history/
      2026-07-14-s-repair-minimum-game-frame-v2-001.md

captures: []

decisions_needed: []

play_check:
  - 1 Name the contradiction: done; Minimum Game Frame v1 deferred the run/economy/persistence layer while later owner direction selected a short finite run, gas value, artifact exceptions, full wipe, fast restart, 4–8 composition and Ball/Bubble anchor; the research source also overclassified hypotheses and examples as one law package.
  - 2 Reconstruct: done; current NOW/CHARTER/TREE, active process, v1, checksum-addressed research and handoff sources, eight-player requirement, current canon, c-001 and parent history were reconciled newest-first; mandatory sources retain their parent checksums by preserved commit ancestry and END_OF_FILE markers.
  - 3 Propose corrected state: done; exact Minimum Game Frame v2, source/status matrix, real macro forks, evidence limits and two separate future CALLs are specified; no TREE/CHARTER/canon/product mutation is included.
  - 4 Confirm: done; owner verdict cited verbatim: «FRAME READY».
  - 5 Friction: skipped; the contradiction came from an explicit later design revision, not an OS procedure hole. The stale g-d3a8/TREE and canon wording is routed to a separate owner-present reconciliation rather than silently repaired here.

log: repair g-d3a8 Minimum Game Frame v2 — owner verdict FRAME READY; accepted current whole-game frame, issued owner-present g-d3a8 reconciliation and held co-op-composition continuation; no canon/TREE/CHARTER/product change.

next: |
  CALL c-map-g-d3a8-frame-v2-reconciliation-001
  to: session
  direction: indie-game-development
  play: map
  node: g-d3a8
  surface: any
  parent: s-repair-minimum-game-frame-v2-001

  goal: |
    The g-d3a8 design/canon branch of TREE accurately reflects accepted
    Minimum Game Frame v2, the current eight-player owner requirement and
    the actual separation between frame, paper answers and canon, without
    rewriting unrelated branches.

  context: |
    Read:
    - live/indie-game-development/NOW.md
    - live/indie-game-development/CHARTER.md
    - live/indie-game-development/TREE.md
    - live/indie-game-development/work/minimum-game-frame-v2.md
    - live/indie-game-development/knowledge/
      g9c41-players-8-owner-requirement.md
    - current gas_coop_game_canon CONSTITUTION.md, CORE.md, INDEX.md and
      canon/c-001-investigation-readiness.md
    - live/indie-game-development/history/
      2026-07-14-s-repair-minimum-game-frame-v2-001.md

    Minimum Game Frame v2 has owner verdict FRAME READY and is the current
    whole-game design basis, but is not canon.

    The current g-d3a8 TREE text still carries stale 1–4-player and
    solo-startable language. Current owner direction requires support for
    eight players and treats solo as outside the present design target.

    c-research-q-coop-interdependence-002 is issued separately but remains
    HELD until this reconciliation closes.

  boundaries: |
    Owner-present, text only.
    Touch only the g-d3a8 design/canon branch and necessary NOW routing.
    Do not change CHARTER, canon, product or implementation.
    Do not activate Gate Q, select a paper answer or generate mechanics.
    Do not rewrite unrelated TREE branches.

  done_when: |
    An exact g-d3a8 TREE/map correction exists and the owner explicitly
    approves it or blocks it.

    The corrected branch:
    - reflects Minimum Game Frame v2;
    - reflects the current eight-player requirement;
    - distinguishes frame, OWNER-SELECTED PAPER ANSWER and canon;
    - names remaining macro forks and immediate design dependencies;
    - leaves unrelated TREE content unchanged;
    - gives c-research-q-coop-interdependence-002 an unambiguous READY or
      still-HELD disposition.

  return: |
    Short Russian owner-readable contradiction brief;
    exact g-d3a8 branch diff and dependency map;
    verbatim owner verdict;
    one RESULT.

  budget: one owner-present text-only session

END_OF_FILE: live/indie-game-development/history/2026-07-14-s-repair-minimum-game-frame-v2-001.md
