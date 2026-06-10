# Project Setup Rollout Eval

status: active_repository_completion_framework

## Source files to inspect

- `workflow_v3/PROJECT_SETUP_MODEL.md`
- `workflow_v3/project_setup/CHATGPT_PROJECT_CREATION_GUIDE.md`
- `workflow_v3/project_setup/PROJECT_FILES_MANIFEST_TEMPLATE.md`
- Project Instructions source files under `workflow_v3/project_setup/**`
- `workflow_v3/project_packs/README.md`
- `workflow_v3/project_setup/CHATGPT_PROJECT_CREATION_GUIDE.md`

## Evidence required

- Project type and rollout authorization;
- Project Instructions UI source and payload marker count when changed;
- Project Files/Sources manifest impact;
- request-only sources impact;
- do-not-upload list;
- Code repository dependency next move test requiring complete Transfer Packet / code repository dependency packet;
- explicit statement whether actual UI update or refresh occurred.

## PASS criteria

- Repository commit, Project Instructions UI update, Project Files/Sources refresh, and request-only source refresh are separated.
- Payload count is measured for changed instruction sources.
- Payload is at or below 8,000 characters.
- Project Instruction sources are not listed as Project Files/Sources uploads.
- Code repository dependency next move test requires a complete Transfer Packet / code repository dependency packet when that next move is selected.
- `workflow_v3/interfaces/**`, `workflow_v3/templates/**`, `workflow_v3/completion/**`, `workflow_v3/adoption/**`, `workflow_v3/procedures/**`, and `workflow_v3/evals/**` remain do-not-upload unless later explicit rollout says otherwise.

## WARN criteria

- Payload is above 7,200 characters but at or below 8,000.
- Future manual Project UI update is required but not performed.

## FAIL criteria

- Payload exceeds 8,000 characters.
- Project UI update conflated with repository commit.
- Project Files/Sources treated as authority.
- Project Files/Sources refresh implied without authorization.
- Request-only sources uploaded by default.
- Code repository dependency next move test permits an incomplete dependency packet or makes the user assemble the code-assistant prompt manually.
- Do-not-upload list missing required Workflow v3 source paths.

## Common failure modes

- Treating Project Instructions UI as documentation storage.
- Treating Project Files/Sources as source authority.
- Claiming a Project was updated because repository source changed.

## Required recovery/repair action

Block rollout, trim payload or split future package, repair manifest classifications, and rerun payload and refresh-category validation.

END_OF_FILE: workflow_v3/evals/PROJECT_SETUP_ROLLOUT_EVAL.md
