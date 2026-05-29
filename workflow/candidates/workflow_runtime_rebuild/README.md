# Workflow Runtime Rebuild Candidate

status: candidate

## Статус и границы

Этот пакет является кандидатом архитектуры Workflow Runtime Rebuild.

Stage 1 остается candidate baseline. Stage 2 candidate documentation добавлена как transport / adapter setup layer. Stage 3 candidate documentation добавляется как operational control layer: Signals / Handlers / Action Inbox / Console / Quality.

Он является документацией, а не рабочей средой:

- not authority for the current Workflow OS runtime;
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

Стадии не смешиваются. Этот пакет фиксирует Stage 1 baseline, Stage 2 candidate documentation и Stage 3 candidate documentation. Stage 4 не завершен.

## Candidate package contents

Stage 1 baseline:

- `README.md`
- `IMPLEMENTATION_PLAN.md`
- `ROOT_RUNTIME_MODEL.md`
- `OPERATING_FLOW.md`
- `CORE_ENTITIES.md`
- `GLOSSARY.md`

Stage 2 transport / adapter setup:

- `TRANSPORT_AND_INTERACTION_PROTOCOL.md`
- `CHAT_TYPES.md`
- `PACKET_FORMATS.md`
- `CODEX_WORKFLOW.md`
- `ADAPTER_SETUP_AND_CONTEXT_ACCESS.md`

Stage 3 signals / console / quality:

- `SIGNALS_HANDLERS_ACTION_INBOX.md`
- `DIRECTION_CUSTOMIZATION_PROFILE.md`
- `RUNTIME_CONSOLE_MODEL.md`
- `QUALITY_GATES_AND_FAILURE_RECOVERY.md`

## Следующий шаг

Следующий шаг: parent/integration review для Stage 3 candidate documentation перед Stage 4 pilot scenarios / integration acceptance.

## Устаревший кандидат

Старый `workflow/candidates/clean_runtime/**` является obsolete и удален этим изменением. Он не используется как baseline для этого пакета.

END_OF_FILE: workflow/candidates/workflow_runtime_rebuild/README.md
