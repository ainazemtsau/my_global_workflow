# NEXT_CHAT_CARD Template

status: template

## NEXT_CHAT_CARD

```text
NEXT_CHAT_CARD:
  title:
  why:
  main_procedure_to_start:
  context_to_paste:
  expected_result:
  evidence_or_return_needed:
  start_instruction:
```

## Copy-Paste Prompt

`context_to_paste` must be complete enough that the user can open the next chat and paste it without assembling missing pieces manually.

Recommended content:

```text
Start Workflow v3 using main procedure: <entrypoint>.
Task:
Context:
Required sources:
Expected result:
Evidence or return needed:
Begin with START_CONTRACT and wait for START / СТАРТ before material RUN.
```

## Boundary

Use `NEXT_CHAT_CARD` only when workflow continuation needs a new material chat. If no continuation is needed, closure must state `no_next_chat_needed` with reason.

END_OF_FILE: workflow_v3/templates/NEXT_CHAT_PROMPT_TEMPLATE.md