# AGENTS.md - Project `Питание` Codex instructions

Status: active

## Scope

These instructions apply only to the nutrition project:

```text
directions/health-and-beauty/projects/nutrition/**
```

This is not a Direction-wide instruction file.

Do not apply these rules to:

```text
directions/health-and-beauty/project_files/**
directions/health-and-beauty/phases/**
workflow/**
directions/* except directions/health-and-beauty/projects/nutrition/**
```

unless the user explicitly asks for workflow or Direction lifecycle repository maintenance.

## Role

Codex is the save-only repository writer for ChatGPT Project `Питание`.

ChatGPT Project `Питание` may produce save packets such as:

```text
nutrition_state_update_packet
global_nutrition_plan
weekly_plan
active_week_menu
week_tracking_report
week_review
next_week_inputs
```

These packets are proposed durable state updates. They do not save themselves.

Codex must apply approved packets to GitHub files, verify the result, commit, push, and report which ChatGPT Project Files must be refreshed manually.

## Preflight

Before editing:

```text
git fetch origin
git checkout codex/direction-health-and-beauty
git rebase origin/main
git status --short
```

If the worktree is dirty before edits, report STUCK unless the dirty files are clearly part of the current requested save operation.

## Allowed files for normal nutrition save operations

Normal save operations may modify only:

```text
directions/health-and-beauty/projects/nutrition/state/**
directions/health-and-beauty/projects/nutrition/research/**
directions/health-and-beauty/projects/nutrition/weeks/**
```

Do not modify:

```text
workflow/**
directions/health-and-beauty/project_files/**
directions/health-and-beauty/phases/**
directions/health-and-beauty/project_setup/**
directions/* except directions/health-and-beauty/projects/nutrition/**
```

unless explicitly requested.

## Global Strategy targets

Nutrition save operations must understand these Global Strategy targets:

- `state/USER_PROFILE_AND_CONSTRAINTS.yml`
- `research/DEEP_RESEARCH_REQUEST.md`
- `research/DEEP_RESEARCH_RESULT.md`
- `research/DEEP_RESEARCH_SYNTHESIS.md`
- `state/GLOBAL_NUTRITION_PLAN.md`

Do not apply nutrition save packets to the repository root, Direction-level project files, sibling Directions, or `workflow/**`.

Do not save generic nutrition plans.

For Global Strategy saves, validate that profile, research request, research result, research synthesis, and final plan remain separated.

## Packet routing

If a packet contains `target_files`, use those paths as the primary target list.

If the packet contains `global_nutrition_plan`, update:

```text
state/GLOBAL_NUTRITION_PLAN.md
```

If the packet contains user profile fields such as age, sex, height, weight, constraints, allergies, schedule, equipment, training context, or risk notes, update:

```text
state/USER_PROFILE_AND_CONSTRAINTS.yml
```

Treat `state/USER_PROFILE_AND_CONSTRAINTS.md` as legacy compatibility input only, not as the canonical Global Strategy save target.

If the packet contains Deep Research request, result, or synthesis content, update the matching target:

```text
research/DEEP_RESEARCH_REQUEST.md
research/DEEP_RESEARCH_RESULT.md
research/DEEP_RESEARCH_SYNTHESIS.md
```

If the packet contains nutrition history, update:

```text
state/NUTRITION_HISTORY.md
```

If the packet contains progress metrics, update:

```text
state/PROGRESS_METRICS.md
```

If the packet contains weekly planning state, update as appropriate:

```text
weeks/ACTIVE_WEEK_POINTER.md
weeks/current/WEEKLY_PLAN.md
weeks/current/ACTIVE_WEEK_MENU.md
weeks/current/WEEK_TRACKING_REPORT.md
weeks/current/WEEK_REVIEW.md
weeks/current/NEXT_WEEK_INPUTS.md
```

Prefer explicit packet `target_files` over inference.

## Apply rules

Read target files before editing.
Preserve existing markdown/YAML style where possible.
Do not save the packet wrapper itself unless an existing file explicitly uses that pattern.
Do not invent missing health data.
Do not turn risk notes into diagnoses.
Do not generate live diet/menu/training content while saving state.
Do not claim external writes unless files were actually changed, read back, committed, and pushed.
If the packet conflicts with existing state or target files are unclear, report STUCK.

## Validation

After editing, return:

```text
Status: DONE or STUCK

Worktree:
Branch:
Rebase result:
Changed files:
Diff summary:
Read-back anchors:
Forbidden-path check:
Commit SHA:
Push result:
Main integration:
Project Files refresh required:
  target ChatGPT Project: Питание
  files to refresh:
Blockers/warnings:
```

Required checks:

```text
git diff --stat
changed files list
read-back anchors from every changed file
confirm no workflow/** files changed
confirm no directions/health-and-beauty/project_files/** files changed
confirm no sibling Direction files changed
confirm no superseded Project Питание legacy files were reintroduced
```

For Global Strategy saves, also confirm that profile, research request, research result, research synthesis, and final plan stayed separated.

## Commit messages

Use one of:

```text
save nutrition global strategy state
save nutrition weekly plan state
save nutrition active week menu
save nutrition tracking state
save nutrition project state
```

## Project Files refresh rule

A GitHub commit does not update ChatGPT Project Files.

If any file under:

```text
state/**
research/**
weeks/**
```

changed, report the exact file names that must be manually refreshed in ChatGPT Project `Питание`.

END_OF_FILE: directions/health-and-beauty/projects/nutrition/AGENTS.md
