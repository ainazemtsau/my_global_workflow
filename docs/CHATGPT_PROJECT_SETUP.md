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
  last_updated: "2026-05-18"
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
Objective architecture model: workflow/runtime/OBJECTIVE_ARCHITECTURE_MODEL.md
Context acquisition policy: workflow/runtime/CONTEXT_ACQUISITION_POLICY.md
GitHub long-file read guard: workflow/runtime/GITHUB_LONG_FILE_READ_GUARD.md
Runtime cache manifest: workflow/runtime/WORKFLOW_RUNTIME_CACHE_MANIFEST.md
Stage registry: workflow/stage_registry/STAGE_REGISTRY.md
Stage prompts: workflow/stage_prompts/<requested stage only>
Transport templates: workflow/transport/* when packet templates are needed
```

GitHub repository files remain the source of truth.

ChatGPT Project Files are runtime cache, not source of truth. They must be manually refreshed when Codex changes cached files.

If a GitHub read is truncated, omitted, lacks tail verification, or cannot prove full-file availability, do not treat that read as source authority. Return Context Request naming the exact path.

GitHub connector/tool should be enabled and authorized for every active Direction Project when possible. If it is not exposed in a run, Context Request `acquisition_audit` must state `github_connector.available: false` / `not_exposed`.

Do not treat "not uploaded as Project File/attachment" as missing context until `workflow/runtime/CONTEXT_ACQUISITION_POLICY.md` has been applied.

Stage prompts are request-only by exact stage ID. Do not bulk-load all stage prompts. Do not reconstruct missing prompts from memory.

Do not invent Direction, Direction Map, Phase, Goal, Portfolio Queue, Context Loading Index, Wave, execution, or project state.

Do not use external personal notes as workflow source.

Do not use `migration/` or migration/admin docs as runtime context unless the task is explicitly a migration/admin task.

Shared workflow changes must be evaluated across all active Direction Projects, not only Workflow Governance.

## User-guided external setup and UI operation

When a setup or maintenance task requires the user to operate ChatGPT Project UI, a website, admin console, local program, setup wizard, Unity, Blender, or another external interface, and ChatGPT/Codex do not have a verified direct tool binding, use `U1_USER_GUIDED_EXECUTION`.

U1 is the default guided mode for:

- creating or configuring a ChatGPT Project manually;
- uploading or refreshing Project Files;
- copying Project Instructions into the ChatGPT UI;
- checking visible setup state;
- installing/configuring external tools when the user must operate the UI;
- Unity/Blender/editor tasks where no verified MCP/tool binding exists.

U1 should guide one visible step at a time for novice or unknown-skill users, request screenshots or exact error text when screen state differs, and stop before irreversible, permission, security, privacy, payment, or secret-related actions.

Do not use F0_FAST_DIRECT for human-operated external UI tasks. F0 is for small direct execution with explicit artifacts, target paths, and validation anchors. Use E1 to prepare the execution envelope, then U1 for guided external operation when needed.

## Required shared runtime Project Files for every active Direction

Manually load these shared runtime cache files into every active Direction ChatGPT Project:

```text
WORKFLOW_SOURCE_OF_TRUTH.md
workflow/runtime/WF_VNEXT_R_RUNTIME_CORE.md
workflow/runtime/OBJECTIVE_ARCHITECTURE_MODEL.md
workflow/runtime/CONTEXT_ACQUISITION_POLICY.md
workflow/runtime/GITHUB_LONG_FILE_READ_GUARD.md
workflow/runtime/WORKFLOW_RUNTIME_CACHE_MANIFEST.md
workflow/stage_registry/STAGE_REGISTRY.md
```

Also manually load that Direction's own Project Files `00-08` from:

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
08_DIRECTION_MAP.md
```

Do not upload stage prompts as default Project Files.

Do not upload old rebuild Project Files, migration/admin notes, raw chats, archive notes, or execution evidence dumps as default Project Files.

`08_DIRECTION_MAP.md` is strategic routing context, not a replacement for Phase or Goal state. If it is uninitialized or marked `needs_m0_review` and a material strategic Phase/Goal choice is needed, run `M0_DIRECTION_MAP`.

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
workflow/runtime/OBJECTIVE_ARCHITECTURE_MODEL.md
workflow/runtime/CONTEXT_ACQUISITION_POLICY.md
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
directions/workflow-governance/project_files/08_DIRECTION_MAP.md
```

Project Instructions handling:

```text
Paste the compact bootstrap instructions from the Project Instructions source above.
Do not paste expanded runtime cache lists into Project Instructions.
Full runtime context lives in Project Files defined by workflow/runtime/WORKFLOW_RUNTIME_CACHE_MANIFEST.md and directions/workflow-governance/project_files/06_CONTEXT_LIBRARY_INDEX.md.
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
workflow/runtime/OBJECTIVE_ARCHITECTURE_MODEL.md
workflow/runtime/CONTEXT_ACQUISITION_POLICY.md
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
directions/solo-max-productive/project_files/08_DIRECTION_MAP.md
```

Project Instructions handling:

```text
Paste the compact bootstrap instructions from the Project Instructions source above.
Do not paste expanded runtime cache lists into Project Instructions.
Full runtime context lives in Project Files defined by workflow/runtime/WORKFLOW_RUNTIME_CACHE_MANIFEST.md and directions/solo-max-productive/project_files/06_CONTEXT_LIBRARY_INDEX.md.
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
workflow/runtime/OBJECTIVE_ARCHITECTURE_MODEL.md
workflow/runtime/CONTEXT_ACQUISITION_POLICY.md
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
directions/indie-game-development/project_files/08_DIRECTION_MAP.md
```

Project Instructions handling:

```text
Paste the compact bootstrap instructions from the Project Instructions source above.
Do not paste expanded runtime cache lists into Project Instructions.
Full runtime context lives in Project Files defined by workflow/runtime/WORKFLOW_RUNTIME_CACHE_MANIFEST.md and directions/indie-game-development/project_files/06_CONTEXT_LIBRARY_INDEX.md.
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
workflow/runtime/OBJECTIVE_ARCHITECTURE_MODEL.md
workflow/runtime/CONTEXT_ACQUISITION_POLICY.md
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
directions/health-and-beauty/project_files/08_DIRECTION_MAP.md
```

Project Instructions handling:

```text
Paste the compact bootstrap instructions from the Project Instructions source above.
Do not paste expanded runtime cache lists into Project Instructions.
Full runtime context lives in Project Files defined by workflow/runtime/WORKFLOW_RUNTIME_CACHE_MANIFEST.md and directions/health-and-beauty/project_files/06_CONTEXT_LIBRARY_INDEX.md.
```

## Required ChatGPT Read Test

For each Project, run this read-only check after pasting the matching Project Instructions and loading the matching Project Files:

```text
Using GitHub repo ainazemtsau/my_global_workflow, read only:
- WORKFLOW_SOURCE_OF_TRUTH.md
- workflow/runtime/WF_VNEXT_R_RUNTIME_CORE.md
- workflow/runtime/OBJECTIVE_ARCHITECTURE_MODEL.md
- workflow/runtime/CONTEXT_ACQUISITION_POLICY.md
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
- directions/<direction-id>/project_files/08_DIRECTION_MAP.md

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
workflow/runtime/OBJECTIVE_ARCHITECTURE_MODEL.md
workflow/runtime/CONTEXT_ACQUISITION_POLICY.md
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
directions/<direction-id>/project_files/08_DIRECTION_MAP.md
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

## Direction worktree repository maintenance setup

Repository maintenance uses a clean main integration worktree plus one worktree per active Direction.

Main integration worktree:

```text
C:\my_global_workflow
branch: main
role: clean integration worktree
```

Direction worktrees:

```text
Workflow Governance:
  C:\my_global_workflow_worktrees\workflow-governance
  codex/direction-workflow-governance

Solo Max Productive:
  C:\my_global_workflow_worktrees\solo-max-productive
  codex/direction-solo-max-productive

Indie Game Development:
  C:\my_global_workflow_worktrees\indie-game-development
  codex/direction-indie-game-development

Health and Beauty:
  C:\my_global_workflow_worktrees\health-and-beauty
  codex/direction-health-and-beauty
```

Direction-specific work happens in the matching worktree/branch.

Before work:

```text
git fetch origin
git rebase origin/main
```

After work:

```text
git status
git add <approved files>
git commit -m "<approved summary>"
git push
```

Then merge or PR the Direction branch into `main` from `C:\my_global_workflow`, or return explicit unmerged reason with conflict evidence.

Do not edit sibling Directions from a Direction worktree unless the approved task explicitly requires it.

## End-of-file marker

`END_OF_FILE: docs/CHATGPT_PROJECT_SETUP.md`
