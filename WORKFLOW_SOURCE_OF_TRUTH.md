# Workflow Source of Truth

Status: migration_in_progress

Current canonical workflow source: existing accepted migration source until explicit Step 10 acceptance.

Target canonical workflow source after migration: GitHub repository `ainazemtsau/my_global_workflow`.

GitHub is not active/canonical yet. During migration, GitHub content is a migration workspace and validation target until Step 10 is accepted.

Direction data rule:
- Do not invent Direction, Phase, Goal, Portfolio Queue, Context Loading Index, or execution state.
- Direction data must be migrated only from existing accepted source notes.
- Missing or contradictory source data must be marked `source_missing`, `migration_incomplete`, or returned as `NEEDS_INPUT`.

Runtime rule during migration:
- Do not treat GitHub as canonical for workflow runtime until Step 10.
- Do not change runtime semantics before the source-of-truth refactor step.
- Do not use migration/admin notes as runtime context unless a migration task explicitly asks for them.

Finalization rule:
- GitHub becomes the canonical AI workflow source only after Step 10 validation passes and this file is updated to `active`.
