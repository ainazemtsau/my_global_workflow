# Repository Agent Instructions

Status: migration_in_progress

This repository is the future canonical AI workflow source after migration acceptance.

Rules:
- Do not treat this repository as active/canonical until `WORKFLOW_SOURCE_OF_TRUTH.md` says `active`.
- Do not invent Direction data.
- Do not touch other Direction folders unless the task explicitly names them.
- Use small diffs.
- Do not delete files or notes without explicit approval.
- Stage prompts live under `workflow/stage_prompts/`.
- Direction state lives under `directions/<id>/project_files/`.
- Migration/admin documentation lives under `docs/` and must not be loaded as runtime context unless a migration task asks for it.
