# Workflow Runtime Rebuild Implementation Plan

status: candidate

## Правило стадий

Стадии нельзя смешивать. Каждая стадия должна завершаться проверяемым результатом, review и явным решением о переходе дальше.

До Stage 4 нельзя:

- replace active runtime;
- migrate active directions;
- roll out Project Instructions;
- delete current runtime files;
- import legacy state;
- declare candidate active authority;
- run the new runtime as production process.

## Stage 1 — Root Model + Operating Flow

### Goal

Зафиксировать простой корневой runtime model и практический operating flow для долгих solo+AI проектов.

### Includes

- главный путь Direction Spine → Active Front → Work Graph → Work Contract / Run / Evidence / Acceptance → Memory → Signals / Handlers / Action Inbox → Next Move;
- минимальные core entities;
- правила Accepted State, Memory, Signal, Handler, Action Inbox и Adapter boundaries;
- пользовательский flow без требования писать YAML;
- границы того, что Stage 1 не определяет.

### Done when

- шесть файлов кандидата существуют в `workflow/candidates/workflow_runtime_rebuild/`;
- пакет читается как самостоятельная документация;
- ясно указано, что пакет не является active runtime authority;
- old clean_runtime package удален;
- parent/integration review подтверждает, что Stage 1 можно использовать как baseline для Stage 2 design.

### Not included

- transport formats;
- adapter launch details;
- detailed packet schemas;
- detailed storage layout;
- Runtime Console details;
- quality/failure recovery details;
- migration active Directions;
- production runtime activation.

## Stage 2 — Transport + Adapter Setup

### Goal

Спроектировать, как runtime передает bounded work между adapters и как возвращает results без активации production runtime.

Stage 2 candidate docs добавляются и сохраняются в этом candidate package как документация. Это не означает acceptance, rollout или runtime activation.

### Includes

- high-level Launch Packet and Result Packet boundaries;
- adapter setup rules for ChatGPT, Codex, Claude Code, Deep Research, GitHub, future AI providers and human actions;
- minimal handoff expectations for work chats and Codex implementation packages;
- generic canonical storage wording without exact storage layout;
- separation between adapter output and Accepted State;
- persisted candidate docs for transport protocol, chat types, packet formats, Codex workflow and adapter context access.

### Done when

- transport boundary is documented;
- adapters are described as role implementations, not core runtime primitives;
- no provider output is treated as accepted by itself;
- Stage 2 candidate docs are present in `workflow/candidates/workflow_runtime_rebuild/`;
- Stage 2 review confirms that design can support pilot scenarios later.

### Not included

- runtime activation;
- Project Instructions rollout;
- detailed storage layout;
- full packet schema standard;
- production migrations;
- quality console implementation.

## Stage 3 — Signals / Action Inbox / Console / Quality

### Goal

Спроектировать вспомогательный слой контроля: факты, кандидаты действий, обзор состояния и проверки качества.

### Includes

- Signal semantics as facts only;
- Handler semantics as candidate creators only;
- Action Inbox item requirements;
- Check Job concept;
- Runtime Console direction at a high level;
- quality and review checkpoints at design level.

### Done when

- Signal, Handler and Action Inbox behavior is clear;
- Action Inbox cannot mutate workflow by itself;
- Console and quality concepts are bounded and ready for pilots;
- review confirms that Stage 3 does not activate the candidate as authority.

### Not included

- active console implementation;
- automatic route decisions;
- production failure recovery;
- live direction migration;
- replacing current Workflow OS.

## Stage 4 — Pilot Scenarios + Integration Acceptance

### Goal

Проверить кандидата на ограниченных pilot scenarios и принять или отклонить integration path.

### Includes

- selected pilot scenarios;
- integration acceptance criteria;
- comparison with current Workflow OS behavior;
- explicit acceptance/update path for Accepted State;
- decision on whether any later rollout work is allowed.

### Done when

- pilots have evidence;
- integration review has a clear decision;
- accepted transitions are recorded through the explicit acceptance/update path;
- any future activation or migration work is separately authorized.

### Not included

- automatic migration of active Directions;
- silent replacement of active runtime;
- uncontrolled deletion of current runtime files;
- treating chat output, Codex output, document existence, Signal, Handler result or Project Files as accepted state.

END_OF_FILE: workflow/candidates/workflow_runtime_rebuild/IMPLEMENTATION_PLAN.md
