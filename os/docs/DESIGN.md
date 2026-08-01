# Direction OS — проектный документ

Дата: 2026-06-10. Спроектировано с нуля по os/docs/REQUIREMENTS.md и os/docs/RESEARCH_BASIS.md. Прошлые поколения (archive/workflow/, archive/workflow_v3/, archive/directions/) — только источник уроков.

## 1. Архитектура одним взглядом

```
os/                          ← система (правила; меняется по os/MAINTENANCE.md)
  KERNEL.md                  ← конституция: сессия, состояние, пакеты, 10 гейтов
  plays/  frame map shape converge converge-arch converge-verify day
          work guide review research pulse repair
  schema/ direction-files, packets
  adapters/ SESSION_PAYLOAD, chatgpt-project, claude-project,
            other-platforms, coding-agent, autonomy, runtime
  engineering/ CONTOUR, PROJECT_SETUP, VALIDATION, TOOLING, profiles/
  MAINTENANCE.md, EXTENDING.md, FRICTION.md, BOOTSTRAP.md, docs/

live/<direction-id>/         ← направления (живое состояние)
  CHARTER.md  TREE.md  NOW.md  LOG.md  history/  knowledge/  work/
  plays/                     ← локальные процедуры направления (опционально,
                               EXTENDING.md; правила, не state)

<product repos>              ← код продуктов (репо игры и т.п.), своя жизнь,
                               связь только через executor CALL
```

Поток: **frame** → **map** → выбранный outcome идёт одним из двух путей. Обычный build-outcome: **converge-readiness** (verified/OFF → shape; иначе converge → verify) → **shape** → **work**×N → свежий **review**. `outcome_kind: specification`: untracked owner-authority **work** создаёт exact owner-approved artifact → свежий **converge-verify** пытается его опровергнуть → узкий **review** закрывает parked-узел без shape/bet/tasks/tracks. Поверх — **pulse**; сбой — **repair**; побочные вопросы — **research**-дети. **day** — read-only стратегическая оболочка и пишет только после явного «сохранить».

## 2. Ключевые решения и отвергнутые альтернативы

**D1. Одна рекурсивная сущность цели (узел дерева) вместо слоёв Direction→Map→Front→Graph→Node.**
Узел = goal + done_when + status (+appetite/kill_by у бета). Глубина растёт лениво, по месту (shape может породить детей вместо задач). Отвергнуто: фиксированные слои (порождают 60+ сущностей и церемонии на каждом уровне — урок v3) и плоский список задач (теряет стратегию — урок его «маленьких тасок»).

**D2. Бет (Shape Up) как единица обязательства, а не «веха» и не «спринт».**
Appetite фиксируется до задач и не продлевается (G3); смерть по таймеру/kill_by — норма; продолжение = новый бет через новый shape. Это главный механизм против разрастания скоупа владельца: в системе физически нет операции «продлить/раздуть». Отвергнуто: вехи с плавающими сроками (так умер v2: планирование без давления времени).

**D3. Задачи живут только в NOW.md активного бета (G2), дерево — только outcomes.**
Rolling-wave, механически проверяемый. Отвергнуто: work graph всего направления (v3) — детальные планы дальнего будущего гниют и съедают планирование.

**D4. Два пакета (CALL/RESULT) на все случаи: следующая сессия, ребёнок, исполнитель.**
Поля CALL = Goal/Context/Boundaries/Done-when/Return/Budget — схема, на которой сошлись OpenAI, Anthropic и Devin. Отвергнуто: типизированные пакеты на каждый случай (v3: 7+ типов, поля без владельцев).

**D5. Кросс-функциональность через линзы; параллельность только внутри текущей цели.**
Линза — обязательный вопрос, не контейнер работы. TREE содержит одну карту, NOW — не более одного активного бета, а `NOW.tracks` при необходимости группирует независимые execution lanes только внутри этого бета. Будущие цели остаются видимыми как parked/shaped; возникшая вне текущей цели работа попадает в `NOW.issues` с маршрутом и условием пересмотра. `running` — долговечная квитанция запуска, а не оценка прогресса. Отвергнуто: функциональные backlog-треки и отдельный управляющий трек, живущие рядом с глобальной целью, перекрёстные outcome-запросы, скрытая очередь «последний RESULT = следующий» и надежда на память владельца.

**D6. Done — только по доказательствам; бет проверяет свежая сессия через попытку опровержения (G5).**
Прямой ответ на измеренные галлюцинации завершения и сикофантию. Отвергнуто: 30-пунктовые аудиты v3 (непроверяемые) и самопроверка рабочей сессией.

**D7. Решения владельца — редко, батчем, с опциями и рекомендацией (G7); тиры действий вместо сплошных подтверждений.**
Отвергнуто: подтверждение каждого шага (approval fatigue → штамповка; и его явное желание «не участвовать в каждом анализе»).

**D8. Запись состояния — только писателем из RESULT.state_changes; legs не «помнят», а перечитывают Git (recite).**
Отвергнуто: ручной перенос состояния владельцем (корневое трение v3) и доверие памяти чата.

**D9. Система меняется только по журналу трения (≥2 случая), в жёстких бюджетах (§7 ядра).**
Прямой урок мета-аттрактора (40% мета-коммитов в июне; governance как самое активное «направление»). Workflow-governance направлением больше не является.

**D10. Языки: правила OS — английский (надёжнее исполняются моделями, нейтральны к вендору), диалог с владельцем — русский (вшито в ядро), значения полей — любые.**

Где я сознательно отступил от эскизов владельца: (а) нет отдельного плейбука «создать work graph» — задачи порождает shape, и это единственное место; (б) нет console-плейбука — read-only вопросы освобождены от церемонии правилом ядра; (в) «вехи» заменены бетами с нерастяжимым appetite — это жёстче, чем он просил, и именно поэтому это ответ на его главный недостаток.

## 3. Трассировка требований

| Требование | Компонент |
|---|---|
| R-1 направления автономны | live/<id>/ самодостаточен; pulse — единственная кросс-точка |
| R-2 сложные направления | рекурсия дерева (D1) + executor-шов + линзы |
| R-3 заменить команду, закрыть слабости | сессия = специалист (work §2); G3/G6 против скоуп-крипа |
| R-4 владелец-арбитр, путь к автономии | G7, decisions-инбокс, adapters/autonomy (тиры, стадии) |
| R-5 одна работа — один atomic leg | KERNEL §2; обычный state-changing чат = один leg; day сохраняет каждое согласованное изменение отдельным RESULT |
| R-6 чат выдаёт следующий чат | RESULT.next — обязательное поле |
| R-7 чат = явная процедура | play в каждом CALL; «нет play → repair» |
| R-8 ориентация за секунды | orientation header в каждом ответе (KERNEL §2) |
| R-9 дочерние чаты рекурсивно | call:research, parent-поле, return-to-parent |
| R-10 состояние в git | live/**, writer, history |
| R-11 слоистая память | NOW (горячее) → LOG (строка+ссылка) → history (полный) → knowledge |
| R-12 платформо-независимость | пакеты самодостаточны; адаптеры отделяемы |
| R-13 desync — норма | play repair; G5 «не выдумывать прогресс» |
| R-14 рекурсивная декомпозиция | D1; shape Note про детей вместо задач |
| R-15 волна детализации | G2 |
| R-16 возникающая работа не теряется | capture-ход + `NOW.issues` с stable id, route, review_when и evidence; триаж в day/shape/pulse |
| R-17 жёсткий отбор следующего | review шаг 6 + RAT в G6; day рекомендует один фокус и 0..N независимых execution lanes только внутри текущего бета |
| R-18 сила отсечения | G3 (no extend), G6 (cut list), add-back check, parking lot |
| R-19 кросс-функциональность из структуры | D5 |
| R-20 параллельные затеи | будущие цели parked/shaped в TREE; одновременно ≤1 активный бет; owner-set WIP для 0..N collision-free execution lanes внутри него |
| R-21 код — бизнес-задачей агенту | executor CALL kind:engineering; AGENTS.md в репо продукта |
| R-22 запись машиной | writer (kind:mechanical) |
| R-23 нет магии/непроверяемого | 10 гейтов — все механические; единый порядок авторитета |
| R-24 бюджет размера | KERNEL §7 |
| R-25 модульность | os/{KERNEL,plays,schema,adapters} независимы |
| R-26 система ≠ направление | KERNEL §7 + FRICTION.md |
| R-27 обоснованность исследованием | docs/RESEARCH_BASIS.md (каждый механизм ← источник) |
| R-36 владелец-исполнитель | plays/guide; вид задачи guide в shape; guide-CALL из G6-отчётов |
| R-37 кастомизация направления | EXTENDING.md: локальные plays (≤5), политики в knowledge/CHARTER, модули os/<module>/ |
| R-38 recurring-обязательства | NOW.recurring (≤3, решение владельца) + pulse-пункт 7 |
| R-39 защита от обрезки | END_OF_FILE-трейлеры всех state-файлов (writer поддерживает) + правило в payload + writer collect |
| R-40 свободный человеческий интерфейс | KERNEL §2 OPEN/owner-facing + play day + SESSION_PAYLOAD/runtime |
| R-41 атомарный leg и долгий дневной диалог | KERNEL §2 + direction-os + day + SESSION_PAYLOAD + BOOTSTRAP + runtime; day read-only до явного save, каждый save — отдельный RESULT |
| R-42 восстановимость | TREE/NOW/issues/open_calls + durable `running` launch receipt + status/artifact + checkpoint-RESULT + pulse; day перечитывает Git |
| R-43 параллельные направления | worktree на направление; внутри — merge по call/track id; одно перо на apply |
| R-44 со-творчество планов | gate G9 + play map (узел-карточка → вердикт) + frame без детей + writer отклоняет без owner_approved |
| R-45 полно хранить, минимально грузить | why-строка в узле + detail-ссылка на history; слои памяти (R-11) |
| AR-1..AR-5 | нет ритуал-команд; один вопрос — одно место (NOW); правила требуют только видимого сессии; один источник истины (live/); владелец не копирует состояние (writer) |

Белых пятен нет: каждый R закрыт; каждый компонент ссылается на R.

Search-plane волна (2026-06-11) усиливает R-2/R-17/R-18 (стратегический поиск и отбор до выбора бета), не вводя новых R, гейтов или типов state: механизмы — строки в plays + поля в CHARTER/NOW; источник и адверсариальная проверка — в `os/docs/RESEARCH_BASIS.md` (строка search plane) и proposal-доках. Каждый механизм несёт фальсификатор в `os/FRICTION.md` — волна откатывается помеханизменно.

Session-protocol волна (2026-06-11, после инцидентов пилота) закрывает риск №1 из §5 (дисциплина в chat-платформах без enforcement): гейт G10 — opening contract в первом ответе обычного leg; day показывает простой человеческий header/view, остаётся read-only до явного save и после каждого сохранённого atomic leg снова перечитывает Git; RESULT только финальным сообщением state-changing leg, запрет прямой записи сессиями, валидация писателем перед применением, CALL-гигиена (goal без пересказа процедуры). Диагноз, альтернативы и фальсификаторы: `os/docs/SESSION_PROTOCOL_AUDIT.md`.

## 4. Валидация: «кооперативная игра с жёсткой симуляцией газа»

- **frame** (1 чат): миссия, успех «релиз в Steam, ≥$N или окупаемость», линзы product/audience/business/craft, пре-мортем («не выйду на аудиторию», «симуляция съест годы», …→ kill-кандидаты), outside view (медиана Steam ~$249, третьи игры ×2 → рекомендация резать дебютный скоуп), дерево: g-root → «проверенный прототип газового кооп-лупа», «публичное лицо+спрос», «решение о финансировании», «производство», «релиз». Всё parked.
- **converge-readiness** первого узла: без PASS/OFF map открывает converge; trivial-триаж фиксирует OFF и открывает shape, standard/heavy проходит converge[-arch] → converge-verify → shape.
- **Что разбор обязан закрыть, а что нет (пересмотрено 2026-08-01 по замеру).** Разбор закрывает строку ТОЛЬКО из источника вне самой ноги — слова владельца, замороженный канон или улика (код, прогон, замер). Строка, до которой нога додумалась сама, остаётся `open` с названным должником (владелец, PLAN или стройка) и закрытию НЕ мешает: открытые строки едут в shape как его повестка вырезов. Причина: прежнее требование «ноль открытых строк» при отсутствующем владельце и запрете носить ему технические развилки заставляло ногу ВЫДУМЫВАТЬ ответы — четыре узла с триажем heavy дали 89, 27+ и 15 строк собственного авторства и ноль строк продукта, а каждая починка рождала новые находки из предыдущей. Второй FAIL проверки закрывает бумажную фазу узла и выносит владельцу одно решение вместо третьего круга. Это тот же ход, что контракт v35 сделал этажом ниже, убрав прозаический PLAN из ворот запуска.
- **Specification-outcome (current-map trace, g-12fd):** exact owner-approved card is marked `outcome_kind: specification` because its done_when ends at the versioned approved demo specification itself. Map opens one untracked `to: session, play: work` CALL to the direction-declared clean-room owner-authority contour (Canon is one possible instance, not a core controller). It records the exact artifact identity and the owner's approval words while TREE stays parked and `bet: null`. A later fresh `converge-verify` atomizes done_when, runs the play's two attacks against the artifact and never repairs or decides content. PASS opens narrow review; review matches node+artifact+approval+later PASS, marks only g-12fd done under G9/G5, and routes the next ordinary node through readiness. At every point tasks/tracks/executor content verdicts/shape are absent.
- **Ordinary build-outcome trace:** without `outcome_kind: specification`, map opens converge unless a verified receipt or exact OFF triage exists; standard/heavy runs converge[-arch] → fresh converge-verify → shape. Shape alone activates the bet, sets appetite/cuts/tasks/kill_by, and the last work task still opens fresh review. Thus the specification exception cannot bypass build readiness or execution evidence.
- **shape** первого узла: appetite 3 недели; minimal — соло-прототип с газом, кооп позже (cut list: кооп-неткод, арт); lens sweep: product=прототип, audience=разбор 5 похожих + 10 плейтестов, business=not_needed (рано), craft=выбор движка спайком; RAT: «газ-симуляция фаново ощущается на минимальном масштабе» → задача №1; kill_by: «если прототип не фанов 6/10 тестерам к <дата> — узел пересматриваем».
- **work**: прототип — executor CALL в репо игры (бизнес-задача, агент сам решает архитектуру); разбор рынка — обычная сессия, рождает knowledge «в жанре конвертят демо+стримеры» (read_by: shape узлов audience).
- **«Собрать отзывы у друзей»** (R-16 на пальцах): в shape это задача с done_when «≥10 заполненных анкет». Если в work выясняется, что нужен протокол, список людей и видеозапись — это captures; они НЕ исполняются в той же сессии; shape/pulse превращает их в задачи, а «видео-продакшн» при разрастании — в отдельный узел дерева со своим бетом. Ничего не повисает «в стороне».
- **review** (свежая сессия): опровергает «фаново» по анкетам, а не по ощущению чата; harvest: product «масштаб симуляции дорог» → узел оптимизации; audience «друзья просят демо» → подтверждает следующий узел; business «о цифрах говорить рано» → честное nothing. Кандидаты следующего бета из РАЗНЫХ линз, с рекомендацией. Владелец отвечает одной строкой.
- **Скоуп-крип владельца**: «давай добавим разрушаемость» в середине бета = capture → parked (G8), в бет не попадает (cut list — закон); попытка продлить бет на неделю — операции нет (G3), только новый shape, где разрушаемость обязана пережить scope hammer.

- **Стратегический день и безопасная параллельность**: TREE показывает всю карту, но NOW содержит не более одного активного бета. Внутри него `gameplay` и `evidence` могут быть независимыми lanes с общим owner-set WIP; обратный порядок двух RESULT не ломает состояние, потому что writer применяет delta по stable call id и сохраняет соседний CALL. Пока `bet: null`, обычные execution tracks запрещены: допустим только один planning/review/repair frontier. Возникшее «добавить звук» не создаёт второй бет и не теряется — day сохраняет issue со stable id, route, review_when и evidence. Утром day перечитывает Git, показывает цель, один текущий фокус, lanes, проблемы, сроки и forecast; без слова «сохранить» diff отсутствует. После явного save он выпускает ровно один atomic RESULT, а затем снова читает Git. Если для шанса релиза нет reference class, denominator или проверенной калибровки, forecast честно остаётся `no_basis`, а не превращает выполнение задач в псевдовероятность. Закрытие бета всегда идёт через fresh review с исходами met/partial/killed/obsolete; потерянный чат восстанавливается из Git.

## 5. Риски и пилот

Главные риски: (1) дисциплина гейтов в chat-платформах без enforcement — мониторим через FRICTION, лечится переносом state-тяжёлых plays в агентные CLI; (2) NOW.md распухнет — бюджет «один экран» + pulse; (3) система всё же окажется в минус — honesty instrument в pulse (минуты владельца vs закрытые беты).

Пилот: (1) направление **indie-game** через BOOTSTRAP (стресс-тест с нуля); (2) направление **health** поверх готовых планов из archive/directions/health-and-beauty (тест исполнения). Критерий: 10 закрытых сессий подряд, в которых не понадобилась правка os/** (записи в FRICTION допустимы — правки нет). Старые неймспейсы заморожены в archive/; перенос — только содержимого (планы, знания), никогда — механики.

END_OF_FILE: os/docs/DESIGN.md
