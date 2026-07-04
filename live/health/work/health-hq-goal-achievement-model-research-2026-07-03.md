# Health HQ как слой оркестрации достижения цели для Health AI

**This is research input, not product acceptance.**

**This does not initialize Health HQ.**

**This does not authorize implementation.**

## Статус исследования и короткий вывод

Контекст цели здесь необычно важен: речь не о «health dashboard» и не о «коуче по промпту», а о минимальном слое, который должен удерживать курс на долгую цель снижения массы, сохранения результата и постепенного улучшения состава тела, при этом не превращая Direction OS в поток сырых логов. Это согласуется с тем, как в доказательной базе устроено успешное управление ожирением: результат дают **интенсивные многокомпонентные поведенческие вмешательства** с работой по питанию, физической активности, самоконтролю и долгосрочному удержанию, а не одна техника, один экран или одна «умная» подсказка. NICE в руководстве NG246 от 14 января 2025 года, обновлённом 8 января 2026 года, рассматривает ожирение как предмет длительного многокомпонентного ведения; USPSTF рекомендует взрослым с ожирением интенсивные многокомпонентные поведенческие вмешательства; обзор JAMA 2023 года также описывает доказательное лечение ожирения как сочетание поведенческих интервенций, питания и физической активности. citeturn5view2turn0search1turn10search16

Даже **умеренная** первая веха в снижении веса клинически значима. CDC прямо указывает, что уже снижение примерно на 5% может улучшать давление, липиды и гликемию; обзор JAMA 2023 года суммирует, что у людей с ожирением снижение на 5–10% приносит измеримую клиническую пользу. Для вашего исходного веса 125 кг это делает первую веху очень конкретной: **5% = 118,75 кг**, **10% = 112,5 кг**. citeturn0search2turn4search3

В поведенческих программах типа National DPP первая практическая цель обычно формулируется как **5–7% снижения массы тела** и **не менее 150 минут физической активности в неделю**, а сама программа строится не как разовая акция, а как **годовой цикл**: плотный первый блок и поддерживающий блок далее. CDC указывает эти ориентиры для PreventT2/National DPP, а литература по поддержанию веса подчёркивает, что после первичного снижения веса нужен отдельный maintenance-режим с предупреждением рецидива и хотя бы ежемесячным контактом/консультированием. citeturn2search0turn2search8turn10search3turn10search7turn10search10turn10search1turn10search4

Физическая активность и силовая работа в этой модели не «дополнение ради общего здоровья», а часть механики достижения цели. WHO и CDC рекомендуют взрослым не менее **150–300 минут умеренной аэробной активности в неделю** или эквивалент, плюс **силовую работу не менее 2 дней в неделю**; для удержания веса после снижения наблюдательные и клинические данные часто указывают на потребность в **более высоком объёме активности**, нередко около **250+ минут в неделю**. Отдельно мета-анализ 2022 года показал, что резистивный тренинг помогает сохранить безжировую массу при сочетании с ограничением калорий, то есть поддерживает именно качество снижения веса, а не только массу на весах. citeturn1search0turn1search1turn1search8turn11search1turn11search12turn8search1

Сон и восстановление нельзя считать «добровольным nice-to-have». CDC и AHA указывают, что взрослым обычно требуется **7 и более часов**, чаще **7–9 часов** сна, а плохой сон связан с ожирением, кардиометаболическим риском, снижением дневного функционирования и менее благоприятным поведением в питании и активности. Это не делает Health HQ медицинским советником, но делает сон/восстановление обязательным ограничителем оркестрации. citeturn9search2turn1search6turn1search18turn9search0turn9search4turn9search16

**Короткий ответ**

- Health HQ v0 должен быть **слоем оркестрации достижения цели**, а не экраном статуса: его ядро — удержание цели, фаз, вех, метрик, bottleneck-классификации, owner-facing решений и маршрутизации требований в домены.
- Health HQ должен владеть **phase/milestone model**, **metric hierarchy**, **review loop**, **domain demand contracts**, **decision classes** и **safety boundaries**.
- Health HQ **не должен** владеть сырыми логами веса, питания, тренировок и сна; эти данные должны оставаться в доменах/операционных слоях, а в Direction OS должны попадать только сводки, решения, проблемы и next calls.
- Health HQ **не должен** быть «status dispatcher / summary reviewer» как сущность продукта: summary loading и routed requests — это лишь подкомпоненты, а не определение продукта.
- Health HQ **не должен** быть «dashboard / cockpit / integration hub»: доказательная база поддерживает самоконтроль и обратную связь, но не равняет их сущности системы; многокомпонентность и maintenance важнее наличия панели. citeturn2search3turn8search13turn10search1
- Health HQ **не должен** быть «god-agent», который сам переписывает планы питания и тренировок: доказательная база поддерживает совместную, длительную, адаптивную работу, но не оправдывает бесконтрольную автономную модификацию; кроме того, это прямо ломает ваш authority split. citeturn5view2turn10search4
- Health HQ **не должен** быть медицинским советником: он может флагировать риск, остановить эскалацию нагрузки/дефицита, запросить доменный review и предложить владельцу рассмотреть профессиональную консультацию, но не ставить диагноз, не назначать лечение и не «разрешать» опасные симптомы. citeturn6search1turn6search4turn9search2
- Existing summary-only proof **недостаточен** как продукт Health HQ. Он полезен как техническое доказательство того, что summary-only review, adapters, non-mutating routed requests и boundary flags возможны, но он не покрывает решающее: milestone model, strategic review logic, demand contracts, decision classes и ownership boundaries.
- Минимально жизнеспособный Health HQ должен уметь отвечать не только на «что сейчас?», но и на «идём ли мы к вехе?», «что является bottleneck?», «какое доменное требование следует выдать?», «какое owner-решение требуется?» и «что должно произойти следующим шагом?»
- Поэтому следующий шаг после этого исследования — **не код**, а owner-reviewable WHAT/route, где будут явно подписаны сущность HQ, его границы власти, метрики, фазы, review loop и классы решений.

**Установленное доказательное основание**

- Ожирение требует долгосрочного многокомпонентного подхода; успешные программы сочетают питание, физическую активность, поведенческие техники и maintenance. citeturn5view2turn0search1turn10search16turn10search4
- Первая практическая веха 5–10% снижения веса действительно значима и реалистична как ранний ориентир. citeturn0search2turn4search3turn2search0
- Для движения и удержания результата нужны отдельные механизмы: минимум активности для здоровья и отдельный support layer для maintenance. citeturn1search0turn1search1turn11search1turn10search1

**Вывод проектирования**

Health HQ v0 должен быть не «местом, где лежат summary», а **диспетчерской стратегического хода к цели**, которая работает только через owner-triggered reviews и non-mutating demands к доменам.

**Решения владельца, которые исследование не может принять вместо владельца**

Ниже они будут перечислены подробно, но уже на этом этапе видно, что исследование не может за владельца определить: конечный внешний критерий «athletic look», приоритет скорости снижения веса против силовых и recovery-ограничений, список базовых силовых маркеров и допустимый уровень owner-approval для разных классов изменений.

## Почему некоторые модели не подходят

Ниже — пять моделей, включая все обязательно запрошенные, и вывод по каждой.

| Модель | Что это | Почему соблазнительна | Почему не подходит или недостаточна | Что можно спасти |
|---|---|---|---|---|
| **Статус-диспетчер / summary reviewer** | Принимает summary, делает короткий обзор, иногда маршрутизирует запрос дальше | Уже есть технический proof; дешёвая первая версия; хорошо соответствует границе raw-data | Не владеет целями, фазами, bottleneck-классификацией и стратегическим сдвигом. Отвечает на «что видно», но не на «что делать для достижения root goal». Продуктовая сущность остаётся пустой | Summary loading, boundary flags, non-mutating routed requests |
| **Дашборд / cockpit / integration hub** | Единая панель данных, статусов, интеграций, API, maybe wearable feeds | Видимость, «ощущение контроля», лёгко демонстрировать прогресс | Смешивает продуктовую сущность с инфраструктурой. Самоконтроль полезен, но панель сама по себе не решает maintenance, relapse prevention и междоменные trade-offs. Плюс это прямо тянет в API/integration creep, который вы запретили. citeturn2search3turn8search13turn10search4 | Несколько owner-facing summary views и bounded metric snapshots |
| **Автономный god-agent / optimizer** | Сам решает, что менять, и тихо переписывает питание/нагрузку ради лучшей метрики | Кажется «умным» и быстрым; обещает максимальную оптимизацию | Ломает authority split, создаёт silent mutation, конфликтует с governance и при health-temaх опасно размывает границу между orchestration и treatment. Он начинает притворяться и продуктом, и исполнителем, и частично клиницистом одновременно | Bottleneck classification engine и scenario comparison, но только как advisory layer |
| **Prompt-only goal coach** | Разговорный коуч: поддержка, разборы, мотивация, советы по запросу | Просто запустить; выглядит персонально; подходит для лёгких check-ins | Коучинг полезен, но доказательная база показывает, что устойчивое снижение и удержание веса требуют не только разговорной мотивации, а структурированного многокомпонентного процесса, самоконтроля, фаз и maintenance-механики. Самонаправленные/только self-directed интервенции обычно дают лишь скромный краткосрочный эффект. citeturn10search0turn12search15turn10search1 | Owner-facing language, habit support, explanation layer |
| **Слой оркестрации достижения цели** | Удерживает root goal, фазу, вехи, метрики, bottlenecks, доменные запросы и owner decisions; сам не исполняет доменную работу | Соответствует вашему authority split и реальной задаче достижения долгой цели | Требует более чёткой WHAT-модели и governance, чем «просто reviewer»; нельзя запускать без signed boundaries | Это и есть рекомендуемая модель |

**Установленное доказательное основание**

Самоконтроль и цифровые средства могут поддерживать снижение веса, но наилучшие результаты связаны не с одной техникой, а с её включением в **полноценное поведенческое лечение**. Systematic review по digital self-monitoring показывает полезность цифрового самоконтроля, а обзоры по ожирению подчёркивают, что лечение остаётся многокомпонентным; при этом maintenance отдельно требует problem-solving, relapse prevention и длительного сопровождения. citeturn8search13turn2search3turn10search0turn10search4

**Вывод проектирования**

Если кратко:  
dashboard хорош как интерфейс, reviewer хорош как подмодуль, coach хорош как коммуникативный слой, optimizer хорош как analytical engine — **но ни один из них по отдельности не является нужной сущностью Health HQ**. Нужная сущность — orchestration layer, который может использовать все эти подкомпоненты, но не сводится ни к одному из них.

**Решение владельца**

Владельцу нужно формально зафиксировать, что Health HQ — это именно orchestration layer, а не продуктовое имя для уже существующего summary-review proof. Без этого любой следующий executor почти неизбежно скатит HQ либо в reviewer, либо в dashboard.

## Рекомендуемая сущность Health HQ

**Рекомендуемая модель**

Health HQ v0 стоит определить как **owner-triggered goal-achievement orchestration layer** для root health goal. Он должен держать не данные исполнения, а **управляющую модель движения к цели**: что является текущей фазой, какие минимальные метрики нужны сейчас, достигнута ли следующая веха, что мешает прогрессу, какой домен должен что разобрать, какое изменение требует owner approval и что должно быть следующим owner-facing действием.

**Что Health HQ владеет**

| Объект владения | Что это значит practically |
|---|---|
| Root goal и phase state | Хранит формулировку цели, текущую фазу, фазовый exit condition, maintenance corridor |
| Milestone map | Например: первая клинически значимая веха 5–10%, затем масштабирование к целевому диапазону, далее maintenance |
| Metric hierarchy | Минимум метрик сейчас, later-phase метрики, pending-метрики, которые не нужны до появления влияния на решения |
| Bottleneck taxonomy | Классы проблем: adherence, plan mismatch, recovery/capacity, measurement gap, safety uncertainty, governance gap |
| Review loop | Как owner query превращается в разбор, verdict, routed requests и decision log |
| Domain demand contracts | Формат того, что HQ может запрашивать и что домены обязаны уметь вернуть в summary |
| Decision classes | Какие изменения advisory, какие требуют owner approval, какие блокируются safety boundary |
| Review/decision log | Только summary of decisions, problems, next calls — без raw logs |

**Что Health HQ не владеет**

| Что вне HQ | Почему вне HQ |
|---|---|
| Сырые body/nutrition/training/sleep log’и | Это нарушает ваш raw-data boundary и превращает Direction OS в дневник |
| Исполнение доменной работы | Питание, тренировки, активность, сон/восстановление должны жить и исполняться в своих доменах |
| Тихое редактирование артефактов домена | Ломает authority split и governance |
| Медицинская интерпретация, диагноз, лечение | Это за пределами продукта и безопасности |
| Интеграционный слой, polling, API, wearables, database architecture | Это инфраструктурная/будущая работа, а не сущность v0 |

**Какие входы он потребляет**

| Вход | Формат |
|---|---|
| Owner intent | «что сегодня?», «разбери неделю», «проверь прогресс», «где bottleneck?», «добавить новый процесс?» |
| Target state | Root goal, phase target, owner trade-offs, границы approval |
| Domain summaries | Краткие сводки по питанию, training/activity, sleep/recovery, future domains |
| Safety/recovery flags | Красные/жёлтые сигналы, которые ограничивают эскалацию |
| Governance context | Какие изменения требуют owner decision |

**Какие выходы он производит**

| Выход | Содержимое |
|---|---|
| Progress verdict | On-track / at-risk / stalled / blocked / unsafe-to-escalate |
| Bottleneck classification | Главный bottleneck и уровень уверенности |
| Strategy implication | Что это значит для курса: держать, пересмотреть, снизить нагрузку, запросить доменный review |
| Routed domain requests | Немутационные запросы к конкретным доменам |
| Owner decision request | Чётко сформулированная развилка, если нужен апрув |
| Review log entry | Краткая запись в Direction OS: решение, проблема, next call |
| Next owner-facing action | Что делать дальше владельцу: запросить домен, утвердить вариант, вернуться через неделю и т.д. |

**Как Health HQ координирует домены**

Доказательная база показывает, что успешное управление весом требует сочетания питания, физической активности, поведения/самоконтроля и maintenance; сон и recovery связаны с кардиометаболическим риском и поведенческой устойчивостью, а силовая нагрузка помогает сохранять безжировую массу во время снижения веса. Поэтому HQ должен координировать домены **через стратегические требования**, а не через прямое редактирование планов. citeturn10search16turn2search3turn9search0turn8search1

Практически это означает такой режим:

1. HQ сравнивает **phase target vs current summary state**.  
2. HQ определяет, есть ли bottleneck.  
3. HQ формулирует **требование к домену**, а не изменение артефакта.  
4. Домен сам исполняет у себя свою процедуру и возвращает summary/proposal.  
5. Если изменение materially changes strategy, нужен owner approval.  
6. В Direction OS остаётся только итого: verdict, bottleneck, routed requests, decision need, next call.

**Как HQ избегает silent mutation**

- Он не хранит у себя «живой» план питания или тренировок как редактируемый объект.
- Он выпускает только **request objects**: запросить ревизию, сравнить варианты, проверить соответствие фазе, снизить/не повышать эскалацию, подготовить 2–3 owner-approve options.
- Любой mutation может происходить только **внутри домена** и только по правилам этого домена.
- Материальные изменения отмечаются как **approval-required**.

**Почему это не dashboard и не reviewer**

Dashboard отвечает на вопрос «что видно». Reviewer отвечает на вопрос «что я могу сказать по summary». Health HQ должен отвечать на более сильный вопрос: **«что требуется сейчас, чтобы цель продолжала достигаться?»** Это уже не read-only наблюдение, а оркестрация: фаза, веха, bottleneck, implication, demand, decision, next call.

**Роль existing summary-only proof**

Текущий `x_health_hq` proof нужно трактовать как **субкомпонентную техническую улику**, но не как продуктовый ответ.

| Что из proof полезно | Как использовать |
|---|---|
| Summary-only review | Как механизм загрузки сводного состояния |
| Fixtures / adapters | Как способ подключать домены на тестовых summaries |
| Non-mutating routed requests | Как базовую механику безопасной маршрутизации |
| Boundary flags | Как заготовку safety/governance флагов |

| Чего proof не доказывает | Почему этого недостаточно |
|---|---|
| Сущность HQ | Нет ответа, чем HQ является как продукт |
| Phase/milestone model | Нет стратегии движения к root goal |
| Metric hierarchy | Нет различения now/later/pending metrics |
| Bottleneck taxonomy | Нет решающей классификации проблем |
| Decision classes | Нет формального split advisory vs approval-required |
| Domain demand contracts | Нет нормативного интерфейса между HQ и доменами |

**Установленное доказательное основание**

- Self-monitoring — важная, но не единственная часть лечения ожирения. citeturn2search3turn8search13turn8search2
- Resistance training помогает сохранять lean mass во время снижения веса. citeturn8search1turn2search10
- Maintenance — отдельная задача со своим режимом relapse prevention и длительной поддержки. citeturn10search1turn10search4turn10search10

**Вывод проектирования**

Health HQ v0 должен быть **не summary layer и не execution layer, а decision-and-demand layer**.

## Метрики, фазы и цикл стратегического обзора

**Минимальная иерархия метрик**

Ниже — минимальная иерархия, которая нужна именно для решений. Всё, что не меняет решения, не должно попадать в обязательный v0.

**Текущая минимально необходимая группа**

| Метрика | Target | Current | Source / why pending | Какое решение может менять |
|---|---|---|---|---|
| **Тренд веса** | Нисходящий фазо-соответствующий тренд, а не случайное дневное колебание | Последний 7-дневный / недельный агрегат | Из tracking/body summary; если нет — pending until domain exists | Держать стратегию, пересмотреть питание, проверить adherence, не повышать нагрузку |
| **Первая веха 5–10%** | 118,75 кг для 5%; 112,5 кг для 10% от 125 кг | Текущая дистанция до вехи | Вычисляется из baseline + trend summary | Смена фазы, сохранение/усиление/пересборка стратегии |
| **Nutrition adherence/support** | Достаточная приверженность, чтобы объяснять ожидаемый дефицит | On-track / partial / off-track + главный blocker | Nutrition summary; не raw food diary | Запросить nutrition review, поменять структуру плана, не винить training за stall |
| **Силовая приверженность** | Выполнение согласованного минимума силовых сессий и ключевых движений недели | Planned vs completed | Training/activity summary | Удерживать/упрощать шаблон, менять частоту, не эскалировать объём |
| **Объём активности / conditioning** | Минимум для текущей фазы; сначала хотя бы достижение guideline-like base, позже выше для maintenance | Минуты / шаги / сессии по summary | Training/activity summary | Повысить NEAT/кардио, оставить как есть, отложить эскалацию |
| **Сон / восстановление** | Нет признаков, что дефицит или нагрузка ломают восстановление | Green / yellow / red + 1–2 ключевых сигнала | Sleep/recovery summary; если домен не создан — pending with explicit risk | Блок на эскалацию дефицита/объёма, запрос sleep/recovery review |
| **Энергия / боль / дневная функциональность** | Совместимы с продолжением плана | Low / moderate / high interference | Sleep/recovery или training summary | Делoad, pause escalation, domain review, owner decision |
| **Возраст последнего review** | Не старее owner-selected cadence | Кол-во дней с последнего review | HQ review log | Требовать review до изменения стратегии |

**Позднее, когда начнут реально менять решения**

| Метрика | Когда включать | Source / pending | Какое решение меняет |
|---|---|---|---|
| **Базовые силовые маркеры** | Когда цель смещается от «снижать вес» к «сохранять/улучшать силу и композицию» | Training domain; owner must choose movements | Если вес уходит, а сила обваливается — менять training/nutrition balance |
| **Талия или waist-to-height ratio** | Когда появится надёжное и повторяемое измерение | Tracking/body summary; currently likely pending | Уточнять body-composition progress при шумном весе |
| **Body-composition estimate** | Только если есть повторяемый метод и он реально влияет на решения | Pending unless reliable source exists | Решения о recomposition phase |
| **Высокообъёмная активность maintenance** | После достижения целевого диапазона или близко к нему | Training/activity summary | Переход в maintenance standards |
| **Длительность удержания в target corridor** | После входа в 90–95 кг | HQ phase state + weight trend summary | Подтверждение maintenance success / relapse response |

**Оставить в pending до фактического decision impact**

| Метрика | Почему не обязательна в v0 |
|---|---|
| Точные дневные калории в Direction OS | Сырые данные не должны жить в HQ/Direction OS; HQ нужен adherence verdict, а не столбцы лога |
| Макросы с высокой детализацией | Нужны только если nutrition domain докажет, что они меняют решение |
| HRV, resting HR, wearable-derived readiness | Многие такие сигналы шумные и легко создают integration creep |
| Автоматические body-fat % из бытовых устройств | Часто недостаточно надёжны для стратегических решений |
| VO2max estimates | Полезны позже, но не минимальны для v0 |
| Детальные микроэлементы | Обычно не меняют phase-level orchestration в минимальной модели |

**Доказательные якоря для численных порогов**

- Первая клинически значимая веха 5–10% снижения массы хорошо подтверждена; CDC и NIH/NHLBI используют этот ориентир как практический ранний результат. citeturn0search2turn4search20turn4search4
- DPP-style ориентир 5–7% плюс 150 минут/неделю и годовая структура программы подтверждены CDC. citeturn2search0turn10search3turn10search7turn10search11
- База по активности для взрослых — 150–300 минут умеренной активности и 2 дня силовой работы; для удержания веса часто нужен больший объём, нередко 250+ минут/неделю. citeturn1search0turn1search1turn11search1turn11search12
- Для сна — ориентир 7–9 часов у большинства взрослых и учёт не только длительности, но и регулярности, качества и дневного функционирования. citeturn1search6turn1search18turn9search3turn9search4

**Фазовая модель**

| Фаза | Purpose | Entry condition | Exit condition | Доминирующие bottleneck’и | Что HQ должен требовать от nutrition | Что HQ должен требовать от training/activity | Что HQ должен требовать от sleep/recovery | Что запускает strategic review |
|---|---|---|---|---|---|---|---|---|
| **Подготовка и захват управляемости** | Получить минимально надёжную управляемую систему | Есть root goal и хотя бы summary-capable домены | Есть baseline, фазовая цель, owner-approved initial strategy, usable summaries 2–3 недели | Measurement gap, слишком сложный план, early adherence failure | Подготовить 1–3 реалистичных reduced-intake strategies и формат adherence summary | Дать «minimum viable training/activity template» с отчётом planned vs completed | Дать базовые green/yellow/red сигналы сна, энергии, боли | Нет usable summaries; ранние red flags; нет нисходящего тренда после стартового окна |
| **Первая клиническая веха** | Дойти до 5–10% потери массы с приемлемой устойчивостью | Baseline закреплён, initial strategy идёт | Достигнуты 118,75–112,5 кг или эквивалентная доля снижения при контролируемых recovery signals | Adherence drift, weekends, слишком агрессивный дефицит, низкая активность, recovery friction | Разобрать, удерживается ли стратегия и где ломающаяся точка | Обеспечить достижение минимального activity floor и силовой приверженности | Проверить, не начали ли сон/энергия/боль блокировать прогресс | 2–4 недели стагнации, рост боли/усталости, падение compliance, uncertainty в данных |
| **Масштабирование к целевому коридору** | Продолжать снижение от первой вехи к зоне близкой к цели без потери управляемости | Первая веха достигнута или почти достигнута | Достигнут диапазон, близкий к 95–100 кг, с сохранением operability | Adaptive slowdown, накопленная усталость, демотивация, силовой спад | Корректировать стратегию без слома adherence | Поддержать силу и увеличить contribution активности | Контролировать, что recovery не деградирует при длительном процессе | Stall > 3–4 недели, выраженный силовой спад, ухудшение сна/энергии |
| **Целевой диапазон и рекомпозиция** | Войти в 90–95 кг и сместить акцент на силу/композицию/внешний критерий | Масса достаточно близка к целевому коридору | Вход в 90–95 кг и owner-confirmed target-range strategy | Слишком быстрый темп при потере силы, конфликт «look vs performance», неверные body-comp proxies | Сместить акцент с «просто дефицит» на sustain + composition support | Выделить базовые strength markers и прогрессию, совместимую с массой | Не допускать хронического недовосстановления | Разброс метрик: вес падает, но сила/функция валятся; owner не согласен с визуальным критерием |
| **Удержание результата** | Сохранить 90–95 кг не менее 12 месяцев и не допустить скрытого рецидива | Вход в target corridor | 12 месяцев удержания по owner-approved corridor rule | Weight regain creep, ослабление самоконтроля, падение активности, response-to-lapse problems | Maintenance nutrition support, relapse prevention, response plans | Поддерживать активность и силовую основу на maintenance-уровне | Поддерживать устойчивый sleep/recovery baseline | Выход из corridor, повторяющиеся lapse cycles, drop in activity, unresolved fatigue |

**Установленное доказательное основание**

Первая фаза снижения веса логично строится вокруг **умеренной клинически значимой вехи**, а не вокруг финальной «идеальной формы»: CDC и другие источники используют 5–7%/5–10% как осмысленный ранний ориентир. После этого evidence-base делает отдельным предметом **поддержание**: monthly counseling, relapse prevention и adaptive response к колебаниям веса. Для maintenance также обычно требуется сохранять высокую физическую активность. citeturn2search0turn4search3turn4search4turn10search1turn10search4turn11search1

**Вывод проектирования**

Фазы нужны не ради красивой диаграммы, а чтобы Health HQ мог **менять доменные требования в зависимости от стадии цели**. Иначе он превращается или в «вечный weekly review», или в бесконечное повторение одних и тех же советов.

**Owner-triggered strategic review loop**

Ниже — минимальный loop, который должен быть в модели HQ. Он должен запускаться **только по owner intent**, без polling, cron и скрытого фонового процесса.

| Шаг | Что делает HQ | Замечание |
|---|---|---|
| **Intent routing** | Классифицирует запрос: today / week review / progress / bottleneck / add process | Owner trigger only |
| **Loading summary state** | Грузит только summary state по нужным доменам и последние решения HQ | Не raw logs |
| **Reviewability check** | Проверяет, достаточно ли данных/свежести/доменов для обзора | Если нет — возвращает explicit insufficiency |
| **Target vs current comparison** | Сравнивает фазовую цель и текущие summary metrics | Не просто показывает значения, а проверяет отклонение |
| **Bottleneck classification** | Выбирает главный bottleneck и степень уверенности | Например: adherence, recovery, measurement gap |
| **Strategy implication** | Формулирует, что значит bottleneck для курса | Continue / revise / hold escalation / domain review |
| **Routed domain demand** | Выпускает request в нужный домен | Non-mutating only |
| **Owner decision if needed** | Если изменение material, формулирует чёткую развилку | HQ не должен «сам решить тихо» |
| **Review/decision log** | Сохраняет короткую запись в Direction OS | Только summary of decisions/problems/next calls |
| **Next owner-facing action** | Даёт следующий управленческий шаг | Например: «утвердить вариант B питания» |

**Как эти owner queries должны маршрутизироваться**

| Owner input | Тип обзора | Ожидаемый результат |
|---|---|---|
| **«что сегодня?»** | Быстрый operational review | Сегодняшний фокус, риски, next action |
| **«разбери неделю»** | Cadence review | Недельный verdict, отклонения, главные bottleneck’и |
| **«проверь прогресс»** | Milestone/phase review | Идём ли к вехе; если нет — почему |
| **«где bottleneck?»** | Diagnostic review | Главный ограничитель и какие домены нужно дёрнуть |
| **«добавить новый процесс?»** | Governance/capability review | Нужен ли новый домен/процедура, какие boundary changes потребуются |

**Обязательная форма ответа review**

```markdown
Прогресс: on-track / at-risk / stalled / blocked / unsafe-to-escalate

Главный bottleneck:
- ...
Уверенность:
- high / medium / low

Стратегическое следствие:
- ...

Запросы в домены:
- nutrition: ...
- training/activity: ...
- sleep/recovery: ...

Решение владельца требуется:
- да / нет
- если да: развилка A/B/C

Какие метрики нужны сейчас:
- ...

Какие метрики позже:
- ...

Следующее owner-facing действие:
- ...
```

**Установленное доказательное основание**

Такой loop согласуется с доказательной логикой успешных программ: нужны самоконтроль, регулярная обратная связь, problem-solving и maintenance-focused adaptation, а не разовые советы. CDC DPP строится как длительный годовой процесс; обзоры по maintenance подчёркивают relapse prevention и adaptive responses to weight fluctuations. citeturn10search3turn10search7turn10search4turn3search0

**Вывод проектирования**

Если review loop не заканчивается явным **progress verdict + bottleneck + implication + domain demands + owner decision need + next action**, то это не orchestration, а просто commentary.

## Контракты доменов и границы безопасности

**Checklist интеграции домена через HQ**

Один и тот же контракт должен работать для nutrition, training/activity, sleep/recovery и будущих доменов.

| Поле контракта | Что обязательно |
|---|---|
| **Responsibility** | За что домен отвечает у себя |
| **Root-goal contribution** | Как именно домен влияет на снижение веса, силу, composition, maintenance |
| **Summary/report format** | Период, verdict, ключевые метрики/сигналы, blockers, requests back |
| **Exposed metrics/signals** | Только те, что домен готов надёжно возвращать |
| **Accepted request types from HQ** | Только немутационные запросы |
| **What HQ must not request** | Запрещённые классы запросов |
| **Approval-required changes** | Какие результаты доменного review нельзя менять без owner/governance |
| **Safety/recovery flags** | Что домен обязан поднимать как yellow/red |
| **Freshness / fixture / pending** | Насколько свеж источник; fixture это или live; что пока pending |

**Контракт по типам доменов**

| Домен | Responsibility | Supported root-goal contributions | Summary/report format for HQ | Exposed metrics/signals | Accepted request types from HQ | Что HQ не должен запрашивать | Что требует owner/governance approval | Safety/recovery flags | Freshness / fixture / pending |
|---|---|---|---|---|---|---|---|---|---|
| **Nutrition** | Стратегия питания, adherence support, recipe/process support | Energy deficit sustainability, satiety, recovery support, maintenance nutrition | Период, adherence verdict, главные blockers, phase-fit assessment, 1–3 proposal options | Weight-support status, adherence status, meal-structure fit, lapse pattern | Review deficit sustainability; explain stall; prepare revised options; request recipe/process support | Не переписывать тихо план; не требовать raw diary в Direction OS; не требовать unsafe deficit | Материальная смена стратегии, резкая эскалация дефицита, изменение canon processes | Excessive hunger, dizziness, persistent energy crash, rapid unexplained loss/inability to sustain | Дата диапазона, fixture/live, confidence |
| **Training/activity** | Силовая работа, активность, conditioning, progression | Strength retention/gain, energy expenditure, functional capacity, maintenance activity floor | Planned vs completed, recovery impact, bottlenecks, proposal options | Session completion, activity minutes/frequency, key movement status, soreness/pain interference | Review plan-fit; propose simpler/harder variants; adjust volume/frequency options; define baseline tests | Не требовать silent edit; не требовать unsafe escalation despite red flags; не ставить мед. ограничения | Смена базовых движений канона, material progression standard, добавление новых compulsory processes | Pain escalation, dizziness, extreme shortness of breath, severe functional drop | Дата диапазона, fixture/live, confidence |
| **Sleep/recovery** | Сон, восстановление, усталость, болевые/дневные сигналы | Constraint management, sustainability, capacity to continue deficit/load | Green/yellow/red state, top signals, interference level, review recommendation | Sleep duration/regularity status, daytime sleepiness, fatigue, pain interference | Review compatibility of current load/deficit; propose recovery options; classify escalation risk | Не требовать медицинский диагноз; не требовать «разрешить» красные симптомы без проверки | Превращение sleep/recovery в полный обязательный домен, изменяющий HQ gating | Persistent poor sleep, daytime dysfunction, rising pain, signs incompatible with escalation | Дата диапазона, fixture/live, confidence |
| **Future domain** | Любая новая специализированная функция | Только после явного описания вклада в root goal | Обязан принять тот же summary contract | Только declared signals | Только declared non-mutating requests | HQ не должен придумывать скрытые полномочия новому домену | Любое подключение нового domain class | Обязательные safety fields до включения в HQ | Обязательный статус declared/pending |

**Что значит “non-mutating request” practically**

Допустимые формулировки запроса от HQ:

- «Разобрать, совместима ли текущая nutrition strategy с phase target и recovery signals».
- «Подготовить 2 варианта упрощения training week для сохранения adherence».
- «Оценить, является ли сон/recovery ограничителем эскалации».
- «Сравнить вариант A и B по риску срыва и влиянию на силу».
- «Подготовить owner-reviewable proposal».

Недопустимые формулировки:

- «Перепиши план питания на X калорий».
- «Уменьши тренировки на 30%».
- «С сегодняшнего дня меняем фазу без owner approval».
- «Игнорируй боль, главное держать дефицит».
- «Слей сырые логи в Direction OS».

**Немедицинские safety и recovery boundaries**

В доказательной базе про движение и сон есть достаточно нормативных причин держать жёсткую границу: если во время активности появляются боль, крайняя одышка или головокружение, официальные источники советуют остановиться и обратиться за помощью; при проблемах со сном, которые регулярно повторяются или мешают дневной жизни, CDC и NHS советуют обсудить это с медицинским специалистом. HQ отсюда не получает права диагностировать, но получает право **не эскалировать** и **поднять вопрос**. citeturn6search1turn6search4turn6search12turn9search2turn6search3

| Ситуация | Что HQ может делать | Когда HQ должен остановить эскалацию дефицита/нагрузки | Когда HQ должен запросить domain review | Когда HQ должен спросить owner о проф./мед. помощи | Что HQ никогда не должен делать |
|---|---|---|---|---|---|
| **Нарастающая боль / ухудшение функциональности** | Флагировать yellow/red, пометить unsafe-to-escalate | Сразу при red; при persistent yellow тоже | Training/activity + sleep/recovery | Если симптомы нарастают, повторяются или мешают обычной жизни | Диагностировать причину боли или назначать лечение |
| **Головокружение, выраженная одышка, “не чувствую себя нормально” на нагрузке** | Считать red flag | Немедленно | Training/activity review | Да, если это повторилось или похоже на серьёзный симптом | Говорить «это нормально, продолжай» |
| **Боль/давление в груди, сочетание с одышкой, потливостью, обмороком и т.п.** | Только флаг опасности и прекращение эскалации | Немедленно | Не достаточно одного domain review | Да, прямо поднять вопрос о срочной/неотложной мед. оценке | Интерпретировать как benign, успокаивать без оснований |
| **Хронический недосып, сильная дневная сонливость, плохой сон, мешающий дню** | Пометить recovery-limiter | До разъяснения причины — да | Sleep/recovery review | Да, если регулярно повторяется или явно мешает функционированию | Назначать лечение сна |
| **Слишком быстрый или необъяснимый темп снижения** | Флагировать uncertainty / safety concern | Да, до review | Nutrition review | Да, если темп выглядит неуправляемым или сопровождается симптомами | Декларировать это автоматически как «успех» |

**Установленное доказательное основание**

- MedlinePlus по exercise safety указывает: при боли, выраженной одышке или головокружении следует остановить тренировку и обратиться за помощью. citeturn6search1
- NHS по chest pain и related symptoms подчёркивает необходимость медицинской оценки, а при симптомах, похожих на неотложные, — срочной помощи. citeturn6search4turn6search12
- CDC и NHS указывают, что регулярные проблемы со сном и плохой дневной функционал — повод поговорить с медицинским специалистом. citeturn9search2turn6search3turn6search7

**Вывод проектирования**

Safety boundary в HQ — это не медицинский модуль, а **гейт на эскалацию и маршрутизацию на review**. HQ должен уметь сказать не «что у вас за проблема», а «я не буду усиливать дефицит/нагрузку, пока это не разобрано».

## Владельческие решения и путь к следующему WHAT

**Decision-class checklist для converge-verify**

Следующая сессия converge-verify должна проверять не «есть ли какой-то код», а проходит ли дизайн по сущности.

| Проверка | Что должно быть истинно | Признак провала |
|---|---|---|
| **Positive essence** | HQ определён как goal-achievement orchestration layer | HQ описан как dashboard/reviewer/integration hub |
| **Phase/milestone model** | Есть фазы, вход/выход, первая 5–10% веха, maintenance phase | Есть только общий «progress status» без фаз |
| **Metric hierarchy** | Явно разделены now / later / pending metrics | Либо метрик почти нет, либо их бесконтрольный зоопарк |
| **Owner-triggered review loop** | Есть 10-шаговый loop и owner intents | Есть polling/cron/автообновление как ядро |
| **Domain demand contracts** | Для доменов есть structured non-mutating contract | HQ напрямую редактирует доменные артефакты |
| **Authority split** | HQ review/classify/recommend/request/route; domains execute | HQ исполняет доменную работу вместо доменов |
| **Raw-data boundary** | В Direction OS попадают summaries/decisions/problems/next calls | Direction OS хранит body/nutrition/training raw logs |
| **Safety boundary** | HQ умеет stop escalation / flag / request review / ask owner about professional input | HQ даёт медицинские интерпретации или игнорирует красные сигналы |
| **No dashboard/API/integration creep** | v0 не зависит от integrations, polling, wearables, db architecture | Проект расползается в integration program |
| **No silent domain edits** | Все запросы немутационные, изменения явно проходят через domain process | HQ тихо меняет планы |
| **Existing proof treated correctly** | `x_health_hq` признан technical evidence only | Proof объявлен product acceptance |

**Вопросы, которые должны остаться решениями владельца**

| Вопрос | Почему это owner decision | Варианты | Рекомендация |
|---|---|---|---|
| **Какие силовые движения считать baseline** | Это определяет смысл «силы» в вашем контексте и влияет на канон training domain | 1) базовые gym lifts; 2) machine/function markers; 3) hybrid | Выбрать 3–5 устойчивых и воспроизводимых маркеров, не максимум |
| **Что значит “athletic look”** | Наука не определит ваш эстетический критерий за вас | 1) только вес; 2) вес + талия; 3) визуально-силовой критерий | Зафиксировать owner-visible criterion отдельно от медицинских преимуществ |
| **Темп: быстрее худеть или больше беречь силу/энергию** | Это личный trade-off, а не универсальная истина | 1) aggressive deficit; 2) moderate sustainable; 3) strength-first slower cut | Для v0 выбрать moderate sustainable как default |
| **Когда sleep/recovery становится полноценным доменом** | Это архитектурное и governance-решение | 1) сразу; 2) when red/yellow issues recurring; 3) позже | Делать полным доменом, когда recovery реально начинает менять решения регулярно |
| **Предпочитаемая cadence owner reviews** | Это UX/operating preference владельца | 1) daily quick + weekly deep; 2) weekly only; 3) ad hoc only | Поддержать все три, но default — ad hoc + weekly deep when active phase |
| **Какие HQ requests требуют owner approval** | Это граница власти системы | 1) только phase changes; 2) все material strategy changes; 3) почти всё | Для v0: все material strategy changes и все boundary changes |
| **Какой corridor считать maintenance success** | Нужен конкретный критерий удержания | 1) жёстко 90–95; 2) живой corridor ±2 кг; 3) wider range | Для практики удержания лучше owner-approved corridor, а не одна цифра |
| **Какие источники summary считать каноническими** | Иначе HQ будет спорить с доменами о «настоящих» данных | 1) nutrition owns weight summary; 2) separate tracking summary; 3) mixed transitional | Лучше отдельный summary-source contract, чтобы избежать путаницы |
| **Нужно ли включать медикаментозные/клинические ветки в scope HQ позже** | Это радикально меняет safety и authority | 1) never in HQ; 2) advisory mention only; 3) full expansion later | Для текущего v0 — только advisory boundary, без product expansion в medical layer |

**Implementation-neutral process recommendation**

Это исследование нужно использовать как **advisory input** для Direction OS, а не как скрытое ТЗ на немедленную сборку.

| Что делать с результатом исследования | Что не делать |
|---|---|
| Перевести в owner-reviewable WHAT/canon candidate: сущность HQ, authority split, milestone model, metric hierarchy, review loop, domain contracts, safety boundary | Не считать исследование автоматически принятым определением продукта |
| Сформировать отдельный route для architecture/verify перед executor work | Не запускать реализацию напрямую из текста исследования |
| Вынести owner decisions в явный список на подпись | Не позволять executor’у «додумать» спорные вопросы по умолчанию |
| Попросить следующий implementation вернуть доказательства по checklists | Не принимать «работающий summary reviewer» как достаточно близкий результат |

**Что должно стать WHAT/canon candidate**

- Формальное определение Health HQ как orchestration layer.
- Обязательные phase/milestone objects.
- Minimum metric hierarchy with now/later/pending split.
- Owner-triggered strategic review loop.
- Domain demand contract format.
- Safety/recovery escalation boundary.
- Decision classes: advisory / approval-required / blocked.

**Что должно остаться research notes only**

- Нештатные later-phase метрики, пока не доказан decision impact.
- Спекуляции о будущем integration layer.
- Любые конкретные UI/dashboard решения.
- Любые идеи про polling/background workers.
- Конкретные training/nutrition prescriptions beyond contract logic.

**Что должно быть owner-approved до executor implementation**

- Сущность HQ.
- Authority split.
- Список обязательных метрик текущей фазы.
- Фазовая модель.
- Approval classes.
- Safety boundary.
- Canonical summary sources.

**Какой evidence должен вернуть следующий Health AI implementation**

Следующий implementation не должен возвращать «я построил нечто похожее». Он должен вернуть проверяемые артефакты:

1. Пример owner-triggered review для всех основных intent-классов.  
2. Пример phase-aware progress verdict.  
3. Пример bottleneck classification с strategy implication.  
4. Пример non-mutating routed requests по минимум трём доменам.  
5. Пример owner approval gate на material change.  
6. Пример review/decision log без raw data.  
7. Демонстрацию, что `x_health_hq` proof использован как subcomponent, а не выдан за продукт.  
8. Демонстрацию safety boundary: HQ умеет остановить эскалацию и поднять owner-facing concern, но не лечит и не диагностирует.

**Рекомендуемый следующий шаг**

Рекомендуемый следующий шаг — **сделать owner-signable WHAT/route для Health HQ v0**, в котором будет зафиксировано одно предложение сущности продукта:

> **Health HQ — это owner-triggered слой оркестрации достижения root health goal через фазы, вехи, decision-grade metрики, bottleneck-классификацию и немутационные требования к доменам, при жёсткой границе raw-data, safety и governance.**

После этого уже можно делать отдельную converge-verify сессию против checklist выше. Только после owner-signoff на WHAT/route допустим следующий executor implementation.

**Confidence level**

**Средне-высокий.** Рекомендация опирается на устойчивую доказательную базу по многокомпонентному управлению ожирением, первой клинически значимой вехе 5–10%, роли самоконтроля, потребности в maintenance и роли физической активности/силовой работы/сна как ограничителей или усилителей процесса. citeturn0search1turn4search3turn10search1turn11search1turn8search1turn9search0

**Что изменило бы рекомендацию**

Рекомендация изменилась бы, если бы выяснилось одно из следующего:

- владелец на самом деле хочет **не orchestration**, а лишь разговорный review layer;
- владелец готов отдать HQ право на **прямое редактирование** доменных артефактов;
- цель «90–95 кг и athletic look» будет заменена на более узкую клиническую или более широкую lifestyle-цель;
- появятся уже подписанные owner decisions по канону силовых маркеров, maintenance corridor и approval classes;
- окажется, что некоторые later-phase метрики уже реально меняют решения, и тогда их надо поднимать из pending в current-phase minimum.

Этот вывод остаётся **исследовательским advisory input only**. Он не определяет Health HQ автоматически, не инициализирует его и не даёт разрешения на implementation.