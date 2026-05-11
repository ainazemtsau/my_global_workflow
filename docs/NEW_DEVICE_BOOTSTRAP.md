# New Device Bootstrap

Status: active

Use this file to connect a new device or fresh ChatGPT/Codex workspace to the GitHub-only workflow runtime.

## Canonical Repository

- Repository: `https://github.com/ainazemtsau/my_global_workflow`
- Runtime source of truth: GitHub markdown files in this repository
- Source-of-truth marker: `WORKFLOW_SOURCE_OF_TRUTH.md`

## Required Local Setup

1. Clone the repository.
2. Read root `AGENTS.md`.
3. Read `WORKFLOW_SOURCE_OF_TRUTH.md`.
4. For Direction work, read the target Direction `AGENTS.md`.
5. Use only the target Direction folder plus shared workflow files required by the task.

## Direction Runtime Files

Default Direction context lives in:

- `directions/<direction-id>/project_files/00_DIRECTION_START_HERE.md`
- `directions/<direction-id>/project_files/01_DIRECTION_STATE.md`
- `directions/<direction-id>/project_files/02_CURRENT_PHASE.md`
- `directions/<direction-id>/project_files/03_FOCUS_REGISTER.md`
- `directions/<direction-id>/project_files/04_ACTIVE_GOAL.md`
- `directions/<direction-id>/project_files/05_PORTFOLIO_QUEUE.md`
- `directions/<direction-id>/project_files/06_CONTEXT_LIBRARY_INDEX.md`

Shared runtime files live in:

- `workflow/runtime/WF_VNEXT_R_RUNTIME_CORE.md`
- `workflow/stage_registry/STAGE_REGISTRY.md`
- `workflow/stage_prompts/<requested-stage>.md`
- `workflow/transport/*`

## Codex Rules

- Use GitHub files as workflow state.
- Keep edits inside the named Direction unless the task explicitly expands scope.
- Preview diffs before applying when requested.
- Do not invent missing Direction, Phase, Goal, project, repository, or execution state.
- If required files are unavailable, return `NEEDS_INPUT` with exact GitHub paths.
- Use Repository Patch / `repository_patch.v1` terminology for workflow writes.

## ChatGPT Project Rules

Use `docs/CHATGPT_PROJECT_SETUP.md` for Project Instructions.

Each Project should load only:

- its own `directions/<direction-id>/**` files;
- shared workflow runtime files needed for the requested stage;
- transport schemas when packet formatting is needed.

Do not use sibling Direction folders unless explicitly requested.

## Migration/Admin Area

The `migration/` folder is admin-only. It records historical migration inventory, manifests, logs, and deferred decisions. It is not default runtime context for Direction Projects.
