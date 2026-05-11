# Workflow Source of Truth

Status: active

Canonical AI workflow source: GitHub repository `ainazemtsau/my_global_workflow`.

Runtime source-of-truth model: GitHub markdown files in this repository.

Migration status: closed.

Direction data rule:
- Do not invent Direction, Phase, Goal, Portfolio Queue, Context Loading Index, or execution state.
- Direction data must be read from current GitHub Direction files unless an explicit migration/admin task says otherwise.
- Missing or contradictory source data must be returned as `NEEDS_INPUT` with the exact repository path and blocker.

Runtime rule:
- ChatGPT and Codex should use GitHub markdown files for workflow state.
- Runtime Direction files must not depend on migration/admin notes.
- Runtime Direction files must not require a note-database layer.
- Repository Patch / `repository_patch.v1` is the runtime write proposal format.

Admin documentation:
- Migration/admin docs remain under `migration/` and selected setup docs under `docs/`.
- Migration/admin docs are not loaded by default in Direction Projects.
