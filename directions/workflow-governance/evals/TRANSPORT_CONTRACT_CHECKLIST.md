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
