# Codex App Setup

Status: migration_in_progress

Use this file as the user-facing task template for Codex app runs against this repository.

Do not mark GitHub canonical from this setup alone. Final canonical activation is controlled by `WORKFLOW_SOURCE_OF_TRUTH.md` and Step 10.

## Default Codex Task Template

```text
Repository:
ainazemtsau/my_global_workflow

Target Direction:
directions/<direction-id>

Allowed scope:
- directions/<direction-id>/**
- workflow/runtime/WF_VNEXT_R_RUNTIME_CORE.md read-only unless task explicitly says runtime update
- workflow/stage_registry/STAGE_REGISTRY.md read-only unless task explicitly says registry update
- workflow/stage_prompts/<specific stage> only if task targets that stage
- workflow/transport/* only when packet/schema work is required

Forbidden scope:
- directions/<other-direction>/**
- unrelated stage prompts
- unrelated workflow/codex contracts
- docs/MIGRATION_FROM_TRILIUM.md unless the task is a migration/admin task
- WORKFLOW_SOURCE_OF_TRUTH.md unless the task is a source-of-truth/admin step

Task:
[describe exact task]

Mode:
PREVIEW_DIFF first.
Do not commit/apply until I approve.

Return:
- files read
- files changed
- diff summary
- validation performed
- blockers or missing inputs
- next user action
```

## Direction IDs

- `solo-max-productive`
- `indie-game-development`
- `health-and-beauty`

## Required Codex Behavior

Codex must:

- read `AGENTS.md` at repo root before material edits;
- read the target Direction `AGENTS.md` before Direction edits;
- keep edits inside the allowed scope;
- use GitHub repository markdown files as the workflow state substrate after Step 10;
- use `Repository Patch` / `repository_patch.v1` language for workflow writes;
- return exact changed paths;
- include validation evidence;
- stop with `NEEDS_INPUT` when required state, credentials, paths, or permissions are missing;
- avoid cross-Direction changes unless the task explicitly names them.

Codex must not:

- invent Direction, Phase, Goal, Queue, Context Index, Wave, execution, or project data;
- write before preview when the task requests preview-first;
- commit or push unless explicitly authorized;
- modify other Direction folders;
- modify runtime prompts unless the task targets a prompt;
- use migration/admin notes as runtime context;
- delete files without explicit human approval.

## Preview Validation Checklist

Before apply/commit, verify:

- scope is correct;
- no unrelated Direction files changed;
- no runtime source-of-truth flip occurred unless Step 10 task explicitly asks;
- no invented Direction state appears;
- `repository_patch.v1` terminology is preserved;
- validation command or file-read verification is listed;
- user approval is still required before apply/commit.

## Apply Return Checklist

After approved apply/commit, return:

```yaml
codex_app_result:
  status: DONE | NEEDS_INPUT | STUCK
  repository: ainazemtsau/my_global_workflow
  target_direction:
  files_read:
  files_changed:
  commit_sha:
  validation:
  forbidden_scope_check:
  unresolved_risks:
  next_user_action:
```

If no commit was authorized, set `commit_sha: none`.
