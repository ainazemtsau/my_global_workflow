# CHARTER — solmax

## Mission

Solmax строит **Zaratustra** — операционную систему для экспертов. Эксперт это AI
с закреплённой зоной ответственности, живущий над файлами владельца: владелец
разговаривает с центром, центр раздаёт работу экспертам и собирает результаты.
Мозг это файлы, модели это сменные думающие руки — руки меняются с каждой новой
фронтир-моделью, мозг остаётся и растёт.

Zaratustra это **преемник workflow** (Direction OS), а не ветвь под зонтиком и не
надстройка над существующим: работа владельца переезжает в неё целиком, и после
переезда workflow выключается. Проект чистый, с нуля.

Читается первым: `work/zaratustra-v2-plan-2026-09-03.md` — план перехода,
утверждённый словами владельца 2026-09-03 (§0 несёт его слова дословно). План
старше допущений в старых карточках; живое слово владельца старше плана.

## Success criteria

Сроков нет (владелец). Это состояния «получилось», а не даты. Три критерия ниже
заменяют прежние SC1–SC3 («глубокое использование в ≥3 областях», «≥8 возможностей по четырём
осям», «глубже обычного чата») решением владельца 2026-09-03.

1. **Владелец ведёт через Zaratustra игру и хотя бы одну область жизни каждый
   день** *(главный критерий — сторож против «вечного черновика ядра»)*
   - Тридцать календарных дней подряд: за каждый из этих дней в журнале
     Zaratustra есть события и по игре, и минимум по одной области жизни; день
     начинается планом дня, который построила программа.
   - Мера — события журнала и его собственные запуски, а не число построенных
     функций.
   - В этом же окне workflow не используется как рабочее место.

2. **Другой человек ставит Zaratustra и обновляет её без нас**
   - Человек, не участвовавший в разработке, по публичной инструкции создаёт
     своё приватное рабочее место из шаблона и доводит его до первого плана дня;
     затем переводит его на новую версию командой обновления — миграции
     проходят, он читает «что нового».
   - Доказательство — его собственный отчёт или issue в публичном репозитории, а
     не наш прогон. Любая наша подсказка внутри прогона засчитывается как провал
     прогона.
   - Это второй установочный экземпляр, а не второй пользователь одной системы:
     принцип строго индивидуального использования не нарушается.

3. **Новая возможность это плагин с нулём правок ядра, доказанным диффом**
   - Второй эксперт, второй инструмент, вторая поверхность и второй вид
     добавлены после волны 1, и на каждом из этих добавлений `git diff` по
     объявленным файлам ядра пуст.
   - Тронуть ядро ради добавления считается дефектом ядра, а не работой.

Personal-vs-product is handled as a checkpoint in Constraints, not a success criterion, so success never forces a product outcome.

## Constraints

- **Преемник, а не зонтик.** Solmax больше не зонтик над несколькими ветвями: у
  направления один продукт — Zaratustra. Слова владельца 2026-09-03:
  «Zaratustra — это преемник Workflow, туда должно всё переехать. То есть я через
  него должен буду работать»; «Нужен чистый проект… я хочу именно с нуля начать…
  Workflow не остаётся как есть. Это железобетонно.» Пока переезд не завершён,
  владелец продолжает работать в workflow: «Я буду в Workflow работать, пока
  Zaratustra не будет готов, чтобы как-то мигрировать туда.»
- **Ветка operating-substrate закрыта** решением 2026-09-03. Отдельного
  переиспользуемого субстрата как самостоятельного маршрута направление не ведёт;
  его роль занимает ядро Zaratustra, описанное текстом (CORE.md). Репозиторий
  `solmax-operating-substrate` остаётся историей. Вердикты по узлам этой ветки
  выносит `map`, не устав.
- **Строго индивидуальное использование.** Один владелец, одно рабочее место.
  Никаких команд, ролей и общих рабочих мест: сущность «владелец» ровно одна, и
  многопользовательность не проектируется. Слова владельца: «строго для отдельных
  челиков… только индивидуальное использование… если команда, то это чисто для
  управленца.»
- **Два репозитория.** Публичный движок — Python-пакет `zaratustra`, команда
  `zara`, MCP-сервер, схемы, шаблоны экспертов, миграции, документация для
  ассистентов, образцовое рабочее место — без единого личного факта; и приватное
  рабочее место владельца, созданное из публичного шаблона. Код движка в рабочем
  месте не лежит, стоит зависимостью с закреплённой версией. Открытый исходник
  движка допустим; личные данные никогда не покидают приватное рабочее место.
- **Отношение к workflow на время переезда:** пока переезд не завершён, workflow
  остаётся рабочим местом владельца, а Zaratustra **никогда** в него не пишет;
  чтение read-only допустимо как одна возможность из многих. После переезда
  workflow выключается и вопрос снимается.
- **Build mode:** the system is built primarily by **background AI agents** (Codex / Claude Code) under owner review. Work is decomposed into **small, agent-buildable, independently-verifiable increments** with clear contracts/tests/done_when. The owner orchestrates and reviews in spare time; he does not hand-code large stretches.
- **Money:** new cash budget ≈ $0; the cognitive engine is the owner's **already-paid subscriptions, not the API**, until he explicitly decides otherwise. ⚠️ subscription `claude -p` draws a separate ~$20/mo Agent-SDK credit that silently halts when exhausted — the engine layer must budget and fail over.
- **Priority / do-no-harm:** this is the owner's **lowest-priority** direction. It must not steal time or attention from higher-priority directions (game, health). Solmax never preempts an active bet in a higher-priority direction. Одна линия работы: у Solmax один поток чатов, чтобы не отнимать их у игры. Критерий SC1 требует, чтобы игра шла ЧЕРЕЗ Zaratustra, — это не повышает приоритет её постройки.
- **Anti-perpetual-draft (from the worst-failure):** the core stays **tiny and stable on purpose**. Effort goes to accreting real, used capabilities and to depth — not to endlessly re-architecting the kernel. Re-opening the kernel design needs an explicit reason (like a concept that is not casually reopened). Это не гипотеза: ставка «Первый полезный Health-срез» стоила 21 день и 18 ног и дала 194 зелёных теста при нуле запусков владельца — `knowledge/light-close-throughput-measured.md`, `history/2026-09-03-s-solmax-zaratustra-v2-review-053.md`.
- **Personal-vs-product checkpoint:** if/when the system delivers real personal value, the owner makes an explicit decision whether to keep it personal or productize it. Until then it is personal.
- **Privacy / trust:** it holds the owner's whole-life data → local-first where possible, an auditable ledger, and **owner approval for irreversible / external / spend-incurring actions** (effect-tier gate).

## Lenses

1. **Extensibility** — every bet keeps the kernel tiny; capability is added by registration; "the Nth capability = ~0 kernel diff." Work that bloats the kernel is suspect. Тронуть ядро ради добавления это дефект ядра, а не работа.
2. **Real depth** — a capability must produce deep, personalized, multi-step help, not Q→A; the bar is "better than a plain ChatGPT/Claude session."
3. **Agent-buildability** — work decomposes into increments a background agent can build and that are verifiable (test / contract / done_when), because the owner builds via agents + review, not hands-on hours. Измерено: строка, перевыводимая из закоммиченных байтов, закрывается за одну-две ноги; строка, требующая суждения о поведении на настоящих данных владельца, тянет неделю — `knowledge/light-close-throughput-measured.md`. Задачи режутся по способу доказательства, а не по объёму.
4. **Daily use / dogfood** — a capability counts only when actually used and helping (the guard against the perpetual-draft failure). Мера — события журнала и запуски владельца, это же SC1.
5. **Privacy / trust / safety** — least-surprise; owner approval for irreversible/external/spendy actions; local-first; auditable ledger.
6. **Cost discipline** — engine on subscriptions; the credit cliff and compute budget are first-class; no silent spend.

## Owner edges

1. **Готовый разбор и измеренные дефекты собственной рабочей системы**
   - Proving fact: живое markdown-ядро workflow (LOG/history/plays/gates), на
     котором за 2026 год измерены его настоящие отказы — 21 день ставки с нулём
     запусков владельца, семь ног на одну задачу тяжёлого закрытия, пять заходов
     на ядро без пользующегося эксперта, — плюс проработанный ~2000-строчный
     концепт EXOCORTEX. Преемник строится не с чистого листа догадок, а с описи
     того, что именно ломалось.

2. **Enterprise engineering depth**
   - Proving fact: 10 years of professional software development (Java/full-stack) → architecture, ports, contracts, and event-log come naturally.

3. **Orchestration skill + paid subscriptions**
   - Proving fact: the owner already drives Codex / Claude Code as executors in his OS → he can build via background agents cheaply on subscriptions (exactly the build mode).

4. **OS as the build harness**
   - Proving fact: the Direction OS decomposes work into frame/map/shape/work/review with done_when evidence and gates, compensating for solo blind spots and keeping the kernel disciplined. Пока переезд не завершён, этот же harness строит своего преемника.

5. **Владелец — единственный пользователь, и это теперь принцип**
   - Proving fact: идеальная петля обратной связи, нет задачи поиска аудитории
     (в отличие от направления игры); решение 2026-09-03 о строго индивидуальном
     использовании убирает многопользовательность из проектирования целиком.

## Risk posture

**explore**

Rationale: no external stakes, no deadline, no money gate; the value is open-ended compounding, and over-controlling it would kill the compounding. Два жёстких сторожа остаются: **anti-perpetual-draft** (SC1 плюс линза ежедневного использования) и **do-no-harm** старшим направлениям. К ним добавлены стоп-правила перехода: волна вышла за свой размер в полтора раза → стоп и вопрос владельцу; проверка владельца дважды не прошла на одной волне → стоп и перечитать CORE.md, а не добавлять.

## Outside view

Solo "build my own AGI / second brain / exocortex" projects have a very high abandonment / perpetual-tinkering base rate — most die as endless core refactors that are never actually used (exactly the owner's worst-failure). The few that compound win by (1) a tiny stable core plus capability accretion (VS Code, Home Assistant, Obsidian — extensible platforms that lasted years) and (2) being genuinely used from early on (tools-for-thought winners). Current analogues: OpenClaw (local-first multi-channel agent gateway), Letta/MemGPT (agent memory). Implication for sequencing: keep the kernel tiny and stable, ship capabilities that get used, and measure success by real use + accretion, not by core perfection.

Собственная измеренная база (2026): пять заходов на ядро, рантайм и контракты до
появления эксперта, который ими пользуется, умерли; последняя ставка дала 194
зелёных теста и ноль запусков владельца за 21 день. Это тот же базовый исход, что
у чужих попыток, но замеренный на себе, — и он задаёт порядок волн: сначала текст
ядра, потом скелет программы, потом эксперт, который ими пользуется.

Reference cases used during frame:
- Personal second-brain / "my own AGI" abandonment base rate: perpetual core refactors that are never used.
- VS Code / Home Assistant / Obsidian: tiny stable core + plugin ecosystem → multi-year survival and accretion.
- OpenClaw: local-first multi-channel agent gateway (reference for the channel/body axis).
- Letta / MemGPT: agent memory as a first-class concern.
- Собственная история направления 2026: `knowledge/light-close-throughput-measured.md`,
  `knowledge/zaratusta-live-use-failure-and-operating-substrate-route.md`,
  `history/2026-09-03-s-solmax-zaratustra-v2-review-053.md`.

## Canonical repos

- Direction state repo: `github.com/ainazemtsau/my_global_workflow` (this OS repo).
  Пока переезд не завершён, это рабочее место владельца; по завершении переезда
  оно выключается.
- **Движок Zaratustra** (публичный, заводится в волне 0): Python-пакет
  `zaratustra`, команда `zara`, MCP-сервер, схемы, шаблоны экспертов, миграции,
  документация для ассистентов, образцовое рабочее место для тестов. Личных
  данных нет. Точное имя репозитория на GitHub фиксирует нога волны 0 — здесь
  оно не выдумывается.
- **Шаблон рабочего места** (публичный) и **приватное рабочее место владельца**
  из этого шаблона. Код движка в рабочем месте не лежит, стоит зависимостью с
  закреплённой версией.
- Старый продуктовый репозиторий: `github.com/ainazemtsau/zaratusta`, локально
  `C:\projects\zaratusta-product` (голова `53a52cd` на 2026-09-03). Остаётся
  историей: в него больше не пишем, идеи брать можно, структуру нет.
- `github.com/ainazemtsau/solmax-operating-substrate` — ветка закрыта решением
  2026-09-03; репозиторий остаётся историей.
- Zaratustra может читать OS-репозиторий read-only как одну возможность из
  многих; писать в него не может ни при каких условиях.

## Pre-mortem

This direction failed three years from now because one or more of the following happened.

### 1. Perpetual core draft (the worst-failure)

**Failure mode:** the kernel was re-architected endlessly; capabilities never accreted or got used.

**Mitigation:** SC1 (ежедневное ведение игры и одной области жизни через Zaratustra) + the dogfood lens + the anti-perpetual-draft constraint; порядок волн, где текст ядра идёт до программы, а эксперт-пользователь до расширений; re-opening the kernel design needs an explicit reason.

**Уже случилось однажды:** 21 день, 18 ног, 194 зелёных теста, ноль запусков владельца — `history/2026-09-03-s-solmax-zaratustra-v2-review-053.md`.

**Kill_by candidate:** if, after the kernel exists, ~5 increments pass with kernel churn but **zero new actually-used capability**, freeze the kernel and put all effort into capability accretion (or reframe).

### 2. Time-sink that steals from priority directions

**Failure mode:** the low-priority direction became a rabbit hole; game and/or health slipped.

**Mitigation:** the do-no-harm constraint; одна линия работы; built by background agents + spare-time review, not focus blocks; Solmax never preempts a higher-priority active bet.

**Kill_by candidate:** if game or health visibly slip because of Solmax, Solmax pauses.

### 3. Background agents produce slop / unverifiable mess

**Failure mode:** agents generated large unreviewable code; the owner could not keep up; quality rotted; kernel discipline was lost.

**Mitigation:** the agent-buildability lens — small increments with tests/contracts/done_when; «нулевой дифф ядра» как механический гейт; нарезка задач по способу доказательства (байты отдельно, суждение отдельно) по `knowledge/light-close-throughput-measured.md`; increment size kept to the owner's review cadence.

**Accepted risk / kill:** if the review backlog grows faster than it is cleared, shrink the increment size or slow agent throughput.

### 4. Just another chat wrapper — depth never materialized

**Failure mode:** it answered Q→A; the promised deep, priority-aware, multi-step help never appeared; the owner kept doing the real work elsewhere.

**Mitigation:** the real-depth lens; SC1 меряет не ответы, а ведение настоящей работы; пятиминутная проверка владельца в конце каждой волны — волна закрывается только его результатом, не нашим.

**Kill_by candidate:** если проверка владельца дважды не прошла на одной волне — стоп, перечитать CORE.md и чинить замысел, а не добавлять функции.

### 5. Subscription economics / credit cliff killed regular use

**Failure mode:** the ~$20 Agent-SDK credit ran out and background runs silently stopped; or ToS friction.

**Mitigation:** the cost-discipline lens; the engine layer budgets + detect-and-fail-over to codex; deterministic work routed off-LLM; the API seam kept ready.

**Accepted risk:** the API funding decision may need to come earlier than hoped (an explicit checkpoint); state stays intact via the ledger.

### 6. Privacy breach / irreversible action / workflow contamination

**Failure mode:** a capability sent/deleted/spent without approval, or leaked personal data; ИЛИ Zaratustra написала в живой workflow во время переезда и испортила рабочее место владельца.

**Mitigation:** the effect-tier gate (tier-2 → owner approval); local-first; the auditable ledger; least-privilege; связь с workflow строго read-only и проверяется, писать нельзя; личные данные живут только в приватном рабочем месте.

**Kill / stop trigger:** a single unreviewed irreversible action is a stop-and-audit trigger. Запись в workflow запрещена, это не принятый риск.

### 7. Vision sprawl — chasing the full vision too early

**Failure mode:** фронтенд, Telegram, демон, бенчмарки моделей и большие идеи полезли раньше, чем ядро и первый эксперт стали использоваться.

**Mitigation:** дисциплина волн 0→6; большие пункты входят только как плагины после того, как ядро используется; new ideas default to parked; map/shape cut lists.

**Kill_by candidate:** any shaped bet without a cut list is invalid (G6).

### 8. Переезд не состоялся: workflow остался жив

**Failure mode:** Zaratustra стала вторым местом рядом с workflow, а не преемником; владелец продолжил настоящую работу в workflow, и два места прожили годы параллельно, съедая внимание оба.

**Mitigation:** SC1 требует окна в тридцать дней, в котором workflow НЕ рабочее место; последняя волна называется «выключение workflow», а не «запуск параллельно»; месяц параллельной работы — это проверка переезда, а не режим жизни.

**Kill_by candidate:** если через месяц после объявленного переезда владелец всё ещё открывает workflow для настоящей работы — стоп и вопрос «что именно не переехало», вместо добавления функций.

### 9. Никто, кроме нас, не смог её поставить

**Failure mode:** SC2 не выполнен, потому что установка держится на наших руках: любая чужая попытка упирается в подсказку, которую даём мы.

**Mitigation:** установка проверяется ЧУЖИМ прогоном по публичной инструкции; наша подсказка внутри прогона засчитывается как провал прогона; входная инструкция и `guide` приходят из установленной версии движка, копий нет.

**Accepted risk:** если желающих нет, критерий проверяется прогоном на чистой машине с нулевым нашим вмешательством в шаги; это слабее, и слабость признаётся явно.

END_OF_FILE: live/solmax/CHARTER.md
