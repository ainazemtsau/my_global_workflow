# Transport Contract Checklist

Use this checklist to validate runtime transport contracts.

## Checklist

- `stage_launch.v1`
- `stage_result.v1`
- `context_request.v1`
- `human_decision.v1`
- `stop.v1`
- `repository_patch.v1`
- `execution_log_entry.v1`
- `documentation_maintenance_gate`
- `changed_files_context_refresh`
- `codex_repository_maintenance_apply.v1`

## Rules

- Packet contracts come from `workflow/runtime/WF_VNEXT_R_RUNTIME_CORE.md`.
- Do not invent local packet schemas.
- Findings must be recorded in `FINDING_REGISTER.md`.

## GitHub file-read verification checks

For any workflow output that depends on a GitHub repository file read, check:

- no `truncated due to tool response token budget` marker is present;
- no `Full entry omitted because the tool response token budget was exhausted` marker is present;
- compact search result was not treated as full file content;
- expected tail anchor or end-of-file evidence is present when required;
- exact stage prompt reads are full before stage execution;
- long runtime files required in every chat are available through Project Files runtime cache or verified full GitHub read;
- if full-file availability cannot be verified, the output returns Context Request instead of continuing material work.

A partial GitHub read is a transport failure, not acceptable runtime context.
