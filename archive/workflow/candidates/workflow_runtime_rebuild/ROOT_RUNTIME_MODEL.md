# Workflow Runtime Rebuild Root Runtime Model

status: candidate

## One-line model

Direction Spine
→ Active Front
→ Work Graph
→ Work Contract / Run / Evidence / Acceptance
→ Memory
→ Signals / Handlers / Action Inbox
→ Next Move

Эта строка описывает минимальный путь работы. Она не активирует runtime и не заменяет текущий Workflow OS.

## Direction Spine

Direction Spine фиксирует основную ось направления: root result, success conditions, spine points and tracks.

Direction Spine is not a detailed roadmap. Он не должен превращаться в полный план всех будущих задач. Его роль — дать устойчивую опору для выбора текущего фронта работы.

Direction Spine меняется только через явный acceptance/update path.

## Active Front

Active Front — это выбранная часть Direction Spine, которая сейчас реально движется.

Он ограничивает внимание. Вместо управления всем проектом сразу runtime работает с понятным текущим фронтом.

Active Front не является глобальным backlog и не должен включать все возможные инициативы.

## Work Graph

Work Graph — локальный граф работы для выбранного Active Front.

Work Graph is local to Active Front, not global to the whole project. Он помогает выбрать следующий node, зависимости и порядок выполнения внутри текущего фронта.

Work Graph не является копией Direction Spine и не является постоянной картой всего проекта.

## Work Contract / Run / Evidence / Acceptance

Work Contract задает bounded work: что нужно сделать, какие границы действуют, какой результат ожидается и какие evidence нужны.

Run — конкретное исполнение Work Contract через adapter или human action.

Evidence — проверяемый результат Run. Evidence само по себе не меняет Accepted State.

Acceptance Decision — явное решение принять, отклонить или вернуть результат на доработку. Только это решение через acceptance/update path может изменить Accepted State.

## Memory

Memory хранит полезные сведения для продолжения проекта, но Memory requires promotion.

Сырые заметки, вывод чата, Signal, Result Packet или документ не становятся Memory Artifact автоматически. Сведения должны быть выбраны, проверены и повышены до памяти через явное действие.

Memory не является Accepted State и не заменяет canonical storage.

## Signals / Handlers / Action Inbox

Signal is a fact and does not change state.

Handler creates only candidates and does not execute or mutate state.

Action Inbox хранит candidate actions, которые пользователь или runtime process может рассмотреть позже. Action Inbox не принимает решения, не запускает работу сам по себе и не меняет Accepted State.

## Next Move

Next Move — точная следующая инструкция после материального чата или принятого решения.

Every material chat must end with exact Next Move. Это может быть инструкция открыть следующий чат, передать bounded package в Codex, проверить evidence, принять решение или обновить accepted record.

Next Move не является accepted state. Он указывает, что делать дальше.

## How the parts interact

1. Direction Spine показывает, куда движется проект.
2. Active Front выбирает текущую рабочую область.
3. Work Graph раскладывает эту область на nodes.
4. Выбранный node получает Work Contract.
5. Run исполняет контракт через adapter или human action.
6. Evidence возвращается на проверку.
7. Acceptance Decision решает, меняется ли Accepted State.
8. Memory получает только продвинутые сведения.
9. Signals фиксируют факты, Handlers создают candidates, Action Inbox удерживает возможные действия.
10. Next Move закрывает материальный чат точной следующей инструкцией.

## Why Accepted State does not live in chat

Accepted State не живет в chat memory, потому что чат является рабочей средой, а не canonical storage.

Chat output, document existence, Codex output, Signal, Handler result and Project Files do not create accepted state by themselves.

Accepted State changes only through explicit acceptance/update path. Это защищает долгие проекты от случайных изменений, потери контекста, неоднозначных решений и расхождений между tools.

END_OF_FILE: workflow/candidates/workflow_runtime_rebuild/ROOT_RUNTIME_MODEL.md
