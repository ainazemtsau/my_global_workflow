# Workflow Runtime Rebuild Candidate

status: candidate

## Статус и границы

Этот пакет является кандидатом архитектуры Workflow Runtime Rebuild Stage 1.

Он является документацией, а не рабочей средой:

- not active runtime authority;
- does not replace current Workflow OS;
- does not create accepted state;
- does not run live Direction runtime.

Новый кандидат не меняет текущее поведение Workflow OS, не активирует новый runtime и не переносит Accepted State.

## Главная модель

Direction Spine
→ Active Front
→ Work Graph
→ Work Contract / Run / Evidence / Acceptance
→ Memory
→ Signals / Handlers / Action Inbox
→ Next Move

Смысл модели простой: держать долгий проект в форме, где понятно, что является принятым состоянием, что сейчас в работе, какой следующий шаг нужен и какой результат должен дать каждый материальный чат.

## Назначение

Workflow Runtime Rebuild нужен для долгих solo+AI проектов, где работа идет через несколько инструментов и людей:

- ChatGPT;
- Codex;
- Claude Code;
- Deep Research;
- GitHub;
- будущие AI providers;
- human actions.

Модель должна поддерживать продолжение работы между чатами. После каждого материального чата пользователь должен получить точный Next Move: что открыть, что передать, что проверить или какое решение принять дальше.

ChatGPT, Codex, Claude Code, Deep Research, GitHub, будущие AI providers и human actions являются adapters / role implementations. Они не являются ядром runtime и сами по себе не создают Accepted State.

## Плановые стадии

- Stage 1 — Root Model + Operating Flow.
- Stage 2 — Transport + Adapter Setup.
- Stage 3 — Signals / Action Inbox / Console / Quality.
- Stage 4 — Pilot Scenarios + Integration Acceptance.

Стадии не смешиваются. Этот пакет фиксирует только Stage 1.

## Следующий шаг

Следующий шаг: parent/integration review, затем Stage 2 design.

## Устаревший кандидат

Старый `workflow/candidates/clean_runtime/**` является obsolete и удален этим изменением. Он не используется как baseline для этого пакета.

END_OF_FILE: workflow/candidates/workflow_runtime_rebuild/README.md
