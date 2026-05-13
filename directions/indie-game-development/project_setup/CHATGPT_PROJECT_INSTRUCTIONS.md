# ChatGPT Project Instructions - Indie Game Development

## Project Identity

- Project name: `Indie Game Development`
- Source of truth: GitHub repository `ainazemtsau/my_global_workflow`
- Direction path: `directions/indie-game-development`
- Run this as a separate ChatGPT Project for this Direction.

## Runtime Authority

- GitHub repository files are the runtime authority.
- Project Files are a runtime cache, not a replacement source of truth.
- If a verified full GitHub read conflicts with Project File cache, GitHub wins and the Project File cache must be refreshed.
- If GitHub read is truncated, omitted, lacks an expected tail anchor, or cannot verify full-file availability, do not treat it as authority. Return Context Request.
- Do not use external personal notes, old Trilium files, rebuild files, migration/admin files, raw chats, or archive notes as runtime source unless explicitly asked.

## Required Runtime Cache and GitHub Files

For normal runtime, manually load these files into this ChatGPT Project Files as runtime cache:

- `WORKFLOW_SOURCE_OF_TRUTH.md`
- `workflow/runtime/WF_VNEXT_R_RUNTIME_CORE.md`
- `workflow/runtime/GITHUB_LONG_FILE_READ_GUARD.md`
- `workflow/runtime/WORKFLOW_RUNTIME_CACHE_MANIFEST.md`
- `workflow/stage_registry/STAGE_REGISTRY.md`
- `directions/indie-game-development/project_files/00_DIRECTION_START_HERE.md`
- `directions/indie-game-development/project_files/01_DIRECTION_STATE.md`
- `directions/indie-game-development/project_files/02_CURRENT_PHASE.md`
- `directions/indie-game-development/project_files/03_FOCUS_REGISTER.md`
- `directions/indie-game-development/project_files/04_ACTIVE_GOAL.md`
- `directions/indie-game-development/project_files/05_PORTFOLIO_QUEUE.md`
- `directions/indie-game-development/project_files/06_CONTEXT_LIBRARY_INDEX.md`
- `directions/indie-game-development/project_files/07_PHASE_MEMORY_INDEX.md`

## Direction Boundary

Use only:

- `directions/indie-game-development/**`
- `WORKFLOW_SOURCE_OF_TRUTH.md`
- `workflow/runtime/WF_VNEXT_R_RUNTIME_CORE.md`
- `workflow/runtime/GITHUB_LONG_FILE_READ_GUARD.md`
- `workflow/runtime/WORKFLOW_RUNTIME_CACHE_MANIFEST.md`
- `workflow/stage_registry/STAGE_REGISTRY.md`
- `workflow/stage_prompts/<requested stage only>`

Do not use sibling Direction folders unless explicitly asked.

## Stage Prompts

Stage prompts are request-only by exact stage ID.

Do not bulk-load all stage prompts.

If an exact stage prompt read from GitHub is truncated, omitted, or lacks tail verification, the stage prompt is considered unavailable for that run. Stop and request the exact prompt manually, as a Project File/chat attachment, split file, chunked export, or Codex read-only verification.

Do not reconstruct missing prompts from memory.

## Context Failure

If required GitHub files or Project Files are unavailable, stale, inaccessible, contradictory, truncated, or missing tail verification, return Context Request instead of inventing state.

Do not invent Direction, Phase, Goal, Portfolio Queue, Context Loading Index, Wave, execution, or project state.

## Default Behavior

- Choose the smallest safe route.
- Ask only for blocking missing context.
- Do not overbuild.
- Use ruthless scope cutting and smallest testable version where relevant.
- Do not emit `repository_patch.v1` operations until explicitly approved by the user.
- Do not run product/project execution unless the correct execution route and context are present.
