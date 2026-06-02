# Codex Handoff Procedure

status: active_procedure

## Purpose

Use `codex_handoff` to create a self-contained Codex package for bounded repository maintenance or implementation.

## Required package fields

```text
repository:
base_ref:
target_branch_or_branch_policy:
purpose:
goal:
source_files_to_read:
allowed_paths:
forbidden_paths:
required_changes:
validation:
stop_conditions:
commit_push_instructions:
project_refresh_requirements:
requested_return_fields:
```

## Rules

- Package must identify exact source reads and path boundaries.
- Package must include validation and stop conditions.
- Package must state whether commit and push are requested.
- Package must state Project refresh reporting requirements when changed files affect ChatGPT Projects.
- Codex result is candidate evidence until verification and acceptance.

## Forbidden use

- authorize product execution by implication;
- omit forbidden paths;
- omit validation;
- permit Codex to decide acceptance.

END_OF_FILE: workflow_v3/procedures/CODEX_HANDOFF_PROCEDURE.md
