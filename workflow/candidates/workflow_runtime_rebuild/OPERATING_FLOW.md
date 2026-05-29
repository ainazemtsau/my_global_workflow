# Workflow Runtime Rebuild Operating Flow

status: candidate

Этот flow описывает практическую работу без тяжелого архитектурного языка. Пользователь не должен писать YAML, чтобы вести направление.

## Setup workspace

Пользователь выбирает место, где будет храниться canonical storage для направления. На Stage 1 точный storage layout не определяется.

Важно только, что принятые решения и evidence не живут только в памяти чата.

## Create direction

Пользователь создает direction: называет проект, формулирует его смысл и отделяет его от других направлений.

Direction не обязан сразу иметь полный план.

## Define Direction Spine

Пользователь задает Root Result, Success Conditions, Spine Points и Tracks.

Direction Spine остается простой осью проекта. Это не подробная дорожная карта и не список всех задач.

## Select Active Front

Пользователь выбирает, какая часть Direction Spine сейчас должна двигаться.

Active Front помогает не распыляться и не запускать работу по всему проекту одновременно.

## Open Work Graph

Для Active Front открывается локальный Work Graph.

Граф показывает ближайшие nodes, зависимости и возможный следующий результат. Он не является глобальным графом всего направления.

## Select next node

Пользователь выбирает node, который даст один meaningful result.

One material chat produces one meaningful result. Если работа слишком большая, node нужно уменьшить.

## Create Work Contract

Runtime или пользователь формирует Work Contract:

- что надо сделать;
- что нельзя менять;
- какой результат нужен;
- какие evidence нужны;
- кто или какой adapter может выполнить работу.

## Launch work chat

Работа запускается в подходящем чате или инструменте. Это может быть ChatGPT, Deep Research, Claude Code, human action или другой provider.

Чат получает ограниченный контекст и ожидаемый результат. Он не получает право менять route, product meaning или acceptance.

## Receive result

После работы пользователь получает result и evidence.

Результат остается candidate, пока нет Acceptance Decision.

## Launch Codex when ready

Codex запускается только когда нужен bounded implementation package.

Codex receives bounded implementation packages. В package должны быть scope, allowed paths, forbidden paths, validation и ожидаемый return state.

Codex does not decide route/product meaning/acceptance. Он выполняет ограниченную реализацию и возвращает evidence.

## Verify Codex result

Пользователь или review process проверяет changed files, validation, evidence и соответствие Work Contract.

Если результат не проходит проверку, его можно вернуть на доработку или отклонить.

## Update accepted state

Accepted State меняется только через явный acceptance/update path.

Chat output, document existence, Codex output, Signal, Handler result and Project Files do not create accepted state by themselves.

## Use Memory

Memory используется для сохранения полезных сведений, которые помогут продолжить проект позже.

Memory requires promotion: не каждая заметка или фраза из чата становится Memory Artifact.

## Use Action Inbox

Action Inbox хранит candidate actions: проверки, напоминания, возможные follow-up, вопросы, stale items.

Action Inbox does not manage workflow by itself. Каждый item должен быть связан с причиной, relation, priority и условием запуска или устаревания.

## Use Runtime Console later

Runtime Console на Stage 1 не определяется подробно.

Позже он может показывать Active Front, Work Graph, open contracts, recent evidence, Action Inbox и Next Move, но это относится к будущим стадиям.

## Continue in next chat

Каждый материальный чат заканчивается exact Next Move.

Пользователь получает точную следующую инструкцию: какой чат открыть, какой package передать, что проверить, какое решение принять или какой accepted record обновить.

## Full simple example

1. Пользователь создает direction: "перестроить workflow runtime для долгих solo+AI проектов".
2. Direction Spine задает Root Result: "простая runtime model, которую можно пилотировать".
3. Active Front выбирает "Stage 1 candidate package".
4. Work Graph содержит nodes: root model, operating flow, core entities, glossary, validation.
5. Следующий node: "создать Stage 1 documentation package".
6. Work Contract ограничивает allowed paths и запрещает менять active runtime.
7. Codex получает bounded implementation package и создает markdown files.
8. Пользователь проверяет diff, EOF markers, forbidden paths and validation.
9. Acceptance Decision решает, принимать ли candidate package.
10. Next Move говорит: "провести parent/integration review и затем открыть Stage 2 design".

END_OF_FILE: workflow/candidates/workflow_runtime_rebuild/OPERATING_FLOW.md
