# Как усилить planning/intelligence layer Direction OS

## Исполнительный вердикт

По доступному GitHub-срезу видно, что актуальная система живёт в `ainazemtsau/my_global_workflow`: `AGENTS.md` прямо определяет репозиторий как **Direction OS**, указывает `os/KERNEL.md` как конституцию, `live/**` как живое состояние, а `archive/**` — как замороженные легаси-доказательства, но не авторитет. При этом в доступном срезе `os/docs` видны `DESIGN.md`, `REQUIREMENTS.md`, `RESEARCH_BASIS.md` и `STATUS.md`, а прямой запрос `os/docs/CREATIVE_EDGE_PROPOSAL.md` вернул 404; отдельный публичный доступ к `GasCoopGame` через web-снимок также не открылся. Поэтому ниже я опираюсь на доступный текущий Direction OS и внешние исследования, а не на недоступный файл-предшественник. citeturn54view0turn18view1turn24view0turn9view0

Главный вывод такой: **Direction OS уже хорошо решает задачу контроля исполнения, но пока слабо решает задачу поиска стратегии**. В ядре уже есть почти всё, что нужно для дисциплины: один чат = одна работа, шесть типов state, строгий WIP-лимит, rolling-wave, appetite до задач, evidence-only done, отдельный review через попытку опровержения, owner approval для CHARTER/TREE, а также жёсткие бюджеты на рост самой OS. Это очень сильная база. Но map/shape/review пока больше помогают аккуратно выбрать и исполнить курс, чем систематически **искать** нетривиальные, owner-specific, асимметричные и к домену правильно откалиброванные курсы. citeturn55view0turn20view1turn20view2turn25view1turn27view1

Поэтому усиливать надо **не бюрократию и не количество файлов**, а несколько маленьких процедурных механизмов внутри уже существующих plays: механизм принудительного дивергентного поиска, механизм кодирования owner-edge, механизм outside-view/forecast cards, механизм adversarial selection, механизм доменного risk profile и механизм review-калибровки. Все они хорошо ложатся на текущую философию OS, потому что могут жить в истории сессий и в `decisions_needed`, не требуя новых state file types. citeturn55view0turn27view1turn26view0

То, чего **не** надо добавлять: новый planning-layer из отдельных документов; постоянный «совет агентов»; длинные scorecards; универсальные «креативные фреймворки»; ещё один большой playbook; новые state file types; новый kernel-gate до пилота. В самом `KERNEL.md` уже зафиксировано, что «желание добавить больше структуры обычно означает, что решается не та проблема», а `MAINTENANCE.md` требует минимального изменения на один кейс за сессию. Здесь ядро право: если усиление planning требует большого нового ритуала, это почти наверняка плохое усиление. citeturn55view0turn27view1

## Что уже сильно и где именно пробел

Сильные стороны текущего дизайна понятны и подтверждаются самими файлами. `KERNEL.md` определяет строгий authority order, сессию как RAM с обязательной записью результата, два универсальных пакета `CALL`/`RESULT`, шесть типов state, девять механически проверяемых gates и абсолютные size budgets. `shape.md` уже принуждает к appetite-first, outside-view sanity-check, cut list и раннему тесту riskiest assumption; `review.md` уже принуждает к verification by refutation и tree-harvest по линзам. Это очень нетипично хорошо для персональной AI-операционной системы: здесь уже встроены защита от scope creep, от ложного «done» и от расползания системы в мавзолей мета-работы. citeturn55view0turn20view2turn25view1turn27view0

Слабое место тоже видно довольно конкретно. `map.md` просит предложить 3–6 top-level outcomes и оформить их карточками `goal / done_when / why / risk`, но не требует ни дивергентного поиска по разным стратегическим классам, ни сохранения нескольких жизнеспособных направлений до позднего этапа, ни отдельного outside-view на сами варианты. `shape.md` хорошо режет scope и формирует **один** bet, но outside view там используется только как sanity-check для размера appetite, а не как сопоставление разных стратегических вариантов. `review.md` предлагает 2–3 кандидата на следующий bet, но без отдельного прогнозного пакета, без обязательной adversarial pressure перед выбором и без цикла калибровки предыдущих стратегических прогнозов. `research.md` вообще определён как bounded child question, а не как специальный контур option search. citeturn20view1turn20view2turn25view0turn25view1

Внутренние сигналы из репозитория подтверждают именно этот диагноз. `FRICTION.md` фиксирует, что в первом пилоте дерево было сформировано без участия владельца и без обоснований, тогда как владелец ожидал со-творчества глобальных планов; это и было исправлено через G9, map play и обязательный `why`. `STATUS.md` дополнительно говорит, что дерево текущего направления пока «болванка», а после setup-бета владельцу нужен настоящий map-чат как «настоящее планирование карточками узлов». Иными словами: execution-control слой уже проектно осмыслен, а strategic map layer ещё в фазе становления. citeturn25view3turn45view0

Внешняя литература хорошо объясняет, почему обычный chat-planning тут проседает. Люди и модели рано фиксируются на первых идеях; при отборе люди систематически предпочитают более осуществимые и желательные варианты ценой оригинальности; LLM-помощь часто повышает локальную креативность отдельного пользователя, но уменьшает коллективное разнообразие идей; а современные работы по LLM-идеации прямо указывают на две ключевые проблемы: **низкое разнообразие генераций** и **провалы self-evaluation**. Отсюда следует, что Direction OS сейчас не столько «слишком слаб в креативности», сколько **слишком мало структурирует сам поиск вариантов и сам отбор между ними**. citeturn49view0turn39search0turn39search5turn38view2turn38view0

Если формулировать кратко: сейчас OS — отличный **control plane**, но ещё не полноценный **search plane**. Для competitive directions это означает риск застывать в правдоподобном, но усреднённом плане. Для safety-sensitive directions это означает другой риск: красивый и гладкий план может маскировать недостаточную доказательность или плохую калибровку риска. Чтобы закрыть оба риска сразу, нужны механизмы, которые делают поиск шире, отбор жёстче, а профиль риска — доменно-зависимым. citeturn36view0turn35view2turn47view1turn47view0

## Ранжированный набор механизмов

### Контур асимметрий

**Что решает.** Этот механизм нужен для того, чтобы стратегия рождалась не из усреднённого «best practice», а из сочетания **owner-specific means** и конкретного пространства рычагов в данной ситуации. Без этого LLM почти неизбежно даёт «хороший совет для среднего стартапа». Логика effectuation прямо рекомендует начинать с «кто я / что знаю / кого знаю», а не с абстрактной идеальной цели; исследования по solo ventures и small teams дополнительно показывают, что маленькие команды и даже соло-основатели нередко выигрывают не числом, а более высокой скоростью, меньшими координационными потерями и более disruptive search pattern. citeturn52search1turn52search9turn34view1turn53search1turn53search19

**Куда встраивать.** Лучшее место — `map`, `shape` и очень короткое расширение `CHARTER.md`. Не новый файл, а маленький блок в CHARTER уровня «means_at_hand / unfair_edges / hard_limits». В state хранится только компактная память об этих means; подробности живут в истории сессий. Это соответствует текущей архитектуре: медленное состояние в CHARTER, живая детализация в history. citeturn55view0turn26view0

**Процедурная форма.** В начале planning-сессии агент обязан восстановить 3–5 пунктов owner-edge: навыки, связи, доступы, taste edge, distribution edge, prior work, доступные AI-рычаги, а также 3–5 hard limits. Затем агент обязан выделить 3–5 стратегических рычагов текущей ситуации: wedge сегмента, канал дистрибуции, pricing/business model, partnership, product/tech leverage, data/AI leverage, speed-based wedge. После этого он не предлагает «просто лучший план», а строит 4–7 option cards, где каждая карточка явно говорит: **какой owner-edge используется, какой blind spot крупного игрока эксплуатируется, какой быстрый falsifying signal проверит гипотезу, и какой downside cap удерживает ставку**. Минимум одна карточка должна быть «weird/high-upside», минимум одна — «boring/probable», если доменный risk profile это допускает. Это уже не общий brainstorm, а структурированный поиск асимметрий. Поддерживающая идея из design-by-analogy полезна здесь же: хотя бы одна карточка должна быть вдохновлена **far-field** аналогией, потому что именно дальние и менее распространённые аналоги повышали novelty решений в исследованиях по design ideation. citeturn36view2turn32search8turn52search1turn53search1

**Ожидаемая польза.** Для solo-owner, усиленного агентами, это, вероятно, самый важный механизм: большие компании обычно сильнее в development of existing trajectories, а не в поиске узких disruptive wedges; исследования по командам в науке и технологиях как раз показывают, что маленькие команды чаще создают disruptive вклад, а большие — развивают уже популярные линии. Значит, Direction OS должен сознательно искать не только «оптимальный план», но и **стратегические места, где маленькость — преимущество**. Это не романтика weirdness, а конкретная конкурентная логика. citeturn53search1turn53search19turn47view0

**Слабые места и как убить.** Риск здесь в шаблонном «натягивании асимметрии», когда агент просто придумывает фальшивые edges. Ещё один риск — чрезмерный локализм: система может слишком заякориться на текущих средствах и перестать видеть более амбициозные траектории. Поэтому kill-правило должно быть жёстким: если после трёх planning-сессий карточки оказываются семантически почти одинаковыми или owner consistently оценивает их как «общие слова, просто переименованные», механизм удаляется или упрощается. citeturn38view0turn49view0

**Минимальный patch sketch.** В `os/plays/map.md` после `Recite` добавить короткий шаг `Edge recite`; в `Candidate cards` добавить поля `edge_used`, `blind_spot`, `fast_signal`, `downside_cap`. В `os/plays/shape.md` до `Minimal solution` вставить одно правило: если у узла есть ≥2 правдоподобных стратегических реализации, их надо показать owner’у карточками до выбора одного. В `CHARTER.md` — только один новый небольшой блок про means/edges. Сам `KERNEL.md` на первом проходе лучше не трогать. citeturn20view1turn20view2turn55view0

### Дивергентный first-pass до оценки

**Что решает.** Это прямой ответ на две проблемы сразу: design fixation и LLM homogeneity. Современные работы показывают, что независимые LLM-сэмплы склонны быть менее разнообразными, чем человеческие, потому что модель фиксируется на ранних выходах и тянет генерацию к единому распределению знаний; при этом targeted prompting может повысить diversity. Другая свежая линия показывает, что при parallel ideation простая «накидка нескольких ответов» часто создаёт *illusion of exploration*: кажется, что вариантов много, но они сидят в одном семантическом бассейне. А недавний анализ multi-agent dialogues для ideation показывает, что большее разнообразие ролей и critic-side heterogeneity увеличивают разнообразие и feasibility идей. citeturn38view0turn38view1turn37view1turn47view3

**Куда встраивать.** Это не новый play, а режим работы внутри `map`, `shape` и, при необходимости, `research` через `call:research`. Ключевой structural point: **генерация и оценка должны быть разнесены**. Сначала — дивергенция, потом — кластеризация, потом — выбор представителей, и лишь затем — judgment/recommendation. Это тот случай, где не «попросить модель быть креативной», а буквально изменить topological order шагов. citeturn25view0turn20view1turn20view2turn38view2

**Процедурная форма.** Сессия planning должна сначала сделать blind generation pass: 4–8 независимых генераций, которые **не видят друг друга**. Их можно получить либо последовательными prompt-runs с разными criteria/persona/semantic directions, либо 2–4 bounded research children с очень маленьким бюджетом. Основания для diversification должны быть не случайными, а привязанными к задаче: разные values/criteria, разные search directions, разные user segments, разные asymmetry hypotheses. Затем агент обязан сгруппировать идеи в 3–5 семантических bins и выбрать по одному представителю из каждого. Пока не появилось как минимум три реально разных bins, recommendation запрещена. Только после этого начинается оценка. Для творческих и конкурентных направлений полезно добавить one-shot “semantic direction stratification” — отдельный planning call, который сначала придумывает broad semantic directions, а уже потом порождает варианты внутри них; в работе 2026 года именно этот режим дал лучший diversity–quality–compute frontier среди проверенных anchorless методов. citeturn38view1turn38view0turn47view3turn38view3

**Ожидаемая польза.** Это один из самых надёжных способов уменьшить «генерик от LLM». Исследование Si, Yang и Hashimoto показало, что современные LLM могут давать очень novel идеи, но страдают от слабой feasibility и низкого diversity, а также плохо self-evaluate. Отсюда практический вывод: модель нельзя оставлять в режиме «сама придумала, сама оценила, сама рекомендовала»; ей нужно искусственно расширять поисковое пространство до начала отбора. Плюс, если верить работе Doshi и Hauser, AI-помощь действительно повышает креативность отдельно взятого пользователя, но за счёт сужения коллективного разнообразия; значит, Direction OS должен защищать diversity процедурно, а не надеждой на температуру. citeturn38view2turn39search0turn39search5

**Слабые места и как убить.** Главная опасность — превратить всё в дорогой «цирк персон». Если персоны фиктивны, а search directions не различаются по сути, получится токеновый шум. Kill-правило простое: если два пилота подряд дают почти дубликаты или owner не видит реального расширения option space, механизм сворачивается до более простого правила «3 независимых passes + binning», без elaborate multi-agent theatrics. citeturn38view0turn38view1turn38view3

**Минимальный patch sketch.** В `map.md` и `shape.md` добавить одно правило вида: «before recommendation, run a divergence pass with ≥4 independent variants across ≥3 search directions; cluster; compare representatives only». В `research.md` можно не менять ядро текста, а лишь явно разрешить такой `return format` для child-calls. Ядро и state types трогать не надо. citeturn20view1turn20view2turn25view0turn55view0

### Карточка внешнего вида и прогноза

**Что решает.** Сейчас `shape.md` уже требует outside-view sanity-check, но только для appetite sizing; этого мало. Для хорошего стратегического выбора нужен не просто список опций, а **forecast card на каждую финальную опцию**: reference class, base rate, вероятность уложиться в appetite, earliest credible signal, main uncertainty, и что именно изменит мнение. Это не для «магии цифр», а чтобы у owner-а был не просто совет, а сравнение вариантов с outside view. Исследования по reference class forecasting показывают, что метод специально создавался для снятия optimism bias и strategic misrepresentation; moreover, Hong Kong case показывает практическое применение на большом сравнительном наборе и явную связь с risk appetite decision-makers. citeturn35view2turn30search17

**Куда встраивать.** В `shape` перед owner decision и в `review` после результата. В state не надо писать длинную карточку; она живёт в history/RESULT и компактно отражается в `decisions_needed`. Текущая архитектура packets уже это позволяет без новых сущностей. citeturn55view0turn25view1

**Процедурная форма.** На 2–3 финальные опции делается маленькая forecast card: `reference_class`, `inside_view`, `p(done_when within appetite)`, `earliest_signal_date`, `failure_modes`, `what_would_change_my_mind`. Числа разрешены только диапазонами или вероятностями с оговорками, а не мошенническими точками. Для competitive directions reference class может быть грубым: похожие релизы, похожие acquisition motions, похожие каналные эксперименты. Для safety-sensitive domains reference class должен опираться на внешние, авторитетные или клинические/регуляторные evidence sources. Наконец, recommendation не должна быть просто «лучший вариант», а «лучший вариант при текущем risk profile и current evidence». citeturn35view2turn35view1turn44search0turn44search1

**Доказательная база.** Здесь есть сильная поддержка из forecasting science. Good Judgment Project показал, что лучшие forecasters были точнее и быстрее учились по мере появления новой информации; они чаще обновляли оценки, больше делились источниками и активнее задавали уточняющие вопросы. Работа Ferreiro и соавторов дополнительно показывает, что **compromise forecasts** — агрегированные прогнозы — могут повышать точность на реальных данных GJP. Для Direction OS отсюда следует практический урок: bet-selection выигрывает не от «уверенной рекомендации», а от сравнимых, обновляемых и при необходимости агрегируемых прогнозных карточек. citeturn50view0turn50view1turn44search0turn44search1

**Слабые места и как убить.** Основная опасность — псевдоточность и плохой reference class. Если аналогов нет, карточка должна честно говорить «base rate unknown; only local signal plan is credible». Если за 3–5 shape-сессий owner ни разу не использует forecast cards для реального выбора, механизм либо слишком тяжёлый, либо плохо формулируется — его надо упростить до `outside_view + earliest_signal + failure_modes`. citeturn35view2turn49view0

**Минимальный patch sketch.** В `os/plays/shape.md` после шага про appetite вставить пункт `Finalist forecast cards — 2–3 options, outside view + probability range + earliest signal + what would change the answer`. В `review.md` — короткий `forecast check` сразу после verification step. Kernel пока не менять. citeturn20view2turn25view1turn55view0

### Пакет враждебного отбора

**Что решает.** Это механизм против sycophancy, business-book genericity и слишком гладкого выбора. Внутри текущего OS review уже построен как refutation after work. Но до commit в bet такого же процедурного давления пока нет. Между тем premortem давно является признанным способом поднять выявление причин провала, а литература по devil’s advocacy / dialectical inquiry в стратегическом decision making существует десятилетиями и показывает, что structured conflict может улучшать качество стратегических решений, хотя и не бесплатно по социальным издержкам. Современные LLM-исследования тоже указывают, что self-evaluation у моделей слабое место; значит, отбор нельзя оставлять в мягком режиме «модель слегка покритикует себя сама». citeturn29search2turn29search6turn29search1turn41search1turn38view2

**Куда встраивать.** Прямо в `shape` между появлением finalist options и owner decision. В `review` у вас уже есть refutation after the fact; здесь нужен refutation before commitment. Это не отдельный red-team play: слишком тяжело. Это просто обязательный шаг внутри shape. citeturn20view2turn25view1

**Процедурная форма.** На каждую финальную опцию делается короткий attack memo из двух частей. Первая часть — premortem: «представь, что через X срок ставка провалилась; почему именно?» Вторая — counter-case: «если эта опция ошибочна, какая из альтернатив выигрывает и по какому switch trigger мы бы это поняли?» Минимум одна атака должна идти из market/user lens, минимум одна — из execution/safety/constraint lens. Owner в `decisions_needed` видит не только recommendation, но и strongest case against recommendation. Это резко снижает вероятность того, что очевидный план пройдёт без столкновения с лучшим контрпланом. citeturn25view1turn29search2turn47view1

**Ожидаемая польза.** Для competitive directions это увеличивает шанс найти скрытый failure mode до входа в ставку. Для health и других safety-sensitive domains польза ещё выше: там HRO-подход прямо требует preoccupation with failure, reluctance to simplify и deference to expertise. Иначе говоря, творческий поиск допустим, но commit должен проходить через более жёсткую враждебную проверку. citeturn47view1

**Слабые места и как убить.** Плохой сценарий — endless negativity или риторический театр. Если attack memo не выводит на decision-changing risks и только раздражает owner-а, его надо сократить до одного premortem + одного switch trigger. Kill-правило: если механизм три shape-сессии подряд не обнаруживает ни одного нового существенного риска и не меняет выбор/kill criteria, оставить только premortem на guarded/safety-critical профилях. citeturn29search1turn29search2

**Минимальный patch sketch.** В `shape.md` после finalist options добавить шаг `Attack memo — premortem + best counterplan + switch trigger`. В `review.md` ничего радикально менять не нужно: он уже умеет refutation и add-back check. citeturn20view2turn25view1

### Профиль риска по домену

**Что решает.** Пользовательская формулировка очень точна: OS не должен «просто делать рискованные планы», он должен **по домену решать, когда быть дерзким, а когда становиться evidence-heavy и консервативным**. Сейчас такого явного механизма нет: `KERNEL` содержит сильные общие gates, но не вводит переменную, которая меняет burden of proof по признакам домена. Для этого нужен короткий risk profile, основанный на reversibility, downside radius, latency of harm, legal/trust exposure и наличии внешней evidence base. Здесь особенно полезно сочетание трёх источников: Bezos о reversible vs irreversible decisions, effectuation об affordable loss, и HRO-подходы для safety-critical систем. citeturn47view0turn35view3turn34view2turn47view1

**Куда встраивать.** В `shape`, а источник правды о tolerances может жить в `CHARTER constraints`. Новый state type не нужен. В большинстве случаев достаточно короткой классификации bet-а в начале shape и явного указания профиля в summary to owner. citeturn55view0turn20view2

**Процедурная форма.** Предлагаю четыре профиля.  
**Explore**: обратимо, downside локален, harm detected quickly. Здесь разрешены weird/high-upside options, если есть affordable-loss cap и быстрый falsifying signal.  
**Venture**: обратимо не полностью, но основной downside — время/деньги владельца. Здесь обязательны forecast cards, attack memo и жёсткий `kill_by`, но можно идти быстрее, с 60–70% информации, если можно быстро course-correct.  
**Guarded**: возможен вред пользователю, удар по доверию, legal/externality risk или delayed harm. Здесь дивергентный поиск остаётся, но commit требует внешней evidence base, более консервативного thresholds и часто — `guide`/внешнего человеческого действия вместо прямого AI-driven execution.  
**Safety-critical**: здоровье, медицина, серьёзные финансы, регуляторика, необратимые последствия. Здесь creativity смещается из object-level intervention в дизайн сбора доказательств, маршрутизации, комплаенса и проверок; прямой bold bet без авторитетной evidence base не допускается. Это не новый bureaucracy layer, а переключатель evidence burden. citeturn47view0turn47view1turn35view3turn43search17

**Ожидаемая польза.** Этот механизм сразу решает конфликт между «мы хотим выигрывать асимметрией» и «мы не хотим дурной бравады в health». Для reversible bets Amazon-подобная логика high-velocity decisions уместна; для domains, где ошибки накапливают harm or trust debt, логика high reliability уместнее. В effectuation terms это означает: boldness допустима, пока downside ограничен тем, что реально afford to lose; когда downside вылезает за рамку owner-only loss, нужен другой режим. citeturn47view0turn47view1turn35view3turn34view2

**Слабые места и как убить.** Самый большой риск — overclassification: всё объявить safety-sensitive и парализовать систему. Второй риск — формальная классификация без реального изменения поведения. Значит, kill-правило такое: если profile не меняет ни evidence burden, ни выбор, ни тип next task, он лишний и должен быть удалён или упрощён. citeturn47view1turn55view0

**Минимальный patch sketch.** В `shape.md` перед option comparison добавить `Risk profile — explore | venture | guarded | safety-critical` с короткими критериями. В `CHARTER.md` можно добавить только одну строку про non-negotiable downside boundaries. `KERNEL.md` пока лучше не расширять новым gate: сначала пилот. citeturn20view2turn55view0

### Калибровочный хвост в review

**Что решает.** Без калибровки прогнозов planning не учится. Сейчас `review.md` отлично делает verified verdict, harvest, add-back check и next-bet selection. Но он не обязан сравнивать **ожидания planning-сессии** с тем, что реально произошло. Это упущение: superforecasting-literature подчёркивает частые обновления, learning rate и accountability; aggregation work показывает, что forecasting accuracy улучшается не разовым «угадыванием», а дисциплиной сравнения ожиданий с исходами. citeturn25view1turn50view0turn50view1turn44search0

**Куда встраивать.** Просто в `review.md`, сразу после `Verify by refutation`, как короткий `forecast check`. Никаких новых файлов. Из state достаточно одной строки в LOG или короткого history block; в `knowledge/` отправляются только действительно повторяющиеся паттерны. Это уже соответствует текущему принципу knowledge entries: только то, что кто-то потом прочтёт. citeturn25view1turn55view0

**Процедурная форма.** Review должен отвечать на четыре вопроса:  
какой был ex ante probability range;  
когда ожидался earliest signal;  
что реально произошло;  
какой именно surprise class случился — optimistic, pessimistic, wrong-mechanism, wrong-timeline.  
Дополнительно стоит увязать это с existing add-back check: если прогнозы систематически промахиваются в сторону «недооценили hidden work», cuts, возможно, были слишком агрессивны; если наоборот ничего не было missed, cuts могли быть слишком timid. Это сделает `review` не только судом, но и тренажёром качества shaping. citeturn25view1turn35view1turn44search1

**Ожидаемая польза.** По сути это дешёвый способ со временем вырастить в OS локальный forecasting memory без нового memory-bank. Особенно это важно для будущих неизвестных directions: качество системы будет расти не потому, что она запомнила «лучший фреймворк», а потому, что она накопила patterns of over- and underestimation в собственном workflow. citeturn50view0turn50view1turn55view0

**Слабые места и как убить.** Риск здесь в low-signal small-N learning: можно начать видеть закономерности в шуме. Поэтому в `knowledge/` должны попадать только повторяющиеся и operationally useful patterns; разовые surprises остаются в history/LOG. Если за 5 review-сессий forecast check нигде не повлиял на последующий shape, он слишком декоративен и должен быть сокращён. citeturn25view1turn55view0

**Минимальный patch sketch.** В `review.md` после шага 1 вставить короткий шаг `Forecast check`; в `LOG.md` можно добавлять очень компактную пометку вроде `forecast_surprise: low|med|high`, если это реально полезно, но и это можно сначала держать только в history. citeturn25view1turn55view0

### Дальний аналог как опциональный spark

**Что решает.** Это не базовый механизм, а дешёвый ускоритель именно для creative/competitive направлений. Исследования по design-by-analogy показывают, что far-field и less-common examples повышают novelty идей, но одновременно несут риск fixation, если ими пользоваться неосторожно. Значит, дальний аналог лучше использовать не как главный источник решения, а как **обязательный контрастный источник одного из option cards** внутри уже защищённого дивергентного процесса. citeturn36view2turn32search13turn32search2

**Куда встраивать.** Через `call:research` из `map` или `shape`, только когда direction competitive/creative и risk profile не safety-critical. Для health, legal, high-downside domains это не object-level guide, а максимум source of hypothesis for further evidence gathering. citeturn25view0turn47view1

**Процедурная форма.** Parent session запускает bounded child: «принеси один near analogy, один far analogy и один anti-analogy; верни по одной стратегической карточке из каждого». После возврата parent не обязан выбирать их, но обязан сравнить с собственными вариантами. Это дешёво, потому что не требует постоянного creativity ritual; и безопасно, потому что работает как input to search, а не как direct execution instruction. citeturn25view0turn36view2

**Слабые места и как убить.** Если analogies repeatedly дают только красивую упаковку той же идеи, механизм не окупается. Я бы вводил его только как conditional tool, а не как обязательный шаг каждого shape. citeturn36view2turn32search13

**Минимальный patch sketch.** Вообще можно обойтись без изменений OS: просто описать как рекомендуемый `call:research` pattern в maintenance discussion. Если же закреплять — то одной строкой в notes `map.md` и `shape.md`. citeturn20view1turn20view2

## Контур planning edge loop

Ниже — тот цикл, который, на мой взгляд, лучше всего сочетается с существующей философией Direction OS и не требует новой бюрократии.

1. **Ambition / frame.** Владелец формулирует направление и root success criteria; CHARTER фиксирует mission, constraints, lenses и компактный owner-edge block. `frame` не пытается заранее построить глубину — он лишь задаёт корень и правила игры. citeturn55view0turn26view0

2. **Map как поиск, а не только раскладка дерева.** `map` начинает с edge recite, затем делает divergence-first pass, затем строит 4–7 cards across distinct search directions. Owner approving cards по одной сохраняется, потому что G9 — сильная часть дизайна и её ломать не надо. Но recommendation появляется только после того, как реально видны разные стратегические классы, а не первый правдоподобный план. citeturn20view1turn55view0turn38view0turn38view1

3. **Research как поисковый форсаж.** Не каждый раз, но когда нужен контраст, `map` или `shape` запускает 1–3 bounded research children: для far analogy, reference class, market/user evidence, competitor blind spot или special-risk evidence. `research.md` уже допускает дочерние bounded questions и не трогает state — это делает механизм дешёвым и совместимым с «один чат = одна работа». citeturn25view0turn55view0

4. **Shape как выбор ставки из финалистов.** Перед commit в bet показываются 2–3 finalist options, каждая с forecast card и attack memo. Затем выбирается один bet, и уже только на нём работают existing appetite, cut list, lens sweep, RAT-first, kill_by и ≤3 active tasks. Иначе говоря, текущий отличный shape остаётся, но на вход получает более сильный selection layer. citeturn20view2turn25view1turn35view2turn29search2

5. **Work and evidence.** Здесь существующий OS почти ничего не должен менять: выполнение остаётся bounded, evidence-driven, with separate review later. Это достоинство дизайна, а не проблема. citeturn55view0

6. **Review как суд и обучение.** `review` сначала опровергает done_when, потом делает forecast check, потом harvest per lens, затем tree diff, add-back check и next selection. Критично, что review должен не только сказать «сработало/не сработало», но и научить следующий shape: где прогноз был слаб, где option search был узок, где risk profile был ошибочно мягким или жёстким. citeturn25view1turn50view0turn44search0

7. **Map / shape refresh.** Если learning меняет несколько узлов, route обратно в `map`; если меняется только следующий bet — достаточно нового `shape`. Это уже соответствует существующему дизайну: крупная реструктуризация идёт в map, локальный commit — в shape. citeturn20view1turn25view1

Коротко: Direction OS не нужно превращать в «более умную планёрку». Ему нужен **короткий search–selection–calibration loop поверх уже хорошего execution loop**. citeturn55view0turn26view0

## Модель доменного риска и защита от generic LLM output

### Как одному и тому же OS различать смелые и консервативные режимы

Я бы рекомендовал не делать универсальный «risk score», а использовать **четыре режима поведения**, потому что owner-решения удобнее принимать категориями, чем гладкими числами. Основание у этой схемы комбинированное: reversible vs irreversible decisions из Amazon-подхода, affordable loss из effectuation и HRO-principles для высокорисковых доменов. citeturn47view0turn35view3turn47view1

**Explore.** Обратимые действия, локальный downside, быстрый feedback loop. Здесь поощряется асимметрия, weirdness, high variance и быстрые probes; достаточно bounded affordable loss, простого outside view и раннего falsifying signal. Это тот режим, в котором solo owner действительно может выиграть у компании скоростью и неортодоксальным search. citeturn47view0turn35view3turn53search1

**Venture.** Ставка всё ещё в основном про время/деньги владельца, но уже не совсем безобидна. Здесь обязательны divergence pass, forecast cards, attack memo и чёткий `kill_by`. Bold options остаются допустимыми, но только если проигрыш ограничен тем, что реально afford to lose. citeturn35view3turn34view2turn35view2

**Guarded.** Есть заметный риск пользователю, доверительному капиталу, юридической позиции или delayed harm. Здесь OS должен становиться evidence-heavier: внешние источники обязательны, weird options могут жить в search-space, но default commit должен быть консервативнее, чаще через `guide`/человеческое действие, а не через прямой object-level execution агента. citeturn47view1turn55view0

**Safety-critical.** Здоровье, клинические советы, сильная регуляторика, необратимый вред. В этом режиме planning edge должен смещаться с «смелой продуктовой стратегии» на «смелый дизайн проверки, маршрутизации и evidence collection». HRO-подходы здесь особенно релевантны: preoccupation with failure, reluctance to simplify, sensitivity to operations и deference to expertise. В практическом смысле это означает: creative search разрешён на уровне гипотез и проверки, но не на уровне необоснованного воздействия. citeturn47view1

### Конкретные контрмеры против generic LLM output

Первое правило: **нельзя позволять одной и той же когнитивной фазе одновременно генерировать, оценивать и рекомендовать**. Работа Si et al. прямо указывает на проблемы LLM self-evaluation, а новые исследования разнообразия идей показывают, что модели фиксируются и сужают пространство вариантов. Поэтому в OS должны быть разнесены по шагам: generation, clustering, evaluation, recommendation. citeturn38view2turn38view0

Второе правило: **ни одной recommendation до тех пор, пока нет минимум трёх семантически разных bins вариантов**. Это самый дешёвый и самый эффективный structural antidote против «кажется, вариантов много, а по сути все об одном». Исследования по anchorless diversification и criteria-based prompting прямо говорят, что diversity extraction требует специальных процедур, а не просто «ещё пять сэмплов». citeturn38view1turn47view3

Третье правило: **каждая option card обязана привязываться к owner-edge и blind spot конкурента**. Generic idea почти всегда маскируется отсутствием конкретного ответa на два вопроса: «почему именно ты?» и «почему большой игрок этого не делает?» Если карта не отвечает на них, она почти наверняка общая. Этот приём естественно следует из bird-in-hand/effectuation и из логики disruptive advantage маленьких команд. citeturn52search1turn34view1turn53search1

Четвёртое правило: **на финальном этапе обязательны хотя бы один outside-view факт и один source of market/user evidence**, а не только reasoning itself. Reference class forecasting, superforecasting и даже current OS philosophy сходятся в одном: reasoning без внешнего сигнала слишком легко становится гладким самообманом. citeturn35view2turn35view1turn55view0

Пятое правило: **для competitive/creative bets хотя бы одна карточка должна приходить из far analogy или explicitly weird search direction**. Design research показывает, что дальние и uncommon analogies помогают с novelty; без этого модель и человек вместе слишком легко сваливаются в локальный optimum уже знакомых траекторий. Но это правило должно быть conditional: не для safety-critical domains. citeturn36view2turn32search13turn47view1

Шестое правило: **в review должны сохраняться не только выводы по выбранной ставке, но и причины, почему были отвергнуты альтернативы**. Иначе система теряет diversity-memory и постоянно переоткрывает одни и те же варианты по кругу. Это можно хранить не в новом state file, а в history/RESULT и, если надо, в кратком parked-note внутри TREE. citeturn55view0turn20view1

## Что не добавлять

Не стоит добавлять **новый planning state file** вроде `PLAN.md`, `STRATEGY.md`, `OPTIONS.md` или отдельный memory-bank для идей. В Direction OS уже есть жёсткое ограничение на шесть типов state и прямой запрет на speculative structure. Лучшая форма для planning artifacts здесь — временный материал в истории сессии и в `decisions_needed`, а не новый долговечный контейнер. citeturn55view0turn27view1

Не стоит добавлять **постоянный multi-agent swarm** или тяжёлый «совет ролей» на каждый planning-session. Современная литература по LLM creativity действительно показывает плюсы role heterogeneity, но выигрыш даёт конкретная структура дивергенции и критики, а не само по себе умножение агентов. Если закрепить swarm как норму, система почти наверняка вырастет в meta-work and token burn. Для вашей OS это особенно опасно, потому что весь дизайн уже специально борется с «workflow-governance как отдельным направлением». citeturn38view3turn37view1turn26view0turn27view1

Не стоит добавлять **длинные scorecards и псевдоматематику**. Исследования по idea selection прямо показывают tension между originality и feasibility; если это tension затереть в один искусственный composite score, получится ложная точность, а не лучшее решение. Делайте маленькие forecast cards и явные trade-offs, а не большие таблички на 20 критериев. citeturn49view0turn35view2

Не стоит добавлять **“boldness by default” как ценность системы**. Для mutable, reversible, local-downside bets это разумно; для guarded и safety-critical domains — нет. Здесь creativity должна жить в hypothesis search, experiment design, evidence routing, but not in reckless action. Иначе OS потеряет одну из своих сильных сторон — способность быть trustworthy, а не только energetic. citeturn47view0turn47view1turn55view0

Не стоит менять **KERNEL первым**. Почти все сильные улучшения planning можно проверить на уровне `map.md`, `shape.md` и `review.md`, не создавая новый gate и не раздувая конституцию. Это идеально совпадает с вашим maintenance-подходом: один механизм — одна maintenance session — smallest possible fix. citeturn27view1turn55view0

## Пилот, patch-level suggestions и ограничения

### Небольшой пилот без правки `os/**`

Лучший способ проверить идеи — не спорить на уровне принципов, а провести **три ручных planning-пилота** на ближайших настоящих direction-jobs. Первый пилот: следующий `map` или перепланировка карты прогоняется с `контуром асимметрий` и `divergence-first pass`; выход сравнивается с обычным map по четырём метрикам: число реально разных option bins, owner-rated specificity, owner-rated surprise/usefulness и ясность next node. Второй пилот: следующий `shape` делается на 2–3 финалистах с forecast cards и attack memo; метрики — изменился ли выбор, sharpened ли decision, стало ли понятнее `kill_by`. Третий пилот: первый последующий `review` делает forecast check и явно фиксирует, что оказалось неожиданным. Если к концу трёх пилотов owner скажет «варианты стали реально разнее, выбор стал осмысленнее, а добавленная тяжесть мала», механизм достоин maintenance-правки. Если нет — его не надо романтизировать. citeturn25view1turn20view2turn27view1

Я бы мерил пилот очень приземлённо. Не Brier score как фетиш, а пять вопросов:  
появились ли варианты, которые раньше система бы не предложила;  
стало ли яснее, почему выбран именно этот bet;  
изменился ли выбор после outside view / attack memo;  
вписался ли дополнительный planning overhead в разумный бюджет;  
есть ли хоть один реальный learning signal в review.  
Если хотя бы 3 из 5 не улучшились — не вносить механизм в OS. Это соответствует вашему подходу «убивать лишнее» и не превращать workflow в идеологию. citeturn55view0turn27view1

### Патчи, с которых я бы начал

**Самый сильный первый maintenance-кейс** — `os/plays/shape.md`. Именно там сейчас происходит commit из стратегии в bet, и именно там недостаёт strongest selection layer. Я бы добавил туда только три маленьких вставки:  
перед `Minimal solution` — `Finalist options` с требованием показать 2–3 разные реализации, если у узла есть множественность путей;  
после этого — `Forecast cards`;  
после этого — `Attack memo`.  
Ни новых файлов, ни новых packet types, ни нового gate в kernel на первом шаге. citeturn20view2turn55view0turn27view1

**Второй maintenance-кейс** — `os/plays/map.md`. Там я бы изменил не философию co-creation, а только шаги до recommendation: вставить `Edge recite`, затем требование к cards покрывать разные search directions, а в саму карточку добавить `edge_used`, `blind_spot`, `fast_signal`. Это даст owner-specific planning, не ломая G9 и не усложняя tree semantics. citeturn20view1turn55view0

**Третий maintenance-кейс** — `os/plays/review.md`. Добавить один абзац `Forecast check` сразу после `Verify by refutation`, а в `Select next` закрепить правило: когда это уместно, next candidates должны идти из разных lenses/search directions, а не быть тремя вариантами одного и того же курса. Это почти ничего не стоит, но закрывает калибровочную дыру. citeturn25view1

**Что я бы сознательно не трогал на старте.** `KERNEL.md`, количество file types, packet schema, `pulse.md`. Все они уже выполняют свою работу хорошо; planning edge можно нарастить на уровне plays. Только если через несколько maintenance-циклов станет ясно, что shape/map changes реально помогают, можно обсуждать, заслуживает ли какой-то из механизмов статуса hard gate. citeturn55view0turn25view2turn27view1

### Открытые вопросы и ограничения

Главное ограничение этого исследования — доступный набор внутренних артефактов. В публично доступном срезе я смог прочитать `AGENTS.md`, `os/KERNEL.md`, `map/shape/research/review/pulse`, `REQUIREMENTS.md`, `DESIGN.md`, `RESEARCH_BASIS.md`, `FRICTION.md`, `MAINTENANCE.md` и `STATUS.md`; но `os/docs/CREATIVE_EDGE_PROPOSAL.md` в этом срезе не открылся, а `GasCoopGame` не был публично доступен. Поэтому я не утверждаю, что полностью опроверг или подтвердил тот prior proposal; я скорее даю набор механизмов, который совместим с текущим Direction OS и лучше опирается на внешнюю evidence base. citeturn24view0turn18view1turn9view0turn45view0

Второе ограничение — сила доказательств неоднородна. По forecasting, reference classes, idea selection bias, LLM diversity collapse, effectuation/affordable loss и safety-oriented organizing evidence достаточно сильное. По прямому влиянию именно такой OS-процедуры на outcomes solo founder across arbitrary domains — evidence, конечно, более косвенное: это перенос лучших механизмов из нескольких исследовательских традиций, а не уже готовый RCT на Direction OS. Поэтому я бы внедрял всё только через маленькие play-level пилоты с быстрым kill switch. citeturn35view2turn35view1turn49view0turn38view0turn47view1turn27view1

Мой итоговый ranking, если нужно ужать всё до одного предложения: **сначала усиливайте `shape` через finalist options + forecast cards + attack memo; потом усиливайте `map` через owner-edge + divergence-first search; затем добавляйте review calibration; risk profile держите как лёгкий behavioural switch, а не как новую бюрократию**. Это даст Direction OS самый высокий шанс стать не просто аккуратной системой исполнения, а системой, которая действительно ищет и отбирает планы уровня «solo owner + AI против компании». citeturn20view2turn20view1turn25view1turn53search1turn34view1