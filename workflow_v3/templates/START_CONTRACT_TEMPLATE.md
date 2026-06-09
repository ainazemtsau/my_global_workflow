# START Contract Template

status: template

## Human-Facing START

```text
## Коротко

В этом чате я буду <простое описание работы>.

Зачем:
<1-3 строки простым языком>.

Какая процедура ведёт чат:
<entrypoint>. Она выбрана потому, что <простая причина>.

Когда задача будет считаться завершённой:
<проверяемое завершение>. Если для текущей цели понадобится внешняя зависимость, я открою DEPENDENCY_CALL и остановлюсь ждать return.

На что тебе смотреть:
<короткий список важных проверок>. Если всё стандартно: "Особого решения сейчас не нужно; проверь только цель и target."

Что будет дальше:
После START / СТАРТ я пройду stage 0. После каждого важного stage дам короткое резюме и остановлюсь на CONTINUE / ДАЛЬШЕ.

## Техническая часть
```

## START_CONTRACT

```text
START_CONTRACT:
  selected_entrypoint:
  selected_procedure_path:
  kind:
  start_goal:
  terminal_condition:
  completion_contract:
  material_stages:
  routing_dependency_policy:
  required_sources:
  write_boundaries:
  user_confirmation_required: START | СТАРТ
```

## Boundary

Use this as the human-readable START contract before material work. When the operator writes Russian, the human-facing block comes first in Russian and technical fields stay compact below `## Техническая часть`. START selects one main procedure, reads its source, shows its completion contract, states the dependency and write boundaries, and waits for explicit user START / СТАРТ. The terminal condition must be verified completion or explicit blocked result, not a handoff, package, card, dependency envelope, or post-closed continuation.

END_OF_FILE: workflow_v3/templates/START_CONTRACT_TEMPLATE.md
