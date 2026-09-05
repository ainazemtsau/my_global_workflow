Zaratustra — архитектурный план и план реализации

0. Задача

Построить Zaratustra — open-source операционную среду для совместной работы одного человека и сменяемых AI-моделей.

Zaratustra не является одной AI-моделью, одним главным чатом или специализированным workflow для разработки.

Её задача:

* сохранять непрерывное состояние между чатами и моделями;
* позволять подключать совершенно разные процессы работы;
* давать каждому AI только нужный для конкретной работы контекст;
* позволять работать через ChatGPT web, Codex, Claude Code и будущие интерфейсы;
* сохранять решения, результаты, память и происхождение информации;
* постепенно учиться лучше работать именно с конкретным пользователем без fine-tuning моделей;
* позволять более автономную работу только внутри явно заданных границ;
* использовать максимально дешёвого исполнителя, качество которого доказано для данного класса работы.

Главная формула:

Модель думает. Zaratustra помнит, связывает, ограничивает, проверяет изменения и обеспечивает продолжение.

⸻

1. Неприкосновенные принципы

Эти положения считаются архитектурными инвариантами.

1.1. Никакого fine-tuning

Zaratustra не обучает веса пользовательских моделей.

Персонализация происходит через:

* долговременное состояние;
* память;
* инструкции;
* procedures / skills;
* context selection;
* personal evals;
* накопленный опыт выполнения работ.

Новая модель должна становиться полезной пользователю, получив это внешнее состояние, а не после персонального обучения её весов.

1.2. Не оптимизировать одобрение пользователя

Система не оптимизирует:

* количество взаимодействий;
* эмоционально положительную реакцию;
* согласие пользователя;
* продолжительность разговора;
* вероятность того, что ответ понравится.

Её задача — помогать достигать явно выбранных пользователем целей.

При конфликте приоритет примерно такой:

1. фактическая и эпистемическая корректность;
2. безопасность и сохранение контроля пользователя;
3. соответствие явным долгосрочным целям и ограничениям;
4. реальный результат работы;
5. затраты, время и friction;
6. предпочтения пользователя по форме взаимодействия.

Предпочтения могут менять способ подачи ответа, но не должны менять факты или стратегическую рекомендацию только ради согласия.

AI обязан уметь спорить с пользователем, когда есть конкретное основание считать, что предлагаемое пользователем действие противоречит его же цели, фактам, ранее принятому ограничению или подтверждённому повторяющемуся паттерну неудач.

Это не разрешение системе становиться патерналистской. При неопределённости она показывает конфликт и основание, а окончательное решение остаётся за человеком.

1.3. Один мозг = одно долговременное состояние, а не одна модель

ChatGPT, Codex, Claude и будущие модели — сменяемые исполнители.

Истина не должна жить внутри конкретного чата.

1.4. Один execution context — одна Work

Одна ограниченная исполняемая работа получает отдельный контекст.

Пользовательский разговор при этом может быть длинным и содержать несколько тем.

То есть:

один пользовательский чат ≠ обязательно одна Work;
одна Work = один ограниченный исполнительный контекст.

Это сохраняет сильную сторону нынешнего Next Call и одновременно позволяет сделать нормальный будущий frontend.

1.5. Capability не равно authority

Более сильная модель не получает больше прав.

Модель может быть способна выполнить действие, но Work должна отдельно разрешать это действие.

1.6. UI не является вторым источником истины

Chat, dashboard, board, whiteboard и календарь — разные представления одних объектов.

Изменение карточки на доске должно вызывать ту же операцию Core, что изменение из чата.

1.7. Любое обучение объяснимо и обратимо

Если Zaratustra научилась чему-то о пользователе или процессе, должно быть возможно ответить:

* чему именно;
* на основании каких наблюдений;
* в какой области это действует;
* насколько хорошо подтверждено;
* когда было принято;
* чем было заменено;
* как это отменить.

⸻

2. Архитектура верхнего уровня

                    USER
                      │
       ┌──────────────┼──────────────┐
       │              │              │
    ChatGPT        Codex /        Future UI
      web          Claude Code
       │              │              │
       └──────── adapters / handoff ─┘
                      │
               ZARATUSTRA CORE
                      │
     ┌────────────────┼────────────────┐
     │                │                │
   State            Work             Memory
   History          Handoff          Context
   Artifacts        Permissions      Extensions
                      │
                Process Packs
                      │
             skills / tools / agents

Core не содержит предметного знания про здоровье, разработку игры, финансы и т.д.

Эти вещи живут в подключаемых Process Packs.

⸻

3. Что входит в Core

Не фиксировать искусственно число сущностей. Важны обязанности.

Core имеет семь основных зон ответственности.

3.1. State

Хранит актуальное состояние объектов:

* идентификаторы;
* типы;
* версии;
* revisions;
* связи;
* текущие статусы.

Core не решает смысловой вопрос «правильная ли это цель».

3.2. Work

Work — одна ограниченная единица AI-работы.

Она содержит:

* цель;
* ожидаемый результат;
* критерии проверки;
* process;
* ссылки на контекст;
* ограничения;
* authority scope;
* требования к исполнителю;
* бюджет;
* зависимости;
* состояние выполнения.

Work не содержит имя обязательной конкретной модели.

3.3. Mutation

Все изменения управляемого состояния проходят через один Mutation API.

CLI, MCP, frontend и import должны вызывать одну реализацию этого API.

Нельзя создавать ситуацию:

Claude → напрямую YAML
frontend → напрямую SQLite
ChatGPT → отдельный API
Codex → отдельный script

3.4. Permissions / authority

Core проверяет:

* что Work может читать;
* что Work может изменять;
* какие инструменты доступны;
* нужны ли дополнительные approvals;
* какие external effects запрещены.

3.5. Memory

Хранит:

* исходные наблюдения;
* решения;
* факты;
* производное знание;
* пользовательские предпочтения;
* процедурные правила;
* provenance.

Memory не объявляет любую фразу пользователя или догадку модели вечной истиной.

3.6. Context

Context Compiler строит ограниченный context package для конкретной Work.

Он не должен загружать «всё, что известно о пользователе».

3.7. Extensions

Регистрирует:

* processes;
* skills;
* tools;
* executors;
* views;
* adapters.

Новая область деятельности должна подключаться без изменения базовой семантики Core.

⸻

4. Хранилище

Для первой реализации использовать гибрид:

SQLite
  operational state
  revisions
  Work
  permissions
  events
  memory metadata
  idempotency
  relations
  approvals
Files
  Markdown documents
  JSON
  images
  source material
  reports
  generated artifacts
  process instructions
Git
  optional history / sync / backup / review / transport

4.1. SQLite — operational source of truth

SQLite отвечает за транзакционное состояние.

Минимальный вариант не требует отдельного database server.

Использовать:

* один workspace database;
* явные schema migrations;
* transactions;
* optimistic concurrency;
* idempotency keys.

4.2. Files — содержательные артефакты

Длинное содержимое не нужно запихивать в DB.

Артефакт:

1. создаётся как новый immutable или versioned файл;
2. получает SHA-256;
3. регистрируется в DB;
4. active revision объекта переключается transactionally.

4.3. Git — не live database

Git может хранить:

* документы;
* process packs;
* generated read projections;
* handoff inbox;
* history snapshots.

Но git commit не является транзакцией Core.

4.4. Generated projections для ChatGPT

Так как web ChatGPT может иметь GitHub-доступ без прямого доступа к локальной SQLite, Core умеет детерминированно генерировать read-only projections.

Например:

projections/
  overview.md
  processes/
    game.md
    health.md
    solmax.md
  work/
    current.md

Каждая projection содержит:

generated_from_revision: ...
generated_at: ...

Projection не является вторым источником истины и может быть полностью пересоздана из DB.

⸻

5. Протокол изменения состояния

Каждая mutation имеет примерно такую семантику:

operation_id: globally_unique
actor: ...
work_id: ...
operation: ...
expected_revision: ...
payload: ...
artifact_hash: ...
provenance: ...
authority_scope: ...
approval_ref: ...

Алгоритм:

1. Validate input schema.
2. Validate Work and authority.
3. Validate expected revision.
4. Check operation_id for duplicate.
5. Validate referenced artifacts.
6. Apply DB mutation in one transaction.
7. Append event in the same transaction.
8. Return receipt with new revision.
9. Rebuild affected projections.

Если одна операция отправлена дважды, второй вызов не повторяет эффект.

Если Work читала revision 10, а объект уже revision 12, изменение не применяется молча.

Возвращается conflict.

⸻

6. Handoff — основная переносимая единица между чатами

Handoff не считать временным костылём.

Он нужен даже после появления прямых интеграций.

Сегодня:

ChatGPT → handoff text/file → Codex

Позже:

ChatGPT → submit_handoff() → Core

Семантика одна.

Пример логической структуры:

kind: handoff
version: 1
handoff_id: ...
process: ...
related_work: ...
intent:
  type: accepted_result
source_state:
  revision: ...
result:
  artifact: ...
  hash: ...
owner_instruction:
  exact_text: ...
constraints:
  - ...
open_questions:
  - ...
created_by:
  surface: chatgpt

6.1. Handoff не является сам себе authority

Файл не может просто написать:

approved: true

и получить права владельца.

Trust определяется каналом доставки.

На первом этапе

Если пользователь сам вставляет Handoff в локальный trusted chat и говорит «обработай», это считается owner-mediated receipt для безопасных внутренних изменений.

Для external / spend / irreversible действий всё равно требуется отдельное точное подтверждение.

6.2. GitHub inbox

Если конкретный web-chat способен писать в пользовательский GitHub, он может при явной команде владельца писать только immutable handoff-файлы:

inbox/
  <handoff-id>.json

Он не должен напрямую править operational projections, permissions или process state.

Локальный Zaratustra importer затем валидирует Handoff.

Если GitHub write недоступен, чат просто выдаёт тот же объект пользователю для copy/paste.

⸻

7. Next Call и начало новой Work

Сохранить удачную часть нынешнего Workflow.

После Work система может сформировать переносимую карточку следующей работы.

Она содержит:

Goal
Expected result
Acceptance
Current source revision
Process
Context handles
Boundaries
Authority
Executor requirements
Budget
Dependencies

Но pasted Next Call никогда не является единственным source of truth.

Новый агент делает:

zara work open <work-id>

Core сверяет текущую revision и собирает свежий context.

Если старая карточка уже выполнена или потеряла актуальность, повторно она не запускается.

⸻

8. Process Pack

Process — долговременная организация определённой сферы работы.

Примеры:

game development
health
research
personal administration
learning

Они не обязаны работать одинаково внутри.

Обязателен только внешний контракт.

Логически Process Pack содержит:

manifest
instructions
skills
optional schemas
optional tools
memory rules
work types
evals
views

Физическая структура может измениться при реализации.

Минимальный внешний контракт Process

Процесс должен позволять получить:

current status
items needing attention
open decisions
available works
blocked works
recent important results
context requirements for a chosen Work

Центральному помощнику не требуется читать все внутренние инструкции процесса для ежедневного обзора.

⸻

9. Skills

Где возможно, использовать переносимые Agent Skills или совместимую с ними структуру вместо собственного сложного формата инструкций.

Но:

Skill ≠ Process.

Skill отвечает на вопрос:

Как выполнять тип работы X?

Process дополнительно содержит:

* долговременное состояние;
* Work;
* память;
* права;
* историю;
* связи;
* пользовательские решения.

⸻

10. Context Compiler

Context Compiler — одна из самых важных частей системы.

Для конкретной Work он собирает:

Work
+
актуальное состояние Process
+
релевантные authoritative decisions
+
релевантную memory
+
явно referenced artifacts
+
необходимые skills
+
доступные tools
+
authority scope
+
budget

Не:

весь user history
+ весь repository
+ все processes
+ все logs
+ все instructions

10.1. Два этапа

Deterministic envelope

Core определяет:

* что вообще разрешено читать;
* что ещё актуально;
* какие revisions нужны;
* какие namespaces разрешены;
* максимальный budget.

Pluggable selection

Внутри допустимого множества можно позже использовать:

* metadata filters;
* lexical search;
* vector retrieval;
* дешёвую модель;
* frontier model.

Selector выбирает контекст, но не получает право менять истину.

10.2. Context manifest

Каждый запуск должен оставлять список:

что было передано модели
какие revisions
какие skills
какие tools
какие memory entries
какой budget

Это необходимо для debugging и evals.

⸻

11. Memory model

Не делать один USER_PROFILE.md, куда AI складывает всё подряд.

Разделить по смыслу.

11.1. Authoritative state

То, что в данный момент принято системой как действующее решение.

Пример:

Feature X approved.

11.2. Episodic memory

Что произошло.

Пример:

2026-09-05 пользователь отклонил вариант A и выбрал B.

11.3. Semantic memory

Выведенные устойчивые сведения.

Пример:

В определённом виде planning пользователь обычно предпочитает сначала итог.

11.4. Procedural memory

Что оказалось хорошим способом работать.

Пример:

Для Concept Lab сначала divergent exploration, затем explicit narrowing.

11.5. Working memory

Временный scratch конкретной Work.

После Work она либо исчезает, либо отдельные результаты становятся нормальными memory candidates.

⸻

12. Требования к memory entry

Значимое производное знание должно иметь:

content
scope
source / provenance
evidence
valid_from
valid_until optional
supersedes optional
status
confidence_in_inference

confidence означает:

насколько хорошо подтверждён вывод системы,

а не:

насколько система уверена, что пользователь «на самом деле такой».

Возможные статусы:

candidate
active
superseded
stale
rejected
deleted

⸻

13. Персонализация

Персонализация не должна означать «научиться говорить то, что пользователю нравится».

Нужно различать:

explicit preferences
inferred preferences
goals / values
working habits
repeated frictions
process-specific rules

13.1. Mismatch Event

Не писать ожидаемую реакцию на каждый ответ.

Вместо этого сохранять значимые расхождения.

Примеры:

"Ты меня неправильно понял."
"Это слишком сложно."
"Я говорил это как пример, а не как requirement."
"Не надо спрашивать подтверждение в этом случае."
"Мы уже несколько раз делали такой план и он не сработал."

Также mismatch может быть объективным:

result failed tests
decision quickly reverted
work repeatedly stalled
actual outcome contradicted assumption

13.2. Learning loop

event
  ↓
possible mismatch
  ↓
candidate explanation
  ↓
similar evidence
  ↓
candidate rule / preference
  ↓
personal eval
  ↓
temporary use
  ↓
promotion or rejection

Один случай не должен создавать пожизненную характеристику пользователя.

13.3. Goal-aware critical assistance

User Model может содержать не только предпочтения подачи, но и проверяемые рабочие гипотезы о recurring friction.

Например:

Observed pattern:
при определённом типе решения пользователь регулярно расширяет scope после
достижения достаточного результата.
Evidence:
...
Possible intervention:
при повторении явно показать стоимость расширения и предложить минимальную
версию, не запрещая пользователю выбрать расширение.

Это гипотеза, а не диагноз личности.

Assistant использует подобные записи, чтобы помогать пользователю противодействовать собственным неэффективным рабочим паттернам, если evidence достаточно сильный.

⸻

14. Anti-sycophancy policy

Для central assistant и decision-oriented processes создать обязательный policy.

Он должен:

* отделять факт от мнения пользователя;
* говорить о слабом основании прямо;
* показывать существенный контраргумент;
* не соглашаться автоматически;
* не расширять идею только потому, что пользователь звучит заинтересованно;
* не путать «хочу попробовать» с «утверждаю»;
* рекомендовать более простой вариант, если дополнительная сложность не имеет доказанной ценности;
* напоминать об известных целях и ограничениях, когда решение им противоречит.

Но он не должен:

* спорить ради спора;
* навязывать собственные цели;
* психологизировать пользователя без evidence;
* превращать каждое сообщение в intervention.

⸻

15. Что система измеряет вместо user happiness

Не использовать один scalar reward.

Хранить независимые dimensions:

task_success
factual_correctness
goal_alignment
preference_fit
friction
cost
safety
user_intervention_required
retries
rework

Они могут конфликтовать.

Например, пользователь может быть недоволен советом, но позже оставить решение, потому что оно оказалось полезным.

Это не отрицательный learning signal автоматически.

⸻

16. Fine-tuning запрещён

В первой и обозримой архитектуре:

NO:
personal model fine-tuning
RLHF on user's conversations
DPO
custom reward model training

Learning происходит через изменения:

memory
process rules
skills
context selection
eval cases
executor routing

⸻

17. Consolidation Jobs — будущий «сон»

Не строить в первой версии.

Архитектура должна позволять позже запускать дешёвые offline jobs.

Light consolidation

index new events
deduplicate
mark superseded entries
detect obvious contradictions
collect repeated mismatch candidates
update generated summaries

Reflection

Только при важном сигнале:

repeated failure
important finished objective
unexpected outcome
several contradictory observations

Результат:

candidate memory
candidate process improvement
candidate personal eval

Reflection не имеет права самостоятельно переписывать цели или high-authority rules.

Precompute

Позже можно заранее готовить:

tomorrow status capsules
likely next contexts
upcoming deadlines
unresolved decisions

⸻

18. Model / executor abstraction

Work не говорит:

use GPT-X

Она говорит:

requirements:
  reasoning: high
  coding: medium
  tool_use: required
  vision: false
  privacy: cloud_allowed
  reliability: high

Отдельный Executor Registry содержит текущие реализации.

Например:

executor A
  supports coding
  supports tools
  tested for architecture
  cost mode: subscription
executor B
  supports coding
  tested for bounded implementation
executor C
  cheap/local
  tested for extraction

⸻

19. Model tiers

Начать с простого правила:

Tier 1
  high uncertainty / architecture / difficult judgement
Tier 2
  normal bounded implementation and analysis
Tier 3
  narrow repetitive semantic work
Deterministic
  no LLM

Tier — требование Work, а не вечное свойство конкретной модели.

Новая модель получает места в tiers только после evals.

⸻

20. Evals

Не строить сложный router сначала.

Сначала создать три уровня evals.

20.1. Core evals — public

Проверяют:

* duplicate Handoff;
* stale revision;
* crash recovery;
* permission denial;
* external action approval;
* context isolation;
* projection rebuild;
* second Process without core changes;
* new session continuation.

20.2. Process evals

Каждый Process Pack имеет свои типовые случаи.

20.3. Personal evals — private

Возникают из реальной работы пользователя.

Например:

User mentioned capability only as future example.
Expected:
assistant must not silently add it to current roadmap.

Или:

There are several plausible tasks, but only one serves the current explicit goal.
Expected:
assistant recommends the goal-serving task rather than maximizing activity.

Личные evals становятся главным способом проверить:

новая модель / skill / инструкция действительно лучше работает именно для этого пользователя?

⸻

21. Model routing

Не делать learned router в MVP.

Сначала:

Work class
   ↓
minimum requirements
   ↓
executors that pass evals
   ↓
cheapest acceptable executor

Цена считается как:

initial execution
+ retries
+ verification
+ corrections
+ user intervention

Не только цена первого model call.

Для неизвестного класса работы разумно сначала использовать сильного исполнителя и получить baseline.

Переводить работу на более дешёвый executor только после evidence.

⸻

22. Authority / autonomy levels

Заложить модель сейчас, полностью автоматизировать позже.

DISCUSS
  read + reason
PROPOSE
  create proposed mutations / artifacts
WORKSPACE
  change pre-authorized local scope
WORKFLOW
  create and execute child Works inside delegation
EXTERNAL
  external/spend/irreversible actions under explicit policy

Исполнитель не может сам повысить свой уровень.

⸻

23. Delegation Scope

Будущая автономная работа начинается не с «агенту можно всё».

Пользователь утверждает:

goal
done_when
allowed scope
forbidden changes
budget
available executors
external effect policy
stop conditions

После этого:

Planner
  ↓
small Works
  ↓
fresh executor sessions
  ↓
verification
  ↓
integration
  ↓
next Work

Stop при:

* изменении approved concept;
* выходе за authority;
* недостаточном budget;
* невозможности проверить result;
* повторяющемся failure;
* необходимости external irreversible action.

⸻

24. Инструменты

Core operations должны быть семантически узкими.

Примеры:

open_work
submit_result
record_decision
append_observation
propose_memory
import_handoff
request_approval
get_process_status
build_context

Не давать один универсальный:

edit_anything(path, patch)

для управляемого состояния Zaratustra.

Но обычный coding agent может пользоваться shell/editor/git внутри разрешённого project sandbox.

Zaratustra не должна заменять IDE.

⸻

25. CLI / MCP / API

Core должен существовать как обычная Python library/service.

Поверх него:

CLI
MCP adapter
future HTTP API
future frontend adapter

MCP — transport, не архитектура Core.

Начать с CLI.

MCP добавить после доказательства основного flow.

⸻

26. Open-source продукт

Один публичный repository:

zaratustra/
  core/
  cli/
  schemas/
  migrations/
  adapters/
  process_sdk/
  example_processes/
  evals/
  docs/

Реальная пользовательская workspace выбирается самим пользователем.

<any folder>/
  .zara/
  processes/
  artifacts/
  projections/
  inbox/

Продукт не предполагает специального репозитория конкретного владельца.

Workspace может быть Git repository, если пользователь этого хочет.

⸻

27. Предлагаемый стек MVP

Не открывать новый архитектурный спор без evidence.

Использовать:

Python 3.13
uv
SQLite through sqlite3
Pydantic v2 for boundary schemas
pytest
ruff
SHA-256 artifact hashes

Для SQLite migrations сначала достаточно собственного явного последовательного migration mechanism.

Не нужны сейчас:

Postgres
Redis
vector database
message broker
Kubernetes
web framework
distributed event bus

⸻

28. Первая работающая версия

Первая Zaratustra должна доказать один сквозной сценарий.

1. zara init в пустой папке.
2. Создать один тестовый Process.
3. Создать Work.
4. Скомпилировать context.
5. Открыть Work в одном AI chat.
6. Получить Handoff / Result.
7. Импортировать Result.
8. Изменить state.
9. Создать следующую Work.
10. Открыть новый чистый chat.
11. Новый chat правильно понимает текущее состояние без пересказа.

Дополнительно проверить:

import одного Handoff два раза → один эффект;
stale revision → conflict;
crash во время mutation → согласованное state;
Work без permission → отказ;
context другого Process не попал в Work;
audit показывает, что произошло.

До прохождения этого сценария не строить personalization, router, frontend или autonomous agents.

⸻

29. Milestone 0 — Foundation

Результат

Работающий Core с:

workspace
SQLite state
Process registration
Work
Artifact
Event/history
Mutation
Handoff
Context manifest
CLI
generated projections

Acceptance

Все проверки из раздела 28 проходят.

Stop condition

Если для прохождения первого сценария приходится:

* напрямую редактировать DB;
* напрямую править state Markdown;
* делать process-specific exception в Core;
* доверять старому pasted context без revision check;

остановиться и исправить foundation.

⸻

30. Milestone 1 — Modularity

Добавить два очень разных fictional Processes.

Например:

software project

и

recurring personal process

Они нужны как тест, не как готовые product templates.

Acceptance

Второй Process добавлен без изменения основной семантики Core.

Central status view показывает оба через одинаковый внешний contract.

⸻

31. Milestone 2 — Реальный dogfood

Создать первый настоящий пользовательский Process.

Не переносить весь Workflow.

Выбрать один реально используемый поток, где можно быстро почувствовать ценность.

Цель:

пользователь несколько реальных Works подряд
выполняет через Zaratustra
и продолжает их между новыми сессиями.

Если продукт не используется, дальнейшая архитектура приостанавливается.

⸻

32. Milestone 3 — Basic personalization

Добавить:

episodic memory
semantic candidates
explicit preferences
mismatch events
provenance
supersession

Без automatic reflection.

Acceptance

Можно спросить:

Почему система считает это моей preference?

и получить конкретные evidence references.

Ошибочный inference можно удалить или supersede.

⸻

33. Milestone 4 — Personal evals

Из реальных recurring ошибок создать первый небольшой private eval suite.

Не стремиться сразу к сотням случаев.

Начать с реальных failure modes.

После накопления данных расширять.

Только после этого начинать системно сравнивать executors.

⸻

34. Milestone 5 — Executor routing

Создать Executor Registry.

Для каждого значимого Work class хранить результаты evals.

Routing:

capability fit
+ privacy fit
+ quality threshold
+ budget availability
→ cheapest passing executor

Если evidence нет — не выдумывать экономию.

⸻

35. Milestone 6 — Central assistant

Теперь появляется полноценный повседневный помощник.

Он получает только status capsules Processes и общий user context.

Может:

утренний overview
план дня
cross-process conflict detection
owner decisions
recommendations
routing to a Process

Содержательное решение принимает AI.

Core только предоставляет достоверное состояние.

⸻

36. Milestone 7 — Consolidation

Когда накопится достаточно реального материала, добавить:

cheap consolidation
mismatch clustering
candidate preferences
procedural candidates
personal eval generation
selected reflection

Никакого fine-tune.

Никакого automatic rewrite целей пользователя.

⸻

37. Milestone 8 — Frontend

Только теперь добавлять собственный UI.

Сначала:

Today
Processes
Works
Decisions
Chat

Потом при реальной нужде:

Kanban
whiteboard
calendar
charts
custom widgets

Все они являются views над Core.

⸻

38. Milestone 9 — Autonomous workflows

После доказательства:

Work
context
permissions
verification
routing

можно разрешить большие delegation scopes.

Например:

"Эта node игры утверждена.
Довести до playable result.
Не менять concept.
Бюджет X.
При blocker остановиться."

Planner сам создаёт Works.

Каждая выполняется в отдельной свежей сессии.

Проверяемые результаты двигают workflow дальше.

Неопределённость возвращается пользователю.

⸻

39. Что сознательно НЕ строим сейчас

fine-tuning
custom personalized model weights
dopamine scalar reward
prediction реакции на каждый ответ
multi-agent swarm
learned model router
vector DB
AI sleep daemon
large frontend
whiteboard
mobile app
Telegram
voice
distributed sync
automatic external actions
complex plugin marketplace

Архитектура должна позволять их добавить, если реальная потребность появится.

Но они не должны быть prerequisite.

⸻

40. Критические доказательства архитектуры

До масштабирования должны быть доказаны пять вещей.

Proof A — Continuity

Новый чистый chat продолжает работу без ручного пересказа.

Proof B — Transport independence

Один и тот же Handoff работает через copy/paste и через автоматическую интеграцию.

Proof C — Process independence

Радикально другой Process подключается без изменения Core.

Proof D — Mutation correctness

Duplicate, stale revision и crash не портят state.

Proof E — Personalization integrity

Система умеет адаптироваться к пользователю, не превращая disagreement в negative reward и не оптимизируя соглашательство.

⸻

41. Первый порядок работ для Codex

Не пытаться реализовать весь документ.

Работать строго последовательно.

Work 1 — Repository foundation

Создать минимальный проект:

core
cli
tests
docs

Поднять SQLite и migration v1.

Реализовать workspace init.

Work 2 — Core records

Минимально:

Process
Work
Artifact
Event

Не считать этот список священным.

Добавить revisions.

Work 3 — Mutation protocol

Добавить:

operation_id
expected_revision
transaction
event receipt
idempotency

Написать failure tests.

Work 4 — Artifacts + projections

Versioned artifacts.

Generated read-only projections.

Work 5 — Handoff

Schema.

Import from file/stdin.

Duplicate protection.

Stale state handling.

Work 6 — Work context

open_work

Context manifest.

Process isolation.

Work 7 — Result

submit_result

State mutation.

Receipt.

Next Work reference.

Work 8 — End-to-end proof

Один fictional Process.

Полный сценарий:

discussion
→ Handoff
→ import
→ Work
→ Result
→ new clean session

После Work 8 остановиться.

Не автоматически продолжать Milestone 1.

Сначала предъявить реальный сценарий пользователю.

⸻

42. Definition of success первой итерации

Первая итерация успешна не тогда, когда:

есть много abstractions;
есть красивый CORE.md;
есть 200 tests;

а когда пользователь реально может сделать:

обсудить вопрос в ChatGPT
→ зафиксировать результат
→ перенести его в Codex
→ продолжить работу
→ открыть новый чистый chat
→ не объяснять всё заново.

И система при этом может доказать:

что было принято;
кто и на основании чего изменил state;
какая revision действовала;
какой результат получился;
что стало следующим шагом.

⸻

43. Главное правило разработки

При выборе между:

ещё одной архитектурной абстракцией

и

работающим проверяемым vertical slice

по умолчанию выбирать vertical slice.

Расширять Core только когда реальная работа доказывает, что текущего контракта недостаточно.

Не проектировать заранее все будущие процессы.

Не оптимизировать будущую автономность до появления надёжной обычной Work.

Не строить персонализацию до появления реальных повторяющихся interaction data.

Не строить model routing до появления eval data.

⸻

44. Инструкция Codex перед началом

Если этот документ передан Codex в репозитории Direction OS:

1. перечитать актуальный KERNEL/NOW/solmax state;
2. не редактировать Direction OS state напрямую;
3. считать старую Wave 0 архитектуру кандидатом на supersede, а не автоматически действующей новой спецификацией;
4. оформить изменения через предусмотренный Direction OS writer flow;
5. не начинать продуктовую реализацию раньше корректного перехода состояния.

Если документ передан уже в отдельный product repository Zaratustra:

1. реализовывать только Milestone 0;
2. не строить ничего из milestones 1+;
3. не принимать необратимые архитектурные решения, которые не требуются первому vertical slice;
4. после первого end-to-end сценария остановиться и предъявить результат владельцу.

END.

END_OF_FILE: live/solmax/work/zaratustra-architecture-plan-2026-09-05.md
