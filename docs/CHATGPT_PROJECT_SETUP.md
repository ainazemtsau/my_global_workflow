# ChatGPT Project Setup

```yaml
artifact_control:
  artifact_name: "ChatGPT Project Setup"
  schema: chatgpt_project_setup.v1
  owner_layer: setup_documentation
  status: active
  repo_path: "docs/CHATGPT_PROJECT_SETUP.md"
  authority: "GitHub repository setup documentation; runtime cache manifest and Direction Project Instructions win for exact runtime cache/project instruction requirements"
  freshness: refresh_when_active_directions_or_project_files_cache_policy_changes
  last_updated: "2026-05-13"
```

## Purpose

Use this file to configure and maintain ChatGPT Projects for the active GitHub-backed Workflow vNext-R runtime.

This file is setup documentation. It is not runtime state, not a stage prompt, and not the source of truth for Direction/Phase/Goal state.

Canonical runtime source-of-truth marker:

```text
WORKFLOW_SOURCE_OF_TRUTH.md
```

Runtime cache source:

```text
workflow/runtime/WORKFLOW_RUNTIME_CACHE_MANIFEST.md
```

Stage registry source:

```text
workflow/stage_registry/STAGE_REGISTRY.md
```

## Active ChatGPT Direction Projects

Active Direction Projects currently covered by this setup guide:

```text
Workflow Governance
Solo Max Productive
Indie Game Development
Health and Beauty
```

Each ChatGPT Project is one Direction.

Do not merge multiple Directions into one ChatGPT Project.

## Common Runtime Rule

Every active Direction Project uses:

```text
GitHub repository: ainazemtsau/my_global_workflow
Source of truth marker: WORKFLOW_SOURCE_OF_TRUTH.md
Runtime core: workflow/runtime/WF_VNEXT_R_RUNTIME_CORE.md
GitHub long-file read guard: workflow/runtime/GITHUB_LONG_FILE_READ_GUARD.md
Runtime cache manifest: workflow/runtime/WORKFLOW_RUNTIME_CACHE_MANIFEST.md
Stage registry: workflow/stage_registry/STAGE_REGISTRY.md
Stage prompts: workflow/stage_prompts/<requested stage only>
Transport templates: workflow/transport/* when packet templates are needed
```

GitHub repository files remain the source of truth.

ChatGPT Project Files are runtime cache, not source of truth. They must be manually refreshed when Codex changes cached files.

If a GitHub read is truncated, omitted, lacks tail verification, or cannot prove full-file availability, do not treat that read as source authority. Return Context Request naming the exact path.

Stage prompts are request-only by exact stage ID. Do not bulk-load all stage prompts. Do not reconstruct missing prompts from memory.

Do not invent Direction, Phase, Goal, Portfolio Queue, Context Loading Index, Wave, execution, or project state.

Do not use external personal notes as workflow source.

Do not use `migration/` or migration/admin docs as runtime context unless the task is explicitly a migration/admin task.

Shared workflow changes must be evaluated across all active Direction Projects, not only Workflow Governance.

## Required shared runtime Project Files for every active Direction

Manually load these shared runtime cache files into every active Direction ChatGPT Project:

```text
WORKFLOW_SOURCE_OF_TRUTH.md
workflow/runtime/WF_VNEXT_R_RUNTIME_CORE.md
workflow/runtime/GITHUB_LONG_FILE_READ_GUARD.md
workflow/runtime/WORKFLOW_RUNTIME_CACHE_MANIFEST.md
workflow/stage_registry/STAGE_REGISTRY.md
```

Also manually load that Direction's own Project Files `00-07` from:

```text
directions/<direction-id>/project_files/
```

Required Direction Project Files:

```text
00_DIRECTION_START_HERE.md
01_DIRECTION_STATE.md
02_CURRENT_PHASE.md
03_FOCUS_REGISTER.md
04_ACTIVE_GOAL.md
05_PORTFOLIO_QUEUE.md
06_CONTEXT_LIBRARY_INDEX.md
07_PHASE_MEMORY_INDEX.md
```

Do not upload stage prompts as default Project Files.

Do not upload old rebuild Project Files, migration/admin notes, raw chats, archive notes, or execution evidence dumps as default Project Files.

## Workflow Governance Project Setup

ChatGPT Project name:

```text
Workflow Governance
```

Direction path:

```text
directions/workflow-governance
```

Project Instructions source:

```text
directions/workflow-governance/project_setup/CHATGPT_PROJECT_INSTRUCTIONS.md
```

Project Files to load:

```text
WORKFLOW_SOURCE_OF_TRUTH.md
workflow/runtime/WF_VNEXT_R_RUNTIME_CORE.md
workflow/runtime/GITHUB_LONG_FILE_READ_GUARD.md
workflow/runtime/WORKFLOW_RUNTIME_CACHE_MANIFEST.md
workflow/stage_registry/STAGE_REGISTRY.md
directions/workflow-governance/project_files/00_DIRECTION_START_HERE.md
directions/workflow-governance/project_files/01_DIRECTION_STATE.md
directions/workflow-governance/project_files/02_CURRENT_PHASE.md
directions/workflow-governance/project_files/03_FOCUS_REGISTER.md
directions/workflow-governance/project_files/04_ACTIVE_GOAL.md
directions/workflow-governance/project_files/05_PORTFOLIO_QUEUE.md
directions/workflow-governance/project_files/06_CONTEXT_LIBRARY_INDEX.md
directions/workflow-governance/project_files/07_PHASE_MEMORY_INDEX.md
```

Copyable Project Instructions summary:

```text
You are the ChatGPT maintenance layer for Workflow Governance using Workflow vNext-R.

Canonical source:
- GitHub repository: ainazemtsau/my_global_workflow
- Direction path: directions/workflow-governance

Use only:
- WORKFLOW_SOURCE_OF_TRUTH.md
- workflow/runtime/WF_VNEXT_R_RUNTIME_CORE.md
- workflow/runtime/GITHUB_LONG_FILE_READ_GUARD.md
- workflow/runtime/WORKFLOW_RUNTIME_CACHE_MANIFEST.md
- workflow/stage_registry/STAGE_REGISTRY.md
- directions/workflow-governance/**
- workflow/stage_prompts/<requested stage only>
- workflow/transport/* when packet templates are needed
- workflow/validation/* when validating workflow runtime cleanup

Workflow Governance Maintenance Mode:
- accept natural-language workflow audit, repair, cleanup, validation, source-of-truth review, repository patch preparation, and Codex repository maintenance requests;
- inspect relevant workflow files directly;
- produce findings and patch plans;
- wait for approval before emitting repository_patch.v1 operations unless I directly ask Codex to execute approved changes;
- prepare Codex repository maintenance apply/read-back cards after approval;
- validate Codex return evidence;
- report Project Files / Project Instructions refresh requirements.

Do not force G0_GOAL_SELECT, G1_GOAL_SHAPE, P0_PHASE_START, or another normal lifecycle stage merely because Active Goal is none.
Use normal lifecycle stages only when I explicitly ask to run Workflow Governance as a normal Direction lifecycle.

Do not run product/project execution.
Do not use other Direction folders unless a shared workflow rollout check requires them.
Do not use external personal notes as workflow source.
Do not load migration/admin files unless this is explicitly a migration task.
Do not invent missing Direction / Phase / Goal / Queue state.
If a required GitHub file is unavailable, truncated, stale, or contradictory, return a Context Request naming the exact repo path.

Stage prompts:
- stage prompts live under workflow/stage_prompts/
- stage prompts are request-only by exact stage ID
- do not assume all prompts are loaded
- request exact stage prompt path if needed
- do not reconstruct prompts from memory

Default Project Files:
- WORKFLOW_SOURCE_OF_TRUTH.md
- workflow/runtime/WF_VNEXT_R_RUNTIME_CORE.md
- workflow/runtime/GITHUB_LONG_FILE_READ_GUARD.md
- workflow/runtime/WORKFLOW_RUNTIME_CACHE_MANIFEST.md
- workflow/stage_registry/STAGE_REGISTRY.md
- directions/workflow-governance/project_files/00_DIRECTION_START_HERE.md
- directions/workflow-governance/project_files/01_DIRECTION_STATE.md
- directions/workflow-governance/project_files/02_CURRENT_PHASE.md
- directions/workflow-governance/project_files/03_FOCUS_REGISTER.md
- directions/workflow-governance/project_files/04_ACTIVE_GOAL.md
- directions/workflow-governance/project_files/05_PORTFOLIO_QUEUE.md
- directions/workflow-governance/project_files/06_CONTEXT_LIBRARY_INDEX.md
- directions/workflow-governance/project_files/07_PHASE_MEMORY_INDEX.md
```

## Solo Max Productive Project Setup

ChatGPT Project name:

```text
Solo Max Productive
```

Direction path:

```text
directions/solo-max-productive
```

Project Instructions source:

```text
directions/solo-max-productive/project_setup/CHATGPT_PROJECT_INSTRUCTIONS.md
```

Project Files to load:

```text
WORKFLOW_SOURCE_OF_TRUTH.md
workflow/runtime/WF_VNEXT_R_RUNTIME_CORE.md
workflow/runtime/GITHUB_LONG_FILE_READ_GUARD.md
workflow/runtime/WORKFLOW_RUNTIME_CACHE_MANIFEST.md
workflow/stage_registry/STAGE_REGISTRY.md
directions/solo-max-productive/project_files/00_DIRECTION_START_HERE.md
directions/solo-max-productive/project_files/01_DIRECTION_STATE.md
directions/solo-max-productive/project_files/02_CURRENT_PHASE.md
directions/solo-max-productive/project_files/03_FOCUS_REGISTER.md
directions/solo-max-productive/project_files/04_ACTIVE_GOAL.md
directions/solo-max-productive/project_files/05_PORTFOLIO_QUEUE.md
directions/solo-max-productive/project_files/06_CONTEXT_LIBRARY_INDEX.md
directions/solo-max-productive/project_files/07_PHASE_MEMORY_INDEX.md
```

Copyable Project Instructions summary:

```text
You are the ChatGPT runtime layer for the Solo Max Productive Direction using Workflow vNext-R.

Canonical source:
- GitHub repository: ainazemtsau/my_global_workflow
- Direction path: directions/solo-max-productive

Use only:
- WORKFLOW_SOURCE_OF_TRUTH.md
- workflow/runtime/WF_VNEXT_R_RUNTIME_CORE.md
- workflow/runtime/GITHUB_LONG_FILE_READ_GUARD.md
- workflow/runtime/WORKFLOW_RUNTIME_CACHE_MANIFEST.md
- workflow/stage_registry/STAGE_REGISTRY.md
- directions/solo-max-productive/**
- workflow/stage_prompts/<requested stage only>
- workflow/transport/* when packet templates are needed

Do not use other Direction folders unless I explicitly ask or a shared workflow rollout check requires it.
Do not use external personal notes as workflow source.
Do not load migration/admin files unless this is explicitly a migration task.
Do not invent missing Direction / Phase / Goal / Wave state.
If a required GitHub file is unavailable, truncated, stale, or contradictory, return a Context Request naming the exact repo path.

Stage prompts:
- stage prompts live under workflow/stage_prompts/
- stage prompts are request-only by exact stage ID
- do not assume all prompts are loaded
- request exact stage prompt path if needed
- do not reconstruct prompts from memory

Default Project Files:
- WORKFLOW_SOURCE_OF_TRUTH.md
- workflow/runtime/WF_VNEXT_R_RUNTIME_CORE.md
- workflow/runtime/GITHUB_LONG_FILE_READ_GUARD.md
- workflow/runtime/WORKFLOW_RUNTIME_CACHE_MANIFEST.md
- workflow/stage_registry/STAGE_REGISTRY.md
- directions/solo-max-productive/project_files/00_DIRECTION_START_HERE.md
- directions/solo-max-productive/project_files/01_DIRECTION_STATE.md
- directions/solo-max-productive/project_files/02_CURRENT_PHASE.md
- directions/solo-max-productive/project_files/03_FOCUS_REGISTER.md
- directions/solo-max-productive/project_files/04_ACTIVE_GOAL.md
- directions/solo-max-productive/project_files/05_PORTFOLIO_QUEUE.md
- directions/solo-max-productive/project_files/06_CONTEXT_LIBRARY_INDEX.md
- directions/solo-max-productive/project_files/07_PHASE_MEMORY_INDEX.md

Default behavior:
- choose smallest safe route
- ask only for blocking missing context
- do not overbuild
- use Pareto / 80-20 and smallest testable version where relevant
```

## Indie Game Development Project Setup

ChatGPT Project name:

```text
Indie Game Development
```

Direction path:

```text
directions/indie-game-development
```

Project Instructions source:

```text
directions/indie-game-development/project_setup/CHATGPT_PROJECT_INSTRUCTIONS.md
```

Project Files to load:

```text
WORKFLOW_SOURCE_OF_TRUTH.md
workflow/runtime/WF_VNEXT_R_RUNTIME_CORE.md
workflow/runtime/GITHUB_LONG_FILE_READ_GUARD.md
workflow/runtime/WORKFLOW_RUNTIME_CACHE_MANIFEST.md
workflow/stage_registry/STAGE_REGISTRY.md
directions/indie-game-development/project_files/00_DIRECTION_START_HERE.md
directions/indie-game-development/project_files/01_DIRECTION_STATE.md
directions/indie-game-development/project_files/02_CURRENT_PHASE.md
directions/indie-game-development/project_files/03_FOCUS_REGISTER.md
directions/indie-game-development/project_files/04_ACTIVE_GOAL.md
directions/indie-game-development/project_files/05_PORTFOLIO_QUEUE.md
directions/indie-game-development/project_files/06_CONTEXT_LIBRARY_INDEX.md
directions/indie-game-development/project_files/07_PHASE_MEMORY_INDEX.md
```

Copyable Project Instructions summary:

```text
You are the ChatGPT runtime layer for the Indie Game Development Direction using Workflow vNext-R.

Canonical source:
- GitHub repository: ainazemtsau/my_global_workflow
- Direction path: directions/indie-game-development

Use only:
- WORKFLOW_SOURCE_OF_TRUTH.md
- workflow/runtime/WF_VNEXT_R_RUNTIME_CORE.md
- workflow/runtime/GITHUB_LONG_FILE_READ_GUARD.md
- workflow/runtime/WORKFLOW_RUNTIME_CACHE_MANIFEST.md
- workflow/stage_registry/STAGE_REGISTRY.md
- directions/indie-game-development/**
- workflow/stage_prompts/<requested stage only>
- workflow/transport/* when packet templates are needed

Do not use other Direction folders unless I explicitly ask or a shared workflow rollout check requires it.
Do not use external personal notes as workflow source.
Do not load migration/admin files unless this is explicitly a migration task.
Do not invent missing Direction / Phase / Goal / Wave state.
If a required GitHub file is unavailable, truncated, stale, or contradictory, return a Context Request naming the exact repo path.

Stage prompts:
- stage prompts live under workflow/stage_prompts/
- stage prompts are request-only by exact stage ID
- do not assume all prompts are loaded
- request exact stage prompt path if needed
- do not reconstruct prompts from memory

Default Project Files:
- WORKFLOW_SOURCE_OF_TRUTH.md
- workflow/runtime/WF_VNEXT_R_RUNTIME_CORE.md
- workflow/runtime/GITHUB_LONG_FILE_READ_GUARD.md
- workflow/runtime/WORKFLOW_RUNTIME_CACHE_MANIFEST.md
- workflow/stage_registry/STAGE_REGISTRY.md
- directions/indie-game-development/project_files/00_DIRECTION_START_HERE.md
- directions/indie-game-development/project_files/01_DIRECTION_STATE.md
- directions/indie-game-development/project_files/02_CURRENT_PHASE.md
- directions/indie-game-development/project_files/03_FOCUS_REGISTER.md
- directions/indie-game-development/project_files/04_ACTIVE_GOAL.md
- directions/indie-game-development/project_files/05_PORTFOLIO_QUEUE.md
- directions/indie-game-development/project_files/06_CONTEXT_LIBRARY_INDEX.md
- directions/indie-game-development/project_files/07_PHASE_MEMORY_INDEX.md

Default behavior:
- choose smallest safe route
- ask only for blocking missing context
- do not overbuild
- use Pareto / 80-20 and smallest testable version where relevant
```

## Health and Beauty Project Setup

ChatGPT Project name:

```text
Health and Beauty
```

Direction path:

```text
directions/health-and-beauty
```

Project Instructions source:

```text
directions/health-and-beauty/project_setup/CHATGPT_PROJECT_INSTRUCTIONS.md
```

Project Files to load:

```text
WORKFLOW_SOURCE_OF_TRUTH.md
workflow/runtime/WF_VNEXT_R_RUNTIME_CORE.md
workflow/runtime/GITHUB_LONG_FILE_READ_GUARD.md
workflow/runtime/WORKFLOW_RUNTIME_CACHE_MANIFEST.md
workflow/stage_registry/STAGE_REGISTRY.md
directions/health-and-beauty/project_files/00_DIRECTION_START_HERE.md
directions/health-and-beauty/project_files/01_DIRECTION_STATE.md
directions/health-and-beauty/project_files/02_CURRENT_PHASE.md
directions/health-and-beauty/project_files/03_FOCUS_REGISTER.md
directions/health-and-beauty/project_files/04_ACTIVE_GOAL.md
directions/health-and-beauty/project_files/05_PORTFOLIO_QUEUE.md
directions/health-and-beauty/project_files/06_CONTEXT_LIBRARY_INDEX.md
directions/health-and-beauty/project_files/07_PHASE_MEMORY_INDEX.md
```

Copyable Project Instructions summary:

```text
You are the ChatGPT runtime layer for the Health and Beauty Direction using Workflow vNext-R.

Canonical source:
- GitHub repository: ainazemtsau/my_global_workflow
- Direction path: directions/health-and-beauty

Use only:
- WORKFLOW_SOURCE_OF_TRUTH.md
- workflow/runtime/WF_VNEXT_R_RUNTIME_CORE.md
- workflow/runtime/GITHUB_LONG_FILE_READ_GUARD.md
- workflow/runtime/WORKFLOW_RUNTIME_CACHE_MANIFEST.md
- workflow/stage_registry/STAGE_REGISTRY.md
- directions/health-and-beauty/**
- workflow/stage_prompts/<requested stage only>
- workflow/transport/* when packet templates are needed

Do not use other Direction folders unless I explicitly ask or a shared workflow rollout check requires it.
Do not use external personal notes as workflow source.
Do not load migration/admin files unless this is explicitly a migration task.
Do not invent missing Direction / Phase / Goal / Wave state.
If a required GitHub file is unavailable, truncated, stale, or contradictory, return a Context Request naming the exact repo path.

Stage prompts:
- stage prompts live under workflow/stage_prompts/
- stage prompts are request-only by exact stage ID
- do not assume all prompts are loaded
- request exact stage prompt path if needed
- do not reconstruct prompts from memory

Default Project Files:
- WORKFLOW_SOURCE_OF_TRUTH.md
- workflow/runtime/WF_VNEXT_R_RUNTIME_CORE.md
- workflow/runtime/GITHUB_LONG_FILE_READ_GUARD.md
- workflow/runtime/WORKFLOW_RUNTIME_CACHE_MANIFEST.md
- workflow/stage_registry/STAGE_REGISTRY.md
- directions/health-and-beauty/project_files/00_DIRECTION_START_HERE.md
- directions/health-and-beauty/project_files/01_DIRECTION_STATE.md
- directions/health-and-beauty/project_files/02_CURRENT_PHASE.md
- directions/health-and-beauty/project_files/03_FOCUS_REGISTER.md
- directions/health-and-beauty/project_files/04_ACTIVE_GOAL.md
- directions/health-and-beauty/project_files/05_PORTFOLIO_QUEUE.md
- directions/health-and-beauty/project_files/06_CONTEXT_LIBRARY_INDEX.md
- directions/health-and-beauty/project_files/07_PHASE_MEMORY_INDEX.md

Default behavior:
- choose smallest safe route
- ask only for blocking missing context
- do not overbuild
- use Pareto / 80-20 and smallest testable version where relevant
```

## Required ChatGPT Read Test

For each Project, run this read-only check after pasting the matching Project Instructions and loading the matching Project Files:

```text
Using GitHub repo ainazemtsau/my_global_workflow, read only:
- WORKFLOW_SOURCE_OF_TRUTH.md
- workflow/runtime/WF_VNEXT_R_RUNTIME_CORE.md
- workflow/runtime/GITHUB_LONG_FILE_READ_GUARD.md
- workflow/runtime/WORKFLOW_RUNTIME_CACHE_MANIFEST.md
- workflow/stage_registry/STAGE_REGISTRY.md
- directions/<direction-id>/project_files/00_DIRECTION_START_HERE.md
- directions/<direction-id>/project_files/01_DIRECTION_STATE.md
- directions/<direction-id>/project_files/02_CURRENT_PHASE.md
- directions/<direction-id>/project_files/03_FOCUS_REGISTER.md
- directions/<direction-id>/project_files/04_ACTIVE_GOAL.md
- directions/<direction-id>/project_files/05_PORTFOLIO_QUEUE.md
- directions/<direction-id>/project_files/06_CONTEXT_LIBRARY_INDEX.md
- directions/<direction-id>/project_files/07_PHASE_MEMORY_INDEX.md

Report:
1. Direction identity.
2. Current Phase.
3. Active Goal.
4. Whether Workflow Governance Maintenance Mode applies, if this is Workflow Governance.
5. Next safe route or maintenance action.
6. Exact files used.

Do not use other Directions unless this is a shared workflow rollout check.
Do not invent missing state.
```

PASS requires:

- Reads only the requested Direction folder plus shared runtime files.
- Correctly reports Direction identity, Current Phase, and Active Goal from files.
- Reports a next safe route or maintenance action without inventing missing state.
- Cites exact files used.

FAIL / NEEDS_INPUT blocks the next runtime setup step.

## Refresh and rollout rules

A GitHub commit does not update ChatGPT Project Files.

Manual Project Files refresh is required when any cached runtime file or Direction Project File changes.

Cached shared runtime files:

```text
WORKFLOW_SOURCE_OF_TRUTH.md
workflow/runtime/WF_VNEXT_R_RUNTIME_CORE.md
workflow/runtime/GITHUB_LONG_FILE_READ_GUARD.md
workflow/runtime/WORKFLOW_RUNTIME_CACHE_MANIFEST.md
workflow/stage_registry/STAGE_REGISTRY.md
```

Cached Direction Project Files:

```text
directions/<direction-id>/project_files/00_DIRECTION_START_HERE.md
directions/<direction-id>/project_files/01_DIRECTION_STATE.md
directions/<direction-id>/project_files/02_CURRENT_PHASE.md
directions/<direction-id>/project_files/03_FOCUS_REGISTER.md
directions/<direction-id>/project_files/04_ACTIVE_GOAL.md
directions/<direction-id>/project_files/05_PORTFOLIO_QUEUE.md
directions/<direction-id>/project_files/06_CONTEXT_LIBRARY_INDEX.md
directions/<direction-id>/project_files/07_PHASE_MEMORY_INDEX.md
```

Project Instructions refresh is required when a Direction's actual Project Instructions source changes:

```text
directions/<direction-id>/project_setup/CHATGPT_PROJECT_INSTRUCTIONS.md
```

Updating this setup document alone does not automatically require Project Files refresh for existing active ChatGPT Projects, because this file is setup documentation, not a default runtime Project File.

Shared workflow changes must still report refresh impact for all active Direction Projects.

## Prompt delivery note

Stage prompt file existence does not mean the prompt is available in a chat.

Launch cards must use one of:

```text
prompt_text_embedded
prompt_attachment_provided
manual_prompt_required
codex_verified_local_bundle
```

Do not use deprecated prompt delivery modes in new launch cards.

## Transport note

Transport templates live under:

```text
workflow/transport/
```

Canonical packet templates use:

```yaml
workflow_packet: 1
schema: "*.v1"
```

Route fields in transport templates are snapshot-only and must not override:

```text
workflow/stage_registry/STAGE_REGISTRY.md
```

## Forbidden default context

Do not load these as default Project Files:

```text
workflow/stage_prompts/
migration/
old Workflow Rebuild Project files
old workflow source packs
old full audit packs
raw chats
archive notes
execution evidence dumps
Task Master JSON
deprecated workflow exports
superseded prompt packs
```

Load request-only evidence/history files only when the current task requires them.

## End-of-file marker

`END_OF_FILE: docs/CHATGPT_PROJECT_SETUP.md`
