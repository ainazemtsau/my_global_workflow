# Project `Питание` setup package - superseded

Status: `SUPERSEDED_U1_REAL_UI_TEST_FAILED`

Do not install this package. It is retained only as historical evidence of the failed one-chat setup route.

The active Project `Питание` setup is the clean repo-backed multi-chat package at:

```text
directions/health-and-beauty/projects/nutrition/
```

Required operator rule:

- Do not upload this file as Project Instructions.
- Do not upload old files from this directory as Project Files.
- Do not use this file as a runtime source of truth.
- Do not patch this file to restore active behavior.

Reason:

```yaml
supersession_reason:
  trigger: U1_REAL_UI_TEST_FAILED
  old_route: one_chat_setup
  failure_modes:
    - one_chat_collapse
    - premature_menu_generation
    - missing_chat_mode_routing
    - user_prompt_became_protocol
  replacement: directions/health-and-beauty/projects/nutrition/
```

END_OF_FILE: directions/health-and-beauty/project_setup/pitanie/PROJECT_PITANIE_SETUP_PACKAGE.md
