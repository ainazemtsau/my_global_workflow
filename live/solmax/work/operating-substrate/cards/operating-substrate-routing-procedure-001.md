    content: |
# Operating-substrate architecture card — routing and procedure

status: accepted
accepted_at: 2026-07-11
session: s-solmax-operating-substrate-routing-procedure-architecture-forge-001
call: c-solmax-operating-substrate-routing-procedure-architecture-forge-001
card_id: operating-substrate-routing-procedure-001
graph_nodes:
  - q07_routing_procedure

## Owner approval

direction_choice_words: |
  «Я принимаю твою рекомендацию»

selected_direction: |
  Direction B — Route Disposition + Procedure Invocation Contract.

freeze_words: |
  «Approve V1.»

## Вопрос

Как конкретный process превращает входящий intake в легитимный
следующий маршрут и вызов процедуры — с явной ответственностью,
uncertainty/no-route поведением, результатом, continuation и
writer/apply boundary — при этом оставляя реальные процедуры и
domain-routing внутри process pack и не выбирая универсальный router,
schema, provider или orchestration framework?

## Сохранённые parent locks

Q1-Q6 не изменяются.

В частности:

- operating-substrate остаётся стабильным model-neutral и
  carrier-neutral kernel с подключаемыми process packs;
- конкретный процесс создаётся через process pack, а не через
  модификацию kernel;
- procedure является first-class process definition, а конкретные
  каталоги процедур и routing rules принадлежат process pack;
- service zones остаются semantic responsibility families, а не
  физическими сервисами или модулями;
- каждое atomic responsibility claim имеет одного primary normative
  owner;
- invoke, delegate и handoff имеют разные ownership effects;
- каждое открытое обязательство имеет одного current next-action owner;
- delegation сохраняет parent integration и accountability;
- capability, permission, authorization и applied effect не
  эквивалентны;
- query, event, evidence, propose, validate, authorize, apply, result и
  continue не схлопываются;
- accepted state, history, source, evidence, memory, artifact,
  definition и continuation различимы;
- durable mutation проходит через validated writer/apply boundary;
- изменение определения процедуры не переинтерпретирует active work
  молча;
- schema, carrier, provider, runtime, topology, implementation и
  окончательный service-block list не выбраны.

# Frozen answer

## 1. Основная архитектурная граница

Minimal Stable Bootstrap принимает двухслойный reusable contract:

1. Route disposition semantics — каким осмысленным исходом закончилась
   маршрутизация intake.
2. Procedure invocation semantics — что должно быть установлено до
   того, как выбранная процедура легитимно выполняется.

Kernel фиксирует смысл этих двух слоёв, ownership и failure boundaries.

Process pack владеет:

- реальными процедурами;
- их applicability;
- domain vocabulary;
- local routing policy;
- domain-specific evidence, authority и effect rules;
- pack-specific degraded и recovery routes.

Adapter или implementation владеет физическим способом вычисления
маршрута и выполнения процедуры.

Таким образом, routing может быть выполнен моделью, детерминированным
правилом, кодом, человеком или их комбинацией. Ни один из этих способов
не становится universal architecture.

## 2. Procedure

Procedure — отдельно сохраняемое first-class определение ограниченного
вида работы внутри process pack.

Procedure не является:

- неформальным советом внутри prompt;
- именем модели;
- tool call;
- chat transcript;
- названием физического агента;
- одним runtime task;
- произвольным ответом модели;
- универсальным substrate play.

Определение процедуры должно быть семантически достаточным, чтобы
установить:

- какой bounded kind of work оно определяет;
- при каких условиях оно применимо;
- на какой accepted basis может работать;
- какие authority и effect boundaries действуют;
- какого результата, closure и continuation оно требует;
- как active work должен трактоваться при изменении определения.

Это concern categories, а не обязательные поля, manifest sections или
schema.

Actual procedure catalogue и реальные procedure names принадлежат
process pack. Direction OS play names, Zaratusta procedures и любые
будущие consumer procedures не становятся substrate authority.

## 3. Routing

Routing — ответственность превратить принятый intake в один основной
легитимный next route для текущего bounded obligation.

Routing оценивает только то, что требуется для текущего шага:

- objective и ограничения intake;
- current effective process definition;
- применимые procedure definitions;
- релевантный accepted state, source и context;
- известную uncertainty;
- доступные capabilities;
- authority и effect boundaries;
- текущую ownership structure.

Routing не обязан быть одним физическим router component и не требует
центрального orchestrator.

Одна реализация может распределить routing между несколькими ролями.
Другая может выполнить его внутри одного ChatGPT run. В обоих случаях
должно быть семантически определимо:

- кто владел routing obligation;
- какой disposition был установлен;
- кто владеет следующим действием;
- какой unresolved вопрос или block остался.

## 4. Route dispositions

Маршрутизация должна завершиться явным disposition одного из следующих
смысловых классов.

Это не обязательный enum, не packet schema и не закрытый каталог
labels. Реализация может использовать другие названия или объединять
представление, но не может скрывать существенные различия в ownership,
recovery или authority.

### 4.1. Applicable procedure selected

Одна процедура признана применимой и может быть отдельно invoked.

Selection ещё не доказывает:

- принятие обязательства исполнителем;
- начало исполнения;
- перенос ownership;
- наличие authority;
- применение durable change;
- достижение результата.

### 4.2. Bounded clarification required

Objective, scope или существенная часть intent неоднозначны, и process
не имеет легитимного pack-owned правила для разрешения этой
неоднозначности.

Процесс формирует минимальный вопрос, который реально разблокирует
маршрут.

### 4.3. Mandatory input missing

Известно, какой input требуется, но он отсутствует, недоступен или
недостаточно надёжен.

Процесс не придумывает значение и не подменяет его предположением.

### 4.4. Conflicting routes unresolved

Несколько процедур или маршрутов остаются применимыми, а local routing
policy не устанавливает легитимный выбор.

Если различие материально влияет на outcome, authority, cost, risk или
committed direction, оно маршрутизируется подходящему decision owner.

### 4.5. No applicable procedure

Ни одна сохранённая процедура не отвечает текущему виду работы.

Это не разрешение выбрать ближайшую по названию процедуру или
импровизировать скрытый новый process.

### 4.6. Mandatory capability unavailable

Процедура применима по смыслу, но обязательная semantic capability не
может быть легитимно разрешена.

Silent substitution допустима только тогда, когда process pack заранее
определяет совместимый degraded route. Иначе маршрут блокируется или
возвращается как unresolved.

### 4.7. Explicit process or procedure gap

Intake обнаружил отсутствие или внутреннюю несогласованность process
definition, procedure, routing rule либо required responsibility.

Gap создаёт bounded obligation с named resolution owner. Он не приводит
к скрытому созданию новой процедуры или mutation process pack в том же
reasoning run.

### 4.8. Another named legitimate route

Process может установить иной ограниченный маршрут, уже выражаемый
принятыми Q3 semantics, например:

- query;
- bounded owner decision;
- delegate;
- handoff;
- return/result;
- continue;
- explicit refusal.

Такой маршрут обязан сохранить ownership, authority, closure и
continuation semantics.

## 5. Selection, invocation, acceptance, execution, result и continuation

Следующие смысловые переходы различаются:

1. Intake acceptance

   Owner-facing work responsibility принимает bounded routing
   obligation и становится его current owner.

2. Procedure selection

   Routing устанавливает применимую procedure definition.

3. Procedure invocation

   Выбранной responsibility предлагается bounded obligation по
   установленному invocation contract.

4. Acceptance или refusal

   Target принимает, отклоняет либо требует input. До acceptance
   прежний current owner сохраняет ответственность за разрешение
   маршрута.

5. Execution attempt

   Выполняется принятая procedure obligation.

6. Return/result

   Procedure obligation закрывается, checkpoint-ится либо возвращается
   unresolved с явным владельцем остатка.

7. Continuation

   Сохраняется достаточно принятого смысла, чтобы следующий run мог
   продолжить легитимно.

Одна физическая реализация может компактно совместить несколько
переходов. Например, один ChatGPT run может выбрать, принять и
выполнить read-only процедуру.

Conformance всё равно должно позволять установить, что именно
произошло. В частности:

- selection не равен acceptance;
- invocation не равен execution;
- acceptance не переносит human authority;
- execution не доказывает success;
- result не равен artifact или последнему сообщению;
- continuation не равен transcript copy или opaque runtime cursor.

## 6. Semantic minimum procedure invocation

Каждый легитимный invocation должен семантически установить достаточно
информации для следующих выводов.

Это не обязательные packet fields.

### 6.1. Objective и bounded scope

- какое ограниченное обязательство открывается;
- что входит и не входит в работу;
- ожидается completion или допустим checkpoint.

### 6.2. Governing procedure meaning

- какая процедура выбрана;
- какое определение процедуры governing;
- почему она считается применимой;
- какие известные ограничения или uncertainty относятся к выбору.

### 6.3. Accepted basis

- какой accepted state или authoritative reference используется;
- какие sources и context необходимы;
- какие материалы остаются provisional, disputed, stale или
  unavailable;
- какие definition/version semantics интерпретируют работу.

### 6.4. Ownership

- кто current next-action owner;
- кто parent integration owner, если работа delegated;
- кому возвращается результат;
- кто владеет unresolved recovery или clarification.

### 6.5. Authority и effects

- какая bounded operational authority уже существует;
- какие external, irreversible, spend-incurring или durable effects
  запрещены либо требуют отдельного authorization;
- нужен ли writer/apply path;
- какие credentials или capabilities доступны, не превращая capability
  в permission.

### 6.6. Capabilities

- какие semantic capabilities обязательны;
- какие опциональны;
- существует ли pack-declared legitimate degraded route;
- как отсутствие capability меняет result meaning.

### 6.7. Completion semantics

- что означает success;
- что означает bounded stop;
- что означает refusal или input-required;
- как трактуются failed-known-not-done, partial и outcome-unknown,
  когда процедура может производить effects.

### 6.8. Owed return

- какой результат должен вернуться;
- какая evidence/provenance требуется;
- какие обязательства могут остаться открытыми;
- какой return route и current owner должны быть установлены;
- что требуется сохранить для portable continuation.

## 7. Ownership и child work

Routing не создаёт ownerless промежутков.

Обязательные правила:

- routing obligation имеет одного current next-action owner;
- выбранная procedure target не становится owner до принятия
  invocation;
- refusal, lost acknowledgement или ambiguity возвращаются current
  owner для reconciliation;
- delegate получает ownership bounded child execution;
- delegator сохраняет parent integration, child-failure handling и
  owner-facing closure;
- handoff переносит active ownership только после successor acceptance;
- waiting for input или decision сохраняет monitoring и closure owner;
- каждый принятый child obligation должен вернуть result, failure,
  unresolved disposition или continuation;
- internal child failure не перекладывает владельцу обязанность
  управлять внутренней recovery-машиной.

Эти правила специализируют Q3 для procedure routing и не изменяют Q3
semantics.

## 8. Uncertainty, missing input и no-route

Поведение должно быть пропорциональным consequence и реальной
неопределённости.

### Когда process может продолжить без owner question

Process продолжает, если process-pack routing policy легитимно и
однозначно разрешает выбор, а он:

- не расширяет authority;
- не меняет committed direction;
- не подменяет mandatory input;
- не скрывает material evidence gap;
- не создаёт опасный effect;
- не требует создания новой procedure definition.

### Когда process обязан остановить маршрут

Process использует clarification, decision, block или unresolved
disposition, если:

- ambiguity materially меняет результат;
- отсутствует mandatory input;
- применимые маршруты конфликтуют;
- отсутствует mandatory capability без degraded route;
- authority недостаточна;
- procedure или routing definition содержит gap;
- continuation или governing definition несовместимы;
- unsafe effect outcome неизвестен.

### Запрещённые fallback-формы

- silent nearest-match procedure;
- скрытое расширение scope;
- invented input;
- fabricated source или capability;
- generic “best effort”, меняющий semantic result;
- выбор по одному только порядку процедур;
- last-write-wins routing policy;
- самовольное создание новой процедуры;
- выполнение write-effect через read-only reasoning route;
- передача owner решения без объяснения, что именно оно разблокирует.

No-route не обязан завершаться пустым отказом. Process может вернуть
полезную частичную работу, известные факты, bounded options и portable
continuation, если не сообщает их как completed target outcome.

## 9. Process-pack и procedure ownership

Process pack является primary normative owner для:

- procedure catalogue;
- procedure meaning и applicability;
- domain vocabulary;
- local intake classification concerns;
- routing and escalation policy;
- required context и source rules;
- local evidence sufficiency;
- local success, stop и failure meaning;
- mandatory и optional capability requirements;
- legitimate degraded routes;
- domain authority/effect policy;
- process-specific result expectations;
- procedure compatibility и migration obligations;
- process-specific writer procedures или writer policy.

Kernel не определяет реальные процедуры и не имеет универсального
catalogue.

Kernel фиксирует только обязательные semantics:

- явный route disposition;
- stage non-collapse;
- ownership closure;
- bounded invocation minimum;
- no silent fallback;
- result/continuation obligations;
- durable apply boundary;
- active-work compatibility;
- anti-bureaucracy.

## 10. Writer procedure / writer policy

Writer остаётся логической validated apply responsibility, а не
обязательным отдельным агентом, chat или сервисом.

Concrete process pack может отдельно сохранять одну или несколько
writer procedures или writer policies для bounded writable scopes.

Writer definition должна быть семантически достаточной, чтобы
установить:

- какие durable-state или effect boundaries она может изменять;
- кто является normative state/effect owner;
- какой current accepted basis должен быть перечитан;
- какие preconditions и conflicts проверяются;
- какая authority требуется;
- какая validation должна предшествовать apply;
- какие changes запрещены;
- что означает applied, rejected, conflict, failed-known-not-done,
  partial и outcome-unknown;
- какая evidence возвращается;
- как unresolved effect или conflict продолжается;
- какой result и continuation получает caller.

Reasoning route может:

- query;
- assemble evidence;
- propose;
- route validation;
- запросить authorization;
- invoke writer.

Reasoning route не превращает proposal в durable truth.

Codex может сейчас реализовывать executor и writer roles, но Codex не
становится semantic authority. Отдельный writer chat или agent
остаётся допустимой bootstrap topology, а не universal requirement.

Writer procedure сама является process definition. Её изменение
проходит те же admission, compatibility и active-work правила, что и
другая procedure definition.

## 11. Procedure identity и изменение определения

Каждая активная procedure obligation должна сохранять достаточно
semantic identity и lineage, чтобы определить:

- какое procedure meaning управляло работой;
- какая process-pack definition была effective;
- изменилось ли определение;
- совместим ли resume;
- требуются ли revalidation, migration или другой disposition.

Exact identifiers, version strings, hashes, schema и storage
representation остаются открытыми.

Новая или изменённая procedure definition:

- является candidate definition;
- не становится authoritative только из-за редактирования файла или
  prompt;
- проходит Q4 admission/activation semantics;
- не переинтерпретирует начатую работу задним числом.

Каждое затронутое active obligation получает явный disposition:

1. compatible resume;
2. bounded revalidation или migration;
3. pin к прежнему определению и drain;
4. accepted handoff или replacement;
5. block или rejection;
6. unresolved с named resolution owner.

Pinning сохраняет интерпретацию, но не сохраняет:

- revoked authority;
- запрещённое disclosure/use;
- недействительные credentials;
- mandatory policy, которая теперь блокирует работу;
- unsafe effect assumptions;
- недоступный mandatory source без legitimate degraded route.

## 12. Result и portable continuation

Procedure result:

- закрывает или checkpoint-ит bounded obligation;
- возвращает integration responsibility;
- сообщает achieved, not achieved или unresolved disposition;
- различает authoritative effect outcome и narrative;
- указывает remaining obligations и owners;
- сохраняет evidence/provenance, достаточные для stated claim;
- устанавливает continuation disposition.

Portable continuation сохраняет достаточно принятого смысла, чтобы
другой ChatGPT, Codex или будущий run мог определить:

- work identity и objective;
- governing process/procedure definition;
- accepted basis;
- завершённые и открытые obligations;
- current owners;
- decisions и authority bounds;
- effect certainty;
- relevant evidence и provenance;
- compatibility disposition;
- next legitimate action;
- return route.

Она не обязана содержать полный transcript, полный history или полный
audit.

## 13. Current bootstrap mapping

Для первого bootstrap допустима следующая простая реализация.

### ChatGPT Project

Может реализовывать:

- owner-facing intake;
- read-only reasoning;
- route evaluation;
- procedure selection;
- bounded clarification;
- proposal;
- delegation/invocation preparation;
- owner decision presentation;
- result integration;
- portable continuation.

Он не становится durable state owner только потому, что сформулировал
вывод.

### Codex

Может реализовывать:

- bounded executor;
- fresh-state query;
- local file and repository operations;
- validation;
- tests/checks;
- writer/apply responsibility;
- authoritative apply evidence.

Codex не получает human authority только из технической возможности
изменить файлы.

### Owner

Может вручную переносить continuation между ChatGPT и Codex. Automatic
transport, Agents SDK, scheduler или agent mesh не требуются для
semantic validity bootstrap.

### Process pack

Остаётся нормативным владельцем:

- процедур;
- routing policy;
- writer procedure/policy;
- local evidence и effect rules;
- result expectations.

Эта mapping является текущей realization, а не architecture law.

## 14. Anti-bureaucracy rule

Внутренняя routing и procedure machinery должна быть проверяемой, но
по умолчанию не переносится на владельца как операционная нагрузка.

Owner-facing route заканчивается одним из четырёх полезных outcomes:

1. полезный результат;
2. ограниченный вопрос или decision, где ясно, почему он нужен и что
   блокирует;
3. ясный block/failure, где названы причина, текущий owner и recovery
   route;
4. portable continuation, достаточная для следующего run.

Owner не обязан:

- выбирать procedure name, если pack policy может легитимно выбрать её
  сам;
- читать route trace;
- разбираться в lifecycle labels;
- проверять внутренний audit перед получением результата;
- вручную управлять child agents;
- реконструировать previous chat;
- интерпретировать raw state/history machinery.

При этом deeper trace, evidence и governing definitions должны
оставаться inspectable, когда требуется refutation, recovery или
review.

Это обязательная защита от повторения Zaratusta failure: полные
внутренние state/intake/handback surfaces сами по себе не дали
полезного owner-leading процесса и создали бюрократию.

# Responsibility classification

## Invariant kernel semantics

В kernel входят:

- procedure как first-class bounded definition;
- явный route disposition;
- distinction selection/invocation/acceptance/execution/result/
  continuation;
- invocation semantic minimum;
- один current owner на каждое open obligation;
- отсутствие ownership gap;
- retained parent integration under delegation;
- explicit uncertainty/no-route behavior;
- запрет silent fallback;
- capability не равна authority;
- result и continuation closure;
- logical validated writer/apply boundary;
- procedure-change compatibility;
- anti-bureaucracy rule.

## Process-pack declarations

Process pack владеет:

- actual procedure catalogue;
- local routing rules;
- applicability;
- domain terminology;
- context/source requirements;
- safety, evidence и effect policy;
- mandatory и optional capabilities;
- degraded routes;
- procedure-specific success/failure;
- writer procedures/policies;
- active-work compatibility obligations;
- process-specific proof scenarios.

## Owner-profile concerns

Owner profile может предоставлять:

- язык;
- уровень объяснения;
- ask/proceed preference;
- initiative preference;
- presentation style;
- approval и privacy preferences, если они действительно owner-wide.

Owner preference не может:

- изменить kernel semantics;
- ослабить mandatory process policy;
- разрешить конкретный effect автоматически;
- превратить ambiguity в permission to guess.

## Reusable-service candidates

Следующие capabilities могут позднее стать reusable-service semantics,
но Q7 не утверждает final catalogue:

- procedure discovery и retrieval;
- applicability evaluation support;
- required-context assembly;
- capability resolution;
- route explanation;
- invocation validation;
- continuation validation/import;
- compatibility evaluation;
- writer coordination.

Они не получают process-policy ownership только потому, что
предоставляют capability.

## Adapter / implementation concerns

Остаются downstream HOW:

- prompt layout;
- Markdown или JSON representation;
- classifier;
- planner;
- rules/policy engine;
- model-directed routing;
- deterministic routing;
- hybrid routing;
- Agents SDK;
- provider/model selection;
- registry;
- database или files;
- ChatGPT/Codex transport;
- scheduler;
- graph runtime;
- task queue;
- agent mesh;
- physical writer topology;
- application и deployment.

# Pressure test 1 — Health-like safety/evidence process

## Сценарий

В процесс приходит неоднозначный health-related intake:

- две процедуры выглядят потенциально применимыми;
- одна требует current authoritative source;
- source отсутствует или stale;
- возможное продолжение может привести к consequential external effect;
- optional summarization capability доступна, но mandatory evidence
  capability — нет;
- procedure definition была недавно изменена.

## Требуемое поведение

1. Routing не выбирает ближайшую процедуру по wording.
2. Conflicting routes получают explicit disposition.
3. Missing authoritative input остаётся missing, а не заменяется model
   inference.
4. Если различие materially влияет на риск, process задаёт один bounded
   clarification либо маршрутизирует decision.
5. Mandatory evidence capability absence блокирует effect-producing
   route.
6. Read-only полезная часть может продолжиться только если pack
   определяет безопасный degraded route и changed result meaning видим.
7. Procedure selection не авторизует действие.
8. Writer/apply invoked только после current-state validation и
   применимой authority.
9. Изменённая procedure definition не переинтерпретирует active
   obligation: выполняется revalidation, pin/drain, migration или
   block.
10. Owner получает краткое объяснение consequential gap, а не
    внутренний routing graph.

Verdict: PASS.

Health-specific safety policy остаётся process-pack-owned. Kernel
обеспечивает только ownership, evidence/authority distinctions,
explicit no-route и controlled apply.

# Pressure test 2 — Game / productive-play exploratory process

## Сценарий

Owner задаёт творческий intake, который может означать:

- свободный brainstorm;
- convergence к одному варианту;
- исследование референсов;
- canon decision;
- durable canon update.

Optional visualization capability недоступна. Несколько route остаются
разумными, но stakes невысоки. Во время работы публикуется новая версия
creative procedure.

## Требуемое поведение

1. Local routing policy может выбрать brainstorm без owner question,
   если intake однозначно exploratory и нет durable effect.
2. Если brainstorm и canon commitment materially различаются, process
   задаёт один компактный steering question.
3. Отсутствие optional visualization может использовать pack-declared
   degraded route с явным снижением result quality.
4. Draft artifact не становится canon.
5. Canon update требует writer/apply.
6. Delegated research возвращает результат parent integrator.
7. Новый procedure version не захватывает active branch молча: branch
   может продолжить pinned, revalidate или migrate.
8. Owner видит creative output и нужное решение, а не внутренний
   procedure lifecycle.

Verdict: PASS.

Тот же kernel поддерживает exploratory процесс без импорта Health
policy, обязательных тяжёлых gates или универсального router.

# Rejected alternatives

## 1. Provider/framework-first architecture

Отклонено, потому что Agents SDK, model router или orchestration
framework преждевременно сделают текущий tool stack архитектурным
авторитетом.

## 2. Prompt-as-procedure

Отклонено, потому что неформальный prompt не гарантирует applicability,
authority, closure, compatibility или durable preservation.

## 3. Classifier-as-architecture

Отклонено, потому что classifier является возможной реализацией route
evaluation, но не определяет ownership, no-route, result или writer
semantics.

## 4. Universal procedure catalogue

Отклонено, потому что реальные kinds of work и policy legitimately
различаются между process packs.

## 5. Silent nearest-match или best-effort fallback

Отклонено, потому что скрывает missing input, capability gaps, changed
result meaning и потенциальное authority expansion.

## 6. Selection equals acceptance or execution

Отклонено, потому что выбранная procedure target могла не принять
работу, не иметь capability или не иметь authority.

## 7. Ownerless routing

Отклонено, потому что ambiguity, waiting и failed handoff не могут
оставлять obligation без current resolution owner.

## 8. Routing order или last-write-wins как authority

Отклонено, потому что catalogue order, prompt order и newest definition
не доказывают applicability или normative precedence.

## 9. One universal writer agent/chat

Отклонено, потому что инвариантна logical validated apply
responsibility, а не физическая topology.

## 10. ChatGPT и Codex как process semantics

Отклонено, потому что это текущие replaceable adapters.

## 11. Automatically move all work to latest procedure

Отклонено, потому что active obligations, accepted state, authority и
continuation могут быть несовместимы.

## 12. Expose internal route lifecycle as owner interface

Отклонено, потому что protocol completeness не является owner-facing
usefulness и воспроизводит бюрократический failure mode.

# Evidence limits

Карточка не доказывает:

1. какой exact procedure schema нужен;
2. какие route-disposition labels или enum следует использовать;
3. точное entity relationship между intake, work item, run, invocation
   и execution attempt;
4. какой routing algorithm лучше;
5. нужен ли classifier, planner или rules engine;
6. точный procedure identity/version format;
7. точный continuation schema;
8. точный result schema;
9. точные authority/effect classes;
10. какой carrier или repository нужен;
11. что ChatGPT/Codex mapping является оптимальной permanent
    implementation;
12. что первый конкретный process pack уже owner-useful;
13. что semantic conformance автоматически предотвращает плохой UX;
14. какие Q8-Q14 cards обязательно должны быть завершены до
    implementation;
15. финальный reusable-service или physical service-block list.

Health-like и game-like проверки являются semantic refutation
pressures, а не product validation.

# Child and downstream questions

Остаются открытыми:

1. Как связаны intake, durable work item, routing obligation, procedure
   invocation и execution attempt?
2. Каков минимальный machine- and human-portable
   result/continuation contract?
3. Как представлять route rationale владельцу без внутренней
   бюрократии?
4. Какие authority и evidence gates требуют fresh owner decision?
5. Как доказывается compatibility процедуры без exact universal schema?
6. Может ли один obligation композиционно использовать несколько
   процедур, и кто остаётся integration owner?
7. Когда changed capability является простым rebind, а когда требует
   procedure/process readmission?
8. Как проверяется, что pinned work полностью drained?
9. Как representation procedure definitions переносится между
   Markdown/chat и приложением?
10. Какие live-use proof scenarios нужны первому process creator?
11. Какие Q8-Q14 concerns являются implementation blockers, а какие
    допустимо отложить?

Эти вопросы размещаются в существующих downstream routes:

- Q8 — live owner interface;
- Q9 — result/handback и continuation;
- Q10 — authority/gates;
- Q11 — evidence/evolution и definition change;
- Q12 — entity/communication/identity;
- Q13 — proof;
- Q14 — carrier.

# Graph verdict

hidden_prerequisite: none
gap_event: none
top_level_rebalance: not_needed
return_to_cartography: not_required
implementation_activation: prohibited

Q7 является достаточно ограниченным и готовым к freeze, потому что:

- Q1-Q6 дают необходимые ownership, state, definition, authority и
  continuation semantics;
- procedure/routing boundary можно определить без schema и algorithm;
- route disposition classes предотвращают silent fallback, не
  становясь обязательным enum;
- writer boundary определяется без фиксации Codex или отдельного
  агента;
- Health-like и game-like pressures проходят;
- открытые interface, packet, identity, proof и carrier вопросы
  помещаются в Q8-Q14.

Следующий маршрут после approval: implementation-readiness checkpoint,
который классифицирует Q8-Q14 на:

- blocker для первого process creator;
- minimum bootstrap claim, который можно закрыть внутри readiness;
- допустимый post-bootstrap downstream;
- implementation-specific concern;
- proof requirement до live claim.

# Gate — refutation result

## Parent-lock check

PASS.

Q1-Q6 не пересмотрены.

## Atomicity check

PASS.

Карточка замораживает только Q7 routing/procedure boundary.

## Consumer-boundary check

PASS.

Actual procedures, routing policy, domain evidence и writer policy
остаются process-pack-owned.

## No-HOW check

PASS.

Не выбран classifier, algorithm, framework, provider, schema, carrier,
runtime, repository или topology.

## Route-disposition overfreeze check

PASS с защитой.

Перечень зафиксирован как набор обязательных смысловых различий, а не
exact enum или закрытая message taxonomy.

## Invocation-schema leakage check

PASS с защитой.

Invocation minimum сформулирован как semantic determinability, а не
mandatory fields.

## Writer-topology check

PASS.

Заморожена logical validated apply responsibility; отдельный agent/chat
и Codex остаются реализациями.

## Ownership check

PASS.

Нет ownerless waiting, routing gap или silent handoff.

## Active-work compatibility check

PASS.

Изменение procedures получает explicit per-obligation disposition.

## Evidence and proof check

PASS для bounded architecture decision.

Evidence limits и необходимость дальнейшего live-use proof явно
записаны.

## Anti-bureaucracy check

PASS.

Owner-facing outcome ограничен useful result, bounded decision, clear
block или continuation.

## Pressure tests

PASS.

Health-like и game/productive-play cases не требуют изменения kernel и
не копируют policy друг друга.

## Final gate verdict

PASS.

Карточка v1 утверждена владельцем словами:

«Approve V1.»

END_OF_FILE: live/solmax/work/operating-substrate/cards/operating-substrate-routing-procedure-001.md
