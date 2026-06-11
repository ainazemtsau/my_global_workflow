# ARCHIVED RESULT ARTIFACT / LEGACY EVIDENCE ONLY

This file is not active Workflow OS Project setup, not accepted Direction state, and must not be uploaded or pasted for active Workflow Projects. See:

- directions/health-and-beauty/archive/ARCHIVE_INDEX.md
- directions/health-and-beauty/workflow/project_setup/PROJECT_FILES_MANIFEST.md

# Project `Питание` - repo-backed multi-chat nutrition loop

Status: active clean rebuild after `U1_REAL_UI_TEST_FAILED`

This package is the active setup source for ChatGPT Project `Питание`.

It is not a live diet, not a menu prescription, and not clinical nutrition advice. It defines the operating architecture, Project Instructions, Project Files cache, durable GitHub state layout, save boundary, and acceptance tests.

## Architecture

```yaml
source_of_truth:
  durable_state: GitHub files in directions/health-and-beauty/projects/nutrition/
  chatgpt_project_files: refreshable runtime cache copied from GitHub
  chat_memory: non_authoritative
  codex: save_only_repository_maintenance_writer
```

Project `Питание` uses separate chats for separate jobs:

- Global Strategy Chat: first setup or rare strategy rebuild only; must keep `USER_PROFILE_AND_CONSTRAINTS.yml`, `DEEP_RESEARCH_REQUEST.md`, `DEEP_RESEARCH_RESULT.md`, `DEEP_RESEARCH_SYNTHESIS.md`, and the approved `GLOBAL_NUTRITION_PLAN.md` separate.
- Weekly Planning Chat: one week only; creates `WEEKLY_PLAN` and later closes the week from `WEEK_TRACKING_REPORT`.
- Menu Chat: one week only; requires `WEEKLY_PLAN` and creates `ACTIVE_WEEK_MENU`, shopping list, and prep plan.
- Tracking Chat: one week only; requires `WEEKLY_PLAN` and `ACTIVE_WEEK_MENU`; creates `WEEK_TRACKING_REPORT` at week end.

## Install surface

Use:

```text
CHATGPT_PROJECT_INSTRUCTIONS.md
PROJECT_FILES_MANIFEST.md
project_files/
state/
weeks/
protocols/
```

Do not use the superseded setup under:

```text
directions/health-and-beauty/project_setup/pitanie/
```

## Validation

Before treating the Project as usable, run the real-start prompts in:

```text
project_files/07_REAL_START_ACCEPTANCE_TESTS.md
```

Repo rebuild validation must prove required files, supersession anchors, prompt routing, Deep Research gate, one-week chat boundaries, tracking save default, and forbidden-path discipline.

END_OF_FILE: directions/health-and-beauty/projects/nutrition/README.md
