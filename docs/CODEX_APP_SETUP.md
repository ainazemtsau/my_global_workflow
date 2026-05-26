# Codex App Setup

Status: active

Use this file as the user-facing setup guide for Codex repository maintenance runs against this repository.

Canonical activation is recorded in `WORKFLOW_SOURCE_OF_TRUTH.md`.

## Active Authority

Codex must treat `workflow/**` as the active workflow authority.

Codex must not treat old vNext-R runtime, stage, transport, or Direction `project_files/00-08` files as active authority.

The active `workflow/` directory is the current Workflow OS namespace. Use the legacy branch/tag if old vNext-R historical copies are needed.

Old files may be inspected as legacy evidence only when the task explicitly asks for that, and imported only through the Legacy Import Receipt process.

## Repository Maintenance Boundary

Codex repository maintenance instructions should follow workflow transport rules when provided.

Codex Commit Handoff Cards must be self-contained. A commit handoff must include repository, worktree, branch, mode, allowed paths, forbidden paths, validation, commit behavior, push behavior, and separated project refresh requirements when ChatGPT Project surfaces are affected.

Product/project execution is separate from repository maintenance and must not be inferred from a maintenance request.

Do not run product/project execution unless an explicit admitted task authorizes it.

## Execution Harness Boundary

The Execution Harness is a request-only capability area.

Execution is not a semantic primitive.

Codex is not the execution system.

CodexRun is a gated Operator family inside execution.

Product repo execution setup is separate and target-repo-local. Do not create product `.execution/**` files inside this workflow repository.

## Default Codex Task Template

```text
Repository:
ainazemtsau/my_global_workflow

Target branch:
main or named branch

Mode:
repository maintenance

Allowed paths:
[exact paths]

Forbidden paths:
[exact paths]

Task:
[describe exact maintenance task]

Return:
- files changed
- validation results
- commit SHA if committed
- push result if pushed
- separated project refresh requirements
- risks or blockers
```

## Required Codex Behavior

Codex must:

- read `AGENTS.md` at repo root before material edits;
- keep edits inside the allowed scope;
- use GitHub repository markdown files as the storage substrate;
- preserve the workflow rule: Receipt -> Verify -> Commit -> Ledger update;
- return exact changed paths;
- include validation evidence;
- report changed files, validation, commit SHA, push result, and separated project refresh requirements when relevant;
- stop with `NEEDS_INPUT` or `STUCK` when required state, credentials, paths, permissions, or conflict resolution authority is missing;
- avoid cross-Direction changes unless the task explicitly names them.

Codex must not:

- invent Direction proof state;
- treat old Direction project files as accepted state;
- use old workflow runtime/stage files as active process authority;
- commit or push unless explicitly authorized;
- delete files without explicit human approval;
- infer product/project execution from repository maintenance.

## Validation Checklist

Before commit/push, verify:

- scope is correct;
- no forbidden paths changed;
- no unrelated Direction files changed;
- no old workflow authority was reintroduced;
- no Direction proof state was invented;
- validation command or read-back evidence is listed;
- separated project refresh impact is reported.

## Return Checklist

After authorized commit/push, return:

```yaml
codex_app_result:
  status: DONE | NEEDS_INPUT | STUCK
  repository: ainazemtsau/my_global_workflow
  files_changed:
  validation:
  commit_sha:
  push_result:
  project_instruction_ui_update_required:
  project_instruction_ui_payload_char_counts:
  project_sources_files_refresh_required:
  request_only_sources_refresh_required:
  do_not_upload_as_project_file:
  forbidden_scope_check:
  unresolved_risks:
  next_user_action:
```

END_OF_FILE: docs/CODEX_APP_SETUP.md
