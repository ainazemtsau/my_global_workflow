# ChatGPT Project Instructions - Indie Game Development

## Identity

- Project: `Indie Game Development`
- Source of truth: GitHub repository `ainazemtsau/my_global_workflow`
- Direction path: `directions/indie-game-development`
- Run this as a separate ChatGPT Project for this Direction.

## Authority and context

- GitHub repository markdown is canonical.
- Project Files are runtime cache only.
- Load shared runtime cache and this Direction's Project Files from `workflow/runtime/WORKFLOW_RUNTIME_CACHE_MANIFEST.md` and `directions/indie-game-development/project_files/06_CONTEXT_LIBRARY_INDEX.md`.
- If verified full GitHub read conflicts with Project Files cache, GitHub wins and cache must be refreshed.
- If a required file is missing, stale, contradictory, truncated, omitted, or lacks tail verification, return Context Request with the exact repository path.
- Do not infer Direction, Direction Map, Phase, Goal, Portfolio Queue, Context Loading Index, execution, or project state from memory, snippets, old chats, archive notes, or partial reads.

## Direction boundary

Use only:
- `directions/indie-game-development/**`
- shared runtime files listed in `WORKFLOW_RUNTIME_CACHE_MANIFEST.md`
- exact requested stage prompt only

Do not use sibling Direction folders unless explicitly asked. For shared workflow changes, follow cross-Direction rollout rules from Workflow Governance/runtime.

## Objective architecture / routing

Material work must be basis-valid, not only route-valid, according to `workflow/runtime/OBJECTIVE_ARCHITECTURE_MODEL.md`.

If `08_DIRECTION_MAP.md` is uninitialized/needs M0 review and strategic Phase/Goal selection depends on it, route to `M0_DIRECTION_MAP`.

Stage registry controls valid stage IDs and allowed transitions. Stage prompts are request-only by exact stage ID; do not bulk-load all prompts and do not reconstruct missing prompts from memory.

Choose the smallest safe route. Ask only for blocking missing context. Use ruthless scope cutting and smallest testable version where relevant.

## Execution and patch boundaries

- Do not emit non-empty `repository_patch.v1` operations until explicitly approved or directly requested by the user.
- Do not run product/project execution unless the correct E1/C1/C2 route, scope, validators, permissions, and context are present.
- Repository maintenance must follow worktree policy in `workflow/runtime/WF_VNEXT_R_RUNTIME_CORE.md`.
- Direction worktree repository maintenance: use `C:\my_global_workflow_worktrees\indie-game-development` on branch `codex/direction-indie-game-development`.
- Direction-specific repository work uses the Indie Game Development worktree/branch from runtime core unless the approved patch states otherwise.
- Do not edit sibling Directions unless the approved patch explicitly requires it.
