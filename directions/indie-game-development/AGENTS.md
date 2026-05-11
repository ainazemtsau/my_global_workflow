# Indie Game Development Direction Instructions

Status: active

Direction path: `directions/indie-game-development`

Source of truth: GitHub repository markdown in `ainazemtsau/my_global_workflow`.

## Scope

Allowed by default:
- `directions/indie-game-development/**`
- shared workflow files under `workflow/` only when the task asks for workflow runtime, stage prompt, transport, or Codex protocol context.

Forbidden unless explicitly requested:
- `directions/solo-max-productive/**`
- `directions/indie-game-development/**`
- `directions/health-and-beauty/**`

The current Direction folder above is the only exception to the forbidden Direction list.

## Runtime Rules

- Do not use external personal notes as workflow source.
- Do not routinely load migration/admin files.
- Do not invent Direction, Phase, Goal, Portfolio Queue, Context Loading Index, project metadata, repo URLs, local paths, or execution state.
- If required state is missing, return `NEEDS_INPUT` with the exact GitHub path needed.
- Runtime Direction state belongs in `project_files/`.
- Reusable Direction knowledge, canon, decisions, patterns, and reviews belong in `knowledge/` and are canonical only when present as GitHub files.
- Domain documentation belongs in `domain_docs/`; do not invent domain canon when a required file is missing.
- Project metadata belongs in `projects/` and `direction.meta.yml`; unknown repos stay `not_created` / `needs_user_input`.

## Change Rules

- Use small diffs.
- Do not delete files without explicit approval or a migration manifest replacement route.
- Do not modify other Direction folders unless the task explicitly names them.
- Do not copy stage prompts into Direction project files.
- Report changed files and validation evidence after edits.
