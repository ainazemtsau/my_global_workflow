# Demo-Driven Design & Canon Workflow v1

status: OWNER-APPROVED PROCESS
approved_on: 2026-07-22
owner_verdict: "ПРИНИМАЮ DEMO-DRIVEN DESIGN & CANON WORKFLOW V1"
authority: |
  Binding Direction design-routing process for gameplay and visual design.
  It preserves accepted Frames and canon, does not define game content, and
  does not replace Launch Control ownership of the Demo Contract.
supersedes: |
  Question-first Canon routing, the current-question-front as scheduler,
  READY/NEXT inference and automatic successor routing.

## Назначение

Направлять дизайн от целого публичного demo к необходимой детали и не
позволять отдельному готовому или разблокированному вопросу становиться
текущей работой без доказанной связи с demo.

Этот документ не определяет фактические сцены, биты, механику или содержание
Demo Contract. Он определяет только порядок, authority и маршрутизацию работы.

## 1. Верхний источник направления — Demo Contract

**Demo Contract** — корневой вход процесса.

Его владельцем остаётся **Launch Control**. Canon не переписывает Demo
Contract и не выбирает release scope самостоятельно.

Demo Contract отвечает:

- что публичное demo обещает игроку;
- что оно обязано доказать;
- что относится к `MUST / SHOULD / CUT`;
- какая действует нижняя граница качества;
- какие утверждения разрешено делать публично;
- каким внешним доказательством demo принимается.

Demo Contract не обязан определять точную механику. Его задача — задать
проверяемое player-facing целое, из которого выводится необходимая
дизайн-работа.

Ни Frame, ни canon card, ни старый вопрос, ни техническая возможность сами
по себе не могут стать корнем текущей дизайн-работы.

## 2. Demo Experience Tree

Работа раскладывается только сверху вниз по одной последовательности:

`demo → experience spine → beat / situation → observable outcome →
required capability → decision gap → evidence / build`

### Demo

Принятый Demo Contract целиком.

### Experience spine

Крупная последовательность переживания игрока, необходимая для выполнения
Demo Contract.

Она отвечает:

> Какой связный опыт должен пройти игрок, чтобы demo действительно исполнило
> обещание?

В этой сессии конкретный spine не определяется.

### Beat / situation

Одна ограниченная игровая ситуация внутри spine.

Она отвечает:

> В какой конкретной ситуации игрок должен что-то понять, решить, сделать
> или пережить?

### Observable outcome

Наблюдаемый результат ситуации.

Он формулируется через игрока или измеримое поведение:

- что игрок увидел;
- что понял;
- какое решение принял;
- какое действие выполнил;
- как изменилась ситуация;
- чем это можно подтвердить.

Не допускается outcome вида «система реализована» без player-visible или
проверяемого эффекта.

### Required capability

Способность дизайна или продукта, без которой observable outcome невозможен.

Например, это может быть:

- понятное правило;
- системное поведение;
- визуальное различие;
- элемент пространства;
- техническая возможность;
- интерфейсный канал;
- воспроизводимая сборка.

Capability не становится текущей работой только потому, что она полезна игре
вообще.

### Decision gap

Точное нерешённое решение, которое мешает определить, построить или принять
required capability.

Decision gap обязан указывать:

- какой capability он блокирует;
- какой observable outcome из-за этого не доказан;
- какой beat и spine являются родителями;
- что решается;
- что не решается;
- какая принятая design truth ограничивает ответ;
- каким evidence mode решение может созреть.

### Evidence / build

Минимальная бумажная, визуальная, продуктовая или внешняя работа, необходимая
для проверки конкретного утверждения узла.

Evidence не является отдельным roadmap. Оно существует только как дочерняя
работа exact decision gap, capability или outcome.

## 3. Строгое правило parent trace

Никакая gameplay- или visual-design работа не может стать активной без одного
из двух оснований:

1. существует полный принятый путь от этой работы до Demo Contract; или
2. владелец дал один явный override.

Полный путь означает, что приняты и названы все звенья:

`Demo Contract
→ experience spine
→ beat / situation
→ observable outcome
→ required capability
→ decision gap`

Наличие старого вопроса, принятого Frame, canon card, технического
prerequisite, статуса `READY` или полезности для полной игры не заменяет этот
путь.

### Owner override

Override допустим только с точными словами владельца и обязан содержать:

- какой узел открывается;
- какого принятого родителя пока нет;
- почему работа всё же открывается сейчас;
- какой результат должен либо создать отсутствующего родителя, либо вернуть
  работу в suspended state;
- когда override истекает;
- подтверждение, что override не открывает соседние вопросы и не становится
  прецедентом.

Override не делает отсутствующего родителя принятым и не создаёт
автоматическую ветку продолжений.

## 4. Parent-first expansion

Дерево расширяется только от принятого родителя.

Если родитель не определён, спорен или не принят:

- потомок может быть сохранён как исторический вопрос или capture;
- он может быть помечен как `blocked by missing parent`;
- по нему нельзя запускать сравнение вариантов, изображения, прототип или
  реализацию;
- его техническая готовность ничего не меняет.

Нельзя проектировать потомка, чтобы задним числом угадать родителя.

Если во время работы обнаружен скрытый родительский пробел, текущая работа
останавливается и возвращается к этому пробелу. Она не перескакивает к
следующему готовому вопросу.

## 5. В дереве нет `READY → NEXT`

Demo Experience Tree хранит структуру и принятую связь, но не очередь
исполнения.

В нём запрещены значения и выводы:

- `NEXT`;
- `READY FIRST`;
- `READY PARALLEL`;
- «следующий после закрытия X»;
- автоматический приоритет из порядка расположения;
- автоматический запуск потомка после закрытия prerequisite.

Полный parent trace создаёт только **структурную допустимость**.

Текущей работой узел становится лишь после отдельного явного выбора и
регистрации CALL.

## 6. Закрытие prerequisite ничего автоматически не запускает

Когда decision gap, capability или evidence закрываются:

1. результат записывается;
2. родительский observable outcome пересматривается;
3. Launch Control и владелец оценивают Demo Contract, текущий milestone,
   риски, cuts и другие допустимые ветки;
4. только затем выбирается новая работа либо не выбирается ничего.

Даже единственный оставшийся допустимый потомок не становится текущим
автоматически.

Слова `unblocked`, `eligible`, `available` и `structurally valid` не означают
`selected` или `active`.

## 7. Canon Decision Ledger

**Canon Decision Ledger** отвечает только на вопрос:

> Что принято, в каком scope, с какой authority и чем это основано?

Он не отвечает:

> Что делать следующим?

Ledger отделён от планирования, приоритета и расписания.

### Минимальные поля записи

- statement;
- exact scope;
- authority;
- linked Demo Experience Tree nodes, если применимо;
- owner verdict;
- source;
- evidence limit;
- replaces / supersedes;
- unresolved dimensions.

### Authority

Запись явно различает:

- принятый Frame;
- owner-selected paper или visual decision;
- admitted canon;
- superseded decision.

Принятое не копируется между классами authority автоматически.

### Запрещённые поля и функции

Ledger не содержит:

- `READY`;
- `NEXT`;
- priority;
- schedule;
- current task;
- dispatch instruction;
- автоматического successor;
- очереди нерешённых вопросов.

### Текущая реализация

Существующие `INDEX.md` и карточки `c-001`, `c-002`, `c-003` остаются
действующей канонической частью Ledger и не переписываются этим workflow.

Minimum Game Frame v2 и Sphere Frame остаются принятыми Frame-источниками и
подключаются ссылками, не копируются и не становятся каноном.

## 8. NOW и CALL зеркалят активную parentage

Demo Experience Tree показывает смысловую иерархию. `NOW.md` и CALL показывают
только явно выбранное исполнение.

Каждый gameplay- или visual-design CALL обязан назвать полный demo path
обычными словами:

`Demo Contract → spine → beat → observable outcome → capability →
decision gap`

Внутри одного трека дочерние evidence/research CALL должны быть parented к
CALL того gap или capability, которому они служат.

Между треками не создаются незаконные cross-track children. Вместо этого:

- Launch Control формулирует требуемый release outcome;
- owning track открывает свой lawful root;
- оба артефакта ссылаются на один точный Demo Experience Tree path.

В Canon одновременно может существовать не более одного выбранного root
design gap. Остальные вопросы остаются неактивными независимо от структурной
допустимости.

Если закрывается текущий CALL, локальный handoff может быть выдан только через
`RESULT.next` и зарегистрирован как явный `open_calls` root того же трека.
Он не выводится из дерева, не создаёт глобальный selector/focus и сам по себе
не запускает работу.

## 9. Visual work является частью дерева

Visual work не имеет самостоятельной очереди или visual roadmap.

Каждое изображение, diagram, sequence, mockup, reference или comparison set
привязывается к:

- точному Demo Experience Tree node; либо
- точному decision gap этого узла.

Visual artifact обязан назвать, какое player-visible различие, отношение,
состояние или решение он помогает определить.

Минимальные metadata:

- `linked_node`;
- `purpose`;
- `status: scratch | candidate | selected | superseded | evidence`;
- `source`;
- `accepted_rules`;
- `non_binding`.

Продолжают действовать правила `c-003`:

- binding становятся только явно перечисленные rules и relations;
- placeholder не получает скрытой authority;
- неперечисленные generated details остаются accidental;
- выбранная картинка не становится целиком каноном;
- reference не становится production asset автоматически;
- runtime legibility, fun, performance и production cost требуют отдельного
  evidence.

Исторические изображения без нового node link остаются evidence-only. Старый
gas visual остаётся invalid target / negative evidence only.

## 10. Markdown-first visual portal

Authoritative информация существует только в:

1. Demo Experience Tree;
2. Canon Decision Ledger;
3. media-файлах и минимальных node-linked metadata;
4. `NOW.md` и CALL для текущего исполнения.

Generated multi-page portal является read-only представлением.

Он может показывать:

- Demo Contract;
- путь от целого demo к деталям;
- страницы spine и beat;
- observable outcomes и gaps;
- Ledger entries;
- visual comparisons и media;
- evidence;
- generated management views, отдельно определённые Launch Control.

Portal:

- ничего не принимает;
- ничего не dispatch’ит;
- не хранит уникальную authority;
- не является вторым состоянием;
- может быть полностью удалён без потери design truth.

Markdown и обычные media-файлы остаются переносимыми и renderer-independent.

**Zensical** — только первый кандидат renderer pilot. Он не является
постоянной зависимостью.

Сейчас не открываются:

- portal implementation;
- установка Zensical;
- custom web application;
- Trilium или Notion как authority;
- AI image pipeline;
- sound pipeline;
- hosting, CI, theme или production styling.

## 11. Evidence lanes

Каждое утверждение получает самый дешёвый подходящий evidence mode. Evidence
привязано к точному node и claim.

### Paper

Подходит для:

- смысла;
- терминов;
- ограничений;
- причинной модели;
- сравнения вариантов;
- проверки согласованности с Frame и canon.

Не доказывает fun, реальное поведение игроков или runtime legibility.

### Visual

Подходит для:

- формы;
- визуального отношения;
- последовательности;
- информационной иерархии;
- visual hypothesis;
- сравнения читаемых состояний.

Не доказывает фактическую читаемость в движении или стоимость исполнения.

### Prototype

Подходит для:

- interaction;
- системного поведения;
- физической причинности;
- технической осуществимости;
- ограниченного experiential claim.

Не доказывает автоматически, что реальные игроки понимают или любят
результат.

### Playtest

Подходит для наблюдения:

- понимания;
- решений;
- ошибок;
- кооперации;
- communication;
- fun;
- recovery;
- повторяемости поведения.

Результат ограничен конкретной сборкой, сценарием и составом участников.

### Performance evidence

Подходит для измерения:

- frame time;
- memory;
- simulation cost;
- network behavior;
- stability;
- min-spec соответствия.

Оно требует названного hardware, build и нагрузки.

### External evidence

Подходит для:

- понятности публичного обещания;
- playtest recruitment;
- market response;
- wishlist, funding или paid-validation signal;
- внешней реакции на demo.

Внешний интерес не превращает неподтверждённую механику в canon.

## 12. Обращение с существующей truth и историей

### Принятый canon

`c-001`, `c-002`, `c-003` сохраняются без изменений.

Они ограничивают допустимые решения там, где применимы, но не создают текущую
работу.

### Minimum Game Frame v2

Сохраняется как current owner-approved whole-game Frame, не canon.

Его открытые вопросы не мигрируют в Demo Experience Tree автоматически.

### Sphere extraction/custody Frame

Сохраняется как owner-approved specialized Frame, не canon.

Он не становится demo scope и не активирует свои открытые dimensions.

### CORE и CONSTITUTION

Game-design truth, pillars, anti-loss rules и accepted direction сохраняются.

Однако прежняя процессная возможность активировать downstream detail до
принятого родителя не может использоваться как текущая routing permission.
После принятия workflow этот конфликт должен быть исправлен точной
process-routing amendment без изменения game-design truth.

### Старые question maps

Сохраняются как историческая dependency и provenance evidence.

Они не являются scheduler, backlog или источником `NEXT`.

### Нерешённые вопросы

Не удаляются и не объявляются неправильными.

Они остаются unparented inventory до тех пор, пока будущая работа не создаст
для конкретного вопроса полный принятый demo path.

Автоматической миграции нет.

### Исторические media

Сохраняются.

Без fresh selection и exact node link они являются historical reference,
scratch или negative evidence согласно `c-003`.

## 13. Замена старых process surfaces

| Поверхность | Disposition | Точный эффект |
|---|---|---|
| `local/canon-forge` | **SUPERSEDE как routing authority; PRESERVE как исторический процесс до установки replacement play** | Полезные controls — bounded question, readiness, comparable candidates, owner selection и отдельный canon admission — переносятся в работу над exact decision gap. Forge больше не выбирает вопрос и не запускается из QUEUE |
| `local/canon-cartography` | **SUPERSEDE как самостоятельный question-front builder; PRESERVE dependency/gap techniques** | Dependency analysis применяется только при расширении конкретного принятого parent node; отдельный граф всех вопросов больше не управляет текущей работой |
| `g-d3a8-current-question-front-v3.md` | **SUSPEND сейчас; SUPERSEDE как scheduler после принятия workflow; PRESERVE как history** | Ни `READY`, ни `NEXT`, ни dependency order из файла не dispatch’ят работу |
| canon `QUEUE.md` | **SUPERSEDE как queue/routing surface; PRESERVE как process receipt до точной amendment** | Canon repo больше не объявляет следующий вопрос; допустимо только сообщать, что активного design question нет, и ссылаться на Direction workflow |
| canon `CONSTITUTION.md`, process rule permitting downstream-first work | **SUPERSEDE только как scheduling permission; PRESERVE все design pillars и canon authority** | Точный текст amendment должен установить parent trace либо explicit owner override; game-design решения не меняются |
| `INDEX.md` и `c-001..c-003` | **PRESERVE** | Остаются accepted canon authority |
| Minimum Game Frame v2 и Sphere Frame | **PRESERVE** | Остаются Frames, не scheduler и не canon |
| Старые вопросы и maps | **PRESERVE + SUSPEND** | История и inventory без права запуска |
| Historical media | **PRESERVE** | Evidence-only, пока не reselected и не linked |
| Generated portal output | **DELETE/REGENERATE разрешены** | В нём нет уникальной истины |
| Authority-bearing или historical source files | **DELETE: NONE** | История не уничтожается |

## 14. Negative walkthroughs

### Тест 1 — V1: visual readability Counter / Brake / Time

Старый question front называет V1 `READY` и прежним `NEXT`.

По новому workflow этого недостаточно.

Сейчас отсутствует принятый путь:

`Demo Contract
→ accepted experience spine
→ accepted beat
→ observable outcome, требующий различить Counter / Brake / Time до
  последствия
→ required readability capability
→ V1 decision gap`

`c-002`, `c-003` и Sphere Frame дают допустимые constraints, но не создают
parentage.

Поэтому V1:

- сохраняется;
- не считается ошибочным;
- не активируется;
- не генерирует изображения;
- не становится текущим после закрытия visual-contract prerequisite.

Открыть V1 можно только после принятия полного пути либо exact owner override.

**Результат теста: V1 не может стать current.**

### Тест 2 — E0: safe-return conversion

Старый question front считает вопрос технически готовым.

Demo Contract сейчас требует понятный результат попытки, но полный
economy/progression относится к CUT. Ни один принятый demo beat пока не
требует, чтобы физически возвращённый газ превращался в durable run power
именно внутри demo.

Следовательно, отсутствуют:

- parent beat;
- observable demo outcome;
- required conversion capability.

Accepted Frame truth о безопасном возврате сохраняется, но не является
расписанием.

**Результат теста: E0 не может стать current.**

### Тест 3 — C0: paper design of 4–8-player cooperation

Полная игра обязана поддерживать меняющийся состав 4–8 игроков. Эта truth
сохраняется.

Но текущий Demo Contract требует минимум двух игроков и хотя бы один момент,
где cooperation меняет результат; full eight-player proof относится к CUT.

Пока не принят конкретный demo beat и outcome, требующий более подробной
4–8-player composition, весь C0 остаётся full-game question без demo parent.

Общая важность co-op и старый статус `READY` не позволяют его запустить.

**Результат теста: C0 не может стать current.**

Эти тесты доказывают главное:

> Принятая истина и техническая готовность сохраняются, но больше не
> превращаются в текущую работу без demo parent.

## 15. Минимальный пилот

Пилот проводится только после появления будущего реального owner-approved
Demo Contract. Этот документ его не проектирует.

### Pilot input

- один принятый Demo Contract;
- текущие Frames;
- текущий canon;
- отсутствие автоматически мигрированных вопросов.

### Pilot sequence

1. Launch Control показывает владельцу один proposed experience-spine node.
2. После его принятия показывается один beat/situation.
3. После принятия beat формулируется один observable outcome.
4. Из outcome выводится одна required capability.
5. Только затем формулируется один decision gap.
6. Gap получает один минимальный подходящий evidence mode.
7. По gap проводится один owner-present resolution cycle.
8. После результата родительский outcome пересматривается.
9. Никакой successor не запускается автоматически.

Каждый parent artifact принимается отдельно; пилот не проектирует всё дерево
заранее.

### Negative controls пилота

Пилот проходит только если одновременно доказано:

- один старый `READY` вопрос остаётся неактивным;
- отсутствующий parent действительно блокирует потомка;
- закрытие gap не запускает следующий;
- visual material невозможно сохранить без exact node link и
  binding/non-binding правил;
- Ledger не содержит priority или `NEXT`;
- удаление generated portal не удаляет authority;
- Launch Control остаётся владельцем Demo Contract;
- Canon не становится release scheduler.

### Pilot pass

Пилот принят, если владелец может обычными словами показать путь:

> «Вот обещание demo; вот нужный опыт; вот ситуация; вот наблюдаемый
> результат; вот capability; вот точный нерешённый gap; вот почему именно эта
> работа нужна сейчас».

Если путь нельзя показать без ссылок на «вопрос давно готов» или
«prerequisite закрылся», пилот не пройден.

## 16. Operating rule в одной фразе

> **Мы не выбираем следующий готовый дизайн-вопрос. Мы идём от принятого
> целого demo вниз до первой точной неизвестности, которая мешает доказать
> конкретный player-visible результат.**

## 17. Основания проекта

Проект построен на:

- текущих owner instructions из CALL;
- accepted Launch Control authority и Demo Contract;
- текущих `NOW.md`, `TREE.md`, `CHARTER.md`;
- Minimum Game Frame v2;
- Sphere extraction/custody Frame;
- accepted canon `c-001`, `c-002`, `c-003`;
- suspended current-question-front v3;
- принятом Markdown-first Visual Portal Contract v1;
- evidence о провале question-first routing;
- ограничениях Direction OS: отдельные authority, owner verdict, отсутствие
  прямой записи и отсутствие автоматического successor.

Никакого game-design ответа, изображения, portal implementation, product
change или `os/**` mutation этот документ не содержит.

END_OF_FILE: live/indie-game-development/work/demo-workflow/demo-driven-design-canon-workflow-v1.md
