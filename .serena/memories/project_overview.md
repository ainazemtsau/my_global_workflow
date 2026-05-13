# Project Overview

`my_global_workflow` is the canonical AI workflow source repository. Runtime prompts live under `workflow/stage_prompts/`, the stage registry lives under `workflow/stage_registry/`, shared runtime behavior lives under `workflow/runtime/`, and Direction state lives under `directions/<id>/project_files/` or phase folders.

Repository maintenance tasks should respect `WORKFLOW_SOURCE_OF_TRUTH.md` when relevant and must not invent Direction data. Migration/admin docs under `docs/` and `migration/` are not runtime context unless a migration task asks for them.