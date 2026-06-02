# Codex Result Verification Procedure

status: active_procedure

## Purpose

Use `codex_result_verification` to verify a Codex return before acceptance or storage update reliance.

## Required verification

Verify:

```text
branch
commit_sha
changed_files
allowed_paths
forbidden_paths
validation_output
EOF markers
payload character counts when Project Instructions sources changed
project refresh categories
push status
residual risks
```

## Rules

- No validation means no done claim.
- Verification is candidate evidence, not acceptance by itself.
- Forbidden path changes block acceptance.
- Missing EOF markers block acceptance for markdown files that require them.
- Project Instructions source changes require measured payload character count and refresh classification.

## Required output

```text
verification_status: passed | failed | blocked
branch:
commit_sha:
changed_files:
forbidden_paths_touched:
validation_output:
payload_character_counts:
project_refresh_categories:
residual_risks:
exact_next_move:
```

END_OF_FILE: workflow_v3/procedures/CODEX_RESULT_VERIFICATION_PROCEDURE.md
