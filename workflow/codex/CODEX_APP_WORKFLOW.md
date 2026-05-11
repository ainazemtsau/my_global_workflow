# Codex App Workflow

Status: migration_in_progress

This contract defines how Codex app tasks should operate against the GitHub repository workflow layer.

## Purpose

Codex app work uses this repository as the working substrate for workflow files, Direction project files, stage prompts, transport contracts, and Codex support contracts.

Codex must default to preview-first work. Apply, commit, or push only after explicit user approval.

## Required Task Fields

Every Codex app task should identify:

```yaml
repository: ainazemtsau/my_global_workflow
target_direction:
allowed_scope:
forbidden_scope:
task:
mode: PREVIEW_DIFF first
approval_required_before_apply: true
```

## Scope Rules

Allowed Direction scope:

```yaml
allowed_scope:
  - directions/<direction-id>/**
  - workflow/runtime/WF_VNEXT_R_RUNTIME_CORE.md read-only unless task explicitly says runtime update
  - workflow/stage_registry/STAGE_REGISTRY.md read-only unless task explicitly says registry update
  - workflow/stage_prompts/<specific stage> only if task targets that stage
  - workflow/transport/* only when packet/schema work is required
```

Forbidden default scope:

```yaml
forbidden_scope:
  - directions/<other-direction>/**
  - unrelated stage prompts
  - unrelated workflow/codex contracts
  - migration/admin docs unless task is migration/admin
  - WORKFLOW_SOURCE_OF_TRUTH.md unless task is source-of-truth/admin
```

## Preview Result

Preview results must include:

```yaml
codex_preview_result:
  status: PASS | NEEDS_INPUT | FAIL | STOP
  repository: ainazemtsau/my_global_workflow
  target_direction:
  files_read:
  files_to_change:
  diff_summary:
  validation_plan:
  missing_inputs:
  forbidden_scope_check:
  apply_command_or_next_user_action:
```

`PASS` permits an approved apply. `NEEDS_INPUT`, `FAIL`, or `STOP` blocks apply.

## Apply Result

Apply results must include:

```yaml
codex_app_result:
  status: DONE | NEEDS_INPUT | STUCK
  repository: ainazemtsau/my_global_workflow
  target_direction:
  files_read:
  files_changed:
  diff_summary:
  validation_performed:
  commit_sha:
  forbidden_scope_check:
  unresolved_risks:
  next_user_action:
```

Use `commit_sha: none` if the task was applied locally but not committed by explicit instruction.

## Repository Patch Compatibility

Workflow persistence language must use:

- `Repository Patch`
- `repository_patch.v1`
- `Changed Files / Context Refresh List`
- file read-back / diff verification / commit verification

Do not reintroduce note-database write terminology into runtime workflow files.

## Stop Conditions

Return `NEEDS_INPUT` before material execution when:

- target Direction is missing;
- required Direction project files are missing;
- required runtime or stage prompt file is missing;
- repository write permission is missing;
- user approval is required but absent;
- scope crosses Direction boundaries without explicit authorization;
- validation command or file verification cannot be determined.

Return `STUCK` only after work begins and bounded repair cannot safely complete.
