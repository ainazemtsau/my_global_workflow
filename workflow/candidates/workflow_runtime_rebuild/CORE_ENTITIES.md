# Workflow Runtime Rebuild Core Entities

status: candidate

Stage 1 определяет только минимальные сущности. Он не задает detailed packet schemas, detailed storage layout, Runtime Console details или quality/failure recovery details.

## Core mutation rule

Accepted State changes only through explicit acceptance/update path. Chat output, document existence, Codex output, Signal, Handler result and Project Files do not create accepted state by themselves.

## Adapter boundary rule

ChatGPT, Codex, Claude Code, Deep Research, GitHub, future AI providers and human actions are adapters / role implementations, not core runtime primitives. Adapter может выполнить Run или вернуть candidate result, но не может сам принять state transition.

## Action Inbox rule

Action Inbox не управляет workflow самостоятельно и не меняет Accepted State.

each item must have reason, relation, priority, and when_to_run or stale condition.

## Minimal entities

| Entity | What it is | Why it is needed | What it is not | Who/what may change it | Typical example |
| --- | --- | --- | --- | --- | --- |
| Direction Spine | Простая ось направления: Root Result, Success Conditions, Spine Points and Tracks. | Дает устойчивую опору для долгого проекта. | Не подробная roadmap и не task backlog. | Пользователь или authorized review через acceptance/update path. | "Stage 1 accepted, Stage 2 transport design next." |
| Root Result | Главный результат, ради которого существует direction. | Помогает оценивать все fronts and nodes. | Не список функций и не sprint goal. | Пользователь или authorized review через acceptance/update path. | "Workflow runtime can support long solo+AI continuation." |
| Success Conditions | Проверяемые условия успешности Root Result. | Делают приемку менее субъективной. | Не полный test plan. | Пользователь или authorized review через acceptance/update path. | "Every material chat ends with exact Next Move." |
| Spine Point | Крупная точка на Direction Spine. | Делит долгую работу на понятные milestones. | Не микрозадача. | Пользователь или authorized review через acceptance/update path. | "Stage 2 adapter transport design reviewed." |
| Track | Параллельная линия внимания внутри direction. | Помогает разделять архитектуру, integration, evidence и rollout. | Не отдельный проект сам по себе. | Пользователь или authorized review через acceptance/update path. | "Runtime model track", "Adapter setup track". |
| Active Front | Выбранная часть Direction Spine, которая сейчас движется. | Ограничивает текущую работу. | Не весь project backlog. | Пользователь или route decision через acceptance/update path. | "Stage 1 candidate docs." |
| Work Graph | Локальный граф nodes для Active Front. | Показывает зависимости и следующий node. | Не глобальный граф всего проекта. | Runtime planning step with user/review acceptance. | "README before glossary validation." |
| Node | Один bounded work item внутри Work Graph. | Позволяет получить один meaningful result. | Не открытый исследовательский поток без результата. | Runtime planning step or user adjustment before contract. | "Write Core Entities file." |
| Work Contract | Ограниченный контракт работы для node. | Задает scope, boundaries, evidence and expected output. | Не accepted state и не право менять route. | Пользователь, planner or review before Run. | "Create six markdown files, do not edit active runtime." |
| Run | Конкретное исполнение Work Contract. | Связывает работу с исполнителем и временем. | Не приемка результата. | Adapter, role implementation or human action may perform it. | "Codex run creates candidate package." |
| Evidence | Проверяемые результаты Run. | Нужны для acceptance decision. | Не accepted state by itself. | Run produces it; reviewer may classify it. | "git diff --check passed, required files exist." |
| Acceptance Decision | Явное решение принять, отклонить или вернуть результат. | Только оно может провести accepted transition. | Не автоматический вывод tools. | User or authorized acceptance role. | "Accept Stage 1 package as candidate baseline." |
| Memory Artifact | Продвинутая память, полезная для продолжения. | Сохраняет проверенный контекст между чатами. | Не сырая chat memory и не Accepted State. | User or memory promotion step. | "Stage 2 must not activate runtime." |
| Signal | Факт, который стоит заметить. | Позволяет отделить наблюдение от действия. | Не команда, не acceptance и не mutation. | Tools, checks, adapters or humans may report it. | "A source file is stale." |
| Handler | Правило или процесс, который реагирует на Signal. | Создает candidate action. | Не исполнитель и не state mutator. | Runtime design or authorized configuration may change it. | "If stale source signal appears, create inbox item." |
| Action Inbox Item | Candidate action for later attention. | Удерживает follow-up без автоматического управления workflow. | Не обязательство выполнить и не accepted transition. | Handler may create it; user/review may edit, run or close it. | "Check Stage 2 transport assumptions before design." |
| Next Move | Точная следующая инструкция. | Обеспечивает продолжение после material chat. | Не accepted state и не полный план. | Current material chat or reviewer writes it; user may accept/update. | "Open Stage 2 design chat with reviewed Stage 1 package." |
| Adapter | Role implementation for work execution or information retrieval. | Позволяет подключать ChatGPT, Codex, Claude Code, Deep Research, GitHub, future AI providers and human actions. | Не core runtime primitive и не acceptance authority. | Runtime setup may configure it; adapter may only return candidate result/evidence. | "Codex executes bounded implementation package." |

END_OF_FILE: workflow/candidates/workflow_runtime_rebuild/CORE_ENTITIES.md
