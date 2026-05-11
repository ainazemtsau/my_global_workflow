# Documentation Index

## Documentation Index

## purpose

Эта note — навигационная карта текущей документации по Direction `Indie Game Development`.

Её задача:

- быстро показать, какие документы уже существуют;
- кратко объяснить, что в каждом из них лежит;
- помочь человеку или AI запросить нужный документ по имени;
- не смешивать current truth, direction-level rules и archive/history.

Эта note не является самостоятельным источником истины по игре. Она только индексирует documentation set.

## how to use with AI

Когда эта note даётся в ChatGPT, правильный режим работы такой:

- Сначала AI читает этот индекс.
- Потом AI запрашивает только те notes, которые реально нужны для текущей задачи.
- AI не должен достраивать missing content из index note.
- Если вопрос упирается в конкретную truth, AI должен просить exact source note по имени.
- Archive, review gates и workspace notes не считаются текущей truth, если постоянная note уже существует.

## current durable documentation

### Game Foundation

Path: `Directions/Indie Game Development/Game Documentation/Game Foundation`

Summary: Компактная foundation-note по самой игре. Держит concept spine, first product hypothesis и non-goals.

Use when: Нужно понять, что это за игра и какой у неё current foundation-frame.

### Technical Foundation — Gas and Grid Contract

Path: `Directions/Indie Game Development/Game Documentation/Technical Foundation — Gas and Grid Contract`

Summary: Technical foundation-note по тому, как связаны Gas и Grid. Держит ownership boundaries и required contract surfaces.

Use when: Нужно понять technical truth текущего foundation и dependency line Gas ↔ Grid.

### Clean-start Transfer Boundary

Path: `Directions/Indie Game Development/Game Documentation/Clean-start Transfer Boundary`

Summary: Boundary-note нового старта. Держит starting set, transfer-later, reference-only, do-not-carry и GridV2 status.

Use when: Нужно понять, что именно переносится как foundation, а что нет.

### Foundation Docs Index

Path: `Directions/Indie Game Development/Game Documentation/Foundation Docs Index`

Summary: Короткая карта authoritative foundation-docs и update rules.

Use when: Нужно быстро понять, какие notes являются authoritative и как их обновлять.

## direction-level documentation

### direction-context.md

Path: `Project file: direction-context.md`

Summary: Direction charter, thesis, completed goals, current trajectory, emerging understanding и canon snapshot.

Use when: Нужно понять общий контекст Direction.

### Canon

Path: `Directions/Indie Game Development/Canon/`

Summary: Hard rules, которые уже пережили review и стали обязательными.

Use when: Нужно понять, какие линии уже нельзя нарушать без явного пересмотра.

### Knowledge

Path: `Directions/Indie Game Development/Knowledge/`

Summary: Полезные рабочие наблюдения и lessons learned, которые не являются hard rules.

Use when: Нужно понять patterns и рабочие приёмы.

### Direction History

Path: `Directions/Indie Game Development/History`

Summary: Краткая история закрытых goals.

Use when: Нужно быстро восстановить trajectory Direction по прошлым Goal cycles.

## archive / historical materials

### Goal Archive

Path: `Archive/[Goal name]/`

Summary: Исторический пакет Goal: source artifacts, review gates, workspace notes, session trail.

Use when: Нужно проверить, как текущая truth была материализована и locked.

Warning: Archive полезен как history/proof, но не заменяет current durable docs.

## current canon set

- Gas не трактуется как isolated transferable asset; foundation фиксируется через dependency contract Gas ↔ Grid.
- Если game-truth, созданная в Goal, нужна игре дальше, её надо вынести из goal-local notes в постоянную документацию.

## current knowledge set

- Для early foundation-goals разбивка на несколько lockable artifacts помогает удержать scope и честно закрыть Goal.

## retrieval rule

Если задача касается:

- сути игры → сначала читать `Game Foundation`;
- технической зависимости Gas ↔ Grid → сначала читать `Technical Foundation — Gas and Grid Contract`;
- границы переноса foundation → сначала читать `Clean-start Transfer Boundary`;
- того, какой документ authoritative → сначала читать `Foundation Docs Index`;
- direction-level смысла, history или canon → читать `direction-context.md`, `Canon`, `Knowledge`, `History`.

Если index note недостаточно, AI должен запросить exact source note по имени, а не догадываться.
