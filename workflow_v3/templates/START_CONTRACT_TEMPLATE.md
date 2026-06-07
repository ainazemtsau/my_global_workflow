# START Contract Template

status: template

## Operator Brief

```text
## Operator Brief

- Goal:
- Selected main procedure:
- Why this procedure:
- Terminal condition:
- Child procedure calls:
- Before START / СТАРТ, review:
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
  child_call_policy:
  required_sources:
  write_boundaries:
  user_confirmation_required: START | СТАРТ
```

## Boundary

Use this as the human-readable START contract before material work. START selects one main procedure, reads its source, shows its completion contract, states the child/adaptor and write boundaries, and waits for explicit user START / СТАРТ. The terminal condition must be verified completion or explicit blocked result, not a handoff, package, card, child-call envelope, or post-closed continuation.

END_OF_FILE: workflow_v3/templates/START_CONTRACT_TEMPLATE.md
