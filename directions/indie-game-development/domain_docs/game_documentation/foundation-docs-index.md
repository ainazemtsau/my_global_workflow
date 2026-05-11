# Foundation Docs Index

## Foundation Docs Index

## purpose

Эта note фиксирует текущую карту authoritative foundation-документов и durable game documentation по новой игре.

Она нужна для того, чтобы человек и AI быстро понимали:

- где лежит текущая truth по игре;
- где лежит текущая technical foundation truth;
- где лежит текущая selected product-bet truth;
- где лежит текущая experience model truth;
- где лежит proof handoff для следующего Goal;
- какие документы являются навигацией, а не источником истины.

Эта note не заменяет сами foundation-docs и не хранит их содержание у себя. Она только показывает, какие notes сейчас authoritative и как с ними работать.

## authoritative foundation docs

### 1. Game Foundation

Path: Directions/Indie Game Development/Game Documentation/Game Foundation

What it is: Главная компактная foundation-note по игре.

What is authoritative there:

- purpose игры на foundation-уровне;
- concept spine;
- first product hypothesis;
- non-goals.

Use this note when: Нужно понять, что это за игра на foundation-уровне, что она обещает игроку и чего сознательно не утверждает.

### 2. Technical Foundation — Gas and Grid Contract

Path: Directions/Indie Game Development/Game Documentation/Technical Foundation — Gas and Grid Contract

What it is: Главная technical foundation-note по зависимости Gas ↔ Grid.

What is authoritative there:

- peer foundation line;
- Gas-owned responsibilities;
- Grid-owned responsibilities;
- shared contract surfaces;
- non-owned responsibilities.

Use this note when: Нужно понять, как честно устроен текущий spatial/gas foundation и что именно нельзя трактовать изолированно.

### 3. Clean-start Transfer Boundary

Path: Directions/Indie Game Development/Game Documentation/Clean-start Transfer Boundary

What it is: Главная boundary-note нового clean start.

What is authoritative there:

- rules of transfer;
- named starting set;
- transfer-later;
- reference-only;
- do-not-carry;
- GridV2 line;
- explicit exclusions;
- unresolved but allowed unknowns.

Use this note when: Нужно понять, что переносится как foundation нового старта, а что нет.

## authoritative product-bet docs

### 4. Primary Product Bet — Expedition

Path: Directions/Indie Game Development/Game Documentation/Primary Product Bet — Expedition

What it is: Главная durable note по выбранной primary product bet.

What is authoritative there:

- selected primary bet;
- rejected alternative;
- why Expedition won;
- why Containment was rejected as primary;
- stable product identity;
- locked run/session structure;
- locked minimum action contour;
- locked procgen function;
- locked reaction grammar status;
- locked harm / friendly-fire status;
- main non-goals and anti-audience.

Use this note when: Нужно понять, на какую версию игры теперь ставит Direction, почему именно на неё, и что не является этой игрой.

### Expedition Experience Model

Path: Directions/Indie Game Development/Game Documentation/Expedition Experience Model

What it is: Главная locked experience-model note выбранной Expedition bet.

What is authoritative there:

- core loop;
- tension source;
- session/run structure;
- minimum action contour;
- role of gas as core of experience;
- role of gas types and reactions;
- role of topology/grid;
- role of procedural generation;
- co-op pattern;
- harm / friendly-fire pattern;
- player/value promise;
- non-goals;
- anti-audience.

Use this note when: Нужно проектировать, планировать или проверять следующий Goal так, чтобы он проверял именно Expedition experience, а не loose gas sandbox, Containment, tech demo или full game design.

### Expedition Skeleton Document

Path: Directions/Indie Game Development/Game Documentation/Expedition Skeleton Document

What it is: Главная durable skeleton-note по минимальному доказуемому игровому скелету Expedition.

What is authoritative there:

- selected skeleton hypothesis: Нарастающая экспедиционная ставка;
- one-line Expedition skeleton;
- main causal chain;
- local expedition loop;
- between-run value / consequence layer;
- dangerous gas-vessel value;
- gas as decision pressure;
- tools as risky capital roles;
- map / generation as route uncertainty and retreat pressure;
- lift as physical bridge / extraction / risk concentration;
- 4-player-first co-op lens;
- loss / partial success / no-return boundary;
- foundation commitments;
- allowed placeholders;
- deferred hypotheses;
- decision queue;
- first proof meaning boundary;
- forbidden directions for this skeleton.

Use this note when: Нужно shape-ить, планировать или проверять следующий Goal так, чтобы он работал с минимальным Expedition skeleton, а не с isolated gas demo, disconnected feature set, premature full design or archived Goal artifact.

### Expedition Proof Handoff

Path: Directions/Indie Game Development/Game Documentation/Expedition Proof Handoff

What it is: Главная handoff-note для следующего downstream proof Goal.

What is authoritative there:

- one proof question;
- link to locked Expedition bet;
- what the next Goal checks;
- what remains scope out / hypothesis material;
- boundary against prototype/design/metrics/backlog expansion before a proper proof Goal.

Use this note when: Нужно выбрать, shape-ить или планировать следующий Goal, который будет проверять selected Expedition bet.

## related direction-level docs

### direction-context.md

Path: Project file: direction-context.md

What it is: Direction-level context, thesis, current trajectory, completed goals, current phase and canon snapshot.

Use this note when: Нужно понять direction-level контекст, current phase, completed goals and canonical constraints, а не детальную game truth.

### 8. Canon

Path: Directions/Indie Game Development/Canon/

What it is: Жёсткие правила, пережившие отдельные Goals.

Use this note when: Нужно понять, какие правила уже нельзя тихо нарушать.

Current relevant Canon includes:

- Gas is not an isolated transferable asset; foundation is Gas ↔ Grid peer dependency contract.
- Game-truth that survives a Goal and is needed later must be promoted into durable documentation.
- Strong rejected alternatives must be steelman-read before primary product bet decision.
- Before proof-building, separate selected bet commitments, proof slice boundary and deferred design hypotheses.

### 9. Knowledge

Path: Directions/Indie Game Development/Knowledge/

What it is: Полезные наблюдения и рабочие выводы, которые не тянут на Canon.

Use this note when: Нужно понять useful patterns and working methods without turning them into hard rules.

Current relevant Knowledge includes:

- Bounded output contract for upstream shaping.

## update rules

Each authoritative document is updated only in its own home-note.

This index does not override the content of foundation-docs, product-bet docs, Canon, Knowledge, Archive or Project files.

If game truth changes, update the corresponding source note, not this index alone.

Canon updates happen in Canon notes and are reflected in direction-context.md during S7/S_SF project-file rebuild.

Knowledge updates happen in corresponding Knowledge notes.

Session logs, review gates, workspace notes and archive notes do not override current truth.

## non-authoritative materials

The following materials are not current game truth:

- Archive Goal notes;
- review gates;
- workspace notes;
- source-boundary / admissibility notes;
- session logs;
- context bundles;
- chat threads;
- intermediate drafts.

They are history, proof and working trace. They are not the primary source for future Goals.

## current archive sources

Current foundation-docs originate from closed Goal:

Сформировать minimum viable foundation новой игры: concept spine, first product hypothesis, clean-start boundary и minimal documentation/workflow contract

Current product-bet docs originate from closed Goal:

Выбрать одну primary product bet через evaluation frame и explicit experience model

Archive Goals preserve materialization / review / lock history, but they do not replace the permanent notes above.
