# Repository Agent Instructions

Status: active

This repository is the canonical AI workflow source.

Rules:
- Treat this repository as active/canonical only while `WORKFLOW_SOURCE_OF_TRUTH.md` says `active`.
- Do not invent Direction data.
- Do not touch other Direction folders unless the task explicitly names them.
- Use small diffs.
- Do not delete files or notes without explicit approval.
- Stage prompts live under `workflow/stage_prompts/`.
- Direction state lives under `directions/<id>/project_files/`.
- Migration/admin documentation lives under `docs/` and must not be loaded as runtime context unless a migration task asks for it.
