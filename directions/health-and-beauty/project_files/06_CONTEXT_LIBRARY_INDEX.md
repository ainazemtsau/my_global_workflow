# 06\_CONTEXT\_LIBRARY\_INDEX.md

```yaml
project_file_projection: 1
schema: direction_project_file_projection.v1
source_file: "directions/health-and-beauty/project_files/06_CONTEXT_LIBRARY_INDEX.md"
canonical_source: GitHub repository file
projection_status: fresh
activated_at: "2026-05-11"

```

## Canon rule

This file is an active GitHub Direction runtime file. If it conflicts with another current GitHub Direction file, return Context Request; do not invent state.

## Default context

Load the Direction Project Files default set. Current Phase is `MacroFactor Nutrition AI Support Setup`; active Goal is the MacroFactor nutrition AI support Goal.

## Shared runtime and stage prompts

```yaml
shared_runtime_file: "workflow/runtime/WF_VNEXT_R_RUNTIME_CORE.md"
stage_prompt_source_root: "workflow/stage_prompts/"
stage_prompt_load_rule: "request exact stage prompt by stage ID; do not bulk-load all prompts"
local_runtime_core_copy_required: false
```

Stage prompts are request-only runtime inputs. Do not copy stage prompt files into Direction Project Files.

## Request-only context

*   `directions/health-and-beauty/domain_docs/health-domain-documentation.md`
*   `directions/health-and-beauty/knowledge` by topic.
*   Active Goal preserved children: `Sessions`, `Wave Cards`, `Goal Brief`, `Execution Pack`.

## Archive boundary

Archived or historical material is pointer-only and must not be default-loaded.

## Tool boundary

Concrete setup for `12-week-starter` must be verified before Codex execution. Do not infer AGENTS.md, `.codex/config.toml`, Task Master, Serena, Basic Memory, or validators from governance notes.
